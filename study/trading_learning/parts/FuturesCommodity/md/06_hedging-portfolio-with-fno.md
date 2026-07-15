# Hedging a Portfolio with Futures & Options

## Why this matters

Most retail investors have exactly one risk management tool: sell everything in a panic — usually near the bottom, crystallising the loss and triggering tax. Pros don't liquidate a carefully built portfolio to survive a three-week drawdown; they *hedge* it, hold the underlying, and remove the hedge when the storm passes. You already know option pricing and Greeks. This chapter is about the *portfolio-level* application: how to translate a ₹-lakh equity book into the right number of Nifty futures or put contracts using **beta**, and — the part nobody tells retail — *when the hedge is worth its cost and when it quietly bleeds you*.

Honest truth: hedging is insurance. Insurance has a premium. Over-hedging a long-term portfolio is one of the most reliable ways to underperform a simple buy-and-hold — because you pay the premium every cycle but the crash only comes occasionally.

## The essentials

**Beta (β)** measures how much a stock/portfolio moves relative to the index (Nifty 50). β = 1.2 means the stock tends to move 1.2× the Nifty. Your **portfolio beta** = weighted average of holdings' betas.

**Beta-hedge (index futures).** To neutralise market risk you short index futures worth:

> Hedge notional = Portfolio value × Portfolio beta

Number of lots = Hedge notional ÷ (Index level × lot size). A full hedge (β-neutral) removes *systematic* (market) risk but leaves *stock-specific* risk. Shorting futures caps your downside **and your upside** — it's a symmetric trade.

**Protective put.** Buy a put on the index (or stock) as a floor. Downside is limited to (strike − premium); upside is uncapped. Cost = the premium, which you lose if nothing crashes. This is true insurance — asymmetric.

**Collar.** Buy a protective put *and* sell a call above the market to finance the put. Near-zero net premium, but you cap upside at the call strike. Popular for holding a concentrated position through an event.

**Delta-hedge (concept).** Instead of a static hedge, offset the *delta* of your position and re-adjust as price moves (dynamic). Pros running options books do this continuously; for a cash portfolio it's usually overkill — a static beta-hedge is enough.

**When to hedge (India specifics):**
- Around a known binary event — Union Budget (Feb 1), RBI MPC, general election results, US Fed, large earnings.
- When you want to defer capital gains: hedging lets you hold the underlying (no sale, no STCG/LTCG trigger) while protecting value.
- **Tax note (FY2026-27):** F&O gains/losses are **non-speculative business income** (set-off flexible, loss carried forward 8 years), taxed at slab; equity delivery gains are STCG/LTCG. The hedge P&L and the portfolio P&L therefore sit in *different tax heads* — plan for it. Costs on the hedge: STT ~0.05% on futures sell, ~0.15% on option premium (sell), plus brokerage/GST/stamp. **Verify on NSE/broker — rules change (STT figures effective 01-Apr-2026).**

## Worked example — hedging a ₹25 lakh equity portfolio

Portfolio value **₹25,00,000**, weighted **beta 1.2**. Nifty at **24,000**, futures lot size **75** (verify on NSE — revised periodically).

**Step 1 — hedge notional:** ₹25,00,000 × 1.2 = **₹30,00,000** of Nifty exposure to short.

**Step 2 — lots:** one lot notional = 24,000 × 75 = ₹18,00,000. Lots needed = 30,00,000 ÷ 18,00,000 = **1.67 → 2 lots** (round to nearest; 2 lots = ₹36 L, slightly over-hedged; 1 lot leaves you under-hedged — pros pick per conviction).

**Test the hedge (Nifty falls 5%):**
- Portfolio (β 1.2) drops ≈ 5% × 1.2 = 6% → **−₹1,50,000**.
- Short 2 lots gains 5% × ₹36,00,000 = **+₹1,80,000** (gross).
- Net ≈ **+₹30,000** — the over-hedge (2 vs 1.67 lots) even turned a small profit. A 1.67-lot ideal hedge would net ≈ 0.

**Cost of holding the futures short:** STT on exit ~0.05% of ₹36 L sell ≈ ₹1,800, plus brokerage (~₹20/lot), exchange/SEBI/stamp and 18% GST — call it a few hundred to ~₹2,000 round trip. Cheap relative to the ₹1.5 L protected.

**Alternative — protective put:** Buy 2 lots of the 24,000 put. Say premium **₹250/unit** → 250 × 75 × 2 = **₹37,500** premium. If Nifty *rises* instead, you keep 100% of the portfolio upside and lose only the ₹37,500 — the futures short would have surrendered that entire upside. That asymmetry is why you pay for puts before *uncertain, skewed* risk (Budget) and use futures for *pure directional* de-risking.

**Collar:** buy the 24,000 put (₹250), sell the 24,600 call (~₹150) → net premium 100 × 75 × 2 = **₹15,000**, but upside capped at 24,600. Cheapest protection, sacrifices some upside.

## How pros do it / common mistakes

**How pros do it**
- Compute portfolio beta honestly (don't assume 1.0); a small/mid-cap-heavy book can be β 1.4–1.6, so a "full" hedge needs *more* index notional than portfolio value.
- Match the tool to the risk: **futures** for cheap, symmetric de-risking of directional exposure; **puts** for asymmetric event protection where they want to keep upside; **collars** when premium budget is tight.
- Hedge *tactically and time-boxed* — put it on before an identified event, take it off after. They do not carry a permanent hedge on a long-term compounding portfolio.
- Track **basis risk**: an index hedge won't perfectly offset a stock-specific book; residual (idiosyncratic) risk remains.
- Roll the hedge before expiry (last Thursday) if the reason to hedge persists.

**Common mistakes**
- Permanently hedging a long-term SIP-style portfolio and wondering why returns lag the index — you're paying insurance forever.
- Ignoring beta and hedging ₹-for-₹ (a β 1.4 book is under-hedged if you match only portfolio value).
- Buying deep OTM puts that "feel cheap" but never pay out.
- Forgetting the hedge is in a *different tax head* and mismatched settlement/margin.
- Under-margining the short and getting an MTM/peak-margin penalty call at the worst moment.

## Checklist / drill

Before placing a hedge:

1. **Portfolio value** and **weighted beta** — computed, not guessed?
2. **What am I hedging?** Broad market fall (→ futures) or an event with upside I want to keep (→ put/collar)?
3. **Notional & lots:** value × beta ÷ (index × lot size) — rounded which way, and why?
4. **Cost:** premium or STT/charges tallied — is protection worth it vs the risk?
5. **Exit plan & margin:** when do I remove the hedge, do I have SPAN+Exposure margin, and when is expiry?

**Drill:** Take your real (or a mock ₹10 L) holding, look up each stock's beta, compute portfolio beta and the exact Nifty-futures lots for a full hedge. Then re-price it as a protective put and as a collar. Compare the three payoffs for a −7%, 0%, and +7% Nifty move. You'll internalise *when* each is the right instrument.

*STT, lot sizes, margins and tax treatment current as of 2026 — re-verify on NSE / your broker / SEBI before trading; rules change.*
