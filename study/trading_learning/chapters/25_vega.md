# Chapter 25: Vega — Sensitivity to Volatility

Every option price contains a forecast about the future — specifically, a forecast about how much the underlying is going to *move*. Two traders can agree perfectly on where Nifty is today and still disagree violently on what an option is worth, because they disagree on how wild the ride to expiry will be. The price tag the market puts on that expected wildness is called **implied volatility**, and the Greek that measures how much an option's premium responds when that forecast changes is **vega**.

Vega is the Greek that catches more beginners off guard than any other. A new trader buys a Nifty call the morning of the RBI policy decision, the market moves exactly the way they predicted — and the call *loses* money. They were right on direction and still lost. The culprit, almost every time, is vega: they bought volatility when it was expensive and watched it collapse the moment the event passed. This chapter explains exactly how that happens, and how a professional turns the same mechanism into a source of edge.

## Core concepts

### What volatility means, and why "implied" is different

**Volatility** is a measure of how much a price fluctuates — formally, the annualised standard deviation of returns. A volatility of 14% on Nifty means the market expects Nifty's return over the next year to land within roughly plus-or-minus 14% about two-thirds of the time. Higher volatility means a wider range of plausible outcomes.

There are two flavours, and the difference is the whole game:

- **Realised (historical) volatility** is how much the underlying *actually* moved in the past. You compute it from the price series. It is a fact.
- **Implied volatility (IV)** is how much the market *expects* it to move in the future, backed out of current option prices. It is an opinion — a forecast embedded in the premium.

Implied volatility is the single input in the Black-Scholes-Merton formula (Chapter 20) that you cannot observe directly. You can see spot, strike, time, and rates. You cannot see "future movement." So the market *quotes* it through the option price: when traders expect a stormy period, they bid premiums up, and we say IV is high; when they expect calm, premiums sag and IV is low.

### Vega: the definition

**Vega** measures how much an option's premium changes when implied volatility changes by **one percentage point** (for example, IV moving from 14% to 15%), holding spot, time, and rates constant.

`vega = change in option premium per 1 percentage-point change in implied volatility`

If a Nifty option has a vega of ₹6, then a 1-point rise in IV (say from 13% to 14%) adds about ₹6 to its premium, and a 1-point fall subtracts about ₹6. A 3-point IV jump would move it roughly ₹18. (Vega is not perfectly linear over large IV swings, but for the 1-to-few-point moves that dominate day-to-day trading, this straight-line estimate works well.)

A small naming note: "vega" is not actually a Greek letter — the other sensitivities borrowed real Greek names (delta, gamma, theta, rho) and vega just joined the club. Do not let the odd name fool you; it is one of the most important numbers on the screen.

### The key fact: vega has the SAME sign for calls and puts

This is the single most important and most counter-intuitive fact about vega, so sit with it.

**Long options — both calls and puts — have positive vega. Short options have negative vega. The sign does not depend on whether it is a call or a put.**

Why? Volatility is about the *width* of the range of possible outcomes, not its direction. More volatility means the underlying could end up much higher *or* much lower. An option is a one-sided bet: a call profits from big up-moves and loses nothing extra from big down-moves (you just lose your premium either way); a put profits from big down-moves and is indifferent to big up-moves. Either way, **a wider range of outcomes can only help the owner of an option**, because the downside is capped at the premium paid while the upside grows. More volatility means more chance of a large favourable move, with no extra penalty for a large unfavourable one.

So more volatility makes *every* option — call or put — more valuable to its owner. That is why:

- If you are **long** a call or a put, you are **long vega**: rising IV helps you, falling IV hurts you.
- If you are **short** a call or a put, you are **short vega**: rising IV hurts you, falling IV helps you.

Contrast this with delta, where calls and puts pull in opposite directions. With vega there is no such split. A long straddle (long a call *and* a put together) is doubly long vega — it is almost a pure volatility bet, with the directional exposures of the two legs roughly cancelling while their vegas add.

### Where vega is biggest: at-the-money and longer-dated options

Vega is not the same size for every option. Two patterns matter enormously in practice.

**1. Vega is highest at-the-money (ATM).** An option's premium is most sensitive to volatility when the strike sits right at the current spot. The intuition: an ATM option is on a knife-edge — it could easily finish in-the-money or out-of-the-money, so the question "how much will it move?" matters most to its fate. Widening or narrowing the range of outcomes shifts its odds the most. Now take a deep in-the-money or deep out-of-the-money option. A deep ITM option is almost certain to finish ITM; a deep OTM option is almost certain to expire worthless. For both, a small change in expected movement barely moves their near-settled odds, so their vega is small. Vega, plotted against spot, is a hump that peaks at the strike and tapers off on both sides.

