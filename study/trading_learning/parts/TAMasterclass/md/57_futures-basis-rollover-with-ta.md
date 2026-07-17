# Futures Basis & Rollover with TA

## What it is & why it works

In the Indian derivatives market almost every liquid instrument you trade — Nifty 50, Bank Nifty, Fin Nifty, and hundreds of single stocks — trades in **two parallel prices at once**: the cash/spot price and the futures price. The gap between them is the **basis**. Formally, basis is usually written as *futures minus spot* (F − S), though old textbooks flip it to spot minus futures, so always state your convention. When the future trades **above** spot, the market is in **contango** and the basis is positive (a *premium*). When the future trades **below** spot, the market is in **backwardation** and the basis is negative (a *discount*).

Why does the gap exist at all, and why does it move? The theoretical anchor is the **cost-of-carry model**: `F = S × e^(r−d)×t`, where `r` is the financing/interest rate, `d` is the dividend yield of the stock or index over the contract's life, and `t` is time to expiry in years. Because Indian equity index dividends are modest and interest rates positive, index futures *should* trade at a small premium that **decays to zero by expiry** — on expiry day, the future must converge to spot because it settles at the spot closing value (the NSE settlement price). That guaranteed convergence is the single most important fact about basis: **the premium is a melting ice cube.**

But the *realised* basis rarely equals the fair-value basis, and that deviation is pure sentiment and positioning information. When aggressive longs pile into Nifty futures, they bid the premium *above* fair value — the market pays extra to be long. When fear dominates and hedgers/short-sellers dump futures, single stocks and even indices can fall into **discount** — futures trade *below* spot, which is a classic sign of a nervous, hedged, or oversold market. So basis is a **positioning gauge layered on top of price**, and that is why a technical analyst cares: TA reads price structure, and basis + rollover data tell you *who* is behind that structure and *how committed* they are.

**Rollover** is the second half of the story. Indian F&O contracts expire monthly (indices moved to weekly/monthly cycles, but the *big* positioning contract is still the monthly). As the current-month (near) contract nears expiry, traders who want to keep a position must **close the near contract and reopen it in the next month** — that is a *rollover* or *roll*. The **rollover percentage** (open interest rolled to next series ÷ total OI) and the **roll cost** (the spread you pay to shift, roughly next-month price minus near-month price) are published and watched obsessively during the last three sessions before expiry. High rollover into a rising market = conviction longs carrying forward. High rollover in a falling market = shorts staying short. Low rollover = positions being *booked and abandoned*, i.e. a trend running out of committed players.

The behavioural logic: futures are where **leveraged, informed, professional money** expresses conviction. Basis and rollover are the fingerprints that money leaves. Price alone can't tell you whether a breakout is backed by fresh committed capital or by short-covering that will exhaust; basis and rollover can.

## The mechanics

**Basis, precisely.** Take Nifty spot at 24,000 and Nifty near-month future at 24,090. Basis = +90 points, a premium. Annualise it to compare across time: `implied cost = (F/S − 1) × (365/days_to_expiry)`. With 20 days left: `(24090/24000 − 1) × (365/20) = 0.375% × 18.25 ≈ 6.8%` annualised — roughly the risk-free-minus-dividend fair value, so this basis is *normal*. If the same 20-days-out future traded at 24,180 (+180), the annualised carry jumps to ~13.7% — that is an **over-heated premium**, a crowd of leveraged longs, and a caution flag for chasing.

**Basis states table:**

| State | F vs S | Basis sign | Typical meaning | TA use |
|---|---|---|---|---|
| Normal contango | F slightly > S | small + | Healthy carry, orderly | Neutral; baseline |
| Rich premium | F well > S | large + | Crowded longs, leverage high | Fade euphoria / trail tight |
| Flat / near zero | F ≈ S | ~0 | Balanced or expiry near | Read with rollover |
| Discount (backwardation) | F < S | negative | Fear, heavy hedging, short pressure | Contrarian long alert if oversold |
| Deep discount | F << S | large − | Panic / forced hedging / dividend-heavy stock | Capitulation watch |

**Note on single stocks:** heavy expected **dividends** legitimately push a stock future into discount (the `d` term), so *always separate dividend-driven discount from fear-driven discount* by checking the ex-dividend calendar. A discount with no dividend due is sentiment; a discount straddling an ex-date is arithmetic.

**Rollover, precisely.** Reported metrics during expiry week:

| Metric | Definition | What high reading implies |
|---|---|---|
| Rollover % | Next-series OI ÷ (near + next OI) rolled | Conviction to carry position forward |
| Roll cost / spread | Next-month price − near-month price (in points or %) | Cost/appetite to stay positioned |
| Rollover vs 3-mo avg | Current roll % minus average of last 3 expiries | Above avg = stronger-than-usual commitment |
| Market-wide roll | Aggregate F&O roll across stocks | Broad risk appetite |

