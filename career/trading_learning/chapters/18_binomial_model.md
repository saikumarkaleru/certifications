# Chapter 18: The Binomial Model — Pricing by Replication

Imagine a friend offers you a strange bet: he will pay you ₹5,040 if Nifty finishes above 24,000 in two months, and nothing otherwise. What is that promise worth today? Most people reach for a probability — "maybe 40% chance, so 40% of 5,040." That answer is almost always wrong, and the reason it is wrong is the single most important idea in option pricing.

The right way to value the promise is not to guess the odds. It is to ask: **can I build a do-it-yourself version of that payoff using things I can already buy and sell — some Nifty exposure plus some borrowing?** If I can build a portfolio that pays *exactly* what the option pays in every possible future, then the option must cost the same as that portfolio. If it did not, you could buy the cheap one, sell the dear one, and pocket free money. Markets do not leave free money lying around for long. This is pricing by **replication**, and the binomial model is the cleanest place to see it work.

## Core concepts

### The big idea: an option is a recipe you can cook yourself

A **replicating portfolio** is a basket of simpler instruments — here, units of the underlying plus cash you borrow or lend — chosen so that its future value matches the option's payoff in every scenario. The law of one price says two things with identical payoffs must have identical prices. So the cost of *building* the portfolio today is the *fair price* of the option today. No probabilities of the real world enter this argument at all. That feels almost magical, and we will see exactly why it happens.

To make the future tractable, the binomial model makes a deliberately crude assumption: over one small step of time, the underlying can only do one of **two** things — jump **up** by a factor `u`, or **down** by a factor `d`. Reality has thousands of possible closing levels, but a coarse two-outcome world is enough to nail the pricing logic, and we recover realism later by chopping time into many tiny steps.

### One step: building the replica

Let us price a Nifty **call** with strike `K = 24,000`, with one step to expiry. Today spot `S = 24,000`. Say over the step Nifty either rises 10% to `S*u = 26,400` or falls 10% to `S*d = 21,600`. (These round moves are illustrative; in practice `u` and `d` come from volatility.)

The call's payoff at expiry — `max(S - K, 0)` — is therefore:

- Up state: `C_up = max(26,400 - 24,000, 0) = 2,400`
- Down state: `C_down = max(21,600 - 24,000, 0) = 0`

Now build a portfolio of two ingredients: hold `delta` units of Nifty, and borrow `B` rupees of cash today (borrowing means you owe `B` later). We want this portfolio to be worth 2,400 in the up state and 0 in the down state. That is two equations:

- Up: `delta * 26,400 - B = 2,400`
- Down: `delta * 21,600 - B = 0`

(For this first pass set interest to zero, so the cash you owe is still `B` at expiry.) Subtract the second from the first:

`delta * (26,400 - 21,600) = 2,400`, so `delta = 2,400 / 4,800 = 0.5`.

This `delta` is the **hedge ratio** — the amount of underlying that moves rupee-for-rupee with the option. Plug back into the down equation: `0.5 * 21,600 - B = 0`, so `B = 10,800`. You borrow ₹10,800 and buy 0.5 units of Nifty.

What does this recipe cost you *today*? You buy 0.5 units at 24,000 (₹12,000) but ₹10,800 of it is borrowed money, so out of your own pocket:

`Call price = delta * S - B = 0.5 * 24,000 - 10,800 = 1,200`

The call is worth **₹1,200** per index unit. Not because of any forecast — purely because ₹1,200 is what it costs to manufacture the call's payoff. If the call traded at ₹1,000, you would buy the call, sell the replica, and harvest a riskless ₹200. Arbitrage forces the price to 1,200.

### The general one-step formula

The same two equations, solved with symbols, give the hedge ratio for any one-step option:

`delta = (Payoff_up - Payoff_down) / (S*u - S*d)`

And the option price is `delta * S` minus the borrowing needed to match the down state. After tidying up the algebra (and now putting interest back in, with continuous rate `r` over time `T`), the price collapses into a strikingly simple form:

`Option = e^(-r*T) * [ p * Payoff_up + (1 - p) * Payoff_down ]`

where

`p = (e^(r*T) - d) / (u - d)`

This `p` is the famous **risk-neutral probability**. The price is just a discounted average of the two payoffs, weighted by `p` and `1 - p`.

### Why "risk-neutral" — and why not the real odds?

Here is the part that trips everyone up. The number `p` *looks* like the probability that Nifty goes up. It is not. It is a manufactured weight that has nothing to do with how likely an up move really is.

Notice what is missing from every equation above: **the actual probability of an up move never appeared.** We matched payoffs state by state; we never asked "how likely is each state?" Two traders who violently disagree about whether Nifty will rise or fall will still compute the *same* `delta`, the same `B`, and the same ₹1,200. Their forecasts are irrelevant because the replica is hedged — it pays the right amount whichever way the market goes.

So where does `p` come from? It is the *one* probability under which the underlying's expected growth equals the risk-free rate — a world where investors demand no extra reward for risk, hence "risk-neutral." It is a pricing device, a change of bookkeeping that makes discounting clean, not a belief about the future. The deep result (the Fundamental Theorem of Asset Pricing) is this:

- **Real-world probabilities** tell you what is *likely* to happen.
- **Risk-neutral probabilities** tell you what things are *worth* today.

We price with the second because pricing is about replication cost, and replication is blind to real odds. Using real-world probabilities would also force you to pick a risk-adjusted discount rate that nobody can agree on; the risk-neutral trick sidesteps that entirely by discounting at the clean, observable risk-free rate.

Let us put a rate in. Take `r = 6%` per year and a one-month step (`T = 1/12`), so `e^(r*T) = e^0.005 = 1.00501`. With `u = 1.10, d = 0.90`:

`p = (1.00501 - 0.90) / (1.10 - 0.90) = 0.10501 / 0.20 = 0.5251`

`Call = e^(-0.005) * [0.5251 * 2,400 + 0.4749 * 0] = 0.99501 * 1,260.1 = 1,253.9`

So with realistic interest the same call is worth about **₹1,254** — a touch more than the ₹1,200 we got at zero rates, because higher rates lift call values (the carry cost of the replicated position).

### Two steps: backward induction

One step is a toy. The power comes from stacking steps. A **two-step tree** lets the index move twice, producing three possible expiry levels. Crucially, an up-then-down move and a down-then-up move land on the *same* node — the tree **recombines** — which keeps the number of nodes small.

The method to price it is **backward induction**: start at expiry where payoffs are known, then walk the tree *backwards*, applying the one-step risk-neutral formula at each node to get its value from the two nodes that follow it. Repeat until you reach today. Every step is just the simple formula you already know, used over and over. We will work a full numeric example next; the figure below shows the shape of the tree you are about to build.

### More steps: converging to Black-Scholes

A two-outcome step is unrealistic, but a *many*-step tree is not. Slice the two months into 50 or 500 tiny steps, each with its own small up/down move, and the set of possible terminal levels fans out into a finely-grained, bell-shaped (lognormal) distribution — exactly the distribution that real returns roughly follow.

To make the steps consistent with a volatility `sigma`, the standard **Cox-Ross-Rubinstein** choice sets `u = e^(sigma * sqrt(dt))` and `d = 1/u`, where `dt` is the length of one step. As you increase the number of steps toward infinity, the binomial price **converges to the Black-Scholes price** (the subject of the next chapter). The binomial model is not a rival to Black-Scholes; it is the same idea told in discrete time, and it converges to the same answer. This is why the binomial tree is the workhorse for teaching: it shows the machinery (replication, risk-neutral weighting) that Black-Scholes hides inside a formula.

### American options: the tree's killer feature

Black-Scholes prices **European** options — exercisable only at expiry. But many real options are **American** — exercisable any day up to expiry. There is no clean closed-form for those, and this is where the tree shines.