**2. Vega is highest for longer-dated options.** The more time an option has, the more room volatility has to act, so the more a change in the *rate* of movement matters. A one-percentage-point rise in annual IV has far more time to compound its effect over a 90-day option than over a 2-day weekly. Roughly, vega scales with the square root of time to expiry, `vega proportional to sqrt(T)`. This is why a far-month Nifty option reacts much more dramatically in rupee terms to an IV shift than a same-strike weekly — and why, conversely, a Tuesday-of-expiry weekly has tiny vega even though its gamma and theta are screaming.

Hold those two facts together: **the most vega-sensitive option on the board is a longer-dated at-the-money option.** That is the instrument professionals reach for when they want to bet on volatility itself.

![Figure: vega vs spot](figs/vega.png)

The figure plots vega against the spot price. Notice the single hump peaking at the strike (maximum vega at-the-money), the symmetric tapering as the option goes deep ITM or deep OTM, and the fact that the entire curve sits higher and broader for the longer-dated option than for the short-dated one. The same picture works for calls and puts — because vega does not care which it is.

### IV crush: the trap that catches every beginner

Here is the real-world phenomenon that turns vega from a textbook abstraction into a lesson paid for in cash.

Implied volatility is a forecast of *future* movement — so it rises when the market knows a big, uncertain event is coming. Ahead of an event, nobody knows the outcome, so the range of possible results is wide, IV spikes, and option premiums fatten. The instant the event passes and the uncertainty resolves, that forecast of future movement collapses — there is no longer a mystery to price — and IV falls hard. Premiums deflate. This sudden post-event collapse in implied volatility is called **IV crush** (or "volatility crush").

In Indian markets the classic IV-crush events are:

- **Quarterly results** of individual stocks (Reliance, Infosys, HDFC Bank). Stock-option IV ramps up for days before earnings and craters the morning after.
- **The Union Budget** (typically February 1), which can reprice entire sectors.
- **RBI monetary policy** decisions (the MPC meetings), which move rates, banks, and the rupee.
- **General and key state election results**, which can swing the whole index.
- **US Fed decisions and major global data**, which spill into Nifty through global risk sentiment.

The mechanism that burns beginners: ahead of such an event, India VIX (and the IV of the relevant options) climbs, so options are *expensive*. A beginner who buys a call or put is paying a premium inflated by high IV. When the event passes, IV crushes. Even if the underlying moved in the predicted direction, the vega loss from the IV collapse can exceed the delta gain from being right. **You can be correct on direction and still lose money**, because you overpaid for volatility that then evaporated.

This is not a rare edge case. It is one of the most common ways retail option *buyers* lose, and it is precisely why so many professionals prefer to be *sellers* of volatility into events — they are the ones collecting the inflated premium and pocketing the crush.

### India VIX: the market's fear gauge

To trade vega intelligently you need a way to *see* the overall level of implied volatility. In India, that instrument is the **India VIX**.

India VIX is an index published by the NSE that measures the market's expectation of Nifty volatility over the **next 30 calendar days**, derived from the prices of near-month Nifty options. It is quoted as an annualised percentage. Read it like a thermometer:

- **Low India VIX (say 10–13)** — the market is calm and complacent; options are cheap; IV is low. A poor time to *buy* options on vega grounds, a relatively attractive time to be selling (small premiums, but low crush risk).
- **High India VIX (say 20–30+)** — fear and uncertainty; options are expensive; IV is high, often ahead of or during an event or a sell-off. Dangerous to buy (crush risk), potentially rewarding but risky to sell.

India VIX tends to **spike before known events and around sharp market falls** (it is sometimes called the "fear gauge" because it jumps when markets drop), and to **drift back down** once the uncertainty clears — the index-level fingerprint of IV crush. A professional checks India VIX before every trade the way a sailor checks the wind: it tells you whether volatility is cheap or dear *right now*, which decides whether you want to own vega or sell it.

### Trading volatility directly

Once you understand vega, a new dimension of trading opens up: you can take a view on **volatility itself**, almost independently of direction.

- **Long vega (buy volatility) when IV is cheap.** If India VIX is low and you believe the market is underpricing future turbulence — a quiet market before a known catalyst, say — you buy options (or a long straddle/strangle) to be long vega. You profit if IV rises, even if the underlying barely moves.
- **Short vega (sell volatility) when IV is rich.** If India VIX is elevated and you believe the market is overpricing future movement — classically, into an event where premiums are bloated — you *sell* options (a short straddle/strangle, or spreads) to be short vega. You profit as IV crushes back down, collecting the deflating premium. This is the professional's favourite side of the event trade, but its risk is large and, for naked short options, theoretically unlimited.

The cleanest pure-vega structures combine a call and a put so the directional deltas roughly cancel and the vega adds: a **long straddle** is a bet that volatility (realised or implied) will be higher than the market thinks; a **short straddle** is the opposite. These are covered in their own chapters, but the engine underneath them is vega.

