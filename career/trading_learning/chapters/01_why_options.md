# Chapter 1: Why Options Exist — Derivatives, Hedging, Speculation & Income

Before you ever look at a single option chain on the NSE, you need to understand *why* this strange instrument exists at all. An option is not a magic money machine and it is not a lottery ticket, even though it can behave like both in the wrong hands. At its core, an option is a tool — invented centuries ago by farmers and merchants — to solve a very human problem: **the future is uncertain, and people want to control how that uncertainty affects them.** Some want protection from it. Some want to bet on it. Some want to get paid for absorbing it. Options let all three groups trade with each other.

This chapter builds the intuition first. By the end you will know what a derivative actually is, the three honest reasons anyone uses options, how options differ from futures and from simply buying the stock, and why Futures & Options (F&O) trading has exploded among Indian retail traders — for better and, very often, for worse.

## Core concepts

### What is a derivative?

A **derivative** is a financial contract whose value is *derived* from something else — called the **underlying**. The underlying can be a stock (Reliance), an index (Nifty 50, Bank Nifty), a commodity (gold, crude oil), or even a currency pair. The derivative itself has no independent existence; it is a side-contract that references the price of the underlying.

A plain analogy: imagine a cricket match. The match is the "underlying" — the real event. Now imagine a side-bet between two friends on whether India scores more than 300 runs. That side-bet is a *derivative*. Its value depends entirely on what happens in the actual match, but the bet is a separate agreement that the two friends can make, settle, or even sell to a third person before the match ends. The friends are not playing cricket; they are trading exposure to the cricket result.

Another everyday example: a movie ticket booked in advance. You pay today to *lock in the right* to watch a specific show next Friday. The ticket's worth to you derives from the value of that future show. If the movie turns out to be a blockbuster and shows sell out, your advance ticket is suddenly very valuable. If the movie flops, your ticket is worth only its face value or less. The ticket is a tiny derivative on the movie.

In Indian markets, the two derivative types you will live and breathe are:

- **Futures** — a contract to buy or sell the underlying at a fixed price on a future date. *Obligation on both sides.*
- **Options** — a contract that gives one party the *right* (but not the obligation) to buy or sell the underlying at a fixed price. *Right for the buyer, obligation for the seller.*

We will return to that right-versus-obligation distinction shortly, because it is the single most important idea in the whole book.

### Two flavours of option: call and put

There are exactly two basic option types, and everything else is built from them.

- A **call option** gives its buyer the right to *buy* the underlying at a fixed price, called the **strike price** (K), on or before a set **expiry date**.
- A **put option** gives its buyer the right to *sell* the underlying at the strike price on or before expiry.

The buyer pays a fee for this right, called the **premium**. Think of the premium as the price of the right itself — non-refundable, just like the cost of an insurance policy whether or not you ever claim on it.

> Note on Indian mechanics: **Index options** (on Nifty, Bank Nifty) are **European-style** — they can only be exercised *at expiry*, not before — and they are **cash-settled** (no shares change hands; you receive or pay the rupee difference). **Stock options** are American-style and **physically settled** (actual shares are delivered). Most of this book lives in the index-options world, so when we say "exercise," picture a cash settlement at expiry.

### Right vs obligation — the heart of options

This is the idea that separates options from every other instrument, so slow down here.

When you **buy** an option, you buy a *right*. You are never forced to do anything. If the trade goes against you, you simply let the option expire and walk away. Your maximum loss is the premium you paid — not a paisa more. Your potential gain, for a call, is theoretically unlimited as the underlying rises.

When you **sell** (or "write") an option, you take on an *obligation*. In exchange for receiving the premium upfront, you must honour the contract if the buyer chooses to exercise. The seller's profit is capped at the premium received, while the loss can be very large. The seller is, in effect, the insurance company: collecting small premiums regularly, but on the hook for big payouts when things go wrong.

A clean way to remember it:

```
Option buyer:  pays premium  -> gets a RIGHT      -> limited loss, large/unlimited gain
Option seller: gets premium  -> takes OBLIGATION  -> limited gain, large/unlimited loss
```

This asymmetry is why a beginner is usually steered toward *buying* options first (loss is capped and known) and why *selling* options, though it wins more often, demands respect, margin, and risk management.

### The three real uses of options

Stripped of all the hype, there are only three legitimate reasons to use options. Each corresponds to a different kind of person with a different goal.

