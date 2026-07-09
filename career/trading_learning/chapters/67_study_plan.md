# Chapter 67: Your 12-Week Zero-to-Professional Study & Practice Plan

You have read a lot of book by now. You know what a call is, why theta eats long options for breakfast, how India VIX moves, and why nine out of ten retail F&O traders lose money. But knowing is not doing. A surgeon does not become competent by reading anatomy; they become competent by holding the scalpel under supervision, hundreds of times, until the hand knows what the brain knows. Options trading is the same. This chapter turns the whole book into a **12-week training program** — a structured, day-by-day, week-by-week path that takes you from beginner to a *disciplined, competent paper trader who is ready to risk small amounts of real money.*

Be clear about the promise. Twelve weeks does **not** make you a master. Mastery takes years and thousands of trades. What these 12 weeks give you is the **foundation and the habits** — the daily rituals, the journal, the rulebook, and the screen-time — that separate the small minority who survive from the majority who blow up in their first volatile month. Think of it as flight school before you fly solo, not the 10,000 hours that make a captain.

## Core concepts

### How the plan is structured

The 12 weeks map directly onto the parts of this book. You learn a block of theory, then immediately *do* something with it on a live (but fake-money) market. Theory without screen-time is forgotten in a week; screen-time without theory is gambling. The plan alternates so each reinforces the other.

- **Weeks 1-2** — Foundations (Parts I-II): what options are, the market mechanics.
- **Weeks 3-4** — Pricing and the Greeks (Parts III-IV).
- **Weeks 5-6** — Volatility (Part V).
- **Weeks 7-9** — Strategies (Part VI): one family per week, paper-traded.
- **Week 10** — Risk, sizing, journaling (Part VII): review your own stats.
- **Week 11** — Events and advanced topics (Part VIII).
- **Week 12** — Build your trading plan, tools, and personal rulebook (Part IX).

### The three daily habits (the non-negotiables)

From Day 1 to forever, you do three small things every market day. They take 20-30 minutes total and are the heartbeat of the whole program.

1. **The chart review.** Open the Nifty and Bank Nifty daily charts. Note the trend, key support/resistance levels, and where price closed. Thirty seconds of "what is the market doing" trains your context.
2. **The chain review.** Open the option chain for the nearest weekly expiry. Read the at-the-money (ATM) premiums, the implied volatility (IV) column, and where open interest (OI) is piling up. The option chain is the cockpit instrument panel — you must read it fluently, the way a pilot reads an altimeter without thinking.
3. **The VIX review.** Note India VIX (the index that measures expected 30-day Nifty volatility). Is it 11 (calm), 15 (normal), or 22+ (fear)? Write the number down. Over weeks you will build an instinct for what is "high" and "low."

Every trade you take — paper or real — gets **journaled the same day.** No exceptions. The journal is covered in Part VII, but the habit starts in Week 1 even if the "trade" is just a hypothetical you wrote down.

### The weekly review routine

Every weekend (pick a fixed time — say Sunday morning), you run a 45-minute review:

- Read back the week's journal entries. What did you get right? What rule did you break?
- Update your running statistics: number of trades, win rate, average win, average loss, largest loss.
- Pick **one** concrete thing to improve next week (e.g., "stop adding to losers," "size every trade at 1R").
- Preview the macro calendar: RBI policy, US Fed, monthly expiry, big earnings, budget — anything that could spike volatility.

The weekly review is where amateurs and professionals diverge. Amateurs chase the next trade; professionals study the last ten.

### Milestones and self-tests

Each phase ends with a **self-test** — a small bar you must clear before moving on. Do not advance just because seven days passed; advance when you can pass the test. If you cannot, repeat the phase. Slow is smooth, smooth is fast.

### When to go LIVE, and with how much

This is the most important rule in the chapter, so it is bold: **Do not risk real money until you have paper-traded a strategy to consistent profitability over a large sample — at least 30-50 trades across different market conditions.** "Consistent" means positive expectancy with controlled losses, not one lucky home run that hides nine wounds.

