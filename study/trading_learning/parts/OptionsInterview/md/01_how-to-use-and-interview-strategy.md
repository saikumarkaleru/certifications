# How to Use This & Options-Interview Strategy

This bank is built for one job: walking into an *experienced-level* NSE F&O options seat — prop desk, hedge fund, market-maker, or a serious HNI/family-office trading role — in 2026 and sounding like someone who has actually run a book, not someone who read a textbook. Use it as a rehearsal partner, not a script. Read a chapter, then close it and answer out loud. If you can't hit the *"say it crisply"* line from memory, you don't own it yet.

## What senior interviewers are actually probing for

At a junior interview, they check whether you know what a call option is. At the experienced level, the definitions are assumed — they are hunting for three things, and every question is a proxy for one of them:

1. **Do you think in Greeks and vol, not in direction?** A trader who talks only about "market will go up so I bought calls" is a punter. A trader who says "I'm long the 15-delta wing because skew is rich into the event and I want convexity, funded by short gamma at the body" is a professional. The interviewer wants to hear the *second language* — delta, gamma, vega, theta, skew, term structure — used naturally, as the unit you actually think in.

2. **Do you have a risk framework, or do you have a story?** Real desks blow up on the position nobody sized. They will push you: *"What's your max loss? Where's your stop? What happens to this book if Bank Nifty gaps 4% overnight and IV doubles?"* The right candidate has *numbers* — position limits, greek limits, a scenario grid, a stop discipline — and can produce them without flinching. The wrong candidate says "I'd manage it."

3. **Have you actually held a position through pain?** This is the one you cannot fake with theory. They want the scar tissue: the trade where you were short gamma into an RBI policy and got run over, what the P&L did intraday, what you *did* — cut, hedged, rolled, or froze — and what you changed afterwards. Experience is measured in losses survived, not strategies memorized.

## How to structure every answer

Lead with the punchline, then the reasoning, then a concrete example. Interviewers are pattern-matching for clarity of thought under time pressure — the same skill that keeps you alive when the tape is moving.

- **Punchline first (one sentence).** "Short gamma means I lose on big moves and get paid to sit still." Don't build up to it; state the conclusion, then defend it.
- **Reasoning (the mechanism).** Explain *why* in cause-and-effect terms — what the greek does, how the P&L accrues, where the risk hides.
- **A real number.** "On a 200-lot Nifty short straddle at 24,000, a 300-point gap is roughly ₹X of gamma loss before I even touch vega." Numbers signal you've lived it. Use real strikes, real-ish premiums, real lot sizes.
- **The management nuance.** Close with how a *seasoned* trader handles it — the roll, the delta-hedge cadence, the sizing rule. This is what separates you from a bright graduate.

Keep it to 45–90 seconds. If they want more, they'll dig — and the follow-up is where you win.

## Red flags that instantly expose a fake

Interviewers listen for tells. Avoid these, and listen for them if you're ever on the other side of the table:

- **Confusing IV with direction.** "IV is high so the market will fall." IV is the *price of movement*, not its sign. High IV means the market expects a big move *either way*. Saying otherwise ends the interview in their head.
- **No risk framework.** If your answer to "how do you size?" is vibes, you're out. Even a simple, honest rule ("I risk max 1% of capital per structure, and I cap net vega at ₹X per point of IV") beats hand-waving.
- **Never having taken a real loss.** Anyone who describes only winners is lying or hasn't traded size. A clean, specific story about a loss — and the lesson — builds *more* credibility than a win.
- **Greeks as trivia, not tools.** Reciting the BSM formula but unable to say what vanna does to your book around an event. They don't want the formula; they want the *consequence*.
- **Ignoring India microstructure.** Talking pure CBOE theory with no mention of STT on ITM exercise, physical settlement of stock options, SPAN margin, or weekly-expiry gamma. It signals you've never actually cleared a trade here.

## The honesty note (read this twice)

Answer truthfully about *your* real F&O experience. If you've traded a modest personal book, say so plainly and let the *depth of your reasoning* carry the credibility — that is what an experienced interviewer actually weighs. Do **not** invent a P&L, a fund, or a track record; desk heads have seen a thousand candidates and smell a fabricated number instantly, and one caught lie voids everything else you said. It is completely legitimate to say "I haven't run institutional size, but here's exactly how I'd manage this risk and why" — demonstrated understanding of mechanics and risk is the asset you're selling. Your edge in this interview is that you genuinely *understand* options, not that you claim a history you don't have.

## Night-before cram checklist (one page)

**Contract specs (verify current — SEBI/NSE revise these):**
- Nifty 50 lot size **75**; Bank Nifty lot **35** (verify — revised in the 2024–25 cycle). FinNifty, Midcap, Sensex have their own lots.
- Weekly expiries: verify the current schedule — SEBI moved to **one weekly expiry per exchange** (Nifty on NSE) plus monthlies. Do not assume the old multi-weekly grid.
- Index options: **cash-settled**. Single-stock options: **physically settled** on expiry — you deliver/take shares.

**Costs & taxes (2026):**
- **STT on options: ~0.10% of premium on the sell side historically → hiked to ₹0.10% and set to ~0.15% of premium from the 2026 cycle (verify exact rate/effective date).**
- **The ITM-exercise STT trap:** STT on *exercised* ITM options is charged on **intrinsic/settlement value (notional)**, not premium — far larger. Never let a deep-ITM option auto-exercise if you can square off; letting it exercise can cost multiples of the premium in STT.
- Exchange txn charges, GST (18% on brokerage+txn), stamp duty, SEBI turnover fee.

**Margins:**
- **SPAN + Exposure** margin on shorts; SPAN is scenario-based (worst of ~16 risk arrays). Long options: premium only. Margin benefit for hedged/spread positions.

**Greeks & numbers to have cold:**
- ATM option delta ≈ **0.5**; delta ≈ risk-neutral P(ITM) proxy.
- ATM straddle premium ≈ **0.8 × S × σ × √(T)** → back out expected move.
- Gamma and theta peak **ATM**; both explode into expiry. Long gamma = long theta bill.
- Vega highest for **ATM, longer-dated**; per 1 vol-point.
- Put-call parity: **C − P = S − K·e^(−rT)**.
- India VIX: annualized 30-day Nifty IV; daily expected move ≈ VIX/√252.

**Have ready:** your one real loss story (what, why, what you did, what you changed), your sizing rule, and your one-line view on current Nifty/Bank Nifty IV regime.
