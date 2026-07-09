# Chapter 12: Long Put — The Bearish Bet & Portfolio Insurance

Most people find it easy to root for prices going *up*. A rising market feels like good news — your stocks gain, your mutual funds glow green, the headlines are cheerful. So when a trader buys an option that *profits from a fall*, it can feel almost unnatural, even a little pessimistic. Yet the **long put** — simply buying a put option — is one of the most useful and versatile positions in all of options trading. It does two completely different jobs, and a professional must hold both in mind at once.

The first job is **speculation**: if you genuinely believe Nifty is going to drop, a long put lets you profit from that fall while risking only a small, known premium. The second job is **insurance**: if you already own a portfolio of stocks or an index position, a long put acts exactly like a motor or health insurance policy — you pay a premium today, and if disaster strikes (the market crashes), the put pays you back, cushioning the blow. Same instrument, two minds. This chapter teaches you to recognise which job you are doing, because the discipline, the strike choice, and even the emotions involved are different for each.

## Core concepts

### What a long put is, in plain English

A **put option** gives its buyer the **right, but not the obligation, to sell** the underlying at a fixed price — the **strike (K)** — on or before expiry. When you *buy* a put (go "long" the put), you pay a **premium** today, and in return you own a locked-in selling price that protects you against the market falling.

Think of the strike as a **guaranteed floor**. Imagine you own a flat worth ₹80 lakh and you buy, for a small fee, a contract from someone who promises to buy it from you at ₹80 lakh anytime in the next six months. If property prices crash to ₹65 lakh, you happily invoke your contract and still sell at ₹80 lakh — the contract is worth ₹15 lakh to you. If prices rise to ₹95 lakh, you simply tear up the contract (you would rather sell on the open market) and you have lost only the small fee. That contract is a put. The fee is the premium.

The same logic holds whether you own the underlying or not. A speculator who owns *no* flat could still buy that contract and profit purely from prices falling — buying the right to sell at ₹80 lakh, then "buying low" at ₹65 lakh to settle. In Indian index options this all happens in **cash**: Nifty and Bank Nifty options are **European** (exercised only at expiry) and **cash-settled** (you never deliver shares; you simply receive or pay the rupee difference).

### The payoff, breakeven, and maximum loss

Let S be the underlying level at expiry and K the strike. The value of a put at expiry — its **intrinsic value** — is `max(K - S, 0)`. It pays off only when the market finishes *below* the strike, and the further below, the more it pays. Subtract what you paid:

- `Payoff (long put) = max(K - S, 0) - premium`
- `Breakeven = strike - premium`
- `Maximum loss = premium paid` (occurs whenever S finishes at or above K)
- `Maximum profit = (strike - premium)` per unit, reached only if S falls all the way to zero

Three numbers tell the whole story, so let us be precise about each.

**Maximum loss is the premium — full stop.** Because you hold a *right* and never an *obligation*, the worst that can happen is the market stays flat or rises, the put expires worthless, and you lose exactly what you paid. No margin calls, no surprise debits. This is the defining comfort of being an option buyer.

**Breakeven sits one premium *below* the strike.** Owning the put is not enough; the market has to fall *past* breakeven for you to net a profit. If you buy a 24000 put for ₹250, the market must close below `24000 - 250 = 23750` before you are in the money on a net basis. Between 24000 and 23750 the put has *some* intrinsic value, but not enough to recover the premium.

**Profit grows as the market falls — but it is capped.** This is the one important asymmetry between long puts and long calls. A long call has theoretically *unlimited* upside because a price can rise without limit. A long put's profit is **large but bounded**, because the underlying can fall at most to **zero**. The best case is S = 0, giving a per-unit profit of `K - premium`. For a 24000 put bought at ₹250, the absolute ceiling is `24000 - 250 = 23,750` points per unit — enormous, but finite. In practice indices never go to zero, so think of the realistic profit as "a lot if a real crash happens," not infinity.

### Use 1 — Speculation: betting on a fall

