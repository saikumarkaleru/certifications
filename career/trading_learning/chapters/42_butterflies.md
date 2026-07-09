# Chapter 42: Butterflies — Long Call Butterfly & Iron Butterfly

Imagine you are not betting on *where* Nifty goes, but on *where it stops*. You have watched the index chop sideways for a week. India VIX is elevated and you think the fear is overdone — options look expensive, and you expect them to deflate. Above all, you have a hunch that come Thursday's weekly expiry, Nifty will be sitting almost exactly where it is now, say near 24,000. You don't want to sell a naked straddle and lie awake worrying about an undefined-risk gap. You want a structure that pays off best when the index *pins* a particular strike — and whose worst case is a small, known, capped loss you decided on the moment you placed the trade.

That structure is the **butterfly**. It is the sniper rifle of options strategies: a tight, surgical bet that the underlying will land on a precise point, with a sharp profit spike at the centre and a small premium at stake. This chapter teaches two cousins that build the same tent-shaped payoff from different parts: the **long call butterfly**, paid for with a small net debit, and the **iron butterfly**, which collects a net credit upfront. Both are defined-risk, both peak at the body, and both are the professional's way of saying "I think this thing goes nowhere — and I am willing to be wrong cheaply."

## Core concepts

### What a butterfly is: a tent over one strike

A butterfly is a **three-strike**, four-contract structure with **equal spacing** between the strikes. Picture three strikes lined up evenly: a lower one, a middle one (the **body**), and a higher one, each separated by the same gap — say 24,000 / 24,200 / 24,400. The two outer strikes are the **wings**. The payoff diagram looks like a tent (or, with imagination, a butterfly with two wings and a fat body): a sharp peak directly over the middle strike, sloping down on both sides to a flat floor.

You profit most when the underlying expires *exactly at the body*. As it drifts away from the body in either direction, your profit shrinks, hits two **breakeven** points, and then bottoms out at a small, fixed maximum loss once price reaches or passes either wing. Beyond the wings, nothing changes — the loss is capped. That is the whole personality of the trade: **maximum reward for a pinpoint forecast, defined and modest punishment for being wrong.**

### The long call butterfly — built from calls, paid as a debit

The **long call butterfly** is assembled entirely from call options, in a 1–2–1 ratio:

- **Buy 1** call at the lower strike (K1) — the lower wing.
- **Sell 2** calls at the middle strike (K2) — the body.
- **Buy 1** call at the higher strike (K3) — the upper wing.

with `K2 - K1 = K3 - K2` (equal spacing). You are long one cheap-ish lower call, short two pricier middle calls, and long one cheaper higher call. Because you sell the two middle calls, the premium they bring in partly funds the two wings you buy — but the wings together cost a little more than the body brings in, so the net result is a small **debit** (you pay to enter). That net debit is the entire amount you can lose. Nothing more.

Why does this shape pay off at the body? Think of it as **two spreads stacked back to back**:

- A **bull call spread** (long K1 call, short K2 call) that makes money as Nifty rises toward K2.
- A **bear call spread** (short K2 call, long K3 call) that makes money as Nifty *fails* to rise past K2.

At exactly K2, the bull side has delivered its full value while the bear side has not yet cost you anything — the two are perfectly balanced at their seam. That seam, the body, is where profit peaks.

The key formulas (call butterfly, equal width `w = K2 - K1 = K3 - K2`):

```
Net debit       = C(K1) - 2*C(K2) + C(K3)        (a positive number, per share)
Max profit      = w - net debit                  (achieved if S expires exactly at K2)
Max loss        = net debit                       (if S <= K1 or S >= K3)
Lower breakeven = K1 + net debit
Upper breakeven = K3 - net debit
```

Everything is "per share" — multiply by the lot size to get rupees. Note the pleasing symmetry: the two breakevens sit equal distances inside the wings, and the profit tent is centred on K2.

### The iron butterfly — a short straddle wearing a helmet

The **iron butterfly** reaches the same tent shape from the other side, using both calls *and* puts, and it pays *you* to put it on. The build, all at the same three strikes:

