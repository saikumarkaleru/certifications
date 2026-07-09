# Chapter 26: Rho & the Minor Greeks

Every option price secretly contains an interest rate. It is buried in the background, doing quiet work, and most retail traders never notice it — and for the weekly Nifty options they trade, they are right not to. But the rate is there, and on a long-dated option or a large professional book it stops being a rounding error and starts mattering in rupees. **Rho** is the Greek that measures this hidden sensitivity to interest rates: how much an option's premium moves when rates shift.

This chapter does two things. First, it gives you rho — what it is, why calls and puts respond in opposite directions, and why it is the least urgent Greek for a short-dated Indian index trader yet a real one for long-dated positions and the cost-of-carry that links options to futures. Second, it takes you on a guided tour of the *other* lesser Greeks — vanna, volga, charm, epsilon — at an intuition level. These are the second-order Greeks a professional running a large book watches carefully even though a retail trader almost never computes them directly. Knowing they exist, and what each whispers about your risk, separates a trader who merely uses the Greeks from one who understands them.

## Core concepts

### Rho: the interest-rate Greek

Recall from the pricing chapters that an option is valued off a **forward price**, not today's spot. To value a call, the model asks: where is the underlying *likely to be* at expiry, and what is the present value of the expected payoff? Both of those steps involve the risk-free interest rate. The rate pushes the forward up (carrying money forward costs interest) and it discounts the future payoff back to today. Change the rate, and both effects shift the premium slightly.

**Rho** is defined as the change in an option's price for a **1 percentage-point (100 basis-point) change in the risk-free interest rate**, holding everything else constant.

`rho = change in option premium per 1.00% change in interest rate`

The sign is the first thing to learn, and intuition gets it right:

- **Calls have positive rho.** A higher interest rate lifts the forward price of the underlying (the market "expects" it higher in a risk-neutral sense because holding cash earns interest). A higher forward makes a call — the right to *buy* — more valuable. So when rates rise, calls gain.
- **Puts have negative rho.** A put is the right to *sell*. There are two ways to see why higher rates hurt it. First, the same higher forward makes the right to sell at a fixed strike less attractive. Second, and more concretely: a put's eventual payoff is money you receive in the future, and a higher discount rate shrinks the present value of that future cash. So when rates rise, puts lose.

A clean way to remember it: **rates up — calls up, puts down.** Rates behave a little like a gentle tailwind pushing the whole distribution of future prices upward.

### Why rho is the "quiet" Greek for Indian weekly and monthly options

Here is the crucial practical point for an NSE index trader. Rho scales with **time to expiry**. Interest is a per-year effect; the longer your option lives, the more time that interest has to compound and discount, and the bigger rho becomes. The shorter the life, the smaller rho is — almost vanishingly so for a weekly option.

The interest rate moves the value by roughly "rate times time." For a Nifty weekly option with 4 days to expiry, the time fraction is about `4/365 ≈ 0.011` of a year. Even a *full* 1% jump in rates — which essentially never happens overnight — gets multiplied by that tiny fraction, so the premium barely twitches. For a monthly option the effect is still small. Compare this to:

- **Theta**, which on a weekly option can eat several rupees a *day*.
- **Vega**, which can move the premium tens of rupees on a single India VIX swing.
- **Delta and gamma**, which dominate everything intraday.

Against those forces, rho on a short-dated Indian option is a whisper in a storm. A weekly Nifty straddle can swing thousands of rupees from a vol spike while rho contributes a few paise. This is exactly why most retail F&O traders — who live almost entirely in weekly and monthly expiries — can safely ignore rho day to day. It is not that rho is fake; it is that its arena is *long horizons*, and the Indian retail crowd does not trade there.

### Where rho actually bites: long-dated options and the cost-of-carry

Rho earns its keep in two places.

**1. Long-dated options (LEAPS-style).** In the US, traders buy options expiring a year or two out, called LEAPS. India's listed long-dated index options are far less liquid, but the *principle* is the same: stretch the expiry to one or two years and rho becomes a genuine, first-order risk. A one-year ATM option can have a rho large enough that a serious shift in the RBI's policy rate visibly moves its price, so anyone holding long-dated options or multi-year structured products must hedge rate risk deliberately.

**2. The cost-of-carry baked into futures.** This is the channel through which interest rates reach *every* Indian index trader, even weekly ones — just indirectly. An index futures price is not the spot; it is the spot grown forward by the cost of carry:

`Futures ≈ Spot * (1 + (r - q) * T)`

where `r` is the interest rate and `q` is the dividend yield of the index. This is why Nifty futures usually trade at a small **premium** to spot Nifty: the interest cost of carrying the basket exceeds the dividends it pays, so the forward sits above spot. Options are priced off this forward. So when you trade options, you are *already* trading something that contains an interest-rate assumption — you just see it as the futures premium rather than as rho. When carry changes (rates move, or dividends bunch up around earnings season), the futures basis shifts, and your options reprice with it. Rho is the formal name for the part of that repricing driven by the rate itself.

