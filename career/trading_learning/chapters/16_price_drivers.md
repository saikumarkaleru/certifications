# Chapter 16: What Drives an Option's Price — The Six Factors

An option's premium can feel like a number pulled out of thin air. One day the Nifty 24,000 call costs ₹120; the index barely moves overnight and the next morning it is ₹95; an event passes and it gaps to ₹140 even though the index is flat. To a beginner this looks like chaos. It is not. The premium of any option is driven by exactly **six inputs**, and once you know what they are and which direction each one pushes the price, the "chaos" turns into a small set of levers you can track on your screen.

This chapter is the master map for everything that follows. The six factors are the **spot price** of the underlying, the **strike price**, the **time to expiry**, the **volatility**, the **interest rate**, and the **dividends**. We will build the intuition for each one, learn the direction it pushes calls and puts, collect it all into one clean table you can memorise, and then — crucially — show how these same six factors become the **Greeks** in Part IV. The Greeks are not a new subject; they are just the *speeds* at which the premium responds to these six levers.

## Core concepts

### The premium is a function of six things

Every option-pricing model ever built — the Black-Scholes-Merton formula, the binomial tree, and the engines NSE brokers run behind your option chain — takes the same six ingredients and returns one number, the fair premium:

`Premium = f(Spot S, Strike K, Time to expiry T, Volatility sigma, Interest rate r, Dividend d)`

Five of these six change in real time or are knowable in advance; only one (the strike) is fixed the moment you choose your contract. The skill of an options trader is largely the skill of watching the *other five* and knowing, for the position you hold, whether each one is currently working for you or against you.

Two of the six (spot and volatility) are the ones traders obsess over because they move the most. Time is the silent one that works against buyers every day. Interest rate and dividends are gentle background forces — small for weekly Nifty options, but real, and the reason calls and puts are never perfectly symmetric. Let us take them one at a time.

### Factor 1 — Underlying spot price (S)

The spot price is the current level of the underlying — Nifty at 24,000, Bank Nifty at 52,000. This is the single biggest driver of premium because the option's whole payoff is defined relative to it.

- A **call** is the right to *buy* at the strike. The higher the spot climbs above the strike, the more that right is worth. So **spot up → call premium up.** It is the most intuitive relationship in all of options: if the thing you have the right to buy gets more expensive, your right to buy it cheaply is worth more.
- A **put** is the right to *sell* at the strike. The higher the spot, the *less* valuable the right to sell at a fixed price. So **spot up → put premium down**, and **spot down → put premium up.**

Think of a call buyer as someone cheering for the index, and a put buyer as someone cheering against it. Spot is the scoreboard, and it moves both their premiums in opposite directions. The *speed* of this response is the Greek **delta**, and how that speed itself changes is **gamma** — both previewed below.

### Factor 2 — Strike price (K)

The strike is the agreed price in the contract. Unlike the other five factors, it does not move; you lock it in when you pick the option. But comparing options *across* strikes shows its effect clearly.

- For **calls**, a *lower* strike is more valuable (you get to buy cheaper), so **lower strike → higher call premium.** A 23,800 call costs more than a 24,200 call when spot is 24,000.
- For **puts**, a *higher* strike is more valuable (you get to sell dearer), so **higher strike → higher put premium.** A 24,200 put costs more than a 23,800 put.

Strike and spot really work as a pair: what matters is the *distance and direction* between them — the **moneyness** (covered in Chapter 5). A call with spot far above the strike is deep in-the-money and expensive; the same strike with spot far below is out-of-the-money and cheap. So when people say "spot drives the premium," they really mean "the gap between spot and the fixed strike drives the premium."

### Factor 3 — Time to expiry (T)

Time is the factor every option buyer underestimates. More time until expiry means more opportunity for the underlying to move in your favour before the contract dies. That extra opportunity is worth money — to *both* calls and puts.

- **More time → higher call premium AND higher put premium.** A 30-day option is worth more than a 1-day option at the same strike, because anything can happen in 30 days and almost nothing can happen in one. This is the rare factor that pushes calls and puts the *same* direction.

The honest flip side: time only flows one way. Every day that passes, an option loses a slice of this time value, and that decay *accelerates* as expiry nears — brutal for India's hugely popular **weekly** Nifty and Bank Nifty options, which live entirely in the steep part of the decay curve. The premium an option loses purely from one day passing is the Greek **theta**, and for an option buyer theta is a daily headwind: you can be right about direction and still lose if you were not right *fast enough*. (Chapter 6 split the premium into intrinsic and time value; time is the factor that governs the time-value half.)

### Factor 4 — Volatility (sigma)

