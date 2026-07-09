# Chapter 59: Market Making — How the Other Side Thinks

Every time you buy a Nifty call, somebody sold it to you. Every time you sell a Bank Nifty put, somebody bought it from you. That somebody is almost never another retail trader sitting at home — it is a **market maker** or a **proprietary trading desk**, a professional firm whose entire business is to stand in the middle of the market and quote prices all day long. Understanding how that firm thinks is one of the most clarifying things a retail trader can do, because it tells you exactly who you are up against and where your money can realistically come from.

The popular picture is a conspiracy: "the operators" hunting your stop-loss, the big players engineering a crash to grab your premium. The reality is far more boring and far more useful. The professionals on the other side are mostly *not betting against your direction at all*. They run a high-volume, low-margin business of buying slightly below fair value and selling slightly above it, then immediately neutralising the risk they just took on. Once you see the market maker as a careful, hedged, risk-averse plumber rather than a directional predator, you will make better decisions about which strikes to trade, what orders to use, and where your edge must actually come from.

## Core concepts

### Who is on the other side, and what is their job

In the NSE F&O market, the bulk of two-sided quoting is done by a small number of well-capitalised players:

- **Market makers (MMs):** firms that have agreed (sometimes formally, often informally through sheer activity) to continuously post both a **bid** (the price at which they will buy) and an **ask/offer** (the price at which they will sell) on many strikes at once. They want to trade with *whoever shows up*, on either side.
- **Proprietary (prop) desks and arbitrage funds:** firms trading their own capital, running statistical and arbitrage strategies — put-call parity arbitrage, cash-futures arbitrage, volatility arbitrage, and high-frequency quoting.

Their job is **liquidity provision**: making sure that when you want to buy, a seller exists, and when you want to sell, a buyer exists, at a tight and continuous range of prices. In exchange for providing that service, they collect the **spread**.

### The spread is the fee for immediacy

The **bid-ask spread** is the gap between the best buy price and the best sell price on the order book.

```
Spread = ask price - bid price
Mid price = (ask + bid) / 2
```

Suppose a Nifty 24000 call shows a bid of 119.50 and an ask of 120.50. The "fair value" — the mid — is roughly 120. If you want to buy *right now*, you pay 120.50. If you want to sell *right now*, you receive 119.50. The market maker who sits on both sides buys at 119.50 and sells at 120.50, pocketing the **1-point spread** if it can do both before the price moves.

Think of the spread as the price of **immediacy**. You are paying a small toll to transact instantly instead of waiting and hoping someone meets your price. The market maker is the toll-keeper. On a single trade the toll looks trivial — a rupee on a 120-rupee option. But a market maker may do this tens of thousands of times a day across hundreds of strikes. Tiny edge times enormous volume is a real business.

Crucially, the market maker is **not hoping the option expires worthless** and is **not hoping Nifty goes up**. It is hoping to buy at the bid and sell at the ask, again and again, and walk home flat. Direction is, ideally, irrelevant to it.

### Why they must hedge: the Greeks they did not want

Here is the problem. The market maker cannot always buy and sell the *same* option at the same instant. Often it sells you a call and is left **holding a short call** for minutes, hours, or days before an offsetting buyer appears. During that time it carries real risk — the Greeks we studied in earlier chapters:

- **Delta:** a short call has negative delta; if Nifty rises, the position loses money.
- **Gamma:** that delta itself changes as Nifty moves, fastest near the strike.
- **Vega:** if implied volatility rises, the short option gains value against the seller.
- **Theta:** time decay, which for a short option works in the seller's favour.

A market maker who simply accumulated these exposures would be running a giant, unintended directional bet — exactly what it does *not* want. So the instant it takes on a position, it **hedges the Greeks it did not want to keep**.

### Delta-hedging with futures

The first and most important risk to kill is **delta** — exposure to the direction of the underlying. The cleanest tool in India is the **index future** (or, for some desks, a basket of stocks or another option).

If the market maker sells a Nifty call with delta 0.50 on a lot of 75, it has effectively taken on a short exposure of:

```
Position delta (in index units) = option delta * lot size * number of lots
```

