# Cognitive Biases Catalog I

Technical analysis gives you charts, levels and probabilities. Then a human being — anxious, greedy, ego-invested, sleep-deprived — has to press the button. The gap between a good system and a good trader's results is almost entirely psychological, and psychology on the trading desk is mostly a story about **cognitive biases**: the systematic, predictable ways the human mind mis-processes uncertainty, money and self-image.

This is the first of two catalog chapters. Here we cover the eight biases that do the most damage to Indian retail and semi-pro traders: loss aversion, the disposition effect, confirmation bias, recency bias, anchoring, overconfidence, the sunk-cost fallacy and the gambler's fallacy. For each, you get the mechanism (why the brain does it), how it shows up specifically on an NSE/MCX trading screen, a worked India example with real-feeling numbers, and a concrete counter-protocol you can build into your process. The honest framing throughout: you cannot delete these biases. They are hardware. You can only build **process guardrails** that fire before the biased brain gets to act.

## Why biases matter more than your indicators

Consider two traders with the identical strategy — buy Bank Nifty on a retest of a broken resistance, stop below the retest low, target 2R. Backtested, the edge is real: 44% win rate, average winner 2R, average loser 1R, expectancy positive. Trader A follows it mechanically for 100 trades. Trader B "uses judgment." Trader B cuts winners early when they feel scary (fear), holds losers past the stop hoping for a bounce (loss aversion), doubles the size after three wins (overconfidence) and skips the setup after two losses (recency bias). Same signals, same market — Trader B turns a positive-expectancy system into a losing one. The edge never reaches the P&L because bias intercepts it at the point of execution.

That is the entire thesis of trading psychology: **the market does not take your money, your biases hand it over.** SEBI's own studies of the F&O segment found that roughly 9 out of 10 individual traders lose money. Some of that is costs and structural disadvantage, but a very large share is the biased execution of otherwise-fine ideas.

## Bias 1 — Loss aversion

**The mechanism.** Kahneman and Tversky's foundational finding: the pain of losing ₹10,000 is psychologically about twice as intense as the pleasure of gaining ₹10,000. The brain treats losses as threats to survival, firing the same circuitry as physical danger. This asymmetry is not a character flaw; it is a species-wide default.

**On the NSE screen.** Loss aversion is the root of the single most expensive retail mistake: **moving or removing your stop-loss.** Price approaches your stop, the loss becomes real and imminent, and the threat-response brain screams "avoid this pain." So you widen the stop "just a little," or cancel it entirely and tell yourself you'll "watch it manually." You have now converted a defined ₹5,000 loss into an undefined one. The trades that blow up accounts are almost never the ones stopped out on plan — they are the ones where loss aversion overrode the stop.

**Worked example.** You buy 2 lots of Reliance futures at ₹2,940, stop at ₹2,910 (₹30 risk, ₹15,000 total across 500 shares). Price drops to ₹2,914. The loss is now ₹26,000 on paper and the stop is 4 points away. Loss aversion whispers: "It's held ₹2,910 before, don't sell at the bottom." You cancel the stop. Price grinds to ₹2,875. Now you're down ₹65,000 — more than 4x your planned risk — and you're frozen, hoping for a bounce that would merely reduce the loss. This is the exact sequence that destroys accounts: one act of loss aversion, compounded.

