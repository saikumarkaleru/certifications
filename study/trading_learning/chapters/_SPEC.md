# Shared spec — "Options Trading: Zero to Professional" (India / NSE F&O)

You are writing ONE chapter of a ~500-page options book for a reader who has **MBA-finance basics but
almost no options knowledge**, and wants to become a **top professional options trader on Indian markets
(NSE F&O: Nifty, Bank Nifty)**. Write so a complete beginner understands, but build all the way up to
professional depth.

## Voice & approach (non-negotiable)
- **Intuition first, then the math.** Explain every idea in plain English with an analogy or story BEFORE
  any formula. Then give the formula cleanly and a **worked numerical example in Indian terms** (Nifty/
  Bank Nifty levels ~24000 / ~52000, ₹ premiums, lots, weekly expiry).
- **India-focused.** Use NSE mechanics, SEBI rules, India VIX, SPAN margin, STT, ₹. Index options are
  **European, cash-settled**; stock options are physically settled. State time-varying numbers (lot
  sizes, tax rates, margins) conceptually ("about", "currently") since they change.
- **Define every term on first use.** No unexplained jargon.
- **Honest pedagogy.** Tell the truth about risk: long options usually expire worthless, option selling
  has large/undefined risk, and ~9 in 10 retail F&O traders lose money (SEBI studies). No "guaranteed"
  anything. This protects the reader.

## Exact chapter structure (use these section headings)
Start the file with: `# Chapter N: <Title>` (use the number/title given in your task).
Then, in order:
1. **Intro / the big idea** — 1-2 short paragraphs of plain-English intuition (why this matters).
2. **## Core concepts** — teach it step by step, beginner → advanced. Use `###` sub-headings, short
   paragraphs, and bullet/numbered lists. Put key formulas in plain text inside backticks, e.g.
   `Payoff (long call) = max(S - K, 0) - premium`. Greek letters spelled out (delta, sigma, theta).
3. **## Worked example (₹, Nifty/Bank Nifty)** — at least one fully worked numeric example with steps.
4. **A figure** — embed the assigned figure(s) exactly as: `![Figure: <caption>](figs/<name>.png)` on its
   own line, placed where it best supports the text. ONLY use figure names from the manifest below.
5. **## Common mistakes / risk note** — what beginners get wrong; the honest risk.
6. **## Key takeaways** — 4-7 crisp bullets.
7. **## Practice problems** — 4-6 numbered problems (mix conceptual + numeric, India context).
8. **## Solutions** — full worked solutions to those problems.

## Format rules
- Markdown only. Plain-text formulas (no LaTeX, no `$`, no unicode math symbols). Use `*` multiply,
  `^` power, `sqrt()`, write Greek as words.
- Length: **~2,500–3,500 words** (this is a full book chapter — be thorough, not padded).
- Do NOT write a cover/TOC/part header — just your chapter. Do not number sections globally.
- Embed only the figure(s) named in your task. Reference them with the `figs/<name>.png` path exactly.

## Figure manifest (only embed the ones your task assigns)
Payoffs: long_call, long_put, short_call, short_put, long_call_time (P&L now vs expiry),
bull_call_spread, bear_put_spread, bull_put_spread, bear_call_spread, long_straddle, short_straddle,
long_strangle, short_strangle, long_butterfly, iron_butterfly, iron_condor, covered_call,
protective_put, collar, ratio_spread, call_backspread, synthetic_long.
Pricing/value: time_value (intrinsic vs time value), time_decay (value as expiry nears), binomial_tree.
Greeks: delta_call, delta_put, gamma, gamma_vs_time, theta, theta_vs_time, vega, rho.
Volatility: vol_smile, vol_skew, term_structure, pop_distribution (lognormal terminal + breakevens).

After writing, reply with: the file path and your chapter's word count.
