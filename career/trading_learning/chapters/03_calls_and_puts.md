# Chapter 3: Calls & Puts from Zero — Rights, Obligations, Buyers & Sellers

Imagine you spot a flat in a new Pune project priced at ₹80 lakh. You think prices will rise, but you are not ready to buy today. So you pay the builder a small "token" of ₹2 lakh that locks your right to buy that flat at ₹80 lakh any time in the next six months. If prices jump to ₹95 lakh, you exercise your token, buy at ₹80 lakh, and you are sitting on a ₹15 lakh gain (minus the ₹2 lakh token). If prices crash to ₹65 lakh, you simply walk away and lose only the ₹2 lakh. That token is, in essence, a **call option**. The whole of options trading is built from this one idea — paying a small, known amount today to control a much larger position, while capping your downside at what you paid.

A **put option** is the mirror image: it is a token that locks your right to *sell* something at a fixed price, no matter how far the market falls. Think of it as an insurance policy on your portfolio. This chapter defines calls and puts precisely, introduces the four people who sit on the two sides of every options trade, and pins down exactly who has a *right* and who has an *obligation*. Get this chapter right and everything later — Greeks, spreads, volatility — becomes just bookkeeping on top of these foundations.

## Core concepts

### What an option actually is

An **option** is a contract between two parties. One party (the **buyer**, also called the **holder** or the **long**) pays money up front for a *right*. The other party (the **seller**, also called the **writer** or the **short**) receives that money and takes on an *obligation*. The money the buyer pays the seller is the **premium**.

The crucial asymmetry to burn into your memory: **the buyer has rights, the seller has obligations**. The buyer can choose to use the contract or let it lapse. The seller has no choice — if the buyer exercises, the seller must perform. The seller is paid the premium precisely for accepting that lack of choice.

Every option is defined by a handful of terms. Let us define each one cleanly, because they appear in every options quote you will ever read.

- **Underlying:** the asset the option is "on." For us this is usually the **Nifty 50** index (around 24,000) or the **Bank Nifty** index (around 52,000). It can also be a stock like Reliance or HDFC Bank.
- **Strike price (K):** the fixed price written into the contract — the price at which the buyer may buy (call) or sell (put). On NSE you will see strikes like 24000, 24100, 24200, spaced 50 or 100 points apart.
- **Premium:** the price of the option itself, quoted *per unit of the underlying*. If the 24000 call is quoted at ₹250, that ₹250 is the premium for one unit of Nifty.
- **Expiry:** the date the contract dies. After expiry the option no longer exists. Nifty has **weekly** and **monthly** expiries; Bank Nifty currently trades monthly expiries. (Exact expiry days have changed over the years under SEBI/NSE rules, so always check the current calendar.)
- **Lot size:** options trade in fixed bundles called **lots**, never single units. Nifty's lot is currently **75 units**; Bank Nifty's is currently **30 (sometimes 15)**. Lot sizes are revised periodically by NSE, so treat these as "current" numbers. You cannot buy "one Nifty" — you buy one lot.

Putting it together, a real quote reads like **"NIFTY 31 JUL 24000 CE @ ₹250."** That is: underlying Nifty, expiry 31 July, strike 24000, **CE = Call European**, premium ₹250 per unit. A put would read **PE = Put European**. The word "European" matters: Indian *index* options can only be exercised **at expiry**, not before, and they are **cash-settled** (no actual shares change hands — you just receive or pay the rupee difference). Indian *stock* options are American-style and physically settled. This chapter's examples use index options.

### The call option: a token to BUY at a fixed price

A **call option** gives its buyer the **right, but not the obligation, to buy** the underlying at the strike price, on or before expiry.

You buy a call when you are **bullish** — you think the underlying will rise. Pay the premium today; if the underlying climbs well above the strike, your right to buy cheap becomes valuable. Going back to the flat: the call buyer holds a token to buy at a locked-in price and will only use it if the market price ends up *higher* than that locked price.

The defining feature is the asymmetry of outcomes. If you are right and the market soars, your gain grows point-for-point with the underlying above the strike — there is no upper limit. If you are wrong and the market falls, you simply do not exercise; you abandon the worthless token and lose only the premium. **Limited, known loss; large, open-ended gain.** That is what you are buying.

### The put option: a token to SELL at a fixed price (insurance)

A **put option** gives its buyer the **right, but not the obligation, to sell** the underlying at the strike price, on or before expiry.

