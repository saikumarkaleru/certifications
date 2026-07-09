# Chapter 31: How Implied Volatility Is Calculated

In the last chapter you met implied volatility (IV) as the market's forecast of future movement — the one input in the Black-Scholes-Merton (BSM) formula you cannot read off a screen. But that raises an obvious question. If you cannot *observe* implied volatility, where does the number on your option chain — "IV: 14.3%" — actually come from? Nobody at the NSE is broadcasting a volatility figure. So how is it computed?

The answer is one of the most elegant tricks in finance. Implied volatility is not measured; it is *reverse-engineered*. The market gives us the price, and we run the pricing model **backwards** to ask: "What volatility number, if I plugged it into Black-Scholes, would make the model spit out exactly this market price?" That number — the volatility *implied by* the price — is the implied volatility. This chapter shows you precisely how that backward solve is done, why it must be done by trial and error rather than algebra, and how the whole machine connects to the India VIX you will meet next.

## Core concepts

### The big idea: IV is the volatility that makes model price equal market price

Recall the Black-Scholes-Merton formula from Chapter 20. It takes five inputs and returns a fair option price:

`BSM price = f(S, K, T, r, sigma)`

where `S` is the spot price, `K` the strike, `T` the time to expiry, `r` the risk-free interest rate, and `sigma` (sigma) the volatility. Four of those five inputs are sitting right in front of you. Spot is on the ticker. Strike is fixed by the contract. Time to expiry is a calendar calculation. The interest rate is the prevailing risk-free rate (in India, roughly the T-bill or MIBOR rate, currently around 6–7%). Only `sigma`, the volatility, is unknown — and it is the one input that captures the market's *opinion* about the future.

Now turn the problem inside out. In live trading you also know one more thing the formula doesn't normally get handed: the **actual market price** of the option, because it is trading right now on the exchange. So you have a number for everything in the equation *except* sigma. That means you can ask the question backwards:

> "What single value of sigma makes the BSM model price come out *exactly equal* to the price the option is actually trading at?"

That value of sigma is the **implied volatility**. It is the volatility the market is *implying* through the price it has set. Formally, IV is the solution to:

`BSM price(S, K, T, r, IV) = market price`

This is why traders call IV "the market's volatility opinion compressed into a single number." Every buyer and seller haggling over an option's premium is, whether they know it or not, voting on how much they think the underlying will move. Their collective verdict shows up as the traded price, and IV is simply that verdict translated out of rupees and into the language of the model — an annualised percentage of expected movement.

A useful mental image: the BSM formula is a translation machine. Feed it a volatility, it returns a price. Implied volatility runs the machine in reverse — feed it the price, it returns the volatility. The price and the IV are two ways of quoting the *same* thing. Saying "the 24,000 call costs ₹150" and saying "the 24,000 call has an IV of 14%" are, given the other four inputs, equivalent statements. Professionals think in IV because it strips out the mechanical effects of spot, strike, and time and leaves the pure judgement: how stormy does the market expect things to be?

### Why you cannot just solve for IV with algebra

Here is the frustrating part, and the reason this chapter exists at all. If BSM were a simple equation, you would rearrange it — move terms around — to get `IV = (something)` and be done. You cannot. The volatility `sigma` is buried **inside the cumulative normal distribution function** N(.) in the BSM formula, appearing in both `d1` and `d2`, in a way that no amount of algebraic rearrangement can isolate. There is no closed-form expression `IV = ...`. The equation simply cannot be inverted on paper.

When you cannot solve an equation algebraically, you solve it **numerically** — guess, check how wrong you are, improve the guess, and repeat until you are close enough. This is not a hack; vast areas of engineering run on exactly this kind of iterative root-finding. And the option-price-versus-volatility relationship is beautifully well-behaved: as you raise sigma, the option price rises **smoothly and monotonically** (always upward, never reversing), because more volatility always means a more valuable option (it is pure vega, and vega is always positive for a long option). Since the price climbs steadily and never doubles back, exactly **one** volatility produces any given price — so the answer is unique and a sensible search is guaranteed to find it.

### Newton-Raphson: using vega to home in fast

The workhorse method is called **Newton-Raphson**, and its idea is beautifully simple. Suppose you make a guess for the volatility, plug it into BSM, and get a model price. Compare it to the market price. The gap between them — `model price - market price` — is your error. Now you need to know which way to nudge your guess, and by how much.

