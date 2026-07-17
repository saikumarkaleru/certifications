# Trade Management by Setup Type

There is a myth in trading education that "risk management" is one universal rulebook you apply to every position identically: risk 1%, use a 2:1 reward-to-risk, trail your stop, done. It sounds disciplined. It is also wrong, and it quietly bleeds money. A breakout does not behave like a mean-reversion bounce. A trend pullback does not behave like an opening-range scalp. Each *setup type* has its own physics — a characteristic way it succeeds, a characteristic way it fails, and therefore a characteristic way it must be entered, sized, stopped, and exited. Managing every trade the same way is like using one wrench for every bolt in the engine. This chapter builds a setup-specific management playbook for the Indian market.

## The principle: management must match the setup's failure mode

Every setup has a **thesis** and an **invalidation.** The thesis is why you expect it to work; the invalidation is the precise price behaviour that proves it wrong. Correct trade management is nothing more than: place the stop where the thesis is invalidated (not one paisa further), size so that invalidation costs exactly your risk unit R, and take profits in the manner that this specific setup's winners tend to deliver.

The reason one-size-fits-all fails is that setups have radically different **win rates and payoff shapes.** A tight range breakout might win only 40% of the time but pay 3R on winners. A pullback-in-uptrend might win 60% but pay 1.5R. A failed-breakout reversal might win 55% and pay 2R. If you manage all three with the same trailing stop, you will strangle the breakout's fat tail and give back the pullback's modest gains. Management style is not cosmetic — it is what converts an *edge* on paper into money in the account.

Across all setups, one number is fixed: **R, your risk unit** — 0.5% to 1% of equity per trade (see the portfolio-heat chapter). What *changes* by setup is where the stop sits, how the position scales, and how it's exited. We'll build the playbook setup by setup, each with its character, entry, stop logic, scaling, exit, and a worked India example.

## Setup 1 — The range breakout (momentum expansion)

**Character:** price has coiled in a tight range or consolidation; volume has dried up; then it expands out of the range on a surge of volume. The thesis is that trapped energy releases into a directional move. Breakouts have a *low-to-medium win rate but a fat right tail* — the winners can run far. The failure mode is the "fakeout": price pokes out, fails to find follow-through, and snaps back into the range, trapping breakout buyers.

**Entry:** on the breakout candle's close beyond the range, ideally with volume ≥1.5–2x the recent average. Chasing an intraday spike before the close invites fakeouts; a close beyond the level is the confirmation the setup's physics demands. Aggressive traders enter on the break; conservative traders wait for a retest of the broken level as new support.

**Stop:** back inside the range, below the breakout candle's low or the range's midpoint. The invalidation is clean: if price re-enters the range, the breakout has failed. Do *not* use a tiny stop just below the breakout level — that's where every stop-hunt fill sits.

**Scaling & management:** because the payoff is a fat tail, you must *let winners run.* This is the setup where you do NOT take profit early. Move the stop to breakeven only after a clear impulse leg confirms (typically after price travels ~1R in your favour and holds). Then trail loosely — under swing lows on the daily, or a moving average like the 20-EMA — giving the trend room. Taking a fixed 2R and leaving is the single most common way traders destroy the edge of a breakout: they clip the winners that were supposed to pay for all the fakeouts.

**Worked example:** Nifty consolidates 24,600–24,900 for eleven sessions in early 2026, volume falling, India VIX at 11. On day twelve it closes at 24,970 on volume 1.8x average, clearing 24,900. Entry 24,970, stop 24,780 (below the range midpoint / breakout candle low) — 190 points risk. You size so 190 points = 1R. First target is *not* a fixed exit; instead, at 25,160 (1R) you move the stop to breakeven, then trail under daily swing lows. The move extends to 25,900 over three weeks before a swing low breaks and you exit at 25,760 — roughly 4.1R. That one runner pays for the previous three fakeouts that each cost ~0.9R. *That* is why you don't cap breakout winners at 2R.

## Setup 2 — The pullback in an uptrend (trend continuation)

**Character:** an established uptrend pulls back to a support zone — a rising moving average (20/50-EMA), a prior breakout level, or a Fibonacci retracement (38.2–61.8%) — and then resumes. The thesis: the trend is intact, and the pullback is a discount entry. This is a *higher win rate, moderate payoff* setup. Failure mode: the pullback becomes a reversal — support breaks and the trend structure (higher highs, higher lows) is violated.