#### 1. Hedging — options as insurance

**Hedging** means reducing the risk of an existing position. This is the original, oldest reason options exist. You already own something (or have exposure to something), and you want protection against an adverse move — exactly like buying insurance on a house you already own.

*Indian example.* Suppose a long-term investor holds a portfolio worth about ₹20 lakh that closely tracks the Nifty 50, currently at **24,000**. Union Budget season is approaching and she is worried about a sharp 5–10% fall over the next month, but she does not want to sell her holdings (taxes, long-term conviction). She **buys a Nifty 24,000 put option** — the right to "sell" the index at 24,000. If the market crashes to 22,000, her portfolio loses value, but her put gains value and offsets much of that loss. If the market instead rises, she loses only the premium she paid — the cost of her "insurance policy" — and keeps all her portfolio upside. This is the **protective put**, the textbook hedge.

#### 2. Speculation — options as leverage

**Speculation** means taking a position purely to profit from an expected price move, with no underlying exposure to protect. Options are attractive here because of **leverage**: a small premium controls a large notional value, so a modest move in the underlying can produce a large percentage move in the option.

*Indian example.* A trader is convinced Bank Nifty (at **52,000**) will jump after a strong banking-sector result this week. Buying the underlying basket is capital-intensive. Instead he buys one weekly **Bank Nifty 52,000 call** for a premium of, say, ₹400 per unit. With a lot size of around 15 units, his total outlay is roughly ₹6,000. If Bank Nifty rallies to 53,000 by expiry, the call's intrinsic value becomes about ₹1,000, so the position is worth ~₹15,000 — more than doubling his money on a roughly 2% move in the index. That is leverage working *for* him. But the same leverage works *against* him: if Bank Nifty stays flat or falls, the option can expire worthless and he loses the entire ₹6,000. Leverage is a magnifier in both directions.

#### 3. Income — options as premium selling

**Income** strategies aim to *collect* premium by selling options, betting that the option will expire worthless or lose value so the seller keeps the premium. This is the "be the insurance company" approach. It wins frequently — but each win is small and capped, while the occasional loss can be large.

*Indian example.* An investor owns a large position in Reliance shares that he is happy to hold. Each month he **sells a call option** slightly above the current price (a **covered call**). He collects the premium every month as income. If Reliance stays below the strike, the call expires worthless and he simply keeps the premium — a yield on shares he already owned. The trade-off: if Reliance rockets far above the strike, his upside is capped, because he is obligated to sell at the strike. He has traded away big upside in exchange for steady income.

These three uses — hedging, speculation, income — are not contradictory. The same option being *bought* by a hedger or speculator is being *sold* by an income seeker. The market works precisely because these different motives meet.

### Options vs futures vs buying the stock/index

To understand options, contrast them with the two simpler ways to take a market view.

**Buying the stock or index (cash/spot).** You pay the full price and own the asset outright. Your profit and loss move one-for-one (linear) with price. No expiry, no premium decay, no leverage (unless you borrow). Simple and unlimited holding period — but capital-heavy and your money is fully exposed to a fall.

**Futures.** A contract to buy/sell the underlying at a fixed price on a fixed future date. You post only **margin** (a fraction of contract value), so futures are leveraged. P&L is still **linear** — you gain or lose rupee-for-rupee with the index times the lot size. Crucially, futures carry **obligation on both sides**: if the market moves hard against you, your losses can exceed your initial margin and you face margin calls. There is no premium and no "right to walk away."

**Options.** Also leveraged and also expiry-dated, but **non-linear** and **asymmetric**. The buyer pays a premium for a right with capped loss; the seller collects premium and takes on obligation. Options let you shape your payoff — protect a downside, bet on a direction, or even profit from the market going *nowhere* — in ways neither the cash market nor futures can.

A compact comparison:

```
                  Cash/Spot         Futures              Options (buyer)
Capital needed    Full price        Margin (leveraged)   Premium (small)
Leverage          None (unleveraged) Yes                 Yes (high)
P&L shape         Linear            Linear               Non-linear, asymmetric
Obligation        You own it        Both sides obligated Buyer: right; Seller: obligation
Max loss          Price falls to 0  Can exceed margin    Buyer: premium only
Expiry            None              Yes                  Yes
Time decay        No                No                   Yes (works against buyer)
```

The phrase to burn into memory: **futures are linear and symmetric; options are non-linear and asymmetric.** That asymmetry is both the appeal and the danger.

