# Chapter 4: Reading the NSE Option Chain

Imagine walking into a giant marketplace where, for a single underlying like Nifty, hundreds of different contracts are being bought and sold at once. Every contract is a bet on where Nifty will be on a future date, at a particular price. The **option chain** is simply the price board for that marketplace. It is one screen that lists every call and every put, at every available strike, for a given expiry, with their live prices and a few numbers that tell you how much interest the crowd has in each one.

For a professional, the option chain is not just a price list. It is a *map of where the market thinks the action is*. Learning to read it is like a doctor learning to read an X-ray: the same picture that looks like noise to a beginner reveals support, resistance, sentiment, and crowding to a trained eye. This chapter teaches you to read that X-ray, column by column, using a small illustrative chain around Nifty at 24000.

## Core concepts

### What the option chain is, and where to find it

An option chain (also called an *option matrix*) is a table that shows, for one underlying and one expiry, all the listed call options and put options across strike prices, together with their live market data.

You will mostly meet it in two places:

1. **The NSE website** (`nseindia.com`) under *Derivatives → Option Chain*. This is the official, exchange-sourced view. You pick the underlying (e.g., NIFTY), then the expiry date. It refreshes through the trading day. It is free, authoritative, and the data vendors ultimately trace back to it.
2. **Your broker's trading terminal** (Zerodha Kite, Upstox, Angel One, Dhan, Fyers, and so on). Brokers show the same data, usually with extra tools: one-click buy/sell, the ability to build multi-leg strategies, and sometimes the Greeks and implied volatility computed for you. This is where you actually trade.

The underlying for Nifty and Bank Nifty index options is the *index spot value* (the live index level). Remember from earlier chapters that **index options on NSE are European-style and cash-settled** — they can only be exercised at expiry, and settlement is in cash, not shares. Keep that in mind: the chain is a snapshot of a forward-looking, expiry-settled market.

### The layout: calls left, puts right, strikes down the middle

Almost every option chain in the world uses the same physical layout, and NSE is no exception:

- **Strike prices run down the centre column**, from low at the top to high at the bottom.
- **Call options sit on the left** of the strikes.
- **Put options sit on the right** of the strikes.

So one *row* is a single strike price. Reading across that row, the left side tells you everything about the call at that strike, and the right side tells you everything about the put at that strike. For example, the 24000 row shows you the 24000 call (left) and the 24000 put (right) at the same time.

A helpful mental picture: the strikes are a ladder. Climb up to higher strikes and calls get cheaper (a call to buy at a high price is worth less) while puts get more expensive (a put to sell at a high price is worth more). Climb down and the opposite happens. This *mirror symmetry* — calls and puts moving in opposite directions as you walk the strikes — is the first pattern your eye should learn to see.

### The columns, explained for a beginner

Each side (call and put) typically shows the same set of columns. Let us define every one of them. We will use the call side for examples; the put side is identical in meaning.

**LTP (Last Traded Price) — the premium.** This is the price at which the option last changed hands. The premium is what a buyer pays the seller for the contract, *per unit of the underlying*. Because Nifty options have a lot size (currently about 75 units per lot — lot sizes are revised by NSE from time to time, so always check), the rupee cost of one lot is `LTP * lot size`. If the 24000 call shows an LTP of 180, one lot costs `180 * 75 = ₹13,500`. The LTP is the headline number, but it is the *last* trade — it may be slightly stale. For what you can actually transact at *right now*, look at the bid and ask.

**Bid and Ask (and the spread).** The **bid** is the highest price a buyer is currently willing to pay. The **ask** (or *offer*) is the lowest price a seller is currently willing to accept. The gap between them is the **bid-ask spread**.

- If you want to *buy immediately*, you pay the ask.
- If you want to *sell immediately*, you receive the bid.
- The spread is a hidden cost. Buy at the ask and instantly sell at the bid, and you lose the spread.

A *tight* spread (say bid 178 / ask 180, a ₹2 gap) signals a liquid, heavily traded option — good. A *wide* spread (say bid 150 / ask 175) signals a thinly traded, illiquid option — you will get a poor fill and pay dearly to exit. **Rule of thumb for beginners: trade only options with tight spreads**, which in practice means near-the-money weekly Nifty and Bank Nifty options.

**Volume.** The number of contracts traded *today*. It resets to zero each session and builds through the day. High volume means the strike is active and easy to enter and exit. It is a flow measure — how much trading happened — not a position measure.

**Open Interest (OI).** This is one of the most important and most misunderstood columns, so go slowly. **Open Interest is the total number of option contracts that are currently open — created but not yet closed out or expired.** Unlike volume, OI does not reset daily; it carries over and changes as positions are opened and closed.

The key idea: every option contract has a buyer and a seller. OI counts the number of *live agreements*, not the number of trades.

