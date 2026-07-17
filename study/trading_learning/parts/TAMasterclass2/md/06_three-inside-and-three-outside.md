# Three Inside Up/Down & Three Outside Up/Down

The single most common complaint about the two-candle reversal patterns — the harami and the engulfing — is that they fire too early. A harami tells you momentum has stalled; an engulfing tells you one side has taken control for a day. But neither *confirms* that the reversal will actually follow through. The Japanese answer to this problem was elegant: **add a confirmation candle.** Take a harami, add a third candle that confirms, and you get the **Three Inside** pattern. Take an engulfing, add a third candle that confirms, and you get the **Three Outside** pattern. These are not exotic — they are the two most-used two-candle patterns wearing a seatbelt. This chapter covers all four variants (Three Inside Up, Three Inside Down, Three Outside Up, Three Outside Down), why the confirmation candle materially improves the odds, and exactly how to trade them in Indian equities and indices.

## What they are & why they work

### Three Inside Up/Down — the confirmed harami

The **harami** is a two-candle pattern where a large candle is followed by a small candle whose body is *contained within* the first candle's body (like a pregnant woman — *harami* is old Japanese for "pregnant"). It signals that a strong trend candle was followed by a day of indecision/contraction — momentum has paused. But a pause is not a reversal.

The **Three Inside Up** takes a *bullish harami* (in a downtrend: big red candle, then a small green candle inside it) and adds a **third green candle that closes above the second candle** (ideally above the first candle's open). That third candle *confirms* that the pause has become an actual turn. The sequence: capitulation down-day → contraction/indecision → decisive up-day. The story is complete.

The **Three Inside Down** is the mirror in an uptrend: big green candle, then a small red candle inside it (bearish harami), then a **third red candle closing below the second** — confirmed reversal down.

Why the confirmation candle matters: a bare harami has a mediocre historical hit rate because indecision resolves *either* way. By demanding a third candle that breaks in the reversal direction, you filter out all the haramis that simply resolve back into the trend. You trade fewer signals, but the ones you take have already shown follow-through. You are paying a little (a later, slightly worse entry) for a lot (a materially higher probability).

### Three Outside Up/Down — the confirmed engulfing

The **engulfing** is a two-candle pattern where the second candle's body completely *engulfs* the first's. A bullish engulfing (downtrend: small red candle, then a big green candle that swallows it) shows buyers overwhelmed sellers in a single session. It is stronger than a harami, but it can still be a one-day wonder.

The **Three Outside Up** takes a *bullish engulfing* and adds a **third green candle that closes higher still.** The sequence: sellers in control → buyers violently engulf and take over → buyers press the advantage. The third candle confirms the engulfing wasn't a fake-out.

The **Three Outside Down** is the mirror: in an uptrend, a bearish engulfing (small green, then big red swallowing it), then a **third red candle closing lower** — confirmed reversal down.

The name logic: the second candle is *outside* (engulfs) the first → "Three Outside." The second candle is *inside* (contained by) the first → "Three Inside." Simple mnemonic.

**Why "three-candle" confirmation is worth it.** Empirically and logically, the confirmed versions outperform their two-candle parents because a confirmation candle in the reversal direction is direct evidence of follow-through — the exact thing the two-candle pattern cannot promise. In choppy, gap-prone markets like India's, where single candles are frequently reversed the next day, that third candle screens out a large fraction of head-fakes. The trade-off is fewer signals and a slightly later entry, which is almost always a worthwhile exchange for a swing trader.

## Mechanics, settings & identification

**Three Inside Up (bullish):**
1. Downtrend in progress.
2. Candle 1: long red body.
3. Candle 2: small green body **contained within** C1's body (a bullish harami). Opens above C1's close, closes below C1's open — body inside.
4. Candle 3: green, **closes above C2's close** (stronger if it closes above C1's open / C1's high).

**Three Inside Down (bearish):** downtrend→uptrend context reversed: uptrend, long green C1, small red C2 inside it (bearish harami), red C3 closing below C2 (stronger if below C1's open/low).

**Three Outside Up (bullish):**
1. Downtrend.
2. Candle 1: small red body.
3. Candle 2: long green body that **engulfs** C1 (bullish engulfing) — opens below C1's close, closes above C1's open.
4. Candle 3: green, **closes higher** than C2.

**Three Outside Down (bearish):** uptrend, small green C1, long red C2 engulfing it, red C3 closing lower.

**Settings & tolerances.**
- The reversal (third) candle should close *decisively* beyond the second — a token higher/lower close is weak. Prefer C3 closing beyond the *first* candle's far extreme where possible.
- Body sizes matter: C1 should be a real trend candle; the harami's C2 should be genuinely small (contraction). For the engulfing, C2 should fully cover C1's body (some allow shadow-inclusive; body-inclusive is stricter and better).
- Prior trend must exist. All four are *reversal* patterns; they mean nothing in a flat range.

**Screening (Chartink/TradingView).** These compound three-bar conditions are hard to encode perfectly, but a Chartink approximation for Three Inside Up: candle-3 close > candle-2 close, candle-2 is a green harami inside candle-1 (candle-2 high < candle-1 open, candle-2 low > candle-1 close), candle-1 red and long, and a prior downtrend filter (e.g. close < SMA(20)). Expect to eyeball results. TradingView's built-in candlestick pattern indicators include "Three Inside Up/Down" and "Three Outside Up/Down" — useful for backtesting but verify context and volume manually.

**Timeframe.** Reliable on **daily** and **weekly** charts (swing/positional). On intraday index futures (15-min), the confirmation candle is genuinely useful because it filters the many intraday fake reversals — but position size down for noise.

## Worked India examples (levels & ₹)

**Three Outside Up — reconstructed on HDFC Bank** (verify on your chart). Suppose HDFC Bank has been under FII-selling pressure, drifting from ₹1,720 to ₹1,640. Monday prints a small red candle (open ₹1,648, close ₹1,638) — sellers tiring but still in control. Tuesday, on strong results from a peer and value buying, HDFC Bank opens at ₹1,635 and **engulfs** Monday entirely, closing at ₹1,672 — a big green bullish-engulfing candle. Wednesday confirms: it opens at ₹1,674 and closes at ₹1,695 on rising volume. That is a **Three Outside Up**: small red → engulfing green → higher green. The reversal off the ₹1,640 support is now confirmed by follow-through. Entry on the Wednesday break (or Thursday above ₹1,695), stop below the engulfing candle's low (₹1,632), target the prior ₹1,720-1,740 zone.

**Three Inside Down — reconstructed on Nifty near a top.** Suppose Nifty rallies to 24,600 into euphoria. Monday: long green candle (open 24,420, close 24,590). Tuesday: a small red candle *inside* Monday's body (open 24,560, close 24,470) — a bearish harami, momentum stalling. Wednesday: a decisive red candle opening 24,465 and closing 24,360, below Tuesday's close and back below Monday's open. That is a **Three Inside Down**: the euphoric green day, then contraction, then a confirmed red reversal. It warns the up-leg is done. On an index, act via puts or a bear put spread; stop above Monday's high (24,600), first target the prior support around 24,200.

**Three Inside Up — reconstructed on a mid-cap at support.** A pharma mid-cap falls from ₹560 to ₹500. Thursday: long red candle (open ₹512, close ₹502). Friday: small green harami inside it (open ₹504, close ₹509) — sellers exhausted. Monday: green candle opening ₹510, closing ₹524 above Friday's close and Thursday's open — confirmation. **Three Inside Up** off ₹500 round-number support. Entry above ₹524, stop below ₹500, target ₹550-560.

## How to trade them — entry, stop, target

**Bullish (Three Inside Up / Three Outside Up):**

| Element | Rule |
|---|---|
| Trigger | Enter on the **close of the third (confirmation) candle**, or more conservatively on a next-day break above C3's high. The confirmation candle is your permission to act — that's the whole point of the pattern. |
| Stop | Below the **low of the pattern** — for Three Outside Up, below the engulfing candle's low; for Three Inside Up, below C1's (or the harami's) low. |
| Target 1 | Prior swing high / measured move ≈ 1.5-2x risk. |
| Target 2 | Larger resistance; trail with a moving average or chandelier stop. |
| Timeframe | Daily swing (days-to-weeks hold). |
| Regime | Best when the broader index is neutral-to-supportive; a bullish reversal aligned with a stabilising Nifty is far higher-odds. |

**Bearish (Three Inside Down / Three Outside Down):**

| Element | Rule |
|---|---|
| Trigger | Enter short on C3's close or a break of C3's low; use it to exit longs/hedge immediately. |
| Stop | Above the **high of the pattern** (engulfing high for Three Outside Down; C1/harami high for Three Inside Down). |
| Target | Prior support / measured move; on indices prefer put spreads to cap risk. |
| Timeframe | Daily swing. |

**Three Outside vs Three Inside — which to prefer?** The Three Outside (confirmed engulfing) is generally the stronger of the two because its middle candle already showed *domination* (an engulfing), whereas the Three Inside's middle candle only showed *contraction* (a harami). If you must rank: Three Outside Up/Down > Three Inside Up/Down in reversal strength, all else equal. But the Three Inside often gives a *tighter* stop (the harami is compact), which can mean better risk-reward when it works.

## Confluence (including OI)

- **Location.** All four are dramatically stronger at a tested support/resistance, round number, moving average, or Fibonacci retracement. A Three Inside Up floating mid-range is far weaker than one off Nifty 24,000 or a 200-DMA.
- **Volume.** The confirmation (third) candle ideally carries above-average volume — real participation validating the turn. For Three Outside, the engulfing candle itself should show a volume surge.
- **Momentum.** A bullish version coinciding with a bullish RSI/MACD divergence is a high-conviction stack. A bearish version with an overbought RSI rolling over adds confidence.
- **Option chain / OI.** For an index bullish Three Outside/Inside Up near support, look for heavy and rising **Put OI** at that strike (put writers defending) plus **Call unwinding** overhead — smart money agreeing with the reversal. For a bearish Three Inside/Outside Down at resistance, look for aggressive **Call writing** at the top strike and Put unwinding below. In F&O stocks, confirm with futures OI: a bullish reversal with price up + OI up on the confirmation day = fresh longs (sustainable); price up + OI down = short covering (may fizzle).
- **Multiple-timeframe alignment.** A daily Three Outside Up that also sits at a weekly support is a premium setup.

## Pitfalls

1. **Trading the pattern with no prior trend.** These are *reversal* patterns. In a sideways chop they generate constant, meaningless signals. Demand a clear preceding trend.
2. **Weak confirmation candle.** If the third candle barely closes beyond the second, the "confirmation" is hollow. Demand a decisive close — ideally beyond the first candle's far extreme.
3. **Ignoring location.** The biggest edge multiplier is *where* the pattern forms. Off a major level = trade it; mid-air = skip it.
4. **Over-tight labelling on the harami/engulfing.** Be reasonable with body/shadow tolerances, but don't call every three-candle wiggle a Three Inside/Outside. The middle candle must genuinely be a harami (contained) or engulfing (engulfs).
5. **Position sizing on indices.** On Nifty/Bank Nifty, express bearish versions with defined-risk option structures, not naked futures shorts — gap risk overnight is real.
6. **Forgetting the trade-off.** The confirmation candle costs you a later entry. Accept it. Traders who try to "jump the gun" and enter on the harami/engulfing before the third candle are just trading the weaker two-candle pattern and forfeiting the entire benefit.

## Interview-ready summary

The **Three Inside** and **Three Outside** patterns are the harami and the engulfing, respectively, with a third **confirmation candle** added. Three Inside Up = bullish harami (big red, small green inside) + a green candle closing higher; Three Inside Down is its bearish mirror in an uptrend. Three Outside Up = bullish engulfing (small red, big green swallowing it) + a green candle closing higher; Three Outside Down is its bearish mirror. The third candle is the whole innovation: it converts a *possible* reversal into a *confirmed* one, filtering out the many two-candle head-fakes at the cost of a slightly later entry. Three Outside (confirmed engulfing) is generally stronger than Three Inside (confirmed harami) because its middle candle already showed domination. Trade the confirmation candle's close, stop beyond the pattern's opposite extreme, demand a prior trend plus a supportive location (support/resistance, round number, MA, Fib), and confirm with volume, momentum, and option-chain OI (put/call writing and unwinding). Fewer signals, better signals — that is the entire point of adding the third candle.