Volatility is how much the underlying is expected to swing, regardless of direction. It is the factor that separates amateurs from professionals, because it is invisible on a price chart yet it can dominate the premium. In India, the market's expected near-term volatility is summarised by **India VIX** — when VIX jumps, option premiums across the board inflate; when it collapses (often right after a big event), they deflate.

- **Higher volatility → higher call premium AND higher put premium.** Like time, volatility helps *both* sides, because both calls and puts have one-sided payoffs: bigger expected swings mean a fatter chance of a large favourable move, while the loss stays capped at the premium paid. You are paying for the right tail; more volatility means a fatter right tail.

A vivid way to feel this: imagine insuring two cars, one driven calmly on the highway and one driven recklessly through crowded lanes. The reckless car (high volatility) is more likely to produce a big claim, so its insurance premium is higher — for *both* the dent cover and the theft cover. An option is insurance, and volatility is how reckless the underlying is expected to drive. The premium's sensitivity to volatility is the Greek **vega**.

The trap, again stated honestly: traders constantly buy options before an expected event (a budget, an RBI policy, election results) when volatility — and therefore the premium — is already pumped up. The event passes, India VIX deflates, and the option loses value even if the index moved their way. This "volatility crush" is one of the most common ways retail buyers lose money while being "right."

### Factor 5 — Interest rate (r)

Now the two gentle background factors. The risk-free interest rate is the return on safe money (think the rate on government treasury bills) over the life of the option. Its effect is small for short-dated options but it is real, and it pushes calls and puts in *opposite* directions.

- **Higher interest rate → higher call premium, lower put premium.**

The cleanest intuition uses the idea of a substitute. Buying a call instead of buying the index outright lets you control the same upside while parking most of your cash in the bank earning interest. The higher that interest rate, the more valuable this "buy the call, keep the cash earning" deal is — so the call is worth more. The mirror argument: a put is like delaying the *receipt* of cash from a sale (you sell later at the strike). The higher the interest rate, the more it costs you to wait for that money, so the put is worth less. The premium's sensitivity to interest rates is the Greek **rho**, the smallest of the major Greeks for short-dated index options.

### Factor 6 — Dividends (d)

The last factor matters when the underlying pays dividends over the life of the option. A stock (or the basket of stocks inside an index) drops in price by roughly the dividend amount when it goes ex-dividend, because that cash leaves the company. An option holder does *not* receive that dividend — only the actual shareholder does. So expected dividends pull the *future* spot down, which hurts calls and helps puts.

- **Higher expected dividends → lower call premium, higher put premium.**

Note the neat symmetry: dividends push premiums in the *opposite* direction to interest rates. Higher rates help calls and hurt puts; higher dividends hurt calls and help puts. They are two sides of the same "cost of carrying the underlying" coin. For weekly **Nifty** options the dividend effect is tiny (only the handful of index stocks going ex-dividend that week matter), but for **single-stock** options around a big dividend it can be meaningful, and there is no single standard Greek for it on a retail screen — it is folded into the model's forward price.

### The master table: which way each factor pushes

Here is the whole chapter in one grid. "Up" means the factor increasing; the arrows show what happens to each premium, holding the other five factors constant.

| Factor increases | Call premium | Put premium | Why (one line) |
|---|---|---|---|
| **Spot price S** up | **Up** | **Down** | Right to buy worth more; right to sell worth less |
| **Strike price K** up | **Down** | **Up** | Buying dearer is worse for calls, selling dearer is better for puts |
| **Time to expiry T** up | **Up** | **Up** | More time = more chance to move favourably (helps both) |
| **Volatility sigma** up | **Up** | **Up** | Bigger expected swings, capped downside (helps both) |
| **Interest rate r** up | **Up** | **Down** | Call lets you keep cash earning; put delays receiving cash |
| **Dividends d** up | **Down** | **Up** | Dividends pull future spot down; hurts calls, helps puts |

Memorise the shape, not just the cells. **Time and volatility are the two "friends of both"** — they raise calls and puts together because both buy *possibility*. **Spot, rate, and dividend are the three "splitters"** — they help one side and hurt the other. The strike is the one factor you fix yourself.

### How the six factors become the Greeks (Part IV preview)

The six factors tell you the *direction* a premium moves. The **Greeks**, coming in Part IV, tell you the *amount* — they are the measured sensitivity of the premium to each factor. Every Greek is just "rate of change of premium with respect to one of these six inputs." Here is the bridge:

| The factor that moves | The Greek that measures it | Plain meaning |
|---|---|---|
| Spot price S | **delta** | Premium change per 1-point move in the underlying |
| Spot price S (again) | **gamma** | How fast delta itself changes as spot moves |
| Time to expiry T | **theta** | Premium lost per one day passing |
| Volatility sigma | **vega** | Premium change per 1% change in volatility (India VIX) |
| Interest rate r | **rho** | Premium change per 1% change in interest rates |

Notice spot earns *two* Greeks: delta (the first-order speed) and gamma (the acceleration), because spot is the dominant driver and traders need to track both its speed and how that speed changes. Dividends are the one factor without a standard retail Greek — they enter through the model's forward price rather than a dashboard number. Keep this table in your head and Part IV will feel like detail being filled into a frame you already own, not a new language.

## Worked example (₹, Nifty/Bank Nifty)

Start from a base case and change **one factor at a time**, watching the premium of a single contract respond. This is exactly how a pricing model "thinks," and it is the most useful mental drill in options.

**Base case.** Nifty spot **S = 24,000**, we look at the **24,000 call (ATM)** and the **24,000 put (ATM)**, with about 7 days to a weekly expiry, India VIX around 13. Suppose the model gives:

- 24,000 call ≈ **₹120**
- 24,000 put ≈ **₹110**

(The call is slightly richer than the put here mainly because of the positive interest-rate effect — a real, if small, asymmetry.)

Now flick each lever:

**1) Spot rises to 24,100 (+100 points), everything else held.**
The call gains value (right to buy at 24,000 is now more valuable) — it might rise from ₹120 to about **₹175**. The put loses value — it might fall from ₹110 to about **₹70**. Spot is a *splitter*: call up, put down. The call did not gain the full 100 points because it is ATM and its delta is only about 0.5 — it captures roughly half the move. That ~0.5 is delta in action.

**2) Back to base, then volatility jumps — India VIX 13 → 20.**
A volatility spike inflates *both* premiums even with spot pinned at 24,000. The call might rise from ₹120 to about **₹165** and the put from ₹110 to about **₹155**. Both up — volatility is a *friend of both*. The size of that jump per unit of volatility is vega. This is precisely the "premium gaps up while the index is flat" mystery from the chapter's opening: someone re-priced volatility.

**3) Back to base, then one quiet day passes — time 7 days → 6 days, spot unchanged.**
Pure time decay. Both ATM premiums slip: the call from ₹120 to about **₹108**, the put from ₹110 to about **₹99**. Both *down* — time is the mirror of volatility, draining possibility from both sides. The ~₹11-₹12 lost in a single flat day is theta, and on a Nifty lot of about 75 units that is roughly `12 * 75 = ₹900` gone per lot, per quiet day, for the *buyer* — and collected by the *seller*. (Lot sizes are set by the exchange and change from time to time.)

**4) Back to base, then interest rates rise.**
A *splitter*, and a gentle one: the call ticks *up* a rupee or two, the put *down* a rupee or two. For a 7-day Nifty option this rho effect is almost invisible — which is why rho is the Greek you worry about least for weekly trades and more for long-dated positions.

**5) Back to base, then index dividends go ex this week.**
The opposite splitter: expected dividends nudge the *future* index down, so the call eases *down* slightly and the put edges *up* slightly. Tiny for a weekly Nifty option; potentially material for a single stock around a fat dividend.

Step back and read the pattern across all five flicks. The two big, fast levers were **spot** (moved the premiums tens of rupees and in opposite directions) and **volatility** (moved both the same way by a large amount). **Time** quietly bled both. **Rate and dividend** barely registered for a weekly contract but pointed in opposite, predictable directions. That is the entire personality of an option premium in one experiment.

## Common mistakes / risk note

- **Watching only spot.** Beginners track the index and ignore the other five factors. You can be exactly right on direction and still lose money to time decay (theta) or a volatility crush (falling vega effect). Spot is the loudest lever, not the only one.
- **Buying options when volatility is already high.** Before budgets, RBI policy, and results, India VIX and premiums are pumped up. After the event, volatility deflates and the premium sags even if the index moved your way. Check whether volatility is rich *before* you buy.
- **Forgetting that time helps the seller exactly as much as it hurts the buyer.** Every rupee of time value the buyer loses, the seller gains. This is structural, not luck — and it is a core reason SEBI studies find roughly **9 in 10 retail F&O traders lose money.** It does not make buying wrong; it makes *overpaying for time and volatility, then holding too long*, wrong.
- **Treating calls and puts as mirror images.** They are not perfectly symmetric, precisely because of the interest-rate and dividend factors. At the same strike with spot on the strike, the call is usually worth slightly more than the put.
- **Thinking the Greeks are a separate, harder subject.** They are just the measured speeds of these same six factors. If you understand the table above, you already understand what every Greek is *for*.
- **The seller's honest risk.** Collecting time value by selling options is not free money. The decay tailwind is real, but a naked seller's loss is large and, for an uncovered option, effectively undefined. The same six factors that bleed the buyer can gap violently against the seller when spot jumps and volatility spikes together.