When you do go live, start *humiliatingly small.* The first live capital exists to teach you about your own emotions, not to make money. Use an amount whose total loss would not hurt — for many Indian beginners that is something like ₹15,000-₹50,000 of genuine risk capital, and you risk only a tiny slice (well under 5%) per trade. Because index option lots have real notional size, this often means trading the smallest possible position (one lot of a defined-risk spread, not naked selling). The goal of live trading in this phase is to feel real money move and discover whether your discipline survives contact with your own greed and fear. It usually does not, the first time. That is the lesson.

## Worked example (₹, Nifty/Bank Nifty)

Let us walk through a single representative day and a single paper trade so the abstract plan becomes concrete. Suppose it is a Tuesday in Week 7 (your first strategy week — vertical spreads).

**Morning chart + chain + VIX review (08:45 IST):**

- Nifty closed yesterday at 24,000, in a mild uptrend, with support around 23,800.
- India VIX is 14 — normal, slightly calm.
- The nearest weekly expiry is Thursday. ATM is the 24,000 strike. You read the chain:
  - 24,000 call premium: ₹150, IV about 13%.
  - 24,100 call premium: ₹95.

**The paper trade (a bull call spread, because your bias is mildly up):**

You decide to *buy the 24,000 call and sell the 24,100 call* — a defined-risk debit spread.

```
Net debit = premium paid - premium received
          = 150 - 95 = ₹55 per unit
Nifty lot size = about 75 (state-of-the-day; lot sizes change)
Cost (max loss) = 55 * 75 = ₹4,125
Max profit  = (spread width - net debit) * lot
            = (100 - 55) * 75 = 45 * 75 = ₹3,375
Breakeven   = lower strike + net debit = 24,000 + 55 = 24,055
```

You write all of this in the journal *before* the position is "open": the thesis ("mild uptrend, VIX calm, expecting drift toward 24,150 by Thursday"), the entry, the max loss (₹4,125), the max profit (₹3,375), and your exit plan ("close if Nifty breaks 23,800, or take profit at 70% of max").

**Thursday outcome:** Nifty expires at 24,120. Both your long 24,000 call (worth 120 intrinsic) and short 24,100 call (worth 20 intrinsic) settle; the spread is worth its full ₹100 width.

```
Settlement value = (24,120 - 24,000) capped at spread = 100 per unit
Profit = (100 - 55) * 75 = ₹3,375 (the max)
```

That evening you journal the result, the emotion ("wanted to close early Wednesday when it dipped — glad I followed the plan"), and tag it as a clean, by-the-book win. **One trade like this, done with full process, is worth more to your education than ten impulsive trades that happen to be profitable.** The process is the asset; the profit is a by-product.

### The full week-by-week roadmap

**Weeks 1-2 — Foundations (Parts I-II).** Read the foundational chapters. **Action:** open a *demo / paper trading account* (most Indian brokers offer one, or use a simulator/spreadsheet). Start the three daily habits immediately. Learn to read an option chain end to end: strikes, premiums, IV, OI, bid-ask spread. *Milestone / self-test:* explain a call and a put, ATM/ITM/OTM, European cash-settlement, and lot/notional size to an imaginary beginner — out loud, no notes. Read one full option chain and correctly identify the ATM strike and the most-traded strikes.

**Weeks 3-4 — Pricing and the Greeks (Parts III-IV).** Learn intrinsic vs. time value, then delta, gamma, theta, vega, rho. **Action:** price options *by hand* for a few cases, then build a simple Black-Scholes or binomial sheet in Excel/Google Sheets and reproduce a real chain's prices approximately. Each day, before reading the broker's IV, *estimate* the ATM premium yourself and check how close you were. *Self-test:* given a spot move of 50 points and a delta of 0.5, state the expected premium change; explain why a long option loses value over a flat weekend (theta); explain why premiums balloon before results (vega).

