# Chapter 14: Short Put — Selling Bullish / Getting Paid to Buy

Imagine you genuinely want to buy a flat in a building you like, but you think today's price is a little too high. You'd happily buy it 8% cheaper. So you go to the owner and say: "Pay me a fee today, and in return I promise that if the price falls to my level over the next month, I'll buy it from you at that level." If the price never falls, you keep the fee and walk away — you got paid for your patience. If it does fall, you buy the flat at the price you wanted anyway, and you're a little richer for the fee you already pocketed. That, in one sentence, is a **short put**: you sell someone the right to *sell the underlying to you* at a fixed price, you collect cash up front for taking on that obligation, and you profit as long as the market stays up, drifts sideways, or only falls a little.

A short put is the mirror image of a short call. The short call seller is bearish-to-neutral and dreads a rally. The short put seller is **bullish-to-neutral** and dreads a crash. It is one of the most popular income strategies in the world — and one of the most dangerous when done carelessly, because the risk lives in exactly the place beginners ignore: the rare, violent fall. This chapter teaches both faces of it: the disciplined "get paid to buy" version that professionals respect, and the hidden fat tail that quietly wrecks the careless.

## Core concepts

### What you are actually selling

A **put option** gives its *buyer* the right (not the obligation) to sell the underlying at a fixed **strike price** K on or before expiry. When you **sell** (also called **write**) that put, you take the other side. You receive a **premium** today, and in exchange you accept an obligation: if the put buyer chooses to exercise, you must **buy the underlying from them at K**, no matter how far the market has fallen below K.

So the put buyer is buying insurance against a fall. You, the put seller, are the insurance company: steady small profits most of the time, a large loss occasionally. Whether that's a good business depends entirely on whether you priced the premium well and sized the position sanely.

### The payoff: small fixed gain, large variable loss

Let S be the price of the underlying at expiry, K the strike, and let `premium` be what you collected per unit. Your payoff per unit is:

```
Payoff (short put) = premium - max(K - S, 0)
```

Read it in two pieces:

- The `premium` is yours the moment you sell. It is the most you can ever make.
- The `max(K - S, 0)` is what you owe the buyer at expiry. If S stays at or above K, this term is zero — the put expires worthless and you keep the whole premium. If S falls below K, this term grows rupee-for-rupee as S falls, and it is subtracted from your premium.

Let's name the three landmark numbers.

```
Maximum profit  = premium                 (when S >= K at expiry)
Breakeven       = K - premium             (the price at which P&L = 0)
Maximum loss    = (K - premium) per unit  (when S falls all the way to 0)
```

The maximum loss formula deserves a stare. The worst case is the underlying going to zero. Then you are forced to buy at K something now worth nothing, after pocketing `premium`, so you lose `K - premium` per unit. For a Nifty 24000 put that collected ₹200, the theoretical worst case is `24000 - 200 = 23800` points of loss **per unit** — and one Nifty lot is about 75 units, so the absolute-worst loss is around `23800 * 75 ≈ ₹17.85 lakh` on a contract you sold for `200 * 75 = ₹15,000`. The index will not actually go to zero, but the *shape* of the risk is the point: you risk a large, market-sized number to earn a small, fixed one. This asymmetry is the entire personality of option selling.

### Why anyone sells puts: the three legitimate motives

If the loss is so lopsided, why is selling puts a respected professional strategy? Three honest reasons.

1. **Probability is on your side.** Markets drift up over long horizons, and an out-of-the-money put pays out only if the market falls past your strike. Most of the time it expires worthless and you keep the premium — insurance that usually isn't claimed.

2. **Implied volatility is usually richer than realised volatility.** Put buyers are often frightened buyers who overpay for downside protection, especially on indices, because people will pay up to sleep at night. This is the **volatility risk premium**, and the put seller harvests it. (We unpack skew in later chapters; for now, just know index puts are structurally a bit expensive, tilting the odds toward the seller.)

