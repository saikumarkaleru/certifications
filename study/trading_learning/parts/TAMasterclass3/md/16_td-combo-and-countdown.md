# DeMark TD Combo & Countdown

TD Sequential's Countdown is the more famous of DeMark's exhaustion engines, but it was never his only one. Tom DeMark built **TD Combo** as a stricter, faster-arming sibling — same 13-bar destination, different (and tougher) route. In practice, professional DeMark users run **both** Sequential Countdown and Combo Countdown side by side and treat the cases where the two agree as their highest-conviction exhaustion signals. This chapter goes deep on the Countdown mechanics that Chapter 15 only sketched, then builds TD Combo in full, contrasts the two, and trades their confluence on Indian instruments. If Chapter 15 was "here is the whole Sequential pipeline," this chapter is "here is the Countdown machinery in surgical detail, plus its tougher cousin."

## What they are and the logic

Both TD Combo and TD Sequential Countdown try to pinpoint the exact bar where a trend runs out of participants. The philosophical difference is about **how much internal consistency the exhaustion must show**:

- **Sequential Countdown** is *lenient*: it only requires that a Countdown bar's close relate to price two bars earlier. Bars can qualify out of order, and the Setup that precedes it needs only to have completed. It answers, "have we accumulated enough stretched closes since the trend got tired?"
- **TD Combo** is *strict*: it demands that the exhaustion be building **in real time, in the correct order**, with each Countdown bar also satisfying momentum, position, and progression conditions simultaneously. It answers, "is the trend *currently* rolling over in a clean, ordered way?"

Because Combo's conditions are harder to satisfy, a Combo 13 typically arrives **earlier and closer to the actual turn** than a Sequential 13, but it also fires less often. Sequential 13s are more frequent but can lag the low. Using both gives you a fast signal (Combo) and a confirming signal (Sequential), and their overlap is gold.

## The Countdown machinery in full (Sequential recap + depth)

Recall from Chapter 15 that Sequential Countdown begins **only after a Setup 9 completes** and counts:

- **Buy Countdown:** close ≤ low two bars earlier, to 13.
- **Sell Countdown:** close ≥ high two bars earlier, to 13.
- Bars need **not** be consecutive.

Three refinements matter enormously in live trading and deserve full treatment:

**1. The bar-8 qualifier.** Countdown bar 13 is only "true" if, for a buy, its **low ≤ the close of Countdown bar 8**. Until that is satisfied the platform prints "13" deferred as **12 + a pending bar** (often shown as a "+"). This stops a limp bar from claiming the exhaustion.

**2. Cancellation.** A live Countdown dies if:
- Price **closes through the TDST** line in the trend's direction with enough force (a "trend is too strong" flag), or
- A new Setup forms in the **opposite** direction (the market already turned without needing the 13), or
- **Recycling** occurs — see below.

**3. Recycling (the biggest practical trap).** If, while a Countdown is in progress, a **new Setup forms in the same direction** and that new Setup's price extreme is *larger in magnitude* than the prior one (DeMark's "Setup within a Setup" size test), the Countdown **resets to zero**. Intuition: the trend just produced a fresh burst of stretched closes, so any prior exhaustion tally is stale. Recycling is not a bug — it is the tool refusing to call a bottom in a market that keeps accelerating down. Many DeMark platforms let you choose the recycle rule (aggressive vs. lenient); know which you use.

### Aggressive Sequential Countdown variant

DeMark also defined an **aggressive Countdown** where the comparison is close ≤ *low* two bars earlier replaced by close ≤ *close*... more precisely the aggressive version requires each Countdown bar's low (buy) to be less than or equal to the low two bars earlier, forcing lower lows into the count. It arrives faster and is favored in fast markets like intraday Bank Nifty, at the cost of more false signals. Treat it as an option, not the default.

## TD Combo — exact construction and rules

TD Combo shares the Setup phase with Sequential (identical 9-bar Setup and TDST). The difference is entirely in the **Countdown**. Combo Countdown has **four simultaneous conditions** on each count bar, and — in the standard "Version 1" — Countdown begins on **Setup bar 1**, not after Setup 9, letting it run concurrently.

For a **buy Combo Countdown**, each of the 13 counting bars must satisfy **all** of:

| # | Condition | Meaning |
|---|---|---|
| 1 | Close ≤ low two bars earlier | Same stretched-close test as Sequential |
| 2 | Low < low of previous bar | Price is still making progress lower (position) |
| 3 | Close < close of previous bar | Momentum still down bar-over-bar |
| 4 | Close < close of the prior counted bar | Ordered progression: each count closes lower than the last count |

For a **sell Combo Countdown**, reverse every inequality (close ≥ high two bars earlier; high > previous high; close > previous close; close > prior counted close).

Because all four must hold on the **same** bar and in order, Combo counts are far harder to accumulate. A choppy pullback that would tick off Sequential counts will fail Combo's "close < prior counted close" progression the moment a bar closes higher than the last count.

**Combo Version 2** relaxes conditions on counts 11–13 (dropping the strict momentum test for the final bars) so the count can complete on the terminal thrust; Version 1 keeps all four conditions through 13. Most software defaults to Version 2 for the last three bars. As with Sequential, a **bar-8 style qualifier** and **TDST cancellation/recycling** also apply.

### Side-by-side contrast

| Feature | Sequential Countdown | TD Combo |
|---|---|---|
| Starts | After Setup 9 completes | On Setup bar 1 (V1), concurrent |
| Conditions per bar | 1 (close vs low/high 2 bars ago) | 4 simultaneous (V1) |
| Consecutive required | No | Effectively yes via progression tests |
| Typical timing | Later, can lag the low | Earlier, nearer the turn |
| Frequency | More signals | Fewer, stricter |
| Best use | Confirmation | Early warning / trigger |

## Worked India example — Bank Nifty daily

Take a Bank Nifty rally that has run from ~45,800 to ~49,600 over five weeks and is looking parabolic — the kind of move where retail keeps buying calls into strength. We want a **sell** signal (Setup and Countdown to top-tick).

**Setup.** A sell Setup completes when 9 consecutive bars close above the close four bars earlier. Suppose Setup 9 prints at 49,320, perfected (bar 9 high exceeds bars 6–7 highs). TDST **support** is set at the true low of the Setup, say 47,650.

**Sequential sell Countdown.** From Setup 9, we count bars whose close ≥ high two bars earlier. The rally is strong, so counts accumulate: the market keeps grinding up to 49,600, 49,540, 49,680... Sequential reaches 12 near 49,700. Then a final blow-off bar closes at 49,780, and its high (49,860) ≥ the close of Countdown bar 8. **Sequential sell 13 at 49,780.**

**Combo sell Countdown.** Running concurrently, Combo has been ticking only on bars that *also* made higher highs, closed above the prior bar, and closed above the prior counted bar. In a clean parabolic push these conditions are met on the strongest days, so Combo actually reaches **13 a few sessions earlier**, at 49,610 — flagging exhaustion *before* Sequential. 

Now both engines have printed sell 13s within ~170 points of each other, near the round 49,500–49,800 zone, into a parabolic rally. That agreement is the signal.

## How to trade the confluence — entry, stop, target

**Trigger.** Do not short the raw 13. Wait for a **bearish price flip** — the first bar to close *below* the close four bars earlier after the 13. Say that comes at 49,180.

**Entry.** Short Bank Nifty futures (or, better for defined risk, buy a bear put spread) at 49,180 on the flip.

**Stop.** DeMark's rule: a true-range increment **above** the true high of the 13 bar. 13-bar high 49,860 + that bar's true range (~350) → stop **50,210** on a closing basis. If Bank Nifty closes above 50,210 the exhaustion is void — the trend simply refused to die.

**Targets.**
1. **TDST support** at 47,650 — first objective, ~1,530 points / ~3.1% from entry.
2. **Measured move / TD projection** below TDST if it breaks.
3. **Prior consolidation** around 46,500 as a stretch target.

**Management.** Cover half at TDST (47,650), trail the rest under lower TD Setup highs, and exit fully if a fresh **buy** Setup completes (trend flipping back up) or if the count recycles against you.

**F&O expression.** Because Bank Nifty options are liquid and weekly, a sell 13 confluence at ~49,180 is naturally expressed as a **bear put spread** — e.g., buy 49,000 put / sell 48,000 put for the nearest weekly — capping risk to premium (say ₹250–320 per lot times lot size) while capturing the drop to TDST. Selling naked calls off a 13 is tempting but dangerous: exhaustion signals fail often enough in trending regimes that undefined upside risk is unwise, and Bank Nifty gaps are brutal.

