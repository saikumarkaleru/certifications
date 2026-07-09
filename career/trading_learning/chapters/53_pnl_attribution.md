# Chapter 53: P&L Attribution — Was It Direction, Theta or Vega?

At the end of a trading day your screen shows a single number: you are up ₹6,200, or down ₹11,500. That number is the *what*; it tells you nothing about the *why*. Did you make money because Nifty moved your way, because volatility spiked, or simply because a day of time decay fell into your lap as an option seller? Did you lose even though you were right on direction, because India VIX collapsed after an event and crushed the vega out of your long options? The single P&L figure hides all of this, and a trader who only watches that figure is flying blind — repeating habits without knowing which of them actually pays.

**P&L attribution** is the professional habit of breaking that one number into its sources. You split the day's profit or loss into a piece caused by the move in the underlying (delta), a piece caused by the *size* of that move (gamma), a piece from the day of time passing (theta), and a piece from the change in implied volatility (vega), with a tiny leftover for interest rates (rho). When you can say "I made ₹6,200, but it was +₹9,000 from delta, +₹2,000 from gamma, −₹4,000 from theta and −₹800 from vega," you suddenly understand your own trading. You learn whether your edge is direction, volatility, or time — and that feedback loop is what turns a punter into a professional.

## Core concepts

### Why one number is not enough

Imagine a doctor who only ever recorded a patient's total weight — no blood pressure, no temperature, no blood sugar. The weight might be stable while the patient is quietly getting sick in three ways that cancel out. Your daily P&L is exactly that lumped-together weight. Two completely different days can both produce +₹2,000: one where you were right on direction but bled theta, and one where you were wrong on direction but rescued by a volatility spike. Treat both as "a good day" and you will keep doing the thing that was actually losing money.

Attribution is the diagnostic panel. It answers a sharper question than "did I make money?" — it answers "**which of my decisions made the money, and which fought against it?**" That is the only question whose answer makes you better next time.

### The four (or five) sources of an option's daily P&L

Every option you hold changes value each day for a handful of distinct reasons, and each reason has a Greek attached to it. Recall the Greeks from Part IV:

- **Delta** — sensitivity to the underlying's price. If your position has a delta of +40 "Nifty units" and Nifty rises 100 points, the delta piece of your P&L is roughly `40 * 100 = ₹4,000`. This is the *direction* bucket.
- **Gamma** — the rate of change of delta; it captures the *curvature* or convexity of your position. On a big move, delta itself changes during the move, and gamma accounts for that. For a long-option holder gamma is a friend (a bonus on any large move, up or down); for an option seller it is an enemy (a penalty on any large move). This is the *size-of-move* bucket.
- **Theta** — the value lost (or, for a seller, gained) simply because one day passed, holding everything else fixed. This is the *time* bucket, and it is the only one you can predict almost exactly in advance.
- **Vega** — sensitivity to implied volatility, which for the index you read off India VIX. If IV rises, long options gain and short options lose; if IV falls, the reverse. This is the *volatility* bucket, and it is the one that most often surprises beginners.
- **Rho** — sensitivity to interest rates. For short-dated Nifty and Bank Nifty options this is almost always tiny — a few basis points overnight move premiums by pennies — so we note it and move on. It matters mainly for long-dated options.

The professional insight is that these buckets are *separable*. The market handed you four or five distinct bets the moment you put the trade on, whether you realised it or not; attribution simply reads back how each one paid.

### The daily P&L approximation

The whole exercise rests on one equation — a Taylor expansion of the option price, but you can read it as plain accounting. The change in your position's value over one day is approximately:

`dP ~ delta * dS + 0.5 * gamma * dS^2 + theta * dt + vega * dIV`

Read it as a sentence: *I gain delta times the move, plus a gamma bonus that grows with the square of the move, minus (or plus) theta for the day that passed, plus vega times the change in implied vol.* Each term is one bucket:

- `delta * dS` — the **delta P&L** (direction). `dS` is the change in the underlying.
- `0.5 * gamma * dS^2` — the **gamma P&L** (convexity). Because `dS` is squared, this term is always *positive for long gamma* and *negative for short gamma*, regardless of which way the market went. A big move helps the option buyer and hurts the seller, full stop.
- `theta * dt` — the **theta P&L** (time). `dt` is the fraction of a year that passed (one day is about `1/365`); if your theta is already quoted per day, just use one day. Theta is negative for long options (you pay rent) and positive for short options (you collect rent).
- `vega * dIV` — the **vega P&L** (volatility). `dIV` is the change in implied volatility in percentage points. A long-vega position gains when IV rises; a short-vega position gains when IV falls.

Add a small `rho * dr` term if you are being complete, but for weekly index options leave it in the "unexplained" pile.

### The unexplained residual — and why it is information

The formula is an *approximation*. It uses the Greeks measured at the *start* of the day, but the Greeks themselves drift as spot moves and time passes (gamma changes delta, and so on). So when you add up the four buckets they will not perfectly equal the actual P&L. The gap is the **residual** or "unexplained" P&L.

For a normal day with a modest move the residual is small and you ignore it. A *large* residual is itself a signal: the move was big enough that your first-order Greeks went stale (higher-order effects mattered). Desk risk systems report this residual every day, because a suddenly large "unexplained" number is a red flag that the position is behaving in a way the model did not predict.

### You can be right on direction and still lose

This is the single most important lesson in the chapter, and attribution is the only thing that reveals it cleanly. There are two classic ways to be *right and still red*:

1. **IV crush hits your vega.** You buy a Nifty call the evening before the RBI policy or the Union Budget, when India VIX is pumped up to 22 because everyone is hedging the event. The next morning Nifty does drift up in your favour — your delta bucket is positive. But the event has passed, and India VIX collapses from 22 to 15. Your long position has positive vega, so a −7 point IV move is a large negative vega bucket that swamps the delta gain, and your "correct" call loses money. Without attribution you would conclude "I was wrong"; with it you see the truth: *your direction call was fine; your timing relative to the volatility event was the mistake.*

2. **Theta bled faster than the move helped.** You buy a weekly ATM call on Monday expecting a rally. Nifty does inch up 30 points by Wednesday — direction correct — but late-week theta on an expiry-week option is brutal, costing more per day than a tepid 30-point drift earns through delta. Attribution shows a small positive delta bucket and a larger negative theta bucket: *you were right, but not right fast enough to beat the clock you chose.*

Both lessons are invisible in the lump-sum P&L and glaring in the attribution.

### Attribution is the feedback loop that makes you better

Here is the professional payoff. Keep an attribution log for every trade — even a simple spreadsheet of delta / gamma / theta / vega P&L per day. Over a few dozen trades, patterns emerge that no amount of staring at total P&L could reveal:

- If your **delta bucket** is consistently your biggest positive contributor, your edge is *directional* — lean into directional structures and stop overpaying for vega.
- If your **theta bucket** is the steady earner and your delta bucket is noise around zero, your edge is *time decay* — you are an insurance seller, so size and hedge like one (small, frequent premium, defined risk, respect for tail moves).
- If your **vega bucket** is where the money is made and lost, you are really a *volatility trader* — your job is to forecast IV, buying options when it is cheap relative to coming movement and selling when it is rich.
- If your edge looks like nothing in particular and your residuals are large, you may simply be taking random risk dressed up as a strategy.

This is the loop: *trade → attribute → learn which bucket is your real edge → concentrate there.* It is the difference between "I think I'm good at this" and "my data shows my edge is theta on Bank Nifty credit spreads, and it is not direction."

### Position attribution, not just single options

Real positions are spreads and multi-leg structures, and the beauty of the Greeks is that they *add up*. You attribute a whole position by using its **net delta, net gamma, net theta and net vega** in the same formula — no need to go leg by leg. An iron condor, for example, is typically net short gamma, short vega and long theta: attribution on a calm day shows a nice positive theta bucket and near-zero everything else, while a violent-move day shows the gamma and delta buckets turning sharply negative — exactly the risk you sold.