### A tour of the other minor Greeks

The first-order Greeks — delta, theta, vega, rho — tell you how the premium responds to spot, time, vol, and rates. But each of *those* sensitivities itself changes as conditions change. The **second-order Greeks** measure that. A retail trader rarely touches them; a desk running thousands of contracts watches them because they describe how the whole book's risk profile mutates when the market moves. Here they are at the intuition level.

**Gamma** (already met in its own chapter) is the headline second-order Greek: how delta changes as spot moves. The ones below are its lesser-known cousins.

#### Vanna — how delta and vega bleed into each other

**Vanna** answers a two-sided question that is really one question: *how does my delta change when volatility moves?* — which is identical to asking *how does my vega change when spot moves?* (The two are mathematically the same number.)

Why care? Imagine you have hedged a position to be delta-neutral. Then India VIX spikes. Vanna tells you your delta no longer sits at zero — the volatility move alone shifted it — so your "neutral" hedge has quietly developed a directional lean. Vanna is especially important around **skew** (Chapter on volatility skew): because OTM puts carry richer implied vol than OTM calls, a falling market that simultaneously raises vol creates a vanna effect that desks must manage. For a big book, ignoring vanna means your hedges drift exactly when the market is most stressed.

#### Volga (vomma) — how vega itself changes with volatility

**Volga**, also called **vomma**, measures how **vega changes when volatility changes**. Vega is your exposure to vol; volga is the *curvature* of that exposure — the "gamma of vega."

The intuition: a position can be vega-neutral at today's vol level but still make or lose money on a *large* vol move, because vega itself shifts as vol travels. Long-volga positions (often built from OTM strangles) *gain* vega as vol rises, so they profit more than a linear vega estimate suggests during big volatility blow-ups — which is why they are popular as tail hedges. Volga is the Greek of "vol of vol." On an Indian book, a desk holding far-OTM Nifty options through an event (a budget, an election result, an RBI surprise) is implicitly long volga.

#### Charm — how delta decays with time

**Charm** (also called *delta decay* or *delta bleed*) measures how **delta changes simply because time passes**, with spot and vol held still.

This one has a very practical flavour, especially in India's weekly-expiry world. Suppose you sold an OTM Nifty call and hedged its delta on Tuesday. By Thursday morning, even if Nifty has not moved at all, that option is closer to expiry, so its delta has drifted (an OTM option's delta bleeds toward zero as expiry nears; an ITM option's toward one). Charm quantifies that overnight drift. A desk that hedges at Thursday's close and comes back Friday can find its book has developed a delta purely from the calendar — charm is largest for near-expiry, near-the-money options, which is *exactly* the bread and butter of Indian weekly trading. Professionals running expiry-week books pay real attention to charm because it tells them how much their hedge will rot overnight from time alone.

#### Epsilon — sensitivity to dividends

**Epsilon** (sometimes called *psi*) measures how an option's price responds to a change in the **dividend yield** of the underlying.

Higher dividends lower the forward price (cash paid out reduces what holders carry forward), so — mirroring rho — **calls fall and puts rise when expected dividends increase.** For Nifty and Bank Nifty *index* options, dividends are spread across many constituents and are reasonably smooth, so epsilon is usually minor. It matters more for **single-stock options** around a known dividend or special payout, and it is one reason stock-option forwards (and their put-call parity) must explicitly account for the dividend. For the index trader, epsilon mostly shows up indirectly through the `q` term in the cost-of-carry above.

### Why a professional watches these and a retail trader usually does not

A retail trader holds a handful of contracts in one or two expiries. Delta, theta, and vega explain almost all of their P&L; the rest is noise smaller than the bid-ask spread. Computing vanna or volga for a two-lot weekly straddle would be like weighing a truck to find the dust on it.

A **professional running a large book** is in a different regime. When you are net short tens of thousands of options across strikes and expiries, the second-order Greeks describe how your *entire risk picture reshapes* as the market moves — and those reshapings, multiplied across a huge position, become real money. Vanna tells the desk how its delta hedge will fail in a vol spike; volga warns it about the convexity of its vol exposure in a crash; charm tells it how much to re-hedge overnight into expiry; rho and epsilon keep the long-dated and dividend-sensitive corners honest. None of these is optional at scale.

### How interest rates feed put-call parity and the forward

Rho's logic is the same logic that drives **put-call parity** (Chapter 17). Parity for European options ties a call and a put at the same strike and expiry together through the present value of the strike:

`Call - Put = Spot - K * e^(-r*T)`  (or, with dividends, `Spot * e^(-q*T) - K * e^(-r*T)`)

