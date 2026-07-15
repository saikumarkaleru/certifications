# Cross-Asset & Inter-Market Analysis

## Why this matters

Retail traders watch Nifty in a vacuum, as if the Indian equity index were an island. It isn't. Nifty at 9:15 is largely *pre-decided* by what happened overnight in the US, in crude, in the dollar, and in bond yields. The pro edge here isn't a secret indicator — it's *situational awareness*: knowing before the open whether the world woke up **risk-on** (buy equities, sell safe havens) or **risk-off** (dump equities, buy dollar/gold/bonds), and letting that set the day's *bias*. Your options and TA books teach you to trade a chart; this chapter teaches you to read the *weather system* the chart sits inside.

Honest limits: inter-market correlations are *regimes*, not laws. They shift, sometimes invert, and break in a crisis (in a real panic, *everything* except cash and the dollar can fall together). Use them for bias and context — never as a mechanical signal.

## The essentials

The core Indian cross-asset web (typical, regime-dependent relationships):

| Asset | Usual link to Nifty | Why |
|-------|--------------------|-----|
| **US markets (S&P 500 / Nasdaq)** | Positive, leads | Global risk sentiment; FIIs allocate globally; sets our gap |
| **SGX/GIFT Nifty** | Direct lead | Offshore Nifty trades before our open — signals the gap |
| **USDINR** | Inverse | Weak rupee → FII outflows, imported inflation → equity headwind |
| **Brent crude** | Inverse (India imports ~85% of oil) | High crude → CAD/inflation pressure; hurts OMCs, paints, aviation |
| **Gold (MCX / COMEX)** | Mild inverse / safe-haven | Rises in risk-off, when equities wobble |
| **US 10-yr Treasury yield** | Inverse (esp. for growth/IT) | Higher global yields → costlier capital, FII rotation out of EM |
| **India 10-yr G-sec yield** | Inverse | Rising domestic yields pressure rate-sensitives |
| **Dollar Index (DXY)** | Inverse to EM equities | Strong dollar drains EM flows |

**Risk-on signature:** US indices up, DXY down, crude *firm* on demand, gold soft, yields calm, USDINR stable/strong → constructive Nifty bias.
**Risk-off signature:** US down, DXY up, gold up, US yields spiking, USDINR weakening → defensive Nifty bias; expect gaps down and IT/rate-sensitive weakness.

**FII/DII flows** are the transmission mechanism — track daily FII cash & F&O figures (NSE/exchange). Sustained FII selling + weak rupee is a classic drag; DII buying often cushions it.

**Global calendar** (mark these — they move everything): US **Fed FOMC** (~8 times/yr), US **CPI/NFP** (monthly), **RBI MPC** (bi-monthly), Union **Budget (Feb 1)**, **US 10-yr auctions**, OPEC decisions, India **CPI/IIP**. On these dates, cross-asset moves dominate technicals. **Verify exact dates on RBI, Fed, and MoSPI calendars — they change.**

*All relationships as of 2026 and regime-dependent; verify current correlations yourself — they shift.*

## Worked example — reading the tape before a Nifty open

It's a July 2026 morning. Pre-open scan:

| Signal | Overnight reading | Bias contribution |
|--------|-------------------|-------------------|
| S&P 500 | −1.4% | Negative |
| Nasdaq | −2.1% (tech-led) | Negative — hits Indian IT |
| GIFT Nifty | 24,050 vs prev close 24,300 | Gap-down ≈ −250 pts |
| DXY | 105.8, +0.5% | Negative (dollar strong) |
| US 10-yr | 4.55%, +8 bps | Negative for growth/IT |
| Brent | $86, +2% | Negative (imported inflation, OMCs hit) |
| Gold (COMEX) | +0.9% | Confirms risk-off |
| USDINR | 83.60 → 83.85 | Rupee weak — FII-outflow risk |

**Read:** unanimous risk-off. Every needle points the same way — this is a *high-conviction* defensive morning, not a mixed tape. Expected: Nifty gaps down ~250 pts toward 24,050; **IT and rate-sensitives** (β to US yields) lead the fall; **OMCs, paints, aviation** pressured by crude; exporters/IT get a *partial* rupee cushion but the yield/Nasdaq drag dominates.

**Trade implication (bias, not a signal):** on such a morning a pro does *not* buy the gap-down dip reflexively — the whole world is selling risk. If already long, they'd have hedged the prior evening (2 Nifty futures short on a ₹25 L book, per the hedging chapter). If flat, they wait for the cash open, watch whether 24,050 (GIFT-implied floor) holds on volume, and only then decide. Notice the *disagreement test*: had crude been *down* and DXY flat, the signal would be muddier and conviction lower.

Contrast — a **risk-on** morning: S&P +1%, DXY −0.3%, yields easing, USDINR firming to 83.30, GIFT Nifty +180. Bias: gap-up, banks/autos/metals lead; a pullback into the gap is a *higher-probability* long than on the risk-off day. Same chart pattern, opposite context, opposite conviction — that's the entire point of inter-market work.

## How pros do it / common mistakes

**How pros do it**
- Run a **fixed pre-open dashboard** (below) every single morning *before* looking at Indian charts — context first, chart second.
- Look for **confluence**: when 6 of 8 signals agree, conviction is high; when they conflict, they size down or stand aside.
- Map signals to **sectors**, not just the index: crude → OMC/aviation; US yields → IT; rupee → exporters vs importers.
- Respect the **calendar** — flatten or hedge into FOMC/CPI/Budget; those days, macro trumps setups.
- Know correlations **decay and invert** — they re-test them each quarter rather than trusting a textbook sign.

**Common mistakes**
- Trading Nifty as if overnight global moves didn't happen — then getting run over by the gap.
- Treating a single correlation as gospel (e.g., "weak rupee always sinks Nifty" — not when IT/exporters lead).
- Fighting a unanimous risk-off tape with a "dip-buy" reflex.
- Ignoring the economic calendar and getting caught in an FOMC whipsaw.
- Assuming crisis correlations hold — in a true panic, diversification and normal inverses fail; only cash/USD are safe.

## Checklist / drill

**Pre-open cross-asset dashboard (run daily, 8:45–9:10):**

1. **US close** — S&P & Nasdaq %; tech-led or broad?
2. **GIFT/SGX Nifty** — implied gap vs prev close?
3. **DXY & USDINR** — dollar strong/weak; rupee direction?
4. **Brent crude** — level and % move (sector read: OMC/aviation)?
5. **US 10-yr yield** — up/down (IT/growth read)?
6. **Gold** — confirming risk-on/off?
7. **FII/DII flows** — prior day net cash & F&O?
8. **Calendar** — any Fed/RBI/CPI/Budget event today?

**Verdict:** count agree-vs-disagree signals → **risk-on / risk-off / mixed** → set today's bias and conviction size.

**Drill (10 sessions):** Each morning fill the 8-row dashboard, write a one-line verdict and expected Nifty direction *before* the open. After the close, mark whether the day matched. You'll learn which signals lead reliably (GIFT Nifty, US close) and which are noisy — and you'll stop trading Indian equities as if they were an island.

*Inter-market relationships and event dates current as of 2026 and regime-dependent — verify on NSE / RBI / Fed / exchange calendars; correlations change.*
