# Option-Chain / OI Reading Drills

The option chain is the single richest real-time dataset the retail Indian trader has free access to — and the most widely misread. Every Nifty, Bank Nifty, Fin Nifty, and stock-F&O chain is a live map of where option writers (mostly well-capitalised institutions and prop desks) have placed their bets, where they *don't* want price to go, and where they're being forced to run for cover. Learn to read it and you gain a probabilistic sense of support, resistance, and the day's likely range that price-only chartists never see.

But the chain is also a minefield of half-truths. "High Call OI = resistance" is true — until it isn't, when that OI is being aggressively bought and price rips through it. Open interest is a *two-sided* number: for every writer there's a buyer, and the number alone never tells you *who's winning*. You must read OI *together with* price and with the *change* in OI, not in isolation. This chapter drills exactly that skill through realistic Indian option-chain snapshots, each with a decision and a detailed key.

## Quick refresher on the four OI states

Before the drills, internalise the master table — every OI read reduces to combining the direction of *price* with the direction of *open interest*:

| Price | Open Interest | Interpretation | Who's in control |
|-------|--------------|----------------|------------------|
| Up | Up | **Long build-up** | Fresh buying, bullish, strong |
| Up | Down | **Short covering** | Shorts running, bullish but often late-stage |
| Down | Up | **Short build-up** | Fresh selling, bearish, strong |
| Down | Down | **Long unwinding** | Longs exiting, bearish but often late-stage |

Two more essentials. **PCR (Put-Call Ratio)** = total Put OI ÷ total Call OI; high PCR (>1.3–1.5) means heavy put writing (supportive/bullish, or complacent at extremes), low PCR (<0.7) means heavy call writing (resistive/bearish, or fearful at extremes) — it's a *contrarian-tinged* sentiment gauge, not a mechanical signal. **Max Pain** is the strike at which the most option buyers lose money / writers profit, toward which price is often (weakly) drawn near expiry. Keep this table in front of you for the drills.

---

## Drill 1 — The wall above

**Scenario.** Nifty spot is 24,180 on a Tuesday. The chain shows the 24,200 Call with the **highest Call OI** of any strike (say 1.2 crore), and 24,300 Call second. On the put side, 24,000 Put has the highest Put OI. Change-in-OI today shows *additions* to the 24,200 and 24,300 Calls. Price is drifting up toward 24,200. What's the read?

**Answer.** The **24,200 strike is the immediate resistance / call wall**: writers have parked the most Call OI there and are *adding* to it today (fresh call writing = short build-up on the call side), signalling they expect 24,200 to cap the move — they're betting Nifty stays below it into expiry. The **24,000 Put wall is the day's support** — put writers are defending that floor. So the operative expected range is roughly **24,000–24,200**, with 24,300 as the next resistance if 24,200 breaks. *Decision:* if you're long, 24,200 is a logical place to book/trim; fresh longs into a fresh-call-write wall carry poor odds unless the wall starts *unwinding*. **The nuance that separates pros from novices:** watch the *change* in 24,200 Call OI as price approaches. If it keeps *rising*, the wall holds — writers are confident. If it starts *falling* while price pushes up (call short-covering), the wall is *cracking* and a breakout is brewing.

---

## Drill 2 — The wall that breaks (short covering)

**Scenario.** Same setup — 24,200 Call was the big resistance wall all morning. Now, in the afternoon, Nifty pushes to 24,210, and you notice the 24,200 Call OI is *dropping fast* (down 30% from its peak) even as its premium *rises*. The 24,300 and 24,400 Calls are seeing OI reductions too. What's happening and what do you do?

**Answer.** This is a **short-covering breakout** — the most explosive bullish move the chain produces. The call writers who sold 24,200 are now *underwater* (spot moved through their strike), and they're **buying back their calls to cut losses**, which is why Call OI is *falling* while premium *rises*. Their buy-to-cover orders add fuel to the up-move — the very wall that was resistance flips into a launchpad, and the covering can cascade up strike by strike (24,300, 24,400 unwinding too). *Decision:* this is a **long trigger**, not a place to short. Go with the move — buy the breakout above 24,200 (or the retest of it as new support), stop back below 24,180, targeting the next call wall where fresh writing appears. **Key lesson:** "high Call OI = resistance" is only half the rule. Resistance is real *while OI builds*; the moment that OI *unwinds against the writers*, resistance becomes acceleration. Always read the **change**, not the static level.

---

## Drill 3 — PCR at an extreme

**Scenario.** It's a strong up-trending Thursday morning. The overall Nifty PCR has climbed to **1.9** — very high — as put writers pile in aggressively at every strike below spot, confident of more upside. A friend says "PCR is 1.9, super bullish, load up on longs." What's the correct, honest read?