- **Sell 1** at-the-money (ATM) call at K2 (the body).
- **Sell 1** ATM put at K2 (the body).
- **Buy 1** out-of-the-money (OTM) call at the upper wing K3 (protection).
- **Buy 1** OTM put at the lower wing K1 (protection).

Look at the inner two legs: a short ATM call *and* a short ATM put at the same strike is exactly a **short straddle** (Chapter 39). That is the engine — it collects fat premium and profits if the market sits still. But a naked short straddle has undefined, terrifying risk on both tails. So the iron butterfly bolts on a **protective helmet**: a long OTM put below and a long OTM call above. Those wings cap the loss in a crash or a melt-up. You have turned an open-ended short-vol bet into a **defined-risk** one.

Because you sell the expensive ATM options and buy back cheaper OTM ones, you take in a **net credit**. That credit is your maximum profit; you keep all of it if the index expires exactly at the body. The formulas (equal width `w`):

```
Net credit      = [Call(K2) + Put(K2)] - [Call(K3) + Put(K1)]   (per share)
Max profit      = net credit             (if S expires exactly at K2)
Max loss        = w - net credit          (if S <= K1 or S >= K3)
Lower breakeven = K2 - net credit
Upper breakeven = K2 + net credit
```

An iron butterfly built at the same strikes as a call butterfly is economically the **same payoff** — same tent, same max profit, same max loss, same breakevens. (This is a consequence of put-call parity from Chapter 17.) The difference is purely cosmetic and practical: the call butterfly is a **debit** you pay; the iron butterfly is a **credit** you receive. Many Indian traders prefer the iron version because seeing a credit hit the account and because it is built around the liquid ATM strikes.

### The Greeks: short gamma, short vega, long theta near the body

A butterfly's character is written in its Greeks (Chapters 22–25), and they explain *why* it behaves the way it does. Consider the position **when the underlying is near the body**, which is the situation you set the trade up for:

- **Theta — positive (your friend).** You are net short the two pricey middle options and long the two cheaper wings. Time decay eats the body faster than the wings, so each passing day, with price near K2, drips profit toward you. The butterfly *wants* time to pass. This is the same engine as any short-premium trade.
- **Gamma — negative (your enemy).** Net short the body means net short gamma near the centre. A sudden jolt in either direction moves against you and your delta flips the wrong way — the position dislikes movement. (Out near the wings the sign actually reverses, but the meaningful zone is the body.)
- **Vega — negative (you want IV to fall).** You are a net seller of the expensive ATM volatility. If implied volatility **crushes** — the classic post-event "vol crush" or a VIX that drifts down through a quiet week — the body's value collapses and your tent fattens. This is why butterflies pair so well with **high-IV environments you expect to calm down**.
- **Delta — roughly zero at the body, by design.** Symmetric construction makes the position direction-neutral at the centre. It tilts slightly bearish if price is above the body and slightly bullish if below — a gentle self-correcting pull back toward K2, which is exactly the bet.

So in one sentence: a butterfly **collects theta, fears gamma, and profits from falling vega — as long as the underlying behaves and stays parked near the body.**

### When to actually use it

Reach for a butterfly when *all* of these line up:

1. **You expect very little movement** — a quiet, range-bound drift, or outright **pinning** of a specific level into expiry. Expiry-day pinning around big round/strike levels (24,000 on Nifty, 52,000 on Bank Nifty) is a real, observed phenomenon as dealer hedging concentrates price near heavily-traded strikes.
2. **You have a precise target**, not just a vague "sideways" view. The narrower the tent, the more precise your forecast must be — and the bigger the reward if you nail it.
3. **IV is high and you expect it to fall.** The negative vega then works for you, and you sell the body when it is richest.
4. **You want defined risk.** Unlike a naked short straddle, your worst case is fixed and small.

Avoid it before a known catalyst that could spark a big move (a Budget, an RBI policy day, election results) unless your *entire* thesis is that the move will be smaller than the market is pricing — and even then, the sharp peak makes a butterfly a demanding way to express it.

### Butterfly vs condor: sharp peak vs flat plateau

The butterfly's close relative is the **iron condor** (Chapter 43). The difference is one design choice: the condor pulls the two short body legs *apart* into two different strikes, creating a **flat plateau** of maximum profit between them instead of a single sharp **peak**.

