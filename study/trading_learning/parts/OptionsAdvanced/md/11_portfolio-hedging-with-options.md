# Hedging an Equity Portfolio with Options

*Practitioner supplement — NSE F&O options, India, 2026. Lot sizes, STT, and contract specs are date-stamped to Jan 2026 and change; **verify current Nifty/Bank Nifty lot sizes, STT schedule and index expiry days** before executing.*

## The idea

You hold a portfolio of Indian equities — a mix of large-caps, some mid-caps, a few high-beta banks and IT names. It has run well and you don't want to sell: selling triggers capital-gains tax, breaks long-term compounding, and forfeits dividends. But you're nervous — stretched valuations, an event calendar (Budget, Fed, elections), or simply a portfolio that has grown to a size where a 15% drawdown is real money. **Hedging with options lets you keep the portfolio and rent downside protection**, converting an unbounded left tail into a defined, budgeted cost.

The core insight: a diversified Indian equity portfolio is, statistically, mostly **Nifty (and partly Bank Nifty) plus some idiosyncratic noise.** You can hedge the *systematic* part — the market beta — cheaply and liquidly with index options, without touching a single holding. You cannot cheaply hedge every stock's specific risk, and you usually shouldn't try; diversification already handles much of the idiosyncratic risk, and what you fear in a crash is precisely the systematic move where correlations rush to 1.

Hedging earns its keep when: (1) you have unrealised gains you don't want to tax-realise, (2) a known event threatens a gap, (3) your portfolio beta has drifted high, or (4) you're near a financial goal and a drawdown would be catastrophic (sequence-of-returns risk). It is *not* free — a permanent full hedge bleeds premium and will underperform an unhedged portfolio across most years. The craft is **hedging selectively, cheaply, and only as much as your actual exposure requires.**

Honest framing: the most common hedging mistakes are *over-hedging* (paying so much premium the portfolio can't grow), *mis-sizing* (ignoring beta, so the hedge is half or double what's needed), and *panic-hedging* (buying puts after the fall, when IV and put skew are already expensive). A good hedge is sized, is bought when it's cheap, and is budgeted like an insurance premium.

## The mechanics

### Step 1 — measure what you're hedging: portfolio beta

You hedge *beta-adjusted* exposure, not rupee exposure. If your ₹1 crore portfolio has a weighted beta of 1.2 to Nifty, it behaves like ₹1.2 crore of Nifty. The **hedge notional** you need is:

Hedge notional = Portfolio value × Portfolio beta

Portfolio beta = Σ (weight_i × beta_i). Bank/IT/mid-cap heavy books run beta 1.1–1.4; defensive FMCG/pharma books run 0.7–0.9.

### Step 2 — convert to index lots

Number of index option lots (for a full-notional hedge) ≈

Lots = (Portfolio value × Beta) / (Nifty spot × Nifty lot size)

If Nifty = 24,000 and lot size = 25 (verify current — SEBI revised lot sizes/contract values in 2024–25 toward ~₹15–20 lakh notional), one Nifty lot ≈ 24,000 × 25 = ₹6,00,000 notional. A ₹1 cr portfolio at beta 1.2 = ₹1.2 cr exposure → ₹1.2cr / ₹6L ≈ **20 lots** to fully hedge with ATM protection (delta ≈ 1). If you buy OTM puts with delta ~0.3, you need proportionally more contracts to match the *delta* you want to offset — or you accept a partial, deductible-style hedge.

### Step 3 — choose the hedge structure

| Structure | What it does | Cost | Keeps upside? | Best when |
|---|---|---|---|---|
| **Protective put** (buy OTM Nifty put) | Floor below current level | Premium (1–3%/quarter) | Yes, fully | You fear a gap, want clean insurance |
| **Put spread** (buy put, sell lower put) | Floor over a *band* of decline | Cheaper (net debit) | Yes | Budget-limited; expect moderate fall |
| **Collar** (buy put, sell call) | Floor funded by capping upside | ~Zero cost | No (capped) | Willing to forgo upside for free protection |
| **Covered call** (sell call vs holdings) | Income + small cushion | Credit (income) | Capped | Sideways/mildly bearish, generate yield |
| **Put ratio / financed put** | Cheap partial hedge | Low/credit | Yes | Cost-conscious, moderate-fall view |

### Greeks of a hedge

A long put adds **negative delta** (offsets your long-stock positive delta), **positive gamma** (the hedge gets *more* protective as the market falls — convexity you want), **positive vega** (gains as fear/IV rises in a selloff — a second tailwind), and **negative theta** (the bleed — the premium you pay for time). A crash typically spikes IV, so a protective put pays off on *both* delta and vega — this is why index puts are a better crash hedge than short futures (futures give you delta but no vega/convexity kicker).

