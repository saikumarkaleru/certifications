# Chapter 15: Buyer vs Seller — Time Decay, Probabilities & the Honest Reality

Picture two people standing on opposite sides of the same counter. On one side is a man buying a lottery ticket: he pays a small, fixed amount, he knows exactly how much he can lose (the ticket price), and he dreams of a payday many times his stake. On the other side is the shop that sold him the ticket: it collects a steady stream of small payments from thousands of buyers, wins almost every single transaction, and lives in quiet dread of the one ticket that hits the jackpot. The option *buyer* is the lottery customer. The option *seller* is the lottery shop. Almost everything that confuses beginners about options dissolves the moment you internalise that these two are not two strategies — they are two completely different businesses with opposite shapes of risk, opposite relationships with time, and opposite emotional textures.

This chapter is the honest, foundational one. Everything you've learned about calls and puts so far has shown you the mechanics of each position. Now we step back and ask the questions that decide whether you survive: Who has the edge, the buyer or the seller? Where does time go? Why do most retail traders in India lose money — and what, precisely, separates the small minority who don't? No diagrams here, just the truth told plainly with simple numbers. If you absorb only one chapter of this book, absorb this one.

## Core concepts

### Two businesses, not two trades

When you buy an option you pay a premium today for the *right* to a payoff later. When you sell an option you receive that premium today and take on the *obligation* to deliver that payoff if asked. The money simply changes hands: every rupee the buyer pays, the seller pockets, and vice versa at expiry. Options are, at their core, a **transfer of risk for a fee**. The buyer hands over a small, certain amount of money to escape (or to bet against) an uncertain future. The seller accepts that uncertain future in exchange for the small, certain fee. This is exactly what an insurance company does, and the analogy is not loose — it is the literal structure.

From this single transfer, two opposite profiles are born:

- **The buyer has defined risk and (often) undefined reward.** The most a long-option buyer can lose is the premium paid. A long Nifty call bought for ₹150 can lose at most ₹150 per unit, full stop — no margin call, no surprise. But its upside, if the market runs, can be many multiples of that. Limited, known downside; large, open upside.
- **The seller has defined reward and (often) undefined risk.** The most a naked seller can make is the premium collected — that's the entire prize. But the loss, if the market moves hard against them, can be far larger than the premium, sometimes catastrophically so (recall the short call's theoretically unlimited loss from Chapter 13). Limited, known upside; large, open downside.

Neither shape is "better." They are mirror images, and which one suits you depends on what you're trying to do and how you manage the dangerous side.

### Time: the engine that runs one way

The single most important difference between the two sides is their relationship with time, captured by the Greek letter **theta** (time decay). Every option contains **time value** — the portion of its price that exists purely because the future is still open and anything could happen (Chapter 6). As expiry approaches, that future shrinks, and time value bleeds away toward zero. This bleed is not optional and not symmetric in feel:

- For the **buyer**, theta is a headwind. Every day that passes with the market sitting still, a long option is worth slightly less, even if nothing went wrong. The buyer is renting hope, and the rent is charged daily. This is why a long option that's "right but too early" or "right but too slow" can still lose money.
- For the **seller**, theta is a tailwind. Every quiet day, the option they're short loses a little value, which is a profit to them because they'd buy it back cheaper. The seller is the landlord collecting that rent.

Crucially, time decay **accelerates** as expiry nears, especially for at-the-money options. An option might lose a small slice of its time value with a month to go, but in the final week — and brutally in the final day of a weekly expiry — the remaining time value collapses. This is why Indian weekly index options are a theta battlefield: sellers love the fast decay of the last two days; buyers of cheap weekly out-of-the-money options are fighting a clock that speeds up against them. Time, quite literally, is money, and it flows from the buyer's pocket to the seller's.

### Probabilities: who wins how often

Here is the part that traps beginners. The buyer and seller don't just have different *sizes* of win and loss — they have different *frequencies*, and the two are inversely linked.