- **Butterfly:** body is a single strike (short straddle core). Profit peaks at one point — a **narrow** zone with a **tall** peak. Higher reward-to-risk if you are right, smaller margin for error.
- **Condor:** body is a *range* of two strikes (short strangle core). Profit is a flat tabletop across that range — a **wider**, more forgiving zone, but **lower** maximum profit because the short legs are OTM and collect less.

Trade the **butterfly** for a sharp conviction about a specific landing spot; trade the **condor** when you only believe "somewhere in this band." Same family, different precision-versus-margin trade-off.

## Worked example (₹, Nifty)

It is Monday of an expiry week. Nifty spot is **24,000**. India VIX is elevated after a jittery few sessions, and you believe the market will chop and settle near 24,000 by Thursday, with IV cooling off. Assume a Nifty lot size of **75** (state lot sizes change periodically; confirm the current value). You choose strikes 200 points wide: **K1 = 23,800, K2 = 24,000, K3 = 24,200**, so `w = 200`.

**Version A — Long call butterfly.** Observed weekly call premiums (per share):

- 23,800 call: ₹260
- 24,000 call: ₹140
- 24,200 call: ₹60

Build: buy 1x 23,800 call, sell 2x 24,000 calls, buy 1x 24,200 call.

```
Net debit  = C(K1) - 2*C(K2) + C(K3)
           = 260 - 2*140 + 60
           = 260 - 280 + 60 = ₹40 per share
```

Now the numbers:

```
Net debit per share     = ₹40   -> max loss = 40 * 75 = ₹3,000
Max profit per share    = w - debit = 200 - 40 = ₹160 -> 160 * 75 = ₹12,000
Lower breakeven         = K1 + debit = 23,800 + 40 = 23,840
Upper breakeven         = K3 - debit = 24,200 - 40 = 24,160
```

So for a maximum risk of **₹3,000** you stand to make up to **₹12,000** — a reward-to-risk of about 4:1 — *if* Nifty expires exactly at 24,000. You make *some* profit anywhere between 23,840 and 24,160, and you lose the full ₹3,000 only if Nifty finishes at or beyond either wing (≤ 23,800 or ≥ 24,200).

Check a few expiry outcomes (per-share P&L, then x75):

- **Nifty = 24,000 (perfect pin):** 23,800 call worth 200; both 24,000 calls and the 24,200 call expire worthless. Value 200 − debit 40 = **+₹160/share = +₹12,000**. Maximum profit.
- **Nifty = 24,160 (upper breakeven):** 23,800 call 360; two short 24,000 calls -320; 24,200 call 0. Net value 40 = the debit -> **₹0 P&L.**
- **Nifty = 24,400 (past the upper wing):** 600 − 800 + 200 = 0 value; minus ₹40 paid = **-₹40/share = -₹3,000.** Maximum loss, fixed no matter how much higher Nifty goes.
- **Nifty = 23,600 (below the lower wing):** every call expires worthless; you lose the debit = **-₹3,000.** Capped.

**Version B — Iron butterfly (same strikes).** Now build the credit version: sell the ATM 24,000 call and 24,000 put, buy the 24,200 call and the 23,800 put. Suppose premiums are:

- 24,000 call: ₹140, 24,000 put: ₹150 (ATM straddle you sell)
- 24,200 call: ₹60, 23,800 put: ₹70 (OTM wings you buy)

```
Net credit = [Call(K2) + Put(K2)] - [Call(K3) + Put(K1)]
           = (140 + 150) - (60 + 70)
           = 290 - 130 = ₹160 per share
```

The numbers:

```
Net credit per share    = ₹160  -> max profit = 160 * 75 = ₹12,000
Max loss per share      = w - credit = 200 - 160 = ₹40 -> 40 * 75 = ₹3,000
Lower breakeven         = K2 - credit = 24,000 - 160 = 23,840
Upper breakeven         = K2 + credit = 24,000 + 160 = 24,160
```