3. **You actually want to own the thing.** The cleanest motive — and it leads us to the cash-secured put.

### The cash-secured put: getting paid to buy

A **cash-secured put** is a short put where you set aside enough cash to actually buy the underlying at the strike if you get assigned. You are not gambling — you are placing a disciplined limit order to buy, and getting paid a premium while you wait.

Here is the logic, step by step:

- You want to own (say) a stock or accumulate index exposure, but you think today's price is slightly high. You'd be happy to buy 8–10% lower.
- Instead of placing a passive limit buy order at that lower price and earning nothing while you wait, you **sell a put** at that lower strike.
- **Outcome A — the market stays up.** The put expires worthless. You keep the premium. You didn't get your shares, but you got paid for your patience, and you can do it again next month. Your effective "interest" on the cash you reserved can be attractive.
- **Outcome B — the market falls to your strike.** You're assigned. You buy the underlying at K — the price you wanted anyway — and because you already pocketed the premium, your **effective purchase price is `K - premium`**, which is *below* the strike. You bought what you wanted, at a discount to the price you'd already decided was fair.

In both outcomes you win relative to having done nothing. That is why the cash-secured put is sometimes called "getting paid to buy." The catch — and there is always a catch — is **Outcome C: the market doesn't stop at your strike, it keeps falling.** You're still obligated to buy at K while the price is now far below `K - premium`. You own the underlying at a loss. The strategy only "gets paid to buy" the thing you genuinely wanted at a price you genuinely liked; it does not protect you from a crash. More on that tail below.

### Assignment and settlement: what you actually receive

What lands in your account when a short put is exercised against you depends on what you sold.

- **Index options (Nifty, Bank Nifty) are European and cash-settled.** "European" means the buyer can only exercise *at* expiry, so you can't be assigned early. "Cash-settled" means no basket of stocks changes hands — at expiry the exchange simply debits the cash difference `max(K - settlement, 0)` per unit from your account. You never literally "buy the index." For an index cash-secured put, "setting aside the cash" is a discipline you impose on yourself, not a literal share purchase.
- **Single-stock options in India are physically settled.** If you sold a put on, say, Reliance and it finishes in-the-money, you will be **delivered the actual shares** and must pay K per share for the full lot — a real, large cash event of several lakh rupees. Traders who forget this get an ugly expiry-day surprise: a stock they didn't plan to own, bought with money they didn't plan to spend, plus possible auction penalties if they can't fund it. With physically settled stock puts, *always* know whether you can and want to take delivery before letting one expire in-the-money.

### Margin: the price of admission for sellers

When you *buy* an option, you pay the premium and that's the end of it — your maximum loss is the premium, so no further collateral is needed. When you *sell* a put, your potential loss is large, so the exchange demands **margin**: collateral posted up front to guarantee you can meet the obligation.

In India, margins are computed using the **SPAN + Exposure** system. SPAN simulates a range of adverse moves in price and volatility and charges you the worst-case loss across those scenarios; the exposure margin is an additional buffer on top. For a single Nifty put this typically runs into the range of roughly ₹1–1.5 lakh of blocked capital per lot, varying with strike, volatility, and India VIX. Two consequences follow:

- **Your real return is on margin, not premium.** Collecting ₹15,000 against ₹1.2 lakh of blocked margin is about a 12.5% gross return *for that holding period* — not the eye-popping "infinite" return beginners imagine because "I didn't pay anything." You did pay: you tied up capital that could have earned elsewhere.
- **Margins rise exactly when you're hurting.** If the market falls and volatility spikes, SPAN re-prices the worst case higher and your margin requirement *increases* on a position that is already losing. If you're fully deployed, you face a **margin call** and may be forced to close at the worst possible moment. Never sell puts to the hilt of your available margin; keep a deep buffer.

### Short put vs covered call: same payoff shape, different risk story

