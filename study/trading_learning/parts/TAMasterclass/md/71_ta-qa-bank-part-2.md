# TA Question Bank Part 2 (Patterns, Derivatives, Scenarios)

## What it is & why it works

Part 1 drilled the concepts and the indicator toolkit. Part 2 is the half of the technical-and-derivatives interview that gets you hired or exposed: **chart patterns**, the **option-chain / open-interest** layer that Indian markets now trade around, and **live scenario questions** where an interviewer describes a situation and watches you reason in real time.

This block works as a learning tool because pattern recognition and derivatives reasoning are exactly the skills that *look* easy on a printed chart and *feel* impossible under a "what would you do right now?" question. Anyone can circle a head-and-shoulders after it completed; the test is whether you can say, mid-formation, "this *could* be a right shoulder, here's what would confirm it, here's what would invalidate it, and here's where my risk sits." The market behaviour underneath every good pattern answer is the same: patterns are just structured pictures of accumulation, distribution, and the trapping of one side of the market. A double top is not a shape — it is buyers failing twice at a level while sellers defend it, and a cohort of longs getting trapped near the highs whose stops become fuel for the breakdown. When you answer from that order-flow story rather than from the picture, your answers survive follow-ups.

The derivatives layer is non-negotiable in India in 2026. Nifty, Bank Nifty and Fin Nifty weekly and monthly options, and the option chain's OI, are where positional conviction actually shows up. A technician who can't read max-pain, PCR, OI build-up and IV is only seeing half the tape. So Part 2 deliberately fuses price patterns *with* the option chain, because that fusion is what a technical-and-derivatives research analyst is paid to do.

## The mechanics — how to use this bank

Same shape as Part 1: **Q**, **A**, and a **Why / trap** where it earns its place. Difficulty tags **[F]/[I]/[A]**. Scenario questions are tagged **[S]** and are answered as a *reasoning process*, not a single fact, because that is what interviewers grade.

| Tag | Level | What it tests |
|-----|-------|---------------|
| [F] | Foundational | Pattern definition, OI basics |
| [I] | Intermediate | Confirmation rules, measured moves, chain reading |
| [A] | Advanced | Failures, traps, IV/greeks nuance |
| [S] | Scenario | Live reasoning under a described situation |

India levels assume 2026: Nifty ~23,000–27,000, Bank Nifty ~50,000–58,000, Fin Nifty ~24,000–27,000. Adjust arithmetic, keep the logic.

### Block A — Reversal patterns

**Q1 [F]. Describe a head-and-shoulders top and its measured move.**
A: Three peaks — left shoulder, higher head, lower right shoulder — sharing a neckline drawn across the intervening lows. It confirms on a *close* below the neckline (ideally on rising volume). Measured target = neckline minus the head-to-neckline height, projected down. Right-shoulder volume lighter than the head is the tell that buying is exhausting.

**Q2 [I]. On Nifty daily: head at 25,600, neckline at 24,900. Neckline breaks. Target?**
A: Height = 25,600 − 24,900 = 700. Target = 24,900 − 700 = **24,200**. Entry on the neckline break (or the retest of 24,900 as new resistance — Part 1 polarity), stop above the right shoulder, e.g., ~25,200. Risk ~300 for a ~700 reward ≈ 1:2.3.

**Q3 [I]. Double top vs double bottom — confirmation and the common mistake.**
A: Double top: two peaks at ~same level, confirmed on a close below the intervening trough (the "neckline"); target = height projected down. Double bottom mirror. *Mistake:* trading the second touch of the level as if the pattern is already done — it isn't a double top until the trough breaks; until then it's just resistance being tested.

**Q4 [A]. Why do so many "textbook" head-and-shoulders fail in Nifty?**
A: Because they're spotted and traded by everyone, so stops cluster just below the neckline — making the neckline a magnet for a stop-hunt wick that then reverses (a bear trap). Pros filter with: a *close* (not a wick) below, volume confirmation, a broader-market/Bank Nifty confirmation, and often they prefer to sell the *retest* of the broken neckline rather than the break itself, so a fakeout doesn't catch them.