Consider an out-of-the-money (OTM) Nifty call: the market is at 24,000 and you buy the 24,500 call. For this to pay off at all, the market must rise more than 500 points by expiry. Most weeks, it doesn't. So this option, like a lottery ticket, **usually expires worthless** — the buyer loses the whole premium, again and again, in small bites. But on the occasional week the market explodes upward, the same cheap option can multiply five- or ten-fold. The buyer's profile is therefore **low probability of winning, high payoff when they do**.

The seller of that same call sits on the exact opposite. They win the small premium **most of the time** — week after quiet week — and suffer a large loss on the rare violent move. The seller's profile is **high probability of winning, capped payoff, occasional big loss**.

This is the deep asymmetry, and it's worth saying out loud because it's so counter-intuitive: *the side that wins more often is not the safer side.* The seller "wins" maybe 70–80% of trades and still risks blowing up, because the rare losses dwarf the frequent wins. The buyer "loses" 70–80% of trades and can still come out ahead, for the same reason in reverse. Win-rate alone tells you almost nothing. To judge a strategy you must combine *how often* with *how much* — and that combination has a name.

### Expectancy: why there is no free lunch

**Expectancy**, also called **expected value (EV)**, is the average rupee outcome of a trade if you could repeat it thousands of times. It is the only honest scoreboard, and the formula is simple:

```
Expectancy = (probability of win * average win) - (probability of loss * average loss)
```

Apply it to both sides of one trade and a beautiful, sobering fact appears. Suppose an option has a "fair" price — meaning the market has correctly priced the odds. Then:

- The **buyer's** rare big wins, weighted by their small probability, exactly equal the frequent small losses. Expectancy before costs ≈ 0.
- The **seller's** frequent small wins, weighted by their high probability, exactly equal the rare big losses. Expectancy before costs ≈ 0.

In a fairly priced market, **both sides have an expectancy of roughly zero before costs.** The premium is, in theory, the price at which the buyer's dream and the seller's dread are balanced. This is the heart of "no free lunch": selling options is not "easy money because they usually expire worthless," and buying options is not "smart money because the upside is huge." If it were that simple, everyone would pile onto one side and the premium would move until the edge vanished. The high win-rate of selling is *paid for* by the size of the rare loss. The low win-rate of buying is *compensated by* the size of the rare win. The market sets the premium precisely so neither lunch is free.

Two real-world wrinkles tilt this slightly. First, **implied volatility is usually a bit higher than the volatility that actually shows up** (the volatility risk premium), which gives the seller a small structural edge — buyers, on average, slightly overpay for protection and for lottery tickets. Second, and far more powerful in the other direction, are **costs**. And costs are where the theory meets the brutal Indian reality.

### Costs: the house always takes a cut

In a casino, the wheel has a green zero, so even a "fair" bet loses slightly over time — that green zero is the house edge. In Indian F&O, the green zeroes are everywhere:

- **Brokerage** on every order, entry and exit.
- **STT (Securities Transaction Tax)** — charged on options, and notably on the *settlement value* of in-the-money options that are exercised, which can be a nasty surprise for buyers who let an ITM option expire instead of squaring off.
- **Exchange transaction charges, SEBI turnover fees, stamp duty, and GST** on top of the brokerage and charges.
- **The bid-ask spread** — the invisible cost of crossing from the buy price to the sell price, which widens on illiquid strikes and far weeklies.

Stack these up and the picture is grim: a zero-expectancy bet becomes a *negative*-expectancy bet for both buyer and seller once the house takes its cut. The more you trade, the more cuts you pay. This single fact — costs turning a fair game into a losing one for the average participant — is the quiet engine behind the most important number in Indian retail trading.

### The SEBI reality: why most retail traders lose