### Costs and tax (2026, verify)

- **Buying puts:** premium + txn charges + stamp (buy) + GST on charges; **no STT on the buy**. STT hits the sell/settlement side.
- **Selling calls (collar/covered call):** collect premium; **STT ~0.1% on sell premium**, plus margin (SPAN + exposure) since short options require margin. If the short call expires ITM (index cash-settled), STT-on-intrinsic applies — square before expiry.
- A hedge is a *cost centre*; budget it as, say, **2–4% of portfolio value per year** for continuous protective puts, far less for spreads/collars.

## Worked trade — protecting a ₹1 crore portfolio into an event-heavy quarter

**Setup (illustrative, Jan-2026 levels).** Portfolio value **₹1,00,00,000**, weighted **beta 1.15** (bank/IT tilt). Nifty spot = **24,000**. Budget (Feb 1) + Fed + results season ahead. I want a **3-month floor ~8% below spot** — protect against a crash, accept a small deductible, keep upside.

**Hedge notional** = 1cr × 1.15 = **₹1.15 cr**.
**Per-lot notional** = 24,000 × 25 = ₹6,00,000 (verify lot size).

**Structure chosen: 3-month Nifty put spread (buy 22,000 put, sell 20,500 put)** — a *disaster band* hedge that's far cheaper than an outright put and covers the 8–15% fall zone I actually fear.

| Leg | Strike | Action | Premium (₹/sh) | Delta |
|---|---|---|---|---|
| Put (long) | 22,000 PE (3M) | Buy | 320 | −0.30 |
| Put (short) | 20,500 PE (3M) | Sell | 130 | −0.14 |
| **Net debit** | | | **190** | −0.16 net |

