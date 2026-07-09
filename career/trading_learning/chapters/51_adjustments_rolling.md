# Chapter 51: Adjustments & Rolling — Defending a Trade

Imagine you're playing a hand of cards and the table turns against you. You have three choices: throw in more chips to defend the hand, change your bet to a different shape, or fold and walk away with a small, known loss. Adjusting an options position is exactly this moment of decision. The market has moved against your trade, the position is bleeding, and you must choose: do I *defend* it — reshape it to give it more room, more time, or more credit — or do I simply *cut* it and take the planned loss?

This chapter is about that fork in the road. "Adjusting" and "rolling" are the professional's toolkit for nursing a position back toward health when the market drifts the wrong way — moving strikes, moving expiries, capping a runaway risk. But there is a darker side that ruins more accounts than any single bad trade: the temptation to *keep* adjusting a position whose underlying thesis was simply wrong. The single most important sentence in this chapter is one you already know from everyday life — **don't throw good money after bad.** A great adjustment defends a trade that still makes sense. A bad adjustment is a refusal to admit you were wrong, dressed up as a strategy.

## Core concepts

### What "adjusting" actually means

An **adjustment** is any change you make to an open position *after* you've entered it, in response to how the market has moved. You are not closing the trade and you are not opening a fresh, unrelated one — you are *modifying* what you already hold by adding, removing, or replacing legs. Every adjustment does one of a small number of things:

- **Gives the trade more room** — moves a threatened strike further from the danger.
- **Gives the trade more time** — pushes the expiry out so the thesis has longer to play out.
- **Collects more credit** — brings in extra premium to widen your breakeven and offset losses building elsewhere.
- **Caps a runaway risk** — converts an open-ended loss into a defined, bounded one.

Notice that the first three *defend* a position you still believe in, while the fourth is about *damage control* on a position that has already gone wrong. Knowing which job you're doing — defending a live thesis versus limiting a dead one — is the whole game.

### Rolling: moving in time and/or strike

**Rolling** is the most common adjustment, and it means closing your existing option (or spread) and simultaneously opening a similar one at a **different strike, a different expiry, or both.** Think of it as picking up your position and setting it down somewhere safer on the board.

There are three flavours:

1. **Rolling out (in time).** You close the near-expiry option and re-sell the same strike in a *later* expiry — say, this week's Nifty into next week's. You're buying time for your view to come good. Because a longer-dated option carries more time value, rolling out usually brings in **extra credit** (for a short option) — the market pays you to extend the deadline.

2. **Rolling up or down (in strike).** You move the strike to a safer level — *up* if you're defending a short call that's being threatened by a rally, *down* if you're defending a short put under a falling market. You're giving the position more distance from the spot.

3. **Rolling out *and* up/down (the diagonal roll).** The workhorse move: go to a later expiry *and* a safer strike at the same time. The later expiry's fatter premium often funds the move to the safer strike, sometimes even for a net credit, so you defend the position without paying out of pocket.

The mechanical rule for a short option: `Roll = buy back the current option + sell the new one`. The net of those two prices is either a **credit** (money in — good, you got paid to roll) or a **debit** (money out — you paid to roll, which deepens your risk and should make you pause).

### The golden rule: roll for a credit, never pay to dig

A roll that brings in a net credit *improves* your position — it widens your breakeven and lowers your cost basis. A roll that costs you a debit *worsens* it — you're putting more capital at risk to defend a trade that's already losing. As a discipline, professional sellers strongly prefer to **roll only when they can do so for a net credit.** If defending the position requires paying a debit, that's often the market telling you the move is real and you should consider cutting instead. Paying to roll a losing directional bet again and again is the textbook way to turn a small, survivable loss into an account-ending one.

### Converting a naked option into a spread

A second classic adjustment is **capping risk by adding a long leg.** Suppose you sold a naked (unhedged) Nifty call to collect premium, and the market starts rallying toward your strike. A naked short call has *theoretically unlimited* loss — the higher Nifty goes, the more you lose, with no ceiling. The defensive move is to **buy a further-OTM call**, converting your naked short call into a **bear call spread** (a defined-risk credit spread).

What this does:

- Your **maximum loss becomes capped** at the distance between the two strikes minus the credit, instead of infinity.
- Your **margin (SPAN) usually drops sharply**, because the exchange now sees a hedged position and only charges for the bounded risk — freeing up capital.
- The cost: you pay a debit for the long call (reducing your net credit), and you've accepted that the trade is in trouble.

