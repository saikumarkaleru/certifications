# Chapter 27: Second-Order Greeks — Vanna, Volga & Charm

The first-order Greeks — delta, gamma, theta, vega, rho — tell you how an option's price reacts to a move in spot, the passage of time, a shift in volatility, or a change in rates. For a retail trader holding two lots of a weekly Nifty option, that is the whole story. But a professional managing a *book* of thousands of contracts across many strikes and expiries quickly runs into an uncomfortable truth: **the Greeks themselves move.** Your delta is not a fixed number you hedge once and forget. It drifts when spot moves (that is gamma, which you already know), but it *also* drifts when volatility changes, and it drifts purely because a day passed. Your vega is not constant either — it grows and shrinks as volatility itself travels.

This chapter is about the Greeks of the Greeks: the **second-order Greeks** that describe how your first-order risk reshapes as the market moves. Three earn real names on a trading desk — **vanna**, **volga**, and **charm** — and we will treat each with a light numeric illustration. A few more (**colour**, **speed**, **zomma**) you only need to recognise by name. The goal is not to compute these for a two-lot trade; that would be like weighing a lorry to find the dust on it. The goal is to understand *why a desk watches them*, so that when you scale up — or simply want to see how professionals keep a hedge accurate while the market heaves — you know what is going on.

## Core concepts

### Why first-order Greeks are not enough

Picture a delta hedge as balancing a ball on a table. Delta is the tilt of the table; keep it level (delta-neutral) and the ball does not roll. Gamma is the warning that the table is not really flat — it is gently curved, so as the ball moves, the tilt changes and you must keep re-levelling. That much you met in the gamma chapter.

But the table *also* tilts when **volatility** changes, even if the ball has not moved, and when **time** passes, even if nothing else changes. A professional hedge is therefore never "set and forget." It is continuous re-balancing against three forces that can each undo your neutrality: spot moving, vol moving, and the clock ticking. The second-order Greeks are the precise names for *how much* each force disturbs your delta and vega.

Here is the clean mental map. Every second-order Greek is a "rate of change of a first-order Greek with respect to something":

- **Gamma** = how delta changes when **spot** moves. (Already covered.)
- **Vanna** = how delta changes when **volatility** moves (equivalently, how vega changes when spot moves).
- **Charm** = how delta changes when **time** passes.
- **Volga** (vomma) = how vega changes when **volatility** moves.

Notice that three of these four are about how your *delta* gets disturbed — by spot (gamma), by vol (vanna), by time (charm). That is not an accident. Delta is the hedge you most care about keeping at zero, so the desk pays closest attention to everything that can move it.

### Vanna — when your delta and your vega bleed into each other

**Vanna** measures a single fact that can be stated two equivalent ways:

`vanna = change in delta per 1-point change in volatility = change in vega per 1-point move in spot`

These are the *same number* (a deep result: both are the second derivative of the option price with respect to spot and vol, and the order of differentiation does not matter). That dual nature is exactly why vanna matters, so sit with it.

Read it the first way — **how does my delta change when volatility moves?** Suppose you have carefully hedged a position to be delta-neutral on a calm morning. Then India VIX spikes from 13 to 18 because a global shock hits. You have not traded, spot has barely moved, yet vanna tells you your delta is **no longer zero.** The vol move alone has tilted the table. Your "neutral" book has quietly grown a directional lean — precisely at the moment the market is most dangerous.

Read it the second way — **how does my vega change when spot moves?** As Nifty falls toward a put strike you are short, that put's vega swells; as it rallies away, the vega shrinks. Your exposure to volatility is itself moving around as spot travels.

**Why vanna is central to skew and risk-reversals.** Recall the volatility skew (covered in the volatility chapters): out-of-the-money Nifty puts trade at a *higher* implied volatility than equidistant out-of-the-money calls, because the market pays up for crash protection. In a falling market, two things happen *together* — spot drops and implied vol rises. These are not independent; they are correlated, and vanna is the Greek that captures the joint effect. A **risk reversal** (long an OTM call, short an OTM put, or vice versa) is essentially a *bet on skew*, and its dominant risk is vanna. A desk that has sold downside puts is short vanna in the worst way: as the market falls and vol jumps, its delta turns more and more short, forcing it to buy back into a crashing market to re-hedge — the classic accelerant behind sharp sell-offs. Ignoring vanna means your hedges drift exactly when you can least afford it.

### Volga (vomma) — the convexity of your vega

**Volga**, also spelled **vomma**, measures:

`volga = change in vega per 1-point change in volatility`

If vega is your sensitivity to volatility, volga is the *curvature* of that sensitivity — it is the "gamma of vega." Just as gamma tells you that delta is not constant as spot moves, volga tells you that **vega is not constant as vol moves.**

