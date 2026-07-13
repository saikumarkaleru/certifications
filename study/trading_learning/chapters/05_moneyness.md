# Chapter 5: Moneyness — ITM, ATM & OTM

Imagine you hold a coupon that lets you buy a smartphone for ₹20,000. If the phone currently sells for ₹35,000 in the market, your coupon is obviously valuable — you could buy at ₹20,000 and immediately be ₹15,000 richer. If the phone sells for exactly ₹20,000, the coupon is worth using but gives you no instant gain. And if the phone sells for ₹12,000, your coupon is pointless today — why use it to pay ₹20,000 when the open market is cheaper? That single idea — *where the current price sits relative to your locked-in strike price* — is called **moneyness**, and it is one of the most important lenses through which professional traders look at every option.

Moneyness sounds like a casual word, but it carries precise, practical consequences. It tells you how much of an option's premium is "real" value you could cash in today versus pure hope. It previews how fast the option's price will move when the index moves. It decides whether you are buying a cheap lottery ticket or an expensive, high-probability position. Master moneyness and you stop guessing at strikes; you start *choosing* them.

## Core concepts

### The three buckets: ITM, ATM, OTM

Every option, the moment you look at it, falls into one of three buckets depending on the **spot price** (the current market level of the underlying, e.g. Nifty) relative to its **strike price** K (the fixed price written into the contract).

- **In-the-money (ITM):** the option already has real, exercisable value baked in. Exercising it right now would put money in your pocket (ignoring premium paid).
- **At-the-money (ATM):** the strike is (roughly) equal to the spot price. There is essentially no instant exercise gain, but the option sits right at the knife's edge.
- **Out-of-the-money (OTM):** the option has no exercisable value today. It is pure potential — it only pays off if the market moves your way before expiry.

The crucial twist for beginners: **calls and puts are mirror images.** A call profits when the market goes *up*, so a call is ITM when spot is *above* the strike. A put profits when the market goes *down*, so a put is ITM when spot is *below* the strike. Forgetting this mirror is the single most common moneyness mistake.

### The defining table

Let S = spot price and K = strike price. Here is the rule, exactly:

| Moneyness | Call option | Put option |
|---|---|---|
| **In-the-money (ITM)** | S > K (spot above strike) | S < K (spot below strike) |
| **At-the-money (ATM)** | S = K (approximately) | S = K (approximately) |
| **Out-of-the-money (OTM)** | S < K (spot below strike) | S > K (spot above strike) |

A memory hook: **a call wants to "call" the price up; a put wants to "put" the price down.** A call is happy (ITM) when spot has climbed above its strike. A put is happy (ITM) when spot has fallen below its strike. Whatever makes a call ITM makes the put at the same strike OTM, and vice versa — at any single strike, the call and the put are always on opposite sides of the money (except exactly at the money, where both are ATM).

In real markets the spot rarely lands exactly on a listed strike, so traders use **near-the-money** loosely for the strike closest to spot, and reserve ATM for "the nearest available strike." On the NSE, Nifty strikes are listed every 50 points (50-point intervals near the money) and Bank Nifty every 100 points, so when Nifty trades at 24,037 the 24,050 or 24,000 strike is treated as ATM.

### Intrinsic value vs time value — moneyness made quantitative

Recall from earlier chapters that an option's premium splits into two parts:

`Premium = Intrinsic value + Time value`

**Intrinsic value** is exactly the moneyness measured in rupees — the guaranteed payoff if expiry were *right now*. It can never be negative (you would simply not exercise a losing option):

- `Intrinsic value (call) = max(S - K, 0)`
- `Intrinsic value (put) = max(K - S, 0)`

**Time value** (also called extrinsic value) is everything left over — the premium you pay above intrinsic, representing the *chance* that the option moves further into profit before expiry:

`Time value = Premium - Intrinsic value`

Now connect this to the three buckets:

- **OTM options have zero intrinsic value.** Their entire premium is time value — 100% hope. A 24,200 call when Nifty is at 24,000 cannot be exercised for a gain today; whatever you pay for it is purely the market pricing the chance it finishes above 24,200.
- **ITM options have positive intrinsic value plus some time value.** A 23,800 call when Nifty is 24,000 already holds ₹200 of intrinsic value; the premium will be ₹200 plus a smaller time-value cushion.
- **ATM options have zero (or near-zero) intrinsic value but the *largest* time value of any single strike.**

That last point surprises beginners, so it deserves its own explanation.

### Why the ATM option carries the most time value

Time value is the market's price for *uncertainty about which side of the strike you'll finish on*. The more genuinely uncertain that outcome, the more an option is worth beyond its intrinsic value.

Think about where uncertainty is greatest:

- **Deep OTM (say a 25,000 call, Nifty at 24,000):** almost certainly finishes worthless. There is little uncertainty — the answer is "probably zero." So time value is small in absolute rupees.
- **Deep ITM (say a 22,000 call, Nifty at 24,000):** almost certainly finishes in the money and behaves like the index itself. Again little uncertainty — the answer is "almost surely worth about ₹2,000." So time value is small.
- **ATM (a 24,000 call, Nifty at 24,000):** maximum suspense. A coin-flip whether it ends ITM or OTM. A move in either direction flips its fate. This is exactly where the *optionality* — the right but not the obligation — is most valuable.

A useful analogy: time value is like the betting interest in a cricket match. A lopsided match (deep ITM or deep OTM) attracts little betting action because the result feels settled. A perfectly even contest (ATM) draws the most money because either side could win. The ATM strike is the "even match," so it commands the richest time-value premium.

This is why option *sellers* who want to collect the fattest premium per unit of width gravitate to ATM and near-ATM strikes, and why straddle buyers (who buy the ATM call and put together) are paying for the maximum possible time value. It also means the ATM option suffers the largest **theta** — time decay in rupees — because that big time-value cushion must melt to zero by expiry.

### Moneyness and delta (a preview)

**Delta** is the rate at which an option's price changes for a one-point move in the underlying — roughly, "how many rupees the option gains if Nifty rises one point." Delta also doubles as a rough, market-implied probability that the option finishes ITM. Moneyness maps almost directly onto delta:

- **Deep ITM call:** delta near +1.0. It moves nearly one-for-one with the index — it behaves like owning the index outright. Market says "very likely to finish ITM."
- **ATM call:** delta near +0.5. A move up or down is a coin-flip, so the option captures about half the index's move. Market says "about 50/50."
- **Deep OTM call:** delta near 0.0. The index can wiggle and the option barely reacts. Market says "very unlikely to finish ITM."

Puts have negative delta (they rise when the market falls): a deep ITM put approaches -1.0, an ATM put about -0.5, and a deep OTM put about 0.0. The headline takeaway, which we develop fully in the Greeks chapters, is simple: **moneyness is delta in words.** When a trader says "I want a 30-delta call," they are precisely specifying an OTM strike — and they are saying "roughly a 30% chance this finishes in the money."

### The cost / leverage / probability trade-off

Here is where moneyness becomes a trading decision rather than a definition. Suppose you are bullish on Nifty for the week. You can express that view by buying a call at *any* strike — but the choice of moneyness sets three dials at once, and they always trade off against each other:

1. **OTM (cheap "lottery tickets"):** low premium, high leverage, low probability. You pay very little, so a big favourable move multiplies your money many times over. But most of the time the option expires worthless. This is the classic retail trap — buying far-OTM weekly Nifty calls for ₹15–30 because they "look cheap" and dreaming of a 10-bagger, while the base rate of success is brutally low.

2. **ATM (balanced):** moderate premium, moderate leverage, ~50% probability. The most responsive option to the *next* move (highest gamma, which we cover later), but also the costliest in pure time value and the fastest to decay if the market stalls.