**Q5 [I]. What's a rounding top / bottom and where does it show up on NSE?**
A: A slow, arc-shaped transfer of control (distribution/accumulation) with no sharp pivot — common in large, slow-moving names (some PSU and FMCG leaders) and in indices after extended trends. It signals a gradual regime change; because there's no clean neckline, traders use a horizontal break of the arc's base/rim as the trigger.

### Block B — Continuation patterns

**Q6 [F]. Flag vs pennant — the difference.**
A: Both are brief consolidations after a sharp move (the "pole"). A flag is a small rectangular channel sloping against the trend; a pennant is a small symmetrical triangle. Both resolve in the direction of the pole; measured target = pole height added to the breakout.

**Q7 [I]. Reliance runs from ₹1,300 to ₹1,450 (the pole), then drifts down to ₹1,410 in a tight channel on falling volume. Read and target?**
A: A bull flag — sharp advance, shallow counter-trend drift, contracting volume (healthy). Long on a break above the flag high (~₹1,435) with volume; measured target = pole (1,450−1,300 = 150) added to breakout ≈ **₹1,585**; stop below the flag low (~₹1,400).

**Q8 [I]. Symmetrical, ascending, descending triangle — bias of each.**
A: Ascending (flat top, rising lows) = bullish bias (buyers getting more aggressive). Descending (flat bottom, falling highs) = bearish bias. Symmetrical (converging both sides) = neutral, trades in the direction of the eventual break, usually continuing the prior trend. Measured move = the triangle's widest height projected from the breakout.

**Q9 [A]. Why is "the earlier the breakout within the triangle, the more reliable"?**
A: A triangle breakout in the first 50–70% of the pattern (before the apex) tends to have momentum behind it. Near the apex, energy has dissipated and price often just drifts out sideways or produces a weak, fakeout-prone break. Late-apex breaks are the ones that whipsaw.

**Q10 [I]. What is a cup-and-handle and its India caveat?**
A: A rounded base (cup) followed by a small pullback (handle), then breakout above the rim — a bullish continuation/base pattern. Target = cup depth added to the breakout. India caveat: it needs a liquid, trending name and can take months; forcing it on illiquid mid/small-caps produces false reads because low liquidity distorts the shape.

### Block C — Candlesticks & price action

**Q11 [F]. Bullish engulfing, hammer, shooting star — one line each.**
A: *Bullish engulfing:* a green body fully engulfing the prior red body at a low — demand overwhelming supply. *Hammer:* small body, long lower wick at a downtrend low — rejection of lower prices. *Shooting star:* small body, long upper wick at an uptrend high — rejection of higher prices.

**Q12 [I]. Why does a candlestick signal need location to matter?**
A: A hammer in the middle of a range is noise; a hammer *at a tested support with an oversold RSI* is a signal. The candle describes a single session's battle; only its location relative to structure/levels tells you whether that battle matters. Context converts a candle from decoration into information.

**Q13 [A]. What is a "trap" candle and how do pros use liquidity sweeps?**
A: A trap is a break of an obvious level that immediately reverses — e.g., price wicks below yesterday's low (triggering breakout-short and stop-loss sells), sweeps that liquidity, then closes back inside. Pros treat the reclaim of the swept level as a high-probability long trigger (stop below the wick), because the move ran the weak hands out and now has fuel.

### Block D — Gaps & special situations