Nifty monthly rollovers typically run **75–80%**; Bank Nifty often **70–78%**. A roll **meaningfully above** the 3-month average with a **rising roll cost** in an *uptrend* is bullish continuation fuel. A roll *below* average as price stalls says the trend lacks fresh carry.

**Where to see it:** NSE option-chain and F&O reports, broker terminals (Kite, etc.), and rollover dashboards on TradingView/Chartink-style tools. Practically, watch the **near-month premium/discount live** (it ticks every second) and the **rollover % on T-2, T-1, expiry day**.

## Reading it — a worked India example

Let's walk a realistic **Bank Nifty** sequence across an expiry cycle. Numbers are illustrative but internally consistent.

**Phase 1 — mid-cycle base (15 days to expiry).** Bank Nifty spot is grinding sideways at **52,000**, coiling in a symmetrical triangle on the daily chart after a prior uptrend. Near-month future sits at **52,140** — a +140 premium, annualised ~6.5%, i.e. *normal contango*. Nothing unusual; TA says "wait for the triangle to resolve." Basis adds no urgency yet.

**Phase 2 — the breakout (8 days to expiry).** Price breaks the triangle's upper trendline at **52,400** on strong volume. A pure price trader buys the breakout. But watch the basis: as the breakout prints, the future jumps to **52,700** while spot is 52,400 — premium widens to **+300**, annualised carry spikes toward ~13%. Simultaneously, the day's **futures OI rises ~9%** with price. **Interpretation:** fresh **long build-up** (price up + OI up + premium expanding) — this is *committed leveraged buying*, not a hollow move. Confluence is bullish; the breakout has fuel. You size the trade normally, stop just below the breakout level at 52,150.

**Phase 3 — the push and the warning (4 days to expiry).** Bank Nifty runs to **53,600**. Premium, however, has **collapsed to +90** even though price is higher — and crucially, this is *not* just expiry decay (there are still 4 days; fair premium should be ~+180). A shrinking premium *into a rising market* means the marginal buyer at the top is the **cash market / short-coverer**, not fresh futures longs; leveraged conviction is quietly leaving. This is a **negative basis divergence** — a caution flag layered on an otherwise strong chart. You tighten your stop to 53,050 (below the last intraday higher-low) rather than adding.

**Phase 4 — expiry-week rollover verdict (T-1).** Rollover data prints: Bank Nifty roll **68%, below its 3-month average of 74%**, and the roll cost has *narrowed*. Translation: a chunk of the longs that drove Phase 2 are **booking profits and NOT carrying forward**. Combined with the Phase-3 premium divergence, the message is coherent: **the up-leg is mature and under-committed.** Price is still at 53,500, but the *positioning* has hollowed out.

**Phase 5 — resolution.** On the new series, with fewer carried longs to support it, Bank Nifty stalls at 53,600, fails to make a new high, and mean-reverts to **52,900** over the next three sessions. Your trailed stop at 53,050 takes you out with the bulk of the move captured. The basis/rollover read didn't predict the exact top — TA never does — but it *shifted the probabilities* and made you a trailer/booker instead of an adder at exactly the wrong moment.

## Trading it

**Setup A — Confirmed-conviction breakout (highest probability).** Price breaks a well-defined level *and* OI rises *and* premium expands (or discount narrows toward premium). 
- **Entry:** on the breakout close or a shallow retest of the level. 
- **Stop:** below the breakout / retest structure (Phase 2 example: 52,150). 
- **Target:** measured move of the pattern (triangle height projected), trailed as long as premium and OI hold up. 
- **Management:** as long as OI *rises with price and premium stays firm*, ride and trail below successive higher-lows. The *moment* premium diverges (Phase 3), stop adding and tighten.

**Setup B — Basis-divergence exit / fade.** Price makes a new high (or new low) but **basis diverges** (premium shrinks on new highs / discount deepens then price makes new low with waning momentum). 
- **Action if long:** book/trim, tighten stop to the last swing low. Do *not* short on divergence alone — divergence is a *warning*, not a trigger. 
- **Fade trigger (aggressive):** only after price *also* breaks a short-term structure (e.g., loses the prior higher-low) do you consider a counter-trade, stop above the failed high.

**Setup C — Discount-driven contrarian long.** A quality stock/index in **fear-driven discount** (no dividend due), price sitting on a major support with a bullish reversal candle (hammer/bullish engulfing), and OI *falling* (short-covering setup) or a fresh oversold RSI. 
- **Entry:** reversal candle confirmation off support. 
- **Stop:** below the support / candle low. 
- **Target:** prior swing / VWAP mean-reversion. The discount tells you shorts are crowded and vulnerable to a squeeze; the chart tells you *when*.

**Setup D — Rollover-based trend continuation.** On the new series, if rollover printed **above average with rising cost in the direction of the trend**, treat pullbacks to moving-average/support as *buy-the-dip* (uptrend) opportunities — the committed carry supports continuation. If rollover was *below* average, treat rallies/pullbacks with suspicion and favour range/mean-reversion tactics.

