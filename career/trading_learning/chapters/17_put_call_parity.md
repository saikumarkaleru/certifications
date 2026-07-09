# Chapter 17: Put-Call Parity — The Most Important No-Arbitrage Rule

Here is a claim that sounds too neat to be true: if you know the price of a Nifty call, the price of the spot index, and the interest rate, then the price of the matching put is *already decided*. You do not need a fancy model, you do not need to guess volatility, you do not even need to know which way the market is heading. The put's price is locked in by pure arithmetic. Get it wrong and someone will take your money for free.

That iron link between a call, a put, the spot, and the strike is called **put-call parity**. It is the single most important no-arbitrage relationship in all of options trading. Almost everything that comes later — synthetic positions, the box spread, conversion-reversal arbitrage, even the structure of the Black-Scholes formula — grows out of this one equation. This chapter builds it from intuition, shows you exactly how a violation hands out free money (and therefore why it almost never lasts), and uses it to construct *synthetic* positions: ways of building a call out of a put, or a long stock position out of two options.

## Core concepts

### Two portfolios that must end up in the same place

Forget formulas for a moment. Imagine two investors at the start of the week, both looking at Nifty trading around 24,000, and both wanting protection or upside tied to the 24,000 level for this Friday's expiry.

**Investor A — the "protective put."** She buys one unit of the Nifty index itself, and also buys one 24,000-strike **put** (the right to sell at 24,000). Whatever happens, she owns the index, but the put guarantees she can never effectively sell below 24,000. Her downside is floored.

**Investor B — the "fiduciary call."** He buys one 24,000-strike **call** (the right to buy at 24,000), and separately sets aside enough cash today so that it grows to exactly 24,000 by Friday. He keeps the cash safe in a risk-free deposit and holds the call.

Now ask: what is each portfolio worth at expiry on Friday, for any possible level of Nifty?

- **If Nifty finishes above 24,000** (say 24,500): Investor A holds the index worth 24,500; her put expires worthless. Total = **24,500**. Investor B uses his 24,000 cash to exercise the call and buy the index at 24,000, now worth 24,500. Total = **24,500**.
- **If Nifty finishes below 24,000** (say 23,600): Investor A holds the index worth 23,600 but exercises her put to sell at 24,000. Total = **24,000**. Investor B lets the call expire worthless and simply keeps his cash, which has grown to 24,000. Total = **24,000**.
- **If Nifty finishes exactly at 24,000:** both portfolios are worth **24,000**.

In *every single state of the world*, the two portfolios are worth exactly the same. This is not a coincidence — both are really the same thing: "I get the upside above 24,000, and I am protected at 24,000 on the downside." One bundles that promise as stock-plus-put, the other as call-plus-cash.

Here is the punchline. **If two portfolios are guaranteed to be worth the same at expiry, they must cost the same today.** If they did not, you could buy the cheap one, sell the expensive one, pocket the difference immediately, and never owe anything later because the two sides cancel perfectly at expiry. That "free money" is exactly what arbitrage hunts, and its absence is what forces the prices into line.

### Writing it as a formula

Let us name the pieces:

- `S` = current spot price of the underlying (Nifty index level).
- `K` = strike price (24,000 in the story).
- `C` = price of the European call at strike K.
- `P` = price of the European put at strike K (same strike, same expiry).
- `r` = the risk-free interest rate (annualised, as a decimal).
- `T` = time to expiry in years.
- `e^(-r*T)` = the discount factor that tells you how much cash you must set aside *today* to have 1 rupee at expiry. So to have K rupees at expiry you set aside `K * e^(-r*T)` today.

Investor B's "fiduciary call" costs `C + K*e^(-r*T)` (the call plus the present value of the cash). Investor A's "protective put" costs `S + P` (the index plus the put). Setting them equal:

`C + K*e^(-r*T) = P + S`

That is **put-call parity**. It is most often rearranged so the two options sit on one side:

`C - P = S - K*e^(-r*T)`

Read it in plain English: *the call minus the put equals the spot minus the present value of the strike.* The left side is pure option pricing; the right side is just the cash market and an interest-rate calculation. The equation chains them together.

A note on `K*e^(-r*T)`: this is **continuous compounding**, the convention used in Black-Scholes. For a weekly Nifty option `T` is tiny (about 7/365 of a year), so the discount factor is very close to 1; the exact convention matters more for longer-dated options.

### The dividend version

The story above quietly assumed the index pays you nothing while you hold it. Real stocks and indices pay **dividends**, and a dividend is cash that flows to the *stockholder*, not to the option holder. Investor A, who owns the actual index, collects those dividends; Investor B, who only holds a call, does not. So owning the stock is worth a little *more* than the bare spot price suggests, and we must discount the spot by the dividends it will throw off before expiry.

