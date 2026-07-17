# Confidence, Conviction & Sizing

Position sizing is where technical analysis meets money, and money is where psychology stops being an abstraction. You can have the best chart read on the desk — a textbook Bank Nifty breakout retest with volume confirmation — and still blow up, if you size it wrong. Conversely, a mediocre edge, sized with discipline, survives for years. This chapter is about the middle layer that almost no retail trader manages deliberately: the translation of *how confident you are* into *how much you bet*, without letting confidence curdle into arrogance or evaporate into fear.

## The principle: conviction and size must be coupled — but bounded

There are two failure modes, and most traders live at one extreme.

The **flat-sizer** bets the same amount on every trade regardless of setup quality. This is disciplined but leaves money on the table: it treats a marginal, forced setup the same as a once-a-month, everything-aligned A+ setup. Over a career, failing to press your genuinely best opportunities is a real and large cost.

The **wild-sizer** bets according to raw emotion — huge on a "sure thing," tiny on the trades that scare them. The problem is that a trader's *feeling* of certainty correlates poorly, and sometimes inversely, with actual probability. The trades that feel like "can't-lose" are frequently the crowded, obvious, late-stage moves where risk/reward is worst. Emotional conviction is a terrible sizing input on its own.

The professional answer is **structured conviction sizing**: you tier your setups by objective, pre-defined quality criteria, assign each tier a size multiple, and *cap the maximum*. Conviction moves your size — but within a bounded, rules-based band, never to the moon. The coupling is real but leashed.

## The method: a conviction-tiered sizing framework

First, define your base unit. Everything is expressed as **R**, your risk per standard trade, set as a fixed small percentage of equity — for most serious retail traders, **0.5% to 1.0% per trade.** On a ₹5,00,000 account at 1%, 1R = ₹5,000 of risk (not position value — the amount you lose if stopped).

Now tier your setups by *objective confluence*, not feeling:

| Tier | Objective criteria (must meet most) | Size | Frequency |
|---|---|---|---|
| A+ | Higher-timeframe trend aligned + key level + pattern + volume + no event risk | 1.5–2.0R | Rare (few/month) |
| A | HTF trend aligned + level + one confirmation | 1.0R | Bread-and-butter |
| B | Decent setup, one element missing (e.g. against minor trend) | 0.5R | Common |
| C | Marginal, forced, "I'm bored" | 0R — skip | Should not exist |

The critical discipline: **conviction must be earned by confluence you can name, not by a feeling.** Before you upsize to A+, you must be able to list — out loud or in your journal — the specific, objective reasons this setup is superior: "Weekly trend up, price at a retested breakout level with a bullish engulfing on the daily, above-average volume, and no RBI or Fed event for three days." If you cannot enumerate the confluence, it is not an A+ trade no matter how excited you feel. Excitement without articulable confluence is the exact signature of a crowded trap.

### Why the cap matters: the mathematics of ruin

The reason A+ is capped at ~2R and not 5R or "all-in" is the mathematics of risk of ruin. Even a strong edge produces losing streaks. If you size any single trade large enough that a normal streak can cripple you, then your *long-run compounding* is destroyed by a *short-run* variance event that was always going to happen.

Consider the Kelly Criterion, the mathematically optimal growth-maximising bet size. For a trade with win probability *p*, loss probability *q = 1−p*, and win/loss payoff ratio *b*:

**f\* = (b·p − q) / b**