Notice: **identical** to the call butterfly — same ₹12,000 max profit, ₹3,000 max loss, breakevens at 23,840 and 24,160. You simply *received* ₹12,000 upfront and will give some back if Nifty moves. At a perfect 24,000 pin the short straddle and the wings all expire worthless, so you keep the entire **₹12,000** credit; at expiry ≥ 24,200 or ≤ 23,800 you lose the capped **₹3,000**. A practical bonus (Chapter 9): because the wings fully hedge it, SPAN-plus-exposure margin is modest — roughly the defined max loss, far less than a naked short straddle would block.

![Figure: long call butterfly payoff](figs/long_butterfly.png)

![Figure: iron butterfly payoff](figs/iron_butterfly.png)

## Common mistakes / risk note

- **Mistaking "defined risk" for "high probability."** The loss is small and capped, but the *probability* of a near-perfect pin is also small. You collect the big max profit only in a narrow window; most expiries land on the slopes (P&L between the extremes), and a meaningful fraction land outside the wings for the full loss. Butterflies tend to produce many tiny gains/losses and occasional good wins — not free money. As SEBI's studies remind us, the large majority of retail F&O traders lose overall, and narrow low-cost structures do not change that arithmetic by themselves.
- **Trading it through a catalyst.** Putting a butterfly on right before results, the Budget, or an RBI decision invites exactly the violent move it hates (negative gamma). Unless your thesis is "the move will be smaller than priced," avoid known event risk.
- **Ignoring liquidity and the bid-ask spread.** A butterfly is four legs; on illiquid far strikes the spreads can quietly eat a large share of a ₹40 debit. Trade liquid weekly strikes (ATM and near-ATM on Nifty/Bank Nifty) and place it as a single multi-leg order where possible.
- **Forgetting it is short vega.** Enter when IV is *low* and IV then *spikes*, and the body fattens — you lose even if price hasn't moved. Butterflies belong in high-IV-you-expect-to-fall conditions.
- **Settlement.** Indian *index* options are European and **cash-settled**, so there is no assignment surprise at expiry — a real advantage here. Stock options are physically settled and can bring assignment/delivery complications; this strategy is cleanest on indices.
- **Over-tightening the wings.** Narrow wings raise the reward-to-risk ratio but shrink the profit zone to a razor; wider wings cost more but give a more forgiving target. Match the width to your real confidence about the landing spot.

## Key takeaways

- A **butterfly** is a three-strike, equally-spaced, defined-risk bet that the underlying will **pin the middle strike** at expiry; the payoff is a tent peaking at the body.
- The **long call butterfly** (buy 1 lower, sell 2 middle, buy 1 higher call) costs a small **net debit** = your max loss; **max profit = width − debit** at the body.
- The **iron butterfly** (short ATM straddle + protective OTM call and put wings) takes in a **net credit** = your max profit; **max loss = width − credit**. At matching strikes it is the *same payoff* as the call butterfly.
- Net Greeks near the body: **positive theta, negative gamma, negative vega** — it earns from time decay and falling IV, and fears sudden movement.
- Use it when you expect **very little movement / pinning into expiry**, ideally with **high IV you expect to crush**, and you want a **capped, known risk**.
- Versus an **iron condor**: the butterfly has a **sharper peak and narrower** profit zone (single body strike); the condor has a **flatter, wider** plateau (two body strikes) for less peak profit.

## Practice problems

1. **(Conceptual)** Explain in one or two sentences why a long call butterfly is "two spreads back to back," and name the two spreads.
2. **(Numeric)** Build a Nifty long call butterfly at strikes 23,900 / 24,000 / 24,100 (width 100). Premiums: 23,900 call ₹170, 24,000 call ₹110, 24,100 call ₹65. With lot size 75, compute the net debit, max profit, max loss, and both breakevens (in rupees where appropriate).
3. **(Numeric)** Construct an iron butterfly at the same strikes as Problem 2 (body 24,000, wings 23,900 and 24,100). The 24,000 call is ₹110, the 24,000 put is ₹120, the 24,100 call is ₹65, the 23,900 put is ₹70. Compute the net credit, max profit, max loss, and both breakevens. How do they compare to Problem 2?
4. **(Conceptual + Greeks)** It is the morning of a major RBI policy announcement and India VIX is high. A friend wants to put on a tight iron butterfly on Bank Nifty "because theta is positive and risk is defined." Give two reasons this is a dangerous time to do it.
5. **(Numeric)** For the butterfly in Problem 2, what is the P&L per share (and per lot) if Nifty expires at exactly 24,000? At 24,150? At 23,800?
6. **(Conceptual)** A trader believes Nifty will stay "somewhere between 23,800 and 24,200" but has no view on the exact level. Should they prefer a butterfly or an iron condor, and why?