The fix is beautifully simple. At every node during backward induction, compare two numbers:

- **Continuation value** — what holding the option is worth (the discounted risk-neutral average of the next two nodes).
- **Exercise value** — the intrinsic value if you exercised *right now* at that node: `max(S - K, 0)` for a call, `max(K - S, 0)` for a put.

Take the larger: `Node value = max(continuation value, exercise value)`. If exercising now beats holding, the rational owner exercises, so that node's value is the exercise value. Carry this through the tree and you have priced an American option — something the Black-Scholes formula simply cannot do.

A note for India: NSE **index** options (Nifty, Bank Nifty) are **European and cash-settled**, so early exercise never applies to them — for those, European pricing is all you need. NSE **single-stock** options are **American-style** (and physically settled), so the early-exercise check genuinely matters there. We will see it bite in the worked example.

## Worked example (₹, Nifty/Bank Nifty)

**Setup.** Price a two-month Nifty **call**, strike `K = 24,000`, spot `S = 24,000`. We use two monthly steps with `u = 1.10` and `d = 0.95` (an up move of +10% or a down move of −5% per month — deliberately asymmetric so the tree is interesting). Risk-free rate `r = 6%` per year, so per step `e^(r*dt) = e^(0.06/12) = e^0.005 = 1.00501`.

**Step 1 — build the tree of index levels.**

- After one step: `S_u = 24,000 * 1.10 = 26,400`; `S_d = 24,000 * 0.95 = 22,800`
- After two steps:
  - `S_uu = 26,400 * 1.10 = 29,040`
  - `S_ud = 26,400 * 0.95 = 25,080` (and `22,800 * 1.10 = 25,080` — it recombines)
  - `S_dd = 22,800 * 0.95 = 21,660`

**Step 2 — payoffs at expiry** (`max(S - 24,000, 0)`):

- `C_uu = max(29,040 - 24,000, 0) = 5,040`
- `C_ud = max(25,080 - 24,000, 0) = 1,080`
- `C_dd = max(21,660 - 24,000, 0) = 0`

**Step 3 — the risk-neutral probability.**

`p = (e^0.005 - 0.95) / (1.10 - 0.95) = (1.00501 - 0.95) / 0.15 = 0.05501 / 0.15 = 0.3668`

So `p = 0.3668` and `1 - p = 0.6332`. (It is well below 0.5 because the up move is twice the size of the down move; risk-neutrality must weight the big up move less to keep expected growth at the risk-free rate. This is your proof that `p` is not a real-world forecast.)

![Figure: a two-step binomial tree for Nifty](figs/binomial_tree.png)

**Step 4 — backward induction.** Discount factor per step: `e^(-0.005) = 0.99501`.

Value at the up node (`S_u = 26,400`), looking at `C_uu` and `C_ud`:

`V_u = 0.99501 * [0.3668 * 5,040 + 0.6332 * 1,080] = 0.99501 * [1,848.4 + 683.9] = 0.99501 * 2,532.3 = 2,519.7`

Value at the down node (`S_d = 22,800`), looking at `C_ud` and `C_dd`:

`V_d = 0.99501 * [0.3668 * 1,080 + 0.6332 * 0] = 0.99501 * 396.1 = 394.1`

Value today, looking at `V_u` and `V_d`:

`V_0 = 0.99501 * [0.3668 * 2,519.7 + 0.6332 * 394.1] = 0.99501 * [924.1 + 249.6] = 0.99501 * 1,173.7 = 1,167.8`

**The fair value of the Nifty 24,000 call is about ₹1,168 per index unit.** At a lot size of about 75, one contract costs roughly `1,168 * 75 ≈ ₹87,600`.