When you buy a put with **no underlying holding**, you are taking a directional **bearish** view: you expect the market (or a stock) to drop, and you want leveraged, loss-limited exposure to that drop. The attraction is the same asymmetry that makes long calls appealing — **limited, known loss; large, open-ended-feeling gain** — just pointed downward.

Why buy a put instead of simply short-selling the future? Because shorting a future exposes you to *unlimited* loss if the market rallies, and it ties up large SPAN margin that can trigger intraday margin calls on a sharp up-move. A long put caps your loss at the premium and needs no margin beyond it. You sleep at night. The trade-off is **theta** (time decay, discussed below): the put bleeds value every day the crash does not arrive, whereas a future does not decay.

### Use 2 — Hedging: the protective put

Now suppose you already **own** something — a basket of stocks, an index ETF, or a long Nifty future — and you are nervous about a near-term fall (a Budget, an election result, a global shock) but you do not want to *sell* your holdings and trigger tax or miss the upside. You buy a put against the holding. This is the **protective put**, and it is genuine portfolio insurance.

The mechanics are beautiful in their symmetry. If the market falls, your stocks lose value but your put *gains* value, offsetting the loss below the strike. If the market rises, your stocks profit normally and the put simply expires worthless — you "wasted" the premium, exactly as you waste a health-insurance premium in a year you stay healthy. You have converted an uncertain, open-ended downside into a known, fixed cost (the premium), while keeping all of your upside.

The strike you choose sets your **deductible**. A higher strike (closer to the current price) insures more of your portfolio but costs more premium; a lower, out-of-the-money strike is cheaper but only kicks in after the market has already fallen some distance — you "self-insure" the first slice of losses. This is identical to choosing the deductible on any insurance policy: more protection, more premium.

A subtle but important point for Indian investors: to hedge a *diversified equity portfolio*, you typically buy **Nifty puts**, because the Nifty proxies the broad market. The hedge is imperfect — your specific stocks may not move exactly with the index (this residual is called **basis risk**) — but a Nifty put is far more liquid and cheaper than buying puts on every individual holding.

### Choosing strike and expiry

For both uses, two decisions shape the trade:

- **Strike.** An **at-the-money (ATM)** put (strike near the current level) has the most time value and the highest premium, but reacts quickly to a fall (high delta magnitude). An **out-of-the-money (OTM)** put (strike below the current level) is cheaper, decays faster in percentage terms, and needs a *bigger* fall to pay off — it is a higher-leverage lottery on a sharp drop. For *speculation*, traders often pick slightly OTM strikes for cheapness; for *hedging*, the strike is chosen by how much loss you are willing to absorb before insurance kicks in.
- **Expiry.** A **weekly** put is cheap but gives the move very little time to happen — theta is brutal in the final days. A **monthly** (or longer) put costs more but buys time for your thesis to play out. A common professional error is buying a too-short, too-cheap put, watching the thesis come true *a week late*, and still losing money because the put already expired. Buy enough time.

### Theta drag — the rent you pay

A long put, like any bought option, is a **decaying asset**. Each day that passes, the option loses a slice of its **time value** — this daily bleed is called **theta** (and is a negative number for a buyer). If the underlying simply sits still, your put loses money *every single day*, with the decay accelerating as expiry approaches.

This is the hidden cost of insurance and of bearish speculation alike. You are paying "rent" for the right you hold, and the rent comes due whether or not the market falls. For the speculator, theta means you must be roughly *right on timing*, not just direction. For the hedger, theta is the steady premium cost of carrying protection — which is exactly why no one buys puts on their portfolio every single week forever; the cumulative theta would quietly drain returns. Insurance is bought when the risk is elevated, not perpetually.

### Why buying puts is psychologically hard

Long puts are emotionally awkward in a way long calls are not, and a professional should name this honestly:

1. **You are betting against optimism.** Markets drift upward over long horizons, and buying a put means hoping (or at least preparing) for a fall — which can feel like rooting against your own country's economy or your own stocks.
2. **Insurance feels like a waste when nothing goes wrong.** In most months the market does not crash, your protective put expires worthless, and your brain screams "I just threw away that premium." This regret pushes people to *stop* hedging right before the crash that would have justified it — the classic mistake.
3. **The decay is visible and demoralising.** Watching a put lose value day after day in a calm market tests anyone's conviction, tempting an early exit just before the move.

