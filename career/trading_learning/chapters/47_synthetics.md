# Chapter 47: Synthetics — Building Any Position from Parts

Here is a liberating idea that changes how you see the entire options market: there is no such thing as a "call position" or a "put position" or a "futures position" that is fundamentally different from the others. They are all the *same set of Lego bricks*, snapped together in different orders. A long Nifty future, it turns out, is nothing more than a long call and a short put hiding under a different name. A protective put is secretly just a call. Once you see this, you stop memorising dozens of separate strategies and start seeing one underlying grammar — a small alphabet of parts that can spell any position you want.

The machine that makes this possible is **put-call parity**, the no-arbitrage rule from Chapter 17. Parity ties four instruments — a call, a put, the underlying, and cash — into one equation, and any four-term equation can be rearranged to isolate any one term using the other three. That rearrangement *is* a recipe for a synthetic. This chapter turns that algebra into a toolkit: how to manufacture a long underlying, a short underlying, a call, or a put from the others; why the futures and options markets are the same market wearing two hats; how arbitrageurs called **conversions** and **reversals** force the prices to agree; and why professionals reach for synthetics constantly. We finish with the **box spread** — a synthetic loan — and a full ₹ Nifty example proving a synthetic long *is* a futures position.

## Core concepts

### The one equation everything grows from

Recall put-call parity for European options (Chapter 17):

`C + K*e^(-r*T) = P + S`

where `C` is the call price, `P` the put price (same strike K, same expiry), `S` the spot price of the underlying, `r` the risk-free rate, and `T` the time to expiry in years. The term `K*e^(-r*T)` is just the present value of the strike — the cash you set aside today to have exactly K rupees at expiry.

Think of this equation as a balance scale with four weights on it. If you know any three, the fourth is forced. More usefully: **you can move any single weight to the other side, and whatever ends up alone is "synthesised" by the combination across from it.** That is the entire trick. Every synthetic in this chapter is one line of algebra applied to this one equation. Let us derive them.

### Synthetic long underlying = long call + short put

Start by isolating the spot `S`. Rearranging parity:

`S = C - P + K*e^(-r*T)`

Read the right side as a position: **buy a call, sell a put** (both at strike K, same expiry), and the constant `K*e^(-r*T)` is just a financing term (cash you hold). The combination `long call + short put` behaves *exactly* like owning the underlying. This is the **synthetic long underlying**, the most important synthetic of all.

The intuition is clean if you walk through expiry:

- **Above the strike**, the call you own is in-the-money and gains point-for-point with the underlying — just like a stockholder. The put you sold expires worthless.
- **Below the strike**, your call is worthless, but the put you sold is exercised against you: someone makes you *buy* at K while the market is lower, so you lose point-for-point — again exactly like a stockholder who is underwater.

In every state, your gains and losses track the underlying one-to-one. You have manufactured a long position with no shares and no future — just two options. The payoff is the familiar straight 45-degree line of a long underlying position.

![Figure: synthetic long payoff](figs/synthetic_long.png)

### Synthetic short underlying = short call + long put

Flip every sign. Isolating `-S`:

`-S = P - C - K*e^(-r*T)`

So **sell a call, buy a put** (same strike, same expiry) and you have a **synthetic short underlying**. Above the strike, the short call loses point-for-point (like a short-seller squeezed by a rally); below the strike, the long put gains point-for-point. You profit when the underlying falls — exactly a short position, built without ever borrowing and selling shares. This is invaluable in India, where directly short-selling cash equities intraday is restricted and carrying a short overnight in the cash market is not allowed for retail — but a synthetic short via options is perfectly ordinary.

### Synthetic long call = long underlying + long put

Now isolate the call. From parity:

`C = S + P - K*e^(-r*T)`

The right side is **own the underlying and buy a put** — which you already know as a **protective put** (Chapter 49 territory). Put-call parity reveals the punchline: a protective put *is* a synthetic long call. It makes perfect sense. Holding the stock gives you the upside; the put floors your downside at K. Capped downside plus unlimited upside is precisely a call's profile. The "insurance" framing and the "leveraged upside" framing describe the same payoff.

### Synthetic long put = short underlying + long call

Finally, isolate the put:

`P = C - S + K*e^(-r*T)`

That is **buy a call and short the underlying**. Short exposure gives you downside profit; the long call caps your loss if the underlying rallies. Capped upside-risk plus open downside profit is a put. So shorting the future and buying a call manufactures a synthetic long put.

