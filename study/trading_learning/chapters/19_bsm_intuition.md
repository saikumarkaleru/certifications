# Chapter 19: Black-Scholes-Merton I — The Intuition

In 1973, three economists wrote down a single equation that told traders, for the first time, what an option *should* cost — not as an opinion, but as a number forced on you by the rest of the market. It won a Nobel Prize and built the modern derivatives industry. Yet the most important idea behind it is not the formula at all. It is a startling claim: an option is not really a separate thing to be priced. It is a *recipe* — a self-adjusting mixture of the underlying and cash that, if you follow it precisely, reproduces the option's payoff exactly. And if you can build the option out of ingredients the market already quotes, then the fair price of the option is simply the cost of the ingredients. No guessing about the future required.

This chapter teaches that idea before any formula appears: why an option can be *replicated* by holding delta units of the underlying, why that replication lets the real-world expected return vanish from the answer (the "risk-neutral" trick), why prices are modelled as lognormal, and what the terms N(d1) and N(d2) really mean. The formula and a worked Nifty example come in the next chapter. Here we build the *understanding* that makes that formula obvious instead of magical.

## Core concepts

### The big idea: an option is a hedging recipe in disguise

Forget options for a second. Imagine you sell a friend a promise: "If Nifty closes above 24,000 next Thursday, I'll pay you whatever it is above 24,000." You have just sold a call. The terrifying question: how much should you charge, and how do you avoid being wiped out if Nifty rockets?

Here is the insight that started everything. Suppose that every moment you hold *some* quantity of Nifty futures against your promise. When Nifty is far below 24,000 your promise is nearly worthless, so you hold almost no futures. When Nifty is far above 24,000 you are almost certain to pay out the full difference, so you hold close to one full unit — every point Nifty rises is then matched by a point of hedge gain. In between, you hold a fraction.

This fraction — units of underlying held per option — is the **hedge ratio**, and it is exactly the Greek **delta** you met earlier. The fact Black, Scholes, and Merton proved is this: if you continuously adjust your holding to keep delta units of the underlying against each option, your hedged position has *no* exposure to market direction. Whatever Nifty does on a small move, your option loss is cancelled by your futures gain. You have manufactured the option's payoff out of stock and cash.

The chain of logic then snaps shut:

1. A perfectly delta-hedged option position is **riskless** over each instant.
2. A riskless position can earn only the **risk-free rate** — otherwise there is free money (arbitrage), and traders pounce until the gap closes.
3. Therefore the cost of running the hedging strategy *is* the fair price of the option. Pay more and you overpaid for something you could have built yourself; charge less and you handed a competitor an arbitrage.

The option's price is not a forecast. It is **the cost of the cheapest strategy that replicates it** — the whole soul of Black-Scholes.

### Replication: building an option from stock and cash

Let us make the recipe concrete without heavy maths. To replicate one Nifty call, at every instant you hold **delta units of the underlying** (the directional ingredient — it rises when Nifty rises, mimicking the call) plus **a borrowing or lending of cash** (the financing ingredient that pins the value to the right level).

As Nifty drifts, delta changes, so you must trade: buy more underlying as the market rises through the strike, sell as it falls. This constant tweaking is **dynamic hedging** (or **delta hedging**). In theory it is continuous; in real Indian markets a trader rebalances at intervals — every few minutes, or whenever delta drifts past a threshold.

This strategy is self-financing: once you put up the initial amount, all the rebalancing trades fund themselves, and the final value of the portfolio equals the option's payoff exactly. That initial amount — the seed capital the recipe needs — is the option's theoretical price. Black-Scholes computes that seed capital in closed form, so you do not have to simulate the whole hedging path to find it.

A vital consequence: the seller who delta-hedges is not betting on direction. They are *manufacturing* the option and selling it at cost-plus. Their real exposure is to whether the underlying moves *more or less* than the price assumed — that is, to volatility. This is why professionals say option trading is really **volatility trading**.

### Risk-neutral valuation: why the stock's expected return disappears

Now the part that shocks every newcomer. Ask a hundred investors what return Nifty will earn next year and you get a hundred answers — 8%, 12%, 15%. Surely a call's price depends on which is right? A bullish view should make calls worth more.

It does not. The expected return on the underlying **does not appear** in the option price at all. Here is the intuition. Because you hedge the direction away, your profit or loss no longer depends on which way Nifty goes — only on how *much* it moves. And if the answer cannot depend on the direction, it cannot depend on your forecast of the direction either. The optimist and the pessimist, if both hedge, must arrive at the *same* fair price — otherwise one is offering the other an arbitrage.

