# Shared spec — "The Options Strategy Encyclopedia" (India / NSE F&O)

You are writing ONE group-chapter of a 200-strategy encyclopedia that is appended to a professional
options book. The reader has MBA-finance basics and is learning to trade NSE F&O (Nifty ~24000, Bank
Nifty ~52000, weekly/monthly expiry, ₹ premiums, lot ~75 for Nifty). Be practical, honest, and concrete.

## Your data source (use it — do NOT invent numbers)
Read `strategies_metrics.json` in the project root. Each record has:
`n, slug, name, category, view, vol, legs_text, net_cost, debit_credit, max_profit, max_loss,
max_profit_unlimited, max_loss_unlimited, breakevens, risk_reward, lot, fig`.
- The numbers were computed by a Black-Scholes engine on Nifty at 24000 (points per unit; multiply by
  `lot`≈75 for ₹ per lot). USE THEM EXACTLY. Do not recompute or contradict them.
- `max_profit`/`max_loss` are in points; `null` with the matching `*_unlimited: true` means
  unlimited/undefined — say "Unlimited" (profit) or "Undefined — large" (loss).
- `net_cost` > 0 = net debit (you pay); < 0 = net credit (you receive). For stock strategies `net_cost`
  includes the ~24000 index outlay — describe the OPTION premium separately in words when it matters.
- `breakevens` is a list of Nifty levels. `risk_reward` is reward:risk as a number (null when a side is
  unlimited).

## Honest-pedagogy rule (important)
For naked-short / stock-owning trades (short put, covered call, the wheel, jade lizard, etc.) the engine's
`max_loss` is the theoretical loss if the index fell to ZERO (a bounded but catastrophic number, and the
reason `risk_reward` looks tiny like 0.01). Always add one honest sentence: *"This worst case assumes the
index collapses to zero; in practice you size small and manage/stop at a multiple of the credit."* Never
imply premium-selling is free money — most retail F&O traders lose (SEBI studies).

## File structure
Start the file with:
`# Strategy Group <N>: <Category Name>`
Then a 2–3 sentence intro to the family (what unites these, the core trade-off). Then EACH strategy in
ascending `n` as its own `##` section, exactly:

`## <n>. <Name>`
`*<view> · <vol> · net <debit/credit></>*`  (one italic context line)

**The idea (intuition).** 1–3 sentences, plain English: the story/why this structure exists, in terms a
beginner gets. Use an analogy when it helps.

**When & why to use it.** The market conditions that call for it — direction, IV regime (high/low IV
rank, India VIX), days to expiry, catalyst — AND when NOT to use it. This is the heart of "when to use
what." Be specific to NSE (e.g., "sell after a Budget-day IV spike", "Bank Nifty weekly", "IV rank > 70").

**How to build it (₹, Nifty).** State the legs concretely from `legs_text` (e.g., "Buy 24000 CE, sell
24300 CE"), the net debit/credit in points and in ₹ per lot (points × lot). One worked line.

`![Figure: <Name> payoff at expiry](<fig from JSON>)`   ← use the `fig` path verbatim.

**The numbers (modelled at Nifty 24000).** Max profit, max loss, breakeven(s), net debit/credit, and
risk:reward — taken verbatim from the JSON, each in points and (where useful) ₹ per lot. Note "Unlimited"
/ "Undefined — large" where flagged.

**Greeks & behaviour.** The net delta (direction), theta (does time help or hurt?), and vega (does rising
IV help or hurt?) — sign and one line on what dominates the P&L.

**Management & exit.** A concrete target (e.g., "close at ~50% of max credit"), a stop or adjustment/roll
idea, and when to take it off (e.g., "exit before expiry-week gamma" or "roll the tested side").

**Risk note.** The honest danger in one or two sentences (assignment, gap/tail risk, IV crush, liquidity,
STT on exercised ITM options for stock names, etc.).

## Format rules
- Markdown only. Plain-text formulas (no LaTeX, no `$`). Greek letters as words (delta, theta, vega).
- ~400–550 words PER strategy (be substantive but tight — this is a reference, every line earns its place).
- Embed each strategy's own figure with the exact `fig` path from the JSON, on its own line.
- Do not write a cover/TOC/part divider. Just your group-chapter. Do not renumber the strategies.
- Vary the prose — do not paste a template; make each entry read like a desk trader explaining the trade.

After writing, reply with: the file path and your file's word count.