**Answer.** **Caution — an extreme PCR cuts both ways.** A high PCR (heavy put writing) does reflect bullish positioning and provides real *support* (all those put writers defending lower strikes). *But* a PCR of 1.9 is an **extreme of complacency**: when *everyone* has written puts and is positioned bullish, the market is crowded, and a sharp down-move can trigger a cascade of **put writers covering** (buying back puts = selling pressure) that accelerates a fall. Extreme PCR readings are therefore best read *contrarily as a caution flag*, not a "load up" signal. *Decision:* stay with the trend if price action is strong, but **don't add fresh risk naively on the PCR number alone**; tighten stops and be alert for a reversal. **The honest point:** PCR is a *sentiment gauge*, not a trade trigger. Mid-range PCR (0.9–1.3) is informative about bias; *extreme* PCR is informative about *crowding and reversal risk*. Never trade a single number in isolation.

---

## Drill 4 — Bank Nifty range from the chain

**Scenario.** Bank Nifty spot is 52,050 on expiry Wednesday. Chain: highest Call OI at **52,500**, highest Put OI at **51,500**, second-highest Put OI at 51,000, second-highest Call OI at 53,000. Max Pain is computed at **52,000**. Both 52,500 Call and 51,500 Put OI are large and *stable* (little change today). How do you trade the day?

**Answer.** The chain defines a clear **expiry range of 51,500–52,500**, with the strongest gravity toward **Max Pain at 52,000** (very close to spot) — a classic *pin* setup on a low-conviction expiry day. Stable OI at both walls means neither side is breaking; writers on both flanks are comfortable. *Decision (range-appropriate):* on expiry with defined walls and spot near max pain, the higher-expectancy plays are **premium-selling / range structures** — e.g., a defined-risk iron condor with short strikes around 51,500 and 52,500, harvesting theta as spot pins toward 52,000. *Intraday scalpers* can fade the edges: short near 52,500 (into the call wall), long near 51,500 (off the put wall), tight stops just beyond each wall. **What NOT to do:** buy far-OTM options hoping for a breakout — on a pin day with stable walls, they bleed to zero. **Caveat:** if either wall's OI starts *unwinding* (covering) as spot approaches it, abandon the range thesis immediately — a wall in retreat means a breakout, and Bank Nifty breakouts are fast.

---

## Drill 5 — Long build-up vs short covering (why the difference matters)

**Scenario.** Two stocks both rallied 3% today. In **Stock A**, futures OI *rose* 12% alongside the price rise. In **Stock B**, futures OI *fell* 15% as it rose. Both charts look identically bullish. Which up-move is more trustworthy for a fresh swing long, and why?

**Answer.** **Stock A (long build-up) is the higher-quality, more sustainable move.** Price up + OI up means *fresh money is entering long positions* — new buyers are committing capital with conviction, and there's an established base of longs to support continuation. **Stock B (short covering)** is price up + OI *down*: the rally is driven by *shorts buying back to exit*, not fresh conviction buying. Short-covering rallies are often **sharp but late-stage and hollow** — once the trapped shorts have finished covering, the fuel runs out and the move can stall or reverse, because no fresh longs stepped up. *Decision:* prefer a fresh swing long in **Stock A**, where OI confirms real accumulation. Treat Stock B's move with suspicion — it may be the *end* of a down-move rather than the start of an up-trend; if you play it, keep it short-term and trail tightly. **This is the single most valuable OI skill:** two identical-looking rallies can have opposite futures ahead, and *only the OI change* tells you which is which.

---

## Drill 6 — OI shift intraday (support rising)

**Scenario.** Morning Nifty chain: highest Put OI at 24,000. By 1 PM, spot has risen from 24,050 to 24,180, and you notice the put writers have **shifted up** — the biggest Put OI is now at **24,100**, with heavy fresh additions at 24,100 and 24,150. Call wall remains at 24,300. What does this shift tell you?

**Answer.** **The support floor is rising with price — a bullish structural signal.** Put writers are the smart, well-capitalised side; when they *move their biggest positions up* (from 24,000 to 24,100) and *add* fresh puts at higher strikes, they're expressing growing confidence that Nifty won't fall back — they're comfortable defending a *higher* floor. A rising put-OI base beneath a rising price is exactly what you want to see in a healthy up-move; it confirms the trend has real support underneath it. *Decision:* the bias is bullish and continuation toward the 24,300 call wall is favoured; dips toward the new 24,100–24,150 put support are buy-the-dip candidates with a stop below 24,080. **Contrast this with the warning sign:** if instead put writers had been *unwinding* (removing OI from lower strikes as price rose without adding higher), it would signal *eroding* support — a hollow rally. Watching *where the walls migrate* through the day is a live read on shifting institutional conviction.

---

## Drill 7 — The trap of static OI at expiry

