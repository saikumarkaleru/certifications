# Chapter 38: Vertical Spreads I — Bull Call & Bear Put (Debit Spreads)

You like the direction of a move, but you hate two things about simply buying an option: it is expensive, and most of that cost is "rented" time value that bleeds away every day. What if you could buy the option you want, then sell a second option a little further out to claw back part of the cost? You give up the dream of an unlimited home run, but in return you pay less, lose less if you are wrong, and stop fighting the clock so hard. That trade-off — pay less, cap the upside — is the heart of the **debit vertical spread**, and it is the first real "strategy" most professionals reach for.

This chapter covers the two debit verticals: the **bull call spread** for a moderately bullish view and the **bear put spread** for a moderately bearish view. They are mirror images of each other. Once you understand one, you understand both. We will build the intuition, derive the three numbers that define every spread (max profit, max loss, breakeven), look at how the Greeks soften compared with a naked long option, and work full rupee Nifty examples end to end.

## Core concepts

### What a vertical spread is

A **vertical spread** is a two-leg position where you simultaneously **buy one option and sell another** of the **same type** (both calls or both puts) and the **same expiry**, differing only in **strike price**. The word "vertical" comes from the option chain: same expiry means same column, and the two strikes sit one above the other vertically.

There are two flavours, defined by which leg costs more:

- **Debit spread** — the option you *buy* is more expensive than the option you *sell*, so cash flows *out* of your account on entry. You pay a **net debit**. This chapter is about debit spreads.
- **Credit spread** — the option you *sell* is more expensive than the option you *buy*, so cash flows *in*. You receive a **net credit**. (That is the next chapter — bull put and bear call spreads.)

The single idea behind a debit spread: **the short leg subsidises the long leg.** You still own the directional bet from your long option, but you have sold away the part of the move you do not expect to capture, and pocketed that money to reduce your cost.

### The bull call spread — the core debit structure

Suppose Nifty is at 24,000 and you think it will rise to around 24,300 over the next two weeks — a moderate, not explosive, move. You could buy a 24,000 call outright, but it is pricey and you do not believe Nifty will rocket past 24,500, so you are paying for upside you do not expect.

The **bull call spread** fixes this:

1. **Buy** a lower-strike call (say the 24,000 call) — this is your directional engine.
2. **Sell** a higher-strike call (say the 24,300 call) of the same expiry — this finances part of the purchase.

Because the lower-strike call is always worth more than the higher-strike call (it is more in-the-money or less out-of-the-money), you pay a **net debit**:

`Net debit = premium paid for lower call - premium received for higher call`

You have built a position that profits as Nifty rises — but only up to the higher strike. Above 24,300, every rupee you gain on your long 24,000 call is exactly offset by a rupee you lose on your short 24,300 call. Your profit is **frozen** above the upper strike. That frozen ceiling is the price you pay for the discount.

### The three numbers that define a bull call spread

Every vertical spread is fully described by three quantities. Let `K1` be the lower (bought) strike, `K2` the higher (sold) strike, and `D` the net debit paid.

**Maximum loss** happens when both calls expire worthless — Nifty closes at or below `K1`. You simply lose what you paid:

`Max loss = net debit = D`

This is the entire risk of the trade. It is **defined** and known the moment you enter — a key reason spreads are loved.

**Maximum profit** happens when Nifty closes at or above the upper strike `K2`. The long call is worth `(K2 - K1)` of intrinsic value, the short call's loss caps your gain, and you subtract what you paid:

`Max profit = (K2 - K1) - D`

The quantity `(K2 - K1)` is the **strike width** — the distance between the two strikes. So the rule is simply: **max profit = strike width minus debit.**

**Breakeven** is the spot at expiry where profit is exactly zero. You need the long call to recover the debit you paid:

`Breakeven = K1 + D`

Notice the elegant symmetry. The strike width `(K2 - K1)` is split into two parts: the debit `D` you pay, and the max profit `(K2 - K1) - D` you can earn. The ratio of these is your **risk-reward**. If you pay a debit of 100 points for a 300-point-wide spread, you risk 100 to make 200 — a 1:2 risk-reward.

### The bear put spread — the bearish mirror

The **bear put spread** is the exact reflection for a moderately *bearish* view. Now you use puts, and you buy the *higher* strike:

1. **Buy** a higher-strike put (say the 24,000 put) — gains value as Nifty falls.
2. **Sell** a lower-strike put (say the 23,700 put) of the same expiry — finances the purchase.

The higher-strike put is worth more, so again you pay a **net debit**. The position profits as Nifty falls, but only down to the lower strike, below which your profit is frozen.

Let `K1` be the lower (sold) strike, `K2` the higher (bought) strike, and `D` the net debit. The three numbers mirror the bull call spread exactly:

- `Max loss = net debit = D` — occurs when Nifty closes at or above `K2` (both puts worthless).
- `Max profit = (K2 - K1) - D` — occurs when Nifty closes at or below `K1`.
- `Breakeven = K2 - D` — the bought (higher) strike minus the debit, because here profit grows as spot falls below the upper strike.

Same skeleton, flipped direction. Bull call: bullish, breakeven *above* the lower strike. Bear put: bearish, breakeven *below* the higher strike.

### Why the Greeks are gentler

This is the subtle professional reason spreads beat naked long options for a moderate view. A long option's worst enemies are **theta** (time decay) and **vega** (sensitivity to a fall in implied volatility, written as the Greek vega). In a debit spread, your short leg has *negative* theta and *negative* vega from your perspective — meaning as the seller of that leg, time decay and volatility changes work *for* you on the short option. These partly cancel the *positive* theta drag and vega exposure of your long leg.

- **Net delta** — positive for a bull call spread (you profit as spot rises), negative for a bear put spread. But it is *smaller* than the long leg alone, because the short leg's delta opposes it. Your directional exposure is diluted, which is exactly right for a *moderate* view.
- **Net theta** — much smaller than a naked long option. The short leg's time decay offsets the long leg's. When the spread is roughly at-the-money this near-cancellation is strong, so a bull call spread bleeds far less per day than a lone long call. You are no longer racing the clock nearly as hard.
- **Net vega** — also greatly reduced. A naked long call is badly hurt if India VIX drops after you buy (IV crush). A bull call spread is far more insulated, because the short call you sold also loses vega value, offsetting your long call.
- **Net gamma** — likewise reduced and changes sign across the strikes.

The takeaway: a debit spread is a **calmer, cheaper, more defined-risk version** of the long option. You sacrifice the unlimited tail and the explosive gamma payoff in exchange for lower cost, lower decay, lower volatility risk, and a known maximum loss.

### Exactly when to use a debit spread

Reach for a bull call or bear put spread when **all** of these are true:

- You have a **moderate directional view** — you expect a move to a specific target, not an unlimited runaway. If you genuinely expect an explosive move, a naked long option captures more of it.
- You want **defined, limited risk** — the most you can lose is the debit, fixed at entry. No margin calls, no undefined tail risk like option selling.
- You want to **reduce cost** versus buying the option outright — useful when premiums are fat (high IV) and a naked long would bleed too much theta.
- You are **not strongly worried about an IV crush** going against a naked long — the spread already hedges much of that.

Avoid it when your view is for a huge move (the cap hurts you), or when the spread is so narrow that commissions and the bid-ask spread on two legs eat the thin profit.

## Worked example (₹, Nifty/Bank Nifty)

Let us price a real bull call spread. Assume **Nifty spot = 24,000**, weekly expiry about two weeks out. From the option chain (illustrative premiums; index options are European and cash-settled, lot size about 75):

- 24,000 call (at-the-money): premium = ₹180 per unit
- 24,300 call (out-of-the-money): premium = ₹70 per unit

**Construct the bull call spread:**

- Buy 1 lot of 24,000 call: pay 180
- Sell 1 lot of 24,300 call: receive 70
- `Net debit D = 180 - 70 = 110 points`

Strike width `K2 - K1 = 24,300 - 24,000 = 300 points`.

**The three numbers:**

`Max loss = D = 110 points`
`Max profit = (K2 - K1) - D = 300 - 110 = 190 points`
`Breakeven = K1 + D = 24,000 + 110 = 24,110`

**Convert to rupees** at lot size 75:

- Max loss = 110 * 75 = **₹8,250** (the entire net debit you paid)
- Max profit = 190 * 75 = **₹14,250**
- Risk-reward = 110 risked to make 190, roughly **1 : 1.7**

**Check three scenarios at expiry:**