Here is a fact that confuses many people and enlightens the rest: **a cash-secured short put has essentially the same payoff shape as a covered call** at the same strike. Both are short-volatility, neutral-to-bullish income trades with a capped upside (the premium plus, for the covered call, a little room to the strike) and a large downside if the underlying collapses. They are **synthetically equivalent** — the algebra of put-call parity makes a short put behave like a covered call.

The difference is *operational and psychological*, not in the risk curve:

- A **covered call** means you already own the underlying and sell a call against it. Your downside is "my stock falls." It *feels* safe because you hold a familiar asset, but you are fully exposed to the fall.
- A **cash-secured put** means you don't own the underlying yet; you hold cash and sell a put. Your downside is "I'm forced to buy a falling asset." It *feels* riskier, but the actual risk is the same.

Many professionals prefer the short put for entering a position: one transaction with one set of costs, versus buying stock and selling a call (two legs, two commissions, more capital). The lesson — don't let the covered call's cozy framing fool you into thinking it's lower-risk than a short put. They are the same trade wearing different clothes.

## Worked example (₹, Nifty/Bank Nifty)

Let's walk through a cash-secured Nifty put end to end.

**Setup.** Nifty spot is at **24,000**. You are mildly bullish — you think Nifty holds above 23,500 over the next week — and you'd be content to accumulate index exposure around 23,800 if it dipped. The weekly **24000 put** (at-the-money) is trading at **₹200**. Lot size is about **75 units**. You sell **1 lot**.

**Cash collected up front:**

```
Premium received = 200 * 75 = ₹15,000
```

This ₹15,000 is credited to you immediately (your maximum profit). The broker blocks SPAN + exposure margin — assume about **₹1,20,000** for this lot.

**The landmark numbers:**

```
Maximum profit = premium                = ₹200 per unit  = ₹15,000 per lot
Breakeven      = K - premium            = 24000 - 200     = 23,800
Maximum loss   = (K - premium) per unit = 23,800 per unit = ₹17,85,000 per lot (theoretical, S -> 0)
```

**Now expiry day. Four scenarios.**

*Scenario 1 — Nifty closes at 24,300 (rallied).* The put is out-of-the-money; `max(24000 - 24300, 0) = 0`. It expires worthless. You keep the full ₹15,000. Return on margin ≈ `15000 / 120000 ≈ 12.5%` for the week. Excellent — and you take no delivery because it's cash-settled.

*Scenario 2 — Nifty closes at 24,000 (flat).* Still `max(24000 - 24000, 0) = 0`. The put expires exactly at-the-money, worthless to the buyer. You keep all ₹15,000.

*Scenario 3 — Nifty closes at 23,900 (small dip, between breakeven and strike).* Now `max(24000 - 23900, 0) = 100` per unit owed.

```
Payoff per unit = premium - (K - S) = 200 - 100 = +100
Net P&L         = 100 * 75 = +₹7,500
```

You're still profitable because the dip (100 points) was smaller than the cushion your premium bought you (200 points). Your breakeven was 23,800; the market stayed above it.

*Scenario 4 — Nifty closes at 23,300 (a hard 700-point fall).* Now `max(24000 - 23300, 0) = 700` per unit owed.

```
Payoff per unit = 200 - 700 = -500
Net P&L         = -500 * 75 = -₹37,500
```

You collected ₹15,000 and lost ₹37,500 — a net loss of ₹37,500, more than double your premium, on a single ordinary-looking down week. Notice how fast the loss outran the gain: a 700-point fall (about 2.9%) turned a ₹15,000 credit into a ₹37,500 debit. That is the asymmetry in living colour.

The figure below plots this exact position — a short 24000 put — across the full range of expiry prices. The line is flat and positive on the right (you keep the premium), bends down at the strike, and slopes relentlessly downward to the left.

![Figure: payoff of a short 24000 put at expiry](figs/short_put.png)

