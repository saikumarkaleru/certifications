# Chapter 8: Settlement & Expiry Day — Cash, Physical & the STT Trap

Every option contract is a promise with a deadline. For weeks the promise floats around, changing hands, gaining and losing value — but on one specific day the music stops and the promise must be made good. That day is **expiry**, and the process of making good is called **settlement**. This is the moment the abstract contract turns into an actual movement of money (or, for stocks, an actual movement of shares) in and out of your account. Most beginners spend all their energy on entry — which strike, which direction — and almost none on what happens at the finish line. That is a mistake, because expiry day in India has its own peculiar mechanics, its own taxes, and its own traps that can quietly eat a winning trade.

The single most important thing to burn into your memory is this: **how an option settles depends entirely on what it is written on.** Index options (Nifty, Bank Nifty, FinNifty) settle in **cash** — no shares ever change hands. Single-stock options (Reliance, Infosys, HDFC Bank) settle by **physical delivery** — if you are holding an in-the-money stock option at expiry, you are obliged to actually give or take the real shares. These two worlds behave very differently on the last day, and confusing them is one of the fastest ways for a new F&O trader to receive a margin shock or a brutal tax bill. This chapter walks through both.

## Core concepts

### What "settlement" actually means

Settlement is the exchange's way of closing the books on a contract. When an option expires, one of two things is true:

- The option is **out-of-the-money (OTM)** or **at-the-money (ATM)** — no intrinsic value. It expires worthless and disappears. The buyer loses the premium; the seller keeps it.
- The option is **in-the-money (ITM)** — it has intrinsic value, so value must flow from the seller to the buyer. *How* that value flows is the cash-versus-physical distinction.

Indian options are **European style**, meaning they can only be exercised *at* expiry, never before. (You can always sell the option in the market beforehand — that is different from exercising it.) So all the settlement drama is concentrated on one day.

### Cash settlement: how index options finish

For Nifty, Bank Nifty and the other index options, settlement is purely a cash adjustment. No one delivers a basket of 50 stocks. Instead, at expiry the exchange computes the option's intrinsic value and simply **credits the buyer and debits the seller** that amount of cash.

The crucial subtlety is *which price* the exchange uses. It is **not** the last traded price of the index, and it is **not** the dramatic closing tick you see flash on your screen. It is the **settlement price**, defined as the **time-weighted average of the underlying index over the last 30 minutes of trading on expiry day** (roughly the 3:00 p.m. to 3:30 p.m. window for a normal session).

```
Settlement price = time-weighted average value of the underlying index
                   over the final 30 minutes of the expiry session
```

Why an average rather than the closing print? To stop manipulation. If settlement depended on a single instant, a large player could try to jam the index for one second at 3:30 and tilt crores of rupees of payoffs in their favour. Averaging over half an hour makes that prohibitively expensive and keeps the settlement honest. The practical consequence for you: the level your option settles at can differ — sometimes meaningfully — from the close you saw on the chart. A call that looked 8 points in-the-money on the final tick might settle only 3 points in-the-money if the index drifted up only in the last minute, because the 30-minute average sits lower.

For a cash-settled ITM index option:

```
Cash settlement amount per lot = intrinsic value per unit * lot size
intrinsic value (call) = max(settlement price - strike, 0)
intrinsic value (put)  = max(strike - settlement price, 0)
```

That money is moved automatically. You do nothing. There is no question of "delivering the Nifty."

### Physical settlement: how stock options finish

Single-stock options are a completely different animal. Since 2019, SEBI has required all **stock** derivatives (futures and options) to be **physically settled**. That means an ITM stock option at expiry is converted into an actual obligation to **deliver or receive the underlying shares** at the strike price, in the full lot quantity.

Spell out the four positions a trader can hold into expiry:

- **Long call, ITM:** the right to *buy* at the strike. You must **take delivery** — pay `strike * lot size` in cash and receive the shares in demat.
- **Short call, ITM:** obliged to *sell* at the strike. You must **give delivery** — hand over the actual shares (and if you do not own them, you must buy them, risking an auction).
- **Long put, ITM:** the right to *sell* at the strike. You must **give delivery** of the shares.
- **Short put, ITM:** obliged to *buy* at the strike. You must **take delivery** and pay for them.