**Weeks 5-6 — Volatility (Part V).** Implied vs. realized volatility, IV rank/percentile, the volatility smile and skew, term structure. **Action:** track **India VIX and the ATM IV daily**, and compute a rough **IV rank** ("is today's IV high or low versus the last few months?"). Note how IV behaves around events. *Self-test:* look at today's VIX and IV rank and state whether option *buyers* or *sellers* are structurally favored, and why. Identify skew on the live chain (are puts richer than calls?).

**Weeks 7-9 — Strategies (Part VI), one family per week.** This is the heart of the program. **You paper-trade — never live — one strategy family per week, with a full journal entry for every position.**

- **Week 7 — Verticals** (bull call, bear put, bull put, bear call spreads): defined risk, directional. Place 3-5 paper trades.
- **Week 8 — Neutral / volatility** (straddles, strangles, iron condor, iron butterfly): trading the *level* of volatility, not direction. 3-5 paper trades.
- **Week 9 — Income / overlay** (covered call, protective put, collar, calendars): mixing options with a view or a holding. 3-5 paper trades.

For each, before entering, write the thesis, the max loss, the max profit, the breakevens, and the exit rule. *Self-test (end of Week 9):* from memory, draw the payoff diagram and state max-loss/max-profit/breakeven for any strategy named at random.

**Week 10 — Risk management, sizing, journaling (Part VII).** Now you stop adding trades and **review your own paper statistics** from Weeks 7-9. Compute win rate, average win/loss, expectancy, and your worst drawdown. **Action:** define your sizing rule (e.g., risk a fixed 1-2% per trade), your max portfolio heat, and your stop discipline. *Self-test:* state your position size in lots for a trade given your account size and per-trade risk; identify the two worst trades in your journal and the rule that would have prevented them.

**Week 11 — Events and advanced topics (Part VIII).** Earnings, RBI/Fed days, budget, expiry-day dynamics, IV crush, assignment/settlement nuances, taxes (STT on exercised ITM options, the cost drag of frequent trading). **Action:** paper-trade *around* one scheduled event and watch IV crush in real time. *Self-test:* explain what happens to a long straddle's IV the morning after results, and why "being right on direction" can still lose money after an event.

**Week 12 — Build your trading plan and tools (Part IX), and write your rulebook.** Assemble everything into a one-page **personal trading plan**: which strategies you trade, in which volatility regimes, your sizing, your stops, your daily/weekly routine, and your hard "never do this" list (e.g., "never sell naked options," "never average down on a loser," "never trade on expiry afternoon without a plan"). Set up your tools: the journal template, the watchlist, the sheet, the alerts. *Self-test:* hand your one-page rulebook to a friend; they should be able to follow it and know exactly what you would and would not do.

## Common mistakes / risk note

- **Skipping paper trading to "get to the real thing."** The fake-money phase is where you make the expensive mistakes for free. Rushing it means making them with real money instead. This is the single most common — and most costly — error.
- **Treating one lucky win as "consistency."** A large enough sample (30-50+ trades over varied conditions) is the only honest test of an edge. One green week proves nothing.
- **Journaling only the winners,** or only logging the trade and not the *emotion and the rule-break*. The journal exists to catch the mistakes you do not yet know you make.
- **Going live too big.** Position sizing kills more F&O accounts than bad strategy selection. Start absurdly small; the first live capital is tuition.
- **The honest truth, restated:** SEBI studies show roughly nine in ten retail F&O traders lose money, and option *sellers* face large or undefined risk for capped reward. This plan does not change those odds by magic — it tilts them in your favor by forcing process, defined risk, and discipline. If after 12 weeks your paper trading is not consistently profitable, the correct decision is to keep paper trading, not to fund an account. There is no shame and great wisdom in that choice.

## Key takeaways

- Twelve weeks builds the **foundation and habits**, not mastery — mastery takes years and thousands of trades.
- Three **daily habits** (chart + chain + VIX) and one **weekly review** are the engine of progress; do them without exception.
- The weeks map onto the book's parts: foundations → pricing/Greeks → volatility → strategies → risk → events → your plan.
- **Paper-trade one strategy family per week** in Weeks 7-9, journaling every single position with thesis, max loss, max profit, breakevens, and exit.
- Each phase has a **self-test**; advance only when you pass it, not when the calendar says so.
- Go **LIVE only after 30-50+ paper trades show consistent, controlled profitability**, and then start with humiliatingly small, true risk capital.
- The process is the asset; the profit is the by-product.