The professional framing: do not just ask "will Nifty go up or down?" Ask "is volatility cheap or expensive relative to what's coming?" That second question is the one most retail traders never even pose — and it is the one that separates a volatility trader from a coin-flipper.

## Worked example (₹, Nifty)

Let us put rupees on IV crush so the trap is unmistakable.

**Setup.** It is the day before the RBI monetary policy announcement. Nifty spot is **24,000**. You expect Nifty to rise, so you buy the **ATM 24,000 weekly call**, 3 days to expiry. Because the market is bracing for the RBI decision, India VIX is elevated at **20%**, and at that IV the call is priced at **₹150**. Suppose this call has a **delta of about 0.5** and a **vega of about ₹8**.

**Step 1 — The event happens, and you are right on direction.** The next morning the RBI delivers a mildly dovish surprise and Nifty rises **60 points**, from 24,000 to 24,060. The delta gain on your call is approximately:

`delta P&L ≈ delta * move = 0.5 * 60 = ₹30`

So on direction alone, the call should be worth about ₹180. So far, so good.

**Step 2 — But IV crushes.** With the RBI decision now known, the big uncertainty is gone. India VIX collapses from 20% to **13%** — a 7-point drop in implied volatility. The vega loss is:

`vega P&L ≈ vega * change in IV = 8 * (-7) = -₹56`

**Step 3 — Net result.** Combine the two effects:

`new premium ≈ 150 + 30 (delta) - 56 (vega) ≈ ₹124`

Your call, bought at ₹150, is now worth about **₹124 — a loss of ₹26 per unit even though Nifty moved exactly the way you predicted.** On one lot (Nifty lot size currently around 75 units), that is roughly `26 * 75 ≈ ₹1,950` gone, while you were *right*. The IV crush (−₹56) overwhelmed the directional gain (+₹30). This is the beginner's heartbreak, quantified.

**Step 4 — The other side of the trade.** Now flip it. Suppose instead you had *sold* that 24,000 straddle (call plus put) the evening before, collecting fat premiums inflated by 20% IV. The same IV crush that cost the buyer ₹56 of vega per option works *in your favour* as a seller — you are short vega. As long as Nifty's actual move stays modest (and 60 points is modest), the collapse in IV lets you buy the options back far cheaper than you sold them. The crush that punished the buyer paid the seller. **Same event, opposite vega sign, opposite outcome** — which is the whole reason professionals so often want to be the seller into a known event.

## Common mistakes / risk note

- **Buying options right before a big event "because something will happen."** Something does happen — IV crush. You are buying premium inflated by high IV, and the post-event collapse can wipe out your directional gain. If you must take a directional view into an event, understand that you need the move to be *large enough* to overcome the vega loss, not just correct in direction.
- **Thinking puts and calls react oppositely to volatility.** They do not. Both long calls and long puts *gain* when IV rises. Vega has the same sign for both; only delta flips. Beginners who "hedge" a long call by buying a put discover both legs bleed vega together when IV falls.
- **Ignoring India VIX before entering.** Trading options without checking the VIX is like buying a flight ticket without checking the price — you have no idea whether volatility is cheap or expensive, so you cannot know if you are overpaying. Always know whether you are buying or selling vega, and whether IV is high or low when you do it.
- **Treating short vega as free money.** Selling options into high IV to harvest the crush is a real professional strategy, but it carries large — and for naked options, theoretically unlimited — risk. If the event delivers a *bigger* move than priced, or IV spikes even further, the short-vega seller can lose multiples of the premium collected. The crush is an edge, not a guarantee.
- **Forgetting that vega shrinks into expiry.** A Tuesday-of-expiry weekly has tiny vega; its life is dominated by gamma and theta. Do not expect a vega play to work on a near-dead option — use longer-dated, at-the-money options when you genuinely want volatility exposure.

## Key takeaways

- **Vega** measures the change in an option's premium per **1 percentage-point change in implied volatility**, holding everything else constant.
- **Vega has the same sign for calls and puts**: long options are long vega (gain when IV rises), short options are short vega (gain when IV falls). Only delta flips between calls and puts — vega does not.
- **Vega is largest at-the-money and for longer-dated options**; it scales roughly with `sqrt(T)` and is tiny for deep ITM/OTM and near-expiry options.
- **IV crush**: implied volatility spikes before events (results, Budget, RBI policy, elections) and collapses right after, so a long option can lose money *even when the direction was right*.
- **India VIX** is the 30-day implied-volatility gauge for Nifty — your thermometer for whether options are cheap (low VIX) or expensive (high VIX) before you trade.
- **Trade volatility directly**: be long vega when IV is cheap, short vega when IV is rich; straddles/strangles are the cleanest near-pure vega structures.
- Always ask not just "up or down?" but **"is volatility cheap or expensive relative to what's coming?"** Short vega harvests crush but carries large, sometimes unlimited, risk.