**Counter-protocol.**
- **Bracket orders / OCO.** Enter every trade with the stop attached as a server-side order (Zerodha GTT, cover order, or your broker's bracket order). If the stop lives on the exchange, not in your head, loss aversion has nothing to override.
- **Pre-commit the number, not the price.** Before entry write "max loss on this trade = ₹15,000." When the loss is the number you already accepted, it feels less like a fresh threat.
- **The "would I re-enter?" test.** If you wouldn't put on this exact position fresh at the current price, you have no business holding it. Removing the stop is a disguised new trade you'd never take.

## Bias 2 — The disposition effect

**The mechanism.** A direct child of loss aversion, formalised by Shefrin and Statman: traders **sell winners too early and hold losers too long.** Selling a winner locks in the pleasure of a realised gain (and removes the fear of giving it back); selling a loser locks in the pain of a realised loss (which we avoid). So we do the profitable-feeling thing, which is precisely backwards for trend-following edges.

**On the NSE screen.** You're up ₹8,000 on a Nifty option and you snatch it "before it goes away" — even though your target was ₹20,000 and the trend is intact. Meanwhile a losing position sits open for days because closing it means admitting you were wrong. The result: your average winner shrinks and your average loser grows, quietly inverting your risk-reward until the math no longer works.

**Worked example.** Two positions on the same morning. Long HDFC Bank, up ₹12,000, trend strong, no resistance overhead — you sell "to be safe." Long a lagging PSU bank, down ₹9,000, below its stop — you hold "because it's cheap now." Six sessions later HDFC Bank added another ₹18,000 you didn't capture, and the PSU name is down ₹22,000. The disposition effect made you exit the position you should have held and hold the one you should have exited. Over a hundred trades this single inversion is often the whole difference between profit and loss.

**Counter-protocol.**
- **Rules-based exits, decided pre-trade.** Define the target and the stop before entry, then let them run. The winner exits at the target or a trailing structure, not at the first flush of anxiety.
- **Trail, don't grab.** Instead of a fixed target, trail behind swing lows or a moving average so trends can extend. This directly attacks the "sell winners early" half.
- **Loser audit.** Once a week, list every open losing position and ask of each: "Is my original thesis still valid, and is this above its stop?" If not, close it today. Naming the loss out loud defuses the avoidance.

## Bias 3 — Confirmation bias

**The mechanism.** Once we form a view, the mind hunts for evidence that supports it and discounts evidence that contradicts it. We're not searching for truth; we're defending a position we've already emotionally bought into.

**On the NSE screen.** You're long Nifty and bullish. You scroll X (Twitter) and read only the bullish analysts, mute the bears, and interpret every green candle as confirmation while dismissing the lower high as "just consolidation." You add indicators until one of them agrees with you ("the RSI is turning up!") and ignore the three that don't. Confirmation bias turns your chart into a mirror that shows you what you want.

**Worked example.** You bought Nifty at 24,600 expecting a breakout to 25,000. Price stalls at 24,720 and prints a lower high, breadth turns negative (declines beating advances 2:1), India VIX ticks up, FIIs are net sellers in cash. Every one of these is a warning. But because you're long, you tell yourself: "VIX rising means a squeeze is coming," "FIIs always sell before a rally," "breadth will catch up." You've explained away all the disconfirming evidence. Price rolls over to 24,400 and your ₹15,000 planned risk becomes a ₹40,000 loss because you kept rationalising.

**Counter-protocol.**
- **Write the invalidation first.** Before entry, write the single sentence: "This trade is wrong if ______." (e.g., "if Nifty closes below 24,550 or breadth stays negative into 11am"). Now disconfirming evidence has a pre-agreed meaning.
- **Steelman the other side.** Force yourself to write the best two-line bear case for your long. If you can't articulate it, you don't understand the trade.
- **Follow one credible bear.** Deliberately keep one intelligent opposite-view voice in your feed to break the echo chamber.

## Bias 4 — Recency bias

**The mechanism.** The brain over-weights the most recent events and assumes they'll continue. Three wins and you feel invincible; three losses and the strategy feels "broken" — even though a 44%-win-rate edge produces four-loss streaks routinely.

**On the NSE screen.** After a great week you double your size (the market feels easy), right before a chop phase punishes size. After a losing week you abandon a good system at exactly the moment it was about to revert to its long-run expectancy. Recency bias makes you largest right before drawdowns and smallest right before recoveries — the worst possible sizing rhythm.

**Worked example.** Your Bank Nifty scalp system wins Monday–Wednesday, +₹60,000. Feeling hot (recency), you go from 2 lots to 6 lots Thursday. Thursday is an RBI-policy chop day, three false breakouts, and at 6 lots your normal ₹8,000 loss is a ₹24,000 loss, twice. You give back ₹48,000 — most of the week — because a three-day sample convinced you the future would look like the recent past.

**Counter-protocol.**
- **Fixed fractional sizing.** Risk a constant percentage (say 1% of capital) per trade regardless of recent results. This mechanically prevents recency-driven size spikes.
- **Judge the process on 30–50 trades, not 3.** Keep a rolling expectancy metric. A three-trade streak is noise; only a large sample can tell you if the edge changed.
- **Separate "how I feel" from "what I do."** Feeling hot or cold is allowed; changing size because of it is not.

## Bias 5 — Anchoring

**The mechanism.** We fixate on an irrelevant reference number — usually our entry price or a recent high — and judge everything relative to it, even when the market has moved on.

**On the NSE screen.** "I bought at ₹1,200, I'll sell when it gets back to ₹1,200." The market has no memory of your entry; ₹1,200 is meaningful only to you. Anchoring keeps you in dead positions waiting for a break-even that may never come, and makes you reject good entries because the price is "higher than where I could have bought last week."

**Worked example.** You bought Tata Motors at ₹1,050. It falls to ₹960 on a sector downgrade. The correct read: thesis broken, exit. But you're anchored to ₹1,050 — "I'll just wait for break-even." You hold for three months of dead money while the stock ranges ₹930–₹980, and the capital that could have been in a trending name earns nothing. The anchor cost you not a loss but a far larger **opportunity cost.**

**Counter-protocol.**
- **Evaluate from the current price forward.** The only question is: "Given the price and structure right now, is this a position I want?" Your entry is a sunk fact, irrelevant to that answer.
- **Anchor to structure, not to your fill.** Use meaningful levels — prior swing, VWAP, value-area edges — as references instead of your personal entry.
- **Mark positions to market daily.** Judge each holding on today's chart as if you inherited it flat this morning.

## Bias 6 — Overconfidence

**The mechanism.** Most people rate themselves above average — impossible by definition. Traders systematically overestimate the accuracy of their forecasts and the size of their edge. Barber and Odean's classic study showed overconfident traders **trade more and earn less**; the effect is strongest in the demographic that dominates Indian F&O.

**On the NSE screen.** Overconfidence shows up as oversizing, overtrading, skipping the stop ("I know this one's a winner"), and abandoning the plan to "read the tape." It's especially dangerous after a hot streak, which recency bias inflates into a sense of mastery.

**Worked example.** After a strong month you conclude you've "figured out Bank Nifty expiry." You take an unplanned naked-option-selling position at 2x normal size into Thursday expiry without a hedge, confident it'll expire worthless. A midday news spike moves the underlying 1.5%, the option you sold for ₹40 trades at ₹180, and because you were oversized and unhedged, a single trade erases six weeks of gains. Overconfidence didn't make the trade wrong — it made the *size* catastrophic.

**Counter-protocol.**
- **Cap size mechanically.** A hard rule: no single trade risks more than X% of capital, no exceptions, regardless of conviction. Conviction is exactly the feeling that lies to you.
- **Track your forecast calibration.** Log your predicted probability for each trade and compare to actual hit rates. Most traders discover they're systematically over-optimistic — the data is humbling and corrective.
- **Trade count limits.** Cap trades per day. Overconfidence expresses itself as frequency; a hard limit throttles it.

## Bias 7 — The sunk-cost fallacy

**The mechanism.** We let money, time or effort already spent (and unrecoverable) justify continued commitment. "I've already lost so much, I can't quit now" — as if past losses create an obligation to risk more.

**On the NSE screen.** Averaging down into a losing position is the textbook case. You bought at ₹500, it's ₹460, so you buy more "to lower the average," committing more capital to a thesis the market is actively rejecting. Each add is justified by the prior loss, not by a fresh, valid signal.

**Worked example.** Long a midcap at ₹800, stop should've been ₹770. At ₹760 you "average down" with a second tranche; at ₹720, a third. Your average is now ₹760 and your position is 3x the original — three times the risk on a broken idea, all to avoid admitting the first tranche was wrong. At ₹680 the position is a disaster that a single planned stop would have kept to a ₹15,000 loss. Averaging down turned it into ₹1.2 lakh. Averaging **down** on a broken thesis is sunk cost wearing a costume.

**Counter-protocol.**
- **Only add to winners, never to losers.** Pyramiding into strength is confirmed by the market; averaging into weakness fights it.
- **Reframe: "Would I open this today?"** Ignore what you've already put in. If a fresh you wouldn't buy here, don't add.
- **Pre-set max position size.** Cap the total capital any single idea can consume, so the "average down" impulse hits a wall.

## Bias 8 — The gambler's fallacy

**The mechanism.** The belief that independent random events "owe" a reversal — "red five times, black is due." Markets are not perfectly independent, but streaks in your P&L do not create an obligation for the next trade to go the other way.

**On the NSE screen.** After four losing trades you convince yourself the fifth "has to" win and you upsize it. Or, after a stock has risen six days straight, you short it purely because it's "gone up too much and must fall" — with no signal, just a sense that a reversal is owed. The market owes you nothing.

**Worked example.** Your system has hit four stops in a row (entirely normal for a 45%-win-rate edge — four losses in a row happens ~9% of the time). Gambler's fallacy says "the next one's due," so you take the fifth trade at triple size to "make it back." The fifth trade is statistically independent — still ~45% — and when it also loses, your tripled size turns a routine losing streak into an account-threatening drawdown. The streak felt meaningful; to the math it was noise.

**Counter-protocol.**
- **Treat each trade as independent.** Size is set by rules, not by the outcome of the previous trade.
- **Know your streak statistics.** With a 45% win rate, streaks of 4–6 losses are expected across a few hundred trades. Seeing them as normal removes the "due for a win" pressure.
- **No revenge sizing.** A hard rule: never increase size to recover a loss. That single rule neutralises both the gambler's fallacy and revenge trading.

## Interview-ready summary

- **Cognitive biases are the reason positive-expectancy systems still lose money** in real hands — the edge is intercepted at execution.
- **Loss aversion** (losses hurt ~2x gains) is the root of stop-moving and account blow-ups; defend with server-side bracket/OCO stops.
- **Disposition effect** = sell winners early, hold losers long — it inverts your risk-reward; fix with pre-set, rules-based exits and trailing stops.
- **Confirmation bias** turns the chart into a mirror; counter by writing the invalidation before entry.
- **Recency bias** makes you biggest before drawdowns; counter with fixed-fractional sizing and 30–50-trade evaluation windows.
- **Anchoring** to your entry price traps you in dead positions; evaluate every holding from the current price forward.
- **Overconfidence** makes size catastrophic after hot streaks; cap size mechanically and track forecast calibration.
- **Sunk-cost fallacy** drives averaging down; only add to winners, never to losers.
- **Gambler's fallacy** drives revenge upsizing after streaks; treat every trade as independent and never size up to recover.

The meta-lesson: you cannot out-discipline your hardware in the heat of the moment. You beat biases with **process guardrails built in advance** — server-side stops, fixed sizing, pre-written invalidations, and hard caps — that fire automatically before the biased brain gets its hands on the mouse. Catalog II extends this to a second set of biases (availability, hindsight, framing, herding, attribution, the endowment effect and more), and the following chapter turns the whole toolkit toward the single most destructive emotional state: tilt.
