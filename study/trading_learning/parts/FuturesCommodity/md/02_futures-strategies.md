# Futures Trading Strategies

## Why this matters

Most retail futures traders run exactly one strategy: leveraged directional punting on Bank Nifty, sized to margin, stopped out by noise. That is the single biggest reason the futures segment mirrors the grim SEBI stat — the large majority of individual F&O traders lose money net of costs. The pro's edge is not a better direction-guessing engine; it's owning a *portfolio* of futures structures — directional, calendar, pairs, and hedges — and choosing the one whose risk shape fits the setup. A pair trade doesn't care if the market crashes. A hedge lets you hold cash equity through a scare without selling. This chapter gives you the structures beyond "buy future, pray."

## The essentials

*(Specs/tax as of Jul 2026 — verify on NSE/broker/SEBI; rules change. F&O = non-speculative business income, FY2026-27; losses carry forward 8 years; ITR-3; tax audit u/s 44AB on turnover thresholds.)*

**1. Directional.** Long or short a single future for a trend. Only edge vs options: no theta decay, symmetric payoff, cheaper to hold a strong trend. Cost: unlimited-shaped risk and daily MTM. Rule of thumb — use futures for *conviction trends you'll actively manage*, options for *defined-risk event bets*.

**2. Calendar (horizontal) spread.** Simultaneously long one expiry and short another of the *same* underlying (e.g. long August Nifty, short July Nifty). You're trading the **basis / carry**, not direction. Margin is heavily reduced (the exchange nets the two legs — often 70-90% margin benefit) because your net delta is small. You profit if the spread moves your way (widening/narrowing).

**3. Pair (spread / relative-value) trade.** Long one instrument, short a correlated other — two banks, two IT names, or a stock vs its index. You bet on *relative* performance and are largely **market-neutral**: a broad crash hurts your long but helps your short. Key discipline: match the **rupee notional** of both legs (beta-adjust), not the lot count.

**4. Cash-futures hedge.** You hold a cash-market portfolio and short index futures to neutralise market risk through an event (Budget, election result, Fed) without selling your stock (avoiding STCG, exit costs, and re-entry timing). Hedge ratio = (Portfolio value × Portfolio beta) / (Index future notional).

## Worked example A — pair trade (HDFC Bank vs ICICI Bank)

*(Illustrative numbers.)* You judge **ICICI is outperforming HDFC Bank** and expect the gap to widen — but you don't want market direction risk.

- Short **HDFC Bank future** @ ₹1,600, lot 550 → notional 1,600 × 550 = **₹8,80,000**.
- Long **ICICI Bank future** @ ₹1,200, lot 700 → notional 1,200 × 700 = **₹8,40,000**.
- Notionals matched to ~₹8.5L each (adjust lots so legs balance; both bank betas ≈ 1, so no extra beta scaling needed here).

**Outcome after 2 weeks** — market flat, but ICICI outperforms:
- ICICI → ₹1,260 (+5%): long gain = 60 × 700 = **+₹42,000**.
- HDFC → ₹1,616 (+1%): short loss = 16 × 550 = **−₹8,800**.
- **Net = +₹33,200**, from the *spread*, with minimal exposure to whether the Nifty rose or fell.

**Why it's powerful:** in a day the whole market drops 2%, both legs lose on the index move but the short *gains* offset most of the long's loss — your P&L still tracks the ICICI-minus-HDFC spread. Margin benefit applies too, since correlated offsetting positions attract lower net SPAN. **Risk:** correlation breaks (a HDFC-specific bad news event moves it *against* your thesis on the wrong leg) — pairs are not risk-free, they swap market risk for *relative* risk.

## Worked example B — calendar spread (Nifty carry)

You think July-August Nifty spread of **75 points is too wide** and will compress as month-end funding eases.

- Sell August Nifty @ 24,255, Buy July Nifty @ 24,180 → **spread = 75**, lot 75.
- Because legs offset, margin might be only **~₹40,000-60,000** vs ~₹2.3L for a naked lot.
- Spread narrows to **55**: gain = (75 − 55) × 75 = **+₹1,500** on ~₹50,000 margin ≈ **3%**, with near-zero directional exposure. If it widens to 95 you lose ₹1,500. Small, high-probability, capital-light — the pro's bread-and-butter, run in size across cycles.

## Worked example C — hedging cash with futures

You hold a **₹20,00,000** equity portfolio, beta **1.1**, and want to sit out the Budget-day gap.

- Exposure to hedge = 20,00,000 × 1.1 = **₹22,00,000**.
- One Nifty future notional (24,000 × 75) = **₹18,00,000**.
- Hedge ratio = 22,00,000 / 18,00,000 ≈ **1.2 lots** → short **1 lot** (accept slight under-hedge) or use a smaller-notional contract if available.
- If Nifty falls 3% post-Budget, portfolio loses ~₹66,000 (3% × 1.1 × 20L); the short future gains ~3% × 18L = **~₹54,000**, cutting the net hit to ~₹12,000 instead of ₹66,000 — and you kept every share, avoiding STCG and re-entry risk.

## How pros do it / common mistakes

**Pros:**
- Match **notional/beta**, not lot counts, on pairs and hedges.
- Prefer **spreads and pairs** in choppy/rich-vol regimes — they harvest edge without needing a directional call, and enjoy margin netting.
- Treat **leverage as a dial, not a default** — size directional futures so a normal 1.5-2% adverse day is a survivable, pre-decided rupee loss.
- **Log the spread, not the legs.** Manage a pair by its spread chart; exit on spread targets/stops.

**Classic retail errors:**
- Running a "pair" with mismatched notionals — it's just a disguised directional bet.
- Legging in one side and never completing the hedge (naked risk while you "wait for a better price").
- Ignoring that a broad crash can hit *both* pair legs if correlation regime-shifts.
- Forgetting the tax bucket: F&O is **non-speculative business income** — keep clean books, spreads generate many trades and turnover adds up fast toward the audit threshold.
- Over-hedging into a *negative* directional bet by accident (shorting more index than portfolio exposure).

## Checklist / drill

Before any multi-leg or hedge:
- [ ] Both legs' **rupee notional** computed and matched (beta-adjusted).
- [ ] Entered as a **spread/2-leg order** where possible to control slippage.
- [ ] Defined the trade in terms of the **spread** (target + stop), not the individual legs.
- [ ] Confirmed **margin benefit** actually applied (check blocked margin).
- [ ] For hedges: hedge ratio computed, and I know the **residual risk** left unhedged.
- [ ] Correlation/thesis sanity-checked — what news breaks this pair?

**Drill:** Pick two correlated Nifty stocks. On paper, size a notional-matched pair and track the *spread* daily for 10 sessions alongside the Nifty. Note how often the spread P&L is independent of index direction — that felt experience of market-neutrality is the whole point.
