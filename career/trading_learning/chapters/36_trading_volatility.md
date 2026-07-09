# Chapter 36: Trading Volatility — Long Vol, Short Vol & Regime-Based Strategy Selection

Most people come to options to bet on direction: they think Nifty is going up, so they buy a call. That is a perfectly good reason to be here, but it is only half the board. The deeper insight — the one that turns a punter into a professional — is that an option's price is built mostly out of *movement*, not direction. And movement is something you can trade on its own. You can take a position that makes money if Nifty thrashes around wildly, regardless of which way it ends up. You can take the opposite position that makes money if Nifty sits still and goes nowhere. Direction barely enters into it.

This chapter is about that second axis. Once you accept that you can be **long volatility** (betting on a big move or rising fear) or **short volatility** (betting on calm or falling fear), every strategy you have learned slots into a simple map. You stop asking only "up or down?" and start asking a second, richer question: "is the market going to move more than its price implies, or less?" Answer both questions, check whether volatility is currently cheap or expensive, and the right structure almost picks itself.

## Core concepts

### Volatility is a tradable thing, not just a number

Recall from the vega and India VIX chapters that every option premium contains an embedded forecast of future movement — the **implied volatility (IV)**, the market's annualised guess at how much the underlying will fluctuate. When you buy an option you are paying for that expected movement; when you sell one you are collecting payment for it.

That makes volatility an *asset you can be long or short*, exactly like you can be long or short Nifty itself:

- **Long volatility ("long vol")** — you own movement. You profit if the underlying moves *more* than the price implied, or if IV itself *rises* (option premiums fatten). You generally pay a premium up front, and time decay (theta) works against you while you wait.
- **Short volatility ("short vol")** — you have sold movement. You profit if the underlying moves *less* than implied, stays in a range, or if IV *falls* (premiums deflate). You generally collect premium up front, and time decay works *for* you — but a violent move can hurt badly.

There are two distinct ways to be right when long vol: the *realised* move can be big (the underlying actually swings a lot, helping your gamma), **or** *implied* volatility can rise (the fear gauge climbs, helping your vega). A short-vol position wants the opposite of both: small realised moves and falling IV.

### The long-vol toolkit

These structures profit from large moves and/or rising IV. Their defining feature: **positive vega and positive gamma** — they love movement and uncertainty.

- **Long straddle** — buy the at-the-money (ATM) call *and* the ATM put. The cleanest pure-volatility bet: the two deltas roughly cancel, the two vegas add. Profits from a big move in *either* direction.
- **Long strangle** — buy an out-of-the-money (OTM) call and an OTM put. Cheaper than a straddle (both legs are OTM), but needs a *bigger* move to pay off.
- **Debit spreads** (bull call spread, bear put spread) — a directional move bet with a volatility flavour; long the nearer strike, short the farther one. Lower vega than a straddle, but still a "pay now, profit if it moves my way" structure.
- **Calendars / diagonals** — sell a near-dated option and buy a longer-dated one at the same (or nearby) strike. A more advanced long-*vega* play that profits if IV rises, while the near leg's faster decay helps finance it.

### The short-vol toolkit

These profit from calm and/or falling IV. Their defining feature: **negative vega and negative gamma** — they fear movement and feed on time decay.

- **Short straddle** — sell the ATM call and ATM put. Maximum premium; profit if the underlying expires near the strike. Theoretically unlimited risk on the call side.
- **Short strangle** — sell an OTM call and an OTM put. Wider profit zone, smaller premium. Still undefined risk.
- **Iron condor** — a short strangle with protective wings (buy a farther OTM call and put), turning undefined risk into a defined-risk range bet. The retail favourite for harvesting calm.
- **Credit spreads** (bull put spread, bear call spread) — sell a nearer strike, buy a farther one for protection. Profit if the underlying stays above (or below) your short strike and IV doesn't spike.

### The 2x2: combine your view on direction with your view on volatility

Here is the map that ties it together. A professional holds *two* opinions before placing a trade — one about direction, one about volatility — and the intersection names the strategy.

