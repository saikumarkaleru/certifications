# Chapter 10: How to Read & Draw a Payoff Diagram

Ask any professional options trader to explain a position, and within seconds they will reach for the same thing: a little picture of a kinked line. The **payoff diagram** is the single most important visual in all of options. It compresses everything that matters about a trade — how much you can make, how much you can lose, and exactly where the market has to be for you to win — into one shape you can read at a glance. A trader who can *see* a position cannot be fooled by it.

This chapter teaches you to read and draw that picture from scratch. We will build it on the simplest position there is, the **long call**, then show you a recipe that lets you sketch *any* strategy — spreads, straddles, condors, all of it — by the same method. And we will draw the one distinction that separates beginners from pros: the difference between the clean, kinked **at-expiry** payoff and the smooth, rounded **before-expiry** curve that you actually live with day to day.

## Core concepts

### What a payoff diagram actually is

A payoff diagram is a graph of **profit-and-loss versus the price of the underlying**. That is the whole idea. You fix a moment in time (usually expiry), then you ask: "If Nifty finishes *here*, what is my P&L? And if it finishes *there* instead?" Plot the answer for every possible finishing level and you get a line. The *shape* of that line is the personality of the position.

Two axes, and you must get them straight:

- **Horizontal axis (x):** the price of the **underlying** — the spot level of Nifty or Bank Nifty — at the chosen moment (at expiry, unless we say otherwise). This is the one thing you do *not* control; it is the market's job to land somewhere on this axis.
- **Vertical axis (y):** your **profit or loss** in rupees (or in points, which you scale by the lot size). Above the horizontal centre line is profit; below it is loss. The centre line itself — `y = 0` — is the **breakeven line**.

Everything you need to judge a trade is read off these two axes: where the line crosses zero (breakeven), how far up it can climb (max profit), and how far down it can sink (max loss).

### Plotting one option: the long call

Let us build the picture for the position you will trade most as a beginner — buying a call. Say it is mid-week and Nifty spot is around 24,000. You **buy one 24,000 call** (strike `K = 24,000`) for a **premium of ₹150 per unit**. You now have the *right, not the obligation*, to buy Nifty at 24,000 at expiry.

To draw the payoff, work in two pieces. First, the **value of the call at expiry**, which is pure intrinsic value (time value is gone by expiry — see Chapter 6):

`Value at expiry = max(S - K, 0)`

where `S` is the Nifty settlement level. Then subtract what you paid, because the premium is a sunk cost that came out of your pocket on day one:

`Payoff (long call) = max(S - K, 0) - premium`

That single formula is the whole diagram. Read it in two regimes:

- **Below the strike (S <= 24,000):** the call finishes worthless, `max(S - K, 0) = 0`, so your payoff is `0 - 150 = -150`. You lose the full premium, no matter *how far* below the strike Nifty lands. This is why the left side of a long-call diagram is a **flat horizontal line** sitting at minus the premium.
- **Above the strike (S > 24,000):** the call has intrinsic value `S - 24,000`, so your payoff is `(S - 24,000) - 150`. For every one-point rise in Nifty, your payoff rises by one point. This is a **rising 45-degree line**.

The two pieces meet at the strike, 24,000, where the line **kinks** — it stops being flat and starts climbing. That kink always sits at the strike price. The kink is the signature of an option: a place where the position's behaviour suddenly changes.

### Reading the three numbers off the chart

Once the line is drawn, the three quantities a trader cares about jump out:

**Breakeven** — where the rising line crosses zero (`y = 0`). Set the payoff to zero and solve:

`(S - K) - premium = 0  →  S = K + premium = 24,000 + 150 = 24,150`

So Nifty must finish at **24,150** for you to break even. Notice it is the strike *plus* the premium, not the strike itself. A common beginner error is thinking a call is profitable the moment it goes in-the-money. No — it has to climb past the strike by *enough to repay the premium* first. For a long call, breakeven always sits above the strike.