It then trades the **opposite** amount of the underlying future to bring the *net* delta back to roughly zero. This is **delta-hedging**. After hedging, a small move in Nifty barely changes the market maker's total P&L: what it loses on the option, it gains on the future, and vice versa. It has converted a directional bet into a *position that earns the spread and is largely indifferent to direction*.

But delta is not constant — that is **gamma**. As Nifty moves, the option's delta shifts, so the hedge that was perfect this morning is wrong by the afternoon. The market maker must **re-hedge** periodically, buying or selling more futures to stay neutral. This continuous adjustment is called **dynamic hedging**, and the cost of doing it (crossing spreads, paying brokerage, getting whipsawed in choppy markets) is one of the things the option's premium has to pay for. This is the deep reason a high-gamma option (near expiry, near the money) is "expensive" in time value: it is expensive *to hedge*.

### Managing net gamma and vega across the whole book

A real market maker is not holding one option. It is holding **thousands of contracts** — long some strikes, short others, across multiple expiries. It does not hedge each one individually. Instead it nets everything into a small set of **aggregate book Greeks**: total delta, total gamma, total vega, total theta for the entire portfolio.

- It keeps **net delta** near zero almost continuously, using futures.
- It watches **net gamma**: a large short-gamma book is dangerous in fast markets because the delta runs away from the hedge.
- It watches **net vega**: this is its exposure to India VIX. A desk that is net short vega across the book loses if implied volatility spikes, so it may buy back some options or buy cheaper wings to cap the risk.

The art of market making is keeping all of these aggregate Greeks inside risk limits while still quoting tight, attractive prices that win order flow. The firm makes money on the **spread and small mispricings**; it survives by never letting the residual Greeks blow up.

### Inventory management

Because the market maker cannot perfectly match buyers and sellers, it builds up **inventory** — a net long or net short position in particular options it did not choose to hold. Inventory is risk, and risk that must be financed with margin (SPAN plus exposure, just like yours, only far larger). So the market maker actively *manages* it.

The main lever is **skewing the quotes**. If the desk has accumulated too many short calls, it will quietly *raise* its bids on those calls (to encourage buyers to sell them back to it) and *raise* its asks (to discourage taking on even more). In effect it nudges its own prices to attract the flow that flattens its inventory. This is why, in a strong trending move, you sometimes see option prices behave a little "stickily" — desks are managing inventory, not predicting your stop-loss.

### Adverse selection: the risk of being picked off

There is one risk a market maker fears more than direction: **adverse selection**, also called the risk of being **picked off** by an **informed trader**.

The market maker quotes prices to *everyone* equally. Most of the people who hit its quotes are "noise" traders — retail hedgers, small speculators, and arbitrageurs whose orders are roughly random and harmless. But occasionally the counterparty *knows something*: a fund acting on an information edge, or simply a fast algo that spotted that the market maker's quote is stale a half-second after a news print. When that informed trader trades against the market maker, the market maker reliably loses, because the price is about to move against the side it just took.

This is the market maker's central dilemma:

- **Quote too tight** (small spread) → win lots of friendly retail flow but get badly hurt by the occasional informed trader.
- **Quote too wide** (big spread) → safe from being picked off but lose flow to competitors with tighter quotes.

The spread you pay is, in part, **compensation for adverse selection** — a charge the market maker levies on *everyone* to cover the losses it takes from the few who are better informed. In illiquid, far-OTM, or weekly-expiry-afternoon situations, the chance of facing an informed/fast counterparty is higher and the quotes get wider to compensate. That is exactly why deep-OTM and illiquid strikes have ugly spreads: the market maker is protecting itself, not gouging you specifically.

### Why this whole picture matters to a retail trader

Step back and absorb three consequences, because they should change how you trade.

**1. You pay the spread every time you cross it.** When you place a *market order* or a marketable limit, you transact at the far side of the spread — you buy at the ask and sell at the bid. That difference is an immediate, guaranteed cost handed to the market maker, before the trade has any chance to work. On a liquid Nifty ATM option the spread might be 1-2 rupees; on an illiquid far strike it can be 10-20 rupees, which on a round trip can dwarf your expected profit. **Defence:** trade **liquid strikes** (near-the-money, near-dated index options, where competition forces spreads tight) and use **limit orders** to try to transact at or inside the mid rather than paying the full spread. Patience converts you from a spread-payer toward a spread-saver.

