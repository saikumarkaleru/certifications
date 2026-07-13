# Chapter 43: The Iron Condor — The Range-Bound Income Trade

Imagine you run a small toll booth on a stretch of highway. You don't care whether traffic flows north or south — you collect a fixed fee from every car that passes through your patch of road, and you pocket it as long as nothing crashes. The iron condor is the options version of that toll booth. You stake out a wide lane around the current Nifty level, collect a premium up front, and you keep that premium as long as Nifty stays inside the lane until expiry. You don't need it to go up. You don't need it to go down. You just need it to *stay home*.

That is why the iron condor is the single most popular income strategy among Indian retail option sellers, especially on weekly expiries. It is a short strangle — selling an out-of-the-money call and an out-of-the-money put — but with two protective "wings" bought further out, which cap the disaster scenario. The result is a four-legged, defined-risk, market-neutral trade that earns a little when the market is boring and loses a known, capped amount when the market is not. The whole art of trading it well is understanding that the boring days pay you slowly, the wild days take it back fast, and survival is entirely about the size of the lane and the size of your position.

## Core concepts

### What an iron condor actually is

An iron condor is built from four options, all on the **same underlying and the same expiry**, in two pairs:

1. **A short put spread (a bull put spread)** below the current price — sell an OTM put, buy a further-OTM put for protection.
2. **A short call spread (a bear call spread)** above the current price — sell an OTM call, buy a further-OTM call for protection.

You *sell* the two inner options (the ones closer to the money) and *buy* the two outer options (the wings). Because the options you sell are more expensive than the ones you buy, the whole package comes in at a **net credit** — money lands in your account the moment you open the trade.

Lay the four strikes out in order, from low to high, and the structure is easy to picture:

- **Long put** (lowest strike — lower wing, protection)
- **Short put** (your lower breakeven zone begins here)
- ... current spot sits in the middle ...
- **Short call** (your upper breakeven zone begins here)
- **Long call** (highest strike — upper wing, protection)

The gap between the two *short* strikes is your **profit zone** — the lane you want price to stay inside. The gap between a short strike and its wing (e.g. short call to long call) is the **wing width**, and it determines how much you can lose.

A quick vocabulary check, since every term must earn its place:

- **OTM (out of the money)** — a call whose strike is above spot, or a put whose strike is below spot; it has no intrinsic value yet.
- **Credit** — net premium received for opening the position (the opposite of a debit, where you pay).
- **Defined risk** — your worst case is a fixed, known number, unlike a naked short option whose loss can balloon.

### Why sell the strangle but buy the wings?

A plain short strangle (sell an OTM call and an OTM put, no wings) collects *more* premium, but its risk is theoretically unlimited on the call side and enormous on the put side. One gap-down or a violent rally can wipe out months of income, and your broker demands a large SPAN margin to hold it.

Buying the wings is like buying cheap insurance on a position you've already sold insurance on. You give up a slice of the premium, but in return your maximum loss becomes **fixed and known** before you enter, and your **margin drops dramatically** because the exchange sees the position is hedged. A naked strangle on Nifty might block well over a lakh of SPAN margin; the same trade as a condor can need a fraction of that, since the exchange only charges you for the capped risk. That lets you size the position to a precise rupee risk, which is the foundation of survival.

The trade-off is real: the wings cost money, so your maximum profit is smaller than a naked strangle's, and the capped loss is still typically several times the credit. The condor doesn't remove risk; it makes risk *legible*.

### The four numbers that define every iron condor

For a condor with **equal wing widths** (the standard, symmetric case), four formulas tell you everything. Let:

- `W` = strike width of each spread (short strike to its wing), in points
- `C` = net credit received, in points per unit

Then:

```
Max profit   = C                          (kept if price expires between the short strikes)
Max loss     = W - C                       (per unit; if either wing is fully breached)
Lower breakeven = short put strike  - C
Upper breakeven = short call strike + C
```

To convert points into rupees, multiply by the **lot size** (currently about 75 for Nifty; this changes over time, so always check the current contract). For example, a credit of 60 points on one Nifty lot is `60 * 75 = ₹4,500` collected.

Notice the lovely symmetry: you profit if the underlying lands anywhere between the two breakevens, which is a band *wider* than the gap between the short strikes (the credit pushes the breakevens outward). You suffer the full `W - C` loss only if price blows clean through a short strike *and* reaches the wing beyond it. Between the short strike and the wing, the loss grows linearly — a partial-loss ramp, not a cliff.

### The payoff shape

