# Chapter 7: Contract Mechanics in India — Lots, Expiry, Ticks & Strikes

When you buy a kilo of rice, you do not negotiate the price of a single grain. The shop sells in standard packets, the weighing scale moves in fixed steps, and the bill is whatever the packet weighs times the price per kilo. An options contract works the same way. Before you can think about whether the market goes up or down, you have to know the "packet size" you are forced to trade in, the steps the price is allowed to move in, the dates on which the contract dies, and the menu of prices you are allowed to bet on. These are the **contract mechanics**, and on the NSE they are not suggestions — they are hard rules baked into the exchange. Get them wrong and you will misjudge how much money is actually on the table.

This is the plumbing chapter. It is less glamorous than Greeks or strategies, but every rupee of profit or loss you ever make flows through these pipes. A trader who internalises lots, notional value, expiry cycles, ticks, and strike intervals can glance at a Nifty option quote and instantly know the cash outlay, the risk, and what a one-point move is worth.

## Core concepts

### The lot size: you trade in bundles, not single units

An option does not trade one unit at a time. The exchange bundles a fixed number of underlying units into one **lot**, and the lot is the smallest quantity you can buy or sell. You can trade 1 lot, 2 lots, 17 lots — but never half a lot, and never a single share or index point on its own.

Think of it like an egg tray. The shop will not sell you one egg; it sells trays of 30. The "lot size" of eggs is 30. If you want 45 eggs you cannot have them — you buy one tray (30) or two trays (60). Options are the same. For Nifty, one lot is currently about 75 units of the index. For Bank Nifty it is currently about 30 units. (These numbers are revised periodically by the NSE, so always treat them as "currently about" and check the contract specification before trading — exchanges adjust lot sizes to keep the rupee value of one contract within a target band as index levels drift up or down.)

So when a quote screen says the Nifty 24000 call is trading at ₹150, that ₹150 is the premium **per unit of the index**. You are not paying ₹150. You are paying:

```
Cash outlay = premium per unit * lot size
            = 150 * 75
            = ₹11,250 for one lot
```

This single multiplication trips up more beginners than any Greek ever will.

### Why exchanges set the lot size

Why not just let people trade one index unit? Two reasons, both about keeping the market orderly.

1. **Standardisation and liquidity.** If everyone trades the same standard quantity, buyers and sellers match easily. A market where one person wants 17 units and another wants 4 would be a mess. Fixed lots make every contract fungible — interchangeable — so an exchange-traded option is as standardised as a currency note.

2. **Keeping the contract "serious" but not absurd.** SEBI and the NSE try to keep the rupee value of one lot within a sensible range — historically a few lakh rupees of notional exposure. This is deliberate. If a single lot were worth only ₹5,000 of exposure, the market would fill with tiny, casual punts. If it were worth ₹50 lakh, ordinary participants could not trade at all. As the index rises over the years, the same lot size represents more rupees, so periodically the exchange **cuts** the lot size to bring the rupee value back into the target band. That is why lot sizes are not constants — they are policy levers.

### Notional value: the two numbers that matter

There are two different "sizes" of an options position, and confusing them is dangerous.

**Premium outlay** is the cash that actually leaves your account to buy the option (or the margin you post to sell it). It is small.

**Contract notional value** is the rupee value of the underlying that the contract controls. It is large. This is your true economic exposure — the amount you are effectively long or short in the market.

```
Premium outlay   = premium * lot size
Contract notional = spot price * lot size
```

Suppose Nifty spot is at 24,000 and the lot size is 75:

```
Contract notional = 24000 * 75 = ₹18,00,000
```

One Nifty option lot controls about ₹18 lakh of index. You might pay only ₹11,250 in premium for it, but you are economically exposed to an ₹18 lakh basket. This gearing — controlling ₹18 lakh with ₹11,250 — is **leverage**, and it is exactly why options can multiply both gains and losses so violently. Always know your notional, not just your premium. A trader who thinks "I only risked ₹11,250" has understood half the picture; the position behaves like an ₹18 lakh stake in the market.

### Expiry: every contract has a death date

An option is a wasting asset with an appointment with the undertaker. The **expiry date** is the day the contract settles and ceases to exist. After expiry, the option is gone — either it had value (it was in-the-money and you receive the cash difference) or it expired worthless.

Indian index options are **European style** and **cash-settled**. European means you can only exercise *at* expiry, not before (though you can always sell the option in the market beforehand). Cash-settled means no shares change hands — at expiry the exchange simply credits or debits the cash difference between the strike and the final settlement price. (Single-stock options, by contrast, are physically settled — actual shares are delivered — which is a separate and important complication covered elsewhere.)

### Weekly versus monthly expiries — the Indian landscape

India runs two parallel expiry rhythms on its indices.

