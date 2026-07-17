# Risk of Ruin & Kelly (Deep)

You can have a genuinely profitable system — positive expectancy, a real edge, backtested across regimes — and still go broke. That sentence is not a paradox; it is the central, brutal truth of position sizing. A positive edge tells you that if you could play *infinitely* with *infinitely small* bets, you would end rich. But you cannot. You play a finite number of trades with finite capital, and if you bet too large relative to your edge, a normal losing streak — one that the math *guarantees* will happen — takes your account to a level from which you cannot recover. This chapter is about the two numbers that govern survival: **risk of ruin** (the probability that a losing streak kills you) and the **Kelly criterion** (the bet size that maximises long-run growth without killing you). Get these wrong and no amount of chart-reading skill saves you.

## The Principle: Survival Is Prior to Profit

There is an order of operations in trading that most retail traders invert. They optimise for *return* first and worry about *risk* never. The correct order is: **survive, then grow, then optimise.** The reason is arithmetic and merciless — the **drawdown recovery asymmetry**:

| Drawdown | Gain needed to recover |
|----------|------------------------|
| −10% | +11.1% |
| −20% | +25.0% |
| −25% | +33.3% |
| −33% | +50.0% |
| −50% | +100% |
| −60% | +150% |
| −75% | +300% |
| −90% | +900% |

A 50% loss requires a 100% gain to get back to even. A 90% loss — the classic blown F&O account — requires a *tenfold* return just to be whole. Ruin is not "losing everything"; **ruin is losing enough that recovery becomes practically impossible.** For most traders that threshold is a 40–50% drawdown: the emotional and mathematical hole is simply too deep. Everything in position sizing is in service of never reaching that hole.

## Risk of Ruin: The Formula That Should Scare You

Risk of ruin (RoR) is the probability that your account draws down to a defined "ruin" level (often −50%, or a hard stop like −30%) before you achieve your goal, given your win rate, payoff ratio, and — critically — your **bet size per trade.** 

For a simplified fixed-fractional model where you risk a fraction *f* of capital per trade, with win probability *W* and a payoff ratio, an approximate RoR can be computed via the "gambler's ruin" framework. The intuition matters more than the exact formula, so let's build it with a concrete table. Assume a system, and vary only the **risk-per-trade**:

**System: 45% win rate, winners +2R, losers −1R (expectancy = 0.45×2 − 0.55×1 = +0.35R — a good system).**

| Risk per trade | Approx. Risk of Ruin (to −50%) | Verdict |
|----------------|-------------------------------|---------|
| 1% | < 1% | Safe |
| 2% | ~2% | Safe |
| 3% | ~8% | Caution |
| 5% | ~25% | Dangerous |
| 7% | ~45% | Reckless |
| 10% | ~70% | Near-certain eventual ruin |
| 15% | ~93% | Suicidal |

Read this table until it changes how you feel. **The same profitable system has a 70% chance of ruin at 10% risk and under 1% at 1% risk.** The edge did not change. The *bet size* changed. This is the entire game. The trader risking 10% per trade on a genuinely winning strategy will still, more likely than not, blow up — not because the strategy was bad, but because a run of losers (which a 55%-loss-rate system throws constantly) compounds against an oversized bet.

### Why streaks are longer than your gut believes

The engine of ruin is the losing streak, and human intuition wildly underestimates streak length. For a system that loses 55% of the time, the probability of a run of *k* consecutive losers in a sequence of N trades is far higher than people guess:

- Probability of at least one 5-loss streak in 100 trades: **~85%.**
- At least one 7-loss streak in 200 trades: **~70%.**
- At least one 10-loss streak in 500 trades: **~40%.**

If you trade a 45%-win system for a year (say 250 trades), you should **expect** to hit a 6–8 loss streak at some point. Now do the arithmetic: an 8-loss streak at 3% risk each is a compounded loss of about 1 − (0.97)^8 ≈ **21.7%** drawdown. At 5% risk: 1 − (0.95)^8 ≈ **33.7%**. At 10% risk: 1 − (0.90)^8 ≈ **56.9%** — ruin, from a *normal* streak in a *winning* system. The streak is not bad luck; it is the scheduled, guaranteed weather of your edge. Position sizing is the coat you wear so the weather doesn't kill you.

### An India-specific ruin scenario