The numbers are large. A single lot of a stock option can represent five to fifteen lakh rupees of stock. If you let an ITM Reliance option go to physical settlement, you may suddenly need ₹10–12 lakh of cash (to take delivery) or that much in shares (to give delivery) — for a position where you posted only a small premium or margin. This is why physical settlement is the single biggest "gotcha" in Indian stock options.

### Margins ramp up in expiry week

Because the exchange knows physical delivery is looming, it does not wait until the last moment to make sure you can honour it. For positions that *could* go to physical delivery, brokers and the exchange **progressively increase the margin** through the final week — often described as ramping up over the last four trading days, in steps, until a position that is likely to be physically settled is carrying a margin close to the full delivery value.

The intuition: early in the contract's life, an option is just a bet and a modest margin covers it. But as expiry nears and the option sits in- or near-the-money, the chance it converts into a multi-lakh delivery obligation rises sharply. The exchange demands collateral to match that growing real-world obligation. If you are caught holding such a position without the cash to support the swelling margin, your broker will start issuing margin calls — or square you off.

### Brokers auto square-off physically-settled positions

Most retail traders have neither the cash nor the demat shares to honour physical delivery, and most never intended to — they were trading the option for its price movement, not to actually own Reliance shares. Brokers know this. So nearly every Indian broker runs a **policy of auto square-off for physically-settled positions** that the client has not closed themselves.

Typically the broker publishes a deadline on expiry day (commonly some point in the afternoon, varying by broker and by how deep ITM the option is) by which you must close any stock F&O position that risks going to delivery. If you have not, the broker's risk system will **square it off on your behalf at market price**, often with an additional penalty/charge, to protect both you and the broker from an unfunded delivery obligation. This is a safety net, but it is a clumsy one — it executes at whatever price the market offers at that moment, which may be poor.

Do not rely on the auto square-off as a strategy. Treat it as the fire alarm, not the plan. The professional habit is to manage your own stock-option positions well before any broker cutoff.

### The STT trap on exercised ITM options

Now the part that catches even experienced traders off guard. **Securities Transaction Tax (STT)** is a small tax on securities transactions. On normal options trades — buying and selling the option in the market — STT is charged only on the **premium**, and it is tiny. But there is a vicious asymmetry hidden in the rules: when an option is **exercised** at expiry (i.e. you let an ITM option go to settlement rather than selling it), STT on the exercise is historically charged on a far larger base — effectively on a value tied to the **intrinsic/settlement value of the contract, not just the premium.**

Here is the trap in plain terms. Suppose you bought a far-OTM option cheaply and it drifted just barely into the money by expiry. The premium you paid was small. The intrinsic value is also small — but the *notional on which exercise STT is computed* is large relative to your premium. The STT charged on exercise can be a large multiple of the option's actual intrinsic value, occasionally even **exceeding the entire profit** — turning a nominal winner into a real loser purely through tax.

```
STT on selling the option in market   ~ small rate * premium (tiny)
STT on letting an ITM option exercise ~ much larger base tied to settlement value
```

The exact rates change over time and you should check the current schedule, but the *structure* has been consistent: **exercising a barely-ITM option is tax-expensive; selling it in the market is tax-cheap.** This single fact drives a near-universal professional behaviour.

### Why traders square off before expiry rather than let options exercise

Because of the STT trap (for index and stock options) and the physical-delivery obligation (for stock options), seasoned Indian traders almost never *let* an option exercise. Instead they **square off** — sell the long option, or buy back the short option — in the open market in the minutes or hours before expiry. By closing the position in the market:

- You pay only the small premium-based STT, dodging the punitive exercise STT.
- For stock options, you eliminate the physical-delivery obligation entirely — there is nothing left to deliver.
- You lock in the price you see, rather than waiting for the 30-minute averaged settlement that might come in worse.

The only reason a trader would deliberately allow physical settlement is if they genuinely *want* the shares (e.g. a long call where they intend to own the stock, and have the cash) or genuinely want to dispose of shares they hold (a covered call they are happy to have assigned). For pure directional or premium trades, square off.

### Premiums collapse to intrinsic value through expiry day

On the morning of expiry, an option still has a sliver of **time value** — the part of the premium that pays for the possibility of further movement. But the clock is almost out. As the hours of expiry day tick away, that time value bleeds out fast (this is **theta**, time decay, at its most violent), and by the settlement window the premium **converges to pure intrinsic value**.

```
Premium = intrinsic value + time value
At expiry, time value -> 0, so Premium -> intrinsic value
```

In practice this means:

- An **OTM option** on expiry day is racing toward zero. Its entire remaining premium is time value, and time value is evaporating. This is why buying cheap OTM options on expiry day ("expiry lottery tickets") is so seductive and so often a wipe-out — you need a large, fast move *right now* or the premium collapses to nothing in your hands.
- An **ITM option** sheds its small remaining time value and trades at roughly its intrinsic value, moving nearly one-for-one with the index (delta approaching 1).
- An **ATM option** is the most knife-edge: a few points either side decides whether it finishes worth something or nothing, and its value swings wildly on small index moves.

Understanding this collapse is what makes expiry-day option *selling* attractive to professionals (they harvest the fast-decaying time value) and expiry-day option *buying* a low-probability gamble for most retail traders.

### Do-not-exercise (DNE) and close-to-the-money rules

To protect traders from accidentally triggering the STT trap and physical settlement on options that are only *marginally* ITM, the system has evolved a few safeguards.

- **Do-Not-Exercise (DNE) instructions.** Historically, brokers let clients flag a **close-to-the-money (CTM)** long option with a "do not exercise" instruction, so that an option that finished only slightly in-the-money would *not* be exercised — sparing the holder an exercise STT that exceeded the tiny intrinsic gain. The holder forgoes the small intrinsic value to avoid a larger tax.
- **Automatic exercise of ITM options.** By default, ITM options are **automatically exercised** at expiry; the holder does not need to send any instruction to claim the money. DNE is the exception that switches this off for marginal cases.
- **Evolving mechanics.** The precise CTM/DNE framework has changed over the years as the exchange refined how it handles near-the-money stock options at expiry, so treat the *mechanism* as something to verify with your broker each time, while the *principle* — don't let a marginally-ITM option exercise into a tax/delivery you don't want — stays constant.

The cleanest way to never worry about DNE rules at all is, again, to **square off in the market before expiry.** A closed position has nothing to exercise.

## Worked example (₹, Nifty cash & a stock option physical)

### Example A — Nifty index option, cash settlement

**Setup.** It is weekly expiry day. You are long 2 lots of the **Nifty 24,000 call**, bought earlier in the week at a premium of ₹110. Lot size 75. Through the afternoon, Nifty hovers around 24,180. On the final tick at 3:30 the index prints 24,210, but the **time-weighted average over 3:00–3:30 p.m. comes out to 24,160.**

**If you let it go to settlement (auto-exercise):**

The cash settlement uses the *averaged* settlement price, not the 3:30 print.

```
Intrinsic value per unit = max(settlement - strike, 0)
                         = max(24,160 - 24,000, 0) = 160
Settlement per lot       = 160 * 75 = ₹12,000
Two lots                 = ₹24,000 credited in cash
```

Notice you did **not** get the 24,210 closing tick (which would have been 210 points = ₹15,750/lot). The 30-minute average of 24,160 governs. No shares change hands — this is an index option, so it is pure cash. Against your premium cost of `110 * 75 * 2 = ₹16,500`, your gross profit is `24,000 - 16,500 = ₹7,500` before charges.

**But** letting it exercise triggers the higher **exercise STT** on the settlement value, plus you are at the mercy of the averaged price. The professional alternative:

**If you square off before expiry:** suppose at 3:20 p.m. the call trades at ₹185 (almost all intrinsic now, time value nearly gone). You sell 2 lots:

```
Sale proceeds = 185 * 75 * 2 = ₹27,750
Profit        = 27,750 - 16,500 = ₹11,250 (before charges)
STT charged only on the premium-based market sale (tiny)
```

You captured a better price *and* avoided the punitive exercise STT. This is exactly why active traders close out rather than wait for settlement.

### Example B — Stock option, physical settlement

**Setup.** You are long 1 lot of a **Reliance 2,900 call** (assume lot size 250, a typical magnitude — confirm the live lot). You paid a premium of ₹40. It is monthly expiry day and Reliance is trading at **2,955** — your call is 55 points in-the-money.

**The looming obligation.** This is a *stock* option, so it is **physically settled**. If you do nothing and the call expires ITM, you must **take delivery** of the shares at the strike:

```
Cash required to take delivery = strike * lot size = 2,900 * 250 = ₹7,25,000
Shares received                = 250 Reliance shares into your demat
```