The full family is worth memorising. Each instrument equals the *other two* (plus the cash term):

- Synthetic **long underlying** = long call + short put
- Synthetic **short underlying** = short call + long put
- Synthetic **long call** = long underlying + long put
- Synthetic **long put** = short underlying + long call

A simple way to remember it: **a synthetic long call needs you long the underlying; a synthetic long put needs you short the underlying.** The option you add is always the "insurance" that caps the open end.

### A futures position equals long call minus short put

In India, the natural "underlying" leg is not the cash index — you cannot literally buy 50 stocks in index weights — it is the **Nifty future**. The future already bakes in financing and dividends, so parity is usually written with the futures price `F` in place of the carried spot:

`C - P = (F - K)*e^(-r*T)`

Rearranged, `F = K + (C - P)*e^(r*T)`. The economic content is simple and worth stating plainly: **a long futures position is equivalent to (long call − short put) at the same strike and expiry.** The call-minus-put spread *is* the future, give or take the small financing term. At the at-the-money strike, where `C` and `P` are close, the synthetic long and the future sit right on top of each other.

This is the bridge between the two halves of the F&O market: the futures desk and the options desk trade the same exposure in two packagings, and parity is the exchange rate between them. When a market-maker is handed an unwanted options position, they hedge it in *futures* — and the synthetics arithmetic tells them exactly how many.

### Conversions and reversals: the arbitrage that enforces parity

Synthetics are not just a pricing curiosity — they are policed by real money. Because a synthetic underlying and a real underlying have identical payoffs, they must cost the same. If they ever diverge, an arbitrageur buys the cheap one and sells the dear one and pockets the gap risk-free. These two enforcing trades have names:

- A **conversion** = buy the *real* underlying (long future) + sell the *synthetic* underlying (short call, long put). You are long the cheap real thing and short the expensive synthetic. Net, you are flat — the long future and the synthetic short cancel — so you have locked a fixed payoff with no directional risk.
- A **reversal** (reverse conversion) = short the *real* underlying (short future) + buy the *synthetic* underlying (long call, short put). The mirror image, run when the synthetic is the cheap leg.

Because the two legs cancel in every state of the world, the position's profit is *fixed at the moment you put it on* — the parity gap, locked. Desks run these all day for a few points of edge, and their relentless buying of the cheap leg and selling of the dear leg keeps the Nifty call, put, and future internally consistent. You will rarely find a gap big enough to trade by hand after costs — but the *existence* of these arbitrageurs is your guarantee that the synthetic relationships hold, which is what makes them safe to rely on.

### Why synthetics matter in practice

This is not abstract elegance. Professionals use synthetics every day for four concrete reasons.

1. **Margin and capital efficiency.** A long future and a synthetic long have identical payoffs, but the SPAN+exposure margin can differ, and the synthetic's short-put leg may sit inside an existing portfolio in a way that nets down margin. Desks routinely pick the *cheapest-to-carry* packaging of a given delta.

2. **Working around liquidity.** Want to short Nifty but the future is momentarily wide while the options are tight? Build the short synthetically from the liquid call and put. Or neutralise a call you can no longer trade out of by trading the *other* legs. Synthetics give you more than one road to the same destination, so you take whichever is open.

3. **Locking arbitrage.** When a parity gap *does* open — around events, at expiry, or in less-liquid far months — conversions and reversals harvest it. This is the bread and butter of arbitrage desks.

4. **Understanding structure.** The deepest payoff is conceptual. Once you see that *every* options structure is assembled from the same bricks, complex positions stop being intimidating. An iron condor is two credit spreads; a credit spread is parity rearranged; a collar is a synthetic; a risk reversal is a synthetic underlying shifted across strikes. You are never learning a "new" instrument — only a new arrangement of call, put, underlying, and cash.

### The box spread: a synthetic loan or deposit

Stack two synthetics at *different* strikes and you build the **box spread** — a position so neutral it is essentially a bond in disguise. A box combines:

- A **synthetic long underlying at strike K1** (long K1 call, short K1 put), and
- A **synthetic short underlying at strike K2** (short K2 call, long K2 put),