**The cash-secured framing.** Had you reserved the full notional — about `24000 * 75 = ₹18 lakh` — you would never face a margin call from this trade, and in Scenario 4 you'd simply hold an index position acquired at an effective `24000 - 200 = 23,800`, now marked at 23,300. A paper loss, but on exposure you wanted, at a price below the strike. That discipline — reserving the cash and choosing a strike you'd be *happy* to buy at — is what separates "getting paid to buy" from "blindly selling premium."

## Common mistakes / risk note

- **Confusing premium return with risk.** "I made ₹15,000 risking nothing" is wrong on both counts. You risked up to ₹17.85 lakh in theory and tied up ₹1.2 lakh of margin in practice. Always quote your return on **margin or notional**, never on premium alone.
- **Selling puts in a falling, high-VIX market because the premiums are "juicy."** Premiums are fat precisely when the market is scared and the probability of a further fall is genuinely higher. Fat premium is compensation for real risk, not free money. Selling into a crash is how accounts blow up.
- **Ignoring the tail.** Option selling produces many small wins and the occasional catastrophic loss. The 2020 COVID crash and budget-day gaps skip right past your "I'll just buy it back if it goes against me" plan, because the market opens far below your strike with no chance to exit in between. **One bad gap can erase months of premium.** Size every short put so the worst realistic gap is survivable.
- **Forgetting physical settlement on stock options.** Let an in-the-money stock put ride into expiry and you'll be delivered shares and a large cash bill. For index puts (cash-settled) this specific risk doesn't apply, but the cash debit on a deep loss does.
- **Maxing out margin.** Using all available margin leaves no room for the margin *increase* that comes when the trade moves against you — a spike in India VIX can then force you out at the bottom. Keep a large buffer.
- **Treating it as "set and forget."** A short put needs monitoring. Most professionals define a loss point (e.g., exit at 2x the premium loss, or if the underlying breaks a key level) before entering, and honour it.

## Key takeaways

