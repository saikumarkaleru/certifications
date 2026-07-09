# Chapter 41: Strangles — Long & Short

A straddle, which you met in the previous chapter, buys (or sells) the call and the put at the *same* strike — usually at-the-money. It is the purest bet on movement, but it is also expensive, because at-the-money options carry the most time value of any strike. The **strangle** is the straddle's thriftier cousin. Instead of buying both options at the money, you spread them out: an out-of-the-money (OTM) call *above* the spot and an out-of-the-money put *below* it. You give up the option's "head start," but you pay a much smaller premium for the pair.

That single change — moving the strikes apart — flips the whole personality of the trade. A **long strangle** becomes a cheaper bet on a *big* move (cheaper to buy, but it needs the market to travel further before it pays). A **short strangle** becomes one of the most popular income trades on the Indian options market: you sell both wings, pocket the premium, and win as long as the market stays inside a *wide* zone between your strikes. It is comfortable, it has a high hit-rate, and it carries a tail that can take your house. This chapter teaches both sides honestly, with full rupee Nifty and Bank Nifty examples.

## Core concepts

### What a strangle is

A strangle combines a call and a put with **different strikes but the same expiry**, both typically out-of-the-money:

- **Long strangle** = buy 1 OTM call (strike `Kc`, above spot) + buy 1 OTM put (strike `Kp`, below spot). You pay two premiums. You profit from a **large move in either direction**.
- **Short strangle** = sell 1 OTM call + sell 1 OTM put. You collect two premiums. You profit when the market **stays between the strikes** and time decay erodes both options.

The defining feature is the **gap between the strikes** (`Kc - Kp`). Everything inside that gap is "quiet zone." For a buyer the quiet zone is the enemy; for a seller it is the entire source of profit.

Contrast with the straddle:
- Straddle: both legs at the *same* ATM strike. Expensive, but it starts working on the very first point of movement.
- Strangle: legs *spread apart*. Cheaper, but there is a dead band in the middle where nothing happens.

### The long strangle: a cheaper bet on a big move

Buy an OTM call and an OTM put. You are saying: "I don't know which way Nifty goes, but I'm convinced it goes *far* — far enough to clear both the distance to my strike and the premium I paid." Classic triggers: a Budget, an RBI policy decision, an election result, a major earnings event for a heavyweight stock — anything you expect to crack the market loose, but whose direction you cannot call.

The total cost is the two premiums added together:

`Net debit = call premium + put premium`

This debit is your **maximum loss**, and it occurs whenever the market expires *between the two strikes* — there, both options finish worthless and you lose the whole outlay. That is the price of the wide quiet zone.

There are **two breakevens**, one on each side, because the move has to cover not just the premium but also the distance from spot to the OTM strike:

`Upper breakeven = Kc + net debit`
`Lower breakeven  = Kp - net debit`

Above the upper breakeven, profit climbs point-for-point and is theoretically **unlimited**. Below the lower breakeven, profit climbs as the market falls (capped only because the index cannot go below zero — effectively very large). The payoff is a wide valley: flat-loss floor across the middle, then two ramps heading up and away on the outside.

`Payoff (long strangle) = max(S - Kc, 0) + max(Kp - S, 0) - net debit`

**Long strangle vs long straddle.** Same idea — both win on movement — but the strangle is **cheaper to put on and harder to make money with.** Because the strikes are spread out, the strangle's combined premium is smaller (you are not paying for the rich ATM time value). But the move has to be *bigger* to reach a breakeven, because the market first has to travel the empty distance to the OTM strike before the option even has intrinsic value. A straddle starts earning on the first point past ATM; a strangle does nothing until the market clears the strike. So: **lower cost, lower probability, needs a larger move.** Traders pick a strangle when they want a big, cheap "tail" bet and expect a violent move; a straddle when they want the position working immediately around the current level.

### Greeks of the long strangle