with `K2 > K1`. The long synthetic locks in *buying* the index at K1; the short synthetic locks in *selling* it at K2. Whatever the index does, you have effectively agreed to buy at K1 and sell at K2, so your payoff at expiry is a fixed `K2 - K1`, completely independent of where the underlying lands. (Equivalently, a box is a bull call spread plus a bear put spread on the same two strikes.)

Because the payoff is a known constant, a fairly priced box must cost the present value of that constant:

`Box cost = (K2 - K1)*e^(-r*T)`

So a box is a **synthetic zero-coupon bond**. If you *buy* the box (pay a bit less than `K2 - K1` today, receive exactly `K2 - K1` at expiry), you have made a **synthetic deposit** earning the risk-free rate. If you *sell* the box (receive cash today, repay `K2 - K1` at expiry), you have taken a **synthetic loan** at the risk-free rate — historically a way for institutions to borrow or lend through the options market. The box exists because, deep down, parity says cash itself is one of the four Lego bricks; assemble the other three cleverly and you have rebuilt cash. (Caution, expanded below: a box is only clean on *European, cash-settled* options. On American or physically-settled options, early assignment can shatter the "guaranteed" payoff.)

## Worked example (₹, Nifty)

Let us prove, with concrete numbers, that a synthetic long *is* a futures position — and then check the margin angle.

**Setup.** It is Monday. Nifty spot is **24,000**. The near-month **Nifty future trades at F = 24,060** (the small premium over spot reflects financing minus dividends). We look at the **24,000-strike** options expiring this Friday, so `T = 4/365 = 0.01096` years, and take `r = 6.5%`. The screen shows the **24,000 call (CE) at ₹150** and the **24,000 put (PE) at ₹92**. Assume a Nifty lot of **75** units.

**Step 1 — build the synthetic long.** Buy the 24,000 call (pay ₹150), sell the 24,000 put (receive ₹92). Net debit = `150 - 92 = ₹58` per unit. This `long call + short put` is your synthetic long underlying.

**Step 2 — check it against the future using parity.** Parity (futures form) says `C - P = (F - K)*e^(-r*T)`.
The right side: `(24,060 - 24,000)*e^(-0.065*0.01096) = 60 * 0.999288 ≈ 59.96 ≈ 60` points.
The market's `C - P = 150 - 92 = 58` points. These are within ₹2 — essentially in line (the tiny gap would be eaten by the bid-ask spread). So the synthetic and the future are priced consistently. Good.

**Step 3 — prove the payoffs match, state by state.** Compare two ways of being long: (A) **buy the future at 24,060**, versus (B) **the synthetic** (long 24,000 call, short 24,000 put). Compute each at expiry for three closing levels. For the synthetic, also account that you paid ₹58 to put it on; for the future, your reference entry is 24,060.

| Nifty at expiry | Future P&L (close − 24,060) | Long 24,000 call payoff | Short 24,000 put payoff | Synthetic gross | Synthetic net (− ₹58) |
|---|---|---|---|---|---|
| 23,600 | −460 | 0 | −400 | −400 | −458 |
| 24,000 | −60 | 0 | 0 | 0 | −58 |
| 24,500 | +440 | +500 | 0 | +500 | +442 |

Look at the two outer columns: the **future P&L** and the **synthetic net** track each other almost exactly — they differ by a constant ~₹2 (the small financing/pricing gap from Step 2), not by direction. At every level, a 1-point move in Nifty changes both by 1 point. The synthetic *is* the future. The straight-line, one-to-one payoff is exactly the long underlying line in the figure above.

**Step 4 — the practical "so what" (margin).** Both packagings give you +75 deltas (one lot of long Nifty). Why choose one over the other? Margin and fit. Buying the future costs roughly ₹1.4-1.8 lakh of SPAN+exposure margin per lot. The synthetic's short-put leg also carries margin, but if you already hold offsetting positions, the exchange's portfolio margining can net it down — sometimes making the synthetic cheaper to carry. A desk computes both and takes the cheaper. The *exposure* is identical; only the capital efficiency differs. That, in one sentence, is why synthetics are a daily tool and not a textbook curiosity.

**Step 5 — read a tiny arbitrage.** Suppose instead the call printed **₹175** with the put still at ₹92, so `C - P = 83` while parity says ~60. The synthetic long is now 23 points *too expensive* relative to the future. A desk runs a **conversion**: sell the synthetic (sell the 175 call, buy the 92 put) and buy the future at 24,060. The legs cancel at expiry, leaving the locked gap of about `83 - 60 = 23` points, or `23 * 75 ≈ ₹1,725` per lot, risk-free before costs. In reality a 23-point gap at the ATM would vanish in seconds — which is *why* you almost never see it.

