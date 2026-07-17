# Three Drives & ABCD Patterns

## What they are & why they work

The ABCD and the Three Drives are the two foundational *measured-move* patterns of the harmonic family. Everything more exotic — Gartley, Butterfly, Crab, Bat — is really an elaboration of the ABCD skeleton with extra Fibonacci constraints. Learn these two well and you own the grammar that the whole harmonic vocabulary is built from.

An **ABCD** is a two-leg zig-zag: an impulse leg (A→B), a partial retracement (B→C), and a second impulse (C→D) that is proportional to the first. It is the market breathing in and out — a push, a pause, an equal push. It works because trends move in waves of *similar magnitude*: institutional order flow tends to be executed in comparable clips, and the crowd's profit-taking and re-entry happen at Fibonacci-spaced intervals. When CD mirrors AB, you have a natural exhaustion point at D where the second wave has "done the same work" as the first — a logical place for the move to stall and reverse.

A **Three Drives** is ABCD's bigger cousin: *three* successive drives to a high (or low), each separated by a Fibonacci retracement, ending in exhaustion. Where ABCD has two pushes, Three Drives has three, and the symmetry across all three is what makes the terminal point (drive 3) such a high-probability reversal. It works because it captures the *last gasp* of a trend — three increasingly-strained thrusts into the same direction, each requiring more effort for less reward, until the buyers (or sellers) are spent. It is visually close to an Elliott ending-diagonal or a "rising three drives = distribution."

Both are **reversal-timing tools**. They don't predict *that* a market will turn — they tell you *where* the current leg is likely to complete, so you can fade it with tightly-defined risk. That is their real value: they convert a vague "this looks extended" into a precise price zone with a measurable stop.

## Mechanics, formula & settings — ABCD

Label four points: **A** (start), **B** (end of first impulse), **C** (retracement of AB), **D** (completion). The rules:

1. **BC retraces AB** to a Fibonacci ratio — most commonly **0.618**, but valid anywhere in the **0.382 to 0.886** band. A shallow 0.382 retrace signals a strong trend; a deep 0.786/0.886 signals a weaker one.
2. **CD extends BC** by the reciprocal Fibonacci — if BC = 0.618 of AB, then CD ≈ **1.618 of BC**. If BC = 0.786, then CD ≈ **1.272 of BC**. The deeper the retrace, the smaller the extension, and vice-versa — they are reciprocals.
3. **AB ≈ CD in price and often in time.** The classic ("perfect") ABCD has CD equal in length to AB, and the two legs taking a similar number of bars. This price-and-time symmetry is the pattern's signature.

There are two variants worth knowing:
- **AB=CD (perfect):** CD length = AB length. The default.
- **Extended ABCD:** CD = 1.27 or 1.618 × AB. Common in strong trends; the terminal reversal is often sharper but D is harder to pin.

**Settings:** Draw with a Fibonacci retracement tool (for BC) and a Fibonacci extension tool (for CD projected from C). On TradingView, the built-in "XABCD Pattern" tool lets you drop the points and it prints the ratios live — set it to ABCD by ignoring X. Works on any timeframe; higher timeframes (daily, 4-hour) give cleaner, more reliable Ds than 5-minute charts.

## Mechanics — Three Drives

Label the swings: three drives (**1, 2, 3**) with two intervening pullbacks (**A, B**).

1. **Drive 1** completes an initial thrust.
2. **Pullback A** retraces drive 1 to **0.618**.
3. **Drive 2** extends to **1.272** of pullback A (a higher high in a bearish setup / lower low in a bullish one).
4. **Pullback B** retraces drive 2 to **0.618**.
5. **Drive 3** extends to **1.272** of pullback B — this is the **completion point** and the trade zone.

The elegance is the symmetry: pullback A ≈ pullback B (0.618 each), and drive 2 ≈ drive 3 (1.272 each). When all four legs obey their ratios *and* the two pullbacks look alike in time and price, the drive-3 terminal is a premium reversal spot. Ideally drive 3 also prints a momentum divergence — price higher, RSI lower.