Discipline, then, means treating the premium like an insurance bill — a cost of doing business, paid without resentment — and **sizing positions so a string of worthless puts cannot hurt you**. The put that finally pays during a crash often returns many times its cost, which is the whole point.

## Worked example (₹, Nifty)

Suppose **Nifty is trading at 24,000** today. We will run the *same* 24000 put through both of its jobs. Nifty's lot size is currently **75 units**, and the **24000 PE (Put European) is quoted at ₹250**.

### Part A — Speculation (no holding)

You are bearish ahead of an event and **buy one lot of the 24000 PE at ₹250**, owning nothing else.

**Step 1 — Outlay (your maximum loss).**
`Premium outlay = premium * lot size = 250 * 75 = ₹18,750.`
You pay ₹18,750 to the put seller. That is the most you can ever lose. As a buyer you post no further margin.

**Step 2 — Breakeven.**
`Breakeven = strike - premium = 24000 - 250 = 23,750.`
Nifty must close *below* 23,750 at expiry for you to net a profit.

**Step 3 — Outcomes at expiry.** Per-unit payoff is `max(24000 - S, 0) - 250`, multiplied by 75.

- **Nifty closes at 24,300 (rose).** Your right to sell at 24,000 is worthless when the market is higher. The put expires worthless. **Net P&L = -₹18,750** (full premium lost). The common case.
- **Nifty closes at 24,000 (flat).** Intrinsic value zero; still **-₹18,750.** Being un-wrong on direction is not enough — you needed an actual fall.
- **Nifty closes at 23,750 (breakeven).** Intrinsic = `24000 - 23750 = 250`, exactly the premium. `(250 - 250) * 75 = ₹0`. **You break even.**
- **Nifty closes at 23,500.** Intrinsic = `24000 - 23500 = 500`. Net per unit = `500 - 250 = 250`. **Net P&L = 250 * 75 = +₹18,750** — you doubled your money.
- **Nifty closes at 23,000 (sharp fall).** Intrinsic = `24000 - 23000 = 1000`. Net per unit = `1000 - 250 = 750`. **Net P&L = 750 * 75 = +₹56,250.** The profit grows as Nifty falls — but remember it is *capped*: the theoretical ceiling, if Nifty somehow hit zero, is `(24000 - 250) * 75 = ₹17,81,250`. Finite, if astronomically unlikely.

![Figure: payoff of a long 24000 put at expiry](figs/long_put.png)

Notice the shape this figure captures: a flat line at the loss of -₹18,750 for every level at or above 24,000, a kink (the "hockey-stick" elbow) at the strike of 24,000, then a line rising to the upper-left as Nifty falls, crossing zero at the breakeven of 23,750.

### Part B — The protective put (hedging a holding)

Now the same put, but as insurance. Suppose you hold **one lot equivalent of Nifty exposure** — say a basket of stocks (or one long Nifty future) worth about `24000 * 75 = ₹18,00,000`. You are worried about a Budget-day fall but do not want to sell. You **buy one lot of the 24000 PE at ₹250** as protection, again costing **₹18,750**.

Your combined position is "long Nifty + long 24000 put." Let us see the net outcome at expiry (ignoring the cost basis of the holding, focusing on the change from 24,000):

- **Nifty falls to 23,000.** Holding loses `(24000 - 23000) * 75 = ₹75,000`. Put gains intrinsic `(24000 - 23000) * 75 = ₹75,000`, minus the ₹18,750 premium = `+₹56,250`. **Net = -75,000 + 56,250 = -₹18,750.** Your entire loss is capped at the premium, no matter how far Nifty falls below 24,000.
- **Nifty falls to 22,000 (a crash).** Holding loses `2000 * 75 = ₹1,50,000`. Put gains `2000 * 75 = ₹1,50,000` intrinsic, minus ₹18,750 = `+₹1,31,250`. **Net = -1,50,000 + 1,31,250 = -₹18,750.** Still capped at the same ₹18,750 — that is the insurance working. The 24000 strike is your floor.
- **Nifty rises to 25,000.** Holding gains `1000 * 75 = ₹75,000`. Put expires worthless, costing ₹18,750. **Net = +75,000 - 18,750 = +₹56,250.** You keep almost all the upside; the put was the "wasted" insurance premium in a good year.