This licenses a beautiful shortcut called **risk-neutral valuation**. Since the true expected return drops out, we are free to pretend we live in an imaginary world where every asset is expected to grow at the **risk-free rate** (in India, think of a short government treasury bill, currently around 6-7%). This pretend world is the **risk-neutral measure**: nobody demands extra reward for taking risk, so all expected returns collapse to the risk-free rate. In that world the recipe for any option price becomes astonishingly simple:

`Option price = (expected payoff at expiry, in the risk-neutral world) discounted at the risk-free rate`

Or in words: **price = discounted expected payoff under the risk-neutral measure.** Take every possible expiry level of Nifty, weight each by its risk-neutral probability, multiply by the option's payoff there, average, and discount back to today at the risk-free rate. That average is the price.

Two cautions that matter enormously. First, the risk-neutral probabilities are **not** real-world odds — the risk-neutral chance that Nifty finishes above 24,000 is generally *not* the true chance, but a pricing device that builds in the market's risk preferences automatically; do not read them as forecasts. Second, risk-neutral valuation is a *consequence* of replication, not a separate assumption — it works **because** you can hedge, so where hedging breaks down (gaps, illiquidity, jumps), the clean pricing breaks down too.

### The lognormal model: how Black-Scholes imagines prices move

To compute that expected payoff, the model needs an assumption about how Nifty wanders between now and expiry. Black-Scholes makes the simplest sensible choice.

It assumes the *percentage returns* of the underlying are **normally distributed** — the familiar bell curve. Each instant, Nifty earns a tiny random return drawn from that curve, like a continuous stream of small coin-flips. The model works with returns, not rupee changes, because a 100-point move means something very different at Nifty 8,000 than at Nifty 24,000.

When normal returns compound continuously, the *price* follows a related distribution called **lognormal** — meaning the logarithm of the price is normally distributed. Two features are worth carrying in your head:

- **Prices cannot go negative.** A stock can fall 100% but no further. Normal returns, compounded, produce a price distribution that bottoms out at zero and never crosses it — matching reality, since Nifty cannot print a negative number.
- **The distribution is skewed to the right (a long upper tail).** Because gains compound, a run of good returns can carry the price very high, while a run of bad returns can only push it toward zero. The terminal-price picture is lopsided: a tall hump on the left, a long thin tail stretching right.

This lognormal "fan" of possible expiry levels is the canvas on which the option payoff is painted. The model also assumes **volatility** (sigma — the width of the return bell curve) is constant and that markets are frictionless (no transaction costs, continuous trading, one borrowing/lending rate). These are wrong in detail — volatility is not constant, India sees gaps around results and budgets, and STT and brokerage are real costs — but wrong in *understandable* ways. The chapters on the volatility smile and the Greeks are essentially the story of how traders patch these known flaws.

### What N(d1) and N(d2) actually mean

The Black-Scholes formula (next chapter) contains two terms, N(d1) and N(d2). The N(.) is the **cumulative normal distribution** — a function that turns a number into a probability between 0 and 1, the area under the bell curve up to that point. You do not need the algebra yet, but you should own the meaning of the two outputs, because traders quote them constantly.

**N(d2) is the risk-neutral probability that the option finishes in the money.** For a 24,000 call, N(d2) is roughly the pricing-world chance that Nifty closes above 24,000 at expiry. If N(d2) = 0.40, the model sees about a 40% risk-neutral chance the call expires with intrinsic value. This is why an at-the-money option, with roughly even odds either way, tends to have N(d2) near 0.5. (Again: this is a risk-neutral probability for pricing, not a real-world forecast.)

**N(d1) is the option's delta — the hedge ratio.** It tells you how many units of the underlying to hold per call to stay delta-neutral, and equivalently how much the option's price moves for a one-point move in Nifty. If N(d1) = 0.55, a one-point rise lifts the call by about 0.55 points, and you hold 0.55 units of futures per call to hedge it. Deep in-the-money, delta approaches 1 (the option behaves like the underlying); deep out-of-the-money, it approaches 0 (the option barely reacts).

So the call price has a clean economic reading: **expected money in (the asset, weighted by N(d1)) minus expected money out (the strike, weighted by N(d2))**. The formula is not an arbitrary cluster of symbols — it is "expected money in, minus expected money out," dressed in normal-distribution clothing.

### What the model actually gives a working trader

You will rarely trade purely off a Black-Scholes "fair value," because the real market sets the price and you back out the **implied volatility** instead. So why does every professional desk live and breathe it? Three gifts:

1. **A fair value to argue against.** The model turns a messy quote into one clean question: what volatility is this price implying, and will the world be more or less volatile than that? It converts price-picking into volatility-picking — a sharper, more tradeable judgement.
2. **The Greeks.** Differentiate the formula and you get delta, gamma, theta, vega, and rho — the sensitivities that tell you exactly how your position bleeds or blooms as the underlying, time, and volatility change. They are your risk dashboard, and they fall straight out of this one equation.
3. **A common language.** When a Mumbai desk quotes a Nifty option "at 13 vol," every other desk knows precisely what is meant, regardless of spot, strike, or days to expiry. Black-Scholes is the shared coordinate system the whole market uses to talk about value.

## Worked example (₹, Nifty)

Black-Scholes is famous for its formula, but its *logic* is just the delta-hedge recipe, and you can feel that logic with simple arithmetic. Let us watch a market-maker manufacture a Nifty call.

**Setup.** Nifty spot is 24,000. A market-maker sells one near-term 24,000 call (current lot size is about 25 units, but we reason per unit). The option is at-the-money, and from the chain its delta is roughly 0.50 — so N(d1) is about 0.50.

**The hedge.** To neutralise direction, the maker buys 0.50 units of Nifty (via futures) against the call they sold. Now consider a small move:

- Nifty rises 20 points to 24,020. The call they are short gains about delta * 20 = 10 points, a *loss* of 10 to the seller; their 0.50 units of futures gain 0.50 * 20 = 10. **Net: roughly zero.**
- Nifty falls 20 points to 23,980. The short call loses about 10 points, a *gain* of 10 to the seller; the futures hedge loses 10. **Net: again roughly zero.**

This is the engine of the whole theory: hedged, the maker does not care which way Nifty goes. But notice what they *do* care about. As Nifty rises the call's delta climbs above 0.50; as it falls, delta drops toward 0. To stay neutral the maker must **buy as Nifty rises and sell as it falls** — buying high and selling low, repeatedly, each round trip costing a little. That steady cost is the price of the option, and it grows when Nifty thrashes around more — which is, in arithmetic form, why the price depends on volatility and not on whether you are bullish.

**The risk-neutral reading.** Suppose the chain also tells us N(d2) is about 0.46. The model is saying there is roughly a 46% risk-neutral chance Nifty finishes above 24,000 at expiry. Valued as discounted expected payoff, the call is "about a 46% chance of finishing in the money, times an expected in-the-money amount, discounted back at roughly 6-7% per year for the few days to expiry" — which is exactly what the next chapter's formula computes. You can already *narrate* a Black-Scholes price: probability of finishing in the money, expected payoff if you do, discounted to today, with direction hedged away.

## Common mistakes / risk note

- **Reading N(d2) as a real-world probability.** N(d2) is the *risk-neutral* chance of finishing in the money. The true chance is usually different, because the risk-neutral world deliberately distorts the odds to bake in risk preferences. Do not treat "the market says there's a 46% chance Nifty closes above 24,000" as a forecast.
- **Believing the price forecasts direction.** The hardest idea to accept is that your bullish or bearish view does *not* enter the fair price. If you are bullish, the right expression is to *buy* the option, not to argue it is mispriced because you expect a rally. The model already hedged direction out.
- **Trusting the assumptions too literally.** Black-Scholes assumes constant volatility, no gaps, frictionless continuous trading, and one interest rate. Indian reality breaks every one: volatility spikes around RBI policy, the Budget, and results; Nifty gaps overnight; STT, brokerage, and spreads make rehedging costly; liquidity thins in far strikes. The model is a clean first draft, not gospel.
- **Forgetting that replication can fail when you need it most.** The whole edifice rests on delta-hedging continuously. In a fast gap — a circuit breaker, a shock open — you cannot rebalance and the "riskless" hedge stops being riskless. An option seller who has internalised "it's all hedged" can be wiped out by a single gap. Option *selling* carries large, sometimes undefined, risk precisely because the hedging assumption is an idealisation.
- **Over-respecting "fair value."** The market price is the real authority; the model is a translator. Use it to extract implied volatility and the Greeks, not to declare the market wrong.

## Key takeaways

