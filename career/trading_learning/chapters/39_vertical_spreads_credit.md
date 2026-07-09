# Chapter 39: Vertical Spreads II — Bull Put & Bear Call (Credit Spreads)

In the last chapter you built spreads by *paying* money up front: a bull call spread or a bear put spread is a **debit** structure — you buy the option you want and sell a farther one to cheapen it, and cash leaves your account on day one. This chapter flips the cash flow. Here you **collect** money up front. You sell the option that is closer to the action and buy a farther one purely as a seatbelt, and the difference lands in your account as a **net credit**. That credit is the most you can ever make; in exchange you accept a known, capped loss if the trade goes against you.

Why would a professional prefer to be paid up front? Because most of the time the underlying does *not* make a big, clean move — it drifts, chops, and grinds. A credit spread is a way to get paid for that boredom. You are no longer betting that Nifty will surge; you are betting it will simply *not collapse* through a level you have chosen. That is a fundamentally easier bet to win, and when implied volatility is rich — when option premiums are fat with fear — selling that expensive premium with a hard cap on your risk is one of the cleanest edges an income trader has. This is the workhorse trade of the patient options seller.

## Core concepts

### The credit-vertical idea: get paid, cap the risk

A **vertical spread** is two options of the same type (both puts or both calls) and the same expiry, differing only in strike — they sit *vertically* above one another on the option chain. You met the debit version in Chapter 38. The **credit** version simply reverses which leg you sell and which you buy:

- You **SELL** the option whose strike is *nearer* the current price (the expensive one — it carries more premium).
- You **BUY** the option whose strike is *farther* from the current price (the cheap one).
- Because the option you sold is worth more than the one you bought, the net is money *in*: a **net credit**.

That far option you bought is not there to make you money. It is insurance. On its own, selling a naked option exposes you to large, undefined losses (recall the short-call and short-put chapters). By owning a farther strike, you put a hard floor under how bad the loss can get — you trade away some premium in return for turning an open-ended risk into a defined, sleep-at-night number.

Two mirror-image structures come out of this idea:

- A **bull put spread** — built from puts, profits when the underlying stays *up*.
- A **bear call spread** — built from calls, profits when the underlying stays *down*.

Both are **high-probability, income-style trades**: you win not by predicting a move but by predicting that a move *won't* happen in the wrong direction.

### The bull put spread (sell higher put, buy lower put)

Picture Nifty at 24,000. You think it will hold up — maybe drift higher, maybe just stay flat — but you do not think it will crash. You want to get paid for that view.

You **sell a higher-strike put** (say the 23,800 put) and **buy a lower-strike put** (say the 23,600 put), same weekly expiry. The 23,800 put is nearer the money and richer, so you collect more for it than you pay for the 23,600 put. The difference is your credit.

Now think about what happens at expiry:

- If Nifty stays **above 23,800**, both puts expire worthless. You keep the entire credit. This is your best case — and crucially, it happens even if Nifty doesn't rise a single point. *Sideways is a win.*
- If Nifty falls **between 23,600 and 23,800**, the put you sold goes into the money and starts costing you, while the put you bought is still worthless. Your profit shrinks, then turns into a loss as Nifty drops.
- If Nifty falls **below 23,600**, both puts are in the money. Below this point every further rupee of loss on the put you sold is exactly cancelled by a rupee of gain on the put you bought. Your loss stops growing — it is capped. This is the seatbelt doing its job.

The structure is "bullish" only in the loose sense: you don't need a rally, you just need the market to *not break down* through your short strike.

`Net credit = premium received (higher put) - premium paid (lower put)`
`Strike width = higher strike - lower strike`
`Max profit = net credit (kept if underlying expires above the higher strike)`
`Max loss = strike width - net credit (suffered if underlying expires below the lower strike)`
`Breakeven = higher strike - net credit`

Notice the symmetry: the credit you collect plus the loss you risk always sum to the strike width. The width is the total chips on the table; the credit is your slice, and the rest is what the broker blocks as margin.