This is where **vega** earns its keep. Vega, you will remember from Chapter 25, is precisely the rate at which an option's price changes when volatility changes. So vega is the "exchange rate" between a volatility error and a price error. If your model price is ₹20 too high and vega is ₹8 per volatility point, then your guessed volatility is roughly `20 / 8 = 2.5` points too high — so lower your guess by about 2.5 points. That single step is the whole algorithm:

`IV_next = IV_now - (model price - market price) / vega`

Read it slowly. The numerator `(model price - market price)` is how far off you are, in rupees. Dividing by vega converts that rupee error into a volatility error, in percentage points. Subtracting it from your current guess pushes the guess in the direction that shrinks the gap. If your model price is too *high*, the bracket is positive, you *subtract*, and your volatility guess comes *down* (lowering the next model price). If your model price is too *low*, the bracket is negative, and subtracting a negative *raises* your guess. Either way it self-corrects toward the answer.

Newton-Raphson is prized for its speed: it typically **doubles the number of correct digits each step**, so from a reasonable starting guess two or three iterations pin the IV to a precision finer than the price can even be quoted. A good first guess is something near the current ATM IV or India VIX level, but even a crude start like 20% converges in a handful of steps. This is the routine running silently behind every "IV" column on every broker screen, recomputed for hundreds of strikes many times a second.

### Bisection: the slow-but-sure fallback

Newton-Raphson is fast but occasionally fragile. Its weak spot is the **division by vega**. For deep in-the-money or deep out-of-the-money options, vega becomes tiny (recall from Chapter 25 that vega is largest at-the-money and shrinks toward the wings). Dividing a price error by a near-zero vega can fling the next guess wildly off — to a negative volatility, or to some absurd 300% figure — and the iteration can diverge instead of converge.

When robustness matters more than raw speed, traders fall back on **bisection** — the brute-force "guess the number" game a child plays. You start with a range you are sure the answer lies inside, say volatility somewhere between 1% and 200%, and try the midpoint, 100%. Compute the model price there. If it is too high, the true IV must be in the *lower* half, so you discard everything above 100% and your new range is 1%–100%. Try its midpoint, and so on. Each step **halves** the range that could contain the answer, so the uncertainty shrinks relentlessly: roughly ten steps narrow a 200-point range to a fraction of a percentage point.

Bisection cannot fail to converge — as long as your starting bracket genuinely contains the answer (which the no-arbitrage bounds in the next section guarantee), it *will* close in on it. It is simply slower than Newton-Raphson. So the standard professional implementation is a **hybrid**: try Newton-Raphson for its speed, but if a step jumps outside the sensible bracket or vega gets dangerously small, fall back to a bisection step to stay safe, then resume. Speed when you can, safety when you must.

### No-arbitrage bounds: what keeps IV well-defined

For "the volatility that reproduces the price" to even *have* an answer, the price itself has to be sane. There are hard limits on what an option can legitimately cost — limits enforced not by any rule-book but by **arbitrage**, the fact that a mispricing outside these bounds would be free money that traders would instantly exploit until it vanished. These are the **no-arbitrage bounds**.

For a call option, the price must satisfy:

`max(S - K * e^(-r*T), 0) <= call price <= S`

The **lower bound** is the option's intrinsic value (discounted for the time value of money): a call can never be worth less than the immediate exercise value, because if it were, you could buy the call, exercise, and pocket a riskless profit. The **upper bound** is the spot price itself: a call to *buy* the underlying can never be worth more than just owning the underlying outright. An analogous pair of bounds hems in put prices.

Why does this matter for IV? Because the BSM price, as you slide volatility from 0% toward infinity, sweeps out *exactly* the range between these bounds: at zero volatility the model returns the lower bound (pure discounted intrinsic value), and as volatility grows without limit it approaches the upper bound. So:

- If the market price sits **inside** the no-arbitrage bounds, there is one and only one volatility that reproduces it — IV exists and is unique. Your search is guaranteed to succeed.
- If a quoted price somehow sits **at or outside** the bounds — at intrinsic value, or above spot — then no finite volatility can produce it, and IV is undefined (or zero). In practice this happens with stale quotes, deep-ITM options that barely trade, or the wide bid-ask spreads of illiquid far strikes.

This is the quiet foundation under the whole exercise. The no-arbitrage bounds are what make implied volatility a **well-defined** quantity: they guarantee the search has a target to find and tell the algorithm where to plant its bracket.

### Why IV is quoted per option, and how ATM IV summarises the chain

Notice that the backward solve happens **one option at a time**. Each strike, each expiry, has its own market price, so each produces its own implied volatility. The 24,000 call has an IV; the 24,500 call has a different IV; the same-strike monthly has yet another. There is no single "Nifty volatility" hiding in the data — there is a whole *surface* of IVs, one per contract.