Look at the `K * e^(-r*T)` term: that is the strike discounted at the interest rate. Raise `r`, and `e^(-r*T)` shrinks, so `K * e^(-r*T)` falls, so `Call - Put` rises — the call gets relatively more valuable and the put less. That is *exactly* the rho signs we derived (calls up, puts down) appearing inside the parity relation. Rho is not a separate fact bolted onto options; it is the same interest rate that defines the forward and ties calls to puts. The forward price `F = Spot * e^((r - q)*T)` is where everything starts, and rho and epsilon are simply how the option price reacts when the two ingredients of that forward — the rate `r` and the dividend `q` — move.

## Worked example (₹, Nifty)

Let us make rho concrete by comparing a short-dated Nifty option with a long-dated one. Assume Nifty spot is **24,000**, we look at the **ATM 24,000 call**, implied volatility is **14%**, the dividend yield is negligible, and the interest rate is **7%**. We ask: *how much does the call's premium change if rates rise by a full 1 percentage point, from 7% to 8%?*

**Step 1 — The short-dated weekly option (7 days to expiry).**
Time to expiry `T = 7/365 ≈ 0.0192` years. The rho of an ATM call is roughly proportional to `K * T` (and a probability factor near 0.5 for ATM). A back-of-envelope estimate:

`rho per 1% ≈ K * T * 0.5 / 100 ≈ 24000 * 0.0192 * 0.5 / 100 ≈ ₹2.3`

So a full 1% jump in rates lifts this weekly call's premium by only about **₹2 to ₹3**. Set that against the call's own premium of roughly ₹130–150 and its daily theta of perhaps ₹15–20: the entire 1% rate shock is worth a fraction of a single day's time decay. On one lot (Nifty lot size currently around 75 units), that is a couple of hundred rupees from a once-in-a-cycle rate move — utterly swamped by ordinary intraday delta and vega swings. **Conclusion: rho is negligible here.**

**Step 2 — The long-dated option (2 years to expiry).**
Now stretch the same ATM 24,000 call to `T = 2` years. Rho scales with `T`, so it grows by a factor of about `2 / 0.0192 ≈ 104`:

`rho per 1% ≈ 24000 * 2 * 0.5 / 100 ≈ ₹240`

A full 1% rate move now shifts the premium by roughly **₹240** — and even a more realistic 0.25% RBI move is about ₹60. On one lot of 75, a 1% shift is about `240 * 75 ≈ ₹18,000` of P&L from interest rates alone. That is no longer noise; it is a position you would actively hedge.

**Step 3 — The lesson.** Same index, same strike, same rate shock. On the weekly option rho is ₹2–3; on the two-year option it is ~₹240 — about a hundredfold larger, exactly tracking the hundredfold increase in time to expiry. Rho is not weak or strong in itself; it is **proportional to how long your option lives.** Indian retail trades short, so retail can ignore rho. Stretch the horizon and rho walks straight to the front of the room.

![Figure: rho vs spot](figs/rho.png)

The figure plots rho against spot price. Notice that the call's rho is positive everywhere and the put's negative everywhere, that both grow in magnitude as you go deeper in-the-money (where the option behaves more like the forward, fully exposed to the discounting of the strike), and that the whole curve is far flatter for a short-dated option than for a long-dated one.

## Common mistakes / risk note

- **Thinking rho is irrelevant, full stop.** For weekly and monthly index options it is nearly so — but the moment you hold long-dated options, or trade single stocks around big dividends, or run a structured product, rho and epsilon become real. Dismiss them by habit and you will be blindsided exactly where they live.
- **Forgetting that rates reach you through the futures basis.** Even a pure weekly trader is exposed to interest rates via the cost-of-carry premium of Nifty futures over spot. When that basis shifts, your synthetic and hedged positions reprice. You felt rho whether or not you named it.
- **Believing a delta-neutral hedge stays neutral.** Vanna and charm guarantee it will not: a vol spike (vanna) or simply the passage of a day (charm) moves your delta even with spot pinned. On expiry-week Indian books, charm-driven overnight delta drift is a classic way a "hedged" seller wakes up directional.
- **Mistaking vega-neutral for vol-safe.** Volga means a vega-neutral book can still lose badly in a *large* vol move. Tail events around budgets, elections, and RBI surprises are precisely volga events.
- **Over-engineering a tiny book.** The opposite error: a retail trader computing vanna for two lots is wasting effort on a number smaller than the spread. Match the Greek to the size. The minor Greeks are tools for scale, not for everyone.

## Key takeaways

