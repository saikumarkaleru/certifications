# Chapter 30: Historical vs Implied Volatility

Volatility is the heartbeat of options. Strip away the jargon and an option is, at its core, a bet on *movement* — on how much the underlying will travel before expiry. Direction matters, but movement is the raw material. A call that needs Nifty to rise 200 points is worthless if Nifty is frozen, and priceless if Nifty is thrashing around in 300-point daily swings. So before you can judge whether any option is fairly priced, you have to answer one question: how much is this thing going to move? Everything else — the strikes, the premiums, the Greeks — flows from that.

There are two ways to measure movement, and the gap between them is one of the most reliable sources of edge in the entire options market. **Historical volatility** tells you how much the underlying *actually* moved in the recent past — it is a measured fact. **Implied volatility** tells you how much the market *expects* it to move in the future — it is a forecast, baked into option prices. This chapter teaches you to compute the first by hand, read the second off the screen, and — most importantly — to compare them. Because when you learn that implied volatility is usually *higher* than the realised volatility that follows, you have found the structural reason most professional option sellers stay in business.

## Core concepts

### Volatility is just the standard deviation of returns

In Chapter 25 we met volatility as "the annualised standard deviation of returns." Let us slow down and unpack exactly what that means, because in this chapter you are going to compute it yourself.

When a price moves from one day to the next, it produces a **return** — a percentage change. Some days the return is +0.8%, some days −1.2%, some days +0.1%. **Volatility measures how spread out those daily returns are.** If Nifty's daily returns cluster tightly around zero (lots of ±0.2% days), volatility is low. If they swing wildly (±2% days, then ±1.5% days), volatility is high. The statistical tool for "how spread out" is the **standard deviation**, and that is precisely what volatility is.

A subtle but important detail: professionals use **log returns**, not simple percentage returns. The log return for a day is:

`daily log return = ln(today's close / yesterday's close)`

where `ln` is the natural logarithm. For the small moves we see day to day, a log return is almost identical to the simple percentage change (a +1% day gives a log return of about +0.00995). We use logs for two clean mathematical reasons: log returns add up neatly over time, and they match the lognormal model of prices that sits underneath Black-Scholes (Chapter 19). For your purposes, just know: take the ratio of consecutive closes, take its natural log, and that is your daily return.

### Computing historical (realised) volatility

**Historical volatility** — also called **realised volatility** — is the standard deviation of those daily log returns, scaled up to an annual figure. The recipe has three steps:

1. **Compute the daily log returns** from a series of closing prices: `r = ln(close_today / close_yesterday)` for each day.
2. **Take the standard deviation** of those daily returns. This gives you the *daily* volatility — the typical size of a one-day wobble.
3. **Annualise** by multiplying by the square root of the number of trading days in a year. Indian markets (like most) have roughly **252 trading days** per year, so:

`historical volatility (annual) = standard deviation of daily log returns * sqrt(252)`

Why `sqrt(252)` and not 252? Because volatility scales with the *square root* of time, not time itself. Random daily moves partly cancel out rather than stacking up in a straight line — this is the same "square root of time" rule we saw with vega scaling as `sqrt(T)` (Chapter 25). If a single day has a standard deviation of 1%, a year of 252 such days does *not* have a standard deviation of 252%; it has roughly `1% * sqrt(252) ≈ 15.9%`. That square root is the bridge between a daily wobble and an annual figure, and it is the number quoted everywhere — "Nifty's realised vol is 14%" always means *annualised*.

A quick reference for the conversion, which is worth memorising:

- `sqrt(252) ≈ 15.87` — to annualise a daily standard deviation.
- To go the *other* way — from an annual IV to an expected daily move — divide by `sqrt(252)`: a 16% annual vol implies a typical daily move of about `16% / 15.87 ≈ 1%`. This is a professional's back-of-envelope trick: an India VIX of 16 means the market expects roughly 1% daily Nifty swings.

Historical volatility is always computed over a *window* — the last 10 days, 20 days, 30 days, or whatever you choose. A short window (10 days) reacts fast but is noisy; a long window (60 days) is smoother but slow to register a regime change. There is no single "correct" window; traders watch several. The key point is that historical volatility is **backward-looking** — it is a measured fact about the past, nothing more.

### Implied volatility: the market's forward-looking forecast

**Implied volatility (IV)** is the mirror image. Instead of measuring the past, it extracts the market's *expectation* of future movement from current option prices.