SEBI (the Securities and Exchange Board of India), the market regulator, has studied who actually makes money in equity F&O. The findings, repeated across studies, are blunt and consistent: **the large majority of individual F&O traders lose money** — on the order of nine in ten in net terms — and the aggregate losses run into very large sums, with the average loser down a meaningful amount over a year, *before* even counting transaction costs (which themselves consume a big slice of the rare winners' gains). A small minority is consistently profitable. This is not a rumour or a scare tactic; it is the regulator's own data, and it is the single most important fact a new Indian options trader can know.

Why do so many lose? Not because options are a scam — because of *how* people trade them. The recurring causes:

1. **Overtrading.** Each trade pays the house its cut. A trader taking many trades a day is feeding the green zeroes relentlessly. Even a near-coin-flip strategy bleeds to death on costs at high frequency. Activity feels like work; here it is mostly leakage.
2. **Buying cheap, far OTM weekly options.** This is the most seductive trap. A ₹5 or ₹10 weekly option *feels* like a tiny, harmless bet with lottery upside. But far-OTM options have a very low probability of paying off and decay viciously. Buying them repeatedly is buying lottery tickets that, on average, expire worthless — the textbook negative-expectancy habit, dressed up as "high risk-reward."
3. **No edge.** Most traders have no genuine reason to believe their direction, timing, or volatility view is better than the price already reflects. Without an edge, expectancy starts at zero and costs drag it negative. Trading harder doesn't create an edge; it just pays more costs.
4. **Leverage and oversizing.** F&O is leveraged. One oversized position in a violent move (a gap on Bank Nifty, an event surprise) can erase months of small gains — the "occasional big loss" of the seller, or a margin wipeout for an over-leveraged buyer.
5. **Behaviour.** Cutting winners early and letting losers run, revenge-trading after a loss, chasing tips, and confusing a few lucky wins with skill. The emotional texture of buying (frequent small pain, rare euphoria) and selling (frequent small comfort, rare terror) is engineered to make humans behave exactly wrong.

### What separates the profitable minority

If nine in ten lose, the obvious question is what the tenth does differently. It is not a secret indicator. The profitable minority share a small, unglamorous set of habits:

- **Selectivity over activity.** They trade rarely, only when they believe they have a genuine edge, and they accept doing nothing most of the time. Fewer trades means fewer cuts to the house.
- **Risk management as the first priority, not the last.** They size positions so that the inevitable bad trade is survivable — never risking ruin on one position. Sellers especially define and cap their tail risk (with spreads, hedges, or strict stops) rather than selling naked and praying.
- **Positive expectancy, then repetition.** They focus on the EV equation, not the win-rate. A buyer happy to lose small 70% of the time because the 30% pays enough; a seller respecting that the rare loss must never exceed many wins' worth of premium.
- **Cost awareness.** They treat brokerage, STT and slippage as real opponents and structure trades to minimise turnover.
- **Process and records.** They follow a written plan, journal trades, and let probability play out over many trades rather than judging themselves by the last one.

The uncomfortable summary: success in options is far less about predicting the market and far more about respecting the asymmetry, the costs, and your own psychology. Neither side — buyer nor seller — offers a free lunch. The professional simply manages the meal better.

## Worked example (₹, Nifty)

Let's make expectancy concrete with simple, round numbers on a Nifty weekly option. Nifty is at 24,000. Lot size is about 75 units.

A trader is tempted by a cheap **24,400 weekly call** trading at **₹40**. Suppose, realistically, the option finishes worthless 80% of the time (the market fails to rise past breakeven), and in the 20% of weeks it does pay, the average payoff to the buyer is **₹200** per unit.

**The buyer's expectancy, per unit, before costs:**

```
Expectancy(buyer) = (0.20 * (200 - 40)) - (0.80 * 40)
                  = (0.20 * 160) - (0.80 * 40)
                  = 32 - 32
                  = 0
```

A perfectly fair game — zero edge before costs. Now bring in the house. Say round-trip costs (brokerage + STT + charges + half-spread) amount to about **₹5 per unit** per trade. The buyer's expectancy becomes roughly `0 - 5 = -5` per unit, or about **-₹375 per lot** (5 * 75) on average, every time they take this trade. Repeat it 100 times in a year and the expected drag is around **₹37,500** purely from costs on a zero-edge bet — a clean illustration of how overtrading a fair game produces a steady loss.

Now the **seller** of that same call. Their per-unit expectancy before costs is the exact opposite of the buyer's, so it's also **0**:

```
Expectancy(seller) = (0.80 * 40) - (0.20 * 160)
                   = 32 - 32
                   = 0
```

The seller wins ₹40 in 80% of weeks (high win-rate, comforting), and loses ₹160 in 20% of weeks (rare, larger). After the same ~₹5 round-trip cost, the seller's expectancy is also slightly negative — *but* the small volatility-risk-premium edge (buyers tend to overpay, so maybe the true worthless-probability is 82%, not 80%) can nudge the seller back toward break-even or slightly positive. That tiny structural tilt, harvested patiently with disciplined risk control, is roughly the entire honest case for option selling. It is a thin edge, not a fountain — and one oversized loss in the 20% bucket erases many weeks of premium. The numbers force the lesson: nobody here is getting rich for free; the seller has a sliver of an edge they must protect with risk management, and the buyer must be genuinely *right* often enough to overcome both decay and costs.

## Common mistakes / risk note

- **Judging a strategy by its win-rate.** "This sells options and wins 85% of the time!" tells you nothing without the size of the 15% losses. High win-rate is the seller's seductive trap; it hides the tail.
- **Believing selling is "safe income."** Premium received is not profit earned until expiry passes safely. Naked selling carries large, sometimes ruinous, tail risk — the rare gap can dwarf months of collected premium.
- **Believing buying is "smart" because risk is limited.** Limited risk you pay over and over is still a steady loss. The buyer's defined risk is real comfort, but theta and costs grind a flat market into a losing one.
- **Ignoring costs.** In India, STT, brokerage, charges, and spreads turn a fair game negative. Overtrading is the most reliable way to lose: you pay the house edge hundreds of times.
- **Mistaking the rare win for skill.** A few jackpot weeks from cheap OTM buying feel like genius. Across many trades, expectancy — not the last lucky ticket — is your true result.
- **Oversizing.** Leverage means one bad trade can end the account. The honest risk: the math can be fair and you can *still* be wiped out by sizing too big for the rare adverse move.

## Key takeaways

- Buying and selling options are mirror-image *businesses*: the buyer has defined risk and large open upside (low win-rate, lottery-like); the seller has defined upside and large open downside (high win-rate, occasional big loss).
- Time decay (theta) flows from buyer to seller every day, accelerating into expiry — a headwind for buyers, a tailwind for sellers.
- Win-rate and payoff size are inversely linked; only **expectancy** (`prob_win * avg_win - prob_loss * avg_loss`) tells the truth about a strategy.
- In a fairly priced market, both sides have ~zero expectancy before costs — there is no free lunch. A small volatility-risk-premium gives sellers a thin structural edge.
- Costs in India (brokerage, STT, exchange/SEBI charges, GST, spreads) turn a fair game into a negative-expectancy one — and overtrading multiplies the damage.
- SEBI data shows the large majority of retail F&O traders lose money, mainly from overtrading, buying cheap OTM lottery options, costs, and trading without a genuine edge.
- The profitable minority win through selectivity, risk management, cost discipline, and process — not prediction.

## Practice problems

1. **(Conceptual)** A friend says, "Option selling is great — I win 9 out of 10 trades." Explain in one or two sentences why this statement, by itself, does not prove the strategy is profitable.

2. **(Conceptual)** Two traders take opposite sides of the same Nifty option at a fair price. Trader A buys, Trader B sells. Before costs, what is each trader's expectancy, and who is favoured once realistic Indian transaction costs are included? Why?

3. **(Numeric)** A Bank Nifty weekly 52,500 call costs ₹60. You estimate it expires worthless 75% of the time, and in the other 25% of cases the average payoff (gross) is ₹240 per unit. Ignoring costs, compute the buyer's expectancy per unit. Is this a fair, favourable, or unfavourable bet for the buyer?

4. **(Numeric)** Using the same option as Problem 3, compute the seller's expectancy per unit before costs. Then, if round-trip costs are ₹6 per unit, state each side's expectancy after costs.

5. **(Conceptual / India)** List three specific reasons, drawn from SEBI's findings, that explain why most retail F&O traders in India lose money. For each, name one habit that directly counters it.

6. **(Numeric / reasoning)** A buyer takes a zero-expectancy trade 150 times in a year. Round-trip costs are ₹4 per unit and the lot size is 50 units. Estimate the expected annual loss from costs alone, and explain what this says about overtrading.

## Solutions

**1.** Win-rate alone ignores the *size* of wins versus losses. Selling options typically wins small and often but loses big and rarely; winning 9 of 10 trades can still be unprofitable if the single loss is larger than the nine wins combined. Profitability depends on expectancy (frequency *and* magnitude together), not win-rate alone.

**2.** At a fair price, expectancy before costs is approximately **zero for both** the buyer (Trader A) and the seller (Trader B) — their outcomes are exact mirror images that sum to zero. Once realistic Indian costs (brokerage, STT, exchange/SEBI charges, GST, bid-ask spread) are added, both sides are pushed into *negative* expectancy. The seller is marginally favoured only because of the small volatility risk premium (implied volatility tends to exceed realised, so options are, on average, slightly overpriced — which benefits the side that collects premium). The house, via costs, is the real winner.

**3.** Buyer's expectancy per unit:

```
Expectancy = (0.25 * (240 - 60)) - (0.75 * 60)
           = (0.25 * 180) - (0.75 * 60)
           = 45 - 45
           = 0
```

Expectancy is ₹0 per unit — a **fair** bet before costs (neither favourable nor unfavourable). After costs it would become unfavourable.

**4.** The seller's outcome is the buyer's mirror image:

```
Expectancy(seller) = (0.75 * 60) - (0.25 * 180)
                   = 45 - 45
                   = 0
```

Also ₹0 per unit before costs. After ₹6 round-trip costs, **each side's expectancy becomes about -₹6 per unit** (0 - 6). Both are now losing trades on average; the cost is what makes the game negative-sum for the participants.

**5.** Any three of the following (reasons → countering habit):
- **Overtrading** (paying the house's cut hundreds of times) → trade selectively, only with a genuine edge; do nothing most days.
- **Buying cheap, far-OTM weekly options** (low probability of payoff, vicious decay) → avoid lottery-ticket buys; demand positive expectancy, not just high reward-to-risk.
- **No genuine edge** (direction/timing/volatility no better than the price implies) → define and test an edge before risking capital; otherwise stay out.
- **Leverage / oversizing** (one big move wipes out months of gains) → strict position sizing so no single trade can cause ruin.
- **Poor behaviour** (revenge trading, cutting winners, chasing tips) → follow a written plan, journal every trade, judge over many trades not the last one.

**6.** Expected annual loss from costs alone:

```
Cost per trade per unit  = 4
Units per lot            = 50
Cost per trade per lot   = 4 * 50 = 200
Trades per year          = 150
Annual cost              = 200 * 150 = 30,000
```

The expected annual loss is about **₹30,000** purely from costs, on top of a strategy that was break-even before costs. The lesson: even with zero directional edge and "fair" bets, frequent trading guarantees a steady, compounding loss because the house's cut is paid on every single round trip. Reducing the number of trades is one of the most direct levers an ordinary trader has to improve results — activity is not the same as edge, and in Indian F&O it is usually the enemy.