The intuition: a book can be **vega-neutral at today's vol level and still make or lose serious money on a large vol move**, because vega itself shifts as volatility travels. Think of vega-neutral as balancing on flat ground at the current VIX. Volga is the curvature of that ground a little distance away in either direction.

- **At-the-money options** have the *most* vega but very *little* volga — their vega is large and roughly flat, so a small vol move barely changes it.
- **Out-of-the-money options (the "wings")** have modest vega at today's vol but *high* volga: a big rise in vol fattens the whole distribution, dragging those far strikes meaningfully into play, so their vega *grows* as vol rises.

This is why **trading the wings is really trading volga.** A long-volga position — typically built from far-OTM strangles — *gains vega as volatility rises*, so in a genuine volatility blow-up it makes more than a naive linear vega estimate predicts. That convexity is precisely what makes long-wing structures attractive as **tail hedges.** Conversely, a desk that sells cheap-looking OTM wings to collect premium is **short volga**: in calm markets it earns a trickle, but in a vol explosion its losses accelerate faster than its vega would have warned. Volga is the Greek of "vol of vol." On an Indian book, anyone holding far-OTM Nifty or Bank Nifty options through a budget, an election count day, or an RBI surprise is implicitly trading volga, whether they have named it or not.

### Charm — when your delta decays from the calendar alone

**Charm** — also called **delta decay** or **delta bleed** — measures:

`charm = change in delta per unit of time passing` (holding spot and vol fixed)

This is the most operationally useful second-order Greek for an Indian trader, because India lives in weekly expiries and charm is fiercest near expiry.

The intuition: an option's delta is, loosely, the market's estimate of the probability it finishes in the money. As expiry approaches, that probability estimate *sharpens* even if spot does not move. An out-of-the-money option that still had a fighting chance with five days left looks hopeless with one day left, so its **delta bleeds toward zero.** An in-the-money option becomes near-certain to be exercised, so its **delta drifts toward one** (or toward minus one for a put). Charm is the speed of that drift, driven purely by the clock.

Why a desk cares, concretely: suppose on Tuesday you sold an OTM Nifty call and hedged its delta by buying a few futures. You walk away delta-neutral. You do *nothing* on Wednesday and Thursday — and yet by Thursday morning, even if Nifty has not moved a single point, the call's delta has shrunk (charm at work), so your futures hedge is now too big and your book has developed a delta out of thin air. **Charm tells you how much your hedge will rot overnight from time alone.**

This matters most in two situations the professionals obsess over:

1. **Over a weekend.** Friday's close to Monday's open spans three calendar days of decay but zero trading hours to re-hedge. A desk estimates the weekend's charm on Friday afternoon and pre-adjusts its hedge so it does not walk into Monday with an unwanted delta.
2. **Into expiry week.** Charm is **largest for near-the-money options close to expiry** — which is *exactly* the Indian weekly trader's bread and butter. A book hedged at Wednesday's close can open Thursday (expiry day) with a meaningfully different delta purely from the day's passage, and around the at-the-money strike that drift can be violent.

### Colour, speed and zomma — name-only awareness

You should *recognise* these but never need to compute them by hand. They are third-order Greeks — the rates of change of the second-order Greeks — and they live deep inside a professional risk system.

- **Speed** = how **gamma** changes as **spot** moves (the third derivative with respect to spot). It tells a desk how fast its gamma is itself shifting in a fast market — relevant when running a large gamma position into a sharp move.
- **Zomma** = how **gamma** changes as **volatility** moves. It warns that the gamma you hedged at today's VIX will be different after a vol spike.
- **Colour** (also spelled **color**) = how **gamma** changes as **time** passes. It tells the desk how its gamma profile will look tomorrow given nothing else changes — important when gamma is large and expiry is near, because colour can be big in exactly that corner.

The pattern is worth seeing: just as vanna, charm and gamma describe how *delta* gets disturbed by vol, time and spot, the trio zomma, colour and speed describe how *gamma* gets disturbed by the same three forces. The Greeks form a tidy hierarchy, and a full institutional risk engine simply computes the whole grid.

### How a desk actually uses these to keep a hedge accurate

Strip away the names and here is the working picture. A delta-hedged book is a balance that three forces constantly try to tip: spot (gamma), vol (vanna), and time (charm). A professional does not re-hedge on every tick — that bleeds money to costs and the bid-ask spread. Instead the desk *anticipates*:

- It uses **gamma** to know how much delta a given spot move will create, and sets re-hedge thresholds accordingly.
- It uses **vanna** to know that a vol spike will hand it an unwanted delta, so when VIX jumps it checks its directional lean *before* the next spot move compounds it — and it watches vanna especially closely on any skew or risk-reversal position.
- It uses **charm** to pre-position the hedge for time it cannot trade through — overnight, over a weekend, into expiry — so the book does not drift while the desk sleeps.
- It uses **volga** to understand the convexity of its vol bet, knowing that a vega-neutral book can still bleed or print on a large vol move, and pricing its wings accordingly.