The clean way to handle this is a **continuous dividend yield** `q` (the annualised rate at which the index pays out). The spot in the formula gets replaced by `S*e^(-q*T)`:

`C - P = S*e^(-q*T) - K*e^(-r*T)`

Equivalently, `C + K*e^(-r*T) = P + S*e^(-q*T)`. The intuition is unchanged: we are just acknowledging that the stockholder's leg of the trade is sweetened by dividends, so its effective starting value is lower by the present value of those dividends. For a broad index like Nifty the dividend yield is modest (very roughly 1-1.5% a year), and over a single week `e^(-q*T)` is almost exactly 1, so for weekly index trades the dividend term is a rounding error. It becomes significant for monthly or longer options, and especially around heavy dividend seasons.

### Why a violation is free money

Parity is not a suggestion; it is enforced by self-interest. Suppose the equation is *out of balance*. Concretely, imagine:

`C - P  >  S - K*e^(-r*T)`

The left side (the option spread) is too expensive relative to the right side (the cash side). An arbitrageur does the obvious thing: **sell the expensive side, buy the cheap side.**

- Sell the call (receive C), buy the put (pay P) → net cash in = `C - P`.
- Short the index (receive S), and lend `K*e^(-r*T)` today at the risk-free rate so it grows to exactly K at expiry.

At the moment of setting this up, the trader collects `(C - P)` from the options and `S` from the short, and spends `K*e^(-r*T)` on the loan. Because `C - P > S - K*e^(-r*T)`, this leaves a **positive amount of cash in the trader's pocket today**. Now check expiry, for any Nifty level:

- The short call and long put together act exactly like an obligation to deliver the index at K (this is a synthetic short index, as we will see). At expiry the trader buys the index back at K using the matured loan proceeds (which are exactly K), and returns it to close the short.
- Everything nets to zero at expiry. No leftover obligation, no risk.

So the trader walked away with cash up front and owes nothing later — a **risk-free arbitrage profit**. The reverse imbalance (`C - P < S - K*e^(-r*T)`) is harvested by doing the mirror trade: buy the call, sell the put, short nothing — instead buy the index and borrow `K*e^(-r*T)`. Either way, the moment a gap opens, arbitrage desks pile in, *buying the cheap leg and selling the dear leg*, which pushes the prices back until the gap closes. That collective pressure is **why parity holds** in liquid markets: not because traders are nice, but because any deviation is a money pump that gets drained in seconds.

These two enforcing trades have names you will meet again: buying stock + selling synthetic stock (short call, long put) is a **conversion**; the mirror is a **reversal**. Desks run these to lock small, near-riskless spreads, and their activity keeps the Nifty option chain internally consistent.

### Building synthetic positions from parity

Now for the most *useful* payoff of parity. Because the four instruments (call, put, spot, cash) are tied by one equation, you can always isolate any one of them on the left side and express it using the other three. That gives you **synthetic positions** — a way to manufacture one instrument out of the others. Rearranging `C + K*e^(-r*T) = P + S`:

- **Synthetic long stock** = long call + short put (same strike, same expiry):
  `S = C - P + K*e^(-r*T)`.  Owning a call and having sold a put behaves just like owning the index (plus a financing term). Above the strike the call gives you the upside; below the strike the short put forces you to "buy" at the strike — exactly what a stockholder experiences.
- **Synthetic long call** = long stock + long put (a protective put *is* a call): `C = S + P - K*e^(-r*T)`.
- **Synthetic long put** = short stock + long call: `P = C - S + K*e^(-r*T)`.
- **Synthetic short stock** = short call + long put: `-S = P - C - K*e^(-r*T)`.

Each synthetic has the same payoff as the real thing, so traders pick whichever is *cheaper to execute or margin-efficient* at the moment. In Indian markets, where you can trade Nifty futures as the "stock" leg, synthetics built from futures + options are a daily reality for market-makers.

### A first look at the box spread

Stack two synthetics and you get the **box spread** — a position so neutral it is essentially a bond in disguise. A box combines:

- A **synthetic long stock at strike K1** (long K1 call, short K1 put), and
- A **synthetic short stock at strike K2** (short K2 call, long K2 put),

with `K2 > K1`. The long-synthetic locks in buying the index at K1; the short-synthetic locks in selling it at K2. Whatever Nifty does, you have effectively agreed to buy at K1 and sell at K2, so your guaranteed payoff at expiry is exactly `K2 - K1` — a fixed number, completely independent of where Nifty lands. (Equivalently, a box is a **bull call spread plus a bear put spread** at the same two strikes.)