- **Delta ≈ 0 at entry.** With the call above and the put below, the two deltas roughly cancel. The position is direction-neutral to start — it leans bullish only after a rally (call delta grows), bearish only after a fall.
- **Long gamma.** This is the engine. As the market moves toward and past one strike, that leg's delta accelerates, so the position gains speed in the direction of the move. A long strangle *likes* fast, large moves.
- **Long vega.** You own two options, so a rise in implied volatility (India VIX) inflates both premiums. A jump in VIX can make a long strangle profitable *even before the spot moves much*. The flip side is the trap below.
- **Negative theta.** You own two wasting assets. Every quiet day, time value bleeds out of *both* legs. The long strangle's enemy is a calm, range-bound market — exactly the condition the short strangle loves.

The volatility trap is the same one that bites straddle buyers, only worse: buying a strangle into an event when India VIX is already elevated means you pay inflated premiums, and the **"vol crush"** after the event (VIX collapses once uncertainty resolves) can wipe out your time value even if the market moves your way a little. You must move *enough* to outrun both theta and the post-event vega collapse.

### The short strangle: the popular Indian income trade

Now flip every leg. **Sell** the OTM call and **sell** the OTM put. You collect both premiums up front, and you are betting that Nifty (or Bank Nifty) **stays inside the two strikes** until expiry, where both options expire worthless and you keep the lot. This is, with the iron condor, one of the most widely run strategies by Indian options sellers — premium-selling on the weekly expiry, harvesting theta on an index that spends most of its time grinding sideways.

The appeal is real and worth stating plainly:

- **A wide profit zone.** You make the *full* premium anywhere between the strikes — a much broader comfort band than a short straddle, which only hits max profit at a single point. The market can wander hundreds of points and you still win.
- **Maximum profit = total premium collected**, realised if the market expires anywhere in `[Kp, Kc]`:

  `Max profit (short strangle) = call premium + put premium`

- **Positive theta.** Time is now your *friend*. Every quiet day, both options lose value, and that loss is your gain. You are the house collecting rent on time.
- **Negative vega.** You benefit when implied volatility falls (premiums you are short shrink). Selling into high VIX and watching it normalise is the seller's dream.
- **High probability of a small win.** Because both strikes are OTM, the market usually expires inside them. The hit-rate feels wonderful — a string of green weeks.

The breakevens mirror the long version exactly (the seller's profit zone is bounded by the buyer's breakevens):

`Upper breakeven = Kc + total premium`
`Lower breakeven  = Kp - total premium`

`Payoff (short strangle) = total premium - max(S - Kc, 0) - max(Kp - S, 0)`

Between the breakevens you keep something; outside them you lose. And here is the brutal asymmetry: **losses outside the breakevens are undefined.** On the upside they are theoretically unlimited (the call you sold has no ceiling); on the downside they are very large (the put you sold loses as the index falls toward zero). You collected a small, capped premium in exchange for accepting a large, *uncapped* tail. That is the entire risk story of selling strangles, and it deserves a section of its own.

### The tail risk — read this twice

A short strangle wins small and often, then loses big and rarely. The danger is not the typical week — it is the **gap day**. Indian indices do not always move smoothly; they *gap*. An overnight global crash, a shock RBI move, a geopolitical event, a Budget surprise, a circuit-breaker session — and the market can open hundreds of points *outside* your strike, far past your breakeven, before you can do anything. Index options are **European and cash-settled**, so you cannot adjust mid-gap; you face the settlement.

Concrete shape of the danger:
- You might collect ₹120 of premium per unit and be exposed to a 1,000-point adverse move that costs you ₹880 per unit *net*. One bad week can erase ten good ones.
- The position is **short gamma**: as the market races toward a strike, that leg's delta explodes *against* you, so your losses accelerate exactly when you most need them to slow down. This is the mirror image of the long strangle's friendly gamma.
- A **vol spike** (VIX jumping on fear) inflates the very options you are short, hammering your mark-to-market and triggering margin increases — often forcing you to exit at the worst possible moment.