In short: the first-order Greeks tell you where your risk *is*; the second-order Greeks tell you where your risk *is going* as the market moves. A hedge built only on first-order Greeks is accurate for an instant and stale by the next. The professionals stay accurate by hedging the *changes* in their Greeks, not just the Greeks.

## Worked example (₹, Nifty)

Let us make **charm** concrete, because it is the one a weekly trader meets most directly. Assume Nifty spot is **24,000**, you are looking at the slightly out-of-the-money **24,200 call**, and you sold **5 lots** (Nifty lot size about 75, so 375 options). Implied vol is steady at 14%, spot does not move, and we simply let time pass over expiry week.

**Step 1 — Establish the starting hedge.** On Tuesday, with 2 days to Thursday expiry, suppose the 24,200 call has a delta of about **0.35**. Because you are *short* 375 calls, your position delta is:

`position delta = -375 * 0.35 = -131`

To be delta-neutral you buy futures equivalent to +131 deltas (about 1.75 lots of Nifty futures). Your book is now flat.

**Step 2 — Let one day pass, nothing else.** Charm bleeds the OTM call's delta toward zero. Suppose by Wednesday the same call's delta has fallen from 0.35 to about **0.27** purely from time (spot still 24,000, vol still 14%). The change in delta per option is `0.27 - 0.35 = -0.08` over one day — that is charm in action.

Your *short* position delta is now:

`position delta = -375 * 0.27 = -101`

**Step 3 — See the hedge drift.** You still hold the +131 futures delta from Tuesday, but your options now contribute only -101. Your book is no longer neutral:

`net delta = +131 (futures) - 101 (options) = +30`

You have woken up **long 30 deltas** without trading and without spot moving a single point. That is roughly +₹30 of P&L per one-point Nifty move that you did not intend to carry. To return to neutral you must *sell* about 30 deltas of futures. **Charm predicted this drift in advance:** had you computed it on Tuesday, you would have known Wednesday's hedge needed trimming and could have planned the adjustment instead of being surprised.

**Step 4 — Scale the lesson.** Thirty deltas is trivial on five lots. Now imagine a desk short 5,000 of these expiry-week calls instead of 375. The same per-option charm produces a delta drift of roughly `(0.08) * 5000 ≈ 400 deltas` per day — a position that genuinely must be managed overnight and especially across the weekend, when three days of charm accumulate with no chance to trade. This is why expiry-week desks watch charm as closely as a retail trader watches the spot price.

## Common mistakes / risk note

- **Believing a delta hedge is permanent.** The single most common error is hedging delta once and assuming you are protected. You are protected for an instant. Gamma, vanna and charm are all conspiring to re-tilt your book within hours. A "neutral" position left unattended overnight is rarely neutral by morning.
- **Forgetting that vol and spot move together.** Beginners model a vol shock and a price shock as separate events. In a real Indian sell-off they arrive *together*, and vanna is the Greek of that joint move. Stress-testing only "spot down" while holding vol fixed badly understates the risk of a short-put or risk-reversal book.
- **Selling the wings as "free money."** OTM strangles look like easy premium in calm markets, but selling them makes you **short volga** — your losses accelerate non-linearly in a vol explosion. Around budgets, election counts and RBI decisions, that convexity is exactly when it bites. The premium is the rent the market charges you for taking on negative convexity, not a gift.
- **Over-engineering a small book.** The opposite error: a retail trader computing vanna and volga for two lots. For a handful of weekly contracts, delta, theta and vega explain essentially all of your P&L, and the second-order Greeks are smaller than your transaction costs. These Greeks earn their keep at *scale*; know they exist, but do not drown a small position in them.
- **The honest backdrop.** None of this changes the base-rate reality: long options usually expire worthless, option selling carries large and sometimes undefined risk, and SEBI studies show roughly 9 in 10 retail F&O traders lose money. Mastering the second-order Greeks makes a professional's hedging more *accurate*; it does not turn a losing approach into a winning one. Use them to manage risk, not to manufacture false confidence.

## Key takeaways

- **The Greeks themselves move.** First-order Greeks tell you where your risk is; second-order Greeks tell you where it is heading as spot, vol and time change.
- **Vanna** = how delta changes with vol (= how vega changes with spot). It is the dominant risk in skew and risk-reversal trades, and it hands you an unwanted delta exactly during a vol spike.
- **Volga (vomma)** = how vega changes with vol — the convexity of your vol exposure. Long-wing structures are long volga (good in a blow-up); selling wings makes you short volga (dangerous in a blow-up).
- **Charm** = how delta drifts purely from time passing. It is largest for near-the-money options close to expiry — the Indian weekly trader's home turf — and is critical for managing a hedge overnight, over a weekend, and into expiry.
- **Colour, speed and zomma** are third-order Greeks (how gamma shifts with time, spot and vol); know the names, lean on the risk system for the numbers.
- A professional hedges the *changes* in the Greeks, not just the Greeks — that is what keeps a hedge accurate as the market moves.