**Q14 [F]. Classify the four gap types.**
A: *Common* (in-range, usually fills), *breakaway* (starts a new trend out of a base, often doesn't fill quickly), *runaway/measuring* (mid-trend, marks the midpoint), *exhaustion* (end of trend, fills fast as the move reverses).

**Q15 [I]. Nifty gaps up 200 points on a strong global cue and holds above the gap all session. Trade implication?**
A: A held gap-up (no fill) shows genuine demand — the "gap-and-go". The prior close / gap zone becomes intraday support; longs favour buying pullbacks toward it with a stop below the gap. An *unfilled* gap that holds is bullish; a gap that fills and closes back inside the prior range is a failed gap (often bearish).

### Block E — Option chain & Open Interest fundamentals

**Q16 [F]. What is Open Interest and how does it differ from volume?**
A: OI is the total number of outstanding (not-yet-closed) contracts at a strike; volume is contracts traded in the period. Volume can be high with flat OI (day-traders opening and closing). Rising OI means fresh positions are being added — new money and conviction; falling OI means positions are being closed.

**Q17 [I]. Complete the four price-OI build-up combinations.**
A:
| Price | OI | Interpretation |
|-------|-----|----------------|
| Up | Up | **Long build-up** (fresh longs, bullish) |
| Down | Up | **Short build-up** (fresh shorts, bearish) |
| Up | Down | **Short covering** (shorts exiting, up-move may be weak/temporary) |
| Down | Down | **Long unwinding** (longs exiting, down-move may lack fresh selling) |
*Trap:* a rally on short-covering (price up, OI down) is not the same as a rally on fresh longs — it can fade once covering finishes.

**Q18 [F]. What is PCR (Put-Call Ratio) and how is it read?**
A: PCR = total put OI / total call OI. High PCR (>1.3ish) = heavy put writing / bearish positioning that's often read *contrarian-bullish*; low PCR (<0.7ish) = heavy call writing, contrarian-bearish. It's a sentiment extreme gauge, not a precise trigger — most useful at the tails.

**Q19 [I]. What is max-pain and how do you use it, honestly?**
A: Max-pain is the strike at which the *largest* number of option buyers lose the most (i.e., where total option-holder payout is minimised) — theoretically where option writers "want" expiry to land. It acts as a soft magnet near expiry. Honestly: it's a rough gravitational reference, not a law; it works better in calm expiries and gets overwhelmed by strong trends or news.

**Q20 [I]. How do OI walls act as support and resistance?**
A: A strike with very heavy *call* OI acts as resistance (writers defend it, and hedging flow caps price there); heavy *put* OI acts as support. E.g., if Bank Nifty 55,000 call has the biggest call OI and 54,000 put the biggest put OI, the expected range is 54,000–55,000 and those become the technical rails to trade against.

**Q21 [A]. Why is "high PCR = bullish" dangerous as a standalone rule?**
A: Because PCR is regime-dependent and can stay elevated in a grinding uptrend (constant put-writing) or spike in a genuine crash (panic put-buying, not writing). The *direction of the OI change* and *who is transacting* (writers vs buyers) matters more than the ratio's level. Use PCR only at extremes and always with price structure.

### Block F — IV, Greeks & volatility for the technician

**Q22 [F]. What is Implied Volatility and why should a chart trader care?**
A: IV is the market's forward-looking volatility priced into options; India VIX is the Nifty version. A chartist cares because IV sets option prices (buy options when IV is low, prefer writing when IV is rich), sizes expected ranges, and IV spikes/crushes around events (results, RBI policy, Budget) distort premium independent of direction.

**Q23 [I]. Delta as a probability — explain.**
A: A call's delta ≈ the probability (risk-neutral) it expires in-the-money. A 0.30-delta OTM call is loosely a ~30% chance of finishing ITM. Technicians use delta to align strike selection with their setup's odds — a high-conviction breakout might justify a higher-delta (closer) strike; a lottery play uses low-delta.

**Q24 [A]. Post-results, a stock moves exactly as you predicted but your long call loses money. Why?**
A: **IV crush.** Ahead of results IV is inflated; once the event passes, IV collapses and the option's extrinsic value evaporates — the vega loss can exceed the delta gain from a modest move. The lesson: buying options into a known event is a volatility bet as much as a direction bet; if the move isn't large enough to beat the IV crush, you lose despite being "right".

**Q25 [I]. What is theta and how does it shape weekly-option technical trading?**
A: Theta is time decay — the premium lost per day, accelerating into expiry. On NSE weeklies, theta is brutal in the last two sessions, which is why intraday and expiry-day option-buying needs the move to happen *fast*; writers, conversely, harvest theta. A breakout setup that "should" work but stalls bleeds theta even if it eventually moves.

### Block G — Scenario questions (reason out loud)

**Q26 [S]. "Nifty spot is at 25,000. The 25,000 call has the highest call OI, the 24,800 put has the highest put OI, PCR is 0.9, and price is coiling in a tight range on the 15-min. It's Tuesday, expiry Thursday. Walk me through your read and plan."**
A: *Regime:* balanced PCR + heavy OI at 24,800 (support) and 25,000 (resistance) defines an expected 24,800–25,000 range with max-pain likely near 24,900–25,000. Coiling price + two days of theta favours *range/writing* logic over directional buying. *Plan:* fade the rails — long near 24,800 (put-wall support) with stop below it, short near 25,000 (call-wall resistance) with stop above; or, as a writer, an iron-condor/short-strangle around 24,800–25,000 collecting theta. *Invalidation:* a decisive 15-min close *outside* the rails on volume flips it to a directional breakout — heavy call OI at 25,000 breaking triggers short-covering that can accelerate through it; I'd stop the range trade and flip to breakout logic (buy the 25,000 break, target the next call wall). *Honesty:* near expiry the range holds *until it doesn't*; I size small and respect the break.

**Q27 [S]. "Bank Nifty formed a head-and-shoulders on the daily, neckline 53,000, and just closed below it. But India VIX is falling and the 53,000 put OI is huge. Do you short?"**
A: Conflicting evidence, so I weigh it. *For the short:* completed H&S with a neckline *close* (not just a wick) — a valid, high-quality reversal trigger; target = head-to-neckline height projected down. *Against:* huge 53,000 put OI means writers are defending 53,000 as support (option-flow support right at the neckline), and falling VIX suggests no panic — a poor environment for a clean breakdown. *Resolution:* I don't short the break blindly into a put wall. I wait — either for a *retest* of 53,000 from below that fails (put writers capitulating, confirming the break) before shorting with a tight stop above 53,000; or if price reclaims 53,000 and the put wall holds, the H&S becomes a *failed pattern* and I stand aside or look long. The put wall + falling VIX lowers my conviction enough that I demand the retest confirmation rather than chasing.

**Q28 [S]. "A midcap you follow is up 9% today on 5x average volume, breaking to a fresh high out of a six-month base. RSI is 82. Buy, wait, or avoid?"**
A: This is a *breakout on conviction volume out of a long base* — textbook bullish; the 82 RSI is a sign of strength in a fresh breakout, not a sell (Part 1, Q16). But I don't chase a +9% extended candle — entry risk is poor. *Plan:* buy a *controlled pullback* or a break of the day's high on the next session, not the top of today's bar; or take a partial now and add on the retest of the breakout level (the old base high, now support via polarity). Stop below the breakout level / base high. *Caveat:* midcap liquidity — I check delivery % (genuine accumulation vs operator churn) and size smaller for the wider ATR. Avoid only if the volume is a one-off news pop with no follow-through structure.

**Q29 [S]. "Nifty gaps down 1.5% on a weak global open, then spends the morning grinding back to fill the gap. What does gap-fill behaviour tell you and how do you trade it?"**
A: A down-gap that gets *filled* intraday shows the selling was emotional/overnight-driven, not sustained — buyers are absorbing. Filling the gap is bullish behaviour. *Trade:* I watch what happens *at* the gap-fill level (prior close): if price reclaims it and holds with VWAP support beneath, it's a long toward the day's earlier high, stop below VWAP/the reclaim. If it fills and *rejects* (fails to hold prior close), the gap-fill was just mean-reversion into resistance and the down-day resumes — short back toward the low. So gap-fill is the *setup*; the reaction at the fill level is the *trigger*.

**Q30 [S]. "You're long Fin Nifty from a bull-flag breakout. Halfway to target, a large bearish engulfing candle prints on the daily at a resistance level, but your OI read still shows long build-up. Manage the trade."**
A: Two signals disagree, so I manage rather than abandon. The bearish engulfing at resistance is a genuine *warning* of a pause/pullback; the continuing long build-up (price/OI) says positional money is still adding on the bull side. *Management:* I don't exit fully against fresh long build-up, but I *de-risk* — book partial profit into the engulfing candle, trail the stop up to just below the flag-breakout level or the last swing low so I lock in gains, and hold the remainder for the measured target as long as OI stays supportive. If the next session confirms the engulfing (closes below its low) *and* OI flips to long-unwinding, I'm out — the two signals now agree bearish. This is confluence-based management: act decisively only when independent signals align.

## Reading it — a worked fusion

Fuse a pattern with the chain on one setup. Bank Nifty, daily: a four-week **ascending triangle**, flat top at 55,000, rising lows from 53,200 → 54,100 → 54,600. The option chain shows the **55,000 call with the largest call OI** and rising, **54,500 put OI building**. Read phase-by-phase: the *pattern* says bullish bias with a breakout target of 55,000 + height (55,000−53,200 = 1,800) ≈ **56,800**. The *chain* says 55,000 is a defended call wall — so the breakout has to overcome heavy call writers. The tell to watch: if price presses 55,000 and that call OI starts *falling* (writers covering / rolling up), the wall is cracking and short-covering can rocket price toward 56,800. If call OI keeps *rising* into every test, the wall holds and the triangle is more likely to fail lower toward the rising trendline (~54,600). The pattern gives the target; the OI tells you whether the breakout is real.

## Trading it

- **Breakout long:** enter on a *daily close* above 55,000 *with* falling 55,000 call OI (wall breaking) and volume; stop below 54,600 (last higher-low); target 56,800 (measured move), partial at 55,800.
- **Failure short:** if price rejects 55,000 three times with *rising* call OI and then closes below 54,600 (breaks the ascending trendline), the pattern failed — short toward 53,200, stop above 55,000.
- **Expiry overlay:** near expiry, if 55,000 is also max-pain, expect the wall to hold *into* expiry and the real break to come after — don't chase a Thursday-afternoon poke through 55,000.

## Confluence

The through-line of Part 2: **price patterns tell you the shape and target; the option chain tells you whether the crowd's money agrees.** The highest-probability calls stack (1) a clean pattern with a *close*-confirmed trigger, (2) volume, (3) an OI read that supports the direction (long build-up for longs, cracking call-wall for upside breaks), (4) an IV/VIX check so you're not buying premium into an event crush, and (5) index/cross-market confirmation from Part 1. A head-and-shoulders into a supportive short build-up with falling VIX is a research call; the same pattern into a huge put wall (Q27) is a "wait for the retest".

## Pitfalls & false signals

- **Trading a pattern before it confirms** (Q3) — a double top isn't one until the neckline breaks.
- **Chasing extended breakout candles** (Q28) — great setup, terrible entry.
- **Neckline/level stop-hunts** (Q4, Q13) — prefer the *close* and often the *retest*.
- **Confusing short-covering with fresh longs** (Q17) — covering rallies fade.
- **PCR/max-pain as laws** (Q19, Q21) — soft references, not triggers; fail in strong trends.
- **Buying options into events ignoring IV crush** (Q24) — right on direction, wrong on vega.
- **Reading patterns on illiquid mid/small-caps** (Q10) — low liquidity distorts the shape and the OI.

## Interview-ready summary

Chart patterns are order-flow stories — accumulation, distribution, and trapped traders — that give you a *bias, a trigger (a close, not a wick), and a measured target*. In Indian markets you never read them in isolation from the option chain: OI build-up (long/short, covering/unwinding) tells you whose money is behind the move, call/put OI walls mark the real support and resistance, PCR and max-pain are soft sentiment references best used at extremes, and IV/VIX plus theta and delta govern whether an options expression will actually pay even when the chart is right. In a scenario, answer as a *process* — regime, then the pattern's trigger and target, then the OI/IV confirmation or contradiction, then the invalidation level and how you'd manage the disagreement — because a technical-and-derivatives analyst is paid for a probabilistic plan with defined risk, not a one-word prediction.