- When a *new* buyer and a *new* seller create a fresh contract, OI rises by one.
- When an existing buyer and existing seller both close, OI falls by one.
- When a position simply changes hands (one trader exits, another enters the same side), volume rises but OI is unchanged.

So OI tells you how *crowded* a strike is — how much money is parked there. A strike with very high OI is a strike the market cares about. We will use this heavily below for support and resistance.

**Change in OI.** The increase or decrease in Open Interest compared to the previous day (or, on some terminals, since the start of the session). This is the *direction of the flow* and is often more informative than the OI level itself, because it tells you where positions are being *built right now*.

- **Rising OI + rising price** = new buyers are aggressive (fresh longs being added).
- **Rising OI + falling price** = new sellers are aggressive (fresh shorts being written).
- **Falling OI** = positions are being closed (unwinding), regardless of price direction.

A surge of OI being added at the 24500 call, for instance, often means writers (sellers) are betting Nifty will *not* cross 24500 — they are selling calls there to collect premium.

**Implied Volatility (IV).** IV is the market's forecast of how much the underlying will move, *implied* by the option's price. A later chapter covers it fully; for now, hold this intuition: a premium has two ingredients — what the option is already worth if exercised today (intrinsic value), and a payment for the *uncertainty* of what might happen before expiry (time value). IV is the dial controlling that uncertainty payment. **Higher IV means richer premiums; lower IV means cheaper premiums** — so high IV is good for sellers and costly for buyers, and low IV is the reverse. India's broad volatility gauge, the **India VIX**, is essentially the market-wide version of this number for Nifty.

### Finding the ATM strike

Three labels you must know cold:

- **ATM (At The Money):** the strike closest to the current spot price of the underlying.
- **ITM (In The Money):** an option that already has intrinsic value. For a *call*, that means strike *below* spot; for a *put*, strike *above* spot.
- **OTM (Out of The Money):** an option with no intrinsic value yet. For a *call*, strike *above* spot; for a *put*, strike *below* spot.

To find the ATM strike, look at the live spot value at the top of the chain and find the listed strike nearest to it. Nifty strikes are listed in steps of 50 points. If Nifty spot is 24000, the ATM strike is simply **24000**. If spot were 24023, the nearest strike is still 24000, so 24000 is ATM (the strikes 24050 and 23950 would be the first OTM call and first OTM put respectively).

Most option chains visually shade or highlight the ITM rows so the ATM line jumps out. A quick trick if no shading: the ATM strike is roughly the row where the call premium and the put premium are *closest to equal*, because at the money both sides carry mostly time value and little intrinsic value.

### How OI marks support and resistance

Here is where the chain stops being a price list and starts being a sentiment map. The logic rests on who is doing the selling.

Option *sellers* (writers) collect premium and profit when the option expires worthless. They are typically larger, better-capitalised players — and they place their bets where they believe price will *not* go. Because writing options has large risk, these writers effectively defend their strikes.

- **Heavy call OI above the spot acts as resistance.** Large call writing at, say, 24500 means a wall of sellers is betting Nifty stays below 24500. To push above it, the market has to overpower all those writers — so price often stalls there. The strike with the *largest* call OI is frequently the market's expected ceiling for that expiry.
- **Heavy put OI below the spot acts as support.** Large put writing at, say, 23500 means sellers are betting Nifty stays above 23500. That strike tends to act as a floor. The strike with the *largest* put OI is frequently the market's expected support.

So a fast read of the chain is: scan the call side above spot for the biggest OI (that is your resistance), and scan the put side below spot for the biggest OI (that is your support). The zone between them is the range the option market is implicitly pricing for the expiry. This is not a guarantee — walls break, especially on trending or news days — but it is a genuine, widely-watched edge.

### A first, gentle look at PCR and max pain

Two summary numbers are built from the OI column. We will treat them fully in a later chapter; here is just enough to recognise them.

**Put-Call Ratio (PCR).** This is total put OI divided by total call OI for the expiry:

`PCR = (total put open interest) / (total call open interest)`

It is a crude sentiment gauge. More puts open than calls (PCR above 1) is often read as *bullish* — paradoxically, because heavy put *writing* means sellers expect the market to hold up. PCR well below 1 (far more calls than puts) is often read as *bearish*. The twist that confuses beginners: PCR is frequently a *contrarian* indicator at extremes. Very high PCR can signal over-optimism (a top), very low PCR over-pessimism (a bottom). Treat it as a mood ring, not a crystal ball.

**Max pain.** This is the strike at which the *largest number of option buyers* would lose money — equivalently, where option *writers* collectively pay out the least at expiry. The theory (and it is only a theory, with mixed evidence) is that price tends to gravitate toward the max-pain strike as expiry nears, because the well-capitalised writing community has a collective incentive to keep it there. Brokers display a single "max pain" number per expiry. For now, just know what it claims to be: the strike where the most pain falls on buyers.