**Scenario.** It's 2:45 PM on Nifty expiry Thursday. Spot is 24,240. The 24,200 Call still shows large OI (1 crore) on the screen. A beginner reasons: "Huge Call OI at 24,200, so 24,200 is strong resistance — I'll short Nifty here betting it falls back below 24,200." What's wrong with this reasoning?

**Answer.** The reasoning ignores that **spot is already *above* 24,200 — those calls are now In-The-Money, and much of that "resistance" OI is stale/trapped, not defending anything.** Late on expiry day, high OI at a strike *below* spot doesn't mean resistance — those call *writers* are already losing and are likely covering (which pushes price *up*, not down), while the ITM calls' large OI partly reflects positions being held to settlement, not fresh selling pressure at 24,200. Shorting into a strike the market has *already reclaimed*, on expiry afternoon, fights both the trend and the max-pain drift. *Correct read:* resistance is now the *nearest call wall still above spot with live, building OI* (e.g., 24,300), and the fact that 24,200 was overcome is *bullish*. **Two lessons:** (1) A call wall only acts as resistance while price is *below* it and OI is *building* — once breached, it inverts. (2) Near expiry, OI interpretation warps: focus on strikes *around and above* spot with *changing* OI, and respect max-pain gravity. Static screen-OI at a breached strike is a trap.

---

## Drill 8 — Divergence: price up, both walls building

**Scenario.** Nifty is grinding up slowly, +0.3%. But the chain shows *both* heavy fresh **Call writing at 24,300** *and* heavy fresh **Put writing at 24,000** — writers on both sides adding aggressively, tightening the range. Change in spot is small; both OI columns are ballooning. What's the market telling you?

**Answer.** **Writers on both flanks are betting on a *rangebound, low-volatility* session** — they're selling both the 24,300 calls and the 24,000 puts because they expect Nifty to stay boxed between them and let *theta* decay both legs. This "range-tightening" via two-sided writing is the option market pricing *consolidation*, and it usually resolves as a *quiet, mean-reverting day* — until the range breaks. *Decision:* trade it as a **range** — fade the edges (short near 24,300, long near 24,000) with tight stops, or sell premium via a defined-risk condor; do *not* buy naked options expecting a big trend move, as two-sided writing signals suppressed volatility that bleeds option buyers. **The breakout tell:** the day this range resolves is the day *one* wall starts *unwinding* (writers on the losing side covering). Until then, respect the box the writers have drawn. Reading *both* columns together — not just the call side — is what reveals a *range* thesis rather than a directional one.

---

## Drill 9 — Stock F&O: short build-up before a fall

**Scenario.** A stock, say a metals name, is trading flat around 640 into the afternoon. You notice its **futures OI rising sharply (+18%)** while price *slips slightly* to 636, and on its option chain, fresh **Call writing** is piling into the 640 and 650 strikes while **put writers are unwinding** (removing OI from 620/630). What's the setup and the trade?

**Answer.** Every signal points **bearish — a coordinated short build-up.** (1) Futures: price *down* + OI *up* = **fresh short positions** being initiated with conviction. (2) Call side: aggressive fresh call writing at 640/650 = sellers confident price stays capped there. (3) Put side: put writers *unwinding* = they no longer want to defend the downside floor, i.e., support is being *withdrawn*. All three agree: smart money is positioning for a *decline*, and the removal of put support means a fall could accelerate with little beneath it. *Decision:* this is a **short setup** — sell futures / buy puts (or a bearish put spread) on a break below the day's support (say 632), stop above the 640 call wall / recent high, targeting the next lower support where fresh put writing reappears. **Why this drill matters:** the strongest, highest-conviction signals come when **futures OI, call-side, and put-side all tell the same story.** When the three columns *agree*, the read is robust; when they conflict, stay cautious. Here they agree, and the agreement is bearish.

---

## Drill 10 — Max Pain vs momentum (which wins?)

**Scenario.** Nifty expiry Thursday, 11 AM. Max Pain is at 24,000; spot is 24,150 and *trending up strongly* on a positive global session, breaking through call walls with visible short covering. A trader says "Max Pain is 24,000, so Nifty will get dragged down to 24,000 by close — I'll short." Is this right?

**Answer.** **No — momentum trumps max pain, especially early in the day.** Max Pain is a *weak, end-of-day gravitational tendency*, not a law, and it is routinely *overwhelmed* by genuine directional momentum — particularly a strong trend driven by short-covering and global cues. At 11 AM there are 4.5 hours for the trend to run, and fighting a momentum breakout to bet on a max-pain "magnet" 150 points *below* a rising market is a low-probability short against the day's clear force. *Decision:* **do not short into strength on a max-pain argument.** If anything, max pain itself may *migrate upward* through the day as OI shifts (max pain is recalculated live and follows the writing). Respect the trend; if you must use max pain, use it only late in the day, only when price is already *near* it and *directionless*, as a mild pin bias — never as a reason to fight a clear trend. **Honest framing:** max pain is one of the most over-hyped, over-traded concepts among retail; it's a *tiebreaker in a coin-flip*, not a directional signal.