## Practice problems

1. **(Conceptual)** Your friend is on Day 1 and wants to fund a real account immediately because they "already understand calls and puts." Give three specific reasons, grounded in this plan, to wait — and state the exact bar for going live.
2. **(Routine)** List the three daily habits and explain in one sentence each what skill each habit is training.
3. **(Numeric — sizing)** Your paper account is ₹2,00,000 and your rule is to risk 1.5% per trade. A defined-risk spread has a max loss of ₹4,000 per lot. How many lots can you take? What is your total rupee risk?
4. **(Numeric — spread)** In Week 7 you buy a Bank Nifty 52,000 call at ₹400 and sell the 52,300 call at ₹250 (lot size about 15). Compute net debit per unit, total max loss, max profit, and breakeven.
5. **(Judgment)** After Weeks 7-9 your journal shows 22 paper trades: win rate 64%, but your three biggest losses each exceeded your three biggest wins, and your account is down overall. Are you ready to go live? What does Week 10 tell you to fix?
6. **(Conceptual)** Why does the plan insist you advance on *self-tests* rather than on time elapsed? Give an example of a phase you might need to repeat.

## Solutions

1. Reasons to wait: (a) the demo phase lets you make beginner mistakes for free — going live skips straight to making them with real money; (b) "understanding calls and puts" is foundations (Weeks 1-2 of twelve) — they have not touched Greeks, volatility, sizing, or events; (c) without a journal and a sample of trades, they have no evidence of an edge, only confidence, and ~9 in 10 retail F&O traders lose money. **The exact bar:** at least 30-50 paper trades across varied conditions showing consistent, controlled profitability — only then, and only with humiliatingly small true risk capital.

2. The three daily habits: **chart review** (trains market context — trend and key levels); **chain review** (trains fluent reading of premiums, IV, and OI — your instrument panel); **VIX review** (trains an instinct for whether volatility is cheap or expensive, which favors buyers vs. sellers).

3. Risk budget = 1.5% of ₹2,00,000 = ₹3,000. Max loss per lot = ₹4,000. Lots = 3,000 / 4,000 = 0.75, which rounds **down to 0 lots** — this trade is too large for the rule at this account size. The disciplined answer is **do not take it** (or find a structure with smaller max loss). The lesson: sizing rules sometimes tell you a trade is simply not available to you yet, and that is the rule working correctly.

4. Bank Nifty bull call spread:
```
Net debit = 400 - 250 = ₹150 per unit
Max loss  = 150 * 15 = ₹2,250
Max profit = (spread width - debit) * lot = (300 - 150) * 15 = 150 * 15 = ₹2,250
Breakeven = lower strike + net debit = 52,000 + 150 = 52,150
```
(Here max profit happens to equal max loss because the debit is exactly half the spread width — a roughly 1:1 reward-to-risk trade.)

5. **No — not ready.** A 64% win rate looks attractive but is a trap: the losers are bigger than the winners, so expectancy is negative (the account is down). This is the classic "win often, lose big" pattern. Week 10 tells you to fix it with **risk control and sizing**: cap each loss with a hard stop or defined-risk structure, ensure average win is at least comparable to average loss, and cut the oversized losers. Keep paper trading until expectancy is positive *with* controlled losses — then reassess going live.

6. Time elapsed proves nothing about competence; a **self-test proves you can actually do the skill.** Advancing on the calendar lets gaps compound — e.g., if you cannot estimate a premium change from delta, every later strategy decision rests on sand. Example to repeat: if at the end of Weeks 5-6 you cannot look at today's VIX and IV rank and say whether buyers or sellers are favored, repeat the volatility phase before touching strategies — because strategy selection *depends entirely* on that judgment.