## Worked example (₹, Nifty)

Suppose it is a Tuesday, and the weekly Nifty expiry is on Thursday. Nifty spot is sitting at **24000**. Here is an illustrative (made-up but realistic) slice of the option chain. Lot size is 75.

```
              CALLS                    |  STRIKE  |              PUTS
   OI    Chg OI   Volume   IV    LTP   |          |   LTP    IV    Volume   Chg OI    OI
 ------------------------------------- | -------- | -------------------------------------
  9.1L   +0.4L    21,300   12.1  335   |  23800   |   95    13.0   30,500   +0.6L   12.4L
  7.8L   +0.6L    34,800   11.8  250   |  23900   |  130    12.6   41,200   +1.1L   10.2L
  6.2L   +0.5L    58,000   11.5  180   |  24000   |  180    12.3   60,100   +1.4L    7.5L
 11.5L   +2.1L    72,400   11.4  120   |  24100   |  225    12.1   33,400   -0.3L    5.1L
 18.9L   +4.7L    95,600   11.6   78   |  24200   |  285    12.0   22,800   -0.5L    3.4L
  9.4L   +1.2L    44,100   12.0   45   |  24300   |  355    12.2   12,600   -0.2L    2.0L
  7.1L   +0.9L    27,500   12.4   25   |  24400   |  430    12.6    7,900   -0.1L    1.3L
```

(L = lakh, i.e., 1L = 100,000 contracts of OI. IV in percent. LTP and strikes in rupees/index points.)

Let us read it as a professional would.

**Step 1 — Find ATM.** Spot is 24000, and 24000 is a listed strike, so the **ATM strike is 24000**. Notice the call LTP (180) and put LTP (180) are equal there — the textbook ATM signature, since both are almost pure time value.

**Step 2 — Classify the strikes.** On the call side, 23800 and 23900 are ITM (strike below spot); 24100 and above are OTM. On the put side, it mirrors: 24100 and above are ITM puts; 23900 and below are OTM puts.

**Step 3 — Read the spread and cost.** Say the 24000 call shows bid 178 / ask 180. To buy one lot you pay the ask: `180 * 75 = ₹13,500`. If you immediately sold at the bid (178), you would get `178 * 75 = ₹13,350` — a ₹150 round-trip cost from the spread alone, before brokerage and taxes. That ₹150 is the toll for liquidity.

**Step 4 — Locate resistance from call OI.** Scan the call side above spot. The standout is **24200 with 18.9L OI and a huge +4.7L change** — by far the most call writing, and freshly added today. That marks **24200 as the resistance / expected ceiling** for this expiry. The 24100 strike (11.5L, +2.1L) is a secondary wall.

**Step 5 — Locate support from put OI.** Scan the put side below spot. The largest put OI is **23800 with 12.4L**, with strong fresh additions at 23900 (+1.1L) and 24000 (+1.4L). So **23800 is the support / expected floor**, with 23900 as a nearer cushion.

**Step 6 — Read the implied range.** The option market is, in effect, pricing Nifty to stay roughly between **23800 and 24200** into Thursday's expiry — a tight ~400-point band. A breakout above 24200 or below 23800 would mean those writers are getting run over, which often accelerates the move.

**Step 7 — A glance at PCR.** Add the put OI: `12.4 + 10.2 + 7.5 + 5.1 + 3.4 + 2.0 + 1.3 = 41.9L`. Add the call OI: `9.1 + 7.8 + 6.2 + 11.5 + 18.9 + 9.4 + 7.1 = 70.0L`. So:

`PCR = 41.9 / 70.0 = 0.60 (approx)`

A PCR around 0.60 leans bearish-to-neutral on this slice — there is heavier call writing than put writing, consistent with the strong resistance build-up at 24200. (A real PCR uses the *entire* chain, not seven strikes, so treat this as a teaching figure.)

Put together, the story the chain tells is coherent: *range-bound-to-slightly-heavy, capped near 24200, floored near 23800, with sellers most confident at the 24200 ceiling.*

## Common mistakes / risk note

