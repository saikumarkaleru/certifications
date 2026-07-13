# Chapter 46: Income & Hedging — Covered Call, Cash-Secured Put, Protective Put & Collar

Most of this book has treated options as standalone bets — buy a call, sell a strangle, build a condor. But the original, oldest use of options is humbler and arguably more important: bolting an option onto something you *already own* (or already want to own). A farmer who has a field of wheat doesn't want to gamble on the wheat price; he wants to lock in a floor so a bad harvest year doesn't ruin him. An insurance company doesn't want to gamble on your house; it sells you a contract that pays out if it burns. Options started life as exactly these tools — for hedging real holdings and for earning rent on assets you're sitting on.

This chapter covers the four workhorse strategies that combine an option with an underlying position. Two of them *generate income* by selling an option against an asset (the **covered call** and the **cash-secured put**). Two of them *buy insurance* on a portfolio (the **protective put** and the **collar**). For an Indian investor holding a Nifty portfolio or a basket of stocks, these are the practical, sane, survivable uses of the F&O market — the opposite of the lottery-ticket buying and naked-strangle selling that wipes out most retail accounts. They are how you actually use options to manage money you can't afford to lose.

## Core concepts

A quick vocabulary check before we start, since every term must earn its place:

- **Underlying** — the asset the option is written on. Here it's something you hold: a stock, an ETF, or a Nifty/Bank Nifty futures position standing in for "the index".
- **OTM (out of the money)** — a call whose strike is *above* spot, or a put whose strike is *below* spot; it has no intrinsic value yet.
- **Premium** — the price of the option, in points; multiply by the **lot size** to get rupees.
- **Covered** vs **naked** — a short option is "covered" when you hold the asset (or cash) to honour it, and "naked" when you don't. Covered is survivable; naked is where accounts die.

### Strategy 1: The covered call — renting out your shares

Imagine you own a flat that you're holding for the long term but it's sitting empty. Renting it out earns you monthly income; the only "cost" is that for the duration of the lease you can't sell the flat to a buyer who shows up offering a great price. The **covered call** is exactly this. You own the underlying (shares, an ETF, or a long Nifty future), and you **sell an out-of-the-money call** against it. The buyer pays you a premium today. In exchange, you've promised to hand over the upside above the strike if the market rallies past it.

The construction:

```
Covered call = long underlying + short 1 OTM call (same quantity)
Payoff at expiry = (S - S0) + premium     if S <= K   (you keep the shares + rent)
                 = (K - S0) + premium     if S >  K   (called away; upside capped at K)
```

where `S0` is your purchase price, `S` is the price at expiry, and `K` is the call strike.

What you've done is **trade away your unlimited upside above K in return for guaranteed cash today**. The premium does three things: it's income in a flat market, it cushions a small fall (your breakeven drops by the premium received), and it caps your gains. The payoff diagram is the giveaway — it looks like a long position whose top has been sawn off into a flat plateau above the strike.

![Figure: covered call payoff](figs/covered_call.png)

**When to use it.** You're mildly bullish to neutral on something you own and happy to sell it at the strike if it gets there. You think the next month is likely to be flat or slowly rising, not explosive. It's an income strategy for a sideways market — you collect rent month after month while the stock goes nowhere.

**The cost/benefit.** The benefit is real, regular income and a small downside cushion. The cost is opportunity: if the stock rockets, you're "called away" at the strike and watch the rest of the rally from the sidelines, having capped your own gain. And note the asymmetry the diagram makes brutally clear — your downside is *still nearly the full downside of owning the stock* (cushioned only by the small premium), while your upside is capped. A covered call does **not** protect you from a crash; it just pays you a little rent on the way down. People who forget this get badly hurt in a falling market.

### Strategy 2: The cash-secured put — getting paid to bid

Suppose you'd love to buy Reliance, but only at a price 5% below where it trades today. You could leave a limit order and wait. Or — you could **sell a put** at that lower strike and get *paid* to wait. If the stock falls to your level, you're assigned and buy it exactly where you wanted, with the premium making your effective purchase even cheaper. If it doesn't fall, you simply keep the premium as consolation. This is the **cash-secured put**: you sell an OTM put and set aside the full cash needed to buy the stock if assigned.