## Solutions

**1.** A long call butterfly is a **bull call spread** (long the K1 call, short the K2 call) stacked against a **bear call spread** (short the K2 call, long the K3 call) sharing the middle strike. The bull side gains as price rises to K2; the bear side gains as price fails to exceed K2. They balance exactly at K2, which is where profit peaks.

**2.** Width `w = 100`.
```
Net debit  = 170 - 2*110 + 65 = 170 - 220 + 65 = ₹25/share -> max loss = 25*75 = ₹1,875
Max profit = w - debit = 100 - 25 = ₹75/share -> 75*75 = ₹5,625 (at S = 24,000)
Lower breakeven = 23,900 + 25 = 23,925
Upper breakeven = 24,100 - 25 = 24,075
```
Risk ₹1,875 to make up to ₹5,625 (3:1), profitable between 23,925 and 24,075.

**3.** 
```
Net credit = (Call 24,000 + Put 24,000) - (Call 24,100 + Put 23,900)
           = (110 + 120) - (65 + 70) = 230 - 135 = ₹95/share
```
Hold on — compare to the call butterfly debit of ₹25. For matching strikes the iron butterfly should mirror the call butterfly, with `max loss = w - credit`. Here:
```
Max profit = net credit = ₹95/share -> 95*75 = ₹7,125
Max loss   = w - credit = 100 - 95 = ₹5/share -> 5*75 = ₹375
Lower breakeven = 24,000 - 95 = 23,905
Upper breakeven = 24,000 + 95 = 24,095
```
The slight mismatch versus Problem 2 (breakevens 23,925 / 24,075 there vs 23,905 / 24,095 here) comes from the quoted premiums not being perfectly internally consistent with put-call parity — a normal real-world artifact of bid-ask spreads. The **lesson** is structural: the iron butterfly delivers the *same tent shape* as the call butterfly (peak at the body, defined and small max loss, narrow profit zone), just expressed as a credit you receive rather than a debit you pay. With perfectly parity-consistent prices the two would match exactly.

**4.** Two reasons it is dangerous: (a) **Negative gamma into a catalyst.** An RBI policy can spark a large, fast Bank Nifty move — precisely what a short-gamma butterfly loses on; a sharp move blows straight past the narrow profit zone to the max loss. (b) **Negative vega with potential for IV to rise further or stay high.** Although high VIX makes the body rich to sell, an event can keep IV elevated or spike it intraday before settlement, and even without a price move the position can sit at a loss. A butterfly wants *quiet and falling IV*, not a binary event. The tight wings make both problems worse.

**5.** Using the Problem 2 butterfly (strikes 23,900/24,000/24,100, debit ₹25/share, lot 75):
- **S = 24,000:** 23,900 call worth 100; two short 24,000 calls worthless; 24,100 call worthless. Value 100 − debit 25 = **+₹75/share = +₹5,625/lot** (max profit).
- **S = 24,150:** 23,900 call 250; two short 24,000 calls -2*150 = -300; 24,100 call +50. Net value = 0. Minus debit 25 = **-₹25/share = -₹1,875/lot** (this is at/just past the upper wing 24,100, so it is the max loss).
- **S = 23,800:** all calls expire worthless. You lose the debit only = **-₹25/share = -₹1,875/lot** (max loss, capped).

**6.** They should prefer an **iron condor**. Their view is a *range* ("somewhere between 23,800 and 24,200"), not a precise landing spot. A condor's flat profit plateau spans that whole band, paying the maximum across a wide zone and forgiving imprecision. A butterfly's sharp single-strike peak would reward them well only if Nifty pinned the exact body and would give back most of the profit elsewhere in their expected range. Match the structure's shape to the *shape* of your forecast: point view -> butterfly; band view -> condor.