![Figure: bull put spread payoff](figs/bull_put_spread.png)

### The bear call spread (sell lower call, buy higher call)

The bear call spread is the exact mirror, built from calls, for when you think the market will *not rise* — it will fall or stay flat.

With Nifty at 24,000, you **sell a lower-strike call** (say the 24,200 call) and **buy a higher-strike call** (say the 24,400 call). The nearer 24,200 call is richer, so you collect a net credit.

At expiry:

- If Nifty stays **below 24,200**, both calls expire worthless and you keep the full credit. Again, flat or falling — either one wins.
- Between **24,200 and 24,400**, the call you sold hurts you while the call you bought still pays nothing; profit erodes into loss.
- **Above 24,400**, both calls are in the money, the gains and losses offset rupee-for-rupee, and your loss is capped.

`Net credit = premium received (lower call) - premium paid (higher call)`
`Strike width = higher strike - lower strike`
`Max profit = net credit (kept if underlying expires below the lower strike)`
`Max loss = strike width - net credit (suffered if underlying expires above the higher strike)`
`Breakeven = lower strike + net credit`

![Figure: bear call spread payoff](figs/bear_call_spread.png)

### One picture, two mirrors

Hold the two side by side and the family resemblance is obvious:

| | **Bull put spread** | **Bear call spread** |
|---|---|---|
| Built from | Puts | Calls |
| Sell | Higher strike (nearer) | Lower strike (nearer) |
| Buy | Lower strike (farther) | Higher strike (farther) |
| Wins when underlying | Stays above short put | Stays below short call |
| Directional bias | Bullish / neutral | Bearish / neutral |
| Cash flow | Net credit | Net credit |
| Breakeven | Short strike − credit | Short strike + credit |

Both are credit spreads, both have defined risk, both are short premium. If you can read one, you can read the other by reflection.

### Why credit spreads love rich IV

Here is the strategic heart of the chapter. When **implied volatility (IV)** is high — India VIX elevated, premiums swollen with fear — every option is *expensive*. As a buyer that is bad news; you overpay and need a big move just to break even. As a *seller* it is a gift: you are paid more to take the same bet.

A credit spread is a way to sell that expensive premium **without** taking on the undefined risk of a naked short option. You collect the fat premium, but the long leg caps your downside. Compare the two ways to express "I'll sell expensive premium":

- **Naked short put:** collect a big premium, but a crash can cost you far more than you collected — potentially the whole strike value. Huge SPAN margin blocked.
- **Bull put spread:** collect slightly less premium (you spent some buying the wing), but your worst case is a small, known number, and the margin blocked is roughly just the width minus the credit.

When IV is high, the premium you give up to buy the protective wing is comparatively small, so the spread captures most of the juice while keeping the risk boxed. That is why the seasoned answer to "IV is rich and I have a mild directional lean" is so often a credit spread.

The flip side, told honestly: when IV is *low*, credit spreads pay you very little for the same width of risk. Selling cheap premium while risking the full width is a poor bargain. Credit spreads are a tool you reach for when premium is expensive, not all the time.

### The net Greeks: theta-positive, vega-short, defined risk

Knowing the Greeks of the package tells you what the trade *wants*. For both credit spreads:

- **Theta (positive).** As a net seller of premium, time decay works *for* you. Each day the underlying stays on the right side of your short strike, the spread drifts toward max profit. You are paid to wait — this is the engine of the trade.
- **Vega (negative / short).** You are net short the nearer option, so the position is short vega. If IV *falls* you profit (buy the spread back cheaper); if IV *spikes*, the spread moves against you even with price flat — a real risk to respect. You want to sell when IV is high and have it fall.
- **Delta (small, directional).** A bull put spread carries modest *positive* delta; a bear call spread modest *negative* delta. Far smaller than an outright option because the legs partly offset — these are *probability* bets with a tilt, not strong directional bets.
- **Gamma (negative).** As a net seller you are short gamma — a fast adverse move accelerates the loss. This is the price of positive theta, but the defined-risk wing stops the damage at the far strike.