The payoff diagram looks like a wide, flat-topped plateau with two downward ramps that level off into flat valleys on each side. The flat top is your maximum profit zone (between the short strikes). The ramps are where one spread goes against you. The flat valleys are the capped maximum loss, where even if price keeps running, the wing has already paid out and your loss stops growing.

![Figure: iron condor payoff](figs/iron_condor.png)

Compare this to a short strangle, whose payoff also has a flat top but then plunges in straight lines forever in both directions — no floor. The wings are what bend those plunging lines back to horizontal. You are trading away the tips of the wings' profit for a hard floor under your losses.

### The Greeks: what you're really short

Every position has a Greek signature — its sensitivity to the underlying's price, to volatility, and to time. The iron condor, held near the centre of its range, is:

- **Positive theta (time decay works for you).** This is the engine. Every day that passes with price sitting inside the range, the options you sold lose value faster than the wings you bought, and that decay is your income. Theta is why the trade is called an "income" strategy.
- **Short vega (you are short volatility).** If implied volatility *rises* — fear spikes, India VIX jumps — all four options inflate, but the inner ones you're short inflate more, and your position loses on a mark-to-market basis even if price hasn't moved. If IV *falls* (a "vol crush", common after an event), you gain. This is why you want to *sell* condors when IV is high.
- **Short gamma (movement hurts you).** Short gamma means that as price moves toward a short strike, your losses accelerate and your delta tilts against you — always leaning the wrong way. It is the mirror image of positive theta: you are paid theta precisely *because* you are short gamma. There is no free lunch.
- **Near-zero delta at the centre (market-neutral).** When price is parked in the middle, the call-side and put-side deltas roughly cancel, so you have little directional exposure. As price drifts toward one side, delta builds against you — the position is only neutral while it stays neutral.

The one-line summary every condor seller should tattoo on their forearm: **you are paid theta to be short gamma and short vega.** You earn slowly while things are calm and pay quickly when they move or when fear rises.

### Ideal conditions: when to actually put one on

The condor is not a strategy for all seasons. It thrives in a specific climate:

1. **High IV rank or IV percentile.** Recall from the volatility chapters that IV rank tells you whether today's implied volatility is high or low *relative to its own past year*. You want to sell options when they are *expensive*, i.e. when IV rank is high (say above 50). High IV does two things for you: it fattens the credit you collect, and it sets up a potential vol crush that profits your short-vega position. Selling condors in a dead-low-IV market is collecting peanuts while taking the same tail risk.
2. **A range-bound or post-event market.** The condor wants calm. Good moments: a market that has been chopping sideways in a defined band; the day *after* a big scheduled event (Budget, RBI policy, election result, major earnings) when the uncertainty has resolved and IV is collapsing. Bad moments: ahead of an unknown binary event, or in a market that is clearly trending hard in one direction.
3. **Enough time, but not too much.** Weekly condors decay fast (good theta) but give price little room to misbehave (bad gamma). Monthly condors decay slower but are more forgiving. Many Indian sellers favour entering with a few days to a couple of weeks left, balancing the two.

### Strike selection by delta

How wide should the lane be? The professional way to choose short strikes is by **delta**, not by gut. The delta of an OTM option is a rough proxy for the market's estimated probability that the option finishes in the money. A 16-delta short call sits roughly one standard deviation away — the market implies about a 16% chance price closes beyond it.

A common, sensible recipe:

- **Short strikes at ~15–20 delta each.** This places them around one standard deviation out on each side, giving a profit zone that price stays inside roughly two-thirds of the time at expiry (before accounting for the credit, which widens the breakevens further). Selling closer (30-delta) collects more premium but gets tested far more often; selling further (10-delta) is safer per trade but the credit shrinks toward not-worth-it.
- **Wings 200–400 points beyond each short strike on Nifty** (or a fixed number of strikes). Wider wings collect a touch more credit and have a lower chance of full breach, but raise the maximum loss and margin. Narrower wings cap loss tighter but cost more credit and pinch the reward.

The width choice is a dial between *probability of profit* and *size of reward*. Tighter lanes (higher-delta shorts) pay more but win less often; wider lanes (lower-delta shorts) win more often but pay less. There is no universally correct setting — only a setting that matches your edge and your stomach.

### Position sizing: the number that actually keeps you alive

Here is the uncomfortable arithmetic of the condor. A typical weekly Nifty condor might collect a credit of, say, 60 points against a wing width of 300 points. That means:

- Max profit per lot: `60 * 75 = ₹4,500`
- Max loss per lot: `(300 - 60) * 75 = ₹18,000`

You are risking ₹18,000 to make ₹4,500 — a reward-to-risk of about 1 to 4. You can be right four times and wrong once and end up flat (before costs). This is the defining feature of premium selling: **you win often but small, and lose rarely but big.** The whole game is making sure the rare big loss doesn't exceed several wins, and never betting so large that one bad week ruins you.