You paid only `40 * 250 = ₹10,000` in premium, but settlement would demand **₹7.25 lakh in cash** to take 250 shares. Through expiry week your broker has been **ramping up the margin** on this position precisely because this delivery obligation is now likely. If your account cannot fund the swelling margin, you will get margin calls.

**What actually happens for most traders.** Either:

1. You **square off** the option in the market before the broker's expiry-day cutoff — e.g. sell the call at its intrinsic-plus-tiny-time value of about ₹57:
   ```
   Sale proceeds = 57 * 250 = ₹14,250
   Profit        = 14,250 - 10,000 = ₹4,250 (before charges)
   No delivery obligation, only small premium-based STT.
   ```
2. Or you do nothing and the **broker auto-squares-off** the position near its deadline at whatever market price prevails (possibly worse), often with a penalty — your safety net, not your plan.
3. Or, if you genuinely want to own 250 Reliance shares and have ₹7.25 lakh ready, you **let it go to delivery**, pay the cash, and receive the shares — and accept the higher exercise STT.

For a trader who only ever wanted to play Reliance's price move, option (1) — square off — is clearly correct. The danger is the trader who *forgets* they are holding a stock option, assumes it works like a Nifty option (cash), and is blindsided by a ₹7.25 lakh delivery demand or a ramped-up margin call.

## Common mistakes / risk note

- **Treating stock options like index options.** The deadliest error. Index = cash, painless. Stock = physical delivery, multi-lakh obligation. Always know which one you are holding into expiry week.
- **Letting a barely-ITM option exercise.** The exercise STT is charged on a large settlement-linked base, not on the premium, and can swallow — or exceed — a small intrinsic gain. Square off in the market or use a do-not-exercise instruction.
- **Expecting the closing tick to be the settlement price.** Index options settle on the **30-minute time-weighted average** of the underlying, not the 3:30 print. Your payoff can differ from what the chart's last candle suggests.
- **Relying on broker auto square-off.** It is a backstop that executes at an uncontrolled price, often with a penalty. Manage your own positions before the cutoff; do not outsource your exit to the risk engine.
- **Ignoring expiry-week margin ramp-up on stock options.** Margins climb sharply in the last few days for delivery-eligible positions. An account that was comfortable on Monday can face margin calls by Wednesday.
- **Buying OTM options on expiry day expecting magic.** Time value collapses to zero through the day (peak theta). Without an immediate, large move, the premium evaporates. Most of these "lottery tickets" go to zero.
- **The honest risk.** Expiry mechanics do not create edge — they create ways to *lose* edge you already had. A winning directional call can be turned into a net loss by exercise STT, a poor averaged settlement, or an auto-square-off at a bad price. SEBI studies show roughly 9 in 10 retail F&O traders lose money; sloppy expiry handling is one of the quiet contributors.

## Key takeaways

- **Index options settle in cash; stock options settle by physical delivery.** This single distinction governs everything that happens on expiry day.
- Index settlement uses the **time-weighted average of the underlying over the last 30 minutes**, not the closing tick — designed to prevent last-second manipulation.
- An ITM stock option means a **real obligation to give or take shares** at the strike, often lakhs of rupees; brokers **ramp up margins through expiry week** and **auto square-off** unfunded positions.
- **Exercise STT** on letting an ITM option settle is charged on a large settlement-linked base and can exceed a small intrinsic gain — the classic "STT trap."
- Because of the STT trap and delivery risk, professionals almost always **square off before expiry** rather than let options exercise.
- Through expiry day, **time value decays to zero and premium converges to intrinsic value** — brutal for OTM buyers, the harvest for sellers.
- **Do-not-exercise / close-to-the-money** rules let you decline exercise on a marginally-ITM option; but the simplest protection is to close the position in the market.

## Practice problems

1. **(Conceptual.)** Your friend holds an ITM Nifty call and an ITM Infosys call into expiry, both worth the same intrinsic value. He assumes both will simply pay him cash. Where is he wrong, and what must he do about the Infosys position?

2. **(Numeric — cash settlement.)** You are long 1 lot of the Nifty 23,500 call (lot 75), bought at ₹90. On expiry the final tick is 23,640 but the 3:00–3:30 time-weighted average is 23,610. If you let it cash-settle, what is your settlement credit and your gross profit before charges? How would the answer differ if settlement used the final tick?

3. **(Numeric — selling vs exercising.)** For the position in problem 2, suppose at 3:20 p.m. the call trades in the market at ₹118. Compare squaring off at ₹118 versus letting it auto-exercise on the averaged settlement. Which gives a better gross result, and name one additional reason (beyond the price) to prefer squaring off.