- An option can be **replicated** by continuously holding delta units of the underlying plus cash; its fair price is simply the **cost of that hedging recipe**, forced by no-arbitrage.
- Because delta-hedging removes directional exposure, the underlying's **real-world expected return drops out** of the price — your bullishness or bearishness does not change fair value.
- This allows **risk-neutral valuation**: price = discounted expected payoff in a pretend world where everything grows at the risk-free rate. Those probabilities are pricing devices, not forecasts.
- Black-Scholes models the underlying as **lognormal** — normal percentage returns compounding into a right-skewed price distribution that can never go negative.
- **N(d2)** is the risk-neutral probability of finishing in the money; **N(d1)** is the **delta** (hedge ratio). The call price reads as "expected money in, minus expected money out."
- For a trader the model delivers a **fair value / implied vol** to trade against, the **Greeks** as a risk dashboard, and a **common language** ("quoting in vol"). Its idealised assumptions are exactly why the smile and Greeks chapters exist.

## Practice problems

1. **Conceptual.** Explain why two traders — one expecting Nifty to rise 15% this year, one expecting it to fall 5% — must agree on the fair price of the same Nifty call, assuming both can delta-hedge.

2. **Conceptual.** A friend says, "The Black-Scholes price of the 24,000 call tells me there's a 46% chance Nifty will close above 24,000, so I'll bet accordingly." What is wrong with this reasoning?

3. **Numeric (hedge ratio).** A market-maker is short 4 lots of a Nifty call with delta 0.45 (lot size 25). How many units of futures must they buy to be delta-neutral? If Nifty then rises 30 points, estimate the P&L on the option, on the hedge, and the net.

4. **Conceptual.** Why does Black-Scholes model *returns* as normal rather than modelling rupee price changes as normal? Give one concrete problem that modelling rupee changes directly would create.

5. **Conceptual.** A delta-hedged seller says, "I have no risk because I'm hedged." Identify two distinct ways this claim can fail in the Indian market.

6. **Numeric / intuition.** For a deep ITM Nifty call, N(d1) is about 0.95 and N(d2) about 0.93. For a deep OTM call, both are near 0.05. Explain what each pair tells you about (a) how to hedge and (b) the chance of finishing in the money.

## Solutions

1. Delta-hedging cancels the directional part of the payoff: once hedged, profit depends only on how *much* Nifty moves (volatility), not on direction. Since the fair price cannot depend on the direction of the move, it cannot depend on either trader's *forecast* of direction. If they disagreed on price, one would be handing the other a riskless arbitrage, so competition forces them to the same number despite opposite views.

2. The 46% figure is N(d2), a **risk-neutral** probability — a pricing construct from an imaginary world where all assets grow at the risk-free rate. It deliberately embeds the market's risk preferences and is generally *not* the real-world chance of the event. Betting on it as a true forecast confuses a valuation device with a prediction; the actual probability of Nifty closing above 24,000 is usually different.

3. The maker is short 4 lots * 25 units = 100 call units, each with delta 0.45, so position delta is -100 * 0.45 = -45 (short calls give the seller negative delta). To be neutral they buy **45 units** of futures. If Nifty rises 30 points: the short call position loses about 45 * 30 = **1,350 points** as the calls gain value; the 45-unit futures hedge gains 45 * 30 = **1,350 points**. Net is approximately **zero**. (For larger moves gamma changes delta and the cancellation is no longer exact — that residual is the seller's real exposure.)

4. A rupee-change model treats a 100-point move as equally likely at Nifty 8,000 and at 24,000, which is unrealistic — moves scale with the price level, so percentage returns are the natural, level-independent unit. A concrete failure: a normal distribution on price *changes* assigns positive probability to the price going **negative**, impossible for a stock or index. The lognormal model, built from normal *returns*, keeps prices strictly positive.

5. (a) **Gap / jump risk:** delta-hedging assumes continuous rebalancing, but Nifty can gap overnight or hit a circuit breaker on a shock (Budget, geopolitics, RBI surprise). During a gap you cannot trade, the hedge is stale, and a short option can lose far more than expected. (b) **Frictions and discrete rebalancing:** STT, brokerage, and spreads make constant rehedging costly, and real traders rebalance only periodically, so the hedge is never perfect — the residual, driven by gamma and by realised volatility exceeding the priced level, is genuine and sometimes large.

6. (a) **Hedging:** delta 0.95 means you hold about 0.95 units per call — the deep-ITM option moves almost one-for-one with the index, like the underlying itself; delta 0.05 means you hold almost nothing, as the deep-OTM option barely reacts. (b) **Finishing in the money:** N(d2) of 0.93 says the deep-ITM call has roughly a 93% risk-neutral chance of expiring in the money, while 0.05 gives the deep-OTM call about a 5% chance. The numbers move together because an option almost certain to pay off both hedges like the underlying and is very likely to finish in the money.