3. **ITM (expensive, high-probability):** high premium (because you are pre-paying intrinsic value), lower percentage leverage, high probability of finishing ITM. You behave more like someone who simply owns the index, but with a capped downside (the premium) and less capital than buying futures. You are buying *certainty of direction* rather than *explosiveness*.

There is no free lunch hiding in any of these. The cheap OTM option is cheap precisely *because* it usually loses. The expensive ITM option is expensive precisely *because* it usually wins. The market prices each strike so that, on average, none is a giveaway. Choosing moneyness is choosing your *style* of being right — explosive-but-rare versus reliable-but-modest — not finding a loophole.

A practical rule professionals internalise: **match moneyness to conviction and time.** Strong, fast directional conviction with a clear catalyst → ATM or slightly OTM for responsiveness. High-confidence, lower-volatility directional view where you mainly want exposure → ITM. "I just feel lucky" → that is the deep-OTM lottery ticket, and you should size it like a lottery ticket (tiny).

## Worked example (₹, Nifty)

Let's build a full **strike ladder** with Nifty spot at **24,000**, looking at the weekly expiry, across three strikes — 23,800, 24,000 and 24,200 — for both calls and puts. (Premiums below are illustrative but realistic for a typical ~12–13% India VIX week.) The Nifty lot size is currently 25 (it changes periodically), so multiply any premium by 25 for the cash cost of one lot.

**Step 1 — classify each option's moneyness.** Spot S = 24,000.

| Strike K | Call moneyness | Put moneyness |
|---|---|---|
| 23,800 | ITM (S > K) | OTM (S > K) |
| 24,000 | ATM (S = K) | ATM (S = K) |
| 24,200 | OTM (S < K) | ITM (S < K) |

**Step 2 — compute intrinsic value.** Using `max(S - K, 0)` for calls and `max(K - S, 0)` for puts:

| Strike | Call intrinsic | Put intrinsic |
|---|---|---|
| 23,800 | max(24000-23800,0) = **₹200** | max(23800-24000,0) = **₹0** |
| 24,000 | max(0,0) = **₹0** | max(0,0) = **₹0** |
| 24,200 | max(24000-24200,0) = **₹0** | max(24200-24000,0) = **₹200** |

**Step 3 — split a quoted premium into intrinsic + time value.** Suppose the market quotes these premiums:

| Strike | Call premium | Call intrinsic | Call time value | Put premium | Put intrinsic | Put time value |
|---|---|---|---|---|---|---|
| 23,800 | ₹260 | ₹200 | ₹60 | ₹62 | ₹0 | ₹62 |
| 24,000 | ₹150 | ₹0 | **₹150** | ₹148 | ₹0 | **₹148** |
| 24,200 | ₹64 | ₹0 | ₹64 | ₹258 | ₹200 | ₹58 |

Notice the pattern the theory predicted:

- The **ATM strike (24,000)** carries the **largest time value** on both the call (₹150) and the put (₹148). The richest "pure optionality" sits right at the money.
- The **OTM options** (23,800 put, 24,200 call) are made *entirely* of time value (₹62 and ₹64) — all hope, no instant worth.
- The **ITM options** (23,800 call, 24,200 put) carry their ₹200 intrinsic value plus a *thinner* time-value sliver (₹60 and ₹58) than the ATM strike.

**Step 4 — read off the leverage/probability trade-off.** Per lot of 25:

