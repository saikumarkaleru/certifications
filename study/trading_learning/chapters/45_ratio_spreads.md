# Chapter 45: Ratio Spreads & Backspreads

Imagine a vegetable wholesaler who is fairly sure tomato prices will drift up a little this week, but is genuinely scared of a flood that could spike prices to the moon. He buys one crate today to ride the gentle rise, and to pay for it he sells two "delivery promises" to retailers at a higher price he'd happily sell at. As long as prices climb modestly, he wins on both sides. But he has promised to deliver *two* crates while owning only *one* — and if a flood sends prices vertical, that second, uncovered promise can hurt him badly. That lopsided bet — more sold than bought — is the **ratio spread**. Flip it around — own more than you sold, so you're praying for the flood — and you have its mirror image, the **backspread**.

Both strategies break the neat symmetry of the simple vertical spreads from the previous chapters. A vertical spread buys one option and sells one option. A ratio spread and a backspread deliberately use *unequal* quantities — most commonly 1-by-2 — and that imbalance is the whole point. It lets you express a far more specific view than "up" or "down": a view about *how much* the market will move, and in which direction, often while putting up little or no cash. The price of that precision is a new kind of risk you must understand cold before you ever place one — because, done carelessly, the ratio spread hides an uncovered short option that can deliver an ugly, fast loss.

## Core concepts

### The building block: unequal quantities

Recall the vertical spread (Chapters 38–39): you buy one option and sell one option at a different strike, same expiry, a perfectly hedged 1-by-1 package. A **ratio spread** keeps the same idea but changes the *ratio* of the legs. The classic is **1-by-2**: buy one option, sell two options further out of the money. Because you are short more contracts than you are long, you collect extra premium — often enough to make the whole structure a small **debit** (you pay a little), free (zero cost), or even a **credit** (you get paid to put it on).

A **backspread** is the same structure read backwards: sell one nearer option and buy two further options. Now you are *long* more contracts than you are short. You spend more on the two longs than you collect on the one short — but the longs are cheaper OTM options, so the net cost is often still a small debit or even a credit, and your upside on a big move is large.

The single most important habit when looking at either trade: **count the long and short contracts.** The leg you hold *more* of dominates the far-tail behaviour.

- **More short than long → ratio spread.** The extra short option is uncovered past a point — risk grows if the market runs too far.
- **More long than short → backspread.** The extra long option pays off explosively on a big move — risk is limited and sits in the middle.

A quick vocabulary check, since every term must earn its place:

- **Debit** — you pay net premium to open the position. **Credit** — you receive net premium.
- **Uncovered (naked) short** — a sold option with no long option of the same type beyond it to cap its loss; its risk is open-ended (unlimited for a call, very large for a put).
- **OTM (out of the money)** — a call with strike above spot, or a put with strike below spot; no intrinsic value yet.

### The call ratio spread: buy 1, sell 2

Let's build the most common version. With Nifty at 24,000:

- **Buy 1** call at 24,000 (at the money).
- **Sell 2** calls at 24,300 (further OTM).

Walk through what happens at expiry as Nifty rises, and the personality of the trade appears:

1. **Nifty stays at or below 24,000.** All three calls expire worthless. You keep (or pay) only the net premium. If you opened for a credit, that credit is your profit; if a small debit, that debit is your loss.
2. **Nifty rises to 24,300 — the sweet spot.** Your long 24,000 call is now 300 points in the money (worth ₹300 per unit of intrinsic value). The two short 24,300 calls are exactly at the money and expire worthless. You collect the full 300 points of intrinsic on the long call *plus* keep all the premium from the two shorts. **This is your maximum profit**, and it sits right at the strike of the options you sold.
3. **Nifty rises far above 24,300 — the danger zone.** Now both short calls are deep in the money. You own one call gaining value, but you are short *two* calls losing value. One of those shorts is hedged by your long call; the **second short is uncovered.** Above a certain level your single naked short call overwhelms the gains, and your loss grows without limit, point for point, as Nifty climbs. A 1-by-2 call ratio spread carries the same upside tail risk as being outright short one naked call.

So the call ratio spread is, in plain English: **"I think Nifty drifts up modestly toward 24,300, and I'm willing to be paid for that view — but I am quietly betting it does NOT rocket past it."** It is a mildly bullish, range-targeting trade with a sharp tail on the far side.

### The danger zone and the upper breakeven