You buy a put when you are **bearish** — you think the underlying will fall — or when you want **insurance** on something you already own. The insurance framing is the most useful intuition: just as a motor insurance policy pays you when your car is damaged, a put pays you when the market drops below the strike. You pay a premium (like an insurance premium) for the comfort of a guaranteed selling price. If the market never falls below the strike, your "policy" expires unused and you lose only the premium — exactly like an insurance policy you were lucky enough not to need.

A put buyer's gain rises as the market falls below the strike, down to the point where the underlying hits zero. The loss, again, is capped at the premium paid.

### The two sides of every trade

Here is a fact that trips up beginners: **for every option that is bought, someone has sold it.** Options are not created by a company like shares are; they are *written* by another trader who takes the opposite side. So every call and every put has two participants, giving us **four basic positions** in total. Master these four and you have mastered the grammar of options.

#### 1. Long Call (you BUY a call)

- **You pay** the premium.
- **Your right:** to buy the underlying at the strike. You exercise only if the market is above the strike.
- **Your obligation:** none. You can always walk away.
- **View:** bullish (expect a rise).
- **Maximum loss:** the premium paid (limited).
- **Maximum gain:** unlimited in principle (rises as the underlying rises).
- `Payoff (long call) = max(S - K, 0) - premium`, where S is the underlying level at expiry and K is the strike.

#### 2. Short Call (you SELL / write a call)

- **You receive** the premium.
- **Your right:** none worth speaking of — you have already been paid.
- **Your obligation:** if the buyer exercises (market above strike), you must deliver the underlying at the strike, i.e. settle the difference in cash. You are forced to "sell low."
- **View:** bearish-to-neutral (expect the market to stay below the strike).
- **Maximum gain:** the premium received (limited).
- **Maximum loss:** unlimited — as the market rises, your obligation grows without bound.
- `Payoff (short call) = premium - max(S - K, 0)`.

#### 3. Long Put (you BUY a put)

- **You pay** the premium.
- **Your right:** to sell the underlying at the strike. You exercise only if the market is below the strike.
- **Your obligation:** none. You can walk away.
- **View:** bearish, or hedging a holding.
- **Maximum loss:** the premium paid (limited).
- **Maximum gain:** large but capped (the underlying can only fall to zero): up to `strike - premium`.
- `Payoff (long put) = max(K - S, 0) - premium`.

#### 4. Short Put (you SELL / write a put)

- **You receive** the premium.
- **Your right:** none.
- **Your obligation:** if the buyer exercises (market below strike), you must buy the underlying at the strike, i.e. settle the difference in cash. You are forced to "buy high."
- **View:** bullish-to-neutral (expect the market to stay above the strike).
- **Maximum gain:** the premium received (limited).
- **Maximum loss:** very large (down to `strike - premium` if the underlying goes to zero).
- `Payoff (short put) = premium - max(K - S, 0)`.

Notice the pattern. **Buyers pay premium and own rights with limited loss. Sellers receive premium and carry obligations with limited gain.** Buyers want the market to move (in their direction); sellers want it to sit still so the option expires worthless and they keep the premium. A long call and a short call are two faces of the same contract; whatever the call buyer gains, the call writer loses, rupee for rupee, and vice versa. The same is true for the long put and short put. Options are a **zero-sum** transfer of money between the two sides (before costs).

### Who pays and who receives the premium

The flow of money is simple and one-directional at the start: **the buyer pays the premium; the seller receives it, immediately, at the moment the trade is struck.** That cash is the buyer's maximum possible loss and the seller's maximum possible gain.

But do not confuse "receiving cash up front" with "being safe." The seller's premium income is small and fixed, while the seller's potential loss is large (for a call, unlimited). That is why NSE makes option *sellers* deposit **margin** — collateral, computed by a system called **SPAN** plus an exposure add-on — to prove they can honour their obligation. Option *buyers* pay no margin beyond the premium itself, because the premium is the most they can ever lose. We will study margin in detail later; for now, just register that selling options ties up significant capital precisely because the risk is open-ended.

## Worked example (₹, Nifty)

Let us trace one concrete trade from entry to several possible expiries. Suppose Nifty is trading at **24,000** today. You are bullish over the next couple of weeks, so you **buy one lot of the 24000 CE** (the at-the-money call) at a premium of **₹250**. Nifty's lot size is **75**.

**Step 1 — Outlay (what you pay today).**
`Premium outlay = premium * lot size = 250 * 75 = ₹18,750.`
You pay ₹18,750 to the call seller. This is your **maximum loss**, fixed and known. You post no further margin because you are the buyer.