## Worked example (₹, Nifty/Bank Nifty)

Let's make leverage and asymmetry concrete with a single underlying view, expressed three ways. Assume **Nifty is at 24,000**, the Nifty lot size is about **75 units**, and you are bullish for the week.

**View:** You expect Nifty to rise to 24,400 by weekly expiry (a +400 point, ~1.7% move).

**Option A — Buy Nifty futures.**
- Notional value = 24,000 * 75 = ₹18,00,000. You post SPAN+exposure margin of roughly ₹1,20,000 (about 6–7%).
- If Nifty rises to 24,400: profit = (24,400 - 24,000) * 75 = **+₹30,000**.
- If Nifty *falls* to 23,600 instead: loss = (23,600 - 24,000) * 75 = **-₹30,000**. Symmetric — and the loss keeps growing if it falls further.

**Option B — Buy a Nifty 24,000 call** (at-the-money), premium ₹150 per unit.
- Cost = 150 * 75 = **₹11,250**. That is your *entire* maximum risk.
- Payoff at expiry per unit: `max(S - K, 0) - premium`, where S is the settlement level and K = 24,000.
- If Nifty rises to 24,400: intrinsic = 24,400 - 24,000 = 400. Net per unit = 400 - 150 = 250. Profit = 250 * 75 = **+₹18,750** (a +167% return on ₹11,250).
- If Nifty falls to 23,600: the call expires worthless. Loss = the premium = **-₹11,250**, and not one rupee more. Asymmetric — the downside is capped no matter how far Nifty falls.

**Option C — Sell a Nifty 24,000 put** (income view, mildly bullish), premium ₹150 per unit.
- You receive 150 * 75 = **₹11,250** upfront, but must post margin (often ₹1,00,000+).
- If Nifty rises to or stays above 24,000: the put expires worthless and you **keep the full ₹11,250**. Your gain is capped at exactly this.
- If Nifty falls to 23,600: the put buyer exercises. Per unit you owe `max(K - S, 0) = 400`, net of the 150 premium = a 250 loss. Loss = 250 * 75 = **-₹18,750**, and it grows the further Nifty falls.

Notice the trade-offs. The futures buyer has symmetric, unlimited exposure both ways. The call buyer has a small, fully-known maximum loss but needs a real move to profit (he paid 150 of "time premium" that erodes daily — more on that **time decay** in later chapters). The put seller wins in the larger number of scenarios (flat *or* up), but his reward is capped while his loss is large. **Same bullish view, three completely different risk profiles.** Choosing among them *is* the craft of options trading.

## Common mistakes / risk note

**The honest truth comes first.** SEBI's own studies have repeatedly found that roughly **9 out of 10 individual traders in the equity F&O segment lose money**, with the average loser losing a significant sum, and that aggregate retail losses run into tens of thousands of crores of rupees per year. Options are a professional's tool. Going in without understanding the asymmetry is how most people become part of that 90%.

Specific beginner traps to avoid from day one:

- **Treating cheap out-of-the-money options like lottery tickets.** Buying far-OTM weekly options for ₹5–10 feels like a small bet, but the *vast majority expire worthless*. A long option is a *wasting asset* — every day that passes, time decay (theta) bleeds value out of it, even if the underlying doesn't move.
- **Thinking option selling is "free money."** Sellers win often, which breeds overconfidence. Then one gap-down on a budget day or a global shock wipes out months of premium in a single session, because the loss is large and undefined. Selling *naked* (uncovered) options without strict risk control is how accounts blow up.
- **Confusing "high probability of profit" with "low risk."** Selling a deep-OTM option might win 95% of the time, but the 5% loss can be 20x the premium collected. Win-rate is not the same as expected value.
- **Ignoring costs.** STT (Securities Transaction Tax), brokerage, exchange fees, and GST add up fast on frequent F&O trades and quietly turn marginal strategies into losing ones.
- **Mistaking leverage for skill.** A doubled account in a trending week is leverage, not edge. The same leverage halves it next week.

The defensive posture for a beginner: start by *buying* options (loss is capped and known), trade tiny size, and treat your first months as paid tuition rather than income.

## Key takeaways