Recall the Black-Scholes formula (Chapter 20): feed it spot, strike, time to expiry, interest rate, and volatility, and it returns a fair option price. Five inputs in, one price out. But in the real market, the *price* is the thing you can see — it is right there on the option chain. Four of the five inputs (spot, strike, time, rate) are also observable. The only unknown is volatility. So we run the formula **backwards**: take the option's market price as given, and ask, "what volatility figure, plugged into Black-Scholes, would produce exactly this price?" That number is the implied volatility — the volatility *implied by* the price.

The crucial word is **forward-looking**. IV is not a measurement of anything that has happened. It is the market's collective bet on how much the underlying will move between now and expiry. When traders expect turbulence — an election, a Budget, an RBI decision — they bid premiums up, and IV rises. When they expect calm, premiums sag and IV falls. **India VIX** (Chapter 25) is simply the market's IV forecast for Nifty over the next 30 days, packaged into a single published index.

So the two numbers answer two different questions:

- **Historical volatility:** "How much *did* it move?" (a fact about the past)
- **Implied volatility:** "How much does the market think it *will* move?" (a forecast of the future)

### The volatility risk premium: IV usually beats realised

Here is the single most valuable insight in this chapter, and one of the most important structural facts in all of options trading.

**On average, implied volatility is higher than the realised volatility that subsequently shows up.** The market's forecast of future movement systematically *overstates* the movement that actually arrives. This persistent gap is called the **volatility risk premium** (VRP).

Concretely: if you measured India VIX every day for years and then measured how much Nifty actually moved over the following 30 days each time, you would find that VIX, on average, sat a few points *above* the realised volatility that followed. The forecast runs hot. Studies of Indian and global markets alike show this gap is real and durable — implied vol tends to trade at a premium of a few percentage points to realised vol most of the time.

Why does this happen? It is not market stupidity. It is **insurance pricing**, and it is rational:

- **Option sellers are insurers.** When you sell an option, you take on a one-sided risk: a large, fast move against you can cost far more than the premium you collected, and for naked options the loss is theoretically unbounded. Nobody takes on open-ended tail risk for free. Sellers *demand compensation* for bearing it, and that compensation shows up as premium priced above the statistically "fair" level — i.e., IV set above expected realised vol.
- **Buyers want protection and will overpay for it.** Fund managers, hedgers, and nervous retail traders buy puts (and calls) as insurance against crashes and to chase big moves. Like all insurance buyers, they routinely pay more than the actuarially fair price for peace of mind and convenience. That demand props IV up.
- **Crashes are asymmetric and terrifying.** Markets fall faster than they rise. The memory of sudden gap-downs (a Covid crash, an election shock) keeps a fear premium permanently baked into option prices, especially puts. Sellers must be paid to stand in front of that risk.

Put those together and you get a market where, most of the time, the people *selling* volatility collect more premium than the eventual movement justifies. **This is the structural edge professional option sellers lean on** — the options-market equivalent of an insurance company's underwriting profit: collect premiums that, on average, exceed the claims paid out.

But — and this is the non-negotiable caveat — it is an *edge*, not a *guarantee*. An insurer that under-reserves goes bankrupt in a single hurricane. The VRP is the reward for taking on tail risk, and that tail risk is real: every so often the move dwarfs the premium and the seller takes a brutal loss. It pays a steady stream of small wins in exchange for occasional large losses — positive *on average over time*, which is very different from *safe*. Most retail traders who blow up as option sellers mistook a structural edge for free money and sized as if the tail would never arrive. It always arrives eventually.

### Comparing IV and realised: are options cheap or expensive?

Now we can use both numbers together to do something genuinely useful: judge whether options are **cheap** or **expensive** right now. This is the comparison that separates a volatility trader from a coin-flipper.

The logic is simple. Implied volatility is what you *pay* (or receive) when you trade an option. Realised volatility is roughly what the option *delivers*. So:

- **IV much higher than recent realised vol → options are EXPENSIVE.** The market is charging a fat premium for movement that, judging by recent behaviour, may not materialise. This favours **sellers**: you are collecting rich premium relative to the actual movement. Think of a market bracing for an event with India VIX spiked to 22 while Nifty has been quietly grinding along at 11% realised — premiums are inflated, and the crush that follows (Chapter 25) hands the seller a profit.
- **IV much lower than recent realised vol → options are CHEAP.** The market is charging little for movement, but the underlying has actually been swinging hard. This favours **buyers**: you are paying a thin premium for an instrument that may well move enough to pay off. A long straddle bought when IV is unusually low relative to how much the index is genuinely thrashing is a classic "cheap volatility" trade.
- **IV roughly in line with realised vol (plus the usual small premium) → options are fairly priced.** No obvious volatility edge; trade on other grounds.