**Step 2 — Breakeven (the level you need just to recover the premium).**
`Breakeven = strike + premium = 24000 + 250 = 24,250.`
At expiry, Nifty must finish **above 24,250** for you to make a net profit. Between 24,000 and 24,250 the option has some value but not enough to cover what you paid.

**Step 3 — Outcomes at expiry.** Remember index options are cash-settled at expiry on the final settlement price. Per-unit payoff is `max(S - 24000, 0) - 250`; multiply by 75 for the lot.

- **Nifty closes at 23,500 (fell).** Your right to buy at 24,000 is worthless — why exercise the right to buy at 24,000 when the market is 23,500? The call expires worthless. **Net P&L = -₹18,750** (the whole premium). This is the common case: most bought options, especially out-of-the-money ones, expire worthless.
- **Nifty closes at 24,000 (flat).** The option is exactly at the strike; intrinsic value is zero. **Net P&L = -₹18,750.** Being right about direction is not enough — you needed *enough* movement.
- **Nifty closes at 24,250 (your breakeven).** Per-unit intrinsic value = `24250 - 24000 = 250`, which exactly equals the premium. `(250 - 250) * 75 = ₹0`. **You break even.**
- **Nifty closes at 24,500.** Per-unit intrinsic value = `24500 - 24000 = 500`. Net per unit = `500 - 250 = 250`. **Net P&L = 250 * 75 = +₹18,750** — you doubled your money.
- **Nifty closes at 25,000.** Per-unit intrinsic value = `25000 - 24000 = 1000`. Net per unit = `1000 - 250 = 750`. **Net P&L = 750 * 75 = +₹56,250.** Note how the upside keeps growing the higher Nifty goes — open-ended gain.

**Step 4 — The seller's side, for contrast.** Whoever sold you this call received your ₹18,750 up front. In the first two scenarios (Nifty at or below 24,000) the seller keeps the entire ₹18,750 as profit. But in the last scenario (Nifty 25,000) the seller *loses* ₹56,250 — far more than the premium collected — and had Nifty rocketed to 26,000 the seller's loss would have been larger still. This is the option seller's bargain: collect a small sure thing, risk a large uncertain loss.

A quick mirror example for a **put**: if instead you had been bearish and bought one lot of the **24000 PE at ₹250**, your outlay would again be ₹18,750, your breakeven would be `strike - premium = 24000 - 250 = 23,750`, and you would profit only if Nifty closed *below* 23,750. At a close of 23,500, per-unit payoff = `max(24000 - 23500, 0) - 250 = 500 - 250 = 250`, so **+₹18,750**.

## Common mistakes / risk note

**"The premium is so cheap, it's almost free."** ₹250 looks small, but you control 75 units of a 24,000 index — about ₹18 lakh of notional exposure — for ₹18,750. That leverage cuts both ways. It is entirely normal for a bought option to lose 100% of its value in days. Size positions by the rupees you can afford to lose entirely, not by how "cheap" the premium looks.

**Thinking the option pays just because you were right on direction.** A long call needs the market above *breakeven* (strike + premium), not merely above today's price. Many beginners are correct that the market rose, yet still lose money because it did not rise *enough* before expiry. The premium is a hurdle you must clear.

**Confusing rights with obligations — especially as a seller.** New traders are lured by the steady premium income of selling options and forget that they have *sold away their choice*. A short call has theoretically unlimited loss; a short put can lose almost the entire strike. Sellers also face margin calls if the market moves against them intraday. Never write a naked option without understanding that your maximum loss dwarfs your maximum gain.

**Forgetting that index options are European and cash-settled.** You cannot exercise a Nifty option early to "lock in" a midday gain. You can only *sell the option back* in the market before expiry; settlement against the strike happens only at expiry, on the official settlement price.

**The honest big picture.** SEBI's own studies have found that roughly **9 out of 10 individual F&O traders lose money**, with the average loser losing meaningful sums. Add **costs** — brokerage, exchange fees, GST, and **STT (Securities Transaction Tax)**, which on options is charged on the premium when you sell and, importantly, on the *settlement value* of in-the-money options at expiry. These frictions quietly erode returns. Options are powerful tools, not lottery tickets. Respect the math.

## Key takeaways

