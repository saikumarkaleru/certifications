# Scenario Decision Drills I

Reading a chart in isolation is easy. Making the *right decision* under live pressure — with money at risk, an open position bleeding, and the clock ticking toward 3:30 PM — is the skill that separates traders who survive from traders who donate. This chapter is a decision gym. Each drill puts you inside a specific, realistic Indian-market situation and forces a choice: enter, wait, add, trim, exit, reverse, or stand aside. Then the answer key walks the reasoning — not just *what* the textbook says, but *why* one action has positive expectancy and the others quietly leak capital.

Treat this like a mock exam. Cover the answer, commit to a decision **out loud** (or on paper), assign yourself a position size and a stop, and only then read the key. The discipline of pre-committing before you see the "solution" is exactly the muscle you need on the desk. A drill you passively read teaches nothing; a drill you answer wrongly and then understand teaches more than ten you get right.

## How to use these drills

- **Decide, don't hedge.** "I'd probably wait but maybe enter" is not an answer. Pick one action and one number.
- **Always state your invalidation.** Every entry needs a stop *level*, not a feeling. If you can't name the level, you can't take the trade.
- **Score yourself honestly.** Right action, wrong reason = half marks. In markets the reason is what repeats; the outcome of one trade is noise.
- **India context is baked in.** Levels, gaps, expiry effects, STT, and circuit rules matter. A US-style answer that ignores Thursday expiry or a 20% circuit is wrong here.

A passing grade is 70%+ *with sound reasoning*. Below that, you're pattern-matching shapes without understanding the auction beneath them.

---

## Drill 1 — Nifty gaps up into resistance

**Scenario.** Nifty closed Friday at 24,180. Over the weekend, positive global cues; Monday it opens gap-up at 24,410, printing directly into a well-tested supply zone at 24,400–24,450 that has rejected price three times in the last month. First 15-minute candle is a small-bodied doji with a long upper wick, closing at 24,390. India VIX is 12.5 (low). What do you do?

**Options:** (A) Buy the breakout above 24,450. (B) Short the rejection at resistance with a stop above 24,470. (C) Wait for the first 15-min candle to complete and see a follow-through. (D) Stand aside.

**Answer: B (with tight risk) — or C if you want confirmation.** The gap opened *into* known supply, not through it. A doji with a long upper wick at a thrice-tested resistance is the classic exhaustion signal: buyers pushed, sellers slapped it down. The highest-probability play is a fade — short near 24,400–24,410 with a stop just above the zone at 24,470 (risk ~60 points), targeting the gap-fill back toward 24,250–24,180. Low VIX means moves are orderly, favouring mean-reversion into the gap. **A is the trap:** buying a breakout *at* resistance on the first candle, into a low-volatility tape, is how you get filled at the high of the day. **D is defensible** but leaves a high-quality R:R fade on the table. If you lack confidence, **C** — wait for the 15-min close below 24,350 to confirm sellers have control — is the disciplined middle path.

---

## Drill 2 — Bank Nifty trend-day pullback

**Scenario.** Bank Nifty is in a clean intraday uptrend: higher highs, higher lows on the 15-min, price riding above a rising 20-EMA all session. It's 1:15 PM. Price pulls back from 52,300 to tag the 20-EMA at 52,090, printing a bullish hammer on the 15-min with a pickup in volume. You are flat. What do you do?

**Options:** (A) Go long on the hammer close, stop below the hammer low. (B) Wait for a break of the prior high at 52,300 before entering. (C) Short, expecting the trend to reverse. (D) Stand aside — the day is too old.

**Answer: A.** This is the highest-quality setup in intraday trading: the *trend-day pullback to a dynamic support*. Bank Nifty has demonstrated all session that dips get bought. Price has returned to the rising 20-EMA — the exact zone institutional trend-followers reload — and printed a hammer on rising volume, meaning buyers stepped in aggressively at the low. Enter long on the hammer's close (~52,120), stop below the hammer low (~52,040, risk ~80 pts), first target the day's high 52,300, then trail. **B** costs you the best part of the move; you're chasing the same trade 180 points higher with a wider stop. **C** is trend-fighting suicide — you never short a strong trend day into support on nothing but "it's gone up a lot." **D** ignores that 1:15 PM still leaves two hours of trend for continuation and a possible closing-hour push.