A common professional shorthand is the **IV/HV ratio** — implied vol divided by historical (realised) vol. Because of the volatility risk premium, this ratio normally sits a bit *above* 1.0 (IV usually runs hotter than realised). So you do not get excited just because IV exceeds HV — that is the default state. You look for *extremes*:

- IV/HV well above its usual range (say IV is 1.5x or 2x recent realised) → options are unusually expensive → lean toward selling.
- IV/HV below 1.0 (IV *cheaper* than what the market is actually delivering) → options are unusually cheap → lean toward buying.

The mistake to avoid: comparing IV to HV in a vacuum and concluding "IV > HV, therefore sell." Since IV almost *always* exceeds HV, that rule would have you selling every single day — straight into the tail-risk meat grinder. The signal is in the *deviation from the normal gap*, not the gap itself.

Professionals also use **IV rank** and **IV percentile**, which place today's IV against its own range over the past year. An India VIX of 16 means nothing in isolation; an India VIX of 16 sitting at the *95th percentile* of the past year tells you volatility is richly priced by its own historical standard. "Is IV high?" is always a *relative* question — relative to recent realised vol, and relative to IV's own history.

## Worked example (₹, Nifty)

Let us compute a rough historical volatility for Nifty by hand from a handful of daily closes, then compare it to India VIX to judge whether options are cheap or expensive.

**Setup.** Here are five consecutive daily closing levels for Nifty:

| Day | Close |
|-----|-------|
| 0   | 24,000 |
| 1   | 24,180 |
| 2   | 24,050 |
| 3   | 24,290 |
| 4   | 24,170 |

India VIX is currently quoted at **15%**. Are Nifty options cheap or expensive relative to how the index has actually been moving?

**Step 1 — Compute the daily log returns.** Using `r = ln(close_today / close_yesterday)`:

- Day 1: `ln(24180 / 24000) = ln(1.00750) ≈ +0.007472` (about +0.75%)
- Day 2: `ln(24050 / 24180) = ln(0.99462) ≈ -0.005391` (about −0.54%)
- Day 3: `ln(24290 / 24050) = ln(1.00998) ≈ +0.009936` (about +0.99%)
- Day 4: `ln(24170 / 24290) = ln(0.99506) ≈ -0.004953` (about −0.50%)

So our four daily returns are approximately: `+0.007472, -0.005391, +0.009936, -0.004953`.

**Step 2 — Find the standard deviation of these returns.** First the mean:

`mean = (0.007472 - 0.005391 + 0.009936 - 0.004953) / 4 = 0.007064 / 4 ≈ 0.001766`

Now the squared deviations from the mean:

- `(0.007472 - 0.001766)^2 = (0.005706)^2 ≈ 0.00003256`
- `(-0.005391 - 0.001766)^2 = (-0.007157)^2 ≈ 0.00005122`
- `(0.009936 - 0.001766)^2 = (0.008170)^2 ≈ 0.00006675`
- `(-0.004953 - 0.001766)^2 = (-0.006719)^2 ≈ 0.00004514`

Sum of squared deviations `≈ 0.00019567`. Dividing by `(n - 1) = 3` (the sample standard deviation, the standard choice for a small data set):

`variance = 0.00019567 / 3 ≈ 0.00006522`

`daily standard deviation = sqrt(0.00006522) ≈ 0.008076` (about 0.81% per day)

**Step 3 — Annualise with sqrt(252).**

`historical volatility = 0.008076 * sqrt(252) = 0.008076 * 15.87 ≈ 0.1282`

So Nifty's realised volatility over this short window is about **12.8% annualised**.

**Step 4 — Compare to India VIX and draw the conclusion.** Implied volatility (India VIX) is **15%**; realised volatility is about **12.8%**. The IV/HV ratio is `15 / 12.8 ≈ 1.17`.