4. **(Numeric — physical settlement.)** You are long 1 lot of a stock call, strike ₹1,500, lot size 600, premium paid ₹25, and it expires 30 points ITM. (a) If you let it go to physical delivery, how much cash must you produce and what do you receive? (b) If instead you square off at an intrinsic-plus value of ₹31, what is your profit, and what obligation have you avoided?

5. **(Conceptual.)** Explain why exchanges use a 30-minute average for index settlement rather than the closing price, and give one practical consequence for a trader holding an ATM option into the close.

6. **(Conceptual.)** A trader bought a far-OTM weekly option for ₹3 that finished ₹6 in-the-money at expiry. He is delighted at "doubling his money" by letting it exercise. Why might his celebration be premature?

## Solutions

**1.** The Nifty call is an **index option** — it is **cash-settled**, so it will indeed simply credit the intrinsic value in cash; he need do nothing. The Infosys call is a **single-stock option** — it is **physically settled**. If he lets it expire ITM he is obliged to **take delivery** of the full lot of Infosys shares at the strike, requiring `strike * lot size` in cash (lakhs of rupees), and he faces ramped-up expiry-week margins plus the higher exercise STT. Unless he actually wants to own the shares and has the cash, he must **square off the Infosys call in the market before his broker's expiry-day cutoff** to remove the delivery obligation (otherwise the broker may auto-square-off at a poor price with a penalty).

**2.** Settlement uses the averaged price, 23,610.
```
Intrinsic = max(23,610 - 23,500, 0) = 110
Credit    = 110 * 75 = ₹8,250
Cost      = 90 * 75 = ₹6,750
Gross profit = 8,250 - 6,750 = ₹1,500
```
If settlement used the final tick of 23,640: intrinsic = 140, credit = `140 * 75 = ₹10,500`, gross profit = `10,500 - 6,750 = ₹3,750`. The 30-minute average (23,610) gives a lower payoff than the last tick (23,640) — a reminder that the averaged settlement, not the dramatic close, governs your money.

**3.** Squaring off at ₹118: proceeds = `118 * 75 = ₹8,850`; gross profit = `8,850 - 6,750 = ₹2,100`. Letting it auto-exercise on the average (from problem 2): gross profit = ₹1,500. **Squaring off is better by ₹600** here because you capture the market price (which still holds a little value) instead of the lower averaged intrinsic. The additional reason to prefer squaring off: you pay only the **small premium-based STT** instead of the **punitive exercise STT** charged on the settlement value — so the real-world gap is even wider than ₹600.

**4.** (a) Physical delivery on a long call means you **take delivery** at the strike: cash required = `1,500 * 600 = ₹9,00,000`, and you receive **600 shares** into your demat. You only paid `25 * 600 = ₹15,000` in premium, yet settlement demands ₹9 lakh in cash — the physical-settlement shock. (b) Squaring off at ₹31: proceeds = `31 * 600 = ₹18,600`; profit = `18,600 - 15,000 = ₹3,600`. By squaring off you **avoid the ₹9 lakh delivery obligation** (and the ramped expiry-week margin and exercise STT) entirely.

**5.** A single closing print could be **manipulated** — a large player could briefly jam the index at 3:30 to swing crores of option payoffs in their favour. Averaging the underlying over the final 30 minutes makes such manipulation prohibitively expensive and produces a fairer, smoother settlement value. Practical consequence for an **ATM** holder: because the option is right on the knife-edge, the averaged settlement (rather than the visible last tick) decides whether it finishes with intrinsic value or nothing — so a position that looks ITM on the closing candle can still settle worthless if the 30-minute average sits on the other side of the strike. The safe move is to square off rather than gamble on where the average lands.

**6.** Two reasons. First, if this is a **stock** option, letting it exercise triggers **physical delivery** — a multi-lakh obligation utterly out of proportion to a ₹3 premium. Second, and applying even to index options, the **exercise STT is charged on the large settlement-linked value, not on the tiny premium**. On a barely-ITM option that STT can be a large fraction of — or even exceed — the ₹6 intrinsic gain, so the "doubling" can shrink to a small gain or flip to a net loss. He should have **sold the option in the market** before expiry, paying only the small premium-based STT and (if it was a stock option) avoiding delivery altogether.