```
Cash-secured put = short 1 OTM put + cash held to buy the stock at K
Payoff at expiry = premium                        if S >= K   (put expires worthless)
                 = (S - K) + premium              if S <  K   (assigned; you buy at K)
Effective purchase price if assigned = K - premium
```

The word **cash-secured** is the whole point. A naked short put has large downside and the broker demands SPAN margin; a *cash-secured* put means you've earmarked the money to honour the purchase, so it's a deliberate "I want to own this lower" position, not a leveraged gamble. The payoff is the mirror image of the covered call — in fact it's a **short put**, and by put-call parity a cash-secured put has the *same payoff shape* as a covered call. Both are "sell upside / insurance, keep premium, accept the downside" trades.

**When to use it.** You're neutral-to-bullish on a stock or index you genuinely want to own, and you'd be happy to buy it at the strike. It's the entry strategy that pairs naturally with the covered call: sell a put to get into a position cheaply, then once assigned, sell calls against it. (This two-step cycle is popularly called "the wheel".)

**The cost/benefit.** Benefit: income while you wait, and a lower effective entry price if assigned. Cost: if the stock collapses far below the strike, you're obligated to buy at K while it's worth much less — your loss below the strike is the same as if you'd simply bought the stock there. You give up the chance of buying it at the *new, even lower* price. And in India, remember **stock options are physically settled** — if assigned on a stock put, you must actually take (and pay for) delivery of the shares, so the cash must really be there.

### Strategy 3: The protective put — insurance for your portfolio

