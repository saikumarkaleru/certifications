# Chapter 56: Event Trading — Results, Budget, RBI Policy & Expiry

Markets do not move at a constant drip. Most of the action — most of the *surprise* — is bunched around a handful of scheduled moments: a company posts its quarterly results, the Finance Minister reads the Union Budget, the RBI's rate-setting committee announces its decision, an election result is counted, the US Fed speaks, and every week another expiry rolls around. On the calendar, everyone knows these dates weeks in advance. And precisely *because* everyone knows, the options market does something remarkable in the days before: it gets *expensive*. Implied volatility — the market's priced-in expectation of how much the underlying will move — climbs into the event like water rising behind a dam. Then the announcement lands, the uncertainty resolves in a single instant, and the dam bursts: IV collapses, often violently, in the first seconds of trading after. Traders call this the **IV crush** (or "volatility crush"), and it is the single most important phenomenon in event trading.

This chapter is about reading that rhythm and positioning for it. The core insight is brutally simple to state and surprisingly hard to act on: *the event being big is already in the price.* A long option bought the day before a result is not cheap just because a huge move is "coming" — you are paying full price for that expected move, and if the actual move is anything less than spectacular, the IV crush hands you a loss even when you guessed the direction right. Option *sellers*, meanwhile, are paid handsomely to absorb that pre-event fear — but they carry the matching danger that the event produces a genuine gap that blows through their risk. Event trading is the discipline of knowing which side of that trade the odds favour, and when the honest answer is "neither — stay flat."

## Core concepts

### The universal pattern: IV rises into an event, crushes after

Every scheduled event follows the same volatility arc, and internalising it is 80% of the skill:

1. **Days before:** implied volatility on the affected strikes drifts *up*. Nobody wants to be short cheap insurance going into a known catalyst, so option prices get bid up. India VIX (the index of Nifty option-implied volatility) rises into Budget day, election counting day, big RBI meetings.
2. **The instant after the announcement:** the unknown becomes known. The reason to hold expensive insurance evaporates, and IV *crushes* — frequently dropping several volatility points in minutes, sometimes 20–40% of its value on single-stock results.
3. **The underlying itself** may gap, drift, or barely budge — that part is genuinely uncertain. But the *volatility* almost always falls. The move's *magnitude* is the gamble; the IV crush is nearly a sure thing.

Think of it as the price of an umbrella. The day before a forecast storm, umbrellas are dear — everyone wants one. The moment the storm passes (or fizzles), umbrellas are worthless even if it rained, because nobody needs *tomorrow's* umbrella anymore. You can be completely right that it would rain and still lose money buying umbrellas at the panic price.

### What the crush does to buyers vs sellers

An option's premium has two enemies and one friend for each side. Recall vega — the sensitivity of an option's price to a one-point change in implied volatility. Long options are **long vega** (they gain when IV rises, lose when it falls); short options are **short vega** (the mirror).

- **The option buyer** pays inflated, high-IV premium going in. After the event, two forces hit at once: the IV crush (vega working against them) and, on a long straddle/strangle, the fact that *both* legs can't win. To profit, the buyer needs the underlying to move *more* than the pumped-up IV already paid for. That is a high bar.
- **The option seller** collects that inflated premium and is positioned for the crush. If the underlying behaves — moves less than priced — the seller harvests both the IV collapse (short vega paying off) and the post-event theta. The danger is the fat tail: a genuine surprise that gaps the underlying past the seller's cushion.

This is the central tension of event trading. Buyers are betting the move *exceeds* what's priced; sellers are betting it *falls short*. The IV crush systematically tilts the field toward sellers — which is exactly why selling into events is popular, and exactly why it occasionally detonates.

### The trap: "IV is already pumped"

The most common beginner error is buying a straddle the afternoon before results "because a big move is coming." The big move *is* coming — and it's already in the premium. If a stock's options are pricing an 8% post-results move and the stock moves 5%, the long straddle *loses* despite a 5% move, because the IV crush deflates both legs faster than the 5% move inflates the winning one.

So the buyer's only real edge is to buy **before IV has pumped up** — early, when implied volatility is still cheap relative to the looming catalyst — and let the rising IV (long vega) work *for* you into the event, then sell *before* the announcement. That is a volatility trade, not a direction trade: you're buying cheap vol and selling expensive vol, exiting before the crush. Buying expensive vol the day before is the trap.