**Maximum loss** — the lowest point of the line. For a long call that is the flat left portion, fixed at the premium you paid: **₹150 per unit**, or `150 * lot size` in rupees. You can never lose more than the premium, because an option is a right you can simply abandon. This capped, known, limited downside is the single best feature of buying options.

**Maximum profit** — the highest the line reaches. For a long call the rising line never stops; Nifty can in principle keep climbing forever, so the maximum profit is **theoretically unlimited**. In practice it is bounded by how far the index can realistically move before expiry, but the *shape* is open-ended on the upside.

Limited, known loss on one side; large, open-ended gain on the other. That asymmetry — a floor under your losses and an open ceiling on your gains — is exactly what you paid the premium for, and the payoff diagram makes it impossible to miss.

![Figure: payoff of a long 24000 call at expiry](figs/long_call.png)

Look at the figure and trace it left to right. The flat shelf on the left sits at -150 (the most you can lose). At 24,000 the line kinks upward. It crosses the zero line at 24,150 (breakeven). Beyond that, every point Nifty gains is a point of profit, and the line marches up and to the right with no ceiling. Four features — flat loss shelf, kink at the strike, breakeven above the strike, unlimited upside — and you have read the entire position.

### Building ANY strategy: add the legs

Here is the idea that turns one diagram into a thousand. **A multi-leg strategy's payoff is just the sum of the payoffs of its individual legs.** You draw each option (or futures, or stock) leg on its own, then *add the lines vertically* — at each price on the x-axis, add up the y-values of all the legs. The combined line is your strategy.

This works because P&L is additive: your total profit at any Nifty level is simply the profit of leg one plus the profit of leg two, and so on. Some rules that make the addition easy:

- A **bought (long)** option contributes its payoff as derived above: `+max(S - K, 0) - premium` for a call, `+max(K - S, 0) - premium` for a put.
- A **sold (short)** option contributes the *mirror image*: you *receive* the premium and *owe* the intrinsic value, so a short call is `premium - max(S - K, 0)` and a short put is `premium - max(K - S, 0)`. Its diagram is the buyer's diagram flipped upside down.
- **Each leg kinks at its own strike.** A two-strike strategy has two kinks; a four-strike strategy (like an iron condor) has four. Between consecutive strikes the combined line is always a *straight* segment, so you really only need to compute the payoff at each strike and at the extremes, then connect the dots.

That last point is the practical shortcut: to sketch any expiry payoff, evaluate the total P&L at each strike price (and at zero, and at a very high price), plot those few points, and join them with straight lines. The kinks can only happen at strikes, so straight segments in between are guaranteed. We use exactly this method to build spreads, straddles and condors in the chapters ahead.

### At expiry vs before expiry: kinked lines vs the smooth curve

Now the distinction that matters most — and that most beginners never internalise.

Everything above describes the payoff **at expiry**. At that final instant there is no time value left, only intrinsic value, so the picture is made of perfectly **straight, kinked lines**. It tells you what you will collect *if you hold to the very end*.

But on any day *before* expiry, the option still carries time value (Chapter 6). Its market price is given by a pricing model — the **Black-Scholes** formula for European index options — which blends intrinsic value with the time value that comes from the days remaining and from volatility (India VIX). So the P&L you would actually realise by *closing the position early* does not follow the kinked line. It follows a **smooth, rounded curve that sits above the at-expiry line** everywhere (because there is still time value to sell back).

Picture the long-call diagram again. The before-expiry curve hugs the same general shape but rounds off the sharp kink at the strike into a gentle bend, and floats above the expiry line by an amount equal to the remaining time value. As expiry approaches, that curve **sags down toward the kinked line**, day by day, as time value bleeds away (this is theta decay, Chapter 6). On the final day, the curve *becomes* the kinked line — the time value has vanished and only intrinsic value remains.

Why this matters in real trading:

- The kinked **expiry** line is your map of outcomes *if you hold to settlement*. Indian index options are European and cash-settled, so this is literally how the trade is squared up if you do nothing.
- The smooth **before-expiry** curve is your *live* mark-to-market — what you would gain or lose by exiting today. Because it sits above the expiry line, a long option can show a *profit* on the curve even while the kinked line still says you are underwater. The two answer different questions ("exit now" vs "hold to expiry").
- The *gap* between the curve and the line is the time value you still hold — and stand to lose if the market stalls. Seeing both lines together is how a pro reads the time-decay headwind on a long position.

We will return to this two-line view constantly, because every Greek is really a statement about *how the smooth curve moves and bends* relative to the kinked line. For now, hold the core idea: **straight kinked lines = at expiry; smooth rounded curve = before expiry, courtesy of time value.**

### A recipe to sketch any position

Put it together into a five-step routine you can run on the back of a napkin:

1. **Draw the axes.** Horizontal = underlying price at expiry (mark the strike(s)); vertical = P&L, with a clear zero line.
2. **List the legs and their strikes.** Note for each whether it is bought or sold, and the premium paid or received.
3. **Compute total P&L at each strike** (and at S = 0 and at a very large S). Remember: kinks happen only at strikes, so these points fully determine the shape.
4. **Connect the dots with straight lines.** That is your at-expiry payoff. Read off breakeven(s), max profit, max loss.
5. **(Optional) Round it.** Float a smooth curve above the kinked line to picture the before-expiry P&L, and remember it sags onto the line as expiry nears.

Master this on the long call and the same five steps handle the most exotic structure in the book.

## Worked example (₹, Nifty/Bank Nifty)

Let us build the long-call diagram fully in rupees and read every number off it.

**Setup.** It is Monday. Nifty spot = 24,000. You buy **one lot** of the 24,000 weekly call at a premium of **₹150 per unit**. The Nifty lot size is currently about **75 units** (the exchange sets and revises lot sizes periodically). So your total outlay — and your maximum possible loss — is:

`Premium paid = 150 * 75 = ₹11,250`

**Step 1 — the payoff formula.** Per unit, `Payoff = max(S - 24,000, 0) - 150`. In rupees for the lot, multiply by 75.

**Step 2 — evaluate at several expiry levels.** Build a small table by plugging in candidate Nifty settlement levels:

| Nifty at expiry (S) | Intrinsic = max(S - 24000, 0) | Per-unit payoff = intrinsic - 150 | Lot P&L (× 75) |
|---|---|---|---|
| 23,700 | 0 | -150 | **-₹11,250** |
| 24,000 | 0 | -150 | **-₹11,250** |
| 24,150 | 150 | 0 | **₹0** |
| 24,300 | 300 | 150 | **+₹11,250** |
| 24,600 | 600 | 450 | **+₹33,750** |

**Step 3 — read the three numbers.**

- **Maximum loss:** the flat shelf at any S at or below the strike — **₹11,250** (the whole premium). It does not get worse if Nifty crashes to 23,000 or 20,000; the call simply expires worthless and you have already paid your most.
- **Breakeven:** where lot P&L crosses zero — `S = K + premium = 24,000 + 150 = 24,150`. Nifty must rise 150 points (about 0.6%) just for you to get your money back.
- **Maximum profit:** unbounded. At 24,300 you are up ₹11,250; at 24,600 you are up ₹33,750; the line keeps climbing for every extra point.

**Step 4 — sanity-check the asymmetry.** Risking ₹11,250 to make an uncapped amount sounds wonderful, but notice the catch the diagram also reveals: between 24,000 and 24,150 the call is *in-the-money yet still losing money*, because the intrinsic value has not yet repaid the premium. The position only turns profitable past 24,150. A 150-point rally leaves you flat; you need *more* than that to win. This is the time-value headwind from Chapter 6, now visible as the gap between the strike (where loss stops growing) and breakeven (where profit starts).