## Key takeaways

- An option's premium is driven by exactly six factors: **spot S, strike K, time to expiry T, volatility sigma, interest rate r, and dividends d.**
- **Spot up → call up, put down.** **Strike up → call down, put up.** These work as a pair (moneyness).
- **Time and volatility help BOTH calls and puts** — they buy possibility. They are the two "friends of both."
- **Interest rate and dividends are opposite splitters:** higher rates help calls and hurt puts; higher dividends hurt calls and help puts.
- The factors give *direction*; the **Greeks give magnitude**: spot → delta and gamma, time → theta, volatility → vega, interest rate → rho. Dividends have no standard retail Greek.
- For weekly Nifty/Bank Nifty options, **spot and volatility dominate**, time quietly bleeds buyers, and rate/dividend effects are tiny — so watch the first two relentlessly.

## Practice problems

1. **(Conceptual)** India VIX jumps from 12 to 18 over a single session while Nifty closes exactly flat. What happens to the premium of an ATM Nifty call and an ATM Nifty put, and why?

2. **(Conceptual)** Name the two factors that push a *call* and a *put* in the *same* direction, and explain in one sentence why they affect both the same way.

3. **(Numeric/Direction)** Bank Nifty is at 52,000. For each change below, state whether the 52,000 **call** premium rises or falls, holding everything else constant: (a) spot moves to 52,300; (b) three days pass; (c) India VIX falls from 16 to 11; (d) interest rates rise.

4. **(Conceptual)** Two traders hold the same Nifty 24,000 call into a major event. After the event Nifty is up 80 points but the call is *cheaper* than before. Give the most likely single explanation using the six factors.

5. **(Mapping)** For each Greek — delta, theta, vega, rho — name the factor it measures, and state whether that factor moving up helps or hurts a long *put*.

6. **(Conceptual)** Why is a call usually worth slightly more than a put at the same strike when spot equals the strike? Which two of the six factors are responsible, and which one dominates for a 7-day Nifty option?

## Solutions

**1.** Volatility is a "friend of both." A jump in India VIX from 12 to 18 raises the time-value portion of *both* premiums even though spot did not move, so **both the ATM call and the ATM put rise.** Bigger expected swings make each one-sided payoff more valuable while the downside stays capped at the premium. This is the classic "premiums inflate on a flat day" effect, and its measure is vega.

**2.** **Time to expiry and volatility.** Both raise call and put premiums together because both buy *possibility* — more time, or more expected movement, increases the chance the underlying makes a large favourable move, while the buyer's loss stays capped at the premium. Possibility is valuable to either side of the trade.

**3.** For a **call**:
- (a) Spot up to 52,300 → call **rises** (right to buy at 52,000 is more valuable; spot up helps calls).
- (b) Three days pass → call **falls** (time decay / theta drains time value).
- (c) India VIX 16 → 11 → call **falls** (lower volatility shrinks time value; a vega-driven drop).
- (d) Interest rates rise → call **rises** slightly (positive rho for calls, though small for short-dated options).

**4.** The most likely culprit is a **volatility crush.** Before the event India VIX (and the option's implied volatility) was elevated, pumping up the premium. After the event the uncertainty resolved, volatility collapsed, and the lost vega value outweighed the modest 80-point favourable move in spot — so the call got cheaper despite the trader being "right" on direction. (A secondary contributor is the time value lost as the event day passed: theta.)

**5.**
- **delta** measures **spot price**; spot up *hurts* a long put (put premium falls as spot rises).
- **theta** measures **time to expiry**; time passing *hurts* a long put (it loses time value, like any long option).
- **vega** measures **volatility**; volatility up *helps* a long put (higher premium).
- **rho** measures **interest rate**; interest rate up *hurts* a long put (higher rates lower put premiums).

**6.** The asymmetry comes from the **interest-rate and dividend** factors — the two "splitters" that affect calls and puts oppositely. Higher interest rates lift calls and depress puts (you can hold a call and keep your cash earning interest), while dividends do the reverse. For a **7-day Nifty** option, dividends over that short window are usually negligible, so the **interest-rate effect dominates**, leaving the call worth slightly more than the put at the same at-the-money strike. The gap is small, but it is why calls and puts are never perfect mirror images.
