# Supply & Demand Trading II

Chapter 50 built the theory: zones are footprints of institutional order imbalance, marked by a tight base and an explosive departure, drawn as rectangles with a proximal (entry) edge and a distal (stop) edge. This chapter turns that framework into a *complete, executable trading system* — exact entries, stops, targets, position sizing with real Indian costs, zone-management refinements the professionals use, and specific adaptations for Nifty, Bank Nifty, options, and MCX. The emphasis throughout is on mechanics you can run tomorrow morning on a TradingView chart.

## Origin and idea, refined

The retail S&D community (Sam Seiden's "Online Trading Academy" lineage) popularised zones, but the professional refinement borrows heavily from Wyckoff and modern order-flow: *not all zones are equal, and the same rectangle can be graded on a scorecard*. The system in this chapter is a **zone-scoring, top-down, reward-to-risk-first** approach. You never take a zone because it exists; you take it because it scores well *and* offers 3:1 or better. That single discipline — grading plus R:R gating — is what separates a profitable S&D trader from someone who draws pretty rectangles and bleeds.

## The zone scorecard

Before any trade, score the zone out of a checklist. Assign one point each:

| Factor | Points | What you check |
|---|---|---|
| Strength of departure | 0–2 | 1 pt for a strong leg, 2 pts for a gap/imbalance leaving the base |
| Tightness of base | 0–1 | 1–3 candles = 1 pt; wider = 0 |
| Freshness | 0–2 | untouched = 2, touched once = 1, more = 0 |
| HTF trend alignment | 0–2 | with daily trend = 2, neutral = 1, against = 0 |
| Time away | 0–1 | left the zone quickly and stayed away |
| Confluence (Fib/OI/round no.) | 0–2 | each independent confluence, max 2 |

A zone scoring **8–10 is A+** (size up, set-and-forget acceptable). **5–7 is B** (trade only with confirmation and normal size). **Below 5, skip.** This scorecard forces objectivity onto an inherently discretionary method and gives you a trading journal metric you can actually review.

## Exact entry rules

Two entry protocols; choose per zone grade and per your temperament.

### Protocol A — Set-and-forget (limit order)

Best for A+ zones and for traders who cannot watch screens (working professionals, the Indian retail norm).

1. Place a **buy limit at the proximal line** of a fresh demand zone (or sell limit at supply proximal).
2. Place the **stop-loss just beyond the distal line** — for demand, a buffer of ~0.1–0.2% below the distal wick; for Bank Nifty that is roughly 40–60 points, for Nifty ~15–25 points.
3. Place the **first target at the nearest opposing structure** (a prior swing high for a long).
4. Walk away. Either it fills and works, fills and stops, or never fills. No screen-watching, no fear-driven exits.

Set-and-forget suits Indian salaried traders because it converts trading into a nightly homework task: mark zones after market close, place orders for the next session, done.

### Protocol B — Confirmation entry (lower-timeframe trigger)

Best for B-grade zones, counter-trend bounces, and volatile instruments like Bank Nifty where zones are frequently overshot.

1. Wait for price to *trade into* the zone.
2. Drop to a lower timeframe (e.g., zone found on 15-min → confirm on 3-min).
3. Enter only on a **change of character (CHoCH)** — the lower timeframe makes a higher-high after a downtrend into the zone (for a long), or on a strong reversal candle (bullish engulfing, pin bar) closing back above the proximal line.
4. Stop goes below the lower-timeframe swing low (tighter than the full-zone stop → better R:R), or below the distal line if you want safety.

Confirmation costs you a slightly worse entry price and occasional missed moves (price reacts without confirming), but it dramatically cuts the "zone sliced straight through" losses.

### Entry decision table

| Zone grade | Trend | Entry protocol | Sizing |
|---|---|---|---|
| A+ (8–10) | with trend | Set-and-forget | full |
| A+ | counter-trend | Confirmation | half |
| B (5–7) | with trend | Confirmation | full |
| B | counter-trend | Confirmation | half or skip |
| < 5 | any | Skip | — |

## Stops, targets, and trade management

**Stop-loss.** Always beyond the distal line plus a small buffer, because stop-hunts routinely spike a few ticks past the wick before reversing. A stop *inside* the zone defeats the purpose — the whole point is that price may probe the zone before turning. Invalidation is a *candle close* through the distal line; an intraday wick that closes back inside does not invalidate.

**Targets.** Use a laddered approach:
- **T1** = nearest opposing structure or the far edge of the range. Book 50% here; this is your "get to breakeven and de-risk" target.
- **T2** = next major swing / the opposite HTF zone.
- **Runner** = trail the remainder below successive higher-lows (for longs) using structure, not a fixed rupee amount.

**Break-even discipline.** Once T1 is hit and half is booked, move the stop to entry. Now the trade is risk-free and you let the market decide how far the runner goes. This "de-risk fast, run the rest" model is what makes S&D's 3:1+ zones compound: many small break-evens, occasional large winners.

## Worked India example — Bank Nifty supply zone, intraday

Bank Nifty (representative 2025–26 levels) opens and rallies hard in the first hour:

- 09:15–10:00: rallies from 50,600 to 51,250 (a **rally**).
- 10:00–10:20: two 5-min candles chop between 51,220 and 51,280 — a tight **base**.
- 10:25 onward: a large red candle, then a second — collapses to 50,900 (an **explosive drop**).

This is a **Rally–Base–Drop (RBD) → supply zone** on the 5-min chart. Draw it:
- **Distal line (stop reference):** high of base incl. wick = **51,290**.
- **Proximal line (entry):** body low / open of base = **51,240**.

**Scorecard:** strong departure with a small imbalance (2) + tight 2-candle base (1) + fresh (2) + it is the morning high so slightly counter to no clear daily trend (1) + left quickly (1) + sits near round 51,250 and (say) heavy 51,300 Call OI (2) = **9/10, A+ supply.**

Around 11:40 Bank Nifty rallies back and trades into 51,240. Using Protocol B (Bank Nifty overshoots often), we wait: on the 1-min a bearish engulfing prints and closes back below 51,240. We short.

- Entry: **51,235**.
- Stop: above distal + buffer = **51,320** (85-point risk).
- T1: prior swing 50,900 (335 points).

**Options translation (the realistic Indian intraday trade).** Rather than short futures, many traders express this by buying a slightly ITM/ATM put or shorting a call. Suppose we buy the **51,200 PE** trading at ₹150. If Bank Nifty falls the 335 points to T1, a near-ATM put with delta ~0.5 gains roughly 335 × 0.5 ≈ ₹167 in intrinsic terms plus whatever delta acceleration occurs, but *theta and IV crush work against us*, so a realistic fill might be ₹150 → ₹250–280. On one lot (lot size 35, representative), that is a gain of roughly (270 − 150) × 35 = **₹4,200** against a risk defined by our futures-level stop. If the zone invalidates (close above 51,320), the put might sag to ₹100–110, a loss of ~(150 − 105) × 35 = **₹1,575**. Note the option's non-linearity: our *chart* R:R was ~3.9:1 but the *option* R:R is closer to 2.7:1 because theta and IV eat premium. This is the honest, crucial adjustment — **a clean chart trade does not translate one-to-one into an option P&L.**

Practitioners who want the chart's true R:R should trade **futures** (linear) or deep-ITM options (delta near 1); ATM options add a volatility bet on top of the directional bet.

## Position sizing with realistic Indian costs

The non-negotiable rule: **risk a fixed fraction of capital per trade**, typically 1% (aggressive: 2%, conservative: 0.5%). Work it backwards from the stop.

Suppose account = ₹5,00,000, risk = 1% = ₹5,000 per trade. For the Nifty demand example from Chapter 50 (115-point stop):
- Rupees at risk per lot = 115 × 75 = ₹8,625 — that is *more* than our ₹5,000 budget for a single lot.
- Therefore this trade is **too large for one full lot** at 1% risk. Options: (a) skip it, (b) use MIS/hedged margin and accept the position but reduce elsewhere, or (c) express it with a defined-risk option spread whose max loss is ≤ ₹5,000.

This is where most retail traders quietly blow up: the index lot size forces a risk larger than their per-trade budget, so they either over-leverage or ignore sizing. A ₹5,000-risk trader on a 115-point Nifty stop genuinely cannot take one clean futures lot — and the honest answer is to trade a **bull call/put spread** or wait for a tighter zone with a 50–60 point stop.

**Costs to bake in (per round-trip, representative):**
- Brokerage: ₹20 flat per order (discount broker) → ₹40 round trip.
- STT: higher on the sell side; on options STT is on premium, on futures on turnover.
- Exchange txn charges, SEBI fee, GST on brokerage, stamp duty.
- **Slippage:** on Bank Nifty options this is the silent killer — a ₹2–5 spread on entry and exit can equal ₹70–175 per lot. Zones near round numbers have better liquidity; deep OTM strikes have brutal spreads.

Rule of thumb: assume **₹150–300 of frictional cost per Bank Nifty option round-trip** and demand that your edge clears it comfortably. A 3:1 chart trade with a ₹1,575 risk easily clears ₹300 of friction; a scalp for 20 points does not.

## Backtest and edge notes — the honest picture

Naive S&D rules (buy every fresh demand zone in an uptrend, 3:1 target) tend to show, in Indian index backtests, a **win rate around 40–50% with average R:R near 2.5–3:1**, which is net profitable *if* discipline holds. But three caveats destroy most of the paper edge:

1. **Definitional sensitivity.** Change "explosive departure" from "2 large candles" to "3 large candles" and results swing wildly. The edge is fragile to parameter choice — a red flag for over-fitting.
2. **Much of the edge is just trend-pullback.** Strip out the trend-alignment filter and the zone edge collapses toward random. S&D largely *is* a disciplined pullback-buying framework; the zone is the entry-timing tool, the trend is the actual edge.
3. **Costs and slippage** eat a large share, especially on options and intraday.

Traded honestly — A+ zones only, with-trend, 3:1 gated, 1% risk, futures or spreads to preserve R:R — S&D is a legitimately profitable *discretionary* method. Sold as a mechanical holy grail, it is not. Grade it, gate it, size it, and it works.

## Adaptations for NSE / F&O

- **Nifty (calm, trends smoothly):** zones respected cleanly; set-and-forget works well; 15–25 point stop buffers.
- **Bank Nifty (violent, overshoots):** always use confirmation entries and wider buffers (40–60 pts); expect zones to be probed deep before reacting; smaller size, expiry-day chaos ignores zones.
- **Fin Nifty / Midcap:** thinner; zones on 15-min+ only; avoid scalping thin liquidity.
- **Stock F&O:** zones respect *event risk* poorly — earnings blow through zones. Check the event calendar; never hold a zone trade over results.
- **MCX (Crude, Gold, Silver):** S&D works well on commodities because they trend; mind the international session (Crude reacts to US inventories, NY hours); use 15-min/60-min zones and wider stops for volatility.
- **USDINR:** RBI-managed, low volatility, tight ranges — zones are small and mean-reverting; a specialist, low-R:R play.
- **Options layering:** overlay demand zones with **Put OI walls** (put writers = support) and supply zones with **Call OI walls** (call writers = resistance). When your zone and the OI wall coincide, you have chart + order-flow agreement — the highest-conviction Indian setup.

## Pitfalls specific to the system

1. **Grading inflation.** It is tempting to award confluence points generously to justify a trade you already want. Score *before* you feel the urge, and be stingy.
2. **Options R:R illusion.** As shown, a 3:1 chart trade can be a 2:1 option trade after theta/IV. Compute the option payoff, do not assume the chart R:R.
3. **Sizing denial.** Index lot sizes frequently exceed a 1% risk budget. Do not fudge it — spread or skip.
4. **Expiry-day and event blindness.** Zones are noise on Bank Nifty expiry afternoons and around results/RBI/Fed. Sit out.
5. **Moving the stop.** The distal-close invalidation is sacred. Widening a stop because "it's about to turn" is how a ₹5,000 risk becomes a ₹25,000 loss.
6. **Revisiting stale zones.** Fresh-first. A third-touch zone is a coin flip; treat it as such or skip.

## Interview-ready summary

- The professional S&D **system** is: top-down zone marking (daily → refine on LTF), a **zone scorecard** (departure, tightness, freshness, trend alignment, time away, confluence), and a strict **3:1 R:R gate**.
- **Two entries:** Protocol A set-and-forget limit at the proximal line (A+ zones, hands-off) and Protocol B lower-timeframe confirmation/CHoCH (B zones, volatile instruments like Bank Nifty).
- **Stop** beyond the distal line + buffer; invalidation is a *candle close* through distal. **Targets** laddered — T1 at nearest opposing structure (book half, move to break-even), runner trailed on structure.
- **Position sizing** at 1% risk, worked backward from the stop; index lot sizes often exceed the budget → use **spreads or skip**. Bake in **₹150–300 option friction** per Bank Nifty round-trip.
- **Options do not preserve chart R:R** (theta/IV) — trade futures or deep-ITM for linear payoff, ATM only when also betting on volatility.
- **India adaptations:** Nifty clean, Bank Nifty overshoots (confirmation only), avoid events/expiry, overlay **Put/Call OI walls** for chart+order-flow confluence.
- **Honest edge:** disciplined trend-pullback timing with excellent R:R — real when graded, gated, and sized; a myth when treated as a mechanical holy grail.

Chapter 52 takes the same order-imbalance intuition into the ICT vocabulary — order blocks and fair value gaps — which formalise the "where did the move originate and where is the inefficiency" question with a different, precise ruleset.