IV sits about 2.2 points above realised, an IV/HV ratio of roughly 1.17. That is squarely in the *normal* range — exactly the kind of modest premium the volatility risk premium predicts. The market is charging a little more for future movement than the index has recently delivered, which is the default, healthy state of affairs. There is **no extreme edge** here in either direction: options are neither screamingly expensive nor a bargain. A seller is being paid the usual small premium for bearing tail risk; a buyer is paying the usual small markup. If India VIX had instead been sitting at 24% against this same 12.8% realised (a ratio near 1.9), *that* would flag richly priced options and tilt you toward selling. And if VIX were at 10% against 12.8% realised (ratio 0.78), options would look genuinely cheap and tilt you toward buying.

**A caveat on the method:** a four-return sample is far too small for a trustworthy estimate — real desks use 20 or 30 days, and even then realised vol jumps around. We used five closes so the arithmetic stays visible. The *process*, though, is exactly what professionals run on a full window: log returns, standard deviation, times `sqrt(252)`, then compare to IV.

## Common mistakes / risk note

- **Treating "IV > realised, so sell" as a money machine.** Because of the volatility risk premium, IV exceeds realised vol *most of the time* — that is the default, not a signal. Selling indiscriminately on that basis means perpetually short volatility into the exact tail events that wipe out years of small gains. The edge is in selling when IV is *unusually* rich relative to its own history and to recent realised, with defined risk and proper sizing — not in selling every day.
- **Confusing the two volatilities.** Historical vol is a measured fact about the past; implied vol is a forecast priced into options today. They are different numbers answering different questions. A high realised vol does *not* mean options are currently expensive — the realised move may already be over while IV has collapsed (or vice versa). Always compare the *current* IV to *recent* realised.
- **Forgetting to annualise — or annualising wrong.** A daily standard deviation of 0.8% is not "0.8% volatility"; the quoted figure is always annual, `0.8% * sqrt(252) ≈ 12.8%`. And it is `sqrt(252)`, not 252 — using the wrong scaling inflates your estimate roughly sixteen-fold. Square root of time, every time.
- **Using simple returns instead of log returns, or the wrong window.** For day-to-day moves the difference between simple and log returns is tiny, but be consistent and use logs. And remember the window matters: a 10-day realised vol can look very different from a 30-day one. Quote the window alongside the number.
- **Assuming the volatility risk premium makes selling safe.** It makes selling *positive on average* — which is emphatically not the same as safe. The VRP is compensation for real, occasionally catastrophic tail risk. Naked option selling carries large, sometimes unlimited, downside; the premium you collect is precisely the market's price for the chance that a Covid-style gap blows through your strike. Around 9 in 10 retail F&O traders lose money (SEBI studies), and over-leveraged option selling into the tail is one of the most common ways it happens. Size for the disaster, not the average day.

## Key takeaways

- **Historical (realised) volatility** measures how much the underlying *actually* moved: `historical vol = standard deviation of daily log returns * sqrt(252)`. It is backward-looking — a fact about the past.
- **Implied volatility** is the market's *forward-looking* forecast of future movement, backed out of current option prices by running Black-Scholes in reverse. India VIX is this forecast for Nifty over the next 30 days.
- **Annualise with `sqrt(252)`**, because volatility scales with the square root of time. The handy inverse: an annual IV divided by `sqrt(252) ≈ 15.87` gives the expected daily move (16% IV → about 1% daily swings).
- **The volatility risk premium**: IV is, on average, *higher* than the realised vol that follows, because option sellers demand compensation for tail risk and buyers overpay for protection. This is the structural edge option sellers lean on.
- **Compare IV to recent realised to judge cheap vs expensive.** IV far above realised → options expensive → favours sellers. IV below realised → options cheap → favours buyers. But because IV normally exceeds realised, look for *extremes* (and use IV rank/percentile), not the everyday gap.
- The VRP is an edge **on average**, not a guarantee. It pays small, steady wins for bearing occasional large losses — sell with defined risk and disciplined sizing, never as "free money."

## Practice problems

1. **Daily move from IV (numeric).** India VIX is quoted at 14%. Estimate the typical one-day move the market is pricing in for Nifty, in percentage terms. If Nifty is at 24,000, roughly how many points is that?

2. **Annualise a daily vol (numeric).** Over the last 20 trading days, the standard deviation of Bank Nifty's daily log returns is 0.011 (i.e., 1.1% per day). What is the annualised historical volatility?

3. **Cheap or expensive? (conceptual + numeric).** Nifty's 30-day realised volatility is 10%, and India VIX is sitting at 21% ahead of the Union Budget. Compute the IV/HV ratio. Are options cheap or expensive, and would this environment favour an option buyer or a seller? What is the main risk to that side?