In one line: **a credit spread is a positive-theta, short-vega, defined-risk trade that gets paid for the passage of time and for IV cooling off, as long as the underlying stays on the right side of your short strike.**

### Picking strikes by delta and probability

The single most useful idea for placing these trades is that **the delta of your short option is a quick estimate of the probability it expires in the money** — that is, the rough probability you lose. A put with delta around 0.30 (or −0.30) has roughly a 30% chance of finishing in the money, so selling it gives you about a 70% chance the spread expires worthless and you keep the credit.

This turns strike selection into a dial you can set:

- **Short strike farther OTM (low delta, ~0.15–0.20):** higher probability of profit (often 80%+), but a *smaller* credit. You win often and small.
- **Short strike closer to the money (higher delta, ~0.30–0.40):** larger credit, but lower probability of profit. You collect more but get challenged more often.

The **width** between your strikes is a second, separate dial: it sets your total risk (width − credit) and the margin. Wider strikes mean a bigger credit and a bigger max loss; narrower strikes mean a smaller, tighter trade.

A common professional default for index weeklies: sell the short leg around the **0.15–0.25 delta** strike (roughly the edge of the expected move), keep the width modest (say 100–300 Nifty points), aim to collect a credit of **about one-third of the width** (so risk-to-reward near 2:1 against you but with a ~70–80% win rate), and have a plan to exit at a partial profit (e.g. buy it back at 50% of max profit) rather than holding every trade to expiry.

## Worked example (₹, Nifty)

Let us trade a **bull put spread** on Nifty with real-feeling numbers. Suppose:

- Nifty spot = **24,000**, weekly expiry, lot size = **75**.
- India VIX is elevated, so put premiums are rich — a good environment to sell.
- You are mildly bullish-to-neutral: you think Nifty holds above 23,800.

You set up the spread:

- **Sell** the 23,800 put for a premium of **₹120**.
- **Buy** the 23,600 put for a premium of **₹60**.

Step 1 — Net credit per unit:
`Net credit = 120 - 60 = ₹60`

Step 2 — Strike width:
`Strike width = 23,800 - 23,600 = 200 points`

Step 3 — Max profit (per unit), kept if Nifty expires at or above 23,800:
`Max profit = net credit = ₹60`

Step 4 — Max loss (per unit), suffered if Nifty expires at or below 23,600:
`Max loss = strike width - net credit = 200 - 60 = ₹140`

Step 5 — Breakeven:
`Breakeven = higher strike - net credit = 23,800 - 60 = 23,740`

Step 6 — Convert to rupees per lot (multiply by lot size 75):
- Max profit = 60 * 75 = **₹4,500**
- Max loss = 140 * 75 = **₹10,500**
- Margin blocked ≈ max loss ≈ ₹10,500 (plus a small buffer), far less than a naked short put on Nifty.

Now read the outcomes:

- **Nifty expires at 23,800 or above (held up or flat):** both puts worthless, you keep the full ₹60 → **+₹4,500** per lot.
- **Nifty expires at 23,740 (breakeven):** the 23,800 put is worth 60; you collected 60 net, so you net zero → **₹0**.
- **Nifty expires at 23,700:** short put worth 100, long put still worthless; loss = 100 − 60 credit = 40 per unit → **−₹3,000**.
- **Nifty expires at 23,600 or below (crash):** short put worth at least 200, long put offsets everything beyond 23,600; loss capped = 140 per unit → **−₹10,500**.

Notice the win condition: you make the **full** profit on anything at or above 23,800 — including Nifty going *nowhere*. You only start losing below 23,740, and the damage is capped no matter how hard it falls. With a short strike around the 0.20–0.25 delta, this trade wins perhaps 75–80% of the time, collecting ₹4,500 each time, against a capped ₹10,500 when it fails. The discipline is to size positions so the occasional capped loss doesn't erase a long run of small wins.