This is a genuinely good adjustment because it changes the *nature* of the risk from unbounded to bounded. You're not pretending the trade is fine; you're making sure that if it gets worse, it can only get so much worse.

### Defending an iron condor or strangle

The iron condor (Chapter 43) and short strangle (Chapter 41) are two-sided, range-bound trades, and they offer the most-used adjustment in Indian retail trading: **rolling the untested side.**

Here's the intuition. A condor has a call spread above the market and a put spread below it. When Nifty rallies and threatens your **short call** (the call side is now "tested"), the **put side has, by then, decayed almost to nothing** — it's done its job and there's barely any premium left in it. You can:

- **Roll the untested put spread up** — close the now-cheap put spread and re-sell it at higher strikes, closer to the new spot. Because you're selling richer (closer-to-the-money) options, this **collects fresh credit.** That new credit widens your overall breakeven on the threatened call side and re-centres the whole position around the new price.

The trade-off is honest: you're *narrowing the lane on the safe side* to defend the dangerous side. You've taken on a bit more risk (the put side is now closer to spot) in exchange for more cushion where you actually need it. If the market reverses, you're now exposed on the side you just moved in. Symmetrically, in a falling market you roll the untested *call* spread *down*.

A third option is **rolling the tested short strike further away** — buying back the threatened short call and re-selling a higher-strike call. This buys distance, but on a short-dated option it usually costs a *debit* (the closer option you're buying back is worth more than the farther one you're selling), which violates the credit rule. It's generally weaker than rolling the untested side, and on a strong trend it just postpones the pain.

### How adjustments change your Greeks, max loss, and breakevens

Every adjustment rewrites the trade's risk profile. You must re-derive the numbers — the old ones no longer apply.

- **Rolling the untested side in** *adds* directional and volatility exposure on that side. Your net delta shifts, your short vega grows (more premium sold = more sensitivity to a vol spike), and your **breakeven on the defended side widens** by the extra credit collected. But your breakeven on the rolled side moves *closer* to spot — less room there now.
- **Rolling out in time** typically *reduces* theta per day (longer-dated options decay slower) and *increases* vega (more time = more volatility sensitivity). You've traded faster decay for more breathing room.
- **Converting naked to a spread** caps max loss at a known number and dramatically cuts gamma/vega tail risk, at the price of a smaller net credit (lower max profit).
- **Breakevens always move.** Any credit collected pushes the breakeven outward (good); any debit paid pulls it inward (bad). Recompute `breakeven = short strike +/- net credit` after every adjustment, using the *cumulative* credit across the original trade and all rolls.

The discipline: after any adjustment, write down the *new* max profit, *new* max loss, and *new* breakevens as if it were a fresh trade. If you can't state those three numbers, you don't understand the position you now hold.

### When to adjust vs when to cut

This is the heart of the chapter, and it's a judgement, not a formula. Adjusting is appropriate when:

- **The thesis is still intact.** You sold a range-bound condor, the market is still chopping sideways, it just drifted a bit — defend it. The reason you put the trade on is still true.
- **You can adjust for a credit**, improving rather than worsening your position.
- **The move is noise, not a regime change** — a normal wiggle within a still-valid range, not a decisive breakout.

Cutting (taking the planned, capped loss) is the right move when:

- **The thesis is broken.** You bet on a range and the market has clearly broken into a strong trend. The premise is dead; adjusting only feeds a losing view.
- **Defending requires a debit**, i.e. you'd be paying to add risk to a losing trade.
- **You've hit your pre-defined stop-loss** (e.g. loss = 1.5x to 2x the credit received). The whole point of a defined-risk trade is that the loss is *defined* — honouring the stop is what keeps it that way.

The deadliest error in all of options trading is **adjusting a fundamentally wrong thesis.** If you're short puts because you think the market won't fall, and the market is crashing, rolling those puts down again and again — each time paying a debit, each time selling more downside risk into a falling market — is not "defending," it's *averaging into a disaster.* This is precisely how option sellers blow up: a string of small, comforting wins, then one trend they refuse to accept, defended all the way down until the account is gone. The capped loss you designed at entry exists to be *taken* when the trade is wrong. Adjusting is for trades that are merely *tested*, not trades that are *broken*.

A useful self-check before any adjustment: *"If I had no position right now, would I put this adjusted trade on fresh today?"* If yes, the adjustment is sound. If no, you're rescuing your ego, not your account.

### The costs nobody includes in the fantasy

Adjustments are not free, and in India the frictions bite hard because every roll is *two* transactions (close one leg, open another), often across multiple legs.