- **Confusing volume with Open Interest.** Volume is today's trading activity and resets daily; OI is the stock of live positions and carries over. High volume but flat OI means churn, not a new directional bet.
- **Treating OI walls as guarantees.** Support and resistance from OI are *tendencies*, not laws. On trending days or after news (RBI policy, budget, global shocks), price slices straight through the heaviest OI strike. Never place a stop-loss or a naked short purely because "there is big OI there."
- **Reading the LTP as a tradable price.** The LTP is the *last* trade and can be stale, especially on illiquid far-OTM strikes. What you can actually transact at is the bid/ask. Always check the spread before assuming the premium.
- **Chasing wide-spread options.** Deep OTM and far-expiry strikes often have ugly spreads. A beginner who buys at a fat ask and later sells at a thin bid can lose 10–20% to the spread alone, before the market even moves.
- **Over-trusting PCR and max pain.** These are *sentiment hints*, not signals you can trade mechanically. PCR is often contrarian at extremes, and max pain's pull is weak and unreliable, strongest only in the final hours before expiry. Do not build a strategy on them in isolation.
- **The honest backdrop.** Reading the chain well does not change the base rates: most long options expire worthless, option *writing* carries large and sometimes undefined risk, and SEBI's studies show roughly 9 in 10 retail F&O traders lose money. The chain is a tool for better decisions, not a shortcut to easy ones.

## Key takeaways

- The option chain lists every call (left) and put (right) across strikes (centre) for one expiry — a live map of the options market for an underlying.
- Learn every column: LTP/premium (last trade), bid/ask and the spread (what you can transact at, and its hidden cost), volume (today's activity), OI (live open positions), change in OI (where positions are being built now), and IV (the market's expected-move dial).
- The ATM strike is the listed strike nearest spot; at the money, call and put premiums are nearly equal.
- Heavy *call* OI above spot tends to mark **resistance**; heavy *put* OI below spot tends to mark **support**; the band between them is the market's implied range.
- Volume measures flow and resets daily; OI measures standing positions and carries over — never confuse them.
- PCR (`put OI / call OI`) and max pain are quick *sentiment hints*, often contrarian and unreliable at extremes — useful colour, not standalone signals.
- The chain sharpens decisions but does not repeal the hard truths of F&O risk.

## Practice problems

1. **(Conceptual)** On the chain above, Nifty spot is 24000. Classify the 24100 call and the 24100 put as ITM, ATM, or OTM, and explain why.

2. **(Numeric)** The 23900 call shows bid 246 / ask 250, with lot size 75. (a) What does it cost in rupees to buy one lot at market? (b) If you immediately sell it at the bid, how much do you lose to the spread alone, ignoring brokerage and taxes?

3. **(Reading the chain)** Using only the OI and change-in-OI columns above, identify the single strike most likely to act as resistance into expiry, and justify your choice in one sentence.

4. **(Numeric)** Using the seven strikes shown, you computed total put OI = 41.9L and total call OI = 70.0L. Recompute the PCR and state, in one line, what it suggests about sentiment on this slice.

5. **(Conceptual)** A trader notices the 24200 call traded huge volume today but its Open Interest barely changed. What does this tell you about whether new positions were created? 

6. **(Application)** Nifty spot is 24023 and strikes are listed every 50 points. Which strike is ATM, and which is the first OTM call strike?

## Solutions

1. With spot at 24000, the **24100 call is OTM** because its strike (24100) is *above* the spot — you would not exercise the right to buy at 24100 when the market is at 24000, so it has no intrinsic value yet. The **24100 put is ITM** because its strike (24100) is *above* spot — the right to sell at 24100 when the market is 24000 is worth 100 points of intrinsic value. This is the call/put mirror: above spot, calls are OTM while puts are ITM.

2. (a) Buying at market means paying the **ask** of 250: `250 * 75 = ₹18,750` for one lot. (b) Selling immediately at the **bid** of 246 returns `246 * 75 = ₹18,450`. The loss to the spread is `18,750 - 18,450 = ₹300` (equivalently, the ₹4 spread times 75). That ₹300 is pure friction, paid before the market moves at all.

3. The **24200 call** is the most likely resistance. It carries the largest call Open Interest on the chain (18.9L) *and* the largest fresh addition (+4.7L) today, meaning sellers are aggressively writing calls there and betting Nifty will not cross 24200 into expiry — a wall of sellers defending that ceiling.

4. `PCR = 41.9 / 70.0 = 0.60` (approximately). A PCR meaningfully below 1 means more call OI than put OI on this slice, which leans **bearish-to-neutral** — consistent with the heavy call writing capping the market at 24200. (Caveat: a true PCR uses the full chain, not seven strikes.)

5. High volume with flat OI means positions mostly **changed hands rather than being newly created**. For every contract, if an existing holder sold to a new buyer (or an existing writer was replaced by a new writer), a trade is recorded — so volume rises — but the *total* number of open contracts stays the same, so OI does not move. Net-net: lots of churn, little fresh directional commitment.

6. With spot at 24023 and 50-point strikes, the nearest listed strike is **24000**, so **24000 is ATM**. The first strike *above* spot is **24050**, which is the **first OTM call** (strike above spot = OTM for a call). On the put side, the nearest OTM put is **24000** (strike below spot = OTM for a put).