A Bank Nifty options buyer has a real edge on momentum days: 38% win rate, average winner +3.2R, average loser −1R. Expectancy = 0.38×3.2 − 0.62×1 = +0.596R. Genuinely excellent. He has ₹5 lakh and, feeling confident, risks ₹50,000 (10%) per trade because "the edge is strong." 

His edge *is* strong. But a 62%-loss-rate system throws a 6-loss streak roughly once every 40–50 trades. In his second week he catches one: six choppy, trendless expiry-week sessions where every momentum signal fails. Six losses at 10%: capital falls to 5,00,000 × (0.9)^6 = **₹2.66 lakh** — a 47% drawdown. To recover he now needs +88%. Psychologically shattered, he doubles size to "make it back fast," catches two more losers, and is finished. **The edge never failed. The sizing did.** Had he risked 1.5% (₹7,500), the same six-loss streak costs him just 8.6% — an ordinary, survivable dip he'd barely remember. Same trades, same edge, opposite outcomes, decided entirely by *f*.

## The Kelly Criterion: The Mathematically Optimal Bet

If small bets are safe but slow, and large bets are fast but fatal, there must be an optimal size that maximises long-run *compounded* growth. There is, and it's called the **Kelly criterion.** Kelly answers: *what fraction of capital should I risk to grow my account as fast as mathematically possible over the long run?*

The classic Kelly formula for a bet with win probability *W*, loss probability *L = 1−W*, and payoff ratio *b* (average win ÷ average loss):

**Kelly % = W − (L / b)**

Equivalently, `Kelly f = (b×W − L) / b`. Let's apply it to our systems.

**System 1: W = 45%, payoff b = 2 (winners +2R, losers −1R):**
Kelly f = 0.45 − (0.55 / 2) = 0.45 − 0.275 = **0.175 = 17.5%.**

Kelly says risk 17.5% of capital per trade to maximise growth. **And you should absolutely not do that** — which brings us to the most important practical point in this chapter.

**System 2 (the Bank Nifty options buyer): W = 38%, b = 3.2:**
Kelly f = 0.38 − (0.62 / 3.2) = 0.38 − 0.194 = **0.186 = 18.6%.**

Full Kelly for a strong edge is often in the 15–25% range. Full Kelly is the theoretical growth-maximising fraction — but its **drawdowns are horrific and its assumptions are fragile.**

### Why nobody trades full Kelly

Full Kelly maximises geometric growth *only if* your W and b are known *exactly* and *stable forever*. In real trading, neither is true — you estimate W and b from a noisy sample of 100 trades, and markets change regime. Three deadly problems:

**1. Full Kelly's drawdowns are savage.** At full Kelly, a drawdown of 50% is a *routine, expected* event — it happens with near-certainty over enough trades. Kelly maximises *terminal wealth in theory* while cheerfully accepting 50%+ drawdowns that would psychologically destroy any human and financially destroy anyone with withdrawal needs. A property of full Kelly: the probability of your equity ever halving before it doubles is roughly 50%. No professional accepts that.

**2. Overestimating your edge is catastrophic.** If you *think* W = 45% but the true value is 40%, your "optimal" bet is now *past* the peak of the growth curve — on the far side, where **increasing bet size decreases growth and increases ruin.** Because you always estimate edge with error, and because the cost of overbetting is far worse than underbetting (the growth curve is steep and punishing beyond the peak), you must deliberately bet *below* Kelly.

**3. The growth curve is asymmetric.** Betting at *half* Kelly captures about **75% of the maximum growth rate while roughly halving the volatility and drawdown.** That is one of the best trades in all of finance: give up a quarter of your growth to halve your risk. This is why the standard professional practice is **fractional Kelly.**

### Fractional Kelly — the practitioner's setting

| Kelly fraction | Growth vs. full | Drawdown character | Who uses it |
|----------------|-----------------|--------------------|-------------|
| Full (1.0×) | 100% | Terrifying (50%+ routine) | Nobody sane |
| Half (0.5×) | ~75% | Halved | Aggressive pros |
| Quarter (0.25×) | ~44% | Very manageable | Most professionals |
| Tenth (0.1×) | ~19% | Gentle | Conservative / uncertain edge |

