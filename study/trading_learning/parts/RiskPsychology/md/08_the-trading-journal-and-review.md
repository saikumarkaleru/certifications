# The Trading Journal & Weekly Review System

## Why this matters — the pro vs retail gap this closes

Ask a losing retail trader "what's your expectancy per trade, your win rate by setup, and your worst mistake tag last month?" and you'll get a blank look. Ask a professional and they'll pull up a sheet. That is the whole gap. Without a journal you are not trading a strategy — you are *guessing* that you have one, and your memory is lying to you. Human memory over-weights recent and emotional trades: you remember the one big winner and the one gut-wrenching loss, not the boring middle that actually determines your edge.

A journal converts trading from a feelings-based activity into a measurable, improvable process. It is the single highest-ROI habit an aspiring pro can build, and it costs nothing but discipline. This chapter covers exactly what to log, how to compute your *real* edge (expectancy) from it, the weekly review ritual, the KPIs that matter, and how to iterate your playbook. (References as of 13-Jul-2026 — verify broker/SEBI/tax specifics, rules change.)

## The essentials — what to log and what to compute

**The unit of measurement is R.** R = your initial risk on the trade (entry to stop, in rupees). A trade that risked Rs 3,000 and made Rs 6,000 is **+2R**; one that lost the planned stop is **−1R**. Logging in R (not rupees) makes trades comparable across different sizes and lets you measure the *strategy* independent of position size.

**What every journal entry must contain:**

| Field | Why it matters |
|---|---|
| Date/time, instrument (e.g., Bank Nifty CE, Reliance) | Context, session, expiry effects |
| Setup name (your playbook tag) | So you can measure each setup separately |
| Direction, entry, stop, target | The plan you committed to |
| Size (lots/qty) and Rs risk (= 1R) | The unit |
| Exit price, exit reason | Did you follow the plan? |
| P&L in Rs **and in R** | Comparable performance |
| **Screenshot** of the chart at entry | Objective record vs memory |
| **Mistake tag** | The improvement engine (see below) |
| **Emotion** at entry (calm/FOMO/revenge/fear) | Links Chapter 6 loops to money |
| Charges paid (brokerage+STT+txn+GST+stamp) | Your real net edge |

**Mistake tags** are a fixed short list you pick from, e.g.: *chased entry, moved stop, oversized, no stop, exited winner early, revenge trade, ignored plan, valid loss (no error).* "Valid loss" is crucial — a loss that followed the rules is **not** a mistake. Tagging separates bad luck from bad behaviour.

**Expectancy — your real edge, from your own data:**

> Expectancy (in R) = (Win% x Avg Win in R) − (Loss% x Avg Loss in R)

Positive expectancy = you make money over a large sample; negative = you lose no matter how you feel about it. Example: Win% 45%, avg win +2.2R, loss% 55%, avg loss −1R → (0.45 x 2.2) − (0.55 x 1) = 0.99 − 0.55 = **+0.44R per trade.** At Rs 3,000 risk that's **~Rs 1,320 expected per trade before charges** — *and* you must subtract average charges to get true net expectancy. Many retail "systems" are positive gross and negative *net* once STT/GST/brokerage are counted; the journal is the only place you'll catch that.

## Worked example — reading one week's journal

30 trades, 1R = Rs 3,000. Raw results: 13 wins, 17 losses. Wins totalled +34R, losses totalled −20R (many losers cut before full −1R; some winners ran to +4R).

- Win% = 13/30 = 43%. Avg win = 34/13 = **+2.6R.** Avg loss = 20/17 = **−1.18R** (over 1R — stops slipped or were moved: a red flag).
- Expectancy = (0.43 x 2.6) − (0.57 x 1.18) = 1.12 − 0.67 = **+0.45R/trade.** Gross ≈ +0.45 x Rs 3,000 x 30 = **+Rs 40,500** for the week.
- **Now the mistake tags:** 6 of the 17 losses tagged "moved stop" or "revenge" — those 6 averaged −1.9R vs −0.7R for the disciplined losses. Had they been cut at −1R like the plan, losses would have totalled ~−15.5R instead of −20R — **+4.5R (~Rs 13,500) left on the table by 6 undisciplined exits alone.**
- **By setup:** the "opening-range breakout" tag was +9R across 8 trades; the "expiry-day OTM lottery" tag was −6R across 5 trades. The data says: do more of the first, *delete the second.*

One week's honest log just told this trader their true edge, quantified their discipline leak in rupees, and identified a setup to cut — none of which "how did the week feel?" could reveal.

## How pros do it / common mistakes

- **Pros journal every trade, same day, especially the losers.** The trades you least want to log are the ones with the most to teach.
- **They review weekly, not obsessively daily.** Daily P&L is too noisy; a week (20-30 trades) is a fair sample to read signal from.
- **They let data, not feelings, change the playbook.** A setup is cut only after enough trades show negative expectancy — not after one bad day.
- **They track a small KPI set** (below) and watch trends, not single points.
- **Classic mistakes:** only logging winners (or only losers); journaling in vague prose ("choppy day, felt off") instead of numbers and tags; no screenshot so you argue with your memory later; measuring in rupees so different sizes blur the strategy; never computing expectancy (so you can't tell a real edge from a hot streak); ignoring charges so "profitable" is actually net-negative; changing strategy every week on tiny samples.
- **Red flags:** a growing gap between "gross edge" and "net after charges"; avg loss creeping past 1R (stops not honoured); one mistake tag dominating; you can't answer "which of my setups makes money?"

## Checklist / drill — the review system

**Log per trade (same day, non-negotiable):** setup, direction, entry/stop/target, size, 1R in Rs, exit + reason, P&L in Rs and R, screenshot, mistake tag, emotion, charges.

**Weekly review (fixed 45-min slot):**
1. Compute **Win%, Avg win (R), Avg loss (R), Expectancy (R), net after charges.**
2. **Break expectancy down by setup** — keep/scale winners, cut losers.
3. **Tally mistake tags** — what's the #1 leak in R this week? Write the one rule to fix it.
4. Check **avg loss vs 1R** (stop discipline) and **process-adherence %** (from Ch. 7).
5. **Emotion split:** P&L of calm vs FOMO/revenge trades — confirm the loops cost you.
6. Update the **playbook:** one concrete change, then hold it for a meaningful sample.

**KPIs to track over time (a simple sheet or Excel; export fills from Kite):** Expectancy (R), Win%, Avg win/Avg loss ratio, Max drawdown, Process-adherence %, Net-after-charges edge, Best/worst setup.

**Drill:** log your next 20 trades in full, then compute expectancy and expectancy-by-setup. You will end up with two lists — setups that make money and setups that don't — in your own rupees. Trade more of the first list, delete the second. That single evidence-based edit, repeated monthly, *is* how a retail trader becomes a professional.