**Entry:** on evidence the pullback is ending *at* support — a bullish reversal candle (hammer, bullish engulfing), a hold of the 50-EMA, or a break of the pullback's minor down-trendline. Buying into a falling knife hoping support holds is not this setup; waiting for the *reaction* off support is.

**Stop:** below the support zone / the swing low of the pullback. Invalidation is a decisive close below the higher-low structure — that breaks the trend definition. Keep it just beyond the noise, not so tight it's taken by a one-tick undercut.

**Scaling & management:** this setup rewards a *partial-profit* approach because the payoff is moderate. Take roughly half off at the prior swing high or ~1.5–2R, move the stop on the remainder to breakeven, and let the balance ride for trend continuation to new highs. The high win rate means booking partials keeps your equity curve smooth; the runner captures the occasional strong continuation.

**Worked example:** ICICI Bank is in a clean uptrend, rising 50-EMA. Price pulls back from Rs 1,290 to the 50-EMA near Rs 1,240 and prints a bullish engulfing candle. Entry Rs 1,246, stop Rs 1,222 (below the pullback swing low) — Rs 24 risk. Target 1 at the prior high Rs 1,290 (~1.8R): sell half. Stop to breakeven on the rest. Price continues to Rs 1,335 where momentum stalls; trail out the remainder near Rs 1,320 (~3R on that half). Blended ~2.4R, with the risk largely removed early — the smooth-equity profile this setup is built for.

## Setup 3 — Mean-reversion / oversold bounce

**Character:** a stock or index becomes stretched far from its mean (e.g., 2+ ATRs below the 20-EMA, RSI < 30, a capitulation candle) and snaps back toward the mean. Thesis: short-term overextension corrects. This is a *high win rate, small-and-fast payoff, high-severity-tail* setup — most bounces work, but the ones that don't (catching a genuine trend-down or a news-driven collapse) can be vicious. Failure mode: no bounce; the down-move accelerates.

**Entry:** on the *first sign of reversal*, not into the fall — a reversal candle after a climax, or a reclaim of a short-term level. The mean-reversion trade is a *counter-trend* trade and must be treated with extra respect.

**Stop:** tight and non-negotiable, below the reversal low. Because you are fighting momentum, the stop must be honoured mechanically — no "averaging down," ever. Averaging a losing mean-reversion trade is the classic account-killer. The invalidation is a new low; if the low breaks, you were catching a knife, and you get out.

**Scaling & management:** take profit *fast* and toward the mean (the 20-EMA or the prior consolidation). Do not turn a bounce trade into a trend trade — the edge is the snap-back, and it decays quickly. Target 1–2R and be done. Trailing is inappropriate here; you are harvesting a spring, not riding a trend.

**Worked example:** Tata Steel gaps down on weak global metal prices to Rs 138, RSI 24, more than 2 ATR below its 20-EMA, and prints a long-tailed hammer on heavy volume. Entry Rs 140.5 on the reclaim of Rs 140, stop Rs 136.5 (below the hammer low) — Rs 4 risk. Target: the 20-EMA / prior support near Rs 148 (~1.9R). Price bounces to Rs 147.5 over two sessions; you exit the full position. You do *not* hold hoping for a trend — the down-trend context means the bounce is a rental, not a purchase.

## Setup 4 — Failed-breakout reversal (the trap)

**Character:** price breaks a level, fails to hold, and reverses back through it — trapping the breakout traders whose stops now become fuel for the reversal. Thesis: trapped traders must exit, powering a move in the opposite direction. Medium win rate, good payoff (often 2–3R) because you enter right where the trapped crowd's stops sit. Failure mode: the "failed breakout" was just a normal retest and the original breakout resumes.

**Entry:** on the reclaim — when price closes back inside the range after a false break beyond it. The signature is a poke above resistance (or below support) that reverses on the same or next candle.

**Stop:** just beyond the false-breakout extreme (the high of the failed upside break, for a short). Invalidation is clean: if price makes a new high beyond the false break, it wasn't a trap. Tight, well-defined stop = attractive R:R.

**Management:** partial at the opposite side of the range, runner for an extension, because trapped-trader unwinds can travel far. Similar to the breakout in that you give the runner room, but with a tighter, better-defined initial risk.