The pattern: below the strike your loss is frozen at the premium (₹18,750); above it you participate fully in gains, just reduced by that same premium. You have bought a **known, fixed worst case** in exchange for shaving a little off your wins. That is portfolio insurance.

## Common mistakes / risk note

**Buying a put that is too cheap and too short.** The most common speculator error: grabbing a far-OTM weekly put because it costs ₹15, then being right that the market fell — but it fell next week, after the put expired, or it did not fall *enough* to clear breakeven. Cheap puts are cheap because they are unlikely to pay. Buy enough strike and enough time for your actual thesis.

**Forgetting theta on a "correct" view.** A long put bleeds every calm day. If you are bearish but the market chops sideways for two weeks, you can lose a large chunk of the premium to decay before the fall ever comes. Direction is not enough; you must be roughly right on *timing*, or buy enough time to be patient.

**Treating the profit cap as unlimited.** Unlike a long call, a long put's gain is bounded by `strike - premium` (the underlying can only fall to zero). Do not size or fantasise as though a put can return infinitely.

**Cancelling insurance right before the crash.** Hedgers, frustrated by months of worthless puts, often stop hedging exactly when complacency is highest — and that is usually when the crash arrives. Decide your hedging policy in advance (e.g., "I protect around major events") and follow it without emotion.

**Over-hedging — paying perpetual premium.** Buying puts on your whole portfolio every week, forever, will quietly bleed your returns through cumulative theta, often costing more than the crashes you fear. Insurance is for elevated, identifiable risk, not a permanent tax on every position.

**The honest big picture.** Most bought options — puts included — **expire worthless**, and SEBI studies find roughly **9 in 10 individual F&O traders lose money**. Add costs: brokerage, exchange fees, GST, and **STT (Securities Transaction Tax)**, which on an in-the-money option at expiry is charged on the *settlement value*, not just the premium. A long put is a tool for defined-risk bearish bets and for genuine insurance — not a cheap lottery ticket on a crash.

## Key takeaways

- A **long put** is the right to *sell* at the strike; you buy it to profit from a *fall* or to *insure* a holding. Same instrument, two distinct jobs.
- `Payoff (long put) = max(K - S, 0) - premium`; `breakeven = strike - premium`; **maximum loss = premium**.
- Profit **grows as the underlying falls** but is **capped at `strike - premium`** (the price can fall only to zero) — unlike a long call's unlimited upside.
- As a **protective put**, the put freezes your loss at the premium for any fall below the strike while keeping all upside above it — true portfolio insurance, with the strike acting as a chosen deductible.
- **Strike and expiry** matter: ATM and longer-dated puts cost more but protect/react better; cheap OTM weeklies need a big, fast fall to pay off.
- **Theta** decays the put every calm day — being right on direction is not enough; you must be roughly right on timing or buy enough time.
- Buying puts is **psychologically hard** (betting against optimism, "wasting" premium when nothing breaks). Discipline means treating premium as an insurance cost and sizing so worthless puts can't hurt you.

## Practice problems

1. **(Conceptual)** Explain, in your own words, the two completely different reasons a trader might be long a put. For each, state whether the trader holds the underlying.

2. **(Conceptual)** Why is a long put's maximum profit *capped*, while a long call's maximum profit is *unlimited*? Give the formula for the long put's maximum profit per unit.

3. **(Numeric)** You buy one lot of **Bank Nifty 52000 PE** at a premium of **₹600**. Bank Nifty's lot size is **30**. Compute (a) your total outlay, (b) your breakeven level, (c) your maximum loss, and (d) your theoretical maximum profit.

4. **(Numeric)** Using the position in Problem 3, find your net profit or loss if Bank Nifty closes at expiry at (a) 52,300, (b) 51,400, (c) 50,000.