- A **short put** collects a premium today in exchange for the obligation to buy the underlying at strike K. It is a **neutral-to-bullish, income** strategy.
- Payoff per unit = `premium - max(K - S, 0)`. **Max profit = premium**; **breakeven = K - premium**; **max loss = K - premium per unit** (large — realised if the underlying collapses).
- The **cash-secured put** is the disciplined form: reserve the cash, pick a strike you'd genuinely be happy to buy at, and your effective purchase price becomes `K - premium`, a discount to the strike. You "get paid to buy."
- **Index puts are European, cash-settled** (you can't be assigned early; you receive/owe cash). **Stock puts are physically settled** (you receive actual shares and must pay for them).
- Selling puts requires **SPAN + exposure margin**, which *rises* when the trade goes against you — never sell to the limit of your margin.
- A cash-secured short put is **synthetically the same trade as a covered call**; don't let either framing trick you about the risk.
- The danger is the **fat tail**: gap-down crashes can lose far more than the premium collected. Size for the worst realistic gap, not the typical week.

## Practice problems

1. **(Conceptual)** A trader says, "I sold a Nifty put and the premium is pure profit — there's no way to lose because I didn't pay anything." State two things wrong with this claim.

2. **(Numeric)** You sell one Bank Nifty **52000 put** for a premium of **₹400**. Lot size is about **15 units**. Compute (a) premium collected per lot, (b) breakeven price, and (c) the theoretical maximum loss per lot if Bank Nifty went to zero.

3. **(Numeric)** Using the same 52000 put from Problem 2, compute your net P&L per lot at expiry if Bank Nifty closes at (a) 52,500, (b) 51,800, and (c) 50,900.

4. **(Conceptual)** You sell a cash-secured put on a single stock at a strike of ₹1,000, collecting ₹30 premium per share, lot size 500. The stock closes at ₹950 on expiry. What physically happens to your account, and what is your effective per-share cost of the shares you now hold?

5. **(Conceptual)** Explain why the margin requirement on a short put you've sold can *increase* the day after you sell it, even if you've done nothing, and why that is dangerous.

6. **(Applied)** Your friend wants to "earn safe monthly income" by selling deep out-of-the-money Nifty puts every week with all of his ₹5 lakh capital deployed as margin. Give two specific risks and one change you'd insist on.

## Solutions

1. **Two errors.** (i) *"I didn't pay anything"* is false — the broker blocks substantial SPAN + exposure margin (often ₹1–1.5 lakh per Nifty lot), so capital is very much tied up. (ii) *"No way to lose"* is false — the maximum loss is `K - premium` per unit, a large market-sized number realised if the index falls hard. The premium is the *most* you can make, not a floor on losses. A single gap-down can lose multiples of the premium.

2. **52000 put, premium ₹400, lot 15.**
   - (a) Premium collected = `400 * 15 = ₹6,000` per lot.
   - (b) Breakeven = `K - premium = 52000 - 400 = 51,600`.
   - (c) Theoretical max loss = `(K - premium) per unit * lot = (52000 - 400) * 15 = 51600 * 15 = ₹7,74,000` per lot (if Bank Nifty went to 0). Real-world worst cases are smaller but still very large.

3. **Net P&L per lot (payoff per unit = `400 - max(52000 - S, 0)`, times 15).**
   - (a) S = 52,500: `max(52000 - 52500, 0) = 0`; payoff = `400 - 0 = 400`/unit; P&L = `400 * 15 = +₹6,000` (keep full premium).
   - (b) S = 51,800: `max(52000 - 51800, 0) = 200`; payoff = `400 - 200 = +200`/unit; P&L = `200 * 15 = +₹3,000` (still profitable — dip smaller than premium cushion; above breakeven 51,600).
   - (c) S = 50,900: `max(52000 - 50900, 0) = 1100`; payoff = `400 - 1100 = -700`/unit; P&L = `-700 * 15 = -₹10,500` (loss; market closed below breakeven). Note the loss (₹10,500) already exceeds the premium collected (₹6,000) on a fall of just over 2%.

4. **Physical settlement.** The stock closed at ₹950, below the ₹1,000 strike, so the put you sold is in-the-money and is exercised against you. Because single-stock options are **physically settled**, you are **delivered 500 shares** and must **pay ₹1,000 per share = ₹5,00,000** for them. You now own 500 shares of a stock currently worth ₹950 (₹4,75,000 market value). Your **effective cost per share = strike - premium = 1000 - 30 = ₹970**. So you're holding shares with an effective basis of ₹970 against a market price of ₹950 — a paper loss of ₹20/share (₹10,000 on the lot), and you've committed ₹5 lakh of cash you must be able to fund.

5. **Margin can rise because** it is computed from a worst-case scenario (SPAN), which depends on current price and **implied volatility / India VIX**. If the underlying falls toward your strike and/or volatility spikes, the simulated worst-case loss grows, so the exchange blocks *more* margin against the same position. This is dangerous because the margin demand increases **precisely when the trade is already losing money** — a double squeeze. If you were near-fully deployed, you face a **margin call** and may be forced to close at the worst moment, locking in the loss. The defence is to keep a large unused margin buffer.

6. **Risks and a fix.**
   - *Risk 1 — tail/gap risk.* Deep-OTM puts have a high win rate but a brutal payoff when a crash blows past the strike; one COVID-style gap-down can lose many months of accumulated premium in a single session.
   - *Risk 2 — margin-call risk from full deployment.* With all ₹5 lakh as margin, a market fall both creates losses *and* raises the margin requirement, forcing liquidation at the bottom.
   - *Insisted change:* Deploy only a fraction of capital (e.g., use no more than ~40–50% of margin, keeping a large buffer), and/or **convert the naked short put into a defined-risk spread** by buying a cheaper, lower-strike put — turning unlimited-style downside into a known, survivable maximum loss. Define a pre-set exit (e.g., close at 2x premium loss) before entering.