**Worked example:** Bank Nifty pushes to a new high 52,400, clearing the prior 52,300 resistance intraday, but reverses and closes back at 52,180, below the breakout level, on rising volume — a bull trap. Short entry 52,150, stop 52,450 (above the false-break high) — 300 points risk. Target 1 at the range low 51,600 (~1.8R): cover half. Runner trails; the trapped-longs unwind carries to 51,250 before you're stopped out of the runner near 51,500 (~2.2R). Blended ~2R, entered precisely where the trapped crowd was forced to sell.

## The management matrix

| Setup | Win rate | Payoff | Stop location | Profit style | Key rule |
|---|---|---|---|---|---|
| Range breakout | Low–med (~40–45%) | Fat tail (3R+) | Back inside range | Let it run; loose trail | Never cap the winner at 2R |
| Trend pullback | High (~55–65%) | Moderate (1.5–2.5R) | Below higher-low | Partial + breakeven + runner | Book partials for smooth equity |
| Mean-reversion | High (~60–65%) | Small/fast (1–2R) | Below reversal low | Fast fixed target to the mean | Never average down; exit at mean |
| Failed-breakout | Med (~50–55%) | Good (2–3R) | Beyond false-break extreme | Partial + runner | Enter on the reclaim, not the poke |

Read this matrix as a single lesson: **the exit style is dictated by the payoff shape, which is dictated by the setup's physics.** Fat-tail setups (breakout, trap) demand runners; you accept a lower win rate to catch the big move, so you must not amputate it early. Moderate/high-win-rate setups (pullback, mean-reversion) demand disciplined partials and fixed targets; the edge is consistency, and letting these "run" usually means giving winners back.

## Building it into your routine

**Tag every trade with its setup type at entry.** Before you buy, name it: "this is a breakout / pullback / mean-reversion / trap." Write it in your journal. This single act forces you to apply the right management template and — crucially — lets you later measure *which setups actually pay you.* Most traders discover they have one genuinely profitable setup and three that break even or bleed. You cannot find that out if every trade is an undifferentiated "long."

**Pre-commit the management before entry.** Write the stop (in points and in R), the invalidation condition in plain words, the profit style, and the first-partial level *before* you press buy. In the moment, emotion will argue for moving the stop and grabbing profit early on the runners and holding the losers. The pre-commitment is your defence.

**Review by setup, not by trade.** Monthly, group your trades by tag and compute win rate, average R won, average R lost, and expectancy per setup. Expectancy = (win% x avg win in R) − (loss% x avg loss in R). Cut the negative-expectancy setups. Size up the positive ones. This is how a trader goes from "busy" to "profitable."

**Match the setup to the regime.** Breakouts work in trending, expanding-volatility tapes and fail repeatedly in choppy ranges. Mean-reversion works in ranges and gets destroyed in strong trends. Reading the market regime (from breadth, VIX, and index structure) tells you *which template to favour this week* — don't force breakout trades in a chop-fest or fade a runaway trend.

## Pitfalls

- **Managing a breakout like a pullback** — capping the runner at 2R and killing the fat tail that funds the strategy.
- **Managing a mean-reversion like a trend** — holding a bounce hoping it becomes a trend, then giving back the gain and more.
- **Averaging down on a counter-trend trade** — the fastest route to a catastrophic loss; the invalidation exists precisely to stop this.
- **Moving the stop to "give it room"** — the stop marks invalidation; widening it means you no longer believe your own thesis but won't admit it.
- **Not tagging setups** — you cannot improve what you don't measure; untagged trades hide which edge is real.
- **Ignoring regime** — the right template in the wrong regime is a losing template.

## Interview-ready summary

Trade management is not one universal rulebook — it must match each setup's failure mode and payoff shape. The stop always sits exactly at the setup's invalidation, sized so that invalidation costs one risk unit R; what varies is the *exit style*, dictated by the payoff. Fat-tail setups — range breakouts and failed-breakout traps — win less often but pay big, so you must let winners run with loose trailing stops and never cap them early. High-win-rate setups — trend pullbacks and oversold mean-reversion bounces — pay moderately, so you book partials, use fixed targets toward the mean, and never average down on the counter-trend ones. Tag every trade by setup type, pre-commit the management before entry, and review expectancy per setup so you can cut the losers and press the winners. Matching management style to setup physics is what turns a paper edge into a real one.