|                         | **Expect MORE vol** (big move / rising IV) | **Expect LESS vol** (calm / falling IV)        |
|-------------------------|--------------------------------------------|------------------------------------------------|
| **Bullish (up)**        | Long call; bull call (debit) spread        | Bull put (credit) spread; short put            |
| **Bearish (down)**      | Long put; bear put (debit) spread          | Bear call (credit) spread; short call          |
| **Neutral (sideways)**  | Long straddle / long strangle              | Short straddle / strangle; **iron condor**     |

Read it like this. The *columns* decide whether you are a net buyer (left) or seller (right) of premium. The *rows* tilt the structure up, down, or symmetric. A neutral-but-expecting-fireworks view (left-bottom) is a long straddle: you don't care which way, you just need a big move. A neutral-and-expecting-calm view (right-bottom) is an iron condor: you're betting the market stays boxed in. A bullish-and-expecting-calm view (right-top) is a bull put spread: you want a gentle drift up with deflating premium, and you'd rather *sell* expensive options than buy cheap ones.

The single most common beginner error is filling in only the rows and ignoring the columns — having a direction view but no volatility view, and therefore buying premium when they should be selling it, or vice versa.

### The lognormal distribution: where might it expire, and with what odds?

To bet on movement you need a picture of the *range* of places the underlying might land at expiry. That picture is the **lognormal distribution**.