## Backtest and edge notes with realistic costs

Honest framing: published and independent studies of raw DeMark 13 signals show a **modest** edge — hit rates typically in the 45–58% range depending on instrument, timeframe and whether confirmation is required, with the real value coming from **favorable reward:risk** (targets to TDST are often 2–4x the initial stop distance) rather than from a high win rate. Key backtest lessons for NSE:

- **Confirmation beats close-of-13.** Requiring the price flip before entry meaningfully improves expectancy versus buying/selling the 13 at its close.
- **Combo + Sequential agreement filters strongly.** Trades taken only when both 13s cluster within a small band are fewer but materially better.
- **Higher timeframe wins.** Daily and weekly signals on Nifty/Bank Nifty are far more reliable than 5-minute signals, which are dominated by noise and generate constant recycling.
- **Costs matter.** With Indian charges — STT (0.02% sell side on futures, 0.1% on delivery equity; 0.1% on option sell premium, 0.125% on exercised options), brokerage, exchange fees, GST, stamp duty — a counter-trend futures scalp on tiny 13 signals bleeds out. The edge only survives on swings large enough (multi-percent moves to TDST) to dwarf costs. This is a swing tool, not a scalping tool.
- **Regime dependence.** In strong secular trends (2020–21, 2023 Nifty), sell 13s got repeatedly recycled and stopped; in range-bound years they worked beautifully. Combine with a trend/regime filter (e.g., only take sell 13s when the weekly is not making fresh accelerating highs).

## Adaptations for NSE and F&O

- **Instrument choice.** Use TD Combo/Countdown on index futures (Nifty, Bank Nifty, Fin Nifty), liquid large caps (Reliance, HDFC Bank, Infosys), MCX (crude, gold) and USDINR. Avoid illiquid smallcaps where gappy prints corrupt the counts.
- **Expiry awareness.** A 13 that prints right into monthly expiry can be distorted by settlement flows; give more weight to signals away from expiry day.
- **Defined-risk options.** Always prefer spreads over naked futures for the actual reversal bet — the "this might just recycle" humility of a counter-trend signal maps perfectly onto capped-risk structures.
- **Combine with OI.** A sell 13 at a strike where call OI is peaking (heavy call writing above) is corroborated by positioning; a buy 13 where put OI peaks below marks a positioning floor.

## Pitfalls

1. **Treating Combo like Sequential.** They complete at different bars; if you count Combo with Sequential's single rule you will mis-signal. Know which engine your platform is displaying.
2. **Ignoring recycling.** A same-direction Setup resets Countdown. Traders who miss a recycle short a "13" that no longer exists.
3. **Version confusion (Combo V1 vs V2).** The last-three-bar rules differ; two platforms can show Combo 13 on different bars. Standardize your setting.
4. **Fading the strongest trends.** Parabolic moves recycle repeatedly. The confluence filter (needing both engines *and* a trend/regime check) exists precisely to keep you out of these.
5. **Low-timeframe overtrading.** On 1–5 min charts, both engines fire constantly, costs dominate, and the edge evaporates.
6. **No confirmation.** Entering the raw 13 close without the price flip is the single most common way traders lose money with DeMark tools.

## Interview-ready summary

TD Combo and TD Sequential Countdown are Tom DeMark's two exhaustion engines. Both share the 9-bar Setup and the TDST line, and both count to **13** to mark a possible trend reversal. **Sequential Countdown** is lenient — one condition per bar (close vs. the low/high two bars earlier), non-consecutive, starting after Setup 9, with a bar-8 qualifier and cancellation/recycling rules. **TD Combo** is strict — up to four simultaneous conditions per bar (stretched close, new low/high, lower/higher close than the prior bar, and lower/higher close than the prior *counted* bar), typically starting on Setup bar 1, so it completes earlier and nearer the actual turn but fires less often. Professionals run both and treat clustered Combo + Sequential 13s as high-conviction exhaustion. Trade the confluence counter-trend with a **price-flip confirmation** entry, a stop a true-range beyond the 13 bar's extreme, and the opposing **TDST** line as the first target — ideally expressed through defined-risk option spreads on Nifty/Bank Nifty. The realistic edge is modest on win rate but strong on reward:risk, survives only on swing timeframes where moves dwarf Indian transaction costs, and demands respect for recycling in strong trends.