### IV rank and IV percentile: is it actually cheap or expensive?

You cannot judge "cheap" or "expensive" by the raw IV number — 18% IV is high for a sleepy stock and low for a volatile one. Use **IV rank** or **IV percentile**, which place today's IV on its own one-year range:

`IV rank = (current IV - 1yr low IV) / (1yr high IV - 1yr low IV)`

An IV rank near 0 means IV is near its yearly floor (options relatively cheap — favours *buying* premium / debit structures). Near 1 means IV is near its yearly ceiling (options dear — favours *selling* premium / credit structures). Going into a known event, IV rank is usually elevated; the seller's edge is strongest when it is *extremely* elevated, because the post-event crush back toward normal is then largest.

### The four playbooks

There are really only four sensible responses to a scheduled event:

**1. Buy premium BEFORE IV pumps (long vol, exit before the event).** Only when IV is still cheap (low IV rank) days ahead. A long straddle or strangle bought early gains from rising IV; you close it the day before the announcement, banking the vega gain and *sidestepping the crush entirely*. You never hold a long single-event straddle *through* the announcement hoping for a move — that's paying the crush.

**2. Sell premium to harvest the crush (defined-risk credit structures).** The bread-and-butter event play. Sell expensive pre-event premium and collect the post-event IV collapse. Because the tail risk is a real gap, professionals overwhelmingly prefer **defined-risk** structures over naked short options:
   - **Iron condor** — sell an out-of-the-money put spread and an out-of-the-money call spread. You profit if the underlying stays within a range; max loss is capped at the wing width minus credit. Ideal when you expect a contained move and a fat crush.
   - **Credit spread** (bull put or bear call) — a directional lean with defined risk, for when you have a view on which way the surprise leans.
   - **Iron butterfly** — a tighter, higher-credit condor centred at-the-money for maximum crush capture, with a narrower profit zone.

**3. Calendars — exploit the term-structure bump.** Before an event, the *near-dated* expiry that contains the event has its IV bid up far more than later expiries — the volatility **term structure** develops a bump or even inverts (near-term IV above far-term, abnormal). A **calendar spread** (sell the expensive near-dated option containing the event, buy a cheaper longer-dated option at the same strike) profits when the near leg's IV crushes after the event while the far leg holds its value. You isolate the term-structure distortion rather than betting on direction.