Why lognormal and not a plain bell curve? Because prices compound in percentage terms and cannot go below zero. Modelling *returns* as normally distributed makes the *price* itself lognormal — a bell curve squashed on the left (it can't cross zero) with a longer tail stretching right. For a weekly expiry it looks nearly symmetric; over longer horizons the rightward skew grows.

The width of that distribution is set by implied volatility and time. The key practical quantity that falls out of it is the **expected move** — the one-standard-deviation range the market is pricing in:

`expected move (1 sigma) ≈ Spot * IV * sqrt(T)`

where IV is the implied volatility as a decimal and T is the time to expiry in years. A one-sigma range means the market is implying roughly a **68% chance** the underlying expires inside that band, about **95%** inside two sigma. Equivalently, there is about a 32% chance — roughly one in three — that it finishes *outside* one sigma.

A faster shortcut for a single expiry, avoiding the annualisation, is to scale India VIX down to the number of days left:

`expected move over D days ≈ Spot * (VIX/100) * sqrt(D / 365)`

This single number is the hinge of the whole chapter. The **long-vol trader is betting the underlying travels FURTHER than the expected move** (the realised move beats what was priced). The **short-vol trader is betting it stays INSIDE the expected move** (the underlying goes nowhere special, and the option seller keeps the premium). When you place a long straddle, your two breakevens sit almost exactly at plus and minus the premium you paid — and a fairly priced straddle's premium is close to the expected move. So a long straddle is, quite literally, a bet that the realised move exceeds the expected move; a short straddle is the bet that it doesn't.

![Figure: where Nifty might expire (lognormal) with straddle breakevens](figs/pop_distribution.png)

The figure shows the lognormal distribution of where Nifty might expire, centred near the current spot. The two vertical lines mark a long straddle's breakevens — spot plus and minus the premium paid. The long-vol trader profits in the *tails*, where the underlying finishes beyond a breakeven; the short-vol trader profits in the fat *middle*, where it expires between them. Because the middle holds most of the probability mass, the short-vol trader wins *more often* — but the long-vol trader wins *bigger* when the tail hits. That asymmetry is the heart of this chapter, and we return to its danger below.

### Matching the strategy to the IV regime: IV Rank

Knowing whether to be long or short vol requires knowing whether volatility is currently **cheap or expensive** — not in absolute terms, but relative to its own recent history. India VIX at 14 means nothing on its own; you need to know whether 14 is high or low *for this market lately*.

The tool is **IV Rank** (or the related IV Percentile). IV Rank places the current IV on a 0-to-100 scale between its lowest and highest readings over the past year:

`IV Rank = (current IV - 1-year low) / (1-year high - 1-year low) * 100`

- **High IV Rank (say above 70-80)** — volatility is expensive relative to its own history. Premiums are fat. This is the regime to **sell vol**: short strangles, iron condors, credit spreads. You are selling overpriced movement and betting on mean reversion (IV tends to fall back toward its average).
- **Low IV Rank (say below 20-30)** — volatility is cheap. Premiums are thin. This is the regime to **buy vol**: long straddles, strangles, calendars, debit spreads. You are buying cheap movement and betting either that a move materialises or that IV reverts upward.

The professional mantra is "**sell high IV, buy low IV**," and it works because implied volatility is strongly *mean-reverting* — it spikes and then sags back, rather than trending forever. Selling when IV Rank is high stacks two edges: you collect rich premium *and* you have IV crush on your side as it reverts. Buying when IV Rank is low means you pay little and have room for IV to expand in your favour. India VIX is your raw thermometer; IV Rank tells you whether today's temperature is a fever or a chill.

### Putting regime and event together — the Indian calendar

The regime and the event calendar interact. **Before a known event** (RBI policy, the Union Budget on Feb 1, election results, a heavyweight's quarterly results, US Fed nights) India VIX and IV Rank climb as the market braces, and premiums bloat. **In quiet periods** between events, India VIX drifts to multi-month lows, IV Rank sinks, and premiums thin out. The cleanest setups exploit the *predictability of the IV cycle itself*: be long vol *before* IV ramps (buy the calm), and be short vol *into* the bloated pre-event IV if you can stomach the move risk, harvesting the crush after. We work a full example next.

## Worked example (₹, Nifty/Bank Nifty)

**The setup.** It is a quiet Monday. **Nifty spot = 24,000.** The weekly expiry is **4 days** away (Thursday). There is no scheduled event this week, India VIX is sitting low at **11%**, and your IV Rank screen reads about **15** — volatility is cheap by its own one-year history. The question: long vol or short vol, and which structure?

**Step 1 — Compute the expected move.** Using the day-count shortcut with VIX = 11% and D = 4 days:

`expected move ≈ 24,000 * (11/100) * sqrt(4/365)`
`= 24,000 * 0.11 * sqrt(0.01096)`
`= 24,000 * 0.11 * 0.1047 ≈ ₹276`

So the market is pricing a one-sigma weekly range of about **±276 points**, i.e. roughly **23,724 to 24,276**. There is about a 68% chance Nifty expires inside that band and about a one-in-three chance it finishes outside it.

**Step 2 — Read the regime.** IV Rank is 15 — *low*. Volatility is cheap. The regime mantra says **buy vol**, not sell it. Selling a short straddle here would collect thin premium for unlimited risk — poor risk/reward. So we lean long vol.

**Step 3 — Form a combined view.** You have no strong directional bias (you don't know if Nifty goes up or down), but you notice an *unscheduled* risk: a US Fed decision lands mid-week and global markets are jumpy. You think the realised move could *exceed* the priced ±276. Neutral direction + expecting more vol → the 2x2 sends you to the **long straddle** (neutral-bottom-left cell).

**Step 4 — Price the straddle and find breakevens.** With Nifty at 24,000 and IV at 11%, suppose the ATM 24,000 weekly call costs **₹140** and the ATM 24,000 put costs **₹135**. Total premium paid:

`straddle cost = 140 + 135 = ₹275 per unit`

Notice this is almost exactly the expected move (₹276) — that is not a coincidence; a fairly priced ATM straddle *is* the market's expected move. Your breakevens:

`upper breakeven = 24,000 + 275 = 24,275`
`lower breakeven = 24,000 - 275 = 23,725`

You profit only if Nifty expires **above 24,275 or below 23,725** — i.e. if the *realised* move beats the *expected* move. You are explicitly betting the tail.

**Step 5 — Resolve.** The Fed surprises hawkish; Nifty sells off **350 points** to 23,650 by Thursday. The put finishes ₹350 in-the-money (`24,000 - 23,650 = 350`), the call expires worthless. Payoff:

`gross = 350 (put intrinsic) + 0 (call) = ₹350`
`net P&L = 350 - 275 = +₹75 per unit`

On one lot (Nifty lot size currently about 75 units), that is roughly `75 * 75 ≈ ₹5,625` profit. You were *neutral on direction* and still won, because the realised move (350) exceeded the expected move (276) — exactly the bet a long straddle expresses.

**Step 6 — The mirror image.** Had this been a high-IV-Rank week (say IV Rank 85, India VIX at 22 with bloated premiums and no event left to fear), the trade flips. You would *sell* the straddle (or, to cap risk, sell an **iron condor** with wings) and profit as long as Nifty stayed inside the breakevens and IV crushed back down. Same machinery, opposite regime, opposite side. The regime — not a hunch — decides which side of volatility you take.

## Common mistakes / risk note

- **Trading direction with no volatility view.** Buying a call before an event "because it'll go up" ignores the column of the 2x2. If IV is rich, you overpay and the post-event crush can sink you even when you're right on direction (see the vega chapter). Always hold *both* views.
- **Selling cheap volatility / buying expensive volatility.** Selling a straddle when IV Rank is 15 collects thin premium for unlimited risk; buying a straddle when IV Rank is 90 means paying top-dollar for movement that the post-event crush will deflate. Check IV Rank *before* deciding which side to take.
- **Forgetting theta when long vol.** A long straddle bleeds premium every single day. If the big move doesn't come *soon enough*, time decay grinds the position to a loss even if a move eventually arrives. Long vol is a race against the clock.
- **The fat-tail trap of short vol.** This is the big one. Short-vol structures win *often* — the underlying usually stays inside the expected move, so you pocket premium most weeks. This builds dangerous overconfidence. But the lognormal distribution has **fat tails**: real markets crash and gap far more often than a clean bell curve predicts. A naked short straddle/strangle carries *undefined* loss, and a single gap event — a budget shock, a global crash, a circuit-breaker day — can erase months of steady premium income in one session. Selling volatility is "picking up pennies in front of a steamroller": pleasant until it isn't. **Define your risk** (iron condors, spreads with wings), size small, and never sell so much that one tail event ends you. SEBI studies showing roughly 9 in 10 retail F&O traders lose money are full of over-leveraged option sellers who met the tail.
- **Confusing realised and implied.** You can be long vol and lose because, although IV *rose*, the underlying didn't actually *move* (or vice versa). Know which engine — gamma (realised) or vega (implied) — your trade is really betting on.

## Key takeaways

- You can trade **volatility itself**, not just direction: be **long vol** (profit from big moves or rising IV) or **short vol** (profit from calm or falling IV).
- **Long-vol** tools: long straddles, strangles, debit spreads, calendars — positive vega, positive gamma, pay premium, theta works against you.
- **Short-vol** tools: short straddles/strangles, iron condors, credit spreads — negative vega, negative gamma, collect premium, theta works for you.
- Choose a strategy from the **2x2**: combine your direction view (bullish/bearish/neutral) with your volatility view (more vol / less vol). The volatility column decides whether you *buy* or *sell* premium.
- The **lognormal distribution** defines where the underlying might expire; the **expected move ≈ Spot * IV * sqrt(T)** is the one-sigma band. Long vol bets the realised move *exceeds* it; short vol bets it stays *inside* it. A fair ATM straddle's premium ≈ the expected move.
- Match the strategy to the **IV regime via IV Rank**: high IV Rank → sell vol (rich premium, crush on your side); low IV Rank → buy vol (cheap movement, room to expand). IV mean-reverts.
- **Short vol has fat tails**: it wins often but a single gap can wipe out many wins. Define your risk and size small — never sell volatility naked enough to be ended by one tail event.

## Practice problems

1. **Fill in the grid.** You are mildly *bullish* on Bank Nifty and you also believe implied volatility is too high and about to fall after this week's RBI policy. Which cell of the 2x2 are you in, and which single structure best fits?

2. **Expected move (numeric).** Bank Nifty spot is 52,000, India VIX-equivalent IV is 14%, and there are 7 days to expiry. Estimate the one-sigma expected move in points and the corresponding price band. Roughly what is the probability Bank Nifty expires *outside* that band?

3. **Straddle breakevens (numeric).** Nifty is at 24,000. The ATM 24,000 weekly call trades at ₹160 and the put at ₹150. Find the cost, the two breakevens, and state in one sentence what realised outcome the *buyer* of this straddle needs.

4. **Regime read.** India VIX is at 25 and your IV Rank screen shows 88, the day before the Union Budget. A friend wants to buy a long straddle "because the Budget will cause a huge move." Critique this using the IV-regime idea. What is the main danger?

5. **Conceptual — two ways to be right.** Explain the difference between profiting from *realised* volatility and profiting from *implied* volatility when you are long a straddle. Give an India example of each.

6. **The fat-tail caveat.** A trader has sold an OTM Nifty strangle every week for 30 weeks and won 28 of them, calling it "free money." Explain, using the lognormal distribution and fat tails, why this track record is dangerous and what one change would make the strategy survivable.

## Solutions

1. **Bullish + expecting less vol** → the top-right cell. The structure is a **bull put (credit) spread**: sell an OTM put, buy a farther OTM put for protection. You collect premium (short vol, benefiting from the post-RBI IV crush), profit if Bank Nifty drifts up or simply holds above your short strike, and your loss is capped by the long wing. A plain long call would be wrong here — it's long vega and would get hurt by the falling IV you expect.

2. Using `expected move ≈ Spot * (IV) * sqrt(D/365)` with IV = 0.14, D = 7:
`= 52,000 * 0.14 * sqrt(7/365) = 52,000 * 0.14 * sqrt(0.01918) = 52,000 * 0.14 * 0.1385 ≈ ₹1,008`.
So about **±1,008 points**, a band of roughly **50,992 to 53,008**. One sigma implies about a 68% chance of expiring *inside*, so roughly a **32% chance — about one in three — of finishing outside** the band.

3. Cost `= 160 + 150 = ₹310` per unit. Upper breakeven `= 24,000 + 310 = 24,310`; lower breakeven `= 24,000 - 310 = 23,690`. The buyer needs Nifty to expire **above 24,310 or below 23,690** — i.e. a realised move larger than ±310 points (larger than the expected move the premium implies); anywhere in between, the straddle loses.

4. With India VIX at 25 and IV Rank at 88, volatility is **expensive** — near its one-year high. Buying a straddle means paying *top-dollar* premium. Two things work against the buyer: the move must be enormous just to clear the inflated breakevens, and the moment the Budget passes, **IV crushes** and deflates both legs. The friend could be right that the Budget causes a big move and *still lose*, because the realised move fails to beat the bloated expected move while the vega crush compounds the damage. In a high-IV-Rank regime the edge is on the **selling** side (e.g. a defined-risk iron condor), not the buying side.

5. When long a straddle you have **positive gamma** (helped by realised volatility — the underlying actually swinging around, which you can also harvest by delta-hedging) and **positive vega** (helped by rising implied volatility — the market's *forecast* of movement climbing, fattening your premiums even before any move occurs). *Realised* example: you hold a Nifty straddle over a week and Nifty whips 400 points down then back — the actual movement pushes a leg deep in-the-money. *Implied* example: you buy a quiet, low-IV straddle three weeks before an election; as the event nears, India VIX climbs from 11 to 20 and your straddle gains value from the IV expansion *even though Nifty has barely moved*. Long vol can pay via either engine.

6. A short OTM strangle profits whenever the underlying expires inside the strikes — which, because the lognormal distribution piles most of its probability in the **middle**, happens *most weeks*. Winning 28 of 30 is exactly what the math predicts and proves nothing about safety. The danger lies in the **fat tails**: real markets gap and crash far more often than a clean bell curve implies, and a naked strangle has **undefined loss**, so a single tail event (a crash, a circuit day, a budget shock) can lose more than all 28 wins combined — "picking up pennies in front of a steamroller." The track record breeds overconfidence and larger size, setting up a ruinous blow-up. The one change that makes it survivable: **define the risk** by buying protective wings (converting the strangle into an **iron condor**) and **size small**, so the worst-case single-week loss is capped and cannot end the account. Frequency of winning is not the same as positive expectancy once the rare tail is priced in.