- The **24,200 OTM call** costs 64 * 25 = **₹1,600**. If Nifty rips to 24,500 by expiry, it's worth (24500-24200) = ₹300, i.e. 300 * 25 = ₹7,500 — a ~4.7x gain on ₹1,600. Explosive. But if Nifty merely drifts to 24,150, it expires worthless: total loss. Low cost, high leverage, low probability.
- The **23,800 ITM call** costs 260 * 25 = **₹6,500**. The same move to 24,500 makes it worth (24500-23800) = ₹700, i.e. ₹17,500 — a 2.7x gain. Less explosive in percentage terms, but if Nifty just stays flat at 24,000 it's still worth its ₹200 intrinsic (₹5,000 back), losing only the ₹60 time value. High cost, lower leverage, far higher probability of retaining value.
- The **24,000 ATM call** at 150 * 25 = ₹3,750 sits in between — the most responsive to the *next* point of movement, but it bleeds the full ₹150 of time value if Nifty is pinned at 24,000 on expiry day.

Same bullish view, three completely different risk profiles — chosen entirely by moneyness.

## Common mistakes / risk note

- **Mixing up calls and puts.** "Spot is above strike, so the put is in-the-money" — wrong. Above strike is ITM for the *call*, OTM for the *put*. Re-anchor on the table every time until it's reflex.
- **Thinking OTM options are "cheap" in any meaningful sense.** A ₹20 far-OTM Nifty weekly call is not a bargain; it is cheap because the market judges it almost certain to expire worthless. SEBI's studies repeatedly show that roughly **9 out of 10 retail F&O traders lose money**, and a large share of that damage comes from repeatedly buying cheap OTM weekly options that decay to zero. Cheap is not the same as good value.
- **Confusing "ATM = safe."** ATM options are the most balanced, but they also carry the most time value and therefore the **fastest rupee theta decay**. If the market doesn't move, an ATM long option bleeds value quickest of all. Buyers of ATM straddles before a flat expiry learn this painfully.
- **Forgetting that index options are European and cash-settled.** On the NSE, Nifty and Bank Nifty options cannot be exercised early; "intrinsic value" is what you'd collect *at expiry*, settled in cash, not something you can crystallise mid-week by exercising. Stock options, by contrast, are physically settled — an ITM stock option at expiry can mean you must take or give delivery of shares, with the full contract value and STT consequences.
- **Ignoring the seller's mirror risk.** Everything attractive about selling fat ATM time value comes with **large, potentially undefined risk** if the market moves hard against you. Moneyness that looks comfortably OTM today can be deep ITM after one gap-up, turning a small collected premium into a large loss.

## Key takeaways

- **Moneyness = where spot sits relative to strike.** Calls: ITM above, OTM below. Puts: ITM below, OTM above. They are exact mirrors.
- **Intrinsic value is moneyness in rupees**: `max(S-K,0)` for calls, `max(K-S,0)` for puts. OTM options have zero intrinsic value — 100% time value.
- **The ATM strike carries the most time value** because outcome uncertainty (and thus optionality) peaks there; it also decays fastest.
- **Moneyness ≈ delta ≈ probability of finishing ITM:** deep ITM ~ delta 1.0 (or -1.0 for puts), ATM ~ 0.5, deep OTM ~ 0.
- **Choosing a strike is choosing a trade-off:** cheap OTM = high leverage / low odds; ITM = high cost / high odds; ATM = balanced but maximum time-value bleed.
- **Cheap OTM lottery tickets are cheap for a reason** — most expire worthless. Match moneyness to your conviction and time horizon, and size lottery tickets small.

## Practice problems

1. **Classify the ladder.** Bank Nifty spot is at 52,000. For the 51,500, 52,000 and 52,500 strikes, state the moneyness (ITM/ATM/OTM) of both the call and the put at each strike.

2. **Intrinsic and time value.** A Nifty 23,900 call trades at ₹185 with Nifty spot at 24,000. What is its intrinsic value and its time value? Is it ITM, ATM or OTM?

3. **Spot the richest time value.** With Nifty at 24,000, three calls quote: 23,800 at ₹255, 24,000 at ₹150, 24,200 at ₹66. Compute the time value of each and confirm which strike carries the most. Explain in one line *why* that strike does.