In a perfect Black-Scholes world every option on the same underlying would print the *same* IV, since volatility is supposed to be a property of the underlying, not of the strike you picked. Reality disagrees. Plot IV against strike and you do not get a flat line — you get the famous **volatility smile** or **skew** (the subject of later chapters): out-of-the-money puts typically carry higher IV than at-the-money options, because the market pays up for crash protection. The smile is itself proof that BSM is a simplification — but a wonderfully useful one, because quoting in IV makes these patterns visible and tradeable.

Out of this whole surface, one number is treated as *the* headline reading: the **at-the-money (ATM) implied volatility** — the IV of the option whose strike is nearest the current spot. ATM IV is the market's cleanest single estimate of expected movement, for good reasons. ATM options are the most liquid and most heavily traded, so their prices are the most trustworthy; they carry the most vega, so their IV is computed most reliably (no near-zero-vega division trouble); and they are the least distorted by the skew. When a trader says "Nifty IV is 13% today," they almost always mean the ATM IV. It is the one-number summary of the entire chain — and, as you are about to see, it is the seed from which India VIX grows.

### Reading a price jump: when IV (fear) rose with no spot move

Here is the single most practically useful consequence of everything above, and it falls straight out of the "price and IV are two quotes for the same thing" idea. Suppose you are watching a Nifty option and its premium suddenly jumps — but spot has barely twitched. The 24,000 call leaps from ₹150 to ₹185 while Nifty sits frozen at 24,000. What just happened?

Walk through the inputs. Spot `S` is unchanged. Strike `K` is fixed. Time `T` if anything just *decreased* (which should make the option cheaper, not dearer). The rate `r` did not move. Four of the five BSM inputs are flat or pushing the price *down* — yet the price went *up*. By elimination, the only input that can possibly explain the jump is the fifth one: **volatility**. The market just repriced the option to a higher implied volatility. Run the backward solve and you would find the IV had climbed several points.

And what does a jump in implied volatility *mean*? It means the market suddenly expects bigger future moves — more uncertainty, more **fear**. A premium that swells while spot stands still is the unmistakable fingerprint of rising IV. This is exactly what you see in the minutes before a surprise news headline, an unexpected RBI statement, or a geopolitical shock: premiums balloon across the chain with little or no directional move, because the *width* of the expected outcome range has widened even though its *centre* has not shifted. Learning to read this — "the price moved but spot didn't, so fear rose" — is a genuine professional skill. It lets you see volatility changing in real time, in the raw premiums, without even glancing at a separate indicator.

### How this connects to India VIX

Everything in this chapter — backing IV out of prices, ATM IV as the headline reading — is the foundation of the **India VIX**, the subject of the next chapter. India VIX takes the same idea and industrialises it. Instead of inverting one option to get one IV, it blends the prices of a whole basket of near-month Nifty options (not just the ATM strike, but a spread of out-of-the-money calls and puts on either side) into a single measure of expected 30-day volatility. It is, in spirit, a market-wide weighted average of implied volatilities — the entire chain's fear distilled into one published number. The per-option backward solve you have just learned is the atom; India VIX is the molecule built from many such atoms.

## Worked example (₹, Nifty)

Let us actually *run* the backward solve and watch Newton-Raphson find an IV in two steps.

**Setup.** Nifty spot `S` = 24,000. You are looking at the **ATM 24,000 weekly call** with `T` = 7 days to expiry (about 0.0192 years) and a risk-free rate `r` = 6.5%. The call is trading in the market at a premium of **₹165**. You want to know the implied volatility.

**Step 0 — Make a first guess.** A sensible starting point is the recent ATM IV level; say India VIX has been hovering near **12%**, so start with `sigma` = 12%.

**Step 1 — Price the option at the guess, and find the error.** Plug `S` = 24,000, `K` = 24,000, `T` = 0.0192, `r` = 6.5%, `sigma` = 12% into BSM. For an ATM option this short-dated, the model returns a price of roughly **₹142**. (You can sanity-check the order of magnitude with the ATM rule of thumb from Chapter 20: ATM call ≈ `0.4 * S * sigma * sqrt(T)` = `0.4 * 24000 * 0.12 * sqrt(0.0192)` ≈ ₹160; the precise BSM figure is a little lower once the exact normal terms are used.) The error is:

`model price - market price = 142 - 165 = -₹23`

Our model price is ₹23 *too low*, which tells us our volatility guess is too low — we need to raise it.