Because the payoff is a known constant, a fairly priced box must cost the present value of that constant today:

`Box cost = (K2 - K1) * e^(-r*T)`

In other words, a box spread is a synthetic zero-coupon bond: you pay a bit less than `K2 - K1` now and collect exactly `K2 - K1` at expiry, earning the risk-free rate in between. If the market ever prices the box away from this, that is a parity violation and an arbitrage. (A caution, expanded in the risk note: a "box" on *American* or physically-settled options carries early-exercise and settlement risk and is **not** the risk-free instrument it appears.)

### Why parity holds cleanly for Indian index options

Put-call parity in the clean form `C - P = S - K*e^(-r*T)` was *derived assuming European exercise* — the arbitrage relies on both options settling only at expiry, so the two portfolios can be compared state-by-state on that one date. This is exactly why the relationship is so tight for **Nifty and Bank Nifty options**:

- They are **European** — exercisable only at expiry — so there is no early-exercise wildcard to break the portfolio equivalence.
- They are **cash-settled** against a well-defined expiry settlement value, so the "deliver the index at K" leg is purely a cash calculation; nobody has to source or deliver a basket of 50 stocks.
- The underlying (the index, or its near-month future) is liquid, so the arbitrage trades are cheap to put on.

Put together, Indian index options obey parity about as cleanly as any market on earth. In practice traders use the **near-month Nifty future** as the spot leg, since the future already bakes in financing and dividends; parity then reads `C - P = (F - K)*e^(-r*T)`, with F the futures price. That futures-based form is what desks actually watch on screen.

### The small wrinkles: dividends and stock options

Two real-world frictions bend (but never break) the clean rule:

1. **Dividends.** Dividends accrue to the stockholder, not the option holder, so the spot must be discounted by expected dividends (`S*e^(-q*T)`, or by subtracting the present value of discrete dividends). Ignore this on a longer-dated option and your "parity check" will look violated when it is merely mis-specified. The effect is negligible for weeklies but matters for monthly and quarterly options.

2. **American, physically-settled stock options.** NSE **single-stock** options are American-style (exercisable any day) and **physically settled**. American exercise means the neat equality becomes a pair of *inequalities* (a no-arbitrage band), because a deep-ITM put or a call on a dividend-paying stock might rationally be exercised early — which the European argument forbids. Physical settlement adds delivery and STT considerations. So for stock options, treat parity as an *approximate* relationship with a band of slack; for the **index** options that dominate Indian F&O volume, the sharp European equality applies.

## Worked example (₹, Nifty/Bank Nifty)

Let us check parity with concrete, realistic numbers and then hunt an arbitrage.

**Setup.** It is Monday. Nifty **spot S = 24,000**. We look at the **24,000-strike** options expiring this Friday, so time to expiry is 4 calendar days, `T = 4/365 = 0.01096` years. Take the risk-free rate `r = 6.5%` per year (`r = 0.065`), and ignore dividends for the week (`q ≈ 0`, justified because `e^(-q*T) ≈ 1` over four days).

**Step 1 — present value of the strike.**
`K*e^(-r*T) = 24,000 * e^(-0.065 * 0.01096)`.
The exponent is `-0.065 * 0.01096 = -0.000712`, and `e^(-0.000712) ≈ 0.999288`.
So `K*e^(-r*T) ≈ 24,000 * 0.999288 = 23,982.9`.

**Step 2 — what parity predicts for the call-minus-put gap.**
`C - P = S - K*e^(-r*T) = 24,000 - 23,982.9 = 17.1` points.

So parity says the **call must trade about 17 points richer than the put** at the at-the-money 24,000 strike. (This makes sense: the call buyer defers paying the 24,000 strike until Friday and earns interest on that cash in the meantime, so the call is worth slightly more than the put.)

**Step 3 — check it against quoted prices.**
Suppose the screen shows the 24,000 CE (call) at **₹172** and the 24,000 PE (put) at **₹155**.
`C - P = 172 - 155 = 17` points. Parity predicts 17.1. The market is **in line** — no arbitrage. Good.

**Step 4 — now introduce a mispricing and harvest it.**
Suppose instead the call is quoted at **₹185** while the put stays at **₹155**.
`C - P = 185 - 155 = 30`, but parity says it should be `17.1`. The call side is **too expensive by about 13 points**. Arbitrage: sell the rich side, buy the cheap side.