For System 1 (full Kelly 17.5%): **half Kelly = 8.75%, quarter Kelly = 4.4%.** Even quarter Kelly at 4.4% risk per trade is *aggressive* by retail standards — recall from the RoR table that 5% risk carried ~25% ruin probability. This tension is the crux: **Kelly's "optimal" is far larger than what survival tolerates**, because Kelly optimises growth assuming a perfectly known, stable edge, while survival must account for edge uncertainty and human psychology.

The reconciliation professionals use: **treat 1–2% risk per trade as the practical ceiling, and let Kelly tell you when to be at the low end.** If Kelly says 4% and you cap at 1%, you know your edge has room and you can size at the full 1% with confidence. If Kelly says 0.8%, your edge is thin — size *below* 1%, at maybe 0.5%. **Kelly becomes a governor, not a target.** It tells you how much cushion you have, not how much to bet.

## Building the System Into Your Routine

**Step 1 — Compute your real Kelly from your R-log.** After 100+ trades you have W and b. Plug into Kelly = W − (L/b). Suppose your Nifty swing system shows W = 42%, b = 2.3: Kelly = 0.42 − (0.58/2.3) = 0.42 − 0.252 = **0.168 = 16.8%.**

**Step 2 — Take a small fraction of it.** Quarter Kelly = 4.2%. But apply the survival cap: **you will risk 1%.** Because 1% is well below even quarter Kelly, you know you are sizing *conservatively relative to your edge* — the safest possible zone. This is the whole point: Kelly confirms 1% is safe here.

**Step 3 — When Kelly drops, cut size.** Re-estimate quarterly. If a regime shift pushes your rolling W to 35% and b to 1.8: Kelly = 0.35 − (0.65/1.8) = 0.35 − 0.361 = **−0.011 = negative.** **A negative Kelly means STOP — the edge has vanished and any bet size loses money long-term.** This is Kelly's most valuable signal: it tells you when to stand down entirely, something no chart pattern will.

**Step 4 — Never let Kelly justify going above your survival cap.** If Kelly says 20%, that is information about edge strength, *not permission* to risk 20%. The RoR table is the veto. Growth is worthless if a normal streak ruins you before you compound it.

## Pitfalls

- **Trading full Kelly.** Guarantees repeated 50% drawdowns; overestimated edge makes it fatal. Never do it.
- **Estimating Kelly from too few trades.** With N = 20, your W and b are noise; the Kelly number is fiction. Need 100+ trades.
- **Ignoring correlation.** If you have five open positions all long Nifty-correlated names (banks + financials + Nifty futures), your *effective* risk is not 5 × 1% = 5%; it's closer to one big 4–5% correlated bet because they'll all lose together on a gap-down. Kelly and RoR assume *independent* trades. Correlated positions multiply real risk. Size the *portfolio*, not the trade.
- **Fat left tails break Kelly.** Kelly's payoff *b* assumes losers are bounded at ~1R. Naked option selling has occasional −8R tails; Kelly computed on the "normal" losers massively overstates safe size. For any strategy with tail risk, cut the Kelly fraction hard.
- **Anti-martingale creep.** After a win streak, edge feels huge and traders quietly raise size past Kelly. Recompute from data, not feelings.
- **Confusing account-halving with recoverable.** −50% needs +100%. Traders who "know the math" still routinely reach it because they sized to Kelly, not to survival.

## Interview-Ready Summary

A positive-expectancy system can still go broke if bet size is too large, because losing streaks are guaranteed and drawdowns recover asymmetrically (−50% needs +100%, −90% needs +900%). Risk of ruin is the probability a normal streak takes you to an unrecoverable level; for a fixed system it explodes with risk-per-trade — the same +0.35R system has <1% ruin at 1% risk and ~70% ruin at 10% risk. Streaks are longer than intuition suggests: a 55%-loss system should be expected to throw a 6–8 loss run over a year, which is survivable at 1–2% risk and fatal at 10%. The Kelly criterion, `f = W − (L/b)`, gives the growth-maximising fraction, but full Kelly accepts routine 50% drawdowns and is catastrophic if you overestimate your edge — so professionals use fractional Kelly (half Kelly ≈ 75% of growth at half the volatility; quarter Kelly is common). In practice, cap risk at 1–2% for survival and use Kelly as a governor: it confirms 1% is conservative when Kelly is high, tells you to size down when Kelly is low, and signals a full stop when Kelly goes negative (edge gone). Always size the correlated portfolio rather than the single trade, and cut Kelly hard for any strategy with fat left tails.