5. **(Numeric — protective put)** You hold a basket worth about ₹18,00,000 that tracks Nifty (75 units at 24,000) and buy one lot of the **24000 PE at ₹250** as a hedge. What is your *combined* net P&L (holding + put) if Nifty closes at (a) 22,500 and (b) 25,200? What is the worst case for the combined position?

6. **(Conceptual / risk)** Your colleague says, "I'm bearish on Nifty, so I'll buy the cheapest weekly OTM put I can find — if I'm right about the fall I'll make a fortune." Give two reasons this plan can fail even if Nifty does fall.

## Solutions

**1.** (a) **Speculation:** a bearish bet — the trader expects the market to fall and wants leveraged, loss-limited exposure to that fall. The trader holds **no underlying**; the put alone profits as prices drop. (b) **Hedging (protective put):** the trader **owns** the underlying (stocks, an ETF, or a long future) and buys the put as insurance so that if the market crashes, the put's gain offsets the holding's loss below the strike. Same instrument; in (a) it is a standalone wager, in (b) it is protection on something already owned.

**2.** A long call profits as the underlying *rises*, and a price can rise without any ceiling, so its profit is unlimited. A long put profits as the underlying *falls*, but a price can fall at most to **zero** — so the largest possible payoff is the full strike, and after subtracting the premium the cap is `maximum profit per unit = strike - premium`. The downside has a floor (zero), so the put's upside has a ceiling.

**3.** (a) Outlay = `premium * lot = 600 * 30 = ₹18,000`. (b) Breakeven = `strike - premium = 52000 - 600 = 51,400`. (c) Maximum loss = the premium paid = **₹18,000** (occurs if Bank Nifty finishes at or above 52,000). (d) Theoretical maximum profit = `(strike - premium) * lot = (52000 - 600) * 30 = 51400 * 30 = ₹15,42,000`, reached only if Bank Nifty fell to zero.

**4.** Per-unit payoff = `max(52000 - S, 0) - 600`, times 30.
- (a) **52,300:** above the strike, so `max(52000 - 52300, 0) = 0`; net per unit = `0 - 600 = -600`; total = `-600 * 30 = -₹18,000` (full premium lost).
- (b) **51,400:** intrinsic = `52000 - 51400 = 600`; net per unit = `600 - 600 = 0`; total = **₹0** (breakeven, as expected).
- (c) **50,000:** intrinsic = `52000 - 50000 = 2000`; net per unit = `2000 - 600 = 1400`; total = `1400 * 30 = +₹42,000`.

**5.** Measure changes from 24,000; holding P&L = `(S - 24000) * 75`; put payoff = `(max(24000 - S, 0) - 250) * 75`.
- (a) **22,500:** Holding = `(22500 - 24000) * 75 = -1500 * 75 = -₹1,12,500`. Put = `(1500 - 250) * 75 = 1250 * 75 = +₹93,750`. **Combined = -1,12,500 + 93,750 = -₹18,750.**
- (b) **25,200:** Holding = `(25200 - 24000) * 75 = 1200 * 75 = +₹90,000`. Put expires worthless = `-250 * 75 = -₹18,750`. **Combined = 90,000 - 18,750 = +₹71,250.**
- **Worst case:** for any close at or below the 24000 strike, the combined loss is frozen at the premium of **₹18,750**. The strike is the insured floor; below it, every further rupee of holding loss is matched rupee-for-rupee by the put's gain.

**6.** Two reasons the plan can fail despite a fall: (i) **It may not clear breakeven.** A cheap, far-OTM weekly put needs Nifty to fall *past* `strike - premium` before it nets anything; a modest dip that still finishes above breakeven leaves the put worthless and the premium lost. (ii) **Theta and timing.** A weekly put decays fast; if the fall comes a few days late — after expiry — or the market chops sideways first, time decay can wipe out the premium before the move arrives. Being right on *direction* is not enough; you must also be right on *magnitude* and *timing*, which is precisely what the cheapest weekly puts make hardest.