**Step 5 — before vs at expiry.** Suppose by Wednesday Nifty has nudged up to 24,080. At expiry that level would mean a per-unit payoff of `max(24,080 - 24,000, 0) - 150 = 80 - 150 = -70` — a loss. But it is only Wednesday; the call still has two days of time value. Black-Scholes might value it at, say, ₹165, so closing it *now* would actually return `165 - 150 = +15` per unit — a small **profit** on the live curve even though the kinked expiry line says you are down ₹70. That ₹15-versus--₹70 gap is the remaining time value, and it will melt to zero by Friday. The smooth curve sits above the kinked line; as Friday arrives the curve drops onto the line.

## Common mistakes / risk note

- **Putting time on the x-axis.** The horizontal axis is the *underlying price*, not time. A payoff diagram is a snapshot at one moment across all possible prices — it is not a chart of the position over the days.
- **Confusing the strike with the breakeven.** A long call is not profitable the instant it crosses the strike. Breakeven is strike *plus premium* for a call (strike *minus premium* for a long put). Reading max profit from the strike instead of the breakeven overstates your edge.
- **Reading the at-expiry line as your day-to-day P&L.** Before expiry your real, exit-now P&L follows the smooth Black-Scholes curve, which sits above the kinked line by the remaining time value. Expecting the kinked line to describe a mark-to-market in the middle of the week will confuse you every time.
- **Forgetting to subtract the premium.** The bought-option *value* (`max(S - K, 0)`) and your *payoff* (value minus premium) are different lines. The diagram is the payoff — it must be shifted down by the premium.
- **Ignoring lot size and costs.** Points become rupees only after multiplying by the lot size, and your *true* breakeven is a touch further out once you include brokerage, STT, exchange fees and GST. The clean diagram is a model; real breakeven is slightly worse.
- **The honest risk on the other side.** The long call's beautiful capped loss exists *because* you paid for it — and that premium is usually lost; most long options expire worthless, and the flat loss shelf is the most likely outcome. The mirror diagrams — short calls and short puts — are flipped upside down: capped, modest gain on top, but a loss line that plunges down with **large or effectively unlimited** risk. When you start adding legs, always locate the lowest point of the combined line *before* you trade. If there is no lowest point — if the line falls forever — that is undefined risk, and SEBI's finding that roughly 9 in 10 retail F&O traders lose money is most brutal for those who sell such shapes without respecting them.

## Key takeaways

- A payoff diagram plots **P&L (y) against the underlying's price at expiry (x)**. It is the most important visual in options.
- For a long call, `Payoff = max(S - K, 0) - premium`: a flat loss shelf at minus the premium, a **kink at the strike**, then a 45-degree rise with **unlimited** upside.
- Read three numbers off the line: **breakeven** (where it crosses zero — `K + premium` for a call), **max loss** (the premium), and **max profit** (the highest the line reaches).
- Build *any* strategy by **adding the legs vertically**; kinks occur only at strikes, so compute P&L at each strike and connect straight segments.
- **At expiry = straight kinked lines** (pure intrinsic value). **Before expiry = a smooth Black-Scholes curve** that floats above the line by the remaining time value and sags onto it as expiry nears.
- Always find the *lowest point* of the combined line before trading. No lowest point means undefined risk.

## Practice problems

1. **(Conceptual)** On a payoff diagram, what does each axis represent, and what does the point where the line crosses the horizontal centre line tell you?

2. **(Numeric)** You buy a Nifty 24,500 call for a premium of ₹120. Write the payoff formula, and compute the breakeven, maximum loss, and maximum profit (in points).

3. **(Numeric)** For the call in Problem 2, compute the per-unit payoff if Nifty settles at 24,400; at 24,620; and at 24,800. With a lot size of 75, what is the rupee P&L at 24,800?

4. **(Conceptual)** Two days before expiry, the at-expiry (kinked) line for your long call says you are at a ₹40-per-unit loss for the current Nifty level, yet your broker shows the position at a small profit. Explain how both can be true.

5. **(Numeric)** Bank Nifty spot is 52,000. You buy the 52,000 call for ₹400 and *simultaneously* sell the 52,500 call for ₹200 (a two-leg structure). Using the "add the legs" method, find the total P&L at expiry if Bank Nifty finishes at 51,800; at 52,000; at 52,500; and at 53,000. What are the max profit and max loss?