**2. Your edge cannot be something the pros are already arbitraging away.** The market makers and prop desks have faster data, cheaper capital, lower transaction costs, and continuous hedging. Any *pure pricing* edge — "this option is mispriced by the model" — has almost certainly already been captured by them before you see it. Put-call parity violations, calendar mispricings, obvious IV dislocations: gone in milliseconds. So your realistic edge is **not** out-pricing the market maker. It must come from somewhere they do not compete:
   - **Risk transfer / patience:** willingly holding a position (and its overnight risk) that hedgers want off their books, earning the risk premium for it.
   - **A view on direction or volatility regime** over days and weeks, a horizon market makers deliberately avoid because they hedge it away.
   - **Discipline and structure:** position sizing, defined-risk spreads, exits — behavioural edges, not pricing edges.

**3. You are usually trading against well-capitalised professionals, and that is fine.** The market maker is *not* your enemy and is *not* trying to predict where your stop sits. It is largely indifferent to your direction; it just wants the spread and a flat book. This is genuinely good news. It means the market is mostly **efficient and fair**, not rigged. Prices stay close to fair value precisely because armies of hedged professionals compete to quote them. You lose money not because someone is hunting you, but because you crossed too many spreads, took directional bets without an edge, or sized too big. Those are fixable.

### How prices stay efficient — without a conspiracy

Put the pieces together and you get a clean model of *why* the option chain looks orderly and fair at almost every moment:

1. Many market makers compete to quote each strike, which **drives spreads tight**.
2. Each one **delta-hedges and vega-manages** continuously, so none takes a big directional view that would distort prices.
3. Arbitrage desks **enforce relationships** — put-call parity, cash-futures, the volatility surface — by instantly trading away any gap.
4. The threat of **adverse selection** keeps everyone honest: stale quotes get picked off, so firms keep their prices current.

The result is an option chain whose prices reflect, second by second, the market's best collective estimate of fair value. There is no single puppeteer — just a crowd of competing, hedged, self-interested professionals whose competition *produces* efficiency as a by-product. That is a far more accurate, and far more empowering, picture than any conspiracy.

## Worked example (₹, Nifty)

Let us watch a market maker delta-hedge a Nifty call it just sold, exactly as a desk would.

**The setup.** Nifty spot is at 24,000. A retail trader places a market order to **buy 1 lot** (lot size 75) of the weekly **24,000 call**. The market maker's quote was bid 119.50 / ask 120.50, so the trader buys at the **ask of 120.50**. The market maker is now **short 1 lot of the 24000 call**.

At-the-money, assume this call has:
- delta = +0.50 (per the option; the *seller* is now short this delta)
- gamma = +0.004 per 1-point move (i.e. delta changes by 0.004 for each 1-point move in Nifty)

**Step 1 — Measure the unwanted delta.** By selling the call, the market maker is **short delta**:

```
Position delta = - (option delta) * lot size * lots
             = - (0.50) * 75 * 1
             = -37.5
```

This means: if Nifty rises by 1 point, the short-call position loses about 37.5 rupees; if Nifty falls 1 point, it gains about 37.5 rupees. The desk does not want this directional bet.

**Step 2 — Hedge with futures.** To neutralise -37.5 delta, the market maker must add **+37.5 delta** in the underlying. A Nifty future has a delta of +1 per unit and the future's lot is also 75 units, so one full future lot carries +75 delta. The desk needs only +37.5, so it **buys 37.5 units' worth** — i.e. half a futures lot's worth of delta. (In practice a desk nets this against its whole book and does not literally hold half a lot, but the arithmetic is the point.)

After hedging:

```
Net delta = -37.5 (short call) + 37.5 (long futures) = 0
```

The book is now **delta-neutral**. The market maker has locked in the spread edge (it sold at 120.50 versus a ~120 mid) and is, for the moment, indifferent to small moves in Nifty.

**Step 3 — Nifty moves; gamma bites.** Suppose Nifty rallies 50 points to 24,050. The call's delta does not stay at 0.50; gamma pushes it up:

```
New option delta ≈ 0.50 + gamma * move = 0.50 + 0.004 * 50 = 0.70
New position delta from the short call = -0.70 * 75 = -52.5
```

But the futures hedge is still only +37.5. So the **net delta has drifted**:

```
Net delta = -52.5 + 37.5 = -15
```

The desk is now net short 15 delta — exposed to a further rally. To restore neutrality it must **buy more futures**, adding +15 delta (another 15 units' worth). This is the **re-hedge**, and it had to *buy high* (Nifty already rose) to do it.

**Step 4 — See where the cost goes.** Notice the pattern: as Nifty rose, the desk was forced to buy futures *after* the move; if Nifty now falls back, it will be forced to sell *after* that move — buying high and selling low on its hedges. Every round of dynamic hedging in a choppy market **bleeds a little money**. That bleed is precisely what the option's **theta (time decay)** is meant to compensate the seller for, and it is baked into the premium the retail buyer paid. The market maker's profit, simplified:

```
MM profit ≈ spread captured (~1 pt * 75 ≈ ₹75)
          + theta earned on the short option
          - cost of dynamic delta-hedging (gamma cost)
          - brokerage, STT, exchange fees
```

If implied volatility *realised* by Nifty turns out lower than the IV at which the call was sold, the hedging cost stays small and the market maker keeps the spread and theta. If Nifty turns out to be wilder than implied, hedging costs balloon and the trade can lose — which is exactly why market makers obsess over the **net gamma and vega** of the whole book, not the direction of any single name.

The lesson for you: the rupee you paid by lifting the ask (120.50 instead of ~120) was the market maker's edge on entry, and it is gone the instant you trade. Cross enough spreads and you fund a professional's low-risk business out of your account.

## Common mistakes / risk note

- **Believing in the "operator hunting your stop" story.** Market makers are mostly delta-neutral and direction-indifferent; they want the spread, not your stop. Trading on a conspiracy theory leads to bad, emotional decisions. The honest danger is duller: spreads and slippage quietly draining your account.
- **Using market orders on illiquid strikes.** A market order on a wide-spread, far-OTM, or low-volume strike hands the market maker the entire spread and possibly severe slippage. Always check the bid-ask and prefer limit orders.
- **Assuming you can out-price the pros.** If a strike looks "obviously mispriced," assume the desks have already seen it and there is a reason (an event, a hard-to-hedge risk). Pure pricing arbitrage is not a retail edge.
- **Ignoring liquidity when choosing strikes.** Beautiful strategies on paper die on real spreads. Near-the-money, near-dated Nifty and Bank Nifty options are where competition makes spreads tight; venture far from them and the market maker's protective wide quote becomes *your* cost.
- **Forgetting that selling options puts you in the market maker's chair without the market maker's hedging.** When you sell a naked option, you take on the Greeks a desk would immediately hedge — but you usually don't hedge dynamically. You are running the risky half of the business without the risk machinery. Size accordingly, and remember the SEBI finding that the large majority of retail F&O traders lose money.

## Key takeaways

- The other side of your trade is a **market maker or prop desk** providing liquidity by quoting bid and ask and earning the **spread** — not, mostly, betting against your direction.
- They immediately **hedge the Greeks** they take on: delta-hedging with futures and managing **net gamma and vega** across thousands of contracts, so they earn edge while staying roughly direction-neutral.
- They manage **inventory** by skewing quotes and protect themselves from **adverse selection** (informed traders) by widening spreads where being picked off is likely.
- **You pay the spread every time you cross it.** Trade **liquid strikes** and use **limit orders** to reduce this cost.
- Your **edge cannot be pure mispricing** — that's already arbitraged away. It must come from patience, risk transfer, a longer-horizon view, or behavioural discipline.
- Prices stay efficient through **competition among hedged professionals**, not a conspiracy. The market is mostly fair; most retail losses come from spreads, edge-free bets, and oversizing.

## Practice problems

1. **Conceptual.** A market maker sells you a Nifty put and is now short the put. List the four first-order Greeks it has taken on and state, for each, which way the underlying or volatility must move to hurt the market maker.

2. **Numeric — spread cost.** A Bank Nifty 52,000 call is quoted bid 298 / ask 305. The lot size is 15. You buy one lot at the ask and, immediately changing your mind, sell it back at the bid. Ignoring brokerage and taxes, what is your round-trip loss in rupees, and who received it?

3. **Numeric — delta hedge.** A desk sells 4 lots of a Nifty call with delta 0.45 (lot size 75). How much index delta must it add via futures to become delta-neutral, and does it **buy** or **sell** futures?

4. **Numeric — gamma re-hedge.** Continuing from problem 3, Nifty falls and the call's delta drops to 0.30. What is the new net delta of the (still-futures-hedged-at-the-old-level) book, and what trade restores neutrality?

5. **Conceptual.** Explain why a deep out-of-the-money weekly option tends to have a much wider bid-ask spread than an at-the-money one, using the idea of adverse selection and hedging cost.

6. **Conceptual.** A friend says, "I lost money because the operators hunted my stop-loss." Give a more accurate, market-making-based explanation of where small, repeated retail losses usually come from, and one concrete habit that reduces them.

## Solutions

**1.** Selling a put leaves the market maker **long delta** (a put has negative delta; being short it gives positive delta), **short gamma**, **short vega**, and **long theta**.
   - Delta: it is now long delta, so a **fall** in Nifty hurts it (the short put gains value against it).
   - Gamma: short gamma, so a **large, fast move in either direction** hurts it, because its delta runs away from any hedge.
   - Vega: short vega, so a **rise in implied volatility** (India VIX spike) hurts it.
   - Theta: long theta, so the **passage of time helps** it — this is its compensation for the above risks. It will delta-hedge with futures to remove the directional part.

**2.** You buy at the ask (305) and sell at the bid (298), so you lose the spread on each unit:

```
Loss per unit = 305 - 298 = 7
Loss = 7 * 15 = ₹105
```

The **₹105 round-trip loss** is captured (as spread) by the market maker(s) who took the other side of both your trades. This is why crossing the spread twice with no price move is a guaranteed loss equal to the spread times lot size.

**3.** Selling 4 lots of a 0.45-delta call makes the desk **short delta**:

```
Position delta = - 0.45 * 75 * 4 = -135
```

To reach zero it must add **+135 delta**, so it **buys** futures worth 135 index units (which is 135 / 75 = 1.8 Nifty future lots' worth of delta). Buying futures offsets the short-call exposure.

**4.** With the option delta now 0.30, the short-call position delta is:

```
New position delta from calls = - 0.30 * 75 * 4 = -90
```

The futures hedge is still +135 (unchanged). So:

```
Net delta = -90 + 135 = +45
```

The book is now **net long 45 delta** — it over-hedged once the option's delta shrank. To restore neutrality the desk must **sell** futures worth 45 delta (0.6 of a lot). Note the pattern: Nifty fell, and to re-hedge the desk **sells after the fall** — selling low — which is the gamma cost of dynamic hedging that theta must pay for.

**5.** A deep-OTM weekly option attracts few natural buyers and sellers, so **competition among market makers is thin** and there is little flow to offset inventory. Two forces widen the quote: (a) **hedging is harder and noisier** — the option's delta and gamma can jump sharply on small spot moves near expiry, making the desk's dynamic hedge costly and uncertain; and (b) **adverse selection is relatively higher** — much of the flow in such strikes is opportunistic or informed (lottery buyers, fast algos), and stale quotes get picked off, so the desk demands a larger spread as compensation. An ATM option has deep, competitive flow and a stable, cheap-to-hedge delta near 0.50, so spreads compress.

**6.** A more accurate explanation: the market makers on the other side are mostly **delta-neutral** and indifferent to where any individual's stop sits — they are not hunting you. Repeated small retail losses usually come from **paying the bid-ask spread again and again** (especially via market orders on illiquid strikes), **slippage**, taxes/brokerage, and taking **directional or premium-selling bets with no real edge**, often oversized. Each crossing of the spread is a small, certain transfer to the liquidity provider; do it dozens of times a month and it compounds into a meaningful drag, with no conspiracy required. One concrete habit that helps: **trade only liquid, near-the-money index strikes and use limit orders** placed at or inside the mid, so you stop paying the full spread on every entry and exit.