Some texts allow 1.618 extensions and 0.786 retracements; treat 0.618/1.272 as the core template and the others as acceptable tolerances (± a few percent). Perfection is rare — you want *proximity* to the ratios, not decimal precision.

## Worked India example — ABCD on Bank Nifty (levels & ₹, approximate reconstruction)

Bank Nifty on the daily chart. Verify these levels on your own chart; they are a teaching reconstruction.

- **A = 47,000** (a swing low).
- Rally to **B = 49,500** — the AB impulse leg is **2,500 points**.
- Pullback to **C = 48,000** — BC retraced 1,500 points, which is **0.60 of AB** (≈0.618). Clean.
- For a perfect AB=CD, project CD = AB = 2,500 points from C: **48,000 + 2,500 = 50,500 = D**.
- Cross-check with the extension: CD ≈ 1.618 × BC = 1.618 × 1,500 = 2,427 → D ≈ 50,427. The two methods bracket **50,430–50,500** — that is your **D reversal zone**.

Bank Nifty grinds up and tags 50,470, printing a bearish RSI divergence and a shooting-star candle. That confluence at the projected D says: *the second impulse has done the same work as the first — fade it.*

**The trade (short):**
- Entry: on the reversal candle close inside 50,430–50,500, say **50,450**.
- Stop: above the pattern's structural invalidation — beyond the 1.272 extension of AB, roughly **50,800** (about 350 points risk).
- Target 1: back to C, **48,000** (2,450 points) — a ~7:1 reward-to-risk to the first target alone.
- Target 2: the 0.618 retrace of the whole AD move, or the A origin at 47,000 if momentum accelerates.

Even booking half at C is a superb trade. Note how the pattern did the timing work: without it, "Bank Nifty looks toppy near 50k" is a hunch; *with* it, you have an entry, a stop, and a target defined to the point.

## Worked India example — Three Drives on Nifty (approximate)

Nifty daily, a topping sequence:
- **Drive 1** high at **24,200**, pullback A to **23,800** (0.618-ish of the prior up-leg).
- **Drive 2** to **24,500** = 1.272 extension of pullback A. Pullback B to **24,150** (≈0.618 of drive 2).
- **Drive 3** projects to 1.272 of pullback B → **24,150 + 1.272 × (24,500−24,150 measured appropriately)** ≈ **24,580–24,620**.

Nifty pokes **24,600**, the third and most-strained thrust, with RSI making a *lower* high than at drive 2 — a textbook bearish divergence at the terminal drive. Three pushes, diminishing momentum, symmetric structure: distribution.

**The trade (short):** enter on the reversal near 24,600, stop above 24,720 (beyond drive 3), first target back to pullback-B at 24,150, second target to pullback-A at 23,800. Risk ~120 points for 450+ points of first-target reward.

## How to trade them (entry / stop / target)

| Element | ABCD | Three Drives |
|---|---|---|
| Trigger | Reversal candle / lower-timeframe structure break at **D** | Reversal candle at **drive 3** terminal |
| Entry | Inside the D zone on confirmation, not on a limit into thin air | Inside the drive-3 zone on confirmation |
| Stop | Beyond the 1.272 extension of AB (a hair past D) | Beyond the drive-3 extreme |
| Target 1 | Point **C** | Pullback **B** |
| Target 2 | 0.618 retrace of AD / point **A** | Pullback **A** / drive-1 origin |
| Timeframe | 4-hour and daily cleanest; usable intraday | Daily/weekly for majors; intraday on indices |
| Regime | Fading over-extension in ranges or at trend ends | End-of-trend exhaustion; strong in distribution/accumulation |

The universal discipline: **wait for D (or drive 3) to actually print and show a reversal signal.** These are *reaction* trades — you are betting the leg completes and reverses, so let it complete. Entering a limit order "somewhere near D" before price arrives is how traders get run over when the pattern extends or fails.