6. **(Conceptual)** Why does the before-expiry curve for a long option always sit *above* the at-expiry kinked line, and what happens to the gap between them as expiry approaches?

## Solutions

**1.** The **horizontal (x) axis** is the price of the underlying — the Nifty/Bank Nifty spot level — at the chosen moment, normally expiry. The **vertical (y) axis** is your profit-or-loss (in points or rupees), with profit above the centre line and loss below it. Where the payoff line crosses the horizontal centre line (`y = 0`) is the **breakeven**: the underlying level at which the position makes exactly zero profit and zero loss. To the side where the line is above zero you make money; where it is below, you lose.

**2.** Payoff formula per unit: `Payoff = max(S - 24,500, 0) - 120`.
- **Breakeven:** `S = K + premium = 24,500 + 120 = 24,620`.
- **Maximum loss:** the premium, **120 points**, occurring at any settlement at or below the 24,500 strike.
- **Maximum profit:** **unlimited** — the rising line never stops, since Nifty can keep climbing above 24,620.

**3.** Using `max(S - 24,500, 0) - 120`:
- S = 24,400: `max(24,400 - 24,500, 0) - 120 = 0 - 120 = `**-120** points (full loss; below the strike).
- S = 24,620: `max(24,620 - 24,500, 0) - 120 = 120 - 120 = `**0** points (exactly breakeven, as expected).
- S = 24,800: `max(24,800 - 24,500, 0) - 120 = 300 - 120 = `**+180** points.
- Rupee P&L at 24,800 with lot size 75: `180 * 75 = `**+₹13,500**.

**4.** Both are true because they answer different questions. The **kinked line is the at-expiry payoff** — what you would collect *if you held to settlement* — and it uses only intrinsic value. The **broker's mark is your live, exit-now P&L**, which follows the smooth Black-Scholes curve and still includes the option's remaining **time value** (two days' worth, plus whatever India VIX supports). Because that curve sits *above* the kinked line by the amount of remaining time value, your sell-now value can be a small profit even while the hold-to-expiry line shows a ₹40 loss. If the market simply sits still into Friday, the time value decays and the curve drops onto the kinked line — so that paper profit would turn into the -₹40 outcome unless Nifty moves in your favour.

**5.** Add the two legs at each level. Long 52,000 call: `max(S - 52,000, 0) - 400`. Short 52,500 call: `200 - max(S - 52,500, 0)`. Net premium paid = `400 - 200 = 200` (a debit). Total payoff = `max(S - 52,000, 0) - max(S - 52,500, 0) - 200`.
- S = 51,800: `0 - 0 - 200 = `**-200** points.
- S = 52,000: `0 - 0 - 200 = `**-200** points.
- S = 52,500: `500 - 0 - 200 = `**+300** points.
- S = 53,000: `1,000 - 500 - 200 = `**+300** points.

The line is flat at -200 up to the 52,000 strike, rises between the two strikes, then flattens at +300 beyond 52,500. So **maximum loss = 200 points** (the net debit, for any finish at or below 52,000) and **maximum profit = 300 points** (capped, for any finish at or above 52,500). This capped-both-ways shape is a bull call spread — the short leg pays for part of the long leg but also caps the upside. (Breakeven, for completeness, is `52,000 + 200 = 52,200`.)

**6.** The before-expiry curve sits above the kinked line because, on any day before expiry, a long option still carries **time value** on top of its intrinsic value — there is still a chance the market moves further in your favour, and that chance is worth money (priced by Black-Scholes from the days remaining and from volatility/India VIX). Since you could sell the option back and collect that extra time value, your exit-now P&L is higher than the pure-intrinsic at-expiry payoff at every price — hence the curve floats above the line. As expiry approaches, the time remaining shrinks, time value bleeds away (theta decay), and the gap narrows. At the moment of expiry the time value is exactly zero, the curve coincides with the kinked line, and the smooth curve *becomes* the straight payoff.