- **Sell** the 24,000 call → receive ₹185.
- **Buy** the 24,000 put → pay ₹155.
- **Buy** the index (go long Nifty via the future/basket) at 24,000.
- **Borrow** the present value of the strike, `23,982.9`, to be repaid as 24,000 at expiry.

Net cash today: `+185 - 155 - 24,000 + 23,982.9 = +12.9` points received up front, with nothing owed later. Let us confirm the "nothing owed later" by checking expiry in two states:

- **Nifty finishes at 24,500:** the short call is settled against us — we effectively deliver the index at 24,000 (we own it, bought at 24,000), netting receipt of 24,000; the put expires worthless; we repay the loan of 24,000. Net = `+24,000 - 24,000 = 0`.
- **Nifty finishes at 23,600:** the short call expires worthless; we exercise our long put to sell at 24,000; we repay the loan of 24,000. Net = `+24,000 - 24,000 = 0`.

Either way the expiry cash flows cancel to zero, and we keep the **12.9 points** collected on Monday. On one Nifty lot of about 75 units, that is `12.9 * 75 ≈ ₹967.50` of essentially risk-free profit (before brokerage, STT, and the bid-ask spread — which in reality would shrink or erase a gap this small almost instantly). That last parenthesis is the whole reason such gaps barely exist: the moment the call printed ₹185, desks would sell it and buy the synthetic, dragging it back toward ₹172.

**Step 5 — read it as synthetics.** Notice what we built. Long put + short call at the same strike *is* a synthetic short index. We paired it with a real long index and a loan, i.e. we ran a **conversion**. Parity is not abstract here: it is the exact accounting that tells the desk how many points of edge the conversion locks in.

## Common mistakes / risk note

- **Forgetting to discount the strike.** Beginners write `C - P = S - K` and conclude the ATM call and put should be equal. They are *not* equal: the call is richer by the interest on the strike, `S - K*e^(-r*T)`. The gap is small for a weekly but real, and it grows with tenor and rates.
- **Ignoring dividends on longer-dated or stock options.** Leave out `e^(-q*T)` (or the PV of discrete dividends) on a monthly option and parity will look "violated" when your inputs are simply wrong. Always discount the spot for dividends before crying arbitrage.
- **Applying the sharp equality to American, physically-settled stock options.** NSE single-stock options are American and deliverable; early exercise turns the equation into an inequality band, and physical settlement adds delivery/STT risk. The crisp identity is for **European, cash-settled index options** (Nifty, Bank Nifty).
- **Assuming a box spread is truly risk-free in all settings.** On European cash-settled options a box is a clean synthetic bond. On American or physically-settled options, early assignment on a short leg can blow up the "guaranteed" payoff and saddle you with a stock delivery — traders have suffered large, sudden losses assuming a box was riskless when it was not.
- **Mistaking parity for a profit machine for retail traders.** Real parity gaps are tiny, fleeting, and eaten by transaction costs (brokerage, STT, exchange fees, and the bid-ask spread). They are harvested by automated desks with low costs and fast execution, not by clicking two legs by hand. The honest lesson of parity for a retail trader is *conceptual*: it lets you price puts from calls, build synthetics, and understand structure — not mine free money. And the broader truth still stands: SEBI studies find roughly 9 in 10 retail F&O traders lose money, and no equation changes that.

## Key takeaways

- Put-call parity for European options: `C - P = S - K*e^(-r*T)`; with dividends, replace `S` by `S*e^(-q*T)`.
- It comes from two portfolios — a protective put (`S + P`) and a fiduciary call (`C + K*e^(-r*T)`) — that have identical payoffs at expiry and therefore must cost the same today.
- Any violation is a risk-free arbitrage: sell the expensive leg, buy the cheap leg (a conversion or reversal). Arbitrageurs enforcing this are *why* parity holds.
- Parity lets you build synthetics: synthetic long stock = long call + short put; synthetic call = stock + put; synthetic put = short stock + long call.
- A box spread (synthetic long stock at K1 + synthetic short stock at K2) pays a fixed `K2 - K1` and must cost `(K2 - K1)*e^(-r*T)` — a synthetic bond.
- Parity holds cleanly for Nifty and Bank Nifty options (European, cash-settled). Dividends and American/physically-settled stock options introduce small wrinkles and turn the equality into a band.

## Practice problems

1. **(Conceptual)** Explain in one or two sentences why, at the at-the-money strike where `S = K`, the call must trade slightly *more expensively* than the put. Which term in the parity equation creates that gap?

2. **(Numeric)** Bank Nifty spot is 52,000. For the 52,000-strike monthly options with `T = 30/365` years and `r = 6.5%`, ignoring dividends, what does parity predict for `C - P`? If the put trades at ₹720, what should the call trade at?