Take a good edge: p = 0.50, b = 2 (winners twice the size of losers). Full Kelly says f\* = (2×0.5 − 0.5)/2 = 0.25 — bet 25% of capital per trade. This is *insane* in practice. Full Kelly assumes you know your true probabilities perfectly (you don't), tolerates gut-wrenching drawdowns (a 50%+ drawdown is routine at full Kelly), and punishes any overestimate of your edge severely. The professional standard is **fractional Kelly — one-quarter to one-half Kelly.** Quarter-Kelly on the above is ~6% risk, and even that is aggressive for most retail temperaments. This is precisely why the framework caps A+ at 1.5–2% of equity: it sits comfortably inside safe fractional-Kelly territory *even for your best trades*, so no single bet — however "certain" it feels — can threaten the account.

The lesson from Kelly is subtle and worth internalising: **oversizing doesn't just add risk, it lowers your long-term growth rate.** Past a certain point, betting bigger makes you compound *slower* because the drawdowns eat the compounding. Bigger size is not braver; past the optimum it is simply worse math.

## Worked example: Priya sizes three Nifty trades

Priya runs a ₹10,00,000 swing account, 1R = 1% = ₹10,000 risk. She's looking at three setups on a single evening.

**Trade 1 — Nifty positional long.** Weekly trend up, price pulled back to the rising 20-week EMA at 24,600, which coincides with a prior breakout level and the 0.5 Fibonacci retracement of the last leg. Daily prints a bullish hammer on above-average volume. No major event for a week. She enumerates: HTF trend ✓, key level (triple confluence) ✓, reversal candle ✓, volume ✓, no event ✓. **This is A+.** She sizes 1.75R. Her stop is 250 points below entry; risk = 1.75 × ₹10,000 = ₹17,500. Position = ₹17,500 / 250 points per lot-point exposure → she calculates lots accordingly.

**Trade 2 — Reliance swing long.** Uptrend intact, price at the 50-day EMA, but no reversal candle yet and quarterly results are in four days. HTF trend ✓, level ✓, but confirmation missing and *event risk present*. **This is a B, downgraded by the event.** She sizes 0.5R = ₹5,000 risk. The results could gap it either way; small size respects that uncertainty.

**Trade 3 — Bank Nifty countertrend short.** Daily trend is up, but she "feels" it's overextended and due a fall. She checks her criteria: HTF trend is *against* her, no level rejection yet, no bearish confirmation. The only input is a feeling. **This is a C. She skips it.** Two days later Bank Nifty rallies another 400 points. Her discipline saved a loss that emotion would have taken.

Note the structure: her *biggest* bet went on the trade with the most nameable confluence and *least* event risk, her small bet on the promising-but-uncertain one, and the emotion-only "conviction" trade got zero size. Conviction moved her size — but only conviction she could justify objectively.

## The confidence problem: two failure modes and their fixes

Confidence is the psychological fuel of sizing, and it swings dangerously in both directions.

**Overconfidence** typically arrives *after a winning streak.* You've had six green trades, you feel invincible, and you start upsizing everything to A+ regardless of actual confluence, moving stops wider "because you're hot," and taking C-grade setups because "you can't lose right now." This is how good months end in bad weeks. The fix is mechanical: **your tier criteria don't change based on your recent P&L.** An A+ trade requires the same confluence whether you're on a winning streak or a losing one. Winning does not upgrade a B setup to an A+. Bolt this rule down, because the streak will actively lie to you.

**Underconfidence** arrives after losses. You've been stopped out three times, and now you can't pull the trigger on a genuine A+ setup, or you cut your winners at +0.5R because you're terrified of giving back gains. This is equally destructive — it means you *miss the trades that pay for all the losers.* The fix is also mechanical: **if the setup meets the tier criteria, you take it at the tier size, full stop.** Your hesitation is not new information about the trade; it is residue from prior trades that has nothing to do with this chart. Trusting the checklist over the feeling is the whole skill.

The deeper truth: **real conviction is quiet.** It is the calm, almost boring certainty that comes from a checklist being fully ticked, not the adrenaline surge of a "sure thing." When you feel euphoric excitement about a trade, be suspicious — euphoria is usually the crowd's emotion, and the crowd is usually late. When you feel a steady, unhurried "yes, this meets all my criteria," *that* is the feeling to size up on.

## Building it into your routine

- **Pre-trade sizing checklist.** Before every entry, tick the tier criteria and *write the tier and R-multiple down before you click buy.* This forces conviction to be articulated, not felt, at the moment it matters.
- **Fix R as a percentage, recompute in rupees weekly.** As your account grows or shrinks, 1R changes. Update the rupee value of 1R at the start of each week so your sizing scales correctly. Never anchor to a stale rupee figure.
- **Cap the number of A+ trades you allow yourself.** If you're marking five trades a week as A+, you're inflating the grade. Genuine A+ confluence is *rare* — a handful a month. A cap (say, max two A+ per week) keeps the grade honest.
- **Position size from the stop, always.** Number of lots = (R in rupees) / (stop distance in points × value per point). Never size from account balance or from how much you "want to make." The stop defines the size; the target does not.
- **Journal the size decision, not just the trade.** Record *why* you assigned the tier. Over time you'll see whether your A+ trades actually outperform your B trades — if they don't, your grading criteria are wrong and need recalibration. This closes the loop between conviction and reality.
- **Never average down outside a pre-planned scale-in.** Adding to a loser because "conviction is even higher now" is the single most seductive sizing error. If scaling in is part of the plan, it's defined *before* entry with defined levels and a total-risk cap. Improvised averaging is not conviction; it's denial with a position size.

## Interview-ready summary

- **Couple size to conviction, but bound it.** Flat-sizing leaves money on the table; emotion-sizing blows up. Tier setups by objective confluence (A+/A/B/C) and assign R-multiples (2.0 / 1.0 / 0.5 / skip).
- **Conviction must be nameable.** You may only upsize to A+ if you can enumerate the specific confluence. Excitement without articulable reasons is the signature of a crowded trap, not an edge.
- **Cap your best trades at ~1.5–2% of equity** because of risk of ruin. The Kelly Criterion (f\* = (bp−q)/b) shows full Kelly is far too aggressive; professionals use ¼-to-½ Kelly. Oversizing doesn't just add risk — past the optimum it *lowers* your long-term growth rate.
- **Size from the stop, never from the target or the balance.** Lots = R-in-rupees ÷ (stop distance × value per point).
- **Confidence swings both ways and both are traps.** Overconfidence after wins inflates grades; underconfidence after losses freezes the trigger. The fix for both is mechanical: tier criteria and tier sizes do not change based on recent P&L.
- **Real conviction is quiet.** Euphoria signals the crowd; a calm, checklist-complete "yes" is what you size up on.