- To cover ₹1.15 cr with this structure, target lots ≈ hedge notional / per-lot notional = 1.15cr / 6L ≈ **19 lots** (rounded; I'll run **18** to keep it a partial, cost-aware hedge).
- **Net debit** = 190 × 25 × 18 = **₹85,500** ≈ **0.85% of portfolio for 3 months** (~3.4% annualised if held continuously).
- **Protection band:** kicks in as Nifty falls below 22,000 (−8.3%), maxes out at 20,500 (−14.6%). **Max hedge payoff** = (22,000 − 20,500 − 190) × 25 × 18 = (1,310) × 450 = **₹5,89,500**.
- **Greeks added:** net delta ≈ −0.16 × 25 × 18 ≈ **−72 delta** of Nifty (offsets part of my ~+479 portfolio delta equivalent), positive gamma and vega below 22,000.

**Scenario — the crash I feared (Nifty −12% to 21,120).** My portfolio (beta 1.15) falls ~13.8% → **−₹13,80,000**. The put spread: long 22,000 put now ~₹950 intrinsic-ish (deep ITM), short 20,500 put still OTM (~₹120). Spread value ≈ (21,120 below 22,000 → 880 intrinsic + time) minus short leg ≈ net ~₹760/sh. Hedge P&L ≈ (760 − 190) × 25 × 18 = **+₹2,56,500**, and IV-spike adds more. Net portfolio loss cushioned from −₹13.8L to roughly **−₹11.2L** — the deductible (first 8%) is uninsured by design; the disaster band is covered. Had I bought the outright 22,000 put (no short leg), protection would be larger but cost ~₹1,44,000 for the quarter.

**Scenario — market rallies +8% (Nifty 25,920).** Portfolio gains ~+₹9.2L. Put spread expires worthless: **−₹85,500** (the insurance premium). Net +₹8.35L — I kept nearly all the upside, having paid 0.85% for peace of mind. This is the correct, unglamorous outcome most of the time.

## Management

**Roll the hedge, don't abandon it.** As the puts approach expiry, roll to the next quarter to maintain the floor. Roll *strikes* too: if the market rose, roll the whole spread up to keep the floor a constant % below spot; if it fell toward your long strike, you may monetise (see below) and re-establish.

**Monetise into a selloff.** When the market drops and your puts are deep ITM with fat vega, they're worth far more than you paid. **Take profits on the hedge** — sell the appreciated put spread, bank the gain, and either re-strike a fresh lower hedge or hold unhedged if you think the worst has passed. A hedge you never monetise is just a bleed; the skill is harvesting convexity when fear is priced richly.

**Adjusting the collar.** If you funded the put by selling a call (collar) and the market rallies toward your short call, you face a capped-upside problem: roll the call up-and-out (buy it back, sell a higher/later call) to give the portfolio room, accepting a small debit. If the market falls, the short call decays to zero — pure funding win.

**Scenario matrix.**

| Market | IV | Hedge action |
|---|---|---|
| Sharp fall | IV up | Monetise puts (delta + vega gain); re-strike lower |
| Grind down | IV mild | Let puts work; roll near expiry |
| Rally | IV down | Roll spread up to keep floor %; accept small premium loss |
| Sideways | IV down | Puts bleed theta; consider cheaper spread/collar, or covered calls for income |

**Beta drift.** Re-measure portfolio beta quarterly. A book that rotates into high-beta banks/PSUs needs more lots; a rotation into FMCG/pharma needs fewer. An unadjusted hedge silently becomes a half-hedge or a double-hedge.

## Risk & sizing

**Basis risk is the main hidden risk.** Index options hedge *systematic* risk. If your portfolio is concentrated in a few mid-caps that crash while Nifty holds, the hedge won't pay — you hedged the market, not your stocks. Mitigations: keep the portfolio genuinely diversified, or for a large single-name concentration use that stock's own options (if liquid). Accept that idiosyncratic blow-ups are largely un-hedgeable cheaply.

**Over-hedging risk.** A full ATM protective put continuously held can cost 6–10%/year in premium — enough to neutralise the equity risk premium you're invested for. **Prefer partial hedges, spreads, collars, and event-timed hedges** over permanent ATM insurance. Hedge the tail (the disaster band), self-insure the deductible (the first 5–8%), which historically reverts.

**Margin and assignment (short legs).** Collars/covered calls require SPAN margin on the short option and can be assigned/settled ITM (cash-settled on index). Keep margin buffer; square ITM shorts before expiry to avoid STT-on-intrinsic and settlement surprises.

**Sizing discipline.** Size the hedge to *beta-adjusted notional*, choose a floor level you can articulate ("protect below −8%"), and pre-set a premium budget (e.g., ≤ 3% of portfolio/year). Portfolio Greeks after hedging should show meaningfully reduced net delta below your floor and *positive* gamma/vega in a crash — verify the hedge actually convexifies your left tail, not just shaves a little delta.

**Timing.** Buy insurance when it's cheap — when India VIX is low and put skew is flat, *before* the event, not after the gap. Panic-hedging into a spiking VIX means paying peak premium for protection against a move that may be half-over.

## Pitfalls & interview-ready summary

**Pitfalls**
- **Ignoring beta.** Hedging rupee value instead of beta-adjusted value leaves you half-hedged (high-beta book) or over-hedged (defensive book).
- **Over-hedging permanently.** Continuous ATM puts bleed away the equity premium; prefer spreads, collars, and event-timed hedges.
- **Panic-hedging.** Buying puts after the fall pays peak IV and peak skew; the cheap time to insure is before the event, at low VIX.
- **Basis risk denial.** Index hedges won't save a concentrated single-name portfolio; diversify or hedge the name directly.
- **Never monetising.** Deep-ITM puts in a selloff are a gift — harvest the convexity and re-strike, don't let a winning hedge expire unused.
- **STT-on-intrinsic on short legs.** Collar/covered-call shorts left ITM at expiry attract STT on settlement value — square before expiry.
- **Stale beta.** Re-measure after portfolio rotation; an unadjusted hedge drifts to the wrong size.

**Interview-ready summary.** *Hedging an Indian equity portfolio with options means renting downside on the systematic (Nifty/Bank Nifty beta) component while keeping the holdings, their dividends and their tax-deferred gains. You size the hedge to beta-adjusted notional (portfolio value × portfolio beta), convert to index lots at current contract value, and choose a structure by cost tolerance: protective puts for clean insurance, put spreads for a budgeted disaster-band, collars for near-zero-cost protection funded by capping upside, covered calls for income in flat markets. A long put adds negative delta, positive gamma and positive vega — so it pays off on both the fall and the IV spike, giving true left-tail convexity that short futures can't. The craft is to hedge selectively and cheaply: insure the tail, self-insure the first 5–8% deductible, buy protection when VIX is low and before events rather than panic-hedging into a spike, monetise puts when a selloff makes them rich, and roll strikes to keep the floor a constant percentage below spot. Main risks are basis risk (index won't hedge concentrated single names), over-hedging away the equity premium, and STT-on-intrinsic on short legs. Verify 2026 lot sizes, STT and expiry conventions before executing.*