**Step 5 — the replication check (today's hedge).** The hedge ratio at the root:

`delta = (V_u - V_d) / (S_u - S_d) = (2,519.7 - 394.1) / (26,400 - 22,800) = 2,125.6 / 3,600 = 0.59`

To replicate the call today you would hold 0.59 units of Nifty (worth `0.59 * 24,000 ≈ ₹14,170`), funding `≈ ₹13,000` of it by borrowing and putting in `≈ ₹1,168` of your own money — which is, of course, exactly the option's price. The recipe and the price agree.

**A taste of early exercise (American put).** Switch to a one-stock setting where options are American. Take a put with `K = 26,000` on the same kind of tree with `u = 1.10, d = 0.90` (`S_dd = 19,440`). At the down node `S_d = 21,600`, the *continuation* value works out to about ₹4,270, but exercising immediately gives intrinsic `26,000 - 21,600 = 4,400`. Since `4,400 > 4,270`, the rational holder **exercises early**, and the node is worth 4,400, not 4,270. Rolling that back, the American put is worth about ₹2,632 versus a European ₹2,571 — the extra **₹61 is the early-exercise premium** the tree captured and Black-Scholes would have missed.

## Common mistakes / risk note

- **Thinking `p` is the chance of an up move.** It is not a forecast; it is a pricing weight under which growth equals the risk-free rate. Bet your *directional* view with sizing, never by tweaking `p`.
- **Garbage `u` and `d`.** The whole model's realism rides on the up/down factors, which come from your **volatility** estimate (`u = e^(sigma*sqrt(dt))`). Feed it the wrong sigma and a perfect tree gives a perfectly wrong price. India VIX is your starting point for sigma.
- **Too few steps.** A 1- or 2-step tree is for *learning*. For a real quote you need many steps to approach the true (Black-Scholes-like) value; coarse trees can be off by a lot, especially near the money.
- **Forgetting Indian settlement reality.** The American early-exercise check is irrelevant for Nifty/Bank Nifty (European, cash-settled) but real for NSE stock options (American, physically settled — and physical delivery brings its own margin and assignment headaches at expiry).
- **The honest risk.** Pricing tells you what an option is *worth*, not whether you will *make money*. A correctly-priced long call still usually expires worthless; correctly-priced option *selling* still carries large, sometimes undefined, losses. SEBI studies find roughly 9 in 10 retail F&O traders lose money. A fair price is a starting point for risk management, not a promise of profit.

## Key takeaways

- An option can be **replicated** by a portfolio of underlying + borrowing; its fair price is what that portfolio costs to build, enforced by arbitrage.
- Over one step, `delta = (Payoff_up - Payoff_down) / (S*u - S*d)` is the hedge ratio, and price = `delta*S` minus borrowing.
- The clean pricing formula is `Option = e^(-r*T) * [p*Payoff_up + (1-p)*Payoff_down]`, with `p = (e^(r*T) - d) / (u - d)`.
- `p` is the **risk-neutral** probability — a pricing device, *not* the real-world chance of an up move. Real probabilities never enter replication.
- **Backward induction** prices a multi-step tree by applying the one-step formula repeatedly from expiry back to today.
- As the number of steps grows, the binomial price **converges to Black-Scholes**.
- The tree handles **American** options by taking `max(continuation value, exercise value)` at every node — the one thing Black-Scholes cannot do.

## Practice problems

1. **Conceptual.** Two traders disagree completely about where Nifty is heading next month, yet they compute the same option price with a one-step tree. Explain how that is possible.
2. **One step, no interest.** Spot Nifty 24,000; over one step it goes to 26,400 (up) or 21,600 (down). Price the 24,000 **put** by building a replicating portfolio (ignore interest). Find `delta`, the borrowing/lending, and the price.
3. **Risk-neutral probability.** Using `u = 1.10`, `d = 0.90`, `r = 7%` per year, and a one-month step, compute `p`. Then price a 24,000 call with `Payoff_up = 2,400`, `Payoff_down = 0`.
4. **Two-step put.** On the worked-example tree (`S = 24,000`, `u = 1.10`, `d = 0.95`, two monthly steps, `r = 6%`, `p = 0.3668`), price the **European** 24,000 put. Terminal levels are 29,040 / 25,080 / 21,660.
5. **Put-call parity check.** From the worked-example call value (₹1,168) and your answer to problem 4, verify they are consistent with put-call parity `Call - Put = S - K*e^(-r*T)` (use `T = 2/12`).
6. **American early exercise.** On a one-step tree with `S = 24,000`, up to 26,400 or down to 21,600, `r = 6%`, one-month step, decide whether an American 26,000 **put** should be exercised today rather than held. Show the comparison.

## Solutions

**1.** Pricing comes from **replication**, not prediction. The two equations that pin down `delta` and the borrowing match the option's payoff in the up state and the down state separately; the *probability* of reaching either state never appears. Both traders hedge identically and pay identically. Their forecasts affect whether they choose to *buy or sell*, and in what size — not the fair price.

**2.** Put payoffs (`max(24,000 - S, 0)`): up `P_up = 0`; down `P_down = max(24,000 - 21,600, 0) = 2,400`.
`delta = (P_up - P_down) / (S_up - S_down) = (0 - 2,400) / (26,400 - 21,600) = -2,400 / 4,800 = -0.5`.
A negative delta means you **short** 0.5 units of Nifty (puts are replicated by shorting the underlying). The down equation (interest 0): `delta*S_down + L = 2,400`, i.e. `-0.5*21,600 + L = 2,400`, so `L = 13,200` — you **lend** ₹13,200 (the short sale raises cash, part of which you lend). Price = `delta*S + L = -0.5*24,000 + 13,200 = -12,000 + 13,200 = 1,200`. The put is worth **₹1,200**. (Sanity check via risk-neutral, `p = 0.5` at zero rates: `0.5*0 + 0.5*2,400 = 1,200`. Matches.)

**3.** `e^(r*dt) = e^(0.07/12) = e^0.005833 = 1.00585`. `p = (1.00585 - 0.90) / (1.10 - 0.90) = 0.10585 / 0.20 = 0.5292`.
`Call = e^(-0.005833) * [0.5292 * 2,400 + 0.4708 * 0] = 0.99418 * 1,270.1 = 1,262.7`. About **₹1,263**.

**4.** Put payoffs (`max(24,000 - S, 0)`): `P_uu = 0`; `P_ud = 0`; `P_dd = max(24,000 - 21,660, 0) = 2,340`. Discount per step `0.99501`.
`V_u = 0.99501 * [0.3668*0 + 0.6332*0] = 0`.
`V_d = 0.99501 * [0.3668*0 + 0.6332*2,340] = 0.99501 * 1,481.7 = 1,474.3`.
`V_0 = 0.99501 * [0.3668*0 + 0.6332*1,474.3] = 0.99501 * 933.5 = 928.8`. The European put is worth about **₹929**.

**5.** `K*e^(-r*T) = 24,000 * e^(-0.06*2/12) = 24,000 * e^(-0.01) = 24,000 * 0.99005 = 23,761.2`.
`S - K*e^(-r*T) = 24,000 - 23,761.2 = 238.8`.
`Call - Put = 1,168 - 929 = 239`. The two sides agree to within rounding (≈ 239), confirming the call and put we priced off the *same* tree are internally consistent — a good way to catch arithmetic slips.

**6.** Risk-neutral `p` (from problem-3 style at `r = 6%`): `p = (1.00501 - 0.90)/0.20 = 0.5251`. Put payoffs at `K = 26,000`: up `max(26,000 - 26,400, 0) = 0`; down `max(26,000 - 21,600, 0) = 4,400`.
**Continuation value** today `= e^(-0.005) * [0.5251*0 + 0.4749*4,400] = 0.99501 * 2,089.6 = 2,079.2`.
**Exercise value** today `= max(26,000 - 24,000, 0) = 2,000`.
Since `2,079.2 > 2,000`, **hold — do not exercise today**. (Early exercise becomes worthwhile only deeper in the money, where intrinsic value overtakes the discounted continuation value, as in the chapter's two-step American example.)