## Common mistakes / risk note

- **Forgetting the financing term.** A synthetic long is `long call + short put` *plus* the cash term `K*e^(-r*T)`. It does not cost zero just because the premiums partly offset; you are effectively financing a full index position. The synthetic carries the same notional risk as the future — a 5% move against you hurts exactly as much. The capped-loss comfort of a *long option* is gone the moment you sell the other leg.

- **Treating a synthetic short put as "free income."** A synthetic long underlying contains a *short put*. People who build synthetics for margin reasons sometimes forget they now carry naked-put-style downside on that leg. If Nifty gaps down, the short put bleeds exactly like the underlying falling — undefined-feeling, large losses. Respect the short leg.

- **Mixing strikes or expiries by accident.** Parity and every synthetic require the **same strike and same expiry** on both option legs. A long 24,000 call and a short 24,100 put is *not* a clean synthetic long — it is a synthetic with a directional skew (a risk reversal). Useful, but a different animal; do not confuse the two.

- **Assuming a box spread is risk-free everywhere.** On **European, cash-settled** index options (Nifty, Bank Nifty) a box is a clean synthetic bond. On **American, physically-settled single-stock** options, a short leg can be assigned early, the "guaranteed" `K2 - K1` breaks, and you can be dragged into stock delivery with margin spikes. Traders have taken large, sudden losses assuming a box was riskless when it was not. Keep boxes to index options.

- **Thinking synthetics are a retail money machine.** Real conversion/reversal gaps are tiny, fleeting, and eaten by brokerage, STT, exchange fees, and the bid-ask spread on *four* legs. They are harvested by automated desks with low costs, not by clicking legs by hand. For a retail trader the value of synthetics is *structural understanding and capital efficiency*, not free arbitrage. And the broader truth from Chapter 1 still stands: SEBI studies find roughly 9 in 10 retail F&O traders lose money. No clever construction changes the odds on a bad directional view.

## Key takeaways

- Put-call parity, `C + K*e^(-r*T) = P + S`, rearranges to build any one instrument from the other three — that is what a **synthetic** is.
- **Synthetic long underlying = long call + short put** (same strike/expiry); **synthetic short = short call + long put**. Same payoff as holding/shorting the underlying.
- **Synthetic long call = underlying + long put** (a protective put); **synthetic long put = short underlying + long call**.
- A **long futures position equals (long call − short put)** at the same strike: `F = K + (C - P)*e^(r*T)`. The options and futures markets price the same exposure.
- **Conversions** (long real + short synthetic) and **reversals** (short real + long synthetic) are the arbitrages that lock the parity gap and keep all the prices consistent.
- Professionals use synthetics for **margin/capital efficiency, liquidity workarounds, locking arbitrage, and structural clarity** — every options structure is the same few Lego bricks rearranged.
- A **box spread** (synthetic long at K1 + synthetic short at K2) pays a fixed `K2 - K1` and is a **synthetic loan/deposit** costing `(K2 - K1)*e^(-r*T)` — clean only on European, cash-settled options.

## Practice problems

1. **(Conceptual)** Your friend says, "A protective put is a defensive, low-risk strategy, but a long call is an aggressive, leveraged bet — they are totally different." Using parity, explain why their payoffs are actually the same thing, and name which synthetic this is.

2. **(Conceptual)** You want short exposure to Nifty into a feared event but cannot carry a short in the cash market. Describe two different option-only ways to get a synthetic short, and state the strike/expiry condition both legs must satisfy.

3. **(Numeric)** Nifty spot is 24,000, the near future is at 24,050, `r = 6.5%`, `T = 7/365`. The 24,000 call trades at ₹165 and the 24,000 put at ₹120. Does the synthetic long (long call + short put) line up with the future? Compute `C - P`, compare with `(F - K)*e^(-r*T)`, and say whether there is an arbitrage worth noting.

4. **(Numeric)** Using the data in Problem 3's *quoted* prices (call ₹165, put ₹120, net debit ₹45), compute the synthetic long's net P&L per unit at Nifty closing levels of 23,700, 24,000, and 24,400. Confirm the slope is one-to-one with the underlying.

