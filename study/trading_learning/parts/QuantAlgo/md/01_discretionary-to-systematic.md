# From Discretionary to Systematic Trading

## Why this matters — the pro vs retail gap this closes

You already know candlesticks, Greeks, and 200 option structures. That knowledge is necessary but not sufficient. The gap that actually separates a profitable pro from the 90% of retail F&O traders who lose money (SEBI's own study covering FY22–24 pegged net losers at roughly 91–93% of individual F&O traders, average loss around Rs 1.1–1.2 lakh) is not *more* setups. It is **repeatability**. A retail trader who "reads the chart" makes a different decision on the same Bank Nifty setup depending on whether he is up or down for the day, whether he slept well, and whether the last trade won. A systematic trader takes the same input and produces the same output every time. That consistency is what lets you measure an edge, size it, and compound it.

This chapter reframes everything you already know into a process you can test, trust, and scale. It does not throw away discretion — it disciplines it.

## The essentials — edge, randomness, and the three modes

**Edge vs randomness.** An "edge" is a positive statistical expectancy after all costs: over many trades, `(Win% × Avg Win) − (Loss% × Avg Loss) − Costs > 0`. Any single trade tells you nothing — a coin can land heads five times. You need a *sample*. As a rough rule, you cannot distinguish a real edge from noise on fewer than ~100 independent trades, and ideally 200–300. This is why one great week means nothing and why screenshots of single trades are the marketing tool of people who lose over the year.

**The three modes of trading:**

| Mode | Decision source | Repeatability | India-specific reality (2026) |
|---|---|---|---|
| Discretionary | Human judgement per trade | Low | Legal, flexible, but unmeasurable and emotion-prone |
| Systematic | Fixed written rules, executed by hand or semi-auto | High | You decide; rules are backtestable |
| Algo (automated) | Code places orders | Highest | Under **SEBI Retail Algo Framework (mandatory 01-Apr-2026)**: every algo order needs an **exchange Algo-ID**, **open APIs are banned**, retail algos run **only through a registered broker's authenticated API**, and orders above **10/sec** need exchange registration. Third-party strategy vendors must tie up with a registered broker. *Verify current text on NSE/SEBI — rules change.* |

The key insight: **systematic and algo are the same logic; only the executor differs.** Build the system first as written rules a human can follow, prove the edge, and only then consider automating it inside the broker-API rules above. Automating an unproven system just loses money faster.

**Why rules beat gut over time.** Gut feel is pattern recognition trained on a biased, tiny, emotionally-weighted sample. It is genuinely good at some things (reading order-flow context, sensing an event day) and terrible at others (position sizing, cutting losers, avoiding revenge trades). Rules are unemotional, auditable, and improvable. When a rule loses, you can inspect *why*; when your gut loses, you just feel bad.

## Worked example — same setup, two traders

Setup: Bank Nifty (lot size 35 as of 2026 — *verify with NSE, lot sizes revise*) opens and forms a 15-minute opening range. A common rule: **buy the future on a breakout above the first 15-min high, stop at the range low, target 2× risk.**

Say Bank Nifty's first 15-min range on a given day is 52,000–52,180 (180 points wide). Breakout entry 52,180, stop 52,000 (risk 180 points), target 52,540 (+360).

- **Per-point value:** Rs 35/point (1 lot). Risk = 180 × 35 = **Rs 6,300 per lot**. Reward if target hit = 360 × 35 = **Rs 12,600**.
- **Costs (round trip, 2026, one lot future ~Rs 18.2 lakh notional):** brokerage ~Rs 40 (Rs 20 × 2 legs, flat-fee broker), STT on futures ~0.05% on sell side ≈ Rs 910 on ~Rs 18.2L sell value, exchange txn + SEBI + stamp + 18% GST on (brokerage+txn) stack to roughly Rs 150–250 more. Call it **~Rs 1,200–1,400 all-in per lot round trip.** *STT rates effective 01-Apr-2026 per Budget 2026 — verify on your broker's contract note.*

The **systematic trader** takes *every* qualifying breakout, logs it, and after 150 trades knows his real win rate (say 38%) and payoff (avg win 1.9R, avg loss 1.0R). Expectancy per trade = `0.38 × 1.9 − 0.62 × 1.0 = 0.722 − 0.62 = +0.10R` before costs — thin, and costs of ~Rs 1,300 on a 180-point (Rs 6,300) risk eat ~0.21R. **Net expectancy is negative.** The system fails the honesty test, and he *knows it* — so he widens the target, trades bigger ranges, or drops the strategy.

The **discretionary trader** takes the breakout when he "feels" it, skips it when he's scared, doubles up after a loss, and never logs anything. He cannot compute any of the above. He will discover the negative edge only when his account is gone.

The lesson isn't that breakouts are bad — it's that only the systematic trader could *see the truth* and act on it.

## How pros do it / common mistakes

**How pros do it:**
- **Write the rule before the trade, not after.** If it isn't written, it isn't a system.
- **Trade a sample, then judge.** No conclusions before ~100 trades.
- **Cost-first thinking.** Pros subtract 2026 STT + charges *before* deciding a setup is worth it. Many "edges" are real gross and negative net.
- **One change at a time.** Change a stop OR a filter, never both, so you can attribute results.
- **Keep a trade journal that a stranger could audit** — entry, exit, size, R, reason, screenshot.

**Classic retail errors / red flags:**
- Believing a 5-trade winning streak is skill.
- Optimising rules on a chart you've already seen (this is curve-fitting — Chapter 3).
- Position sizing by "how confident I feel" instead of fixed risk.
- Chasing automation before proving the edge — and worse, using a banned open API or an unregistered third-party bot post 01-Apr-2026, which puts your broker relationship and your capital at legal risk.
- No log. If you can't compute your expectancy, you don't have a system; you have a hobby that costs money.

**Realistic expectations.** A good, simple, honestly-costed retail system in Indian markets might deliver a Sharpe of 0.8–1.3 and 15–25% annual returns with 15–20% drawdowns — *if* you survive the drawdowns without abandoning it. Anyone promising 5% a month consistently is selling you something. The systematic path is slower and more boring than the YouTube fantasy; that boredom is the point.

## Checklist / drill

**Systematic-readiness checklist — before you trade any strategy:**
- [ ] The full rule is written in one paragraph a stranger could execute.
- [ ] Entry, exit, stop, target, and position size are all objective (no "looks strong").
- [ ] I have estimated 2026 all-in costs per round trip for this instrument.
- [ ] I have a blank journal ready to log every trade (win or loss).
- [ ] I've committed to a minimum sample (≥100 trades) before judging.
- [ ] I know the max losing streak I'll tolerate before pausing.

**Drill (this week):** Take your favourite discretionary setup. Force it into written rules. Paper-trade or backtest 30 instances and log each in R-multiples. Compute win%, avg win, avg loss, and expectancy *net of 2026 costs*. You will likely be surprised — and that surprise is your first real step from gambler to trader.