A disciplined sizing rule: risk no more than **1–2% of your trading capital** on the maximum loss of any single condor. With ₹10 lakh of capital and a 2% cap, your max loss per position is ₹20,000 — about one lot of the example above. Traders blow up not because the condor is a bad structure but because they sell ten lots, collect ₹45,000 of lovely credit for weeks, and then meet one gap-down that takes ₹1.8 lakh in a single morning.

### Managing the trade: what to do when one side is tested

A condor is not a "set and forget" trade. Plan your exits *before* you enter. The common management playbook:

- **Take profits early.** Many professional sellers close the position once they've captured **50% of the maximum credit**, rather than squeezing the last rupee. Why? The last bit of profit comes slowly and is exposed to the most gamma risk near expiry. Booking at 50% improves your win consistency and frees capital. (For our 60-point credit, that means buying it all back when it's worth ~30 points.)
- **Set a stop on the loss.** A common rule: exit if the loss reaches **1.5x to 2x the credit received**, rather than waiting for the full max loss. This converts the ugly 1-to-4 ratio into something more survivable — you cut the right tail of your loss distribution.
- **Roll the untested side.** When price drifts toward your short call (the call side is "tested"), the put side has by now decayed to almost nothing. You can **roll the untested put spread up** — close it and re-sell it at higher strikes, closer to the new price — to collect additional credit that offsets the loss building on the call side. This is the bread-and-butter adjustment. It re-centres the position around the new price and widens your effective breakeven, at the cost of narrowing the lane on the safe side (you're taking on a bit more risk to defend).
- **Roll out in time**, or simply **take the loss.** If the move is genuine and one-directional, rolling only digs a deeper hole. The honest, professional move is often to accept the planned, capped loss and move on. The condor's entire premise is that the loss is *defined* — defending a losing trade past your stop just converts a known small loss into a larger one. Knowing when to stop adjusting is the hardest skill.

The golden rule of adjustment: **roll the side that is winning, never throw good money after the side that is losing.** And size small enough that you can afford to be wrong without the adjustment becoming compulsory.

### The Indian weekly iron condor and its honest risk

Weekly expiries made the iron condor a retail phenomenon in India. Every week brings a fresh expiry on Nifty (and other indices on their respective days), the premium-to-time ratio is rich, theta decay is brutal in the final days, and a seller can run the toll booth 50-odd times a year. The marketing is seductive: "earn steady weekly income from the market." Thousands of Indian traders run mechanical weekly condors.

Be brutally honest about the risk, because this is exactly where retail gets hurt. The weekly condor's profit profile is a long line of small green weeks punctuated by occasional large red ones. The math means **a single trending or gapping week can eat several weeks of accumulated credit at once.** Indian markets gap on global cues overnight, on geopolitical shocks, on surprise policy — and an index option is cash-settled and European, so you can't escape an adverse expiry, you simply settle at the closing level. A condor that breaches a wing on expiry day delivers the full `W - C` loss with no recourse.

This is why SEBI's own studies show roughly **9 out of 10 retail F&O traders lose money.** It is not because the iron condor is a scam — it is a legitimate, mathematically sound structure. It is because traders run it too large, sell when IV is low (thin credit, same tail), skip the stop-loss, and mistake a string of lucky calm weeks for skill. The structure is fine; the position sizing and the discipline are where accounts die. Respect the 1-to-4 ratio, respect your sizing cap, and treat every quiet winning week as borrowed time you're being paid for — not a guarantee.

## Worked example (₹, Nifty)

Let's build a concrete weekly Nifty iron condor. Assume:

- **Nifty spot** = 24,000, weekly expiry, India VIX elevated (IV rank high — good condor conditions).
- **Lot size** = 75 (current Nifty lot; verify, as it changes).

We select strikes by delta and structure the four legs:

| Leg | Strike | Type | Action | Premium (points) |
|-----|--------|------|--------|------------------|
| Lower wing | 23,500 | Put | Buy | 30 |
| Short put | 23,700 | Put | Sell | 70 |
| Short call | 24,300 | Call | Sell | 75 |
| Upper wing | 24,500 | Call | Buy | 35 |

**Step 1 — Net credit.** Add the premiums received, subtract the premiums paid:

```
Credit = (70 + 75) - (30 + 35) = 145 - 65 = 80 points
```

In rupees: `80 * 75 = ₹6,000` collected up front. This is your **maximum profit**.

**Step 2 — Wing width.** Each spread is 200 points wide:

```
Put spread:  23,700 - 23,500 = 200 points
Call spread: 24,500 - 24,300 = 200 points
W = 200
```

**Step 3 — Maximum loss.**

```
Max loss = W - C = 200 - 80 = 120 points
        = 120 * 75 = ₹9,000 per lot
```

So this condor risks ₹9,000 to make ₹6,000 — a reward-to-risk of 1 to 1.5, which is unusually favourable because we sold in high IV and chose fairly tight wings. (In low IV the same structure might only credit 40 points, giving a 1-to-4 ratio.)

**Step 4 — Breakevens.**

```
Lower breakeven = short put strike  - C = 23,700 - 80 = 23,620
Upper breakeven = short call strike + C = 24,300 + 80 = 24,380
```

**Step 5 — Read the outcome map.** At expiry (cash-settled at the Nifty closing level):

- **Nifty closes between 23,700 and 24,300** (inside the short strikes): all four options expire worthless, you keep the full ₹6,000. *Maximum profit.*
- **Nifty closes between 23,620 and 24,380** (between the breakevens): you keep *some* of the credit. At exactly a breakeven, you net zero (before costs).
- **Nifty closes below 23,500 or above 24,500** (beyond a wing): full **maximum loss of ₹9,000.**
- **Nifty closes between a short strike and its wing** (e.g. 24,400): partial loss along the ramp. At 24,400 the call spread is 100 points in the money, costing `100 * 75 = ₹7,500`, offset by the ₹6,000 credit — a net loss of ₹1,500.

**Step 6 — Profit zone width.** Your full-profit lane is 600 points wide (23,700 to 24,300), and your break-even lane is 760 points wide (23,620 to 24,380). Nifty needs to stay within roughly +/- 1.6% of spot for the week. With ~16-delta shorts, the market implies that happens around two-thirds of the time — and the collected credit nudges the odds a little further in your favour.

**Costs to remember (India-specific).** This is four legs, so you pay brokerage and exchange fees on all four, plus **STT** (Securities Transaction Tax — charged on the sell side of options on premium, and notably on *exercised/settled* in-the-money options at expiry on the settlement value, which can be a nasty surprise on a breached leg). Always close in-the-money legs *before* expiry where possible to avoid the higher settlement STT. Net these costs out of the ₹6,000 — on a single lot they meaningfully shrink the real take-home.

## Common mistakes / risk note

- **Selling condors in low IV.** Thin credit, same fat tail. If IV rank is low, the premium doesn't compensate you for the gap risk. Wait for richer conditions.
- **Sizing for the credit, not the loss.** Beginners see ₹6,000 income and sell five lots. The relevant number is the ₹9,000 (or larger) *max loss per lot*. Size off the loss, capped at 1–2% of capital.
- **No stop-loss, holding to expiry every time.** The flat valleys are comforting on a diagram, but reaching them means a full loss. Define your exit (e.g. 50% profit target, 2x-credit stop) before entering.
- **Defending a losing trend forever.** Rolling the tested side into a strong trend just enlarges the loss. The condor's gift is a *defined* loss — sometimes the right move is to take it.
- **Ignoring event risk and gaps.** Index options are European and cash-settled; an overnight gap through a wing settles against you with no escape. Avoid holding condors across unhedged binary events.
- **Forgetting STT on settled ITM legs.** A breached short option left to settle can attract STT on the full settlement value — close ITM legs before expiry.
- **Mistaking a lucky streak for skill.** A run of calm weeks is the strategy working *as designed*, not proof you've beaten the market. The bill arrives on the volatile week. Respect the asymmetry.

## Key takeaways

- An iron condor = a short OTM call spread + a short OTM put spread on the same underlying and expiry: a short strangle with protective wings.
- It collects a **net credit** and profits if the underlying stays in a **wide range** between the two short strikes until expiry.
- **Max profit = net credit; max loss = wing width - credit** (defined and capped); breakevens = short put - credit (lower) and short call + credit (upper).
- Greeks: **positive theta, short vega, short gamma, ~zero delta at centre** — you are paid theta to be short gamma and short volatility.
- Ideal conditions: **high IV rank** (rich premium, potential vol crush) and a **range-bound or post-event** market. Pick short strikes by delta (~15–20 delta).
- The reward-to-risk is asymmetric (often 1-to-3 or worse): **win often and small, lose rarely and big.** Size off the max loss, capped at 1–2% of capital.
- The Indian weekly condor is popular and legitimate, but a **single trending or gapping week can erase several weeks of credit** — discipline, sizing, and a stop-loss are what separate survivors from the 90% who lose.

## Practice problems

1. **Structure check.** A trader sells a Bank Nifty iron condor: buy 50,000 put, sell 50,500 put, sell 52,500 call, buy 53,000 call. Which two options are sold, which two are bought, and where is the maximum-profit zone?

2. **Core numbers.** On a Nifty condor you collect a net credit of 50 points. Each wing is 250 points wide. Lot size is 75. Compute (a) max profit per lot in rupees, (b) max loss per lot in rupees, and (c) the reward-to-risk ratio.

3. **Breakevens.** Using a Nifty condor with short put at 23,800, short call at 24,200, and a net credit of 70 points, find the lower and upper breakeven levels and the width of the break-even profit band.

4. **Greeks intuition.** India VIX jumps sharply overnight from 12 to 18, but Nifty opens almost exactly where it closed the previous day. You hold an iron condor. Did your position most likely gain or lose on a mark-to-market basis that morning, and which Greek explains it?

5. **Management decision.** You sold a weekly condor for an 80-point credit. Three days later, with price still comfortably between your short strikes, the position can be bought back for 38 points. What does the common "50% profit target" rule suggest, and why might a professional act on it?

6. **The honest risk.** A trader runs the same weekly Nifty condor (60-point credit, 300-point wings, 75 lot size, 4 lots) and wins eight weeks in a row, then in week nine Nifty gaps and closes beyond a wing. Compute the eight weeks of profit, the week-nine loss, and the net result. What lesson does this illustrate?

## Solutions

**1.** You always sell the *inner* options (closer to spot) and buy the *outer* wings. Here: **sold** = 50,500 put and 52,500 call; **bought** = 50,000 put (lower wing) and 53,000 call (upper wing). The **maximum-profit zone** is between the two short strikes, i.e. Bank Nifty closing anywhere between **50,500 and 52,500** at expiry, where all four options expire worthless and the trader keeps the full credit.

**2.** With credit `C = 50`, wing width `W = 250`, lot = 75:
- (a) Max profit = `C * 75 = 50 * 75 = ₹3,750`.
- (b) Max loss = `(W - C) * 75 = (250 - 50) * 75 = 200 * 75 = ₹15,000`.
- (c) Reward-to-risk = `3,750 : 15,000 = 1 : 4`. You can win four times and lose once and be flat (before costs) — the classic premium-selling asymmetry, and a sign the credit is thin relative to the risk (likely a low-IV environment).

**3.** Breakevens:
- Lower = short put - credit = `23,800 - 70 = 23,730`.
- Upper = short call + credit = `24,200 + 70 = 24,270`.
- Break-even band width = `24,270 - 23,730 = 540 points`. Nifty can close anywhere in this 540-point band and the trade is at worst break-even; the credit widened the profitable zone beyond the 400-point gap between the short strikes.

**4.** You most likely **lost** on a mark-to-market basis, even though price didn't move. The condor is **short vega** — when implied volatility (proxied by India VIX) jumps, all the options inflate, and the inner options you are short inflate more than the wings you own, so the position's buy-back cost rises. The Greek is **vega**. (The flip side: if this VIX spike later collapses with price still in range, the vol crush works in your favour — which is exactly why you prefer to *sell* condors when IV is already high.)

**5.** The 50% profit-target rule says: close when you've captured half the credit. Half of 80 is 40, so buying it back at 38 points captures **42 of the 80 points (~53%)** — past the target. A professional acts because the remaining ~38 points of profit will accrue slowly and is exposed to rising gamma risk as expiry approaches; one adverse move could turn a healthy winner into a loser. Booking now locks in the gain, frees margin for the next trade, and improves win consistency. Take-home so far: `42 * 75 = ₹3,150` per lot (before costs).

**6.** Eight winning weeks at full credit: `8 * 60 * 75 = 8 * 4,500 = ₹36,000` per lot, and with 4 lots = `36,000 * 4 = ₹1,44,000`. Week-nine max loss per lot = `(300 - 60) * 75 = 240 * 75 = ₹18,000`, and with 4 lots = `18,000 * 4 = ₹72,000`. Net over nine weeks = `1,44,000 - 72,000 = +₹72,000` *before costs* — still positive here, but a single bad week erased **half** of two months' accumulated credit in one morning. The lesson: the condor's P&L is a long line of small greens broken by occasional large reds; survival depends entirely on **position size** (4 lots cost ₹72,000 on the bad week — had the trader run 20 lots chasing the steady income, that week would have been a ₹3.6 lakh loss) and on a **stop-loss** that caps the red weeks before they reach the full wing. Run it too large or without a stop, and one trending week takes back everything — the precise mechanism behind SEBI's finding that ~9 in 10 retail F&O traders lose money.