| Nifty at expiry | 24,000 call (long) | 24,300 call (short) | Net payoff (points) | Net P&L (₹) |
|---|---|---|---|---|
| 23,900 | 0 | 0 | 0 - 110 = -110 | -8,250 |
| 24,110 | 110 | 0 | 110 - 110 = 0 | 0 (breakeven) |
| 24,300 | 300 | 0 | 300 - 110 = +190 | +14,250 |
| 24,500 | 500 | -200 | (500 - 200) - 110 = +190 | +14,250 (capped) |

Notice the last two rows: above 24,300 the profit stays frozen at 190 points. The short call's growing loss exactly cancels the long call's extra gains. That cap is the cost of paying only 110 instead of 180.

**Compare to buying the naked 24,000 call** (cost 180, ₹13,500). The naked call needs Nifty above 24,180 just to break even (versus 24,110 for the spread), loses ₹13,500 if Nifty stays flat (versus ₹8,250), and bleeds more theta and vega daily. The spread wins on cost, breakeven, and decay — and only loses if Nifty blasts well past 24,300, where the naked call's uncapped upside would pull ahead.

![Figure: bull call spread payoff](figs/bull_call_spread.png)

**Now the mirror — a bear put spread.** Suppose instead you are moderately bearish, expecting Nifty to drift from 24,000 toward 23,700. From the chain:

- 24,000 put: premium = ₹175
- 23,700 put: premium = ₹65

**Construct:**

- Buy 1 lot of 24,000 put: pay 175
- Sell 1 lot of 23,700 put: receive 65
- `Net debit D = 175 - 65 = 110 points`

Here `K2 = 24,000` (bought, higher) and `K1 = 23,700` (sold, lower), width = 300.

`Max loss = D = 110 points = ₹8,250`
`Max profit = 300 - 110 = 190 points = ₹14,250`
`Breakeven = K2 - D = 24,000 - 110 = 23,890`

You profit as Nifty falls below 23,890, with profit maxing out at and below 23,700. If Nifty instead rises and closes above 24,000, both puts expire worthless and you lose the ₹8,250 debit — nothing more.

![Figure: bear put spread payoff](figs/bear_put_spread.png)

## Common mistakes / risk note

- **Forgetting that the upside is capped.** Beginners enter a bull call spread, watch Nifty rocket past the short strike, and feel cheated that profit stopped. That cap is the deal you signed. If you expect a big move, do not use a spread.
- **Choosing strikes too far apart "to get more upside."** A very wide spread costs almost as much as the naked long and behaves like one — you lose the cost and decay benefits. The whole point is a *targeted* width matching your expected move.
- **Choosing strikes too narrow.** A 50-point-wide Nifty spread might yield only ₹1,000–2,000 of max profit, which two-leg brokerage, STT, and bid-ask slippage can largely consume. The reward must justify the friction.
- **Ignoring liquidity on the short strike.** If the higher (or lower) strike is illiquid with a wide bid-ask, you get a poor fill and your real debit is worse than the screen suggests. Stick to liquid, near-the-money strikes on Nifty and Bank Nifty.
- **Assuming "defined risk" means "likely to win."** The max loss is capped, yes — but a debit spread still *loses the full debit* if your direction is simply wrong, and that is the most common outcome. Like all long-premium structures, you can lose 100% of what you put in. Defined risk is not the same as high probability; you are still paying for a directional bet that often does not pay.
- **Holding index spreads expecting early exercise games.** Nifty and Bank Nifty options are **European** — no early assignment. (On physically settled *stock* options, a deep in-the-money short leg can be assigned and trigger physical delivery obligations, so manage those before expiry.)

## Key takeaways

- A **debit vertical spread** buys one option and sells another of the same type and expiry but a different strike, paying a net debit to reduce cost and define risk.
- **Bull call spread** (moderately bullish): buy lower-strike call, sell higher-strike call. **Bear put spread** (moderately bearish): buy higher-strike put, sell lower-strike put. They are mirror images.
- For both: `Max loss = net debit`, `Max profit = strike width - net debit`, and breakeven is `lower strike + debit` (bull call) or `higher strike - debit` (bear put).
- The trade-off is a **capped upside** in exchange for lower cost, lower breakeven, and reduced **theta** and **vega** drag versus a naked long option.
- Net delta is smaller than the long leg alone — perfect for a *moderate* directional view, not an explosive one.
- Use spreads when you want defined risk, a specific target, and cheaper directional exposure; avoid them when you expect a huge move or when the strikes are so narrow that costs eat the profit.

