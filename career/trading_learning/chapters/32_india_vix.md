# Chapter 32: India VIX — Reading the Market's Expected Move

Imagine you could walk up to the entire Nifty options market — every trader, every fund, every hedger pricing puts and calls right now — and ask one question: "How wild do you expect the next month to be?" India VIX is the market's collective answer, boiled down to a single number. It does not tell you which way the Nifty will go. It tells you how *far* the crowd thinks it might travel, up or down, over the coming month. When that number is low, the market is calm and bored. When it leaps, the market is frightened.

This single index is one of the most useful free signals a professional options trader has. It is the difference between selling premium when the market is paying you well for risk versus selling premium for peanuts right before a storm. In this chapter you will learn exactly what India VIX measures, how to turn it into an "expected move" in actual Nifty points, and how professionals use it to size positions, choose between buying and selling options, and time their entries.

## Core concepts

### What India VIX actually is

India VIX is a **volatility index** published by the National Stock Exchange (NSE). The term "volatility" just means how much prices swing around; high volatility means big moves, low volatility means small moves. India VIX is NSE's measure of the volatility the market *expects* in the Nifty 50 over the **next 30 calendar days**.

Three things make it special:

1. **It is forward-looking, not backward-looking.** If you take past Nifty returns and compute their standard deviation, you get *realized* (historical) volatility — what already happened. India VIX is different. It is *implied* volatility — it is reverse-engineered from the prices traders are *currently* paying for Nifty options. Option prices embed the market's forecast of future movement (recall that vega and implied volatility drive an option's price). India VIX squeezes that forecast out of the live order book. It is the market's expectation, with real money behind it.

2. **It is computed from the option order book, following the CBOE method.** NSE does not survey anyone. It takes the live bid-ask quotes of **near-month and next-month Nifty options** across a whole range of strikes — not just the at-the-money strike, but the out-of-the-money puts and calls too — and blends them into one number using the methodology pioneered by the Chicago Board Options Exchange (CBOE) for the original VIX. Because it uses many strikes, India VIX captures the price of the *entire* expected distribution, including the fear premium baked into far-out-of-the-money puts (this is related to the volatility skew you met earlier).

3. **It is quoted as an annualized percentage.** This is the part that trips up beginners. If India VIX reads **14**, it does not mean the market will move 14% next month. It means the market expects the Nifty's volatility, *annualized*, to be about 14% — roughly one standard deviation of return over a full year. To use it for a day or a month, you must scale it down, which we do below.

In short: **India VIX = the annualized, 30-day expected volatility of the Nifty, implied from live option prices.**

### The "fear gauge" interpretation

India VIX is nicknamed the "fear gauge" or "fear index" for good reason. When investors are scared, they rush to buy protective Nifty puts. That buying pressure pushes up option prices, which pushes up implied volatility, which pushes up India VIX. So a rising VIX is the fingerprint of fear spreading through the market.

Rough regimes to keep in your head (these are *typical* ranges, not hard rules — the market re-anchors over time):

- **Low: ~10 to 13.** Complacency. The market is calm, ranging, possibly grinding higher. Option premiums are cheap. This is often the *most dangerous* time to be complacent, because volatility can only stay low for so long.
- **Normal: ~13 to 18.** The everyday background level for the Nifty in recent years.
- **Elevated: ~18 to 22.** Nervousness. Often seen around big events — budgets, election results, major central-bank decisions.
- **High / fear: ~22 to 30.** Real anxiety. Sharp selloffs, gap-downs, uncertainty.
- **Crisis: 30 to 80+.** Panic. During the COVID crash of March 2020, India VIX spiked above **80** — a level that implied the market thought enormous daily swings were coming, and it was right.

A vital, well-documented pattern: **India VIX tends to spike when the Nifty falls and drift lower when the Nifty rises calmly.** We will return to this inverse relationship below. The practical takeaway is that India VIX is mean-reverting — extreme highs tend to collapse back toward the teens once panic fades, and extreme lows eventually give way to a shock. It does not trend forever in one direction the way a stock can.

### Converting India VIX into an expected move

This is the most useful skill in the chapter. India VIX is annualized, but you usually care about a single day or a single expiry (a week or a month). To rescale an annualized volatility to a shorter horizon, you divide by the square root of the number of those periods in a year. This is the **square-root-of-time rule**, and it works because variance (volatility squared) scales linearly with time, so volatility itself scales with the square root of time.

The two formulas every Indian options trader should memorize:

`Expected 1-day move (%) = India VIX / sqrt(252)`

`Expected 1-month move (%) = India VIX / sqrt(12)`

Why those numbers? There are about **252 trading days** in a year, so to go from annual to daily you divide by sqrt(252), which is about **15.87**. There are **12 months** in a year, so to go from annual to monthly you divide by sqrt(12), which is about **3.46**.

A quick mental shortcut professionals use: `sqrt(252)` is close to 16, so **daily expected move is roughly India VIX divided by 16**. If VIX is 16, expect about a 1% daily move. Easy to remember.

To turn a percentage move into actual Nifty points, multiply by the current Nifty level:

`Expected move in points = (expected move %) * Nifty level`

This expected move is a **one-standard-deviation** band. In plain terms, if the move is normally distributed, the Nifty should stay within plus-or-minus one expected move about **68%** of the time, within plus-or-minus two expected moves about **95%** of the time, and within three about **99.7%** of the time. (Real markets have fatter tails than the bell curve, so the true odds of a big move are a bit higher than these textbook numbers — never treat the band as a guarantee.)

### Worked conversions (do these in your head eventually)

Take **India VIX = 14**, **Nifty = 24,000**.

- Daily: 14 / 15.87 = **0.88%**. In points: 0.0088 * 24,000 = **about ±211 points** per day, one standard deviation.
- Monthly: 14 / 3.46 = **4.05%**. In points: 0.0405 * 24,000 = **about ±972 points**, call it **±1,000 points** over the month.

So at a VIX of 14 with Nifty at 24,000, the market is "pricing in" roughly a 210-point typical day and a 1,000-point typical month. If you are selling a strangle, those numbers tell you where to place your strikes. If the Nifty is sitting at 24,000 and someone offers to sell you a one-month 25,000 call, the market itself is saying a move to 25,000 (about +1,000 points, one standard deviation) is on the edge of "normal" — roughly a 16% chance of finishing beyond it on the upside.

Now raise fear: **India VIX = 28**, Nifty = 24,000.

- Daily: 28 / 15.87 = **1.76%** = about ±423 points.
- Monthly: 28 / 3.46 = **8.09%** = about ±1,942 points, nearly ±2,000 points.

Notice the expected move *doubled* when VIX doubled. That is the whole point: when VIX is high, the same strikes are far more likely to be breached, option premiums are richer, and your risk per lot is larger. The number is screaming "wider ranges ahead."

### How professionals use India VIX

**1. Position sizing.** Risk is proportional to the expected move, so smart traders shrink size when VIX is high and can afford more size when VIX is low — *for defined-risk strategies*. A simple discipline: keep your rupee risk roughly constant by scaling lots inversely with VIX. If you trade 10 lots at VIX 14, you might trade closer to 5 lots at VIX 28, because each lot now carries roughly double the expected swing.

**2. Choosing to buy versus sell premium.** This is the big one. Option *sellers* are short volatility — they profit when realized movement comes in below what was priced. Option *buyers* are long volatility — they profit when movement exceeds what was priced.

- When **VIX is very low** (say 10–12), options are cheap. The reward for selling premium is thin and the risk of a volatility spike against you is high. This environment favors *buyers* — buying cheap protection or cheap directional bets — and makes naked selling unattractive.
- When **VIX is very high** (say 28+), options are expensive. Sellers are being paid handsomely for risk, and because VIX mean-reverts, a drop back toward normal hands sellers a double tailwind (volatility falling *and* time decay). This environment favors *premium sellers* — but only those who can survive the wild swings while the storm lasts.

The professional mantra: **sell premium when volatility is high and expected to fall; buy premium when volatility is low and expected to rise.** India VIX is your gauge for which regime you are in.

**3. Timing entries.** Because VIX is mean-reverting, extreme readings are signals. A VIX spike to 30+ during a panic is often a *better* time to start scaling into premium-selling strategies (carefully, in small size) than a sleepy VIX of 11. Conversely, a multi-month low in VIX is a warning to take profits on short-premium books and consider owning some cheap protection before the inevitable shock. Many traders also watch VIX *ahead of known events* — it usually rises into budgets and election counts (the market pre-pays for the expected jump) and then collapses the moment the event passes. That post-event VIX collapse is the famous "volatility crush" that punishes event-driven option buyers.

### The inverse relationship between India VIX and the Nifty

India VIX and the Nifty usually move in **opposite directions**, and the relationship is asymmetric:

- When the Nifty **falls sharply**, India VIX **jumps** — often violently. Fear buying of puts, panic, and uncertainty all spike implied volatility.
- When the Nifty **rises**, it tends to do so slowly and calmly, so India VIX **drifts down** gently.

This is why VIX is a fear gauge and not a "greed gauge" — markets fall faster than they rise, so volatility is tied to downside more than upside. Two practical consequences:

- A **long Nifty position is implicitly short volatility**, and buying puts (long volatility) is a natural hedge that pays off exactly when you need it — during crashes when VIX explodes.
- A sudden VIX spike *without* an obvious news cause can be an early warning that informed money is paying up for protection. Many traders treat a fast VIX move as a heads-up to tighten risk, even before price confirms.

A caution: the inverse relationship is a strong *tendency*, not a law. VIX and Nifty can occasionally rise together (for example, a sharp rally driven by short-covering and frantic call buying). Use it as context, not as a mechanical trading signal.

## Worked example (₹, Nifty)

**Setup.** It is a calm market. The Nifty is at **24,000**, India VIX reads **12**, and there are **30 days** to the monthly expiry. You are considering selling a one-month at-the-money straddle (sell the 24,000 call and the 24,000 put — a short-volatility bet that the Nifty stays roughly put). Suppose the combined premium you collect is **₹560** per unit. The Nifty lot size is **75**, so one straddle collects 560 * 75 = **₹42,000**.

**Step 1 — Expected monthly move.**
`Expected 1-month move % = 12 / sqrt(12) = 12 / 3.464 = 3.46%`
In points: 0.0346 * 24,000 = **±831 points**. One standard deviation says the Nifty is about 68% likely to finish the month between roughly **23,170 and 24,830**.

**Step 2 — Compare to your breakevens.** A short straddle that collects ₹560 has breakevens at 24,000 ± 560 = **23,440 and 24,560**. That ±560-point band is *narrower* than the ±831-point expected move. Translation: the market expects to swing more than the premium protects you for. At a low VIX of 12, you are being paid too little for the risk you would carry. The straddle is a poor sell here.

**Step 3 — Re-run at high VIX.** Now imagine a fearful market: Nifty still 24,000 but **India VIX = 24**, and the same straddle now pays **₹1,150** (premium roughly doubled with volatility).
`Expected 1-month move % = 24 / 3.464 = 6.93%` = **±1,663 points**.
Breakevens: 24,000 ± 1,150 = **22,850 and 25,150**, a ±1,150-point band — still narrower than the ±1,663 expected move, but you are now collecting ₹1,150 * 75 = **₹86,250** per straddle. The richer premium plus the strong odds that VIX will mean-revert downward (helping the seller via falling volatility) make this a far more attractive *sell* than the VIX-12 case — provided you size small and can survive the swings.

**Step 4 — Daily risk check.** At VIX 24, the expected *daily* move is 24 / 15.87 = **1.51%** = about **±363 points**. Selling that straddle means a single ordinary day could move the Nifty 360 points against you. Knowing this *before* you enter is exactly how you size the position so one bad day does not wreck the account.

The lesson: the *same strategy* flips from unattractive to attractive purely based on where India VIX sits, and the expected-move math makes that visible in seconds.

## Common mistakes / risk note

- **Reading VIX as a percentage move.** A VIX of 15 does **not** mean "15% move." It is annualized; you must divide by sqrt(252) for a day or sqrt(12) for a month. Skipping this is the single most common beginner error.
- **Treating the expected move as a ceiling.** The ±1 standard-deviation band is breached about 32% of the time, and real markets have fat tails — crashes are bigger and more frequent than the bell curve predicts. The expected move is a *typical* move, never a *maximum*. March 2020 obliterated every "normal" band.
- **Selling premium just because VIX is high.** High VIX means rich premiums *and* violent ranges. Many traders blow up by selling into a spike that keeps spiking. High VIX favors sellers only with small size, defined risk where possible, and the stomach to hold through chaos. Remember the honest base rate: roughly **9 in 10 retail F&O traders lose money** (per SEBI studies), and a large share of that damage comes from mis-sizing option selling during volatile regimes.
- **Buying options in a low-VIX trance without an edge.** Cheap options are cheap for a reason — the market is calm. Long options still bleed theta daily and usually expire worthless. Low VIX improves your *entry price*, not your *direction*.
- **Trusting the inverse relationship blindly.** VIX usually rises when Nifty falls, but not always. Do not build a system that mechanically shorts one against the other.
- **Ignoring the event-driven volatility crush.** Buying options the day before a budget or election result, when VIX is already elevated, often loses money even if you guess the direction right, because VIX collapses after the event and craters your option's value.

