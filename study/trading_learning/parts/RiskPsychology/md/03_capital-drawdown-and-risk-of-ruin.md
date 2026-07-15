# Capital, Drawdown & Risk of Ruin

## Why this matters — the pro vs retail gap this closes

Retail traders think in returns ("I want to double my money"). Pros think in *drawdowns and survival probabilities* — because the maths of losing is brutally asymmetric and the maths of ruin is unforgiving. A trader who understands that a −50% loss demands a +100% gain to recover, and that risking 5% per trade on a 50%-win system has a meaningful chance of eventually wiping out, will never take the bets that kill most accounts. This chapter is the "staying alive" arithmetic that turns the previous two chapters into a lifetime, not a season.

## The essentials — the maths of staying alive

**1. Drawdown recovery is non-linear.**
To recover a loss of *L*, you need a gain of **L / (1−L)**. The deeper the hole, the disproportionately harder the climb:

| Drawdown | Gain needed to recover |
|---|---|
| −10% | +11.1% |
| −20% | +25% |
| −33% | +50% |
| **−50%** | **+100%** |
| −75% | +300% |
| −90% | +900% |

This is why capping drawdown matters more than chasing returns. Below roughly −50%, most accounts never come back — not because it's mathematically impossible, but because the psychology and the shrunk capital make +100% unattainable.

**2. Expectancy — is there even an edge?**
**Expectancy (per trade) = (Win% × Avg Win) − (Loss% × Avg Loss)**, best expressed in R. Positive expectancy is the *precondition* for survival; without it, better sizing only slows the bleed. Example: 45% win, avg win +2R, avg loss −1R → (0.45×2) − (0.55×1) = **+0.35R per trade.** Over 200 trades that's +70R.

**3. Risk of ruin (RoR).**
RoR is the probability of losing your whole (or a defined chunk of) capital given your win rate and risk-per-trade. Two levers dominate it: **edge (win rate / payoff)** and **risk per trade.** Cutting risk per trade slashes RoR dramatically; raising it explodes RoR — even with a positive edge. A positive-expectancy system can *still* ruin you if each bet is too large, because a losing streak of N in a row has probability (Loss%)^N and *will* eventually occur.

**4. Compounding vs ruin — same force, opposite signs.**
Small, consistent positive-R trades compound beautifully *if* drawdown never craters the base. One oversized bet that causes a −60% drawdown resets the compounding clock by years. The goal is a smooth curve, not a spiky one.

## Worked example — a risk-of-ruin table

Assume winners and losers are both 1R (payoff 1:1) for clarity, and "ruin" = losing 100% of capital. Approximate RoR falls as you cut risk-per-trade and as win rate rises above 50%:

**Risk of ruin (approx.), 1:1 payoff:**

| Win rate | Risk 1%/trade | Risk 2%/trade | Risk 5%/trade | Risk 10%/trade |
|---|---|---|---|---|
| 50% | ~100% (no edge) | ~100% | ~100% | ~100% |
| 52% | ~2% | ~15% | ~44% | ~66% |
| 55% | ~0% | ~0.02% | ~8% | ~28% |
| 60% | ~0% | ~0% | ~0.3% | ~5% |

Read the table honestly. **At a coin-flip 50% with 1:1 payoff, ruin is certain eventually — the costs (STT, brokerage, GST) guarantee it.** A tiny edge (55%) is safe at 1% risk but genuinely dangerous at 5%. The lesson: *even a real edge does not save you from oversizing.*

**Worked drawdown case, ₹5,00,000 capital, 1% risk:**
Suppose a rough patch: 8 losers in a stretch of 12 trades (edge still positive over the long run, but streaks happen). At 1% risk that's roughly −8% +4×(win) — say net −4% to −6%, i.e. capital dips to ~₹4,70,000. Painful but survivable; recovery needs only ~+6%. Now run the *same streak* at 8% risk per trade: −8% eight times compounds toward **−50%+**, capital ~₹2,50,000, needing +100% to recover. Identical trades, identical edge — sizing decides whether it's a dip or a disaster.

**Payoff helps too:** raise avg win to +2R (RR 2:1) and even a 40% win rate carries positive expectancy and low RoR at 1% risk — which is why pros obsess over reward:risk and keep bets small simultaneously.

## How pros do it / common mistakes

**Pros:**
- Set a **max system drawdown** they will tolerate (often −15% to −20%) and *cut size* or stop when approaching it.
- Keep risk-per-trade low precisely *because* they respect RoR maths — they know streaks are guaranteed.
- Verify positive expectancy on 100+ trades before scaling, and re-check it quarterly.
- De-risk after a drawdown (trade smaller until the curve recovers), the opposite of the retail instinct.

**Retail errors & red flags:**
- **"I only need 60% wins to get rich"** — ignoring that 5–10% risk-per-trade ruins even a 60% system in a bad streak.
- **Increasing size during a drawdown** to recover fast — mathematically the fastest path to zero.
- **No expectancy tracking** — trading a negative-edge system and blaming "bad luck."
- Underestimating losing streaks: at 55% win, a run of 6 losers has ~0.9% chance per window and *will* show up over a year.
- Treating a −40% account as "almost back" — it needs +67% just to break even.

## Checklist / drill

**Survival checklist:**
- [ ] Is my expectancy positive over ≥100 real trades (in R)?
- [ ] Is risk-per-trade ≤1% (so RoR is negligible for my win rate)?
- [ ] What is my max-drawdown line, and what do I do when I hit it (cut size / stop)?
- [ ] After a losing streak, am I trading *smaller*, not bigger?

**Drill:** Build the table yourself. In a spreadsheet, simulate 500 trades at your real win rate and payoff, at 1%, 3%, and 6% risk. Run it 100 times. Count how often each setting draws down beyond −25% or hits ruin. Seeing your own numbers ruin at 6% — while barely dipping at 1% — is the most convincing risk lesson you'll ever get. *The maths of staying alive always beats the maths of getting rich fast.*