4. **Leverage vs probability.** Nifty is at 24,000 (lot size 25). You are bullish and choose between a 24,200 call at ₹64 and a 23,800 call at ₹260. Nifty closes at 24,400 on expiry. Compute the rupee profit/loss per lot for each, and the percentage return. Which gave more leverage, and what did you give up to get it?

5. **The put mirror.** Nifty is at 24,000. A trader says "the 24,300 put is out-of-the-money." Is the trader correct? State the put's intrinsic value, and say what the 24,300 *call* moneyness is.

6. **Conceptual.** A beginner buys far-OTM Nifty weekly calls every week because "they only cost ₹15, so my risk is tiny." Explain, using moneyness and probability, why this is a losing strategy on average despite the small per-trade cost.

## Solutions

**1.** With Bank Nifty spot S = 52,000:

| Strike | Call | Put |
|---|---|---|
| 51,500 | ITM (S > K) | OTM |
| 52,000 | ATM (S = K) | ATM |
| 52,500 | OTM (S < K) | ITM |

A call is ITM when spot is above the strike; the put at that same strike is the opposite. At 52,000, spot equals strike, so both call and put are ATM.

**2.** Intrinsic value of a call = `max(S - K, 0) = max(24000 - 23900, 0) = ₹100`. Time value = Premium - Intrinsic = 185 - 100 = **₹85**. Since spot (24,000) is above the strike (23,900), the call is **ITM**.

**3.** Time value = premium - intrinsic, where only the 23,800 call has intrinsic value (`24000 - 23800 = ₹200`):

- 23,800 call: 255 - 200 = ₹55 time value.
- 24,000 call: 150 - 0 = **₹150 time value**.
- 24,200 call: 66 - 0 = ₹66 time value.

The **24,000 (ATM)** strike carries the most time value. *Why:* outcome uncertainty is greatest exactly at the money — it's a coin-flip whether it finishes ITM or OTM — so the market prices the most optionality (and thus the most time value) there.

**4.** Per lot of 25:

- **24,200 call (OTM), cost ₹64:** at expiry Nifty 24,400 → intrinsic = 24400 - 24200 = ₹200. Profit per share = 200 - 64 = ₹136 → per lot = 136 * 25 = **₹3,400 profit**. Return = 136 / 64 ≈ **+213%**.
- **23,800 call (ITM), cost ₹260:** at expiry intrinsic = 24400 - 23800 = ₹600. Profit per share = 600 - 260 = ₹340 → per lot = 340 * 25 = **₹8,500 profit**. Return = 340 / 260 ≈ **+131%**.

The **OTM call gave more leverage** (213% vs 131% on far less capital, ₹1,600 vs ₹6,500). What you gave up: probability and safety. Had Nifty closed at, say, 24,150, the OTM 24,200 call would expire **worthless (-100%)**, while the ITM 23,800 call would still be worth ₹350 intrinsic — a profit. Higher leverage was bought with a much higher chance of total loss.

**5.** The trader is **incorrect.** A put is ITM when spot is *below* the strike. Here spot (24,000) is below 24,300, so the 24,300 put is **in-the-money**. Its intrinsic value = `max(K - S, 0) = max(24300 - 24000, 0) = ₹300`. By the mirror rule, the 24,300 *call* is **OTM** (spot below strike, zero intrinsic value).

**6.** Far-OTM calls have **zero intrinsic value — their entire ₹15 premium is pure time value, i.e. hope**, and a delta near zero means the market assigns them a very low probability of finishing ITM. Most weeks Nifty does not travel far enough to push them above the strike, so they decay to ₹0 and the buyer loses the full premium. The trade looks "small risk" per ticket, but the *expected value* is negative: the rare large win does not, on average, cover the many total losses — which is exactly why an efficient market prices them so cheaply. Repeated weekly, the small losses compound into a large drawdown, a textbook driver of the SEBI finding that about 9 in 10 retail F&O traders lose money. The fix is not "never buy OTM," but to size such bets like the low-probability lottery tickets they are.