3. **(Numeric)** Nifty spot is 24,000. The weekly 24,000 call trades at ₹210 and the 24,000 put at ₹150, with `K*e^(-r*T) = 23,985`. Is parity satisfied? If not, which leg is rich, and sketch the arbitrage trade.

4. **(Conceptual)** You want long exposure to Nifty but your broker's margin on a synthetic (long call + short put) is cheaper today than buying the future. Using parity, explain why the synthetic gives the same payoff as a long index/future position.

5. **(Numeric)** Construct a box spread on Nifty using the 24,000 and 24,200 strikes. What fixed amount does it pay at expiry, and roughly what should it cost today if `r = 6.5%` and `T = 7/365`?

6. **(Conceptual)** A trader checks parity on an NSE single-stock option (American, physically settled) and finds `C - P` sits a few points away from `S - K*e^(-r*T)`. Why is this not necessarily an arbitrage?

## Solutions

**1.** Parity gives `C - P = S - K*e^(-r*T)`. At `S = K`, this is `K - K*e^(-r*T) = K*(1 - e^(-r*T))`, a small positive number because `e^(-r*T) < 1`. Economically, the call buyer defers paying the strike until expiry and earns risk-free interest on that cash in the meantime, so the call is worth that interest more than the put. The discounting term `K*e^(-r*T)` creates the gap.

**2.** `T = 30/365 = 0.08219`. Exponent `= -0.065 * 0.08219 = -0.005342`, so `e^(-0.005342) ≈ 0.994672`. Then `K*e^(-r*T) = 52,000 * 0.994672 ≈ 51,722.9`. Parity: `C - P = S - K*e^(-r*T) = 52,000 - 51,722.9 = 277.1` points. With the put at ₹720, the call should be `C = P + 277.1 = 720 + 277.1 ≈ ₹997`.

**3.** Parity predicts `C - P = S - K*e^(-r*T) = 24,000 - 23,985 = 15` points. The quotes give `C - P = 210 - 150 = 60` points — far above 15, so parity is **violated** and the **call is rich** (by about 45 points). Arbitrage (a conversion): sell the 24,000 call (+210), buy the 24,000 put (-150), buy the index at 24,000, and borrow `23,985` to repay as 24,000 at expiry. Net cash in today = `210 - 150 - 24,000 + 23,985 = +45` points. At expiry the long-put/short-call pair plus the long index plus the loan all cancel to zero regardless of where Nifty settles, leaving the 45 points (≈ `45 * 75 = ₹3,375` per lot) as risk-free profit, before costs. (In reality a 45-point gap at the ATM would never persist — it would be arbitraged away instantly.)

**4.** Rearranging parity, `S = C - P + K*e^(-r*T)`. So long call + short put (same strike, same expiry) replicates owning the index up to the fixed financing term `K*e^(-r*T)`. Above the strike, the long call delivers the upside point-for-point; below the strike, the short put obliges you to buy at the strike — exactly the gain/loss profile of holding the index. Since the payoff at every expiry level matches the index (offset by a known constant), the synthetic *is* a long index position, just assembled from two options. Picking it over the future when its margin is cheaper is a pure execution choice, not a change in exposure.

**5.** A box on strikes K1 = 24,000 and K2 = 24,200: go synthetic long at 24,000 (long 24,000 call, short 24,000 put) and synthetic short at 24,200 (short 24,200 call, long 24,200 put). You have locked in buying Nifty at 24,000 and selling at 24,200, so the box pays a fixed `K2 - K1 = 200` points at expiry no matter where Nifty lands. Its fair cost today is the present value: `200 * e^(-0.065 * 7/365)`. Exponent `= -0.065 * 0.01918 = -0.001247`, `e^(-0.001247) ≈ 0.998754`, so cost `≈ 200 * 0.998754 = 199.75` points. You pay about 199.75 today to receive exactly 200 at expiry — earning the risk-free rate, like a tiny zero-coupon bond.

**6.** Because NSE single-stock options are **American** (exercisable any day) and **physically settled**, the clean European derivation does not hold exactly. Early exercise — for instance, exercising a put early, or a call to capture a dividend — means the two replicating portfolios can diverge before expiry, so parity becomes a no-arbitrage *band* (a pair of inequalities) rather than a sharp equality. A few points of deviation can sit comfortably inside that band, especially once dividends, the cost of borrowing the stock to short, and physical-delivery/STT frictions are included. It is only a true arbitrage if the gap exceeds those costs and the band's width — which for a liquid European index option it almost never does, but for an American stock option it often does not.