- **Monthly expiry.** Every index has a monthly contract that expires once a month. Historically this is the last business day of a designated week of the month. The monthly series has been around since the start of F&O and remains the deepest, most liquid contract for positional traders.

- **Weekly expiry.** Layered on top, the major indices also offer contracts that expire every week. Weeklies were introduced to give traders short-dated, low-premium instruments — a weekly option costs less than a monthly because it has less time value (less time for the market to move), so they became enormously popular with retail traders for short-term bets and for selling premium.

The exact weekly-expiry landscape in India has been **changing**, so treat any specific list of "which index expires on which weekday" as a snapshot, not a law. In 2024–2025, SEBI moved to **rationalise** the explosion of weekly expiries, concerned that a different index expiring almost every day of the week was encouraging excessive, lottery-like retail speculation (recall the SEBI finding that roughly 9 in 10 retail F&O traders lose money). The broad direction of regulation has been to **limit each exchange to one weekly-expiry benchmark index** and to nudge expiry days around. Because this is live policy, the correct professional habit is: **check the current NSE circular for the expiry calendar before you trade**, rather than relying on what was true last year. The *concept* — a weekly cadence plus a monthly cadence — is stable; the *details* are not.

### Expiry-day conventions

A few conventions you must hold in your head:

- **Settlement price.** For cash-settled index options the final settlement value is not the last traded tick. It is typically a **time-weighted average** of the underlying index over the closing window (for example, the average of the index over roughly the last half-hour of the expiry day). This averaging stops a single manipulated print from deciding crores of payoffs. So on expiry day your option does not settle at the dramatic closing spike you see on screen — it settles at the smoother average.

- **The weekly that coincides with the monthly.** In the week that contains the monthly expiry, the weekly and monthly expiries fall on the same day. There is no separate "extra" contract that week — the monthly *is* that week's weekly.

- **Holidays.** If an expiry day is a trading holiday, expiry shifts to the **previous** trading day. Always read the official holiday-adjusted calendar.

### Tick size: the smallest allowed price step

Just as a ruler only marks down to the millimetre, an option price can only move in fixed increments called the **tick size**. On NSE options the tick is currently ₹0.05 (five paise). You cannot quote an option at ₹150.02 or ₹150.131 — the legal prices are ₹150.00, ₹150.05, ₹150.10, and so on.

Why have ticks at all? A tick imposes a minimum grid so that orders queue and match cleanly and so that the bid–ask spread cannot be sliced into meaningless fractions. The rupee value of one tick on a single lot is:

```
Value of one tick = tick size * lot size
```

For a Nifty lot of 75: `0.05 * 75 = ₹3.75` per tick. That is the smallest price flicker your one-lot position can register. It sounds trivial, but for a high-frequency seller trading hundreds of lots, ticks are the very grain of profit.

### One-point move: what the underlying is worth

The most useful back-of-envelope number a trader can carry is **the rupee value of a one-point move in the underlying**, per lot. Because the option's value is ultimately driven by the index, and the lot multiplies everything:

```
Rupee value of a 1-point index move = 1 * lot size
```

For Nifty (lot 75): a 1-point move in Nifty = ₹75 per lot. So if Nifty moves 100 points your way and you hold a position with full exposure (say a deep in-the-money option behaving nearly one-for-one with the index), that is roughly `100 * 75 = ₹7,500` per lot. For Bank Nifty (lot 30): a 1-point move = ₹30 per lot; a 200-point Bank Nifty swing is about `200 * 30 = ₹6,000` per lot.

A subtlety: an option does not move one-for-one with the index unless it is very deep in-the-money. How much the premium moves per index point is governed by **delta** (covered in the Greeks chapters). The "lot size in rupees per point" above is the *maximum* sensitivity — what you get when delta is 1. A premium with delta 0.5 captures only about half: `0.5 * 1 * 75 = ₹37.50` per index point per lot. Keep the two ideas separate: lot size converts index points to rupees; delta converts index points to premium points.

### The contract cycle: near, next and far month

At any moment, several monthly contracts trade side by side. The **contract cycle** is the rolling set of available expiries:

- **Near month** — the contract expiring soonest. Most liquid, tightest spreads, where most action lives.
- **Next month** — the one expiring after the near month.
- **Far month** — the third in line.

As the near month expires and disappears, a new far month is introduced, so there are always three monthly series rolling forward (plus the weekly contracts for indices). When traders speak of "rolling" a position, they mean closing the expiring contract and reopening it in a later month to stay in the trade.

### Strike-price intervals: the menu of bets