This is why the honest framing matters. Selling strangles is *not* "free money," even though a run of easy weeks makes it feel that way. It is selling insurance against large moves: you collect steady premiums and, every so often, pay a catastrophic claim. Professionals respect this by **defining the risk** (converting to an iron condor — buying cheap further-OTM wings as protection, covered in Chapter 47), **sizing small**, and **having a hard stop** (for example, exit if the loss reaches 2x the premium collected). A naked short strangle with no protection and full size is how disciplined-looking accounts blow up on a single gap. SEBI studies find roughly **9 in 10 retail F&O traders lose money**, and over-sized premium-selling that meets one fat tail is a textbook route to that statistic.

### Short strangle vs short straddle

Both are theta-positive, vega-negative, undefined-risk sellers' trades. The trade-off is **safety vs income**:

- **Short straddle** (same ATM strike): collects the *most* premium (richest ATM time value), but the profit peak is a single point and the breakevens are *narrow* — the market has little room to move before you start losing. Higher reward, lower margin for error.
- **Short strangle** (spread OTM strikes): collects *less* premium, but buys a *wide* flat profit zone between the strikes and breakevens that sit further out. Lower reward, much larger margin for error.

In one line: **the strangle trades premium for breathing room.** Most sellers who want a calmer, higher-probability income trade choose the strangle; those squeezing maximum premium from a tight expected range choose the straddle. Both share the same uncapped tail.

![Figure: short strangle payoff](figs/short_strangle.png)

The short strangle payoff (above) is the table-top shape: a flat plateau of maximum profit across the whole zone between the strikes, then two ramps plunging into undefined loss past each breakeven. The long strangle is simply this picture flipped upside-down — a flat-loss valley in the middle, two profit ramps climbing away on the outside (next figure).

### Strike selection by delta

How far out should the strikes go? Professionals do not eyeball it; they use **delta** as a proxy for the probability that an option finishes in-the-money. A call with delta 0.16 has *roughly* a 16% chance of expiring ITM (and the put with delta -0.16 likewise). So selling both at delta ~0.16 builds a strangle whose strikes the market has only about a 16% chance, each side, of breaching — a combined "stay inside" probability in the ballpark of 68%.

- **Closer strikes (higher delta, e.g. 0.25–0.30 each):** more premium collected, narrower profit zone, *lower* probability of staying inside. Aggressive.
- **Further strikes (lower delta, e.g. 0.10–0.15 each):** less premium, wider profit zone, *higher* probability of success. Conservative.

A common seller's rule is the **"16-delta strangle"** — sell each leg near 0.16 delta, roughly one standard deviation out, so the expected-move band sits *inside* your strikes. For a long strangle buyer the same logic runs in reverse: cheaper, further-OTM strikes are bigger lottery tickets needing a larger move. Delta gives you a consistent, probability-aware way to choose strikes instead of guessing round numbers.

### Margin

Buying a strangle is paid for in **full premium up front**, and that debit is your entire risk — no margin calls, you sleep soundly.