- **Brokerage** on every leg, both the close and the open.
- **STT (Securities Transaction Tax)** — charged on the sell side of option premium, and notably at a *much higher rate on exercised/settled ITM options at expiry* on the full settlement value. A tested leg left to settle in-the-money can deliver a nasty STT surprise, so adjustments often double as STT management (close ITM legs before expiry).
- **Exchange transaction charges, GST, SEBI fees, and stamp duty** — small individually, but they stack across many legs.
- **Slippage and the bid-ask spread** — every time you cross the spread to close and re-open, you lose a little. On four-legged condors rolled repeatedly, slippage alone can eat much of the fresh credit you collected.

The lesson: an adjustment that collects "30 points of fresh credit" might net you only 18–20 points after all costs on a multi-lot, multi-leg roll. Over-adjusting — fiddling with a position five times a week — can quietly convert a winning system into a losing one through friction alone. Adjust deliberately and rarely, not reflexively.

## Worked example (₹, Nifty)

Let's walk two concrete defences: a roll of a tested short call, then a condor adjustment with full before/after numbers. Lot size assumed **75** (current Nifty lot; verify, as it changes).

### Part A — Rolling a tested short call out and up

You sold a weekly **24,200 Nifty call** for **80 points** when Nifty was at 24,000. Two days later Nifty has rallied to **24,150** — your short call is now close to the money and threatened. The 24,200 call has risen to **130 points** (you're down `130 - 80 = 50` points on a mark-to-market basis).

You decide the uptrend looks gentle and your range view may still hold into next week, so you **roll out and up**: buy back this week's 24,200 call and sell *next week's* **24,400 call**.

```
Buy back this week 24,200 call:  -130 points (cost)
Sell next week     24,400 call:  +160 points (credit, more time value)
Net roll           = 160 - 130 = +30 points CREDIT
```

**Before vs after:**

| | Before the roll | After the roll |
|---|---|---|
| Short strike | 24,200 (this week) | 24,400 (next week) |
| Premium originally collected | 80 pts | 80 + 30 = 110 pts cumulative |
| Distance from spot (24,150) | 50 pts (dangerous) | 250 pts (comfortable) |
| Breakeven | 24,200 + 80 = **24,280** | 24,400 + 110 = **24,510** |

The roll did two good things: it pushed the danger strike 200 points further away *and*, because it came in for a **net credit of 30 points**, it widened your breakeven from 24,280 to 24,510. You got paid `30 * 75 = ₹2,250` to give the trade more room and more time. **Crucially, it was a credit roll** — the market paid you to defend, which is the only kind of roll you should be doing.

**The honest caveat:** you are now short into *next* week, exposed for longer, and short vega has grown. If the rally was the start of a genuine breakout, you've merely postponed — and possibly enlarged — the loss. The correct discipline: this roll is justified *only* because your range thesis is still alive. If Nifty had instead blasted through 24,400 on heavy volume with a clear trend, the right move would have been to **take the loss**, not chase it into a third week.

### Part B — Defending an iron condor by rolling the untested side

You opened this weekly Nifty condor at spot 24,000:

| Leg | Strike | Action | Premium (pts) |
|---|---|---|---|
| Lower wing | 23,500 put | Buy | 30 |
| Short put | 23,700 put | Sell | 70 |
| Short call | 24,300 call | Sell | 75 |
| Upper wing | 24,500 call | Buy | 35 |

```
Original net credit = (70 + 75) - (30 + 35) = 145 - 65 = 80 points  -> ₹6,000
Wing width W = 200; Max loss = W - C = 200 - 80 = 120 pts -> ₹9,000
Lower breakeven = 23,700 - 80 = 23,620
Upper breakeven = 24,300 + 80 = 24,380
```

Now Nifty falls to **23,800** — the **put side is tested** (short put at 23,700 is close), while the **call side has decayed**: the 24,300/24,500 call spread, originally worth `75 - 35 = 40` points net, is now worth only about **10 points net** (calls have collapsed as the market fell).

**The adjustment: roll the untested call spread down** to re-centre and collect fresh credit. Buy back the cheap 24,300/24,500 call spread (10 pts), and sell a new **24,000/24,200 call spread** closer to the new spot for, say, **35 points net**.

```
Buy back old call spread (24,300/24,500): -10 points
Sell new call spread     (24,000/24,200): +35 points
Net adjustment credit = 35 - 10 = +25 points CREDIT  -> ₹1,875
```

**Before vs after the adjustment:**

| | Before adjustment | After adjustment |
|---|---|---|
| Call spread | 24,300 / 24,500 | 24,000 / 24,200 |
| Put spread (unchanged) | 23,700 / 23,500 | 23,700 / 23,500 |
| Cumulative credit | 80 pts (₹6,000) | 80 + 25 = 105 pts (₹7,875) |
| Lower breakeven | 23,620 | 23,700 - 105 = **23,595** (wider) |
| Upper breakeven | 24,380 | 24,200 + 105 = **24,305** (much closer) |
| Profit lane (short-to-short) | 23,700 – 24,300 (600 pts) | 23,700 – 24,000 (300 pts, narrower) |

What changed and why it matters:

- **You collected ₹1,875 of fresh credit**, raising total credit to ₹7,875. This *lowers your effective loss* if the put side is breached: new max loss on the put side = `(200 - 105) * 75 = ₹7,125`, down from ₹9,000.
- **Your lower breakeven widened** slightly (23,620 → 23,595) — you bought a little extra cushion exactly where the market is pressing.
- **But your upper breakeven crashed inward** (24,380 → 24,305) and the profit lane narrowed to 300 points. **You are now badly exposed to a reversal:** if Nifty bounces back above 24,200, the call side you just moved in gets tested. You defended the down-move by taking on up-move risk.

This is the essential trade-off of rolling the untested side, made numeric: *more cushion where it's tested, less room everywhere else.* It's a sound defence **only if your range view is intact** — if 23,800 is a normal wobble in a sideways market. If instead this is the start of a decisive sell-off, you've just sold *more* call premium into a falling market (useless) while leaving the threatened put side fundamentally exposed — and the right move was to honour your stop and **take the capped loss.**

**Costs reality check:** Part B was a two-leg roll (close two, open two = four transactions) on top of the original four. Brokerage, STT, exchange fees, GST and slippage might consume 5–8 of those 25 fresh points, so the real credit collected is closer to 17–20 points. Roll a condor three or four times in a week and friction alone can erase the entire original edge.

## Common mistakes / risk note

- **Adjusting a broken thesis.** The cardinal sin. If the market has clearly broken your view (a range trade caught in a trend), adjusting just feeds money into a losing bet. Cut it. The defined loss exists to be taken.
- **Paying a debit to roll a loser.** Rolling should bring in a credit. If defending requires paying out, the market is telling you the move is real — that's a cut signal, not a roll signal.
- **Rolling the tested side further out repeatedly.** Each roll on a strong trend collects less and risks more, sliding strikes down (or up) into the move — averaging into a disaster.
- **Forgetting to recompute the numbers.** After any adjustment you hold a *different* trade. If you can't state the new max loss, breakevens, and Greeks, you're flying blind.
- **Ignoring the friction.** Every roll is multiple legs of brokerage, STT, GST and slippage. Over-adjusting bleeds a winning system to death through costs.
- **Leaving ITM legs to settle.** Index options are European and cash-settled; a breached short leg left to expiry attracts high settlement STT on its full value. Close ITM legs before expiry.
- **Adjusting to avoid admitting a loss.** The honest self-test: *"Would I open this adjusted trade fresh today?"* If no, you're rescuing your ego, not your capital.

## Key takeaways

- **Adjusting** reshapes an open position when the market moves against it; **rolling** closes a leg and re-opens it at a different strike, expiry, or both.
- The three rolls: **out** (later expiry, more time/credit), **up or down** (safer strike, more room), and the **diagonal** (both at once — the workhorse).
- **Golden rule: roll for a net credit, never pay a debit to defend a loser.** A credit roll widens your breakeven and improves the position; a debit roll deepens your risk.
- **Convert naked shorts into spreads** to cap unbounded loss and slash SPAN margin — a genuine, structural improvement.
- For condors/strangles, **roll the untested side** toward the new spot to collect fresh credit and re-centre — but accept you're narrowing the lane on the safe side.
- Every adjustment **rewrites your Greeks, max loss, and breakevens** — recompute all three, or you don't know what you hold.
- **Adjust only a live thesis; cut a broken one.** The deadliest error is defending a fundamentally wrong view — don't throw good money after bad. And remember every roll carries real brokerage, STT, GST and slippage costs.

## Practice problems

1. **Roll direction.** You are short a Nifty 24,000 put and the market is falling toward it. To defend by rolling *down*, do you move the strike higher or lower, and would you prefer the roll to come in for a credit or a debit? Explain.

2. **Credit roll arithmetic.** You sold a weekly 52,000 Bank Nifty call for 120 points. It's now worth 200 points (threatened). You buy it back and sell next week's 52,500 call for 240 points. Compute the net roll credit/debit, your new short strike, and the change in your distance-from-strike cushion. Was this a good roll by the credit rule?

3. **Capping risk.** You are short a naked Nifty 24,500 call (collected 90 points) and the market is rallying. You buy a 24,700 call for 45 points to make it a spread. What is your new maximum loss per lot in rupees (lot 75), and roughly what else improves besides capped loss?

4. **Condor adjustment breakevens.** A Nifty condor has short put 23,800, short call 24,200, original net credit 70 points. You roll the untested call spread down and collect an extra 30 points of credit. Find the new cumulative credit and the new lower breakeven. Did the lower breakeven widen or narrow, and why does that help the tested side?

5. **Adjust or cut?** You sold a range-bound condor expecting Nifty to stay near 24,000. Nifty has just broken out to 24,600 on heavy volume after a surprise rate decision, and defending the call side would require paying a 40-point debit. What should you most likely do, and which two principles from this chapter apply?

6. **The cost trap.** A trader rolls a 4-leg condor twice in one week. Each roll involves closing 2 legs and opening 2 legs, and friction (brokerage + STT + GST + slippage) costs about 4 points per leg traded. If the two rolls collected 25 and 20 points of gross credit, what is the net credit after costs, and what is the lesson?

## Solutions

**1.** To roll a short put *down*, you move the strike to a **lower** level (e.g. 24,000 → 23,800), increasing the distance between the strike and the falling spot — more room. You should strongly prefer the roll to come in for a **credit**: a credit roll widens your breakeven and pays you to defend. On a short-dated put in a fast fall, however, rolling down often costs a *debit* (the closer put you're buying back is worth more than the farther put you're selling) — and a debit roll is a warning sign that the move is real and you may be better off cutting than paying to add downside risk into a falling market.

**2.** Net roll = `(sell new 240) - (buy back old 200) = +40 points CREDIT` → `40 * 75 = ₹3,000` received. New short strike = **52,500** (next week). Cushion: before, the 52,000 strike was being tested; after, your danger strike is 500 points higher *and* you bought another week. By the credit rule this is a **good roll** — it came in for a credit, widening your cumulative breakeven (now `52,500 + (120 + 40) = 52,660`) while pushing the strike away. The caveat: you're short for an extra week with more vega, justified only if your view that Bank Nifty won't run past 52,500 is still alive.

**3.** Converting the naked 24,500 call into a 24,500/24,700 bear call spread: net credit becomes `90 - 45 = 45` points. Maximum loss = `(width - net credit) * lot = (200 - 45) * 75 = 155 * 75 = ₹11,625` per lot — and crucially it is now **capped** instead of unlimited. Besides capping the loss, your **SPAN margin drops sharply** (the exchange now charges only for the bounded, hedged risk), freeing capital, and your tail gamma/vega risk is greatly reduced. The cost is a lower net credit (max profit falls from 90 to 45 points).

**4.** New cumulative credit = `70 + 30 = 100 points`. New lower breakeven = `short put - cumulative credit = 23,800 - 100 = 23,700`. The original lower breakeven was `23,800 - 70 = 23,730`, so it **widened** (moved down) from 23,730 to 23,700. This helps the tested side because the extra credit from rolling the untested call spread down acts as additional cushion exactly where the market is pressing — Nifty can now fall 30 points further before you reach break-even on the threatened put side. (The price paid: the upper breakeven moved sharply inward and the profit lane narrowed, so a reversal would now hurt.)

**5.** You should most likely **cut the trade and take the capped loss.** Two principles apply: first, **the thesis is broken** — you bet on a range, and a heavy-volume breakout after a surprise rate decision is a regime change, not noise, so adjusting would feed a losing view. Second, **defending requires a debit** (40 points out of pocket) — paying to add risk to a trade that's already wrong violates the credit rule. Rolling here would be throwing good money after bad; the defined loss you designed at entry exists precisely so you can take it cleanly now and move on.

**6.** Gross credit collected = `25 + 20 = 45 points`. Costs: roll one trades 4 legs and roll two trades 4 legs = 8 legs total, at 4 points each = `8 * 4 = 32 points` of friction. Net credit after costs = `45 - 32 = 13 points` → `13 * 75 = ₹975`. The lesson: friction devoured roughly **71%** of the gross credit. Multi-leg adjustments in India are expensive because every roll is several legs of brokerage, STT, GST and slippage; over-adjusting can convert a winning structure into a losing one through costs alone. Adjust deliberately and rarely — and only when the post-cost credit still meaningfully improves the position.