The crucial number in a call ratio spread is the **upper breakeven** — the level past which the uncovered short turns the trade into a loss. Above max profit (at the short strike), every further point gives you +1 on the long call but -2 on the shorts, a *net -1 per point*. So the profit you banked at the short strike bleeds away one-for-one as Nifty climbs.

```
Max profit (at short strike K2) = (K2 - K1) + net credit       [per unit, credit positive]
Upper breakeven  = K2 + (max profit in points)
Above the upper breakeven: loss grows 1-for-1 with the underlying, unbounded.
```

There is also a **lower (downside) outcome**: if the market falls, all calls expire worthless and you simply keep your opening credit (or lose your opening debit). If the trade was opened for a credit, **there is no downside risk at all** — a fall just leaves you with the credit. All the risk lives in the upper tail. This one-sided risk profile is the signature of the ratio spread, and the figure below shows it clearly: a gentle rise to a peak at the short strike, then a relentless slide down into open-ended loss.

![Figure: call ratio spread payoff](figs/ratio_spread.png)

### The put ratio spread: the bearish mirror

Everything above flips for a **put ratio spread**: **buy 1** put nearer the money, **sell 2** puts further OTM (lower strikes). With Nifty at 24,000:

- **Buy 1** put at 24,000.
- **Sell 2** puts at 23,700.