- A **derivative** gets its value from an **underlying** (stock, index, commodity); an option is a derivative that conveys a *right*, not ownership.
- A **call** is the right to buy at the strike; a **put** is the right to sell at the strike. The buyer pays a **premium** for that right.
- The defining feature of options is **asymmetry**: buyers have limited loss (the premium) and large upside; sellers have limited gain (the premium) and large/undefined loss.
- Options serve **three honest purposes**: hedging (insurance on an existing position), speculation (leveraged directional bets), and income (selling premium).
- Versus **futures** (linear, symmetric, both sides obligated) and the **cash market** (linear, fully capitalised, no expiry), options are **non-linear and asymmetric**, letting you sculpt the payoff.
- Indian **index options are European and cash-settled**; **stock options are American and physically settled**.
- F&O has exploded in India because of low entry capital, weekly expiries, and easy app-based access — a **double-edged sword** that has helped roughly **90% of retail F&O traders lose money**. Respect the risk.

## Practice problems

1. **Conceptual.** In one sentence each, explain the difference between a *right* and an *obligation* in options, and state which one the option *buyer* holds and which the *seller* holds.

2. **Conceptual.** A friend says, "Buying a put option is just like betting the market will fall — it's the same as short-selling Nifty futures." Identify the key difference in the *risk profile* between buying a put and shorting Nifty futures.

3. **Numeric (leverage).** Nifty is at 24,000 with a lot size of 75. You buy one 24,000 call for a premium of ₹120 per unit. (a) What is your total cost and maximum loss? (b) If Nifty settles at 24,500 at expiry, what is your profit? (c) What percentage return is that on your cost?

4. **Numeric (income/selling).** You sell one Bank Nifty 52,000 put for a premium of ₹300 per unit; lot size is 15. (a) What is the premium you collect? (b) What is your maximum profit and in what scenario? (c) If Bank Nifty settles at 51,400, what is your net profit or loss?

5. **Classification.** For each scenario, state whether the trader is using options for **hedging**, **speculation**, or **income**: (a) an investor holding a Nifty ETF buys a Nifty put before election results; (b) a trader with no stock holdings buys weekly Bank Nifty calls expecting a rally; (c) a long-term Reliance holder sells monthly calls above the current price.

6. **Conceptual.** Explain why an at-the-money long option can *lose money even if the underlying ends exactly where it started* at expiry.

## Solutions

**1.** A *right* lets you choose whether to act but never forces you; an *obligation* forces you to honour the contract if the counterparty acts. The option **buyer holds the right** (and pays the premium); the option **seller holds the obligation** (and receives the premium).

**2.** When you **short Nifty futures**, your loss is *unlimited and symmetric* — if the market rises sharply against you, losses grow without bound and can exceed your margin. When you **buy a put**, your maximum loss is *capped at the premium paid* no matter how far the market rises, while you still profit if it falls. Both profit from a decline, but the put has a known, limited downside; the short future does not. (The put also costs premium and decays with time, which the future does not.)

**3.** (a) Cost = max loss = 120 * 75 = **₹9,000**. (b) Intrinsic at expiry = 24,500 - 24,000 = 500 per unit; net per unit = 500 - 120 = 380; profit = 380 * 75 = **₹28,500**. (c) Return = 28,500 / 9,000 = **316.7%**. (Note the leverage: a ~2.1% move in Nifty produced a >300% move in the option.)

**4.** (a) Premium collected = 300 * 15 = **₹4,500**. (b) Maximum profit = **₹4,500**, achieved when Bank Nifty settles **at or above 52,000**, so the put expires worthless and you keep the full premium. (c) At 51,400 the put is in-the-money by `max(52,000 - 51,400, 0) = 600` per unit. Net per unit = premium 300 - 600 = -300. P&L = -300 * 15 = **-₹4,500 loss**. (At a settlement of 51,700, you would break even, since 52,000 - 51,700 = 300 = the premium.)

**5.** (a) **Hedging** — protecting an existing ETF holding against a downside event. (b) **Speculation** — a leveraged directional bet with no underlying position to protect. (c) **Income** — a covered call, collecting premium on shares already owned.

**6.** A long option's premium is made of intrinsic value plus **time value**. An at-the-money option has *zero* intrinsic value — all of its premium is time value, which decays to nothing by expiry (this decay is called **theta**). If the underlying finishes exactly at the strike, the option has no intrinsic value to cash in, so the buyer recovers nothing and loses the entire premium paid. The market did not move, but *time* still ran out — and for an option buyer, the mere passage of time is a cost.