## Key takeaways

- India VIX is a single number published by NSE: the **annualized, 30-day expected volatility of the Nifty**, computed from live near-month and next-month Nifty option prices using the CBOE method.
- It is the market's **fear gauge** — low (~10–13) signals complacency, high (~20+) signals fear, and crisis spikes can reach 30–80+ (over 80 in March 2020).
- Convert it to an **expected move**: daily ≈ `VIX / sqrt(252)` (≈ VIX/16) and monthly ≈ `VIX / sqrt(12)`; multiply by the Nifty level for points. VIX 14 at Nifty 24,000 ≈ ±0.88%/day and ±1,000 points/month.
- The expected move is a **one-standard-deviation band** (~68% containment), not a maximum — markets have fat tails.
- Use VIX to **size positions** (smaller when VIX is high), **choose buying vs selling** (buy when cheap/low, sell when rich/high and likely to fall), and **time entries** around its mean-reverting behavior and known events.
- India VIX and the Nifty are usually **inversely related and asymmetric** — VIX spikes hard on selloffs, drifts down on calm rallies.

## Practice problems

1. **(Conceptual)** A friend sees India VIX at 16 and says, "The market expects the Nifty to move 16% next month." In one or two sentences, correct him and state what 16 actually implies for the *monthly* expected move.

2. **(Numeric)** India VIX is 19 and the Nifty is at 24,500. Compute the expected 1-day move in both percent and points. Use sqrt(252) ≈ 15.87.

3. **(Numeric)** With India VIX at 21 and the Nifty at 22,000, compute the expected 1-month move in percent and points, and state the approximate ±1 standard-deviation price range for the coming month. Use sqrt(12) ≈ 3.464.

4. **(Application)** You run a short-strangle book. India VIX has just collapsed from 26 to 11 over three weeks of a calm rally. Based on the volatility regime alone, should you be *more* eager or *less* eager to put on new short strangles, and why? What alternative does a low VIX favor?

5. **(Numeric / sizing)** You normally trade 12 lots when India VIX is 13. Using the rule of keeping rupee risk roughly constant by scaling lots inversely with VIX, how many lots should you trade when VIX jumps to 26?

6. **(Conceptual)** The Nifty gaps down 3% on global news and India VIX leaps from 14 to 27 in a single session. Explain why VIX rose so sharply, and what this tells a trader holding a large long-Nifty futures position about their implicit volatility exposure.

## Solutions

1. India VIX is an **annualized** volatility, not a one-month move. A reading of 16 implies an expected *monthly* move of about `16 / sqrt(12) = 16 / 3.464 = 4.6%`, not 16%. (The 16% figure would be the rough one-standard-deviation move over a *full year*.)

2. Expected 1-day move % = `19 / 15.87 = 1.197%`, about **1.2%**. In points: `0.01197 * 24,500 = 293 points`, about **±293 points** for a typical day (one standard deviation).

3. Expected 1-month move % = `21 / 3.464 = 6.06%`. In points: `0.0606 * 22,000 = 1,334 points`, about **±1,334 points**. The ±1 standard-deviation range is therefore roughly **20,666 to 23,334**, where the Nifty is expected to finish about 68% of the time over the coming month.

4. You should be **less** eager to put on new short strangles. At VIX 11 the premiums you collect are thin, you are poorly compensated for the risk, and volatility is far more likely to *rise* from such a low base (mean reversion), which hurts short-volatility positions on two fronts — rising VIX and potentially larger realized moves. A low VIX favors **buyers** of premium: cheap long options or cheap protective puts to hedge, since you are paying very little for potential upside in volatility.

5. Inverse scaling means lots ∝ 1/VIX. New lots = `12 * (13 / 26) = 12 * 0.5 = 6 lots`. When VIX doubles, halve the position size so each lot's doubled expected move keeps total rupee risk roughly constant.

6. India VIX rose sharply because a 3% gap-down triggers fear: investors rush to buy protective Nifty puts, demand for options spikes, implied volatility (and therefore VIX) jumps — and because volatility is asymmetric, it rises far faster on a fall than it would drift down on an equivalent rally. For the trader holding a large long-Nifty futures position, this is a reminder that **being long the Nifty is implicitly being short volatility**: the position loses exactly when VIX explodes. A natural hedge is to own some long puts (long volatility), which gain value precisely during these VIX spikes and cushion the drawdown.