## Worked example (₹, Nifty/Bank Nifty)

You are running a short-volatility income position: a **Nifty short straddle** sold on Monday of expiry week. You sold one lot each of the 24,000 call and the 24,000 put, with Nifty spot exactly at 24,000 and India VIX at 14. One lot is 75 (lot sizes change over time; we use 75 here). For the *whole position* (call + put, and remember you are **short**, so the signs flip from a long holder), the opening net Greeks per share are roughly:

- Net delta = **0** (a straddle struck at-the-money is delta-neutral to begin with)
- Net gamma = **−0.005** (short options means short gamma — a big move hurts you)
- Net theta = **+₹14 per day** (you *collect* time decay; this is the engine of the trade)
- Net vega = **−₹11 per IV point** (short options means short vega — you profit if IV falls, lose if it rises)

You collected a combined premium of about ₹250 per share, i.e. `250 * 75 = ₹18,750` for the lot.

**The next day (Tuesday): Nifty falls 120 points to 23,880, and India VIX rises 2 points to 16.** Your P&L screen shows the position is down ₹6,000-odd for the lot. Why? Let us attribute it, per share, using the opening Greeks and `dS = −120`, one day passed, `dIV = +2`.

- **Delta bucket:** `delta * dS = 0 * (−120) = ₹0` per share. You started delta-neutral, so the *first-order* direction effect is nil. (This is the point of a straddle: at inception you are not betting on direction.)
- **Gamma bucket:** `0.5 * gamma * dS^2 = 0.5 * (−0.005) * (−120)^2 = 0.5 * (−0.005) * 14,400 = −₹36` per share. This is the sting of being short gamma: the 120-point move hurt you, and it would have hurt you the same amount if Nifty had *risen* 120 points, because the move is squared. This is the convexity penalty the option seller always pays on a large move.
- **Theta bucket:** `theta * dt = +₹14` per share for the one day that passed. This is the rent you collected — the reward for being short options. It is working for you exactly as designed.
- **Vega bucket:** `vega * dIV = (−11) * (+2) = −₹22` per share. India VIX rose 2 points, and you are short vega, so rising fear cost you. A falling market that *also* spikes volatility is the short straddle's nightmare — both gamma and vega bite at once.

**Add them up:** `0 + (−36) + 14 + (−22) = −₹44` per share. Per lot: `−44 * 75 = −₹3,300`.

But your screen said roughly **−₹6,000**, not −₹3,300. The difference, about −₹2,700 for the lot (−₹36 per share), is the **residual**. Where did it come from? The move was large enough that your delta did *not* stay at zero during the fall — short gamma dragged your delta negative as Nifty dropped, so by day's end you were genuinely short delta into a falling market, a real directional loss the "delta = 0 at the open" term completely missed. A large residual on a big-move day is the tell-tale sign that your opening Greeks went stale mid-move — and here it screams the central risk of a short straddle: *short gamma turns your neutral position directional in exactly the wrong direction.*

**What the attribution taught you:**

- The **theta bucket (+₹14)** confirms the trade's edge is real and paying as designed — you are an income/decay trader here.
- The **gamma bucket (−₹36)** and **large residual** show that a single 120-point day can wipe out two-plus days of theta. You earn ₹14 a day but lost ₹36 to gamma on one ordinary move; you need calm days to win, and a few violent ones undo a week of grind.
- The **vega bucket (−₹22)** shows you were also short volatility into a VIX spike — note for next time: avoid selling straddles when India VIX is unusually low and likely to mean-revert up, and avoid holding short vega into events.

The lump number "−₹6,000" taught you nothing; the attribution taught you that your decay edge is real, but your gamma and vega exposures are what will eventually hurt you — and exactly which conditions to fear.

## Common mistakes / risk note