- **Rho** measures premium change per 1% move in interest rates: **calls positive, puts negative** (rates up — calls up, puts down).
- Rho scales with **time to expiry**, so it is **tiny for Indian weekly/monthly options** and **material only for long-dated (LEAPS-style) positions**.
- Interest rates still reach every index trader through the **cost-of-carry** that sets the futures premium over spot and prices every option's forward.
- **Put-call parity** contains the rate directly in `K * e^(-r*T)` — rho is just that term in motion.
- The minor second-order Greeks: **vanna** (delta vs vol / vega vs spot), **volga/vomma** (vega vs vol), **charm** (delta decay with time), **epsilon** (dividend sensitivity).
- A **professional running a large book** watches all of these because they describe how the whole position's risk reshapes; a **retail trader** rarely needs them directly.
- Match the Greek to the size and the horizon: short and small means delta/theta/vega dominate; long and large means rho and the second-order Greeks earn their place.

## Practice problems

1. **Sign check.** Interest rates in India rise sharply after an RBI policy meeting. All else equal, what happens to the price of an ATM Nifty *call*? To an ATM Nifty *put*? Explain the intuition in one line each.

2. **Why so small?** A trader holds a 5-day Nifty 24,000 call and worries about an upcoming RBI decision. Explain in plain English why rho is almost certainly the *least* of their concerns, naming the two Greeks that actually dominate their P&L over those 5 days.

3. **Scaling with time (numeric).** Using the rough estimate `rho per 1% ≈ K * T * 0.5 / 100` for an ATM call with K = 24,000, compute the approximate rho for (a) a 14-day option and (b) a 1-year option. By what factor does it grow?

4. **Name the Greek.** A desk is delta-hedged at Thursday's close on an expiry-week Nifty book. Friday morning, with Nifty unchanged overnight, the book shows a non-zero delta. Which minor Greek explains this, and why is it large in expiry week?

5. **Carry and the basis.** Nifty spot is 24,000 and one-month Nifty futures trade at 24,090. Using `Futures ≈ Spot * (1 + (r - q) * T)`, and assuming dividend yield q ≈ 1%, roughly what annualised interest rate `r` is implied? (Take T = 1/12.)

6. **Conceptual — volga.** Two traders are both vega-neutral going into the Union Budget. One holds far-OTM Nifty strangles; the other holds an ATM calendar spread. India VIX then doubles. Why might their P&L differ sharply despite both starting vega-neutral?

## Solutions

1. **Call rises; put falls.** A higher rate lifts the forward price of Nifty (cash carried forward earns interest in the risk-neutral world), which makes the right to *buy* — the call — more valuable. The same higher forward, plus the heavier discounting of the put's future payoff, makes the right to *sell* — the put — less valuable. So calls have positive rho, puts negative.

2. **Because rho scales with time, and 5 days is almost no time.** The rate effect is multiplied by `T = 5/365 ≈ 0.014` of a year, so even a full 1% rate jump moves the premium by only a rupee or two. Over those 5 days the P&L is dominated by **theta** (the option is deep in the steep part of the decay curve, losing several rupees a day) and **vega** (a VIX move around the RBI event can swing the premium by tens of rupees). Rho is a whisper against both.

3. Using `rho ≈ 24000 * T * 0.5 / 100 = 120 * T`:
   - (a) 14 days: `T = 14/365 ≈ 0.0384`, so `rho ≈ 120 * 0.0384 ≈ ₹4.6`.
   - (b) 1 year: `T = 1`, so `rho ≈ 120 * 1 = ₹120`.
   - Growth factor ≈ `120 / 4.6 ≈ 26`, which is just the ratio of the times (`365/14 ≈ 26`). Rho grows in direct proportion to time to expiry.

4. **Charm** (delta decay / delta bleed) — the change in delta from the passage of time alone, with spot and vol unchanged. Overnight, the options aged about a day, so their deltas drifted (OTM deltas toward zero, ITM toward one), leaving the previously neutral book with a net delta. Charm is **largest for near-expiry, near-the-money options**, which is precisely the inventory of an Indian expiry-week book, so the overnight drift can be substantial and must be re-hedged Friday morning.

5. The futures premium is `24090 / 24000 - 1 = 0.00375` over one month. Setting this equal to `(r - q) * T` with `T = 1/12`:
   `(r - q) * (1/12) = 0.00375`, so `r - q = 0.045 = 4.5%`. With `q ≈ 1%`, the implied rate is `r ≈ 5.5%` annualised. (The exact figure depends on the dividend assumption, but the method shows how the futures basis encodes the carry — and hence the interest rate — that rho formalises.)

6. **Because of volga (vomma), the curvature of vega.** Vega-neutral only means the *first-order* vol sensitivity is zero at today's vol. The far-OTM strangle holder is **long volga**: as VIX doubles, their vega itself grows, so they gain far more than a flat vega estimate predicts — a profitable convexity in a vol explosion. The ATM calendar spread has very different (often negative or near-zero) volga, so its vega does not balloon the same way. Same starting vega, opposite behaviour in a large vol move — that gap is volga, the Greek of "vol of vol."