- A **call** is the right to *buy* at the strike; a **put** is the right to *sell* at the strike. Both are *rights for the buyer*, granted in exchange for the premium.
- The **buyer (long)** pays premium, holds the right, and has **limited loss** (the premium). The **seller (short)** receives premium, carries the obligation, and has **limited gain** but large/open-ended loss.
- There are exactly **four basic positions**: long call, short call, long put, short put. Every trade pairs a long with a short — options are zero-sum between the two sides.
- The five terms to know cold: **underlying, strike, premium, expiry, lot size.** A quote like "24000 CE @ ₹250" encodes them all.
- Indian **index options are European and cash-settled** (exercise only at expiry, settle the cash difference). Stock options are American and physically settled.
- **Breakeven** for a long call is `strike + premium`; for a long put it is `strike - premium`. Being right on direction is not enough — you must clear the premium.
- Sellers post **SPAN margin** because their risk is open-ended; buyers post only the premium.

## Practice problems

1. **(Conceptual)** In one sentence each, state who has the *right* and who has the *obligation* in (a) a call contract and (b) a put contract.

2. **(Conceptual)** Match the market view to the position: bullish, bearish, neutral-to-bullish, neutral-to-bearish — for long call, long put, short call, short put.

3. **(Numeric)** You buy one lot of **Bank Nifty 52000 CE** at a premium of **₹400**. Bank Nifty's lot size is **30**. Compute (a) your total outlay, (b) your breakeven level, (c) your maximum loss.

4. **(Numeric)** Using the position in Problem 3, find your net profit or loss if Bank Nifty closes at expiry at (a) 51,500, (b) 52,400, (c) 53,000.

5. **(Numeric)** A trader **sells** (writes) one lot of **Nifty 24000 PE** at a premium of **₹250**, lot size **75**. What is the writer's net P&L if Nifty closes at expiry at (a) 24,300 and (b) 23,500? What is the writer's maximum possible profit?

6. **(Conceptual / risk)** Your friend says, "Selling options is great — you get paid up front and most options expire worthless, so I'll just keep writing calls." Give two reasons this is dangerous.

## Solutions

**1.** (a) **Call:** the *buyer* has the right to buy at the strike; the *seller (writer)* has the obligation to sell at the strike if the buyer exercises. (b) **Put:** the *buyer* has the right to sell at the strike; the *seller (writer)* has the obligation to buy at the strike if the buyer exercises. In both cases, rights belong to the buyer and obligations to the seller.

**2.** **Long call → bullish** (wants the market up). **Long put → bearish** (wants the market down). **Short call → neutral-to-bearish** (wants the market to stay at or below the strike so the call expires worthless). **Short put → neutral-to-bullish** (wants the market to stay at or above the strike). Buyers need movement; sellers profit from the market sitting still.

**3.** (a) Outlay = `premium * lot = 400 * 30 = ₹12,000`. (b) Breakeven = `strike + premium = 52000 + 400 = 52,400`. (c) Maximum loss = the premium paid = **₹12,000** (the call expires worthless if Bank Nifty finishes at or below 52,000).

**4.** Per-unit payoff = `max(S - 52000, 0) - 400`, times 30.
- (a) **51,500:** below the strike, so `max(51500 - 52000, 0) = 0`; net per unit = `0 - 400 = -400`; total = `-400 * 30 = -₹12,000` (full premium lost).
- (b) **52,400:** intrinsic = `52400 - 52000 = 400`; net per unit = `400 - 400 = 0`; total = **₹0** (breakeven, as expected).
- (c) **53,000:** intrinsic = `53000 - 52000 = 1000`; net per unit = `1000 - 400 = 600`; total = `600 * 30 = +₹18,000`.

**5.** The writer of a put has `Payoff = premium - max(K - S, 0)` per unit, times 75.
- (a) **24,300:** above the strike, so `max(24000 - 24300, 0) = 0`; net per unit = `250 - 0 = 250`; total = `250 * 75 = +₹18,750`. The put expires worthless and the writer keeps the whole premium.
- (b) **23,500:** `max(24000 - 23500, 0) = 500`; net per unit = `250 - 500 = -250`; total = `-250 * 75 = -₹18,750`. The writer is forced to "buy at 24,000" when the market is 23,500, losing more than the premium collected.
- **Maximum profit** = the premium received = `250 * 75 = ₹18,750`, achieved whenever Nifty finishes at or above the strike of 24,000.

**6.** Two dangers: (i) **The loss is open-ended relative to the gain.** Writing a call earns at most the premium (here a fixed, small sum), but if the market rallies hard the loss is unlimited — one big up-move can wipe out the profit of many successful months. (ii) **Margin and gap risk.** As a seller you must post and maintain SPAN margin; an adverse overnight gap can trigger margin calls and forced exit at the worst possible price. "Most options expire worthless" describes frequency of small wins, not the *size* of the rare large loss — and it is the rare large loss that ruins undercapitalised sellers.