For each expiry you are not free to pick any strike you like. The exchange lists strikes at fixed **intervals** around the current spot. For Nifty, strikes are commonly spaced 50 points apart (…23900, 23950, 24000, 24050…); for Bank Nifty, commonly 100 points apart (…51800, 51900, 52000…). The exchange always keeps a generous ladder of strikes both above and below the spot — typically many in-the-money and many out-of-the-money strikes — and adds new strikes if the index trends far enough that the ladder needs extending.

Tighter strike spacing (Nifty's 50) gives you finer control to target a precise level; wider spacing (Bank Nifty's 100) reflects its larger absolute level and faster moves. The interval is part of the contract specification, so confirm it on the NSE rather than assuming.

## Worked example (₹, Nifty & Bank Nifty)

**Setup.** It is a normal trading day. Nifty spot is 24,000 and Bank Nifty spot is 52,000. Assume Nifty lot size 75 and Bank Nifty lot size 30 (current approximate values). You are looking at two trades.

**Trade A — Buy 2 lots of the Nifty 24,200 weekly call at a premium of ₹120.**

Step 1 — Cash outlay (premium):
```
Per lot   = premium * lot size = 120 * 75 = ₹9,000
Two lots  = 9,000 * 2          = ₹18,000
```
You pay ₹18,000 to enter. This is also your **maximum loss** as a buyer — if Nifty stays below 24,200 at expiry the calls expire worthless and you lose the full ₹18,000, nothing more.

Step 2 — Notional exposure:
```
Per lot   = spot * lot size = 24000 * 75 = ₹18,00,000
Two lots                                  = ₹36,00,000
```
Your ₹18,000 premium controls ₹36 lakh of Nifty. That is the leverage you have taken on.

Step 3 — Value of a one-point move:
```
1 Nifty point = lot size = ₹75 per lot
Two lots                  = ₹150 per point
```
At expiry, the call's intrinsic value is `max(spot - 24200, 0)`. Suppose Nifty closes (on the averaged settlement) at 24,500. Intrinsic value per unit = `24500 - 24200 = 300`.
```
Payoff per lot = 300 * 75 = ₹22,500
Two lots       = ₹45,000
Net profit     = payoff - premium = 45,000 - 18,000 = ₹27,000
```
Breakeven was `strike + premium = 24200 + 120 = 24,320`. Above that you profit; between 24,200 and 24,320 you recover part of the premium; below 24,200 you lose all of it.

**Trade B — Sell (write) 1 lot of the Bank Nifty 52,000 weekly put at a premium of ₹250.**

Step 1 — Premium received:
```
Premium credit = 250 * 30 = ₹7,500
```
This ₹7,500 is your **maximum profit**. As a seller you keep it only if Bank Nifty stays at or above 52,000 at expiry.

Step 2 — Notional and risk. The contract notional is `52000 * 30 = ₹15,60,000`. Unlike the buyer, the seller's risk is large: if Bank Nifty crashes, the put gains value against you almost without limit (down to a Bank Nifty of zero in the extreme). If Bank Nifty settles at 51,400:
```
Intrinsic value per unit = 52000 - 51400 = 600
Loss per lot             = 600 * 30      = ₹18,000
Net result               = premium - loss = 7,500 - 18,000 = -₹10,500
```
You collected ₹7,500 but lost ₹18,000 of value — a net loss of ₹10,500 on a single 600-point move. This asymmetry — small fixed gain, large variable loss — is the heart of option selling, and why sellers must post **SPAN + exposure margin** (a large margin reflecting that downside) rather than just the premium.

Step 3 — Tick check. One tick on the Bank Nifty put is `0.05 * 30 = ₹1.50` per lot. Small, but it sets the minimum spread you cross every time you enter or exit.

## Common mistakes / risk note

- **Confusing premium with cost.** Beginners see "₹120" and think the trade costs ₹120. It costs `₹120 * lot size`. Always multiply by the lot before you decide if you can afford the trade.
- **Ignoring notional / leverage.** "I only put in ₹18,000" hides the fact that you are exposed to ₹36 lakh of index. Size your position by notional and worst-case loss, not by premium paid.
- **Assuming the option moves point-for-point with the index.** It does not, unless deeply in-the-money. The lot converts *index points* to rupees; **delta** converts *index points* to *premium points*. Out-of-the-money options can barely move on a modest index wiggle.
- **Trusting a stale expiry calendar.** Weekly expiry days and which indices carry them have been changing under SEBI rationalisation. Read the current NSE circular every time; do not rely on last year's weekday.
- **Forgetting expiry settles on an average, not the close.** Your in-the-money option settles on the closing-window time-weighted average of the underlying, which can differ from the dramatic last tick on screen.
- **The honest risk.** These mechanics make options easy to access but they do not make them easy to win. Most long options expire worthless because the index does not move enough in time. Option *selling* offers a high probability of a small gain but exposes you to large, sometimes uncapped losses — exactly the Trade B asymmetry. SEBI studies have repeatedly found that roughly 9 in 10 retail F&O traders lose money. Knowing the plumbing protects you; it does not give you an edge by itself.