4. **Why is IV usually above realised?** In plain English, explain the volatility risk premium and give two distinct reasons it exists. Why does this not make option selling "safe"?

5. **Compute historical vol from closes (numeric).** Three consecutive Nifty closes are 24,000, 24,240, and 24,100. Compute the two daily log returns, their sample standard deviation, and the annualised historical volatility using `sqrt(252) ≈ 15.87`.

6. **The default-gap trap (conceptual).** A trader says: "India VIX is 15% and Nifty's realised vol is 13%. IV is above realised, so I'll sell options every day to harvest the difference." What is wrong with this reasoning?

## Solutions

1. The expected daily move is the annual IV divided by `sqrt(252)`: `14% / 15.87 ≈ 0.88%` per day. At a spot of 24,000, that is roughly `0.0088 * 24000 ≈ 211 points`. So the market is pricing in typical daily Nifty swings of a bit under 1%, or about 200 points. (This is the one-standard-deviation daily move — Nifty will exceed it on roughly a third of days.)

2. Annualise by multiplying the daily standard deviation by `sqrt(252)`: `0.011 * 15.87 ≈ 0.1746`, or about **17.5% annualised** historical volatility. (Note we multiply by `sqrt(252)`, not 252 — the square-root-of-time rule.)

3. IV/HV `= 21 / 10 = 2.1`. Implied vol is more than double recent realised vol, so options are **expensive** — the market is charging a rich premium for movement that, by recent behaviour, far exceeds what the index has actually delivered. This favours the **seller**, who collects inflated premium and profits as IV crushes back down after the Budget. **The main risk:** the event delivers a *bigger* move than priced (or IV spikes even further before resolving). A short option into an event carries large — for naked options, theoretically unlimited — downside; the fat premium is precisely the market's price for that tail risk. Size for the disaster.

4. The **volatility risk premium** is the persistent tendency for implied volatility to sit *above* the realised volatility that actually follows — the market's forecast of future movement runs systematically hot. Two distinct reasons: **(a) Sellers demand compensation for tail risk.** Selling an option means taking on open-ended, occasionally catastrophic downside; no rational party does that for free, so they price premium above the statistically fair level. **(b) Buyers overpay for protection.** Hedgers and nervous traders buy options as insurance and, like all insurance buyers, routinely pay more than the actuarially fair price for peace of mind — that demand props IV up. (A third valid reason: crashes are fast and asymmetric, keeping a permanent fear premium in put prices.) It does **not** make selling safe because the premium is *compensation for real tail risk*: the VRP is positive *on average over time*, delivering many small wins punctuated by occasional large losses. An under-sized, over-leveraged seller is wiped out by the very tail event the premium was paying them to bear.

5. Daily log returns:
   - Day 1: `ln(24240 / 24000) = ln(1.01000) ≈ +0.009950`
   - Day 2: `ln(24100 / 24240) = ln(0.99422) ≈ -0.005797`

   Mean `= (0.009950 - 0.005797) / 2 = 0.004153 / 2 ≈ 0.002077`. Squared deviations from the mean: `(0.009950 - 0.002077)^2 = (0.007873)^2 ≈ 0.00006198` and `(-0.005797 - 0.002077)^2 = (-0.007874)^2 ≈ 0.00006200`. Sum `≈ 0.00012398`; divide by `(n - 1) = 1`: variance `≈ 0.00012398`. Daily standard deviation `= sqrt(0.00012398) ≈ 0.011135` (about 1.11% per day). Annualised: `0.011135 * 15.87 ≈ 0.1767`, or about **17.7%**. (With only two returns this is a wildly noisy estimate — illustrative of the method, not a usable figure.)

6. The flaw is that IV being above realised vol is the **normal, default state** of the market, not a signal. Because of the volatility risk premium, implied vol exceeds realised vol *most of the time* — a 15% IV against 13% realised is an entirely ordinary ~1.15 IV/HV ratio, the everyday premium sellers are paid for bearing tail risk. Selling "every day" on that basis means being perpetually short volatility, including straight into the rare tail events (crashes, gap moves, IV spikes) that erase years of small gains in a single session. The real edge is selling when IV is *unusually* rich — high relative to its own one-year history (IV rank/percentile) and well above recent realised — with defined-risk structures and disciplined position sizing. Harvesting the *everyday* gap indiscriminately, with naked positions, is how a large share of the ~9-in-10 losing retail F&O traders blow up.