**Step 2 — Take one Newton-Raphson step using vega.** Suppose the BSM vega of this option at the current guess is about **₹13** per volatility point. Apply the update rule:

`IV_next = IV_now - (model price - market price) / vega`
`IV_next = 0.12 - (-23 / 13 expressed in vol points)`
`IV_next = 12% - (-1.77%) = 12% + 1.77% ≈ 13.77%`

The negative error pushed our guess *up* by about 1.77 percentage points, exactly as intuition demanded. New guess: **13.77%**.

**Step 3 — Re-price at the new guess and check.** Plug `sigma` = 13.77% back into BSM. The model now returns a price of about **₹163** — only ₹2 away from the ₹165 market price. In a single Newton step we have gone from a ₹23 error to a ₹2 error.

**Step 4 — One more step to finish.** Repeat the update with the residual ₹2 error: `IV_next = 13.77% - (-2 / 13) ≈ 13.77% + 0.15% ≈ 13.92%`. Re-pricing at 13.92% gives essentially ₹165, matching the market to within the tick size. We stop.

**Conclusion.** The implied volatility of the 24,000 call is about **13.9%**. We never solved any equation for sigma — we guessed 12%, measured a ₹23 error, used vega to convert that into a +1.77-point volatility correction, and in two iterations converged to the volatility that makes BSM reproduce the ₹165 market price exactly. That 13.9% *is* the market's volatility opinion for this option, and it is what the broker screen would display in its IV column.

(Had this been a deep OTM strike with a vega near ₹1 instead of ₹13, the very first Newton step could have overshot to a silly number — which is exactly when the algorithm would quietly switch to a bisection step, halving a 1%–200% bracket repeatedly until it closed in safely.)

## Common mistakes / risk note

- **Thinking IV is something the exchange "measures" or publishes.** It is not a measured quantity like temperature. It is *back-solved* from traded prices through a model. Different models or different rate/dividend assumptions can give slightly different IVs for the same option — IV is always "IV *according to this model*."
- **Trusting the IV of illiquid, wide-spread options.** The backward solve is only as good as the price you feed it. A stale or wide bid-ask quote on a deep-OTM far-month strike can produce a garbage IV — or none at all if the mid-price sits outside the no-arbitrage bounds. ATM IV is reliable; deep-wing IV often is not.
- **Confusing a price jump with a directional signal.** A premium that surges while spot is flat is *not* telling you the market is about to go up. It is telling you IV (fear) rose — the expected *range* widened. Reading rising premiums as a directional bull signal is a classic misinterpretation.
- **Forgetting IV is per-option.** There is no single "the IV." Quote which strike and expiry you mean. The smile/skew means a 24,000 call and a 23,000 put can have very different IVs at the same instant — and the difference is information, not error.
- **The honest risk.** Knowing how to compute IV does not tell you whether IV is cheap or rich, or which way it will move next. IV can stay elevated longer than your premium can survive theta, and selling "expensive" IV carries the large, sometimes unlimited, risk covered in the vega chapter. The calculation is a measuring tool, not a trading edge by itself.

## Key takeaways

- **Implied volatility is the volatility that makes the BSM model price equal the market price** — the market's volatility opinion compressed into a single number, found by running the pricing model *backwards*.
- **BSM cannot be inverted algebraically** for sigma (it is trapped inside the normal distribution), so IV is solved **numerically** by iterative guessing.
- **Newton-Raphson** uses vega as the volatility-to-price exchange rate: `IV_next = IV_now - (model price - market price) / vega`, doubling the correct digits each step and converging in 2–3 iterations.
- **Bisection** is the slow-but-sure fallback — halve the bracket each step — used when vega is tiny (deep ITM/OTM) and Newton-Raphson risks diverging; real systems run a hybrid.
- **No-arbitrage bounds** (intrinsic value <= call price <= spot) keep IV well-defined: a price inside the bounds has exactly one IV; a price outside has none.
- **IV is quoted per option** because of the volatility smile/skew; the liquid, high-vega **ATM IV** is the headline one-number summary of the whole chain.
- **A premium that jumps while spot is flat means IV — fear — rose**, since volatility is the only BSM input left to explain it. This same per-option IV machinery is what the **India VIX** (next chapter) blends across many strikes.

## Practice problems

1. **The core definition.** In one sentence, state what implied volatility *is* in terms of the BSM model and the market price. Why is it described as "the market's opinion in one number"?

2. **Why no algebra?** A friend with an engineering degree insists that "any formula can be rearranged to solve for any variable." Explain why this fails for BSM and implied volatility, and what we do instead.