## Practice problems

1. **Conceptual.** State, in one sentence each, what vanna, volga and charm measure. For each, name one Indian-market situation where it becomes a first-order concern.
2. **Conceptual.** Vanna can be described two equivalent ways. Write both, and explain why a desk holding a short OTM-put (downside) position is exposed to vanna in a market crash.
3. **Numeric (charm).** You are short 10 lots (lot size 75) of an OTM Bank Nifty call. Today its delta is 0.30; one day of charm is expected to drop the delta to 0.22 with spot and vol unchanged. You are currently delta-hedged with futures. After one day, what net delta will your book carry, and what trade restores neutrality?
4. **Conceptual.** Why is volga small for an at-the-money option but large for a far-OTM "wing" option? What does this imply about who is long and who is short volga in an OTM strangle trade?
5. **Conceptual.** A trader hedges delta at Friday's close and does nothing until Monday. Why might the book open Monday with a non-zero delta even if Nifty opens exactly where it closed on Friday? Which Greek governs this, and why is the effect larger over a weekend than over a single weekday night?
6. **Numeric (vanna intuition).** A delta-neutral book has a vanna such that delta changes by +6 deltas for every 1-point rise in implied volatility (in vol-point terms). India VIX jumps from 13 to 17 overnight with spot unchanged. Estimate the new book delta and state the hedge required to flatten it.

## Solutions

**1.** *Vanna* measures how delta changes when volatility moves (equivalently, how vega changes when spot moves) — it becomes first-order on a risk-reversal or skew position when a falling Nifty raises vol simultaneously. *Volga* measures how vega changes when volatility changes (the convexity of vega) — it becomes first-order when holding far-OTM Nifty wings through an event like the Union Budget or an election result. *Charm* measures how delta drifts purely from time passing — it becomes first-order in expiry week (Thursday) and across weekends, when near-the-money delta bleeds fastest and you cannot trade through the gap.

**2.** The two equivalent statements: (a) the change in delta per 1-point change in volatility, and (b) the change in vega per 1-point move in spot. A desk short downside puts is short vanna in the dangerous direction: in a crash, spot falls *and* implied vol rises together. The vol rise (via vanna) makes the puts' delta more negative, so the short-put book's delta turns increasingly short, forcing the desk to buy futures into a falling market to re-hedge — losses and forced buying compound exactly when liquidity is worst.

**3.** Position is short 10 * 75 = 750 calls. Starting option delta = -750 * 0.30 = -225, hedged with +225 futures deltas (book flat). After one day of charm, option delta = -750 * 0.22 = -165. Net book delta = +225 (futures) - 165 (options) = **+30 deltas long.** To restore neutrality, **sell 30 deltas of Bank Nifty futures** (about 0.4 of a 75-lot, so in practice you would round and manage the residual). The drift came entirely from the calendar, not from any price move.

**4.** Volga is the curvature of vega with respect to vol. An ATM option already has large, near-maximal vega that is roughly flat around the current vol level, so a small vol change barely alters it — low volga. A far-OTM wing has modest vega at today's vol, but a large rise in vol fattens the distribution and drags that far strike toward relevance, sharply increasing its vega — high volga. In an OTM strangle, the **buyer is long volga** (vega grows as vol rises, helping in a blow-up — useful as a tail hedge), and the **seller is short volga** (vega grows against them as vol rises, so losses accelerate non-linearly in a vol spike).

**5.** Over the weekend, time passes — three calendar days — but there are no trading hours in which to adjust. **Charm** causes the options' deltas to drift purely from this passage of time (OTM deltas bleed toward zero, ITM toward one), so the option side of the hedge no longer matches the static futures hedge set on Friday, leaving a net delta on Monday's open even with unchanged spot. The effect is larger over a weekend because charm accumulates with roughly three days of decay rather than one, and there is no opportunity to re-hedge in between — which is why desks pre-adjust for weekend charm on Friday afternoon.

**6.** Vol rises by 17 - 13 = 4 vol points. New delta ≈ starting delta + vanna * vol change = 0 + (+6 per point) * 4 = **+24 deltas.** The book, hedged neutral the night before, now sits long 24 deltas purely from the vol spike (spot unchanged). To flatten, **sell 24 deltas of Nifty futures.** This illustrates vanna's signature danger: a hedge that was neutral becomes directional the moment volatility moves, before spot has done anything at all.