**Position sizing note:** basis richness is a *volatility/leverage* signal. When premium is extremely rich (crowded), reduce size — crowded leverage unwinds violently. When basis is calm/normal, standard size.

## Confluence

Basis and rollover are **positioning overlays**; they shine when stacked with price and option data:

- **Price + OI + basis (the core triad).** Price up + OI up + premium expanding = *strong long build-up* (best continuation odds). Price up + OI down + premium shrinking = *short-covering rally* (fragile, fade-prone). Price down + OI up + slipping into discount = *strong short build-up* (bearish continuation). Price down + OI down = *long unwinding* (selling exhausts, watch for bottom). Memorise this 2×2 — it is the backbone of derivatives TA.

- **Rollover + trend structure.** Above-average roll in the trend direction validates a *continuation* read on the chart (higher-highs/higher-lows). Below-average roll at a chart resistance = *distribution* risk.

- **Basis + option-chain PCR & Max Pain.** A rich futures premium alongside heavy **call writing** overhead and a Max Pain *below* spot warns of a crowded, top-heavy long positioning that expiry gravity may drag down. Discount + heavy **put writing** at support = bullish base being built by option sellers *and* futures hedgers unwinding.

- **Basis + India VIX.** Rising VIX with a **collapsing premium into discount** is the fingerprint of a genuine risk-off scramble (hedgers shorting futures, premium paid for puts). That combination upgrades a bearish chart from "pullback" to "potential trend change."

- **Basis + delivery/cash-market data (stocks).** A stock future flipping to discount *with rising delivery percentage* in the cash market can mean genuine investors accumulating while leveraged traders exit — a bullish divergence between "smart cash" and "nervous leverage."

The rule: **let the chart pick the level and the trigger; let basis/rollover/OI grade the conviction and size.**

## Pitfalls & false signals

1. **Confusing decay with divergence.** Premium *naturally* shrinks toward zero every single day as expiry approaches. A falling premium on T-2 is mostly *time*, not sentiment. Always compare against the *fair-value premium for the remaining days*; only the deviation from fair value is information. Do your divergence reads **mid-cycle**, not on expiry eve.

2. **Dividend discount ≠ fear discount.** A single-stock future in discount around an ex-dividend date is pure arithmetic. Check the corporate-action calendar before you read "fear."

3. **Illiquid single-stock futures.** Basis in thin stock futures can be noisy, wide, and stale. Rollover and basis signals are reliable in **Nifty, Bank Nifty, Fin Nifty and top-liquidity stocks**; treat mid/small-cap F&O basis with heavy skepticism.

4. **Rollover % without context.** A "high" roll number means nothing in isolation — 72% might be *low* for Nifty but *high* for a specific stock. Always compare to that instrument's own 3-month average, and read roll % *together with roll cost and the trend direction* (high roll can be conviction longs *or* trapped shorts refusing to exit).

5. **Divergence is a warning, not a short trigger.** Countless traders short a strong index just because premium shrank — and get run over as price grinds higher for days. Basis divergence should make you *trail and trim*, and you enter a counter-trade only after **price structure** also breaks.

6. **Expiry-day settlement games.** In the final hour, basis distorts around settlement mechanics and Max-Pain pinning. Don't extract sentiment signals from the last 60–90 minutes of expiry.

7. **Regime dependence.** In a strong bull regime, rich premiums can *persist* for weeks — fading every rich premium bleeds you. Basis is a *conditioning* variable to size and grade trades, not a standalone timing oscillator.

Pros filter these by (a) always normalising basis to annualised carry, (b) separating dividend from sentiment, (c) reading basis/OI/rollover as a *bundle* aligned with the chart, and (d) demanding a price-structure trigger before acting.

## Interview-ready summary

"**Basis** is the gap between the futures and spot price. By cost-of-carry, index futures should trade at a small premium that decays to zero by expiry, since the future settles at spot. When I annualise the premium and it runs *far above* fair carry, longs are crowded and leveraged; when a future — with no dividend due — slips into **discount**, that's fear and heavy hedging. I read basis alongside **open interest**: price-up-with-OI-up-and-premium-expanding is genuine long build-up and my highest-conviction continuation; price-up-with-OI-down-and-premium-shrinking is a hollow short-covering rally I don't chase. **Rollover** — the % of OI carried to the next series and the roll cost — tells me whether the committed money is staying: above-average roll with rising cost in the trend direction is continuation fuel; below-average roll as price stalls warns of an under-committed, distribution-prone move. Crucially, I do divergence reads *mid-cycle*, not on expiry eve, because premium naturally decays; I compare rollover to the instrument's own 3-month average; and I treat basis divergence as a signal to *trail and trim*, never as a standalone short trigger — I still need the price structure to break. In one line: the chart picks the level and trigger, basis and rollover grade the conviction and set my size."