## Practice problems

1. **(Conceptual)** Explain in one sentence why a bull call spread always costs a net debit rather than producing a net credit.

2. **(Numeric)** Bank Nifty is at 52,000. You buy the 52,000 call for ₹400 and sell the 52,500 call for ₹180, same expiry, lot size 15. Find the net debit, max profit, max loss, and breakeven (in points and in rupees where asked).

3. **(Numeric)** Using the bear put spread from the worked example (buy 24,000 put at 175, sell 23,700 put at 65), compute the net P&L in rupees if Nifty closes at expiry at (a) 24,200, (b) 23,890, and (c) 23,600. Lot size 75.

4. **(Conceptual)** You are strongly convinced Nifty will surge from 24,000 to 25,500 in a week. Is a bull call spread the right tool? Why or why not?

5. **(Numeric / reasoning)** Two bull call spreads on Nifty (spot 24,000): Spread A is 24,000/24,200 for a debit of 80; Spread B is 24,000/24,500 for a debit of 150. Which has the better risk-reward ratio, and which would you prefer if you expect Nifty to reach exactly 24,300?

6. **(Conceptual)** Why does a bull call spread suffer far less from an India VIX (implied volatility) crash than a naked long 24,000 call?

## Solutions

**1.** Because the option you buy (the lower-strike call) is always worth more than the option you sell (the higher-strike call) — a lower strike gives more right to buy, so it carries a higher premium. Paying more than you receive means cash flows out: a net debit.

**2.** Net debit `D = 400 - 180 = 220 points`. Strike width = `52,500 - 52,000 = 500 points`.
- Max loss = `D` = 220 points = `220 * 15` = **₹3,300** (Bank Nifty closes at or below 52,000).
- Max profit = `width - D = 500 - 220 = 280 points` = `280 * 15` = **₹4,200** (closes at or above 52,500).
- Breakeven = `K1 + D = 52,000 + 220 = 52,220`.
- Risk-reward = 220 risked to make 280, about **1 : 1.27**.

**3.** Net debit = 110 points. Bought 24,000 put, sold 23,700 put.
- (a) **24,200**: both puts expire worthless. Payoff = `0 - 110 = -110` points = `-110 * 75` = **-₹8,250** (full loss).
- (b) **23,890**: long 24,000 put intrinsic = `24,000 - 23,890 = 110`; short 23,700 put = 0. Payoff = `110 - 110 = 0` = **₹0** (breakeven, as expected since breakeven = 23,890).
- (c) **23,600**: long put intrinsic = `24,000 - 23,600 = 400`; short put intrinsic = `23,700 - 23,600 = 100` (a loss to you). Net = `(400 - 100) - 110 = 190` points = `190 * 75` = **+₹14,250** (capped max profit, since 23,600 is below the lower strike 23,700).

**4.** No. A 1,500-point surge would blow well past any reasonable short strike, where the spread's profit is frozen. The cap throws away most of the move you expect. For a strong, large, fast move, a **naked long call** (uncapped upside) captures far more — accepting its higher cost and theta because you expect the move to overwhelm those drags quickly. Spreads are for *moderate*, targeted views; this is not one.

**5.**
- Spread A: max profit = `200 - 80 = 120`, risk-reward = 80 : 120 = **1 : 1.5**.
- Spread B: max profit = `500 - 150 = 350`, risk-reward = 150 : 350 = **1 : 2.33**.
- Spread B has the better risk-reward ratio on paper. But if you expect Nifty to reach **exactly 24,300**, Spread A is already fully maxed out at 24,200 (you collect the entire 120-point profit), whereas Spread B at 24,300 gives only `(24,300 - 24,000) - 150 = 150` points — less than its max and only modestly above its cost. **Prefer Spread A** here: it reaches full profit at your target and risks less capital. The lesson: match the upper strike to your actual target, not just to the headline risk-reward.

**6.** A naked long 24,000 call is **long vega** — a drop in implied volatility (India VIX falling) directly cuts its premium, often sharply right after an event ("IV crush"). In a bull call spread you also **sold** the 24,300 call, which is **short vega**: when IV falls, that short call loses value too, which is a *gain* for you and offsets the loss on your long call. The two vega exposures largely cancel, so the spread's value is far more stable when volatility collapses. You traded away vega exposure along with the capped upside.