5. **(Numeric)** Build a box spread on Bank Nifty using the 52,000 and 52,300 strikes, `r = 6.5%`, `T = 7/365`. What fixed amount does it pay at expiry, and roughly what should it cost today? If you *sell* this box, what have you economically done?

6. **(Conceptual)** A desk holds a long Nifty 24,000 call it can no longer sell at a good price because that specific option has gone illiquid, but the 24,000 put and the future are both liquid. How can the desk neutralise the call's directional risk using the liquid instruments, and what synthetic relationship are they exploiting?

## Solutions

**1.** Parity rearranged gives `C = S + P - K*e^(-r*T)`. The right side — own the underlying and buy a put — *is* the protective put. So a protective put and a long call have identical payoffs: capped downside (floored by the put / by the call costing nothing more), unlimited upside. The "defensive insurance" story and the "leveraged upside" story describe the *same* line on the payoff chart. This is the **synthetic long call**. The only real differences are framing, the cash outlay, and possibly margin — not the exposure.

**2.** A **synthetic short underlying = short call + long put** at the **same strike and same expiry** — sell the 24,000 call and buy the 24,000 put, and you profit as Nifty falls with capped upside-risk. A second route: short the **future** and the position is already short, but if futures are awkward you can also achieve short exposure by simply running the short-call/long-put synthetic on whichever strike is most liquid. In both cases the two option legs must share the **same strike and the same expiry**, or the structure becomes a skewed risk reversal rather than a clean synthetic short.

**3.** `C - P = 165 - 120 = 45` points. Parity target: `(F - K)*e^(-r*T) = (24,050 - 24,000)*e^(-0.065*7/365)`. Exponent `= -0.065 * 0.01918 = -0.001247`, so `e^(...) ≈ 0.998754`, giving `50 * 0.998754 ≈ 49.94 ≈ 50` points. The synthetic shows 45 versus a fair 50 — the synthetic long is about **5 points cheap** relative to the future. In principle a **reversal** (short the future at 24,050, buy the synthetic: long call, short put) locks ~5 points = `5 * 75 ≈ ₹375` per lot. In practice 5 points at the ATM is within the bid-ask plus STT/brokerage on three legs, so it is **not** a tradeable arbitrage by hand — just a confirmation that the prices are essentially consistent.

**4.** Net debit ₹45 (paid). Synthetic gross payoff = call payoff + short-put payoff:
- **23,700:** call `0`, short put `-(24,000-23,700) = -300`, gross `-300`, net `-300 - 45 = -345`.
- **24,000:** call `0`, short put `0`, gross `0`, net `-45`.
- **24,400:** call `+400`, short put `0`, gross `+400`, net `+400 - 45 = +355`.
From 23,700 to 24,000 (a +300 move) net P&L goes from −345 to −45, a change of +300. From 24,000 to 24,400 (a +400 move) it goes −45 to +355, a change of +400. The P&L changes **one-for-one** with Nifty — exactly the slope of a long underlying/future position. The synthetic is a long underlying.

**5.** Box on K1 = 52,000 and K2 = 52,300: synthetic long at 52,000 (long 52,000 call, short 52,000 put) plus synthetic short at 52,300 (short 52,300 call, long 52,300 put). You have locked buying at 52,000 and selling at 52,300, so the box pays a fixed `K2 - K1 = 300` points at expiry, whatever Bank Nifty does. Fair cost = `300 * e^(-0.065*7/365) = 300 * 0.998754 ≈ 299.63` points. So you would pay about **299.6 today to receive exactly 300 at expiry** — a synthetic deposit earning the risk-free rate. If instead you **sell** the box, you receive ~299.6 today and must repay 300 at expiry: you have taken a **synthetic loan** at roughly the risk-free rate through the options market. (Valid because Bank Nifty options are European and cash-settled; never assume this on American, physically-settled stock options.)

**6.** A long call is, by parity, a synthetic long underlying *capped on the downside by a put*: `C = S + P - K*e^(-r*T)`, so `long call` behaves like `long underlying + long put`. To neutralise its directional (delta) risk, the desk offsets the "long underlying" component by **shorting the future**, and offsets the embedded long-put exposure by **selling the 24,000 put**. Concretely, `short future + short put` is a **synthetic short call**, which cancels the long call. The desk is exploiting the synthetic-call relationship — that a call can be replicated (and therefore hedged) by the underlying and the matching put — to flatten an illiquid position using only liquid instruments.