---

## Drill 3 — The failed breakout (bull trap)

**Scenario.** Reliance has consolidated between 2,940 and 2,980 for six sessions. At 10:40 AM it breaks out to 2,995 on decent volume. You buy the breakout at 2,992. Within 25 minutes price slips back to 2,978 — below the breakout level of 2,980 — and is now sitting at 2,974 on rising volume. What do you do?

**Options:** (A) Hold — breakouts often retest. (B) Add more; it's cheaper now. (C) Exit immediately; the breakout failed. (D) Reverse and go short.

**Answer: C (and a strong case for D).** The single most important rule of breakout trading: **a breakout that closes back inside the range is a failed breakout, and failed breakouts move fast in the opposite direction** because trapped longs must puke. Price is not "retesting" — it has re-entered the range and is *accelerating lower on rising volume*, the signature of a bull trap. Your original thesis (buyers in control above 2,980) is objectively invalidated. Cut the trade at 2,974 for a small, planned loss. **A is the rationalisation that turns a ₹18 loss into an ₹80 loss** — "it'll retest" is what everyone tells themselves on the way down. **B (averaging down)** is the cardinal sin: adding to a losing position on a broken thesis. **D (reverse short)** is the professional's move: the failed breakout targets the *other* side of the range (2,940), and trapped longs are your fuel — but only take it if your rules pre-allow reversals and you can define a stop back above 2,995.

---

## Drill 4 — Expiry-day theta on a range

**Scenario.** It's Thursday, weekly Nifty expiry, 1:45 PM. Nifty has been dead-flat between 24,050 and 24,120 all afternoon. India VIX is 11. You believe it will stay in the range into 3:30 PM. Spot is 24,085. What's the highest-expectancy structure?

**Options:** (A) Buy an ATM straddle. (B) Sell an ATM straddle / short strangle. (C) Buy a 24,200 call, betting on a breakout. (D) Stand aside.