## Key takeaways

- You trade in **lots**, never single units. Lot size is currently about 75 for Nifty and about 30 for Bank Nifty, and is revised by the exchange over time.
- **Premium outlay = premium * lot size**; **contract notional = spot * lot size**. The first is the cash you pay; the second is your true economic exposure (your leverage).
- Indian index options are **European and cash-settled**, settling on a time-weighted average of the underlying over the closing window.
- India runs **weekly + monthly** expiry cadences; the precise weekly landscape is under SEBI rationalisation and changing — confirm the current calendar each time.
- **Tick size** (currently ₹0.05) is the smallest legal price step; one tick is worth `tick * lot size` in rupees.
- **A one-point index move is worth `lot size` rupees per lot** (₹75 Nifty, ₹30 Bank Nifty) at delta 1; multiply by delta for the option's actual sensitivity.
- Three monthly series (**near/next/far**) roll forward continuously; strikes are listed at fixed intervals (about 50 for Nifty, 100 for Bank Nifty) around spot.

## Practice problems

1. **(Conceptual.)** Explain in one or two sentences the difference between the *premium outlay* and the *contract notional value* of a single option lot, and why a trader must track both.

2. **(Numeric.)** Nifty spot is 23,800, lot size 75. You buy 3 lots of a call at a premium of ₹95. What is your total cash outlay, and what is your maximum possible loss?

3. **(Numeric.)** For the position in problem 2, what is the total contract notional you control across the 3 lots? Express the leverage as notional-to-outlay ratio.

4. **(Numeric.)** Bank Nifty lot size is 30. You hold 2 lots and Bank Nifty rises by 180 points. Assuming your position behaves one-for-one with the index (delta ≈ 1), what is your rupee gain? What would it be if delta were only 0.4?

5. **(Numeric.)** You sell 1 lot of a Nifty 24,000 put for ₹140 (lot 75). Nifty settles at 23,750. Compute the premium received, the option's intrinsic value at settlement, and your net profit or loss.

6. **(Conceptual.)** A friend says, "Weeklies always expire on Thursday for every index, so I planned my whole strategy around Thursdays." What is wrong, or at least risky, about relying on that statement today?

## Solutions

**1.** The *premium outlay* is the actual cash that leaves your account to buy the option — `premium * lot size` — and for a buyer it is also the maximum loss. The *contract notional value* is `spot * lot size`, the rupee value of the underlying basket the contract controls, i.e. your true market exposure. You must track both because the small premium hides large leveraged exposure; risk and position sizing must be judged on notional and worst-case loss, not on the cash paid.

**2.** Outlay per lot = `95 * 75 = ₹7,125`. Three lots = `7,125 * 3 = ₹21,375`. As an option **buyer**, your maximum possible loss equals the full premium paid: **₹21,375** (the calls expire worthless if Nifty finishes at or below the strike).

**3.** Notional per lot = `23,800 * 75 = ₹17,85,000`. Three lots = `17,85,000 * 3 = ₹53,55,000`. Leverage ratio = `53,55,000 / 21,375 ≈ 250.5`. You are controlling roughly **₹53.55 lakh of Nifty with ₹21,375**, about 250 times leverage on a premium basis — a vivid reminder of how much exposure sits behind a small premium.

**4.** One point per lot = ₹30, so 2 lots = ₹60 per point. At delta ≈ 1: `180 * 60 = ₹10,800` gain. At delta 0.4 the premium captures only 40% of the index move: `0.4 * 180 * 60 = ₹4,320`. This shows the difference between the lot's point-value and the option's actual sensitivity through delta.

**5.** Premium received = `140 * 75 = ₹10,500` (this is the maximum profit). Intrinsic value at settlement = `max(strike - spot, 0) = max(24,000 - 23,750, 0) = 250` per unit, so value owed = `250 * 75 = ₹18,750`. Net result = `premium - payoff = 10,500 - 18,750 = -₹8,250`, a **loss of ₹8,250**. The seller collected ₹10,500 but a 250-point adverse move cost ₹18,750 — the classic small-gain / large-loss asymmetry of writing options.

**6.** Two problems. First, different indices have historically expired on *different* weekdays, so "every index on Thursday" was never universally true. Second and more important, the Indian weekly-expiry calendar has been actively **changing** under SEBI's rationalisation of weekly expiries — expiry weekdays and which indices carry weeklies have shifted. Hard-coding a strategy to a fixed weekday is fragile; the disciplined approach is to read the current NSE expiry circular each cycle and adjust, because the *concept* (a weekly cadence) is stable but the *specific day* is policy that moves.