Selling a strangle is the opposite. Because the risk is undefined, the exchange charges **SPAN + exposure margin** under the SPAN system, sized to a worst-case adverse move across both legs. For a one-lot Nifty short strangle this is typically on the order of **₹1.2–1.7 lakh** (it varies with volatility and the exchange's risk parameters, and rises sharply when VIX spikes). Two practical consequences:

- A **rising VIX raises your margin** mid-trade, which can force liquidation at the worst time — the same spike that is hurting your position is also demanding more capital.
- **Defining the risk by buying protective wings** (turning the short strangle into an **iron condor**) dramatically *reduces* the margin, because the exchange now sees a capped maximum loss. Many sellers run condors largely for this capital efficiency, not only for the safety.

## Worked example (₹, Nifty/Bank Nifty)

It is Monday. **Nifty spot = 24,000**, weekly expiry on Thursday, lot size **75** (set by the exchange; it changes periodically). India VIX is moderate. You look at two OTM strikes 300 points either side of spot:

- **24,300 CE** (OTM call) trading at **₹70**
- **23,700 PE** (OTM put) trading at **₹80**

So `Kc = 24,300`, `Kp = 23,700`, and the combined premium is `70 + 80 = ₹150` per unit.

### Case A — you BUY the strangle (long)

You expect a violent move (say, a big event Thursday) but cannot call direction.

- **Net debit** = `150 * 75 = ₹11,250`. This is your **maximum loss**.
- **Upper breakeven** = `Kc + debit = 24,300 + 150 = 24,450`.
- **Lower breakeven** = `Kp - debit = 23,700 - 150 = 23,550`.
- **Quiet zone (max-loss band)** = anywhere from 23,700 to 24,300 at expiry, both legs expire worthless.

Per-unit payoff = `max(S - 24,300, 0) + max(23,700 - S, 0) - 150`. Lot P&L = that × 75.

| Nifty at expiry (S) | Call value | Put value | Per-unit P&L | Lot P&L |
|---|---|---|---|---|
| 23,200 | 0 | 500 | +350 | **+₹26,250** |
| 23,550 | 0 | 150 | 0 | **₹0** (lower breakeven) |
| 23,700 | 0 | 0 | -150 | **-₹11,250** (max loss) |
| 24,000 | 0 | 0 | -150 | **-₹11,250** (max loss) |
| 24,300 | 0 | 0 | -150 | **-₹11,250** (max loss) |
| 24,450 | 150 | 0 | 0 | **₹0** (upper breakeven) |
| 24,800 | 500 | 0 | +350 | **+₹26,250** |

Read it: the market must clear **24,450 up or 23,550 down** — a move of about 450 points (~1.9%) from spot — *just to break even*. Anywhere in the 600-point band between the strikes, you lose the full ₹11,250. That is the long strangle's bargain: cheap to enter, but it demands a genuinely big move. A 250-point rally to 24,250 — which *feels* like a win — still leaves you at the full max loss, because you never reached the call strike.

![Figure: long strangle payoff](figs/long_strangle.png)

### Case B — you SELL the strangle (short)

Same two strikes, opposite side. You believe Nifty stays rangebound into Thursday and you want to harvest theta.

- **Premium collected** = `150 * 75 = ₹11,250`. This is your **maximum profit**.
- **Upper breakeven** = `24,300 + 150 = 24,450`; **Lower breakeven** = `23,700 - 150 = 23,550`.
- **Profit zone** = expire anywhere in `[23,700, 24,300]` to keep the *full* ₹11,250; you stay net-positive anywhere between **23,550 and 24,450** (a 900-point-wide band).

Per-unit payoff = `150 - max(S - 24,300, 0) - max(23,700 - S, 0)`.

| Nifty at expiry (S) | Per-unit P&L | Lot P&L | Note |
|---|---|---|---|
| 23,550 | 0 | **₹0** | lower breakeven |
| 23,700 | +150 | **+₹11,250** | max profit (zone edge) |
| 24,000 | +150 | **+₹11,250** | max profit (mid-zone) |
| 24,300 | +150 | **+₹11,250** | max profit (zone edge) |
| 24,450 | 0 | **₹0** | upper breakeven |
| 24,800 | -200 | **-₹15,000** | past breakeven, loss exceeds premium |
| 25,200 | -600 | **-₹45,000** | gap scenario — undefined tail |

Notice the asymmetry in the last two rows. Your *best* outcome, no matter how perfectly the market behaves, is **+₹11,250**. But a 1,200-point gap up to 25,200 — the kind of move a global shock or Budget surprise can deliver overnight — costs you **₹45,000**, four times the premium you collected, and the loss keeps growing the further the market runs. You sold ₹11,250 of comfort and accepted a tail with no ceiling. That single row is the whole reason to size small, set a stop (e.g. exit near a ₹22,500 loss, 2x premium), or buy protective wings.

### A Bank Nifty note

Bank Nifty (spot ~52,000, lot size ~15, currently) moves faster and wider than Nifty, so its options are richer but its strangles get breached more often. A seller might place a Bank Nifty short strangle 800–1,000 points either side (say 53,000 CE / 51,000 PE), collect a larger premium, and still face a wider, more violent tail. The higher premium is *compensation* for higher realised volatility, not a free lunch — Bank Nifty's gap risk is exactly what makes its premiums fat.

## Common mistakes / risk note

- **Selling naked strangles for the steady income, ignoring the tail.** The string of easy green weeks is the trap, not the reward. One gap day past your breakeven can erase months of premium. If you sell, **define the risk** (iron condor), **size small**, and **set a hard stop**.
- **Treating a long strangle's low cost as low difficulty.** Cheap to buy is not easy to win. The wide quiet zone means a "decent" move (say 250 points) can still leave you at full max loss because you never cleared the strike. You need a *big* move, fast.
- **Buying a strangle into already-high VIX before an event.** You overpay for inflated premiums, then the post-event **vol crush** collapses your time value. You can be right on direction and still lose to the vega drop. Prefer to buy *before* VIX runs up, or accept that you need a large move to overcome the crush.
- **Selling into low VIX for too little premium.** When India VIX is depressed, the premium you collect is thin while the tail is just as fat — a poor risk-reward. Sellers want *elevated* VIX (rich premium) that they expect to normalise.
- **Forgetting margin can balloon mid-trade.** A VIX spike raises SPAN margin on your short strangle exactly when the position is hurting, potentially forcing liquidation at the worst price. Keep buffer capital; do not run at full margin utilisation.
- **Confusing "high probability" with "high expected value."** A short strangle wins ~70% of weeks and still loses money over time if the rare loss is large enough. A 70% hit-rate with a tail that costs 5x the premium is a losing game without strict risk control.

## Key takeaways

- A **strangle** uses an OTM call above and an OTM put below: cheaper than a straddle, but with a dead "quiet zone" between the strikes.
- **Long strangle** = buy both. Cost = `call premium + put premium` (the max loss). Breakevens = `Kc + debit` (up) and `Kp - debit` (down). Long gamma, long vega, negative theta — it needs a **big, fast** move and is hurt by calm markets and vol crush.
- **Long strangle vs long straddle:** the strangle is cheaper but needs a *larger* move and has a *lower* probability of paying off.
- **Short strangle** = sell both. A popular Indian income trade with a **wide flat profit zone** between the strikes. Max profit = total premium; positive theta; negative vega — wins when the market stays rangebound and VIX falls.
- **Short strangle vs short straddle:** the strangle collects *less* premium but buys a *wider* safety band; both carry the same **undefined tail risk**.
- The short strangle's danger is the **gap day / black swan**: losses past the breakevens are uncapped, gamma works against you, and one outsized move can dwarf many weeks of premium. Define the risk (iron condor), size small, and use a hard stop.
- **Choose strikes by delta** (e.g. the ~16-delta strangle) for a probability-aware, repeatable rule rather than guessing round numbers. Selling requires **SPAN margin**; buying protective wings cuts that margin sharply.

## Practice problems

1. **(Conceptual)** In one sentence each, explain why a long strangle is *cheaper* than a long straddle but *harder* to make a profit on.

2. **(Numeric)** Nifty is at 24,000. You buy the 24,400 CE at ₹60 and the 23,600 PE at ₹65 (lot size 75). Find your net debit, max loss, and both breakevens. What is your lot P&L if Nifty expires at (a) 24,000, (b) 23,300, (c) 24,800?

3. **(Numeric)** Using the same strikes and premiums as Problem 2, you instead *sell* the strangle. State your max profit, the profit zone (where you keep the full premium), both breakevens, and your lot P&L if Nifty expires at (a) 24,000, (b) 25,000.

4. **(Conceptual)** A trader has sold Nifty weekly strangles for eight straight weeks, winning every time, and concludes it is "basically free money." Explain, using gamma and the idea of the tail, why this conclusion is dangerous, and name two concrete ways to control the risk.

5. **(Numeric)** Bank Nifty is at 52,000 (lot size 15). You sell the 53,000 CE at ₹150 and the 51,000 PE at ₹160. Find the premium collected, both breakevens, and your lot P&L if Bank Nifty gaps to 54,200 at expiry. How many times your collected premium is that loss?

6. **(Conceptual)** You want to sell a Nifty strangle and must choose between strikes at ~0.25 delta each and ~0.12 delta each. Describe the trade-off in premium, profit-zone width, and probability of success, and say which you would pick for a conservative income approach.

## Solutions

**1.** *Cheaper:* a strangle's legs are out-of-the-money, so they carry far less time value than the at-the-money options of a straddle, making the combined premium smaller. *Harder to profit:* because the strikes are spread apart, the market must first travel the empty distance to an OTM strike *and then* cover the premium before reaching a breakeven, so it needs a larger move (and has a lower probability of getting there) than a straddle, which begins earning on the first point past ATM.

**2.** Net debit = `(60 + 65) * 75 = 125 * 75 = ₹9,375` = max loss. Upper breakeven = `24,400 + 125 = 24,525`. Lower breakeven = `23,600 - 125 = 23,475`. Per-unit payoff = `max(S - 24,400, 0) + max(23,600 - S, 0) - 125`.
- (a) 24,000: both legs worthless → per-unit -125 → lot = **-₹9,375** (max loss; it sits in the quiet zone).
- (b) 23,300: put intrinsic = `23,600 - 23,300 = 300`; per-unit = `300 - 125 = +175` → lot = `175 * 75 =` **+₹13,125**.
- (c) 24,800: call intrinsic = `24,800 - 24,400 = 400`; per-unit = `400 - 125 = +275` → lot = `275 * 75 =` **+₹20,625**.

**3.** Selling the same structure: max profit = premium collected = **₹9,375**, kept if Nifty expires anywhere in the profit zone `[23,600, 24,400]`. Breakevens are the same levels as the buyer's: **23,475 (lower)** and **24,525 (upper)**; you stay net-positive between them. Per-unit payoff = `125 - max(S - 24,400, 0) - max(23,600 - S, 0)`.
- (a) 24,000: inside the zone, both legs worthless → per-unit +125 → lot = **+₹9,375** (max profit).
- (b) 25,000: call intrinsic = `25,000 - 24,400 = 600`; per-unit = `125 - 600 = -475` → lot = `-475 * 75 =` **-₹35,625**. Note this single loss is nearly **4x** the max profit — the undefined tail in action.

**4.** Eight wins in a row reflects the *high probability of a small win*, not an edge or safety. A short strangle is **short gamma**: as the market accelerates toward a strike, that leg's delta grows rapidly, so losses *accelerate* in a fast move — the rare losing week tends to be very large, not merely a mirror of the small wins. Over a long run, one tail event past the breakevens (a gap on global shock, RBI surprise, etc.) can dwarf many weeks of collected premium; the strategy wins often and small, loses rarely and big, so a winning streak says nothing about long-run profitability. Two concrete controls: (i) **define the risk** by buying cheap further-OTM wings, converting the strangle into an **iron condor** with a capped max loss (also cuts margin); (ii) **size small and set a hard stop** — e.g. exit if the loss reaches ~2x the premium collected — so no single week can be catastrophic.

**5.** Premium collected = `(150 + 160) * 15 = 310 * 15 = ₹4,650`. Upper breakeven = `53,000 + 310 = 53,310`. Lower breakeven = `51,000 - 310 = 50,690`. At 54,200: call intrinsic = `54,200 - 53,000 = 1,200` (the put expires worthless). Per-unit P&L = `310 - 1,200 = -890`; lot P&L = `-890 * 15 =` **-₹13,350**. As a multiple of premium: `13,350 / 4,650 ≈` **2.9x** the premium collected — lost on a single gap, the textbook short-strangle tail.

**6.** *0.25-delta strikes (closer to spot):* collect **more premium**, but the strikes sit nearer the money, so the **profit zone is narrower** and the **probability of staying inside is lower** (each leg has ~25% chance of finishing ITM). Aggressive, higher reward, more often breached. *0.12-delta strikes (further out):* collect **less premium**, but the **profit zone is wider** and the **probability of success is higher** (~12% ITM per leg). For a **conservative income approach**, pick the **~0.12-delta** strangle: the wider band and higher hit-rate suit steady premium harvesting, and you accept the smaller premium as the cost of breathing room. (Either way, the tail remains undefined, so the risk controls from Problem 4 still apply.)
