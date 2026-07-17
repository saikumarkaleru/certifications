# Performance-Review Systems

Most traders review their performance the way most people go to the gym in January — sporadically, emotionally, and without measurement. They glance at their P&L, feel good or bad, and trade again. This is not review; it is mood. A real performance-review system is the feedback loop that turns raw screen-time into compounding skill. Without it, ten years of trading is not ten years of experience — it is one year of experience repeated ten times, with the same leaks bleeding you out the whole way. This chapter builds that loop concretely: what to log, how to score it, and the cadence that turns data into behavioural change.

## The principle: you cannot improve what you do not measure — and you cannot measure P&L

The single most important idea in trading performance review is this: **P&L is a bad primary metric because it is dominated by variance in the short run.** A trader can execute flawlessly for a week and lose money (their edge's win-rate simply varied down), or execute recklessly and win (they got lucky). If you review by P&L, you will *reward your worst behaviour whenever it happens to profit* and *punish your best behaviour whenever it happens to lose.* This is exactly backwards, and it trains you into ruin.

The professional inverts this. You separate two things that amateurs fuse:

- **Process** — did I follow my rules? Did I take the right setups, size correctly, honour my stop, exit per plan? This is *entirely in your control* and is the true object of review.
- **Outcome** — did the trade make money? This is *only partly in your control* over any single trade; over hundreds of trades, if your process is sound, outcome follows.

The performance-review system's job is to relentlessly measure process, use outcome only in aggregate (over large samples where variance averages out), and diagnose the specific, recurring leaks that separate your actual results from your edge's potential. The Japanese manufacturing concept of *kaizen* — continuous, small, measured improvement — is the right mental model, not the fantasy of one big breakthrough.

## The method, layer 1: the trade journal (the raw data)

Everything starts with logging every trade, the moment it closes, with fields chosen so you can later slice and diagnose. A minimum viable journal — buildable in Excel, Google Sheets, or a tool like TradersSync / a TradingView-linked log — captures:

| Field | Why it matters |
|---|---|
| Date / time / instrument | Slice performance by day, session, symbol |
| Setup tier (A+/A/B/C) | Test whether your grading actually predicts results |
| Direction (long/short) | Detect directional bias leaks |
| Entry / stop / target | Reconstruct the plan |
| Planned R | The risk you intended |
| Exit price / actual R | The result in risk-units, not rupees |
| Rule grade (A/B/C) | Did you follow your process? — the key column |
| Emotion tag | Calm / FOMO / revenge / bored / fearful |
| Screenshot | The chart at entry — for later honest review |
| One-line note | "Moved stop, got lucky" / "textbook, stopped clean" |

The two most under-used and most valuable columns are the **rule grade** and the **emotion tag**, because they capture *process and psychology*, the things P&L hides. The **actual R** column matters enormously too: measuring results in R (risk-units) rather than rupees strips out position-size noise and lets you compare a Nifty trade to a small-cap trade on equal footing.

## The method, layer 2: the metrics that actually matter

From the journal, at the end of each week and month, compute a dashboard. The metrics below, taken together, tell you *what kind of trader you actually are* — often very different from what you believe you are.

| Metric | Formula | What it diagnoses |
|---|---|---|
| Win rate | Wins / total trades | Frequency of being right (alone, meaningless) |
| Average win (R) | Mean R of winners | Do you let winners run? |
| Average loss (R) | Mean R of losers | Do you honour stops or let losers bleed? |
| Payoff ratio | Avg win R / Avg loss R | The core geometry of your edge |
| Expectancy (R) | (Win% × AvgWin) − (Loss% × AvgLoss) | **Expected R per trade — the master number** |
| Profit factor | Gross profit / gross loss | >1.5 is solid, >2 is strong |
| Max drawdown | Peak-to-trough of equity curve | Survival risk |
| Rule-adherence % | A-graded trades / total | The process score |

**Expectancy is the master number.** It tells you, in risk-units, what you make per trade on average. An expectancy of +0.3R means every trade, win or lose, is worth 0.3R to you on average — so 200 trades a year is +60R, and your annual return is 60 × your R%. This single number, tracked over time, tells you whether your edge is real and whether it's improving. A trader obsessing over win rate is missing the point: a 40% win-rate system with a 3:1 payoff has an expectancy of (0.4×3) − (0.6×1) = +0.6R, crushing a 60% win-rate system with a 0.8:1 payoff at (0.6×0.8) − (0.4×1) = +0.08R.

The comparison you must run every month is **expectancy by setup tier.** If your A+ trades don't have meaningfully higher expectancy than your B trades, your grading criteria are broken — you are not actually identifying your best setups, you are just labelling them. This is the feedback loop that keeps your conviction-sizing (previous chapter) honest.

## The method, layer 3: the review cadence

Data without a review rhythm is a spreadsheet nobody reads. The cadence that works, escalating in depth:

**Daily (5 minutes, end of session).** Log the day's trades while memory is fresh. Grade each trade A/B/C on rule-adherence. Tag emotion. Write one honest sentence per trade. Do *not* judge the day by money — judge it by rule-adherence percentage. A red-P&L day with 100% A-grade execution is a *good* day. Ask one question: "What did I do well, what did I do poorly, and what's one thing to focus on tomorrow?"

**Weekly (30 minutes, Saturday morning).** Compute the metrics dashboard for the week. Look at the equity curve. Identify your single worst trade and your single best-executed trade (regardless of P&L). Re-read the screenshots of your rule-break (C) trades — *this is where the learning is.* Ask: "What is the one recurring pattern in my mistakes this week?" Pick one concrete, measurable behavioural target for next week (e.g., "no trades in the first 15 minutes" or "no averaging down").

**Monthly (90 minutes).** The full audit. Compute expectancy by setup tier, by day of week, by session (morning vs afternoon), by instrument, and by emotion tag. This slicing reveals your *structural* leaks — the ones invisible at the single-trade level. Review whether last month's behavioural target actually moved the numbers. Set the next month's focus.

**Quarterly (half a day).** Zoom out. Is the equity curve trending up? Is expectancy stable, rising, or decaying? Has the market regime changed (e.g., low-VIX grind vs high-VIX whipsaw) and does your edge still fit it? Decide whether to add size, cut a losing setup entirely, or take a break to retrain.

## Worked example: what Arjun's monthly slice revealed

Arjun trades Nifty and Bank Nifty intraday, ₹8,00,000 account, 1R = ₹8,000. He *believed* he was a solid, disciplined trend trader. His month showed a small net profit — +4R, roughly +₹32,000, or +4%. By P&L alone, a fine month. He'd have moved on. Instead he ran the monthly slices.

**By session:** Morning (9:15–11:30) expectancy was +0.45R across 22 trades. Afternoon (1:00–3:15) expectancy was **−0.30R** across 18 trades. His mornings were carrying the account and his afternoons were quietly bleeding it. He'd never have seen this in the blended P&L.

**By emotion tag:** Trades tagged "calm" had +0.5R expectancy. Trades tagged "bored" or "FOMO" — almost all in those dead afternoon hours — averaged −0.4R. The afternoon losses weren't a strategy problem; they were a *boredom-trading* problem.

**By setup tier:** His A+ trades ran +0.7R, his B trades +0.1R — good, his grading was working. But he noticed his C-grade (should-not-exist) trades numbered *nine* for the month, all clustered in afternoons, all boredom-driven, collectively −5R. Those nine trades had turned a +9R month into a +4R month.

**The intervention:** Arjun made one rule — "No new positions after 12:30 PM unless it's a clearly-marked A+ setup." He didn't change his entries, his indicators, or his strategy. He deleted a *behaviour*. The next month, with the same edge and same market, he did +8.5R. The performance-review system didn't find him a new strategy — it found the leak that was silently draining the good strategy he already had. **This is what review systems actually do:** they make the invisible visible, and most of what's draining you is invisible until you slice the data.

## Building it into your routine (and the traps)

- **Log immediately, not at week's end.** Memory rewrites itself — you will "remember" that you followed your rules when you didn't. Log at the moment of exit, with the screenshot, while it's true.
- **Grade brutally honestly.** The rule-grade column only works if a rule-break gets a C even when it made money. The instant you start giving profitable rule-breaks an A, the system is dead — you've reverted to P&L worship.
- **Review losers *and* winners.** Amateurs only review losses. But a winning trade where you moved your stop, got bailed out by luck, and profited is a *time bomb* — it's a C-grade process that happened to pay, and it will teach you a habit that eventually costs you dearly. Flag lucky wins as aggressively as unlucky losses.
- **Change one thing at a time.** If you alter five behaviours at once, you can't tell which one helped. Pick a single measurable target per week; keep the rest constant. This is basic experimental discipline and most traders skip it.
- **Beware small samples.** A single week of 15 trades tells you almost nothing statistically — variance dominates. Draw conclusions about your edge from 100+ trades, not from a bad Tuesday. Use the daily/weekly reviews for *behaviour* and the monthly/quarterly for *edge*.
- **Keep the equity curve visible.** A chart of your cumulative R over time, updated weekly, is the most honest mirror you own. A choppy, sideways curve says your edge is marginal or your execution is leaking; a steady up-and-to-the-right curve — even a slow one — says the machine works. Trust the curve over your mood.

## Interview-ready summary

- **P&L is a bad primary metric** because short-run variance rewards bad behaviour that profits and punishes good behaviour that loses. Review *process* (rule-adherence, in your control) and use *outcome* only in aggregate over large samples.
- **Layer 1 — the journal:** log every trade at exit with setup tier, actual R, a rule-grade (A/B/C), an emotion tag, and a screenshot. The rule-grade and emotion columns are the most valuable and most skipped.
- **Layer 2 — metrics:** expectancy = (Win% × AvgWinR) − (Loss% × AvgLossR) is the master number. A 40% win-rate/3:1 system (+0.6R) beats a 60%/0.8:1 system (+0.08R). Win rate alone is meaningless.
- **Test grading with expectancy-by-tier:** if A+ trades don't out-earn B trades, your grading is broken — this keeps conviction-sizing honest.
- **Layer 3 — cadence:** daily rule-grading (5 min), weekly dashboard + one behavioural target (30 min), monthly slice-and-audit by session/emotion/tier (90 min), quarterly edge-and-regime review.
- **Slicing reveals invisible leaks:** most of what drains a profitable edge — boredom trades, dead-session losses, lucky rule-breaks — is invisible in blended P&L and only appears when you slice the data. Change one behaviour at a time and trust the equity curve over your mood.