3. **One Newton step (numeric).** You are solving for the IV of a Bank Nifty call trading at ₹240. Your current volatility guess is 15%, at which BSM prices the option at ₹210, and its vega is ₹12 per point. Compute the next IV guess using the Newton-Raphson update. Is your guess moving up or down, and why does that make sense?

4. **Reading a price jump.** Over ten minutes, a Nifty 24,000 put rises from ₹120 to ₹150 while spot stays pinned at 24,000 and there is still a week to expiry. Using the BSM inputs, explain what must have changed and what it says about the market's mood.

5. **When the method breaks (conceptual).** For a deep in-the-money option, Newton-Raphson sometimes throws out a negative or absurd volatility on its first step. Identify which term in the update formula causes this and describe the safer fallback method and why it cannot fail.

6. **Bounds check (numeric).** Nifty spot is 24,000 and a 23,000 call (1,000 points in the money) is quoted at ₹990. Using the lower no-arbitrage bound (treat the discount factor as roughly 1 for a near-dated option), is this price legitimate? What does it imply about the option's implied volatility?

## Solutions

1. Implied volatility is the value of `sigma` that, when plugged into the Black-Scholes-Merton formula along with the known spot, strike, time, and rate, makes the model's output price exactly equal the option's current market price. It is "the market's opinion in one number" because the traded price is the collective verdict of all buyers and sellers on how much the underlying will move, and IV is that verdict translated out of rupees into a single annualised volatility figure — strip away spot, strike, and time, and IV is the pure judgement of expected turbulence.

2. The friend is wrong because volatility `sigma` appears *inside* the cumulative normal distribution function N(.) in BSM (within both `d1` and `d2`), and there is no way to algebraically isolate a variable trapped inside that function — no closed-form `IV = ...` exists. When a formula cannot be inverted on paper, we solve it **numerically**: guess a volatility, compute the resulting model price, measure the error against the market price, and improve the guess, repeating until the model price matches. Because option price rises smoothly and monotonically with volatility, the answer is unique and the search is guaranteed to find it.

3. Error = `model price - market price = 210 - 240 = -₹30`. Update: `IV_next = 0.15 - (-30 / 12 points) = 15% - (-2.5%) = 15% + 2.5% = 17.5%`. The guess moves **up**, from 15% to 17.5%. This makes sense: the model price (₹210) was *below* the market price (₹240), meaning our volatility was too low — a higher volatility produces a higher option price — so the algorithm correctly raises the guess to close the gap.

4. The inputs spot `S`, strike `K`, and rate `r` are unchanged, and time `T` has only *decreased* (which would push the put price slightly *down*). Yet the price rose ₹30. By elimination, the only BSM input that can explain a rising price is **volatility** — the market repriced the put to a higher implied volatility. Rising IV means the market now expects bigger future moves: uncertainty and **fear have increased**. A premium swelling while spot stands still is the classic fingerprint of rising IV — the expected *range* of outcomes widened even though its centre did not move, exactly what happens ahead of a feared event or shock.

5. The culprit is the **division by vega** in `IV_next = IV_now - (error) / vega`. For a deep ITM option vega is very small, so dividing the price error by a near-zero vega produces a huge correction that can fling the next guess to a negative or absurd value, and the iteration diverges. The safe fallback is **bisection**: start with a bracket known to contain the IV (e.g., 1% to 200%), test the midpoint, keep whichever half still brackets the answer, and repeat — each step halves the range. It cannot fail because, as long as the starting bracket contains the true IV (guaranteed by the no-arbitrage bounds), repeatedly halving an interval must converge on the answer; it is only slower than Newton-Raphson, not less reliable. Real systems use a hybrid: Newton for speed, bisection whenever a step misbehaves.

6. The lower no-arbitrage bound for a call is roughly its intrinsic value, `max(S - K * e^(-r*T), 0)`. With `S` = 24,000, `K` = 23,000 and the discount factor taken as ~1, the bound is `24,000 - 23,000 = ₹1,000`. The quoted price of **₹990 is *below* this ₹1,000 floor**, so it is **not legitimate** — it violates no-arbitrage (you could buy the call, exercise to capture the 1,000-point intrinsic value, and lock in a riskless ₹10 profit, ignoring frictions). Because the price sits outside the bounds, **no finite volatility can reproduce it**, so the implied volatility is undefined. In practice this signals a stale or erroneous quote on an illiquid deep-ITM strike, not a real trading opportunity — and it is exactly the kind of price the IV solver would reject rather than return a garbage number.
