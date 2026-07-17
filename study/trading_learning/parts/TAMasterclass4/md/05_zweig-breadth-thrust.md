# Zweig Breadth Thrust & Thrust Signals

## What it is and the logic

Most breadth signals are gradual — a line drifts up, a divergence forms over weeks. The Zweig Breadth Thrust is the opposite: it is a *violent, rare, binary* event. Martin Zweig, the American money manager and author of *Winning on Wall Street*, defined a specific mechanical condition that, when it fires, has historically marked the launch of major bull moves. The logic behind it is the physics of market bottoms.

Markets do not bottom on good news. They bottom when selling exhausts itself — when nearly every stock has been dumped, the sellers are spent, and there is no one left to sell. At that point the market is a coiled spring. When buyers finally step back in, they do not trickle; they *stampede*, because the same universal fear that drove the washout now flips to universal fear-of-missing-out. The result is a sudden, breathtaking surge in participation: the percentage of stocks advancing rockets from near-zero to overwhelming in a matter of days.

Zweig's insight was to *quantify the stampede*. He measured the ratio of advancing issues to total issues (advances plus declines), smoothed it with a 10-day exponential moving average, and defined the thrust as: the smoothed ratio rising from **below 40% to above 61.5%** within **10 trading days or fewer**. That is the entire signal. It captures the transition from broad panic (fewer than 40% of stocks advancing on average) to broad greed (more than 61.5% advancing on average) happening *fast*. Speed is the essence. A slow drift from 40% to 61.5% over three months means nothing; the same move in nine days means the market just changed character violently, and violent changes of character off washouts are how great bull runs begin.

The deeper principle generalizes beyond Zweig's exact numbers into a whole family of **thrust signals**: any measure that captures a sudden, overwhelming, broad-based shift in participation from one extreme to the other. The 90% up-day, the back-to-back 80%+ up-volume days, the surge in percent-above-50DMA off a washout — all are thrust signals built on the same idea. *Explosive breadth off an extreme initiates trends; grinding breadth continues them.*

## Construction and reading

**The Zweig Breadth Thrust indicator, step by step.**

1. Each day, compute the **Breadth Ratio** = Advancing issues / (Advancing issues + Declining issues). This is a number between 0 and 1 (or 0% to 100%). Unchanged issues are excluded from the denominator in the classic construction.
2. Apply a **10-day exponential moving average** to this daily ratio. The EMA is the "Breadth Thrust Indicator." Smoothing matters — it filters single-day spikes and captures sustained shifts.
3. **The signal fires** when the 10-day EMA travels from below **0.40** (40%) to above **0.615** (61.5%) in **10 trading sessions or fewer**.

```
Breadth Ratio(day)   = Advances / (Advances + Declines)
Thrust Indicator     = EMA_10( Breadth Ratio )
SIGNAL = TRUE  if  Thrust Indicator crosses 0.40 → 0.615  within ≤10 days
```

The two thresholds are deliberately asymmetric around 0.50. Below 40% means the average day over the last ten was decisively negative — a genuinely oversold, washed-out tape. Above 61.5% means the average day is decisively positive and broad. The window forces speed.

**Reading it.** The indicator is not something you monitor for daily nuance. It sits dormant for months, oscillating in the 0.45-0.55 band during normal markets, and it means nothing there. You care about exactly two things: (1) has it dropped below 0.40, arming the setup? and (2) if armed, does it then rocket above 0.615 within ten days, firing the signal? Only the completed 40→61.5 journey counts. A dip to 0.40 that recovers slowly is a dud. A dip to 0.38 that explodes to 0.63 in seven days is the real thing.

**The historical record.** In US markets, genuine Zweig thrusts are extraordinarily rare — a small handful per *decade* — and their forward record is exceptional: strong, sustained gains over the following six to twelve months with a very high hit rate. Rarity is a feature, not a bug. The signal's power comes precisely from the fact that it almost never fires, so when it does, it is telling you something structural about the market's turn.

## The wider thrust family

Because the strict Zweig thrust is so rare, practitioners watch a broader set of thrust and momentum-breadth signals that share the DNA:

| Signal | Definition | Meaning |
|---|---|---|
| Zweig Breadth Thrust | 10-EMA of A/(A+D) from <40% to >61.5% in ≤10 days | Rare, powerful bull launch |
| 90% Up Day | Up-volume ≥90% of (up+down) volume AND advancing points ≥90% | Strong one-day demand surge |
| Back-to-back 80% days | Two 80%+ up-volume days within a short window | Confirmed accumulation, trend start |
| Breakaway Momentum | Ratio of 10-day summed advances to 10-day summed declines exceeds a high threshold | Powerful upside initiation |
| %Above 50DMA thrust | Percent-above-50DMA ripping from <15% through 55%+ quickly | Washout-to-recovery confirmation |
| Advance-Decline thrust | AD line vaulting to new highs after a washout | Broad participation returning |

The common thread: an *extreme starting point* plus an *explosive, broad move* off it. Marty Zweig's number is the most famous, but a trader who understands the *category* can recognize a thrust even when the exact 40/61.5 boxes are not perfectly ticked — which matters enormously in India, where clean daily A/D EMA data is not as standardized as on the NYSE.

## Worked India example

India does not publish a canonical "Zweig thrust" ticker, so Indian traders reconstruct the logic from NSE advance-decline data, which every broker and NSE's own site provide daily (advances, declines, unchanged across the NSE universe of roughly 1,900-2,000 traded stocks). Consider a realistic reconstruction around a sharp Indian market bottom.

**Setup — the washout.** The Nifty has fallen from 24,800 toward 21,800 over several weeks. India VIX has spiked above 21. For the last ten sessions the daily advance ratio A/(A+D) has averaged in the low 30s% — most days, 1,400 of the 1,900 traded stocks are declining. The 10-day EMA of the breadth ratio has sunk to 0.36. **The setup is armed**: the indicator is below 0.40, the tape is washed out, percent-above-50DMA (from the companion chapter) is reading single digits.

**The thrust.** A stabilization catalyst arrives — a softer inflation print, a global risk-on turn, an RBI signal, whatever the narrative. Day 1: advances 1,300, declines 550 → ratio 0.70. Day 2: another broad up day, ratio 0.68. Day 3 pauses, ratio 0.52. Days 4-6 resume, ratios 0.66, 0.64, 0.71. The Nifty rips from 21,800 to 22,900. By day 6 the 10-day EMA of the breadth ratio has climbed from 0.36 through 0.48, 0.55, and now prints **0.62 — above the 0.615 threshold, inside the 10-day window.** The Zweig thrust has fired.

**What it means and how to act.** The thrust says: this is not a dead-cat bounce; participation is broad and explosive, the washout is over, and history favors a durable advance over the coming months. The playbook:

- *Bias flips hard to long.* Treat the bear-market "sell rallies" instinct as cancelled.
- *Do not wait for a deep pullback* that may never come — thrusts often lead to persistent, un-retraced rallies. Enter on the first modest pause or a break of a short-term swing high, scaling in.
- *Set a structural invalidation*: if the Nifty closes back below the washout low (21,800), the thrust has failed — rare, but define the exit up front.
- *Ride it with a trend tool*, not a mean-reversion tool. Once the thrust confirms the launch, switch to trailing stops (a moving average, a swing-low trail) and let the position breathe for weeks, not days.

**The trader who respected it** was short or cash into the washout, saw the setup arm below 0.40, and on the sixth-day cross above 0.615 flipped to long size — capturing the first leg of a multi-month recovery from a single, rare, mechanical signal, without needing to call the exact low.

**A near-miss variant.** Suppose instead the EMA had only reached 0.57 before rolling back down — not a completed thrust. Here the disciplined reader does *not* declare a bull launch. They may still lean long on the partial momentum-breadth improvement (a member of the wider thrust family), but with smaller size and a tighter leash, acknowledging the strict signal did not fire.

## How to use it for bias and timing

**The thrust is a bias-setting event, not a day-trading tool.** When a genuine thrust fires, it should dominate your directional stance for weeks to months. Its job is to catch you at the exact moment a bear phase ends and force you to abandon bearishness before the evidence feels comfortable — because by the time it feels comfortable, the first 8-10% of the move is gone.

**Sequencing the breadth toolkit around a bottom:**

1. **Washout** — percent-above-50DMA under 15%, VIX spiking, breadth EMA under 0.40. *The setup arms.*
2. **Thrust** — breadth EMA vaults above 0.615 within ten days. *The signal fires; flip to long bias.*
3. **Confirmation** — the AD line starts making higher highs, percent-above-50DMA pushes past 55%. *Participation broadens and holds.*
4. **Trend management** — switch from mean-reversion entries to trend-following trails. *Ride the leg.*