For the **bear call spread**, flip everything. If instead you were mildly bearish with Nifty at 24,000, you might sell the 24,200 call for ₹110 and buy the 24,400 call for ₹50: net credit ₹60, width 200, max profit ₹4,500/lot, max loss ₹10,500/lot, breakeven = 24,200 + 60 = **24,260**. You keep the full credit on anything at or below 24,200 — flat or falling both win.

## Common mistakes / risk note

- **Mistaking "high probability" for "low risk."** A credit spread can win 80% of the time and still lose money if the 20% losses are bigger than the 80% wins (which, by design, they are — you risk ₹140 to make ₹60). The whole game is position sizing and not letting one ugly day undo a month of credits — the classic "picking up pennies in front of a steamroller" trap when oversized.
- **Ignoring the risk-reward ratio.** Selling ultra-far strikes for a tiny ₹15 credit on a 200-point width risks ₹185 to make ₹15 — one loss wipes out a dozen wins. A credit of roughly a quarter-to-a-third of the width is a saner balance.
- **Selling when IV is low.** Cheap premium means a thin credit for full-width risk. Check India VIX / IV rank first; credit spreads are a *rich-IV* tool.
- **Forgetting the short-vega exposure.** Even with price flat, a sharp IV spike (news shock, gap) can show a temporary loss. Don't panic-close on a vega blip if your short strike is still safe — but respect that an IV spike often accompanies the very move you're short.
- **Index vs stock settlement.** Nifty and Bank Nifty options are **European and cash-settled** — no early assignment, no delivery, clean for these spreads. **Stock** options are American and **physically settled**; an in-the-money short leg held into expiry can land you a delivery obligation. Prefer index spreads, or square off stock spreads before expiry.
- **Letting a tested trade ride to the bitter end.** Many professionals exit at ~50% of max profit, or close when the short strike is breached, rather than holding every spread to expiry and hoping. Remember STT, brokerage and exchange charges nibble at a small ₹60 credit across two legs (and again on exit).

## Key takeaways

- A **credit vertical spread** sells a nearer option and buys a farther one of the same type and expiry, collecting a **net credit** with **defined risk**.
- **Bull put spread:** sell the higher-strike put, buy the lower-strike put. Max profit = credit; max loss = width − credit; breakeven = higher strike − credit. Profits if the underlying stays *above* the short strike — bullish/neutral.
- **Bear call spread:** the mirror — sell the lower call, buy the higher call. Profits if the underlying stays *below* the short strike — bearish/neutral.
- These are **positive-theta, short-vega, defined-risk** trades: you are paid for time passing and for IV falling, with a capped worst case.
- **Favour credit spreads when IV is rich** — you sell expensive premium and the protective wing is cheap relative to the juice you keep.
- Set strikes by **delta as a probability proxy**: short-leg delta ≈ chance of loss. Farther strikes = higher win rate, smaller credit; closer strikes = bigger credit, lower win rate.
- High win-rate does not mean safe. Losses are bigger than wins by design — **size small and respect the capped-but-real max loss**.

## Practice problems

1. **(Conceptual)** You are neutral-to-bullish on Bank Nifty and India VIX is high. Which credit spread fits, and which leg do you sell versus buy? Why does high IV make this attractive?

2. **(Numeric)** A bull put spread on Nifty: sell the 23,500 put for ₹95, buy the 23,300 put for ₹40. Find the net credit, strike width, max profit, max loss, and breakeven (all per unit). Lot size 75 — give max profit and max loss in rupees per lot.

3. **(Numeric)** A bear call spread on Nifty (spot 24,000): sell the 24,300 call for ₹85, buy the 24,500 call for ₹35. Find the net credit, max profit, max loss, and breakeven. At expiry Nifty closes at 24,260 — what is the per-unit profit or loss?

