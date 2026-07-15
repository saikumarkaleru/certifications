# Risk Management: The #1 Skill

## Why this matters — the pro vs retail gap this closes

You already know Greeks, 200 option structures, candlesticks and Wyckoff. None of it matters if a single trade can take out a quarter of your account. The gap between a professional and a retail trader is almost never analysis — it is *bet sizing under uncertainty*. SEBI's own study (Jan 2023, repeated in 2024–25) found roughly **9 out of 10 individual F&O traders lose money**, with average net losses of ₹1–1.5 lakh over the period studied. The losers are not stupid; they are *over-sized*. They risk 10–20% of capital per trade, hit a run of five losers (a statistical certainty), and blow up.

The pro flips the priority order: **survival first, profit second.** You cannot compound an account that hits zero. This chapter is the operating system that every later chapter (sizing, drawdown, stops) plugs into.

## The essentials — precise India-specific mechanics

**1. Risk per trade: the 0.5–1% rule.**
Never risk more than **0.5% to 1% of trading capital on one trade**. "Risk" = (entry − stop) × quantity, i.e. the rupees you lose if the stop hits — *not* the position value or the margin blocked. On ₹5,00,000 capital, 1% = ₹5,000 max loss per trade. Beginners and small accounts should sit at 0.5%.

**2. Think in R-multiples.**
Define **1R = the rupees you risk on a trade.** Every outcome is then measured in R, independent of size:
- Stop hit → −1R
- Target at 2× the risk distance → +2R
- Scratch at breakeven → 0R

An edge is defined by **average R per trade (expectancy)**, not by win rate. A 40%-win system that makes +2R on winners and −1R on losers is highly profitable: 0.4×2 − 0.6×1 = **+0.2R per trade**.

**3. Max daily and weekly loss — the circuit breaker.**
- **Daily stop:** 3R (or 3% of capital) → stop trading for the day. Close the terminal.
- **Weekly stop:** 6R → flat for the rest of the week.
These are *hard* limits that protect you from tilt, revenge trading, and a single catastrophic session (an expiry-day Bank Nifty gap can move 800+ points).

**4. Costs are part of risk (India, from 01-Apr-2026 — verify on NSE/broker/SEBI, rules change).**
Every trade leaks: brokerage + STT (options ~0.15% on sell premium; intraday equity 0.025% on sell; futures ~0.05% on sell) + exchange txn + SEBI fee + **18% GST on (brokerage+txn)** + stamp duty. On a Bank Nifty option round-trip you can pay ₹100–200+ in total charges. Build cost into your R: if a trade nets +2R gross but −0.15R in charges, plan on +1.85R.

| Item | Rule of thumb |
|---|---|
| Risk per trade | 0.5–1% of capital |
| 1R (₹5,00,000 acct) | ₹2,500–₹5,000 |
| Daily stop | 3R / 3% |
| Weekly stop | 6R |
| Min reward:risk to take a trade | ≥ 1.5 : 1 |

## Worked example — an R-based plan on ₹5,00,000 capital

Capital = **₹5,00,000**. Risk per trade = **1% = ₹5,000 = 1R**. Daily stop = **3R = ₹15,000**. Weekly stop = **6R = ₹30,000**.

**Trade: Bank Nifty futures long (illustrative).** Lot size = **35** (verify current lot on NSE — it changes). Say Bank Nifty future at **48,000**, structure-based stop at **47,850** (150 points away).

- Risk per lot = 150 pts × 35 = **₹5,250**. That is just over 1R — so **1 lot is the max**; a second lot would risk ₹10,500 = 2R and break the rule.
- Target at 2R = 300 points → **48,300**, reward = ₹10,500 gross.
- If the stop hits: −₹5,250 (≈ −1R). If target hits: +₹10,500 (≈ +2R) minus ~₹200 charges.

**A losing week, sized correctly:** Mon −1R, Tue −1R, Wed +2R, Thu −1R → net −1R = −₹5,000, i.e. **−1% of capital across four trades.** Compare the over-sized retail version at 5% risk/trade: same trade sequence = −5% −5% +10% −5% = **−5% = −₹25,000** in a single week, and one bad gap could double that. Same edge, same trades — position sizing alone is the difference between a −1% scratch and a −5% wound.

**The daily stop in action:** on a bad Thursday you take −1R, −1R, −1R by 12:30. You have hit 3R. You are **done** — no "just one more to get it back." That rule alone saves most accounts.

## How pros do it / common mistakes

**Pros:**
- Decide the stop and the rupee risk *before* entry; size is an output, never guessed.
- Keep every position at a uniform 0.5–1R so no single trade dominates the equity curve.
- Track results in R, so a ₹5,000 loss and a ₹500 loss on different accounts are comparable.
- Treat the daily stop as sacred — they physically log off.

**Classic retail errors & red flags:**
- **Sizing by margin/"how many lots can I afford,"** not by stop distance. Full-margin one lot of Bank Nifty options can still be a 10R bet if the stop is wide.
- **No stop, or a mental stop they widen** when price approaches it — turning −1R into −4R.
- **Averaging down** a loser (adding risk to a losing thesis) — the #1 account-killer.
- **Revenge trading** after a loss, doubling size to "make it back."
- **Ignoring costs**, then wondering why a 55%-win scalping system bleeds.
- Confusing a lucky +8R month for skill and then jacking size right before the drawdown.

## Checklist / drill

**Pre-trade checklist (every single trade):**
- [ ] What is my stop level, from *structure* (not a round number)?
- [ ] Rupee risk = (entry − stop) × qty. Is it ≤ 1R (₹5,000 on a ₹5L acct)?
- [ ] Is reward:risk ≥ 1.5:1 after estimated charges?
- [ ] Have I hit my 3R daily / 6R weekly stop? If yes → no trade.
- [ ] Is size an *output* of the stop, not a gut number of lots?

**Drill (2 weeks, paper or live-small):** Log every trade only in R. At week's end compute average R/trade and your worst losing streak. If any single trade shows a loss worse than −1.5R, your stop discipline failed — find out where. Do not touch size until 20 trades stay inside ±1R as designed. *Survival is the skill you build first; profit is what survival lets you keep.*
