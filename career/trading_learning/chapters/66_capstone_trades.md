# Chapter 66: Capstone — Five Trades from Idea to Exit

Everything in this book — payoffs, Greeks, implied volatility, strategy selection, sizing, exits — exists to serve a single moment: when you actually put on a trade and then live with it. A trade is not a payoff diagram. It is a *process* that runs from a vague hunch to a closed position and a number in your P&L. Professionals do not think "I'll buy a call." They think: "Here is my read, here is the volatility regime, here is why this structure fits, here is how much I can lose, here is what I do if I'm wrong, and here is where I get out."

This chapter walks five complete, realistic trades through that same nine-step lifecycle on a sample **₹3,00,000 (three lakh) account**. The situations are deliberately different — bullish index, range-bound index, single-stock earnings, portfolio hedge, low-volatility breakout. Some win; some lose and get managed. All use concrete rupee numbers. The premiums and India VIX levels are illustrative — they move daily — but the *reasoning* is exactly how a desk thinks.

## Core concepts

### The nine-step lifecycle every trade should follow

Before the case studies, fix the checklist in your head. Every professional trade answers these in order:

1. **Thesis / market read** — what do I think happens, and over what horizon? Direction, magnitude, time.
2. **IV regime + event check** — is implied volatility (the market's priced-in expectation of movement, read through India VIX and IV rank) high or low? What events (results, Budget, RBI policy, expiry) fall inside my window?
3. **Strategy selection + WHY** — pick a structure whose payoff matches the thesis *and* the IV regime. High IV favours selling premium; low IV favours buying it.
4. **Strike + expiry choice** — translate the view into specific contracts.
5. **Position sizing** — risk no more than 1–2% of the account on the idea. On ₹3,00,000 that is **₹3,000–₹6,000** of defined risk per trade.
6. **Entry** — the fill, the net debit/credit, the margin.
7. **Management / adjustment** — pre-decided rules for what to do as it moves.
8. **Exit** — target, stop, or time-based.
9. **P&L attribution + lesson** — decompose the result into direction, volatility, and theta, and write down what you learned.

The discipline is the edge. Most of the ~9-in-10 retail F&O traders who lose money (per SEBI's studies) skip steps 2, 5, 7, and 9 entirely.

### A word on sizing math

"Risk 1–2%" means the **maximum loss** your plan accepts on a defined-risk trade — or the **stop-loss** you will honour on an undefined-risk one — should be ₹3,000–₹6,000. For a defined-risk spread, max loss is `(width - net credit) * lot size`, or `net debit * lot size`. Lots = risk budget ÷ per-lot max loss, rounded **down**. We use round, current-ish lot sizes (Nifty 75, Bank Nifty 35, a stock 250) and treat costs (STT, brokerage, ~18% GST on brokerage) as a small drag acknowledged at exit.

## Worked example

These five trades *are* the worked example — five of them, each fully numeric.

### Trade 1 — Moderately bullish Nifty: a bull call spread

**(a) Thesis.** Nifty is at **24,000**. After a healthy correction, breadth is improving with a monthly expiry ~17 days out. My read: a *grind* higher to ~24,500 over two weeks — moderately bullish, not explosive. No 1,000-point rip expected.

**(b) IV regime + events.** India VIX is moderate at ~**13–14**, IV rank ~40th percentile — neither cheap nor rich. No RBI policy or major data inside the window. A naked long call would work, but I'd overpay for time and vega I don't need for a modest target.

**(c) Strategy + WHY.** A **bull call spread** (buy a lower call, sell a higher call). Directional but *cheaper* than a naked call because the sold call funds part of the premium; it caps my vega and — crucially — gives **defined risk**, which makes sizing clean. Trade-off: upside capped at the short strike. Fine — my target *is* 24,500.

**(d) Strikes + expiry.** Monthly expiry, ~17 days out. Buy the **24,000 call** (at-the-money) for ₹220; sell the **24,500 call** for ₹90. Net debit = **₹130** per share. Spread width = 500 points. Max profit = `500 - 130 = ₹370` per share. Breakeven = `24,000 + 130 = 24,130`.

**(e) Sizing.** Nifty lot = 75. Max loss per lot = `130 * 75 = ₹9,750`. That is already above my ₹6,000 ceiling for one lot — so a single lot exceeds 2%. I either accept ~3.25% on one lot (too much by my own rule) or I don't trade it at this debit. **I take one lot but tighten my management** so my *realised* risk stays near 2%: I pre-commit to a mental stop at a ₹4,500 loss (roughly half the debit gone) rather than letting the full ₹9,750 ride. Risk controlled by the exit, not just the structure.

**(f) Entry.** Bought 1 lot of the 24000/24500 call spread for net ₹130 (₹9,750 outlay; defined-risk debit spread, so margin is just the debit). 

**(g) Management.** Nine days in, Nifty reaches **24,350**. The spread is worth ~₹290 — ₹160 profit per share with eight days left and theta on my short strike now helping. My rule on a vertical: **take 50–70% of max profit** rather than squeezing the last rupees, because expiry-week gamma can reverse a winner fast.

**(h) Exit.** Nifty touches **24,480** two days later; the spread trades near **₹340**. I close for ₹340 — `(340 - 130) * 75 = ₹15,750` gross, ~**57% of max** (₹27,750). After ~₹250 costs, ~**₹15,500 net**.

**(i) P&L + lesson.** Profit ≈ ₹15,500 on ₹9,750 risked (+159%). Attribution: almost entirely **delta** (direction was right); a little **theta** on the short leg; vega a wash. **Lesson:** a spread turned a *moderately* confident directional view into a defined-risk, fundable trade — and taking 50–70% of max, not 100%, locked the win before expiry-week gamma could spoil it.

### Trade 2 — High-IV, range-bound Bank Nifty: an iron condor harvesting theta

**(a) Thesis.** Bank Nifty is at **52,000** and has been chopping in a 51,000–53,000 band for two weeks. My read: **no trend, range-bound** into weekly expiry. I want to get paid for the market going *nowhere*.

**(b) IV regime + events.** India VIX has spiked to ~**18** after a volatile global session; Bank Nifty's IV rank is ~**70th percentile** — options are *expensive*. No bank results or RBI event this week. Textbook setup for a **premium-selling, range** strategy: rich premium to collect plus a likely *IV mean-reversion* tailwind.

**(c) Strategy + WHY.** An **iron condor**: sell an OTM put spread *and* an OTM call spread. It is **delta-neutral, short vega, positive theta, defined risk**. I profit if Bank Nifty stays inside my short strikes and/or IV falls. The long wings (defined risk) let me size it on a high-vol underlying without undefined tail exposure.

**(d) Strikes + expiry.** Weekly expiry, 4 days out. With expected move roughly ±900 points, I sell strikes outside it:
- Sell **50,800 put**, buy **50,300 put** (500-wide put spread).
- Sell **53,200 call**, buy **53,700 call** (500-wide call spread).
- Credit received: put spread ₹70 + call spread ₹65 = **₹135** per share.

Max profit = ₹135/share (the credit). Max loss = `(500 - 135) = ₹365` per share. Breakevens: `50,800 - 135 = 50,665` and `53,200 + 135 = 53,335`.

**(e) Sizing.** Bank Nifty lot = 35. Max loss per lot = `365 * 35 = ₹12,775`. Too big for one lot under a 2% rule. So I cannot trade a full-width condor at one lot and stay disciplined — **I narrow the wings to 300-wide** instead: sell 50,800 / buy 50,500 put, sell 53,200 / buy 53,500 call. Credit drops to about **₹95**; max loss = `(300 - 95) * 35 = ₹7,175`. Still slightly over ₹6,000, so I pre-set a **management stop at 2x credit lost (~₹6,650)** and treat that as my real risk. One lot.

**(f) Entry.** Sold 1 lot of the 300-wide iron condor for **₹95** credit (₹3,325 collected). Margin: a defined-risk condor blocks roughly the max-loss amount (~₹7,000) as SPAN+exposure margin, well within the account.

**(g) Management.** Two days in, Bank Nifty drifts to **53,050**, toward my call side; the condor is a small loser (~₹40/share against, ~₹1,400). My rule: a condor is **tested** when price reaches a short strike (53,200) — not there yet. India VIX has dropped to ~15, which *helps* (short vega). I hold. Pre-set adjustment if it breaches 53,200: **roll the untested put spread up** to collect credit and recentre. Price stalls; no adjustment needed.

**(h) Exit.** On expiry-eve, Bank Nifty sits at **52,650**, between my shorts. The condor has decayed to ~**₹25**. My rule: **close at 50–75% of max** rather than hold for the last ₹25 and risk an overnight gap. Buy back at ₹25: `(95 - 25) * 35 = ₹2,450` gross, ~**₹2,150 net**.

**(i) P&L + lesson.** Profit ≈ ₹2,150 on ~₹7,000 risked (+31% in four days). Attribution: **theta** was the engine; **vega** (IV 18→15) added a push; **delta** was a small drag. **Lesson:** sell premium only when IV is genuinely rich, keep it defined-risk, and don't be greedy — closing at 25–50% of max, repeated weekly, beats holding to zero and eating the occasional gap. The **narrower wings** were a sizing decision, not a market view.

### Trade 3 — Earnings event on a stock: a short strangle exploiting IV crush (with caveats)

**(a) Thesis.** A large-cap IT stock — call it **INFY at ₹1,600** — reports quarterly results tomorrow. My read: the result is unlikely to be a blockbuster surprise; the stock will move, but **less than the options are pricing**. No directional view. I want to harvest the **IV crush**: implied volatility is jacked up before results and collapses the moment numbers are out.

**(b) IV regime + events.** The single event *is* the trade. Pre-results IV is at the **90th-plus percentile** — front-month options are extremely rich. The catalyst is tomorrow morning; IV deflates within hours of the print regardless of direction.

**(c) Strategy + WHY.** A **short strangle** (sell an OTM call and OTM put) is the purest IV-crush harvester: maximally short vega, positive theta, profits if the stock stays between the strikes and/or IV collapses. **BUT — the honest caveat:** a short strangle on a *single stock through an earnings gap* has **undefined risk**. Stock options in India are **physically settled**, and a shock result can gap the stock 8–10% past your strike overnight, blowing through any intended stop *before you can act*. The market can gap; your stop cannot. So I present both and choose deliberately:
- **Undefined-risk version (illustrative, NOT my pick):** sell the 1,650 call at ₹35 and the 1,550 put at ₹32 = ₹67 credit. Lovely until a gap to ₹1,750 costs `(1,750 - 1,650) - 67 = ₹33`/share and counting — *unbounded*.
- **Defined-risk version (my actual trade): an iron condor / short iron fly** — sell the strangle but **buy protective wings**. Sell 1,650 call / buy 1,700 call; sell 1,550 put / buy 1,500 put. Net credit ≈ **₹40**. Max loss = `(50 - 40) = ₹10`/share. *This* is what a risk-managed desk does on single-stock earnings.

**(d) Strikes + expiry.** Nearest weekly/monthly expiry that includes the event, strikes set just outside the options-implied move (~±5%). Lot size 250 (illustrative). Credit ₹40, width 50, max loss ₹10/share.

**(e) Sizing.** Max loss per lot = `10 * 250 = ₹2,500`. Comfortably under ₹6,000 — I can even do this in clean 1-lot size and stay well inside 1% risk. One lot. Credit collected = `40 * 250 = ₹10,000`; max loss ₹2,500. (Contrast: the naked strangle's "risk" can't be sized at all — that's the point.)

**(f) Entry.** Sold 1 lot defined-risk iron condor around INFY for ₹40 net credit the afternoon before results, with IV near its peak.

**(g) Management.** This is an *event* trade: there is no intraday managing through the gap — the position resolves on the open. The "management" is the structure (the wings) chosen *before* entry. Pre-decided rule: **close the morning after results**, into the IV crush, regardless of direction.

**(h) Exit.** Results are in line. INFY opens at **₹1,585** (~1% move, *inside* my strikes) and IV **collapses** from the 90th percentile to normal. The condor sold for ₹40 is now worth ~**₹12** — both shorts deflated. Buy back: `(40 - 12) * 250 = ₹7,000` gross, ~**₹6,500 net**.

**(i) P&L + lesson.** Profit ≈ ₹6,500 on ₹2,500 risked. Attribution: the cleanest **vega** trade of the five — the IV crush did almost all the work; theta helped; delta was near-neutral. **Lesson:** the edge in earnings selling is the *volatility* collapse, not direction — but gap risk is real and asymmetric, so sell the IV crush through a **defined-risk** structure, not a naked strangle. The naked version's bigger credit is just compensation for tail risk you should not casually accept on a ₹3,00,000 account.

### Trade 4 — Hedging a stock portfolio into the Budget: protective put / collar

**(a) Thesis.** I hold a ₹**2,40,000** basket of large-cap Nifty stocks (cash, long-term holdings I don't want to sell and trigger tax). The **Union Budget** is in nine days. My read: not bearish, but the *event risk* is large and two-sided — I want to **insure** my portfolio against a sharp Budget-day drop without giving up my holdings.

**(b) IV regime + events.** India VIX has crept up to ~**16** as the Budget approaches — index put protection is getting pricier, but that's exactly *why* I want it on before the crowd panics. The Budget is the dominant event in the window.

**(c) Strategy + WHY.** A **protective put** on Nifty: buy an index put sized to offset my basket's market exposure. My basket has a **beta ≈ 1.0** to Nifty, so a Nifty put hedges it well and is cheaper/cleaner than buying puts on each stock. Because the put costs real premium (a drag if nothing happens), I consider upgrading to a **collar**: buy the put *and* sell an OTM call to finance it, accepting a cap on my upside in exchange for cheaper (even free) insurance. The trade-off is explicit: collar = cheaper protection, but I forgo gains above the short call.

**(d) Strikes + expiry.** Nifty at **24,000**; basket ≈ ₹2,40,000, so exposure ≈ `2,40,000 / 24,000 = 10` index units — but a Nifty lot is 75, ~7x my exposure. **One Nifty put massively over-hedges me.** This is the real-world snag: index lots are too big to finely hedge a 2.4-lakh basket. So I treat the put as a **deliberately cheap tail hedge**, not a 1:1 offset: buy the **23,000 put at ₹90** (true disaster insurance), and to cut its cost, **sell the 24,500 call at ₹85** → a near-**zero-cost collar**, net debit ₹5/share.

**(e) Sizing.** Here sizing is about *cost of insurance*, not max loss on a bet. Net debit = `5 * 75 = ₹375` — trivial. The collar bounds my *portfolio* drawdown; the short call caps basket-equivalent upside above 24,500, and its margin is offset by the long put. I accept that the hedge is *coarse* (lot too big) and view it as cheap, slightly oversized disaster cover for ₹375 plus capped upside.

**(f) Entry.** Bought 23,000 put ₹90, sold 24,500 call ₹85, net ₹5 debit, one lot, eight days before Budget.

**(g) Management.** Budget day: Nifty **gaps down to 23,100** on a disappointing fiscal stance. My basket is down ~3.75% (≈ **₹9,000**). My 23,000 put is now near-the-money at ~₹260 (from ₹90) — a gain of ~₹170/share = **₹12,750** on the lot. The short 24,500 call is worthless (I keep its ₹85). Because the put lot is *larger* than my basket, the hedge gain (~₹12,750) actually *exceeds* the basket loss (~₹9,000) — the over-hedge turned the event mildly *profitable*, which is lot-size luck, not skill.

**(h) Exit.** Post-Budget, event passed, I **monetise the hedge**: sell the 23,000 put at ₹260, buy back the near-worthless call, keep the stock basket untouched. The hedge has done its job; no point paying theta on protection I no longer need.

**(i) P&L + lesson.** Hedge P&L ≈ +₹12,750 (put) + ₹6,375 (call kept) − costs, offsetting a ~₹9,000 unrealised basket dip and leaving me net *ahead* while never selling a share. Attribution: **delta + vega** on the put. **Lesson:** insurance is a *cost centre*, not a profit centre — judge it by whether it let you hold calmly through the event, not by whether it "made money." And know your **basis risk**: index lots are blunt for small baskets, so a hedge is usually over- or under-sized — size it consciously as a tail hedge, don't pretend it's precise.

### Trade 5 — Low-IV breakout expectation: a long straddle/strangle

**(a) Thesis.** Nifty has coiled into a tight **300-point range around 24,000** for three weeks — classic compression before a big move (a major RBI policy *and* state-election results both land next week). My read: **a large move is coming, but I genuinely don't know the direction.** I want to be long *movement*.

**(b) IV regime + events.** India VIX has drifted to ~**11** (multi-month lows), IV rank near the **10th percentile** — options are *cheap*. Two binary catalysts sit inside the window. The mirror image of Trade 3: instead of selling rich IV, I'm **buying cheap IV before it expands**.

**(c) Strategy + WHY.** A **long strangle** (buy OTM call + OTM put), a cheaper cousin of the long straddle. It's **long vega, long gamma, negative theta, direction-agnostic**: I profit from a big move *either way*, or from IV expanding even before the move. The enemy is **theta** — if nothing happens, both options bleed. So I want cheap entry (low IV) and a near catalyst.

**(d) Strikes + expiry.** Weekly expiry covering both events, ~6 days out. **Long strangle** to cut cost: buy **24,200 call ₹60** + buy **23,800 put ₹55** = **₹115** debit per share. Breakevens: `24,200 + 115 = 24,315` upside and `23,800 - 115 = 23,685` downside. I need a move bigger than ~315 points *or* an IV pop to win.

**(e) Sizing.** Lot 75. Cost (= max loss) per lot = `115 * 75 = ₹8,625`. Over my ₹6,000 ceiling for one lot. To respect sizing I **widen the strangle** (cheaper) — buy 24,300 call ₹40 + 23,700 put ₹38 = **₹78** debit → max loss `78 * 75 = ₹5,850`, just inside 2%. One lot. (Widening lowers cost *and* pushes breakevens out — a real trade-off: I now need a *bigger* move. I accept it to keep risk at 2%.)

**(f) Entry.** Bought 1 lot 24300/23700 strangle for ₹78 debit (₹5,850 outlay, defined max loss = the debit).

**(g) Management.** Two days pass with Nifty pinned — theta bleeds the position to ~₹62 (down ₹16/share, ~₹1,200 unrealised). This is the long-premium trap: *right that "a move is coming," but early.* My rule: **hold through the catalyst** (that's what I paid for), but set a **time stop** — if both events pass with no move by expiry-eve, cut it rather than donate the rest to theta. Then RBI surprises hawkish and election results are messy: Nifty **breaks down to 23,400** and India VIX **spikes 11→19**.

**(h) Exit.** My 23,700 put is now ~₹328 (intrinsic 300 + fat time value from the VIX spike); the 24,300 call is ~₹8. Strangle ≈ **₹328**. I sell into the spike (don't wait for it to fade): `(328 - 78) * 75 = ₹18,750` gross, ~**₹18,400 net**.

**(i) P&L + lesson.** Profit ≈ ₹18,400 on ₹5,850 risked (+314%). Attribution: a big **delta/gamma** win on the put leg, *amplified by a vega tailwind* (VIX 11→19) — buying cheap IV meant the expansion paid me twice. Theta was the cost I outlasted. **Lesson:** long straddles/strangles are bought for **cheap IV + a near, genuine catalyst**, not casual "I think it'll move" punts — most expire worthless because theta wins when nothing happens. What made this work: entering at *low* IV rank, sizing by widening to stay at 2%, and *selling into the IV spike* rather than holding for the perfect bottom.

## Common mistakes / risk note

- **Skipping the IV-regime step.** Buying premium when IV is high, or selling it when cheap, is the most common structural error. Match structure to regime: **high IV → sell, low IV → buy.**
- **Sizing by gut, not by max loss.** Notice how often the *correct* size forced a structural change (narrower condor wings, wider strangle, smaller hedge). Size first, accept the structure that fits.
- **Naked single-stock selling through earnings.** The market gaps; your stop doesn't. Defined risk on event trades is non-negotiable for a retail account.
- **Holding winners to 100% of max.** Trades 1 and 2 *closed early* by rule. Expiry-week gamma and gaps reverse winners brutally; 50–75% of max, repeated, beats greed.
- **Treating a hedge as a profit trade.** Trade 4 "made money," but that was lot-size luck. Insurance is judged by whether it let you hold calmly through the event.
- **Confusing "I'm right" with "I'm right *now*."** Trade 5 was a paper loser before the catalyst. Theta punishes the early — plan to outlast it, or don't buy premium without a near catalyst.

Above all: ~9 in 10 retail F&O traders lose money. The lifecycle here — especially steps 2 (IV), 5 (sizing), 7 (management), and 9 (the written lesson) — is what separates the process-driven minority from the crowd.

## Key takeaways

- A trade is a **nine-step process**, not a payoff picture: thesis → IV/events → strategy → strikes → sizing → entry → management → exit → attribution.
- **The IV regime dictates whether you buy or sell premium.** High IV rank/VIX favours defined-risk *selling* (condor, earnings IV crush); low IV favours *buying* (straddle/strangle); a clean directional view with moderate IV favours a *spread*.
- **Size to 1–2% of capital (₹3,000–₹6,000 here), and let sizing reshape the structure** — narrower wings, wider strangles, smaller hedges — rather than oversizing a "good idea."
- **Defined risk is how you size honestly.** Naked selling can't be sized and exposes you to gaps; on a retail account, prefer wings.
- **Manage by pre-set rules and take profits early** (50–75% of max); expiry-week gamma and overnight gaps are real.
- **P&L attribution (delta vs vega vs theta) plus a written lesson** turns each trade into a repeatable edge, not a random outcome.

## Practice problems

1. **(Sizing)** On the ₹3,00,000 account (2% rule = ₹6,000), you want a Nifty (lot 75) bull call spread bought for a net debit of ₹110. What is the max loss per lot, and how many lots keep you within the rule?

2. **(Regime match)** India VIX is at 19 and Bank Nifty has been range-bound for two weeks with no events this week. Which structure from this chapter fits, and why — buy premium or sell it?

3. **(Earnings)** A stock at ₹2,000 reports tomorrow; pre-results IV is at the 95th percentile. You sell a naked strangle for ₹50 credit and the stock gaps to ₹2,200 overnight past your ₹2,100 short call. Roughly what is your loss per share, and what one structural change would have capped it?

4. **(Iron condor P&L)** You sell a 300-wide Bank Nifty (lot 35) iron condor for ₹95 credit. State max profit, max loss, and your profit per lot if you close at 50% of max premium captured.

5. **(Hedge logic)** Your ₹2,40,000 basket (beta 1.0) faces a Budget event with Nifty at 24,000 and a lot size of 75. Why does one Nifty put over-hedge you, and what does that imply about how to think of the hedge?

6. **(Long premium)** You buy a Nifty strangle for ₹78 (lot 75) before twin catalysts. Two days later, pre-event, it's worth ₹62 with no move. Are you wrong? What single factor is hurting you, and what rule protects you?

## Solutions

1. Max loss per lot = `110 * 75 = ₹8,250`, which **exceeds** the ₹6,000 budget — so *zero* lots keep you strictly within 2% at this debit. Either reduce the debit (wider/cheaper spread), or — as in Trade 1 — take one lot but enforce a **management stop near ₹4,500–₹6,000** so realised risk stays inside the rule.

2. **Sell premium** via an **iron condor** (defined-risk). VIX 19 with high IV rank means options are *rich*; the underlying is range-bound (delta-neutral fits); no events threaten a directional break. You collect theta and benefit from likely IV mean-reversion. (Trade 2's setup.)

3. Loss ≈ `(2,200 - 2,100) - 50 = ₹50` per share, **and rising** — naked short calls have *unbounded* risk. The fix: **buy a protective wing** (long the 2,150 call) to convert the naked strangle into a defined-risk **iron condor**, capping loss at `(width - credit)` per share. (Trade 3.)

4. Max profit = credit = `95 * 35 = ₹3,325`. Max loss = `(300 - 95) * 35 = ₹7,175`. Closing at 50% of max means buying back at ₹47.5: profit = `(95 - 47.5) * 35 = ₹1,662.5` gross. 50% capture, repeated, with defined risk, is the condor discipline.

5. Exposure ≈ `2,40,000 / 24,000 = 10` index units; one Nifty put covers **75** units — ~**7.5x**. So one lot massively **over-hedges**: a drop produces a put gain far larger than your basket loss. Index lots are **blunt** for small baskets — treat the position as a deliberately sized **tail hedge** (cheap, far-OTM, accept basis risk), not a 1:1 offset. (Trade 4.)

6. You are **not necessarily wrong — just early.** The factor hurting you is **theta**: a long strangle bleeds while the underlying sits still, *before* the catalyst. The rule: **hold through the catalyst you paid for, plus a time stop** — if both events pass with no move, cut it rather than feed the rest to theta. (Trade 5.)