4. **(Conceptual / Greeks)** A trader puts on a bull put spread. Price doesn't move at all for two days, yet the position shows a small loss. Give two distinct reasons this can happen.

5. **(Application)** You want a bull put spread with about a 75% chance of expiring worthless and a credit near one-third of the width. Roughly what delta should the short put be, and how would you choose the width? Explain the trade-off if you instead sold a 0.40-delta short put.

6. **(Risk)** A bull put spread collects ₹60 credit on a 200-point width (lot 75). It wins 80% of the time. Over 10 trades you win 8 and lose 2 at max loss. What is your net rupee result, and what lesson does it teach about sizing?

## Solutions

**1.** Use a **bull put spread** (built from puts; profits if Bank Nifty stays up or merely flat). You **sell the higher-strike put** (nearer the money, richer premium) and **buy a lower-strike put** (farther, cheaper) as protection, collecting a net credit. High IV makes it attractive because every put is expensive, so you are paid a fatter credit for the same defined risk; the protective long put you must buy is comparatively cheap, so the spread keeps most of the rich premium while capping the downside. You also benefit if that elevated IV later falls (short vega).

**2.** 
- Net credit = 95 − 40 = **₹55**
- Strike width = 23,500 − 23,300 = **200**
- Max profit = net credit = **₹55** per unit
- Max loss = width − credit = 200 − 55 = **₹145** per unit
- Breakeven = 23,500 − 55 = **23,445**
- Per lot (×75): max profit = 55 × 75 = **₹4,125**; max loss = 145 × 75 = **₹10,875**.

**3.** 
- Net credit = 85 − 35 = **₹50**
- Max profit = **₹50** per unit (kept if Nifty ≤ 24,300)
- Max loss = width − credit = 200 − 50 = **₹150** per unit
- Breakeven = 24,300 + 50 = **24,350**
- At 24,260: this is **below** the short strike 24,300, so both calls expire worthless → you keep the full credit → **+₹50 per unit** (+₹3,750 per lot). (Note 24,260 is below breakeven 24,350, confirming a profit.)

**4.** Two distinct reasons, even with price flat:
- **Short vega / IV rise.** The position is net short vega. If implied volatility ticked up (a news jitter, an event approaching), the option you are short fattened more than the one you are long, showing a mark-to-market loss despite no price move.
- **Bid-ask / transaction friction.** The credit is marked off the mid, but to *close* you cross two spreads; the immediate liquidation value can be slightly worse than the entry credit, showing a small paper loss. (Theta would push the opposite way, helping over time — so a same-direction loss after two flat days points to IV or spread costs, not decay.)

**5.** For roughly a 75% chance of expiring worthless, sell the short put at about the **0.25 delta** strike (delta ≈ probability of finishing in the money ≈ 25% chance of loss, so ~75% chance of full profit). Then choose the **width** so the credit is near one-third of it — e.g. if you collect about ₹55–₹65, a width of around 200 points gives a credit close to a third of the 200-point risk. The trade-off of instead selling a **0.40-delta** short put: you collect a *larger* credit (better reward), but the probability of profit drops to roughly 60%, the short strike sits closer to spot so it gets breached more often, and you'll be tested (and forced to manage or take losses) far more frequently. More credit, less safety.

**6.** Wins: 8 × ₹60 × 75 = 8 × ₹4,500 = **+₹36,000**. Losses: max loss = (200 − 60) × 75 = ₹10,500 each; 2 × ₹10,500 = **−₹21,000**. Net = 36,000 − 21,000 = **+₹15,000**. The lesson: an 80% win rate is *not* a licence to relax — two losing trades erased more than half of eight winners, because each loss (₹10,500) is over twice each win (₹4,500). If you had merely doubled position size, a cluster of three or four losses could turn the whole sequence negative. The edge in credit spreads lives or dies on **position sizing and loss management**, not on the win rate alone.