- **Judging a trade by total P&L alone.** The classic error. A green day from a lucky VIX move and a green day from genuine directional skill look identical on the screen and are *completely different* lessons. Without attribution you cannot tell skill from luck, and you will scale up the wrong thing.
- **Using stale Greeks for a big move.** The `dP` formula uses Greeks measured at the *start* of the day. On a large move they go stale fast, the residual balloons, and the attribution misleads. For big-move days, recompute Greeks intra-day or treat the residual as real (it is) and investigate it rather than ignoring it.
- **Forgetting the gamma term is squared.** Beginners attribute a loss entirely to "the market went against me" (delta) and miss that, if they were short gamma, a large chunk of the loss was the *size* of the move, not its direction. Short gamma loses on a big move *either way*.
- **Mistaking an IV-crush loss for a bad directional call.** Being right on direction and still losing because vega collapsed after an event is one of the most demoralising — and most *misdiagnosed* — outcomes for Indian retail traders around RBI policy, Budget, and big earnings. Attribution prevents you from "fixing" your direction process when the real fix is your volatility timing.
- **The honest risk.** Attribution is a diagnostic, not a shield. It explains losses; it does not prevent them. The short straddle in our example is a defined illustration of *undefined risk* — option selling collects steady theta but exposes you to large, occasionally savage gamma and vega losses on a single bad day. SEBI studies show roughly nine in ten retail F&O traders lose money, frequently because they collected small premiums for months and gave it all back (and more) on one gap move. Attribution will tell you, precisely and honestly, when that has happened — but only you can size the position so that it does not end your account.

## Key takeaways

- P&L attribution breaks a day's single profit/loss number into separate buckets — delta (direction), gamma (size of move), theta (time), vega (volatility), and a tiny rho (rates) — so you understand *why* you made or lost money.
- The workhorse formula is `dP ~ delta*dS + 0.5*gamma*dS^2 + theta*dt + vega*dIV`, with each term mapping to one Greek bucket.
- The gamma term is squared, so it always helps a long-option holder and always hurts a seller on a big move, regardless of direction.
- You can be **right on direction and still lose** — most often via an IV crush (negative vega) after an event, or via theta bleeding faster than a slow move helped.
- The leftover "residual" after adding the buckets is information: a large residual means your opening Greeks went stale on a big move, a warning that the position turned more directional than you intended.
- Attribute whole positions using their *net* Greeks; spreads and structures add up cleanly.
- Logging attribution trade after trade is the feedback loop that reveals whether your real edge is direction, theta, or vega — and lets you concentrate where you actually have an edge.

## Practice problems

1. **Conceptual.** A trader buys a Nifty call the night before the Union Budget when India VIX is 23. The next day Nifty rises modestly, yet the call loses money. Using the language of attribution, name the bucket most likely responsible and explain why the (positive) delta bucket was not enough.

2. **Numeric.** You are *long* one Nifty 24,000 call with these opening Greeks per share: delta = 0.50, gamma = 0.004, theta = −₹9/day, vega = ₹6. Overnight Nifty rises 100 points and India VIX falls 1 point. One day passes. Attribute the change in premium per share into its four buckets and give the net.

3. **Numeric.** Continue Problem 2. The call's *actual* new premium turned out to be ₹172, having started at ₹130. Compute the residual (unexplained P&L per share) and give one reason it is non-zero.

4. **Conceptual.** Two income traders each made ₹3,000 today. Trader A's attribution shows +₹3,200 theta, −₹200 everything else. Trader B's shows +₹100 theta, +₹4,000 vega, −₹1,100 delta. Both are "up ₹3,000." Describe what each trader's real edge (or luck) was today, and what each should worry about.

5. **Numeric.** A short Bank Nifty position has net gamma = −0.002 per share and net theta = +₹25/day. Bank Nifty moves 400 points in a day (direction irrelevant for this part). Compute the gamma bucket and compare it to one day's theta. How many days of theta did this one move cost?