Now we flip from selling options to buying them. You own a portfolio and you're worried about a crash — maybe a Budget, an election result, or a global wobble is coming. You don't want to sell your holdings (taxes, conviction, you'd have to buy back). Instead you **buy a put** below the current level. That put is an insurance policy: if the market falls below the strike, the put gains rupee-for-rupee and offsets your portfolio's losses. If the market rises, the put expires worthless and all you've lost is the premium — exactly like paying for fire insurance and the house not burning down.

```
Protective put = long underlying + long 1 put
Payoff at expiry = (S - S0) - premium     if S >= K   (full upside, minus insurance cost)
                 = (K - S0) - premium     if S <  K   (losses floored below K)
Maximum loss = (S0 - K) + premium         (fixed, known floor)
```

The protective put gives your holding a **hard floor** while keeping the **full upside** (minus the premium you paid). The payoff diagram looks like a long stock position with the bottom-left losing tail bent flat — losses can't run past the floor.

![Figure: protective put payoff](figs/protective_put.png)

**When to use it.** You're bullish or committed long-term but scared of a specific near-term downside — a known event, a stretched market, a position too large to stomach a 20% drawdown. It's pure insurance: you keep all the upside and cap the downside, and you pay a premium for the privilege.

**The cost/benefit.** Benefit: a precise, known worst case and complete peace of mind through an event, with upside intact. Cost: the premium is a real, recurring drag. Insurance isn't free — buy puts every month and the cumulative premium can quietly eat much of your return, especially when India VIX is high and puts are expensive (which, frustratingly, is exactly when you most want them). Protective puts are best used **selectively around identifiable risks**, not as a permanent always-on hedge that bleeds you dry.

### Strategy 4: The collar — insurance you pay for by renting out the upside

The protective put's one flaw is its cost. The **collar** solves that elegantly: you buy the protective put *and* sell a covered call to fund it. The call premium pays for (most or all of) the put premium. You've combined Strategy 1 and Strategy 3 on the same holding.

```
Collar = long underlying + long 1 OTM put + short 1 OTM call
Net cost = put premium - call premium     (often near zero — a "zero-cost collar")
Payoff at expiry:
  S <  Kput   : floored at (Kput - S0) - net cost      (put protects)
  Kput<=S<=Kcall : (S - S0) - net cost                 (you ride the stock)
  S >  Kcall  : capped at (Kcall - S0) - net cost       (called away)
```

The result **brackets your outcome inside a range**: you can't lose more than the floor set by the put, and you can't gain more than the cap set by the call. You've traded away the fat tails on both ends — no disaster, but also no jackpot — and paid little or nothing for the protection. When the call premium exactly equals the put premium, it's a celebrated **zero-cost collar**: downside insurance for free, funded entirely by giving up your upside above the call strike.

![Figure: collar payoff](figs/collar.png)

**When to use it.** You hold a large, appreciated position you want to protect cheaply through a risky patch, and you're willing to cap upside to avoid paying for the put. It's the institutional hedge of choice — promoters, funds, and serious portfolio holders use collars to ride out events without selling and without bleeding premium.

**The cost/benefit.** Benefit: protection at little or no cash cost, with a defined, comfortable range of outcomes. Cost: you surrender the upside above the call strike — if the market rips higher, you're capped and called away, just like a covered call. The collar is the honest middle path: you give up the dream to be rid of the nightmare.

### The India angle: hedging a portfolio around events

Indian markets are *event-driven* in a way that makes these hedges especially valuable. The **Union Budget** (February), **RBI policy** meetings, **general election** results, quarterly **corporate results** season, and overnight **global cues** all produce sharp, scheduled-or-semi-scheduled gaps. India VIX — the market's fear gauge — visibly climbs into these events and collapses afterward. An investor sitting on a Nifty portfolio has clean, liquid tools to manage this:

- **To hedge an index portfolio:** buy Nifty (or Bank Nifty) puts as a protective put on the whole book. Because index options are **European and cash-settled**, the hedge settles cleanly in cash at the closing level — no delivery hassle. One Nifty put can insure a diversified large-cap portfolio that broadly tracks the index.
- **To hedge cheaply through a Budget or election:** put on a **collar** — buy a protective put a few percent below spot and sell a call a few percent above to fund it. You sleep through the result knowing your worst case is fixed, and it cost you almost nothing because event-inflated call premiums richly fund the put.
- **The hedge ratio matters:** to fully hedge a ₹15 lakh portfolio with Nifty at 24,000 and a lot size of ~75, one lot covers about `24,000 * 75 = ₹18 lakh` of notional — roughly the whole portfolio. Match the notional, not the lot count by gut.

A subtle point: a put on the index only hedges *market* (systematic) risk. If your portfolio is concentrated in a few stocks, an index put won't protect you from a company-specific disaster — for that you'd need stock options (physically settled) on those names. Hedge the risk you actually carry.

## Worked example (₹, Nifty)

Let's price a **zero-cost collar** on a Nifty portfolio ahead of the Union Budget. Assume:

- You hold a portfolio worth about **₹18,00,000** that closely tracks Nifty.
- **Nifty spot = 24,000**, monthly expiry spanning the Budget, **lot size = 75** (current Nifty lot; verify, as it changes).
- One lot of notional = `24,000 * 75 = ₹18,00,000` — matches your portfolio, so **one lot fully hedges it.**

You build the collar by buying a downside put and selling an upside call:

| Leg | Strike | Type | Action | Premium (points) |
|-----|--------|------|--------|------------------|
| Protective put | 23,400 | Put | Buy | 180 |
| Covered call | 24,700 | Call | Sell | 175 |

**Step 1 — Net cost of the hedge.**

```
Net cost = put premium - call premium = 180 - 175 = 5 points
        = 5 * 75 = ₹375 for the whole month
```

For ₹375 — essentially free — you've insured an ₹18 lakh portfolio through the Budget. That's the magic of the collar: the call you sold paid for almost all of the put you bought.

**Step 2 — The downside floor.** If Nifty crashes below 23,400, your portfolio falls with it but the put gains rupee-for-rupee below 23,400. Your floor:

```
Worst case Nifty level protected = 23,400
Portfolio drop to floor = (24,000 - 23,400) / 24,000 = 2.5%
Maximum portfolio loss ≈ 2.5% + ₹375 ≈ ₹45,000 + ₹375 ≈ ₹45,375
```

No matter how badly the Budget is received — even a 10% gap-down — your loss is capped near ₹45,000. Without the hedge, a 10% fall would cost ₹1,80,000.

**Step 3 — The upside cap.** If Nifty rallies above 24,700, you're called away at 24,700 — your gains stop there.

```
Maximum portfolio gain = (24,700 - 24,000) / 24,000 ≈ 2.9% ≈ ₹52,500, minus ₹375
```

**Step 4 — The comfortable middle.** If Nifty closes anywhere between 23,400 and 24,700 (a +2.9% / -2.5% band), both options expire worthless and your portfolio simply gains or loses with the market, having paid ₹375 for the insurance you didn't need to use.

**Step 5 — Read the outcome map.** At expiry (index options cash-settled at the Nifty closing level):

- **Nifty closes at 22,000** (Budget disappoints, -8.3%): portfolio loses ~₹1,50,000, but the 23,400 put gains `(23,400 - 22,000) * 75 = ₹1,05,000`, netting a loss of only ~₹45,000. *Floor held.*
- **Nifty closes at 24,000** (flat): portfolio flat, both options expire worthless, you're out the ₹375. *Insurance not needed.*
- **Nifty closes at 26,000** (Budget euphoria, +8.3%): portfolio gains ~₹1,50,000 on paper, but the 24,700 call you sold loses `(26,000 - 24,700) * 75 = ₹97,500`, so your net gain is capped at ~₹52,500. *You gave up the top of the rally.*

The collar did its job: a violent, scary event became a bounded, sleep-at-night range for the price of a cup-of-coffee premium.

**Costs to remember (India-specific).** You pay brokerage and exchange fees on both legs, plus **STT** (Securities Transaction Tax — charged on the sell side of the call premium, and on settlement of in-the-money options at expiry on the settlement value). If your sold call or bought put finishes deep in the money on a Nifty event, settlement STT can surprise you — close ITM legs before expiry where possible. Net these out of the ₹375; on a one-lot collar they're modest but real.

## Common mistakes / risk note

- **Treating a covered call as downside protection.** It isn't. The premium cushions only a tiny fall; below that, you eat almost the full loss of the stock while your upside stays capped. In a crash, a covered call is barely better than just holding the stock.
- **Capping upside on your best holdings.** Selling calls on a stock you'd hate to lose to a takeover or breakout means you'll get called away exactly when it matters most. Sell calls on holdings you're genuinely happy to part with at the strike.
- **Forgetting physical settlement on stock options.** A cash-secured put on a stock that finishes ITM means you must take *delivery* and pay the full purchase amount. Make sure the cash is actually there, and know your broker's expiry-day delivery rules.
- **Buying protective puts permanently.** Insurance bought every single month bleeds your returns dry, especially when VIX is high. Use protective puts *selectively* around identifiable risks, not as an always-on tax.
- **Mismatching the hedge.** Hedging a concentrated single-stock portfolio with a Nifty put leaves your real (company-specific) risk uncovered. And under-/over-sizing the notional means you're either half-hedged or accidentally net-short. Match notional to portfolio.
- **Chasing zero-cost too aggressively.** To make a collar truly free in low-volatility conditions you may have to sell a call so close to spot that you cap nearly all your upside. "Zero cost" is never zero — you always pay in surrendered upside.

## Key takeaways

- These four strategies bolt an option onto a holding: two earn **income** (covered call, cash-secured put), two buy **insurance** (protective put, collar).
- **Covered call** = long underlying + short OTM call: rent for a flat market, small downside cushion, capped upside — but **not** crash protection.
- **Cash-secured put** = short OTM put + cash set aside: get paid to potentially buy lower; effective entry = strike - premium; same payoff shape as a covered call.
- **Protective put** = long underlying + long put: a hard downside floor with full upside intact, paid for with a recurring premium — best used selectively around events.
- **Collar** = long underlying + long put + short call: brackets the outcome in a range, with the call funding the put — often **near zero cost**, at the price of capped upside.
- **India angle:** use Nifty/Bank Nifty puts (European, cash-settled) for protective puts, and **collars around the Budget, RBI policy, results, and elections** to hedge cheaply through known event risk. Match notional to portfolio.
- Insurance always costs something — either premium (protective put) or surrendered upside (collar/covered call). There is no free hedge, only a choice of how you pay.

## Practice problems

1. **Construction check.** An investor owns 1 lot of a Nifty future at 24,000 and sells a 24,500 call for 90 points. Name the strategy, and state the maximum profit (in points) and what happens if Nifty closes at 25,200 at expiry.

2. **Cash-secured put entry.** You sell a 23,500 Nifty put for 120 points, holding cash to buy at the strike. Lot size 75. (a) If Nifty closes at 23,800, what's your profit? (b) If you're assigned, what's your effective purchase price per unit?

3. **Protective put floor.** You hold a portfolio tracking Nifty bought at 24,000 and buy a 23,000 put for 150 points. What is your maximum loss per unit, and at what Nifty level do you break even on the upside?

4. **Collar cost.** Holding Nifty at 24,000, you buy a 23,500 put for 160 points and sell a 24,600 call for 140 points. (a) What's the net cost of the collar in points and in rupees (lot 75)? (b) Below what level are you protected, and above what level are you capped?

5. **Event hedge sizing.** A ₹36,00,000 portfolio tracks Nifty, which is at 24,000 with a lot size of 75. How many lots of Nifty puts roughly fully hedge the portfolio's market risk, and why might an index put still leave the investor exposed?

6. **Cost/benefit judgement.** Two investors face the Budget. Investor A buys a protective put (net cost 180 points). Investor B puts on a zero-cost collar (net cost ~0). Nifty then rallies 6% on a great Budget. Who is happier at expiry, and what did each give up?

## Solutions

**1.** This is a **covered call** (long underlying + short OTM call). Maximum profit = the gain to the strike plus the premium = `(24,500 - 24,000) + 90 = 500 + 90 = 590 points` (`590 * 75 = ₹44,250` per lot). If Nifty closes at 25,200, you're capped: the future gains 1,200 points but the short 24,500 call loses `25,200 - 24,500 = 700` points, leaving `1,200 - 700 + 90 = 590` points — the same capped maximum. You gave up the 700 points of rally above 24,500.

**2.** Premium received = 120 points. (a) If Nifty closes at 23,800 (above the 23,500 strike), the put expires worthless and you keep the full `120 * 75 = ₹9,000`. (b) If assigned (Nifty below 23,500), your effective purchase price = strike - premium = `23,500 - 120 = 23,380` per unit — you bought at the level you wanted, made cheaper by the premium.

**3.** Maximum loss per unit = `(S0 - K) + premium = (24,000 - 23,000) + 150 = 1,000 + 150 = 1,150 points` (`1,150 * 75 = ₹86,250` per lot) — a fixed floor no matter how far Nifty falls. Upside breakeven = `24,000 + 150 = 24,150`: Nifty must rise past 24,150 for the portfolio to clear the cost of the insurance and turn a net profit.

**4.** (a) Net cost = put premium - call premium = `160 - 140 = 20 points` = `20 * 75 = ₹1,500` per lot — a near-costless collar. (b) You're protected below **23,500** (the put floor) and capped above **24,600** (the call ceiling). Between 23,500 and 24,600 your portfolio simply rides Nifty, having paid 20 points for the bracket.

**5.** One lot of Nifty notional = `24,000 * 75 = ₹18,00,000`. The portfolio is ₹36,00,000, so `36,00,000 / 18,00,000 = 2 lots` of puts roughly fully hedge the market (systematic) risk. It still leaves exposure because an index put only offsets *market-wide* moves — if the portfolio is concentrated and a specific holding suffers a company-specific blow (a fraud, an earnings miss) while the index is flat, the index put pays nothing. Stock-specific risk needs stock-specific hedges (physically settled stock options).

**6.** **Investor B (the collar) is happier on a flat-to-modest market but here, on a 6% rally, it's nuanced.** A rallies 6% minus 180 points of premium — a near-full gain, because the protective put leaves upside intact (it just cost something). B is **capped** at the call strike: a zero-cost collar that sold a call ~2-3% above spot stops gaining there, so B captures only the rise up to the cap and forfeits the rest of the 6% move. So on a *strong rally*, **A is happier** — A paid premium but kept the full upside, while B saved the premium but surrendered the top of the rally. The lesson: the protective put pays in *cash* (premium) to keep upside; the collar pays in *surrendered upside* to save cash. Which is "better" depends entirely on whether the market then rallies hard (favours the put) or stays bounded (favours the collar). There is no free hedge — only a choice of how you pay for it.