This is **mildly bearish**. You profit most if Nifty drifts *down* to exactly 23,700 — your long put gains 300 points of intrinsic while both short puts expire worthless. The danger zone is now to the **downside**: if Nifty *crashes* well below 23,700, your second, uncovered short put creates a large (though technically capped, since price can't fall below zero) loss. Concretely, a market crash hurts a put ratio spread the way a melt-up hurts a call ratio spread.

The mental model: **a call ratio spread fears a rally; a put ratio spread fears a crash.** And since Indian index markets tend to *gap down* harder and faster than they gap up (fear moves quicker than greed — recall the volatility skew of Chapter 33), the put ratio spread's tail is the one to respect most. A surprise overnight gap-down on global cues can blow straight through the short strikes before you can react, and index options are European and cash-settled — you cannot escape the adverse expiry.

### The backspread: buy 2, sell 1 — betting on the breakout

Now reverse the quantities entirely. A **call backspread** (also "call ratio backspread") is:

- **Sell 1** call nearer the money (say 24,000).
- **Buy 2** calls further OTM (say 24,300).

You are now *net long* one extra call. Read the expiry outcomes:

1. **Nifty stays at or below 24,000.** All calls expire worthless; you keep your opening credit (this structure usually opens for a small net credit, because the one near call you sold is pricier than the two cheap far calls you bought). A flat or falling market leaves you with that credit — a small win.
2. **Nifty rises to 24,300 — the worst spot.** Your short 24,000 call is 300 points in the money (a 300-point loss), while your two long 24,300 calls are just at the money and worthless. **This is your maximum loss.** The pain is concentrated in the middle, right at the long strike — exactly the zone where a ratio spread makes its maximum *profit*. They are photographic negatives of each other.
3. **Nifty rockets far above 24,300 — the payday.** Now you own *two* calls gaining value against only *one* short call. The extra long call means your profit grows 1-for-1 (and accelerating past breakeven) as Nifty climbs, **unlimited to the upside.** The backspread is built to catch the violent breakout.

So a call backspread says: **"I expect a big, fast move UP — and if I'm wrong and nothing happens, I lose only a little (or keep my credit). I just must not get stranded in the middle."** Its risk is **defined and limited** (the most you can lose is that middle valley), unlike the ratio spread's open-ended tail. The figure shows the mirror shape: a small credit on the left, a defined-loss valley at the long strike, then an unbounded climb to the upper right.

![Figure: call backspread payoff](figs/call_backspread.png)

There is a **put backspread** too — sell 1 put nearer the money, buy 2 puts further OTM — which profits from a large *downward* breakout (a crash). Because of the skew, far OTM puts are relatively expensive, so put backspreads are a clean, defined-risk way to own crash protection that can even pay you a small credit if the market stays calm. Many professionals run put backspreads as cheap tail-risk hedges on a long portfolio.

### Net Greeks: the signature of each trade

Every position has a Greek fingerprint — its sensitivity to price (delta), to the *rate of change* of delta (gamma), to volatility (vega), and to time (theta). The imbalance in these trades gives them distinctive signatures.

**Call ratio spread (buy 1, sell 2), near the centre:**

- **Delta:** mildly positive at first (you want a small rise), but it *flips negative* past the short strike as the two shorts dominate — the position turns against you on a strong rally.
- **Gamma: net short.** You are short more options than you are long, so large moves hurt you. Short gamma is why the upper tail is dangerous.
- **Vega: net short.** A spike in implied volatility (India VIX jumping) inflates the two short options more than the single long — you lose on a vol spike even before price moves. You prefer to enter a ratio spread when **IV is high** (you're a net seller of expensive options).
- **Theta: net positive.** Time decay works *for* you — you're short more premium than you're long, so quiet days pay you. The ratio spread is, at heart, a premium-selling trade with a directional tilt.

**Call backspread (sell 1, buy 2):** every sign flips.

- **Delta:** can be slightly negative or flat near the centre, turning strongly positive on a big up-move (you're net long calls).
- **Gamma: net long.** Big moves *help* you — this is the engine of the explosive payoff.
- **Vega: net long.** A jump in IV *helps* you; you want to enter a backspread when **IV is low** (you're a net buyer of cheap options) and hope it expands.
- **Theta: net negative.** Time decay works *against* you. Sitting in the dead middle, you bleed a little every day. The backspread is a long-premium trade — it must be *paid for* with movement.

The one-line contrast to remember: **the ratio spread is paid theta to be short gamma and short vega (it earns while calm, fears the big move); the backspread pays theta to be long gamma and long vega (it bleeds while calm, loves the big move).** They are opposite bets on whether the market will *explode or stay put*.

### Exactly when to use each

The structures answer two different questions about the *magnitude* of the move:

**Use a ratio spread when** you have a **mild directional view plus a range/ceiling view**:

- You think Nifty drifts gently up (call ratio) or gently down (put ratio) toward a specific target, and you *don't* expect it to blow past that target.
- **IV is high** (IV rank elevated) so the two options you sell are richly priced — this is what lets you open for a credit or free, and gives you breathing room.
- You want a position that profits in a moderate move *or* even if nothing happens (kept credit), and you can tolerate — and have a plan for — the tail risk.
- You explicitly accept the uncovered-leg danger and will size and stop accordingly.

**Use a backspread when** you expect a **big, fast breakout**:

- You think Nifty is about to make a violent directional move (a breakout from a tight range, an event you expect to surprise, a momentum thrust) but you're not certain it'll happen — and you want **limited risk** if it doesn't.
- **IV is low**, so the two far options you buy are cheap, and you may even structure it for a credit.
- You want defined, limited downside (the middle valley) with open-ended upside on the move — an attractive asymmetry when you're early to a theme.
- Put backspreads specifically: as a cheap, defined-risk hedge against a market crash on an otherwise long book.

### The honest risk of the uncovered leg (ratio spreads)

This deserves its own blunt section, because it is where ratio spreads quietly hurt people. In a 1-by-2 ratio spread, **one of your two short options is naked.** The first short is hedged by your long; the second is not. That means:

- A **call ratio spread** has, in its upper tail, the **unlimited loss profile of a naked short call.** There is no upper bound on how far Nifty can climb, and your loss climbs with it, point for point, ×75 per lot. A trade that looked like "free money — I got paid a credit and Nifty only has to stay below 24,300" becomes a margin-call disaster if a global rally or a budget surprise sends the index up 3% overnight.
- A **put ratio spread** has, in its lower tail, the loss profile of a **naked short put.** The loss is technically capped (price stops at zero) but in practice enormous — and Indian markets gap *down* viciously, so this tail gets tested in exactly the panic conditions where liquidity dries up.
- Because there's a naked short, your broker charges **full SPAN + exposure margin** as if you held that naked option, and that margin *expands* as the position moves against you — you can be forced to add cash or close at the worst moment.

The defences are non-negotiable: **(1)** prefer to open ratio spreads for a *credit* or free, so the near-side and the no-move case can never lose; **(2)** size the position off the *naked* leg's risk, not off the comfortable credit — pretend you're short one naked option, because in the tail you are; **(3)** set a hard stop or a defensive level beyond the short strike and *act* on it; **(4)** consider converting it to a fully defined-risk trade by buying a cheap further-OTM option against the naked leg (turning the 1-by-2 into a "ratio with a wing," sometimes called a broken-wing butterfly). The backspread, by contrast, has *no* uncovered short — its risk is the bounded middle valley — which is precisely why it's the more beginner-safe of the pair.

## Worked example (₹, Nifty)

Let's price a concrete **call ratio spread** and then its **backspread** mirror so the numbers sit side by side. Assume:

- **Nifty spot** = 24,000, weekly expiry. **Lot size** = 75 (current Nifty lot; verify, as SEBI/NSE revise it over time).
- Premiums (points): 24,000 call = 150; 24,300 call = 70.

### A. The call ratio spread (buy 1 × 24,000, sell 2 × 24,300)

**Step 1 — Net premium.**

```
Pay for long:   1 * 150  = 150 points
Collect on shorts: 2 * 70 = 140 points
Net = 140 - 150 = -10 points  →  a 10-point DEBIT
```

You pay 10 points = `10 * 75 = ₹750` to open. (Often in higher IV the two shorts would total more than 150 and you'd open for a credit — here it's a tiny debit.)

**Step 2 — Maximum profit (at the short strike, 24,300).**

```
Long 24,000 call intrinsic = 24,300 - 24,000 = 300 points
Short 24,300 calls = at the money, worthless
Max profit = 300 - 10 (debit) = 290 points = 290 * 75 = ₹21,750 per lot
```

**Step 3 — Downside outcome.** If Nifty closes at or below 24,000, all calls expire worthless and you lose only the **10-point debit = ₹750.** (Had you opened for a credit, a fall would be a small *profit*.)

**Step 4 — Upper breakeven and the danger zone.**

```
Upper breakeven = short strike + max-profit points = 24,300 + 290 = 24,590
```

Below 24,590 you're in profit; **above 24,590 the uncovered short call drives a loss that grows 1-for-1.** If Nifty closes at, say, 24,900:

```
Long 24,000 call:        +900 points
Two short 24,300 calls:  -2 * 600 = -1,200 points
Net intrinsic = 900 - 1,200 = -300 points
Less the 10-pt debit = -310 points = -310 * 75 = -₹23,250 loss per lot
```

And it keeps getting worse the higher Nifty goes — **unbounded.** This is the honest danger: a comfortable-looking trade with a ₹21,750 best case has *no ceiling on its loss* if Nifty melts up. Beyond 24,590 you are effectively short one naked call.

**Outcome map at expiry (cash-settled at Nifty close):**

| Nifty close | Result |
|-------------|--------|
| ≤ 24,000 | Lose the 10-pt debit: -₹750 |
| 24,300 (short strike) | Maximum profit: +₹21,750 |
| 24,590 (upper breakeven) | Break even (₹0) |
| 24,900 | -₹23,250 and worsening |
| Higher | Unlimited loss |

### B. The call backspread (sell 1 × 24,000, buy 2 × 24,300) — the mirror

Same strikes and premiums, quantities reversed:

**Step 1 — Net premium.**

```
Collect on short: 1 * 150 = 150 points
Pay for longs:    2 * 70  = 140 points
Net = 150 - 140 = +10 points  →  a 10-point CREDIT = ₹750 received
```

**Step 2 — Outcomes.**

- **Nifty ≤ 24,000:** all calls worthless, keep the **+10-pt credit = +₹750.**
- **Nifty = 24,300 (worst spot):** short 24,000 call is 300 points ITM (-300), the two long 24,300 calls are worthless. `Max loss = 300 - 10 credit = 290 points = ₹21,750 per lot.` Note this is exactly the ratio spread's *max profit* — they're mirror images.
- **Lower breakeven** (where the descending line crosses zero) = `24,000 + 10 = 24,010`; **upper breakeven** = `24,300 + 290 = 24,590`. Between these you're in the loss valley.
- **Nifty = 24,900 (big breakout up):** short 24,000 call -900; two long 24,300 calls +2×600 = +1,200; net +300 + 10 credit = +310 points = **+₹23,250, and climbing without limit.** The backspread turns the ratio spread's disaster into its triumph.

**The clean contrast:** the ratio spread *makes* ₹21,750 if Nifty lands at 24,300 and *loses* without limit above 24,590; the backspread *loses* ₹21,750 at 24,300 (its capped, defined max loss) and *profits* without limit above 24,590. Pick the structure that matches your view on whether Nifty will *stall near the short strike* (ratio) or *blow through it* (backspread).

**Costs to remember (India-specific).** These are 2–3-leg trades, so brokerage and exchange fees apply per leg. **STT** (Securities Transaction Tax) hits the sell side of options on premium, and — critically — **in-the-money options left to settle at expiry are charged STT on the full settlement (intrinsic) value**, which can be a nasty surprise on a deep ITM short leg. Close ITM legs *before* expiry where possible. And remember the ratio spread's naked leg means **margin** is charged as for a naked short and *expands* against you — never size as if the credit were the only risk.

## Common mistakes / risk note

- **Treating a credit ratio spread as "free money."** Getting paid to open it does *not* mean it's safe. The uncovered short leg has open-ended (call) or very large (put) tail risk. The credit only protects the *no-move* and *near-side* cases.
- **Sizing off the credit, not the naked leg.** Beginners see a ₹750 credit and sell ten lots. Size as if you are short one naked option per ratio, because in the tail you are. Cap the tail loss at 1–2% of capital.
- **Putting on a backspread and getting bled by theta.** The backspread loses a little every quiet day and is worst exactly in the middle. If your big move doesn't come *soon*, the long premium decays. Backspreads need a catalyst and a time horizon — they're not "set and forget."
- **Wrong IV regime.** Sell ratio spreads in *high* IV (you're net short premium); buy backspreads in *low* IV (you're net long premium and want expansion). Doing the reverse fights the vega.
- **Ignoring the skew on put ratio spreads.** Indian indices gap *down* hard and fast. A put ratio spread's naked short put gets tested in panics, when liquidity vanishes and margins balloon. Respect that tail more than the call side's.
- **Leaving ITM legs to settle.** STT on settled in-the-money options is charged on intrinsic value — close them before expiry to avoid an outsized tax bill, and remember index options are European, so you can't exit early via exercise.
- **No defensive plan for the tail.** Decide *before* entering where you'll cap the naked leg — a hard stop level, or a pre-bought far wing converting it to defined risk. The single naked option is what turns a small loss into an account-ending one.

## Key takeaways

- A **ratio spread** is unequal-quantity: **buy 1, sell 2** (more short than long). It opens for a small debit, free, or a **credit**, profits in a **moderate move toward the short strike**, and is **mildly directional** — but the extra short leg is **uncovered**, so a too-far move brings open-ended (call) or very large (put) loss.
- **Max profit on a call ratio spread = (short strike − long strike) + net credit**, banked at the short strike; the **upper breakeven = short strike + max-profit points**, beyond which loss grows 1-for-1, unbounded.
- The **put ratio spread** is the bearish mirror: profits on a mild drop to the short strike, dangerous on a crash. The skew makes its downside tail especially worth respecting in India.
- A **backspread** reverses the ratio: **sell 1, buy 2** (more long than short). Often a net **credit**, with **defined/limited risk in the middle valley** and **open-ended profit on a strong breakout** in its direction. Its risk is the bounded middle, with no uncovered leg.
- **Net Greeks:** ratio spread = short gamma, short vega, **positive theta** (earns while calm, fears the move); backspread = long gamma, long vega, **negative theta** (bleeds while calm, loves the move). They are opposite bets on explosion-vs-stillness.
- **When to use:** ratio spread for a **mild directional + range/ceiling view in high IV**; backspread for an **expected big breakout in low IV** (and put backspreads as cheap, defined-risk crash hedges).
- **The honest risk:** the ratio spread's naked leg carries naked-option tail risk and **expanding margin**. Open for credit, size off the naked leg, set a hard stop, or buy a far wing to make it defined-risk. Backspreads are the more beginner-safe of the two because their risk is capped.

## Practice problems

1. **Count the legs.** A trader on Bank Nifty buys 1 put at 52,000 and sells 2 puts at 51,500. Is this a ratio spread or a backspread? Is it mildly bullish or mildly bearish, and on which side does the danger zone lie?

2. **Max profit and breakeven.** A Nifty call ratio spread: buy 1 × 24,000 call for 160 points, sell 2 × 24,400 calls for 80 points each. Lot size 75. Find (a) the net premium (debit or credit), (b) the maximum profit in rupees and the Nifty level where it occurs, and (c) the upper breakeven.

3. **The danger zone.** Using the spread from problem 2, compute the profit or loss per lot if Nifty closes at expiry at 25,000. Is the loss bounded?

4. **Greeks intuition.** You hold a Nifty call backspread (sell 1 near, buy 2 far). Overnight India VIX jumps from 11 to 17 while Nifty opens flat. Did your position most likely gain or lose on a mark-to-market basis, and which Greek explains it?

5. **Choose the structure.** Nifty has been pinned in a tight 23,900–24,100 range for two weeks, IV rank is low, and a national election result is due tomorrow which you expect to move the market sharply but you're unsure which way. Which of the four structures in this chapter best fits a one-directional big-move bet, and why might a *backspread* be safer here than a ratio spread?

6. **The honest risk.** A trader opens a Nifty call ratio spread (buy 1 × 24,000, sell 2 × 24,300) for a 20-point *credit*, lot size 75, and runs **5 lots**, telling himself "I get paid, and Nifty only has to stay below 24,300." Nifty gaps up overnight on a global rally and closes expiry at 25,100. Compute the per-lot and total result, and state the lesson.

## Solutions

**1.** Count the legs: **buy 1, sell 2** → more short than long → a **ratio spread** (specifically a *put* ratio spread). Buying a higher-strike put and selling two lower-strike puts is **mildly bearish** — it profits most if Bank Nifty drifts down to the short strike of 51,500. The **danger zone is to the downside**: if Bank Nifty *crashes* well below 51,500, the second, uncovered short put creates a large loss (capped only at price zero, but enormous in practice). Given that indices gap down hard, this tail deserves real respect.

**2.** Net premium: collect `2 * 80 = 160`, pay `1 * 160 = 160`. (a) Net = `160 - 160 = 0` → **opened for free (zero cost).** (b) Maximum profit occurs at the **short strike, 24,400**: long call intrinsic = `24,400 - 24,000 = 400` points, both shorts worthless, plus 0 net = **400 points = `400 * 75 = ₹30,000` per lot**, at Nifty = 24,400. (c) Upper breakeven = `short strike + max-profit points = 24,400 + 400 = 24,800`.

**3.** At Nifty 25,000: long 24,000 call = `+1,000`; two short 24,400 calls = `-2 * 600 = -1,200`; net intrinsic = `1,000 - 1,200 = -200` points; plus 0 net premium = `-200 points = -200 * 75 = -₹15,000` per lot. **No, the loss is not bounded** — above the 24,800 breakeven the single uncovered short call drives the loss down 1-for-1 with Nifty forever. At 25,100 it would be -300 points (-₹22,500), at 25,300 it would be -500 points (-₹37,500), and so on without limit.

**4.** You most likely **gained**. A call backspread is **net long vega** (you bought two options and sold only one, so you're long more premium and more sensitive to volatility). When implied volatility — proxied by India VIX — jumps, your two long options inflate more than your single short, lifting the mark-to-market value even though price didn't move. The Greek is **vega**. (This is also why you prefer to *enter* backspreads when IV is low and hope it expands.)

**5.** The best fit for a **one-directional big-move bet with limited risk** is a **backspread** (a call backspread if you lean up, a put backspread if you lean down). It profits open-endedly on a strong move in its direction, only loses a small, *defined* amount if the market sits still, and benefits from being **long vega in a low-IV environment** that an election result is likely to expand. A *ratio spread* would be dangerous here precisely because the scenario is a big, uncertain move: the ratio spread's uncovered leg has open-ended loss if the market blasts past the short strike — exactly what an election surprise can do. The backspread caps the downside in the middle valley and has **no naked leg**, making it the safer way to bet on a breakout. (If you truly had no directional lean at all, a long straddle/strangle from Chapters 40–41 would be the pure play; the backspread adds a directional tilt with a smaller cost.)

**6.** Per lot at Nifty 25,100: long 24,000 call = `+1,100`; two short 24,300 calls = `-2 * 800 = -1,600`; net intrinsic = `1,100 - 1,600 = -500` points; plus the `+20` credit = `-480 points = -480 * 75 = -₹36,000` per lot. With **5 lots**: `-36,000 * 5 = -₹1,80,000`. The trader collected only `20 * 75 * 5 = ₹7,500` in credit up front and faced a **₹1.8 lakh loss** — twenty-four times the credit — from a single overnight gap, and it would have been *worse* had Nifty closed higher, since the loss is unbounded. **The lesson:** a credit on a ratio spread is not free money; the uncovered short leg carries naked-call tail risk, and a global gap-up can blow straight through the short strike. Size off the *naked leg's* risk (not the credit), cap the tail at 1–2% of capital, set a hard stop above the short strike, or buy a cheap far-OTM call to convert it to defined risk. Running 5 unhedged lots "because I got paid" is precisely the behaviour behind SEBI's finding that roughly 9 in 10 retail F&O traders lose money.