## Confluence (including OI)

- **Fibonacci cluster:** The strongest Ds sit where the AB=CD projection *and* an independent retracement of a larger swing land together (a "PRZ" — potential reversal zone). Two Fibs agreeing beats one.
- **Momentum divergence:** A bearish RSI/MACD divergence at D or drive 3 is almost mandatory for high conviction. No divergence → lower probability.
- **Candlestick confirmation:** A pin bar, engulfing, or shooting star exactly at D converts a zone into a trigger.
- **Structural / round levels:** D coinciding with a prior swing high, a round number (Nifty 24,500; Bank Nifty 50,000), or a VWAP anchor adds weight.
- **Open Interest (F&O):** On an index Three-Drives top, look for heavy **call writing** building at the strike near drive 3 — market-makers capping the move — plus **long unwinding** (price up, OI down) into the final drive, signalling the last longs distributing. As the reversal begins, a shift to **call OI addition and put unwinding** confirms sentiment flipping bearish. On a bullish ABCD/Three-Drives *bottom*, the mirror: aggressive **put writing** at the D-zone strike marks the floor, and short-covering (price up, OI down) fuels the reversal off D.
- **Time symmetry:** When CD takes about the same number of bars as AB (or pullback B mirrors pullback A in time), the pattern is "in proportion" and more reliable.

## Pitfalls

1. **Forcing ratios.** Not every three-wave wiggle is an ABCD. If BC retraces only 0.20 or CD is 3× AB, it is not the pattern — it is a trend. Respect the 0.382–0.886 / 1.272–1.618 tolerances and reject setups that don't fit.

2. **Anticipating D instead of confirming it.** The single most common loss: shorting into an extended CD before it tops. In a strong trend, an "AB=CD" can morph into a "1.618 extended ABCD" and blow through your stop. Always demand a reversal trigger *at* D.

3. **Wrong swing selection.** ABCD is subjective — pick different A/B/C points and you get a different D. Anchor to *significant, obvious* swing highs/lows, not micro-noise. If you have to hunt for the points, the pattern isn't there.

4. **Ignoring the higher timeframe trend.** Fading a Three-Drives short inside a powerful weekly uptrend is fighting the tape. Best results come when the pattern completes *against* an over-extended move at a higher-timeframe resistance, not in the middle of a healthy trend.

5. **No divergence, no trade.** A Three Drives whose final drive shows momentum *confirming* (RSI making a new high with price) is likely to continue, not reverse. Skip it.

6. **India gap/circuit risk.** On single stocks, overnight news can gap price through the D zone. Prefer indices (Nifty/Bank Nifty) for cleaner harmonics and, for stock plays, define risk with options rather than naked futures.

7. **Over-optimising decimals.** Chasing 61.8% to two decimals is false precision. These are behavioural approximations; a D at 0.60 or 0.64 is fine. Zones, not points.

## Interview-ready summary

ABCD and Three Drives are the core *measured-move* harmonic patterns. An **ABCD** is a two-impulse zig-zag where BC retraces AB (0.382–0.886, typically 0.618) and CD extends BC by the reciprocal ratio (1.272–1.618), so that CD ≈ AB in price and time; you fade the completion point **D**, stop just beyond it, and target back to C and then A. **Three Drives** stacks three Fibonacci-spaced thrusts — pullbacks of 0.618 and extensions of 1.272 — with the third, most-strained drive marking terminal exhaustion, ideally on a momentum divergence. Both are *timing* tools: they turn "this looks over-extended" into a precise reversal zone with defined risk, and both demand confirmation *at* the completion point rather than anticipation. On Indian indices, pair them with RSI divergence, candlestick triggers, round-number/structural confluence, and OI signals (call-writing and long-unwinding at a top; put-writing and short-covering at a bottom). Traded with patience and honest risk-reward — often 4:1 or better to the first target — they are among the most repeatable fade setups in the harmonic toolkit.