6. **Conceptual / risk.** Your attribution log over 30 trades shows your delta bucket averages near zero with high variance, while your theta bucket is consistently positive and small. What is your real edge, and name one change to your strategy and one risk you must respect.

## Solutions

1. The culprit is the **vega bucket**. Before the Budget, India VIX was elevated at 23 because traders were buying protection into the event, so the call carried a rich, vega-heavy premium. Once the Budget passed and uncertainty resolved, IV collapsed (an "IV crush") — say from 23 toward the mid-teens. The trader's long call has positive vega, so a large fall in IV produces a big negative vega bucket. Even though the delta bucket was positive (Nifty rose modestly in the trader's favour), the small favourable move could not generate enough delta P&L to offset the large vega loss from the collapsing volatility. The direction call was fine; the mistake was paying inflated, vega-rich premium right before a known volatility-crushing event.

2. With `dS = +100`, one day passed, `dIV = −1`:
   - Delta bucket: `0.50 * 100 = +₹50`
   - Gamma bucket: `0.5 * 0.004 * 100^2 = 0.5 * 0.004 * 10,000 = +₹20`
   - Theta bucket: `−₹9`
   - Vega bucket: `6 * (−1) = −₹6`
   - Net ≈ `50 + 20 − 9 − 6 = +₹55` per share. The position gained, driven by the delta and gamma buckets (a favourable, decent-sized move), partly offset by theta and a small vega drag from the calmer market.

3. The formula predicted a change of +₹55, so a predicted premium of `130 + 55 = ₹185`. The actual premium was ₹172, an actual change of `172 − 130 = +₹42`. The **residual** is `actual − predicted = 42 − 55 = −₹13` per share. It is non-zero because the Greeks used were the *opening* values; over a 100-point move the option's delta and gamma changed during the day (the position's higher-order behaviour, and a slightly larger effective vega/theta interaction, are not captured by start-of-day Greeks). A −₹13 residual on a 100-point move is modest but real, and it reminds you that first-order attribution is an approximation that frays as moves get larger.

4. **Trader A** earned almost everything from theta (+₹3,200) with negligible contribution from anything else. A's real edge today was *time decay* — A is functioning as a disciplined option seller / income trader, and the day's profit reflects the strategy working as designed. A should worry about gamma and vega tail risk: the days that will hurt A are big-move or IV-spike days, where the theta engine gets overwhelmed. **Trader B** made the money on *vega* (+₹4,000), while actually losing on direction (−₹1,100) and earning almost no theta. B was not running an income edge at all today — B got paid by a volatility move, which may be skill (a deliberate long-vega bet that paid) or luck (a coincidental IV spike). B should worry that the result is not repeatable unless B can genuinely forecast IV, and that the negative delta bucket shows B's directional read was actually wrong today. Same ₹3,000, completely different stories — which is the whole point of attribution.

5. Gamma bucket: `0.5 * gamma * dS^2 = 0.5 * (−0.002) * 400^2 = 0.5 * (−0.002) * 160,000 = −₹160` per share. One day of theta is +₹25. So this single 400-point move cost `160 / 25 = 6.4` **days of theta**. In other words, more than a week of patient premium collection was wiped out by one large move — the defining danger of a short-gamma income position. Note the loss is −₹160 regardless of whether Bank Nifty rose or fell 400 points, because the move is squared.

6. Your real edge is **theta / time decay**, not direction. The delta bucket averaging near zero with high variance means your directional calls are essentially noise — you are not adding value by predicting market direction, and the variance is just risk you are taking without reward. The consistently positive, small theta bucket is where your genuine edge lives: you are effectively selling insurance and collecting premium. **One change:** stop taking directional bets (keep the position delta-neutral or close to it through hedging), and concentrate on well-structured premium-selling such as defined-risk credit spreads or iron condors, sized for steady theta. **One risk to respect:** you are short gamma and likely short vega, so a single large gap move or an India VIX spike can erase many days — even weeks — of accumulated theta in one session (as Problem 5 quantifies). Size small, define your risk, and never sell so much premium that one bad day ends the account.