**Timing entries after a thrust.** Because thrusts often do not give deep pullbacks, use *shallow* pullback entries: a 1-2 day pause, a flag, a break of the prior three-day high. Waiting for a 5% retracement frequently means missing the trade. Scale in rather than demanding one perfect entry.

**When no thrust is present**, do not manufacture one. The absence of a thrust off a decline simply means the bottom is unconfirmed by this particular tool; rely on your other breadth and price signals and keep size modest.

## Pitfalls

**1. It is rare — do not force it.** The single biggest error is declaring a "thrust" every time breadth improves a bit. Genuine Zweig thrusts happen a handful of times per decade. If you are seeing one every few months, you have loosened the definition into meaninglessness. Respect the strict 40→61.5-in-ten-days boxes for the real signal, and label anything looser as a *lesser* thrust-family event with correspondingly lower conviction.

**2. Indian data construction varies.** Because NSE has no official Zweig ticker, your result depends on whether you use the full NSE universe, F&O stocks only, or a Nifty 500 subset; whether you include unchanged issues; and your EMA convention. Two traders can disagree on whether a thrust fired. Fix one construction and stay with it. Prefer the broad NSE all-stocks A/D count for fidelity to Zweig's intent.

**3. Whipsaw in choppy, low-vol markets.** The 40/61.5 thresholds were designed to be crossed rarely. In an unusually choppy tape the EMA can flirt with the boundaries and produce a marginal, low-quality signal. Weight thrusts far more heavily when they emerge from a *genuine washout* (VIX elevated, percent-above-50DMA in single digits) than from a shallow, orderly dip.

**4. Thrusts confirm bottoms, not tops.** The signal is inherently bullish and asymmetric — there is no clean, equally reliable *downside* Zweig thrust. Do not invert the logic and expect a "bearish thrust" to call tops; tops form via slow narrowing and divergence (the percent-above-MA chapter), not violent breadth collapse. Breadth collapses *accompany* declines already underway; they do not lead them the way upside thrusts lead advances.

**5. It says nothing about magnitude or exact path.** A thrust tells you a durable up-move is likely; it does not tell you it will be smooth. Expect volatility and pullbacks *within* the ensuing bull leg. Manage with trailing stops and position sizing, not with a demand that the market rise in a straight line.

**6. Ignoring the structural invalidation.** Rare as failures are, they happen. Always define the level (a close back below the washout low) at which you concede the thrust failed, so a rare dud costs you a small stop rather than a large conviction-driven loss.

**7. Acting before the cross completes.** The setup arming below 0.40 is *not* the signal. Traders who jump in the moment breadth turns up, before the EMA actually clears 0.615 within the window, are front-running an event that may never complete. Wait for the confirmed cross.

## Interview-ready summary

The Zweig Breadth Thrust is a rare, powerful bull-market launch signal defined mechanically: the 10-day EMA of advancing issues divided by advancing-plus-declining issues rises from below 40% to above 61.5% within ten trading days or fewer. Its logic is the physics of bottoms — markets bottom when selling exhausts and buyers then stampede, producing an explosive, broad surge in participation that this indicator quantifies. Speed is the essence: a slow drift means nothing, a violent nine-day surge off a washout means the market's character just changed, and such changes historically precede strong, sustained advances with a high hit rate. It fires only a handful of times per decade, and that rarity is the source of its reliability. It belongs to a wider *thrust family* — 90% up-days, back-to-back 80% up-volume days, breakaway momentum, percent-above-50DMA thrusts — all sharing the DNA of an extreme starting point plus an explosive broad move. Use it as a *bias-setting* event, not a day-trade: when a genuine thrust fires off a washout, flip decisively to a long stance for weeks-to-months, enter on shallow pullbacks (deep retracements often never come), switch from mean-reversion to trend-following trails, and set a structural invalidation at the washout low. In India, reconstruct it from NSE advance-decline data over the full traded universe with a fixed convention, and weight it most when it emerges from a true washout (elevated VIX, percent-above-50DMA in single digits). The cardinal errors: forcing the signal when breadth merely improves, inverting it to call tops (it confirms bottoms only), and acting before the 40→61.5 cross actually completes. The one-liner: *great bull runs begin with a stampede, and the Zweig thrust is the seismograph that measures it.*