---

## Drill 11 — Rising PCR into a fall (support failing)

**Scenario.** Nifty is falling, down 0.8% to 23,850. Through the decline you watch the PCR *drop* from 1.2 to 0.75, and note that Put OI at 24,000 and 23,900 is being **aggressively unwound** (falling fast) while fresh Call writing appears at 23,900 and 23,800. What's the read?

**Answer.** **Bearish confirmation — support is collapsing.** A falling PCR during a decline means **put writers are capitulating**: they're *buying back* their puts (unwinding OI) because spot is falling through the strikes they sold, and their buy-to-cover on puts + the removal of that put support *accelerates the fall*. Simultaneously, fresh call writing *below* the old spot (at 23,900/23,800) shows sellers now expect *lower* levels and are capping any bounce there — the whole option structure is *repricing downward*. *Decision:* the path of least resistance is **down**; this is a short-continuation environment, not a place to bottom-fish. Sell rallies into the new lower call walls, or hold existing shorts with a trailing stop, targeting the next put-writing support that *stabilises* (stops unwinding). **The mirror of Drill 6:** just as *rising* put walls confirm a healthy up-trend, *unwinding* put walls in a fall confirm the down-move has real force and the floor is giving way. PCR *dropping* through a decline is a classic support-failure signature.

---

## Drill 12 — Putting it together: a full chain snapshot

**Scenario.** Build a complete bias from this Nifty snapshot (Tuesday, spot 24,180, 12:30 PM):
- Highest Call OI: 24,300 (stable), then 24,400 (stable)
- Highest Put OI: 24,000 (rising fast today), then 24,100 (rising)
- PCR: 1.35 (mid-high, healthy)
- Futures OI: rising with price (long build-up)
- Max Pain: 24,100
- Change today: put writers *adding* at 24,000/24,100; call writers *stable*, not adding

State your bias, expected range, and plan.

**Answer.** **Bias: bullish-to-neutral, with an upward tilt.** Reasoning: (1) **Futures long build-up** — fresh money buying, the strongest single signal, confirms real demand. (2) **Put writers adding aggressively at 24,000/24,100** — support is firm and *rising* toward spot, institutions confident of the downside. (3) **Call walls stable, not building** — resistance at 24,300 exists but writers aren't *reinforcing* it, meaning it's less defended and more *breakable* than a wall under fresh writing. (4) **PCR 1.35** — healthy bullish positioning, not yet at a complacent extreme. (5) Max pain 24,100 sits just below spot — mild pin, but overridden by the long build-up. **Expected range:** **24,000 (firm support) to 24,300 (resistance, but soft).** **Plan:** favour the **long side** — buy dips toward the rising 24,100 put support with a stop below 24,000, first target 24,300; and be alert that if 24,300 Call OI starts *unwinding* on a push (short covering), it opens a run to 24,400. Avoid fresh shorts — every column except the soft call wall is bullish. **This is the goal of chain reading:** synthesise futures OI + both option walls + their *changes* + PCR + max pain into one coherent, probabilistic bias — not a single number, but a weighted picture of where the big money is positioned and leaning.

---

## Interview-ready summary

1. **OI is meaningless without price and without *change*.** Memorise the four states (long build-up / short covering / short build-up / long unwinding). Two identical rallies can be fresh buying or hollow short-covering — only OI change reveals which.
2. **Walls are support/resistance *while OI builds*; they invert when OI unwinds.** A call wall under fresh writing caps price; the same wall *covering* (OI falling, premium rising) becomes a breakout accelerant. Always watch the change as price approaches.
3. **Read both columns and their migration.** Rising put walls beneath a rising price confirm a healthy trend; unwinding put walls in a fall confirm collapse. Two-sided fresh writing signals a range.
4. **PCR and Max Pain are weak, contrarian-tinged context — never standalone triggers.** Extreme PCR flags crowding/reversal risk; max pain is a mild late-day pin that momentum routinely overrides.
5. **The strongest reads come when futures OI, the call side, and the put side all agree.** When the three columns tell one story, conviction is high; when they conflict, size down.
6. **Near expiry, interpretation warps** — breached strikes stop acting as resistance, theta dominates, and defined-risk premium selling suits pinned ranges. Respect the microstructure.

Practice by pulling a live NSE option chain (or Sensibull / Opstra) each morning, writing your bias *before* the session, and grading it at 3:30. Within a month, the chain stops being a wall of numbers and starts reading like a sentence.