**4. Stay flat.** Often the right answer. When IV is already extreme and the event is a genuine coin-flip with binary, gap-prone outcomes (a closely-contested election count, a single high-beta stock's earnings), the risk/reward for *every* structure can be poor. A professional with no edge stands aside. There is no rule that you must have a position on every event.

### The danger of overnight GAPS — why stop-losses fail

Here is the seller's nightmare and the reason naked selling into events maims accounts: **a stop-loss does not protect you against a gap.** A stop-loss is an instruction to exit when price *trades through* a level. But results come out after market hours, the Budget can swing the index hundreds of points in minutes, an election result gaps the open. When the underlying *jumps* from one price to a far-away price without trading the levels in between, your stop fills not at your stop price but at wherever the market reopens — potentially far past your intended loss. A short option that was a calm winner at Thursday's close can open Friday as a multiple of the premium you collected, your "protective" stop firing at a catastrophic level.

This is why event selling must be **defined-risk** (spreads, condors — the long wing caps the gap loss to a known maximum) and **position-sized for the max loss, not the stop.** Assume the stop won't work; size so that the *full* capped loss is survivable. Naked short options into a binary event are how traders go from months of small gains to a single account-ending morning.

### Event-by-event: the Indian calendar

- **Corporate results (earnings):** Single-stock, physically-settled options. The cleanest IV-crush plays — IV ramps for days, then crushes hard after numbers — and the gappiest: a surprise can move a stock 10–15% overnight. Defined risk only.
- **Union Budget (Feb 1):** Market-wide, sector-rotating. India VIX climbs into it; sectors named (or not) in the speech gap, and Nifty/Bank Nifty swing intraday as it is read. Term-structure and index condor plays.
- **RBI Monetary Policy (MPC):** Roughly every two months. The rate decision *plus* the Governor's commentary moves Bank Nifty most (banks are rate-sensitive) — often the commentary, not the rate, drives the move.
- **General elections / state-election results:** The biggest gap risk of all — counting day can gap Nifty several percent. IV is extreme beforehand; many professionals reduce size or stay flat through the count.
- **US Fed (FOMC):** Lands late night IST, so its effect is an *overnight gap* on the next Indian session — pure gap risk for anything held overnight, with no chance to stop out while it happens.
- **Weekly/monthly expiry:** Its own recurring event — see below.

### Expiry day as a recurring event

Expiry is the one "event" that arrives every single week, and it has its own physics driven by two Greeks colliding:

- **Theta** (time decay) is maximal — on expiry day, an at-the-money option's entire remaining value is time value, bleeding to zero by close. This is a tailwind for sellers.
- **Gamma** (the rate at which delta changes) explodes — near-the-money options on expiry day have huge gamma, so a small Nifty move flips an option from near-worthless to deep in-the-money and back. Delta whipsaws violently.

The result is the famous expiry-day tension: sellers are paid rich theta but ride a knife-edge of gamma. Add **pinning** — the tendency of the underlying to gravitate toward a strike with very large open interest, as hedgers' delta-hedging activity pulls price toward the "max pain" strike where the most options expire worthless. Indian index options being **European and cash-settled** makes expiry clean (no delivery, no assignment surprise — just a final settlement at the close), which is why expiry-day premium selling on Nifty/Bank Nifty is so heavily traded.

How to play (or avoid) expiry day:
- **Sellers** love the theta but must respect gamma: small size, defined risk, and an awareness that an ATM short can swing wildly on a 30–40 point Nifty move. Many take their 50%-of-credit profit and leave *before* the final-hour gamma chaos.
- **Buyers** treat expiry as a cheap lottery — tiny premium ATM options that, *if* a sharp move comes, can multiply many times over from gamma. Most expire worthless; size accordingly.
- **The honest default for beginners:** the last hour of expiry is the most gamma-violent, lowest-edge hour of the week. Avoiding it is a perfectly professional choice.

## Worked example (₹, Nifty / single stock)

Let's price the IV crush concretely and pit a **long straddle** against a **short strangle** across a results event.

**Setup.** A large-cap stock trades at **₹1,000**, results due after today's close, lot size **500**. Going in, at-the-money implied volatility is pumped to **60%** for the weekly expiry (2 days out). The market is effectively pricing a one-day move of roughly:

`expected move ≈ price * IV * sqrt(days/365) = 1000 * 0.60 * sqrt(2/365) ≈ 1000 * 0.60 * 0.074 ≈ ₹44 (about 4.4%)`

So the options are priced for a ~4.4% move. The ATM 1000 call and 1000 put each cost about **₹30** at this inflated IV.

**Trade A — Long straddle (the buyer paying the crush).** You buy the 1000 call and 1000 put for **₹30 + ₹30 = ₹60** total (₹60 × 500 = **₹30,000/lot**). Breakevens at expiry: **₹940 and ₹1,060** — the stock must move more than ₹60 (6%) for you to profit at expiry, *more* than the 4.4% priced because you bought both legs.

Now the crush. Results land, and post-event IV collapses from 60% to **30%** (a typical results crush). Three scenarios next morning:

- *Stock moves 4% to ₹1,040 (a "big" move — but as priced).* The 1000 call is ~₹40 intrinsic but valued at the *crushed* 30% IV; the put is out-of-the-money and crushed near worthless. The straddle is worth roughly **₹45–50** — you *paid ₹60*. A 4% move and you still **lose** ~₹5,000–7,500/lot. The trap in numbers: right on direction, still down, because the crush ate the gain.
- *Stock barely moves to ₹1,005.* Both legs collapse with the crush to maybe **₹18** total. You lose (60 − 18) × 500 = **₹21,000/lot**.
- *Stock gaps 8% to ₹1,080 (genuine surprise).* The call is ~₹80, the put ~₹2, total ~₹82 even at crushed IV. You make (82 − 60) × 500 = **₹11,000/lot**. The buyer only wins on a *surprise bigger than priced*.

**Trade B — Short strangle (the seller harvesting the crush).** Instead you sell the **1,050 call** and the **950 put** (out-of-the-money, ~1 standard-deviation wings) for a combined credit of, say, **₹40** (₹40 × 500 = **₹20,000/lot** collected). You profit if the stock stays between roughly **₹910 and ₹1,090** (breakevens = strikes ± credit).

- *Stock moves 4% to ₹1,040 (as priced).* Both your short strikes are out-of-the-money; post-crush, the strangle is worth maybe **₹14** to buy back. You profit (40 − 14) × 500 = **₹13,000/lot** — the seller *wins on the same 4% move that lost the buyer money.* That is the IV crush paying the seller.
- *Stock barely moves to ₹1,005.* Both legs crush to near worthless (~₹5 total). You bank (40 − 5) × 500 = **₹17,500/lot**, near max profit.
- *Stock gaps 8% to ₹1,080 (surprise).* The 1,050 call is now ₹30 in-the-money plus value, say ₹35; the put near zero. You lose (40 − 35) × 500 ≈ ₹2,500 here — but a *bigger* gap is unbounded. This is the seller's tail: a naked strangle has theoretically unlimited loss on a large gap, and no stop-loss saves you overnight.

**Trade C — The defined-risk fix (iron condor).** To cap that tail, convert the short strangle into an **iron condor**: also *buy* the 1,100 call and the 900 put as wings. Your credit shrinks (say from ₹40 to **₹28**), but your max loss is now capped. With 50-point wings: max loss = (50 − 28) × 500 = **₹11,000/lot**, *no matter how far the stock gaps.* You give up ₹6,000 of potential profit to make the overnight gap survivable. For event selling, that is almost always the right trade — because the whole point is that the gap *can* happen, and a stop-loss won't protect you when it does.

**The lesson in one line:** across the most likely (as-priced) outcome, the seller harvesting the crush profited while the buyer paying the crush lost — but the seller must be *defined-risk and sized for the gap*, because the rare surprise is where unprotected sellers die.

## Common mistakes / risk note

- **Buying a straddle the day before an event "because a big move is coming."** The move is already priced; you're paying peak IV and the crush will likely beat your move. Buy vol *early and cheap*, or don't buy it.
- **Trusting a stop-loss to cap an event-gap loss.** Stops don't fire across a gap. Results, Budget, Fed, election counts all gap. Use defined-risk structures and size for the *max* loss, not the stop.
- **Naked short options into a binary event.** One adverse gap can exceed many months of harvested premium. If you sell into events, define the risk with wings (condors/spreads).
- **Ignoring IV rank.** Selling premium when IV rank is low (little crush to harvest) or buying when IV rank is high (paying for a crush you'll suffer) is backwards. Check where IV sits on its own range first.
- **Over-trading every event.** No edge, extreme IV, true coin-flip outcome — stay flat. Standing aside is a position.
- **Misjudging expiry-day gamma.** Selling ATM options into the final hour for "easy theta" ignores that a 40-point Nifty swing, magnified by huge gamma, can turn the trade violently. Small size or avoid.
- **Forgetting costs and settlement.** Event trades cross wide pre-event bid-ask spreads, and each leg carries STT/brokerage. Index options are European cash-settled (clean); single-stock options are American and physically settled — an in-the-money short stock option at expiry means a delivery obligation, a real hazard on results plays.

## Key takeaways

- **The universal event pattern:** implied volatility rises into a scheduled event and crushes right after. The crush is near-certain; the underlying's move is the gamble.
- **Buyers pay the crush, sellers harvest it.** A correct directional guess can still lose for a buyer if the move is smaller than the pumped-up IV already priced.
- **Buy premium only BEFORE IV pumps** (low IV rank, exit before the announcement); selling premium and **defined-risk credit structures** (iron condors, credit spreads) harvest the post-event crush.
- **Calendars exploit the term-structure bump** — the event's near-dated expiry is over-priced relative to later expiries.
- **Overnight gaps defeat stop-losses.** Sell events only with defined risk and size for the capped max loss, never the stop.
- **Expiry is a weekly event** with maximal theta and exploding gamma; pinning/max-pain pulls price toward big-OI strikes. Index options are European cash-settled, so it's clean — but the final hour is the lowest-edge, highest-gamma window.
- **Staying flat is a legitimate, often correct, event decision.**

## Practice problems

1. **(Conceptual)** Explain in plain English why a trader can correctly predict that a stock will rise after results, buy a call the afternoon before, and still *lose* money. Name the specific force responsible.

2. **(Numeric)** A stock at ₹2,000 has ATM weekly IV pumped to 50% with 2 days to results. Estimate the move the options are pricing in (use `price * IV * sqrt(days/365)`). If the stock then moves 3% but IV crushes from 50% to 25%, would a long straddle bought at this IV more likely profit or lose? Explain.

3. **(Numeric)** You sell a Nifty iron condor before the Budget for a net credit of ₹70, with 200-point wings (lot 75). (a) What is your max profit per lot? (b) What is your max loss per lot, and why does this number, not the credit, set your position size? (c) Why is a hard stop-loss an unreliable protection here?

4. **(Conceptual)** Why does an option *seller* often prefer a defined-risk iron condor over a naked short strangle when trading around the RBI policy or election results, even though the strangle collects more premium?

5. **(Application)** It is the day before a known catalyst and India VIX (and the stock's IV rank) is already near its yearly high. A friend wants to buy a long straddle "to catch the move." Using IV-rank reasoning, advise them: what's the better volatility posture, and what would have to be true for buying premium to make sense?

6. **(Conceptual)** Describe the two Greeks that dominate Nifty *expiry day* and how they pull in opposite directions for a seller. What is "pinning," and why does European cash settlement make Indian index expiry cleaner than physically-settled stock options?

## Solutions

**1.** Because the expected move is already baked into the option's price via inflated implied volatility. Buying the afternoon before results means paying peak IV. After the announcement, IV crushes (vega works against the long option). For the call to profit, the stock must rise *more* than the pumped IV already paid for; a "correct but modest" rise can be entirely eaten by the **IV crush**. The responsible force is the collapse in implied volatility (long vega turning against the buyer).

**2.** Priced move ≈ 2000 * 0.50 * sqrt(2/365) = 2000 * 0.50 * 0.074 ≈ **₹74, about 3.7%**. The options are pricing roughly a 3.7% move. A 3% actual move is *less* than priced, and on top of that IV halves from 50% to 25%, crushing both straddle legs. The long straddle would **most likely lose** — the move came in under what was priced *and* the IV crush deflated both legs. A buyer needs a move *larger* than ~3.7% (beyond breakevens that are widened further by the crush) to win.

**3.** (a) Max profit = the credit = ₹70 × 75 = **₹5,250/lot**. (b) Max loss = (wing width − credit) = (200 − 70) = ₹130 × 75 = **₹9,750/lot**. You size on this because the Budget can gap Nifty straight to the far wing; the credit is the best case, the ₹9,750 is the realistic worst case you must be able to absorb. (c) A stop-loss only fires when price *trades through* a level. The Budget moves the index in fast jumps (and intraday gaps as the speech is read); price can leap past your stop, filling far worse than intended — so the defined-risk *wings*, not the stop, are your real protection.

**4.** A naked short strangle has **unlimited loss on a large gap**, and stop-losses don't protect against gaps — RBI commentary or an election count can move the underlying violently and overnight. The iron condor *buys wings* that cap the maximum loss to a known, survivable number (wing width − credit). The strangle collects more premium, but the extra credit is compensation for an open-ended tail that, on a single bad event, can exceed many months of harvested premium. Sellers trade some credit for a hard cap because the whole risk in event trading is the gap they cannot stop out of.

**5.** When IV rank is already near its yearly high, options are *expensive*, and buying a straddle the day before means paying peak premium straight into the IV crush — the worst time to be long vega. The better posture is to be a **net seller** of that rich premium (defined-risk: an iron condor or credit spread) to harvest the crush, or to **stay flat**. Buying premium would only make sense if IV were *low* (low IV rank) with the catalyst still days away — buy cheap vol early, ride rising IV up, and sell *before* the announcement to dodge the crush. Buying high-IV-rank premium the day before is precisely the trap.

**6.** The two Greeks are **theta** (time decay), which is maximal on expiry day and pays the seller as the option's remaining time value bleeds to zero, and **gamma** (rate of change of delta), which explodes near-the-money on expiry day so a small Nifty move whipsaws the option's delta violently against the seller. They pull in opposite directions: theta is the seller's reward, gamma is the seller's risk — rich decay riding a knife-edge. **Pinning** is the tendency of the underlying to gravitate toward a strike with very large open interest (the "max pain" strike where most options expire worthless), driven by hedgers' delta-hedging flows. European **cash settlement** makes Indian index expiry clean: there is no early assignment and no delivery — positions simply settle to cash at the closing value — whereas American, physically-settled stock options can be assigned, forcing an unwanted share delivery or purchase obligation if they finish in-the-money.