## Practice problems

1. **Sign check.** You are long one Nifty 24,000 call and, separately, long one Nifty 24,000 put. India VIX jumps from 14% to 18% overnight with Nifty unchanged. What happens to the value of each position, and why does the call not gain while the put loses?

2. **The crush, conceptually.** A friend says: "I bought a Reliance call before earnings, the stock jumped 2% on great results, but my call still lost money. The broker must have cheated me." Explain in plain English what actually happened, naming the phenomenon and the Greek responsible.

3. **Vega magnitude (numeric).** A Nifty option has a vega of ₹7. India VIX falls from 19% to 12% after the Union Budget. Estimate the vega-driven change in the option's premium. If you were *long* the option, is this gain or loss?

4. **Right direction, wrong trade (numeric).** You buy an ATM Nifty 24,000 call at ₹160 ahead of an event, with delta 0.5 and vega ₹9. The event passes: Nifty rises 40 points and IV drops 8 points. Estimate the new premium and your P&L per unit. Were you right on direction? Did you make money?

5. **Where is vega biggest?** You want a near-pure bet that volatility will rise over the next month, with as little directional exposure as possible. Which of these would you choose and why: (a) a deep ITM weekly call, (b) a far OTM weekly put, (c) an ATM 90-day straddle?

6. **Reading the VIX.** India VIX is sitting at 11%, near multi-month lows, and a national election result is due in three weeks. You believe markets are underpricing the turbulence. Are you a natural *buyer* or *seller* of vega here, and what is the main risk to your view?

## Solutions

1. **Both gain.** Vega has the same sign for calls and puts, so a long call and a long put are *both* long vega. When India VIX rises from 14% to 18%, implied volatility is up 4 points, and **both** options gain value — the call does *not* sit still and the put does *not* lose. Volatility measures the width of the outcome range, not its direction, and a wider range helps the owner of either option (more chance of a big favourable move, downside capped at premium). Only delta would distinguish them; vega treats them identically.

2. **IV crush.** Reliance option IV ramped up ahead of earnings (uncertainty about the result), inflating the call's premium. Your friend bought that expensive, high-IV premium. When results came out, the uncertainty resolved and **implied volatility crushed** — collapsed sharply. The friend was **long vega**, so the IV collapse cost them money, and that vega loss exceeded the delta gain from the stock's 2% rise. They were right on direction but overpaid for volatility that then evaporated. No cheating — just vega and IV crush. The lesson: buying options into an event means fighting the crush.

3. The IV change is `12 - 19 = -7` percentage points. Vega-driven change `≈ vega * change in IV = 7 * (-7) = -₹49`. If you are **long** the option you are long vega, so a falling IV is a **loss** of about ₹49 per unit (before any delta/theta effects). This is the IV-crush mechanism in numbers — a Budget-day classic.

4. Delta P&L `≈ 0.5 * 40 = +₹20`. Vega P&L `≈ 9 * (-8) = -₹72`. New premium `≈ 160 + 20 - 72 = ₹108`. P&L `≈ 108 - 160 = -₹52` per unit (about `52 * 75 ≈ ₹3,900` loss on one lot of 75). **Yes, you were right on direction** (Nifty rose), but you **lost money**: the vega loss from IV crush (−₹72) swamped the directional gain (+₹20). This is exactly why buying options into an event is dangerous even with a correct view — the move has to be big enough to beat the crush.

5. **(c), the ATM 90-day straddle.** Vega is largest **at-the-money** and for **longer-dated** options, so a 90-day ATM option has far more vega than any weekly. A straddle (call + put) makes the directional deltas roughly cancel while the two vegas add, giving you a near-pure long-volatility bet. Option (a), a deep ITM weekly, has small vega (deep ITM, near expiry) and large directional delta — the opposite of what you want. Option (b), a far OTM weekly, also has small vega (far OTM, near expiry) and is mostly a long-shot directional punt. Only (c) maximises vega while minimising direction.

6. **A natural buyer of vega (long volatility).** India VIX at 11% means implied volatility — and hence option premiums — is cheap, while a known catalyst (the election result) sits three weeks out that could spike volatility. Buying options (e.g., a longer-dated ATM straddle) makes you long vega, profiting if IV rises toward the event as you expect. **The main risk: theta (time decay).** While you wait for IV to rise, your long options bleed premium every day, and if the market stays calm and IV does not climb, that decay can cost you more than the eventual vega gain. There is also the risk that the event resolves into a *fall* in IV (a "sell the news" crush) if it arrives without surprise. Being long vega is not free — you pay for it in theta and in the chance the volatility rise never comes.