**Answer: B — sell premium (with defined risk via an iron condor if you're not experienced).** On expiry afternoon in a tight range with low VIX, **theta decay is violent** — ATM options are bleeding time value by the minute and will expire near worthless if spot pins. Selling the ATM straddle (or, safer, an iron fly / condor to cap tail risk) harvests that decay. This is the textbook expiry-pin play. **A is the worst choice:** buying a straddle at 1:45 PM on expiry is paying full price for an asset whose value evaporates in the next 105 minutes — you need a huge move just to break even. **C** shares the same disease plus needs a directional breakout you have no evidence for. **D** is fine for a beginner — naked straddle selling has unlimited risk and a stray news-driven spike can wreck you — but if you're structuring it defined-risk, B is where the edge lives. *Honest caveat:* the pin can break. Always cap risk on expiry; a single gap through your short strike near close, with STT on exercised ITM options, can turn a "safe" range trade into a real loss.

---

## Drill 5 — Divergence without a trigger

**Scenario.** Nifty makes a fresh intraday low at 23,880 at 11:30 AM, but the 14-period RSI on the 15-min prints a *higher* low than it did at the previous price bottom — a clear bullish divergence. Price is currently 23,895. You are flat and itching to go long. What do you do?

**Options:** (A) Buy now on the divergence. (B) Wait for a price-based confirmation trigger before entering. (C) Short — the trend is still down. (D) Stand aside entirely.

**Answer: B.** Divergence is a **warning, not a signal.** It tells you downside momentum is weakening; it does *not* tell you the reversal has begun. Markets can keep making lower lows with divergence for a long time ("divergences can persist"), and traders who buy the first divergence in a downtrend get repeatedly stopped. The disciplined play is to wait for *price* to confirm the momentum shift: a break of the most recent minor swing high, a bullish engulfing on the 15-min, or a reclaim of the 20-EMA. Then enter with a stop below the divergent low (23,860). **A jumps the gun** — you're anticipating, not reacting, and you'll be right often enough to feel smart and wrong badly enough to lose money. **C ignores the tell** that the trend is exhausting. **D** is over-cautious; the divergence is real information, you simply need price to ratify it.

---

## Drill 6 — News gap you didn't expect

**Scenario.** You are holding an overnight long in an IT stock, Infosys, from 1,880 (100 shares). Pre-market, the company issues a weak guidance cut. The stock indicates a gap-down open at 1,760 — a ₹120 gap, straight through your mental stop of 1,840. It's 9:15 AM, opening tick 1,758. What do you do?

**Options:** (A) Hold and hope it recovers the gap. (B) Exit at market immediately. (C) Average down at 1,760. (D) Wait 30 minutes for the dust to settle, then decide.

**Answer: B — or a disciplined variant of D, never A or C.** Your thesis is broken by a fundamental event, and the stock has gapped *far* through your stop. The gap did not "trigger" your stop at 1,840 — it leapt over it, which is exactly why stops on individual stocks over news are imperfect. The core principle: **when the reason you owned it is gone, own it no longer.** Exit at market and accept the ₹120/share loss (₹12,000). It hurts, but guidance cuts start *downtrends*, not one-day dips. **A ("hope for the gap-fill")** is how a ₹12,000 loss becomes a ₹30,000 loss as the stock grinds to 1,650 over the week. **C (averaging down into bad news)** is doubling your exposure to a deteriorating story — catastrophic. **D can be acceptable** *only* as a structured plan: give it the first 15-min candle, and if it can't reclaim 1,780 with strength, exit — but this must be a rule, not an excuse to freeze. The default professional answer is B.

---

## Drill 7 — The runaway you're not in

**Scenario.** Adani Ports opens strong and by 10:00 AM is up 4.5% on 3x average volume, making new intraday highs with barely a pullback — a momentum runaway. You missed the entry. Price is 1,412, extended well above the opening range and the VWAP (which sits at 1,375). FOMO is screaming. What do you do?

**Options:** (A) Buy now; strong stocks get stronger. (B) Wait for a pullback to VWAP or a consolidation, then enter. (C) Short it — it's overextended. (D) Stand aside for the rest of the day.

**Answer: B (or D — never A into extension, never C).** The stock is genuinely strong, so the *directional read* is right — but chasing 37 points above VWAP means buying with a stop that's either too tight (instant shakeout) or too wide (terrible R:R). The professional waits for the market to offer a better price: a pullback toward VWAP (1,375–1,385) or a sideways flag that resets momentum, then enters with a stop below the consolidation. Momentum stocks *do* pull back intraday, and patience converts a bad entry into a good one. **A (chasing the extension)** is the FOMO tax — you'll buy the exact tick before the first shakeout. **C (shorting strength)** is the amateur "it's too high" reflex; overextended can get more overextended, and you never front-run a 3x-volume trend. **D** is honest and fine — if no clean pullback comes, the correct number of shares is zero. A trade you missed is not a loss; a bad chase is.

---

## Drill 8 — Support that keeps getting tested

**Scenario.** Tata Motors has bounced off 980 three times this week. Each bounce is weaker — 980 → 1,010, then 980 → 998, then 980 → 991. Right now it's sitting at 982 for the fourth test, volume picking up. You're deciding whether to buy the bounce again. What do you do?

**Options:** (A) Buy the bounce; support is support. (B) Stand aside or prepare to short the breakdown. (C) Buy with a wider stop this time. (D) Buy a bigger size — it's "guaranteed" to bounce.

**Answer: B.** Read the *quality* of the bounces, not just the level. Each rally off 980 is progressively feebler — buyers are exhausting while sellers keep pressing. **The more times a support is tested, the weaker it becomes**, because each test consumes the resting bids. The pattern of lower highs into a flat support is a descending triangle — a bearish continuation that usually *breaks down*. The edge here is to stand aside or, better, prepare to short a decisive 15-min close below 980 (targeting the measured move down), with a stop back above the last minor high. **A treats support as a permanent floor** — it isn't; it's a supply of orders being eaten. **C (wider stop)** just enlarges the loss when it breaks. **D (bigger size on "guaranteed")** is the sentence that precedes account blow-ups; nothing in markets is guaranteed, and conviction is highest right before support fails.

---

## Drill 9 — Two setups, one capital slot

**Scenario.** At 9:45 AM you have capital for exactly one intraday trade. Setup 1: HDFC Bank, a clean flag breakout above the opening range on 2x volume, R:R ~2.5:1, sector (banks) leading. Setup 2: a midcap pharma name, a possible double-bottom but volume is thin and the sector is red on the day, R:R ~1.8:1. Which do you take?

**Options:** (A) Setup 1. (B) Setup 2. (C) Both, half size each. (D) Neither.

**Answer: A.** When capital forces a choice, rank by *confluence and probability*, not by which chart is prettier or which promises a bigger jackpot. Setup 1 wins on every axis: cleaner pattern, stronger volume confirmation, better R:R, and — critically — **sector alignment** (a leading sector lifts its heavyweights; trading *with* sector flow is a tailwind). Setup 2 is fighting a red sector on thin volume, which weakens both the pattern's reliability and your exit liquidity. **C (splitting)** is a classic error: diluting into a weaker second idea *lowers* your blended expectancy and doubles your monitoring load for no benefit. **D** is too passive when a genuinely A-grade setup is on the table. Concentrate capital in your best idea.

---

## Drill 10 — The stop that's about to be hit

**Scenario.** You're long Nifty futures from 24,000, stop at 23,940. Price grinds down to 23,955. Nothing has happened structurally — no news, no breakdown of a major level, just drift. You feel the urge to "give it more room" and move the stop to 23,900. What do you do?

**Options:** (A) Move the stop to 23,900 to avoid a whipsaw. (B) Leave the stop at 23,940. (C) Exit now at 23,955 before the stop hits. (D) Add to the position to lower your average.

**Answer: B.** Your stop was placed with a clear head *before* you were in pain. Now, in the heat of a drawing-down position, your emotional brain wants to move it. **Widening a stop to avoid being stopped out is the single most destructive habit in retail trading** — it converts a defined, survivable loss into an open-ended one, and it trains you to never respect your own risk. The stop at 23,940 represents your invalidation level; if it's hit, your thesis was wrong, full stop. Leave it. **A is the trap dressed as prudence.** **C (panic-exiting at 23,955)** is the opposite error — jumping out before your level on fear, denying the trade the room you already, rationally, allotted it. **D (averaging down)** breaks the same rule as widening the stop, plus increases size into weakness. The only acceptable stop *move* is a trailing stop *tighter* to protect profit, never wider to postpone a loss.

---

## Drill 11 — Opening range on a gap day

**Scenario.** Nifty gaps down 90 points to open at 23,910 (prior close 24,000). For the first 15 minutes it carves an opening range: high 23,930, low 23,875. At 9:31 AM it breaks *below* 23,875 on expanding volume, and the gap above (23,930–24,000) now acts as overhead supply. You're flat. What do you do?

**Options:** (A) Buy, betting on a gap-fill back to 24,000. (B) Short the opening-range breakdown, stop above 23,930. (C) Wait for a pullback to VWAP and reassess. (D) Stand aside.

**Answer: B (with C as a lower-aggression alternative).** A gap-down that *breaks the opening-range low* on rising volume is a "trend-from-open" short: sellers rejected the open, the unfilled gap sits overhead as a supply cap, and momentum points down. Short the ORL break near 23,870, stop just above the OR high / into the gap at 23,935, target the next support / VWAP-extension below. **A (fading for a gap-fill)** is a hope trade against fresh momentum — gap-fills happen, but not while price is breaking *down* out of its opening range; you're catching a falling knife. **C is legitimate** if you prefer to short a *pullback* to VWAP rather than the initial break — often a better price with a tighter stop — accepting you might miss a runaway. **D** leaves a clean, high-momentum setup unplayed. The read is bearish; the only question is aggressive-now (B) versus patient-pullback (C).

---

## Drill 12 — Profit target hit, momentum still strong

**Scenario.** You're long a stock from 500 with a target of 520; it's now trading 521, target achieved, but the tape is *strong* — new highs, rising volume, sector on fire. Your plan said exit at 520. What do you do?

**Options:** (A) Exit fully at 521 as planned. (B) Hold the whole position for more. (C) Book part, trail the rest. (D) Add more, momentum is your friend.

**Answer: C — scale out and trail.** This resolves the eternal tension between *honouring your plan* and *not amputating a winner*. Book a portion (say half or two-thirds) at your planned 520–521 target to lock the win and satisfy the discipline of your plan, then trail a stop under the rising structure (e.g., under the last 15-min swing low or the 20-EMA) on the remainder to capture the extended move. This is how professionals let winners run without giving back everything. **A (full exit)** is disciplined and never *wrong* — but it caps a runner that the tape is telling you has more in it. **B (holding all)** abandons your plan entirely and risks a full round-trip if momentum snaps. **D (adding at new highs beyond target)** increases risk at the worst R:R point of the trade, converting a booked winner into a fresh, poorly-located position. Scaling out is the answer that respects both the plan and the trend.

---

## Drill 13 — The choppy, directionless tape

**Scenario.** It's a Wednesday, 12:30 PM. Nifty has whipsawed all morning in a 40-point band, printing three false breakouts in both directions. India VIX is 10.5 and falling. You've already taken two small losses on failed breakouts today. What do you do?

**Options:** (A) Keep trading breakouts; the next one will work. (B) Stop trading directional breakouts; switch to range-fade or stand aside. (C) Increase size to make back the losses. (D) Trade the exact same setup, opposite direction.

**Answer: B.** The market is *telling you what it is*: a low-volatility, mean-reverting chop where breakouts fail. The professional reads the environment and **stops applying a breakout strategy to a range regime.** Either switch approach — fade the extremes of the band (short the top, buy the bottom) with tight stops — or, better after two losses, stand aside and preserve capital and mental clarity until the tape offers trend. **A is the definition of insanity** — repeating a losing setup in a hostile regime. **C (revenge-sizing) is account death** — increasing risk to recoup losses is emotional, not strategic, and turns a bad morning into a catastrophic day. **D** at least acknowledges the environment but blindly flipping the same mechanical setup ignores the real issue: the *regime*, not the direction, is wrong. When the market isn't paying your strategy, the highest-expectancy trade is often no trade.

---

## Drill 14 — Reversal candle at a daily level

**Scenario.** SBIN has rallied for five straight sessions into a major daily resistance at 640 (a prior swing high). Today it spikes to 644 intraday then reverses hard, closing at 628 — a large bearish engulfing / shooting-star on the daily, on the highest volume in two weeks. You hold a swing long from 605. What do you do?

**Options:** (A) Hold; one red candle in an uptrend is normal. (B) Book profits — the reversal signal at resistance is significant. (C) Add to the long on the dip. (D) Reverse to a full short position.

**Answer: B (book the swing) — with D only for aggressive traders who can define risk.** A high-volume bearish engulfing that *rejects a major daily resistance* after an extended five-day run is a textbook exhaustion/distribution signal. You have a fat, realised profit (605 → 628 = ₹23) and the highest-probability path now is a pullback. Booking here honours the signal and protects a winner near a logical top. **A ("normal pullback")** underestimates the confluence — this isn't a random red candle, it's a rejection at resistance on peak volume after an over-extended move, which is precisely where uptrends pause or reverse. **C (adding at resistance into a bearish engulfing)** is exactly backwards — you'd be increasing size at the worst possible location. **D (full reversal short)** is playable for experienced traders — the setup supports a short toward 605/590 with a stop above 644 — but flipping a swing position requires conviction and a hard stop; for most, cleanly booking the long is the right, low-regret call.

---

## Interview-ready summary

If an interviewer hands you these scenarios, the meta-principles beneath every correct answer are:

1. **Location over prediction.** Where price sits relative to support, resistance, VWAP, and the gap matters more than any indicator. Fade extensions into supply; buy pullbacks to support in trends.
2. **Confirmation before anticipation.** Divergences and support levels are *context*; wait for price to trigger. Anticipating gets you filled early and stopped often.
3. **Failed patterns are the best signals.** A failed breakout / breakdown moves fast the other way because trapped traders must exit. Reversing on a failure is high-expectancy.
4. **Never widen a stop, never average down a broken thesis, never revenge-size.** These three habits, more than any missed setup, are what empty retail accounts.
5. **Read the regime.** Trend day → buy pullbacks. Range/chop → fade or stand aside. Expiry range → sell theta with capped risk. Applying the wrong strategy to the regime is the deepest error of all.
6. **Scale out of winners; cut losers whole.** Book part at target and trail the rest; exit losers in one clean decision when the thesis breaks.

Score yourself, note which *reasons* you got wrong (not just outcomes), and re-run the drills in a week. The goal is that these decisions become reflexive — because on the live desk, you won't have time to deliberate.
