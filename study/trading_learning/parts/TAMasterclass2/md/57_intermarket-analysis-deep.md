# Intermarket Analysis (Deep)

## What it is & why it works

Intermarket analysis is the study of how different asset classes — equities, bonds, currencies and commodities — pull on each other. No market trades in a vacuum. When the US Dollar strengthens, capital tends to leave emerging-market equities and commodities priced in dollars weaken. When crude oil spikes, India's import bill and inflation rise, the rupee weakens, and rate-sensitive sectors like autos and NBFCs feel it. A technician who charts only Nifty and its RSI is reading a single instrument in the dark. An intermarket analyst reads the whole room — the flows of global money that decide whether a Nifty breakout has a tailwind or a headwind behind it.

The discipline was popularised by John Murphy in the 1990s, whose four core relationships (dollar–commodities, commodities–bonds, bonds–stocks, stocks–business cycle) remain the backbone. But India adds its own overlays: heavy dependence on imported crude, a persistent current-account deficit, foreign portfolio investor (FPI) flows that swing the rupee and the index in tandem, and a domestic institutional (DII) base that increasingly absorbs FPI selling. Understanding these lets you answer the question that pure single-chart TA cannot: *is this move supported by the broader macro tape, or is it swimming against the tide?*

Why does it work? Because capital is fungible and moves along paths of least resistance and highest expected return. A rising US 10-year yield raises the global cost of money and the discount rate applied to every risk asset; a falling one does the opposite. These are not folklore correlations — they are cash-flow and arbitrage mechanics. The relationships are probabilistic and regime-dependent, not laws of physics; correlations break, invert and re-form. That is precisely why you chart them rather than assume them.

## The core relationships that matter for India

**US Dollar Index (DXY) ↔ Nifty & rupee.** This is arguably the single most important intermarket relationship for an Indian trader. A strong dollar (DXY rising toward 106–108) typically coincides with FPI outflows, a weaker rupee (USDINR rising toward 84–85+), and pressure on Nifty. A falling DXY (toward 100–102) is a risk-on signal: dollars flow into EM, USDINR firms, and Nifty tends to rally with FPI buying. Track DXY on TradingView (`TVC:DXY`) alongside `FX_IDC:USDINR` and Nifty. The correlation is inverse between DXY and Nifty and positive between DXY and USDINR.

**Crude oil (Brent / MCX Crude) ↔ India macro.** India imports roughly 85% of its crude. Brent above $90–95 is a structural headwind: it widens the trade deficit, pressures the rupee, stokes CPI, and hurts oil-marketing companies (BPCL, HPCL, IOC on their marketing margins), paint makers (Asian Paints, whose input is crude derivatives), tyre makers, aviation (InterGlobe/IndiGo) and logistics. Brent below $75 is a tailwind — the "crude dividend." Chart `TVC:UKOIL` (Brent) or `MCX:CRUDEOIL1!` and overlay it mentally on Nifty and the rupee.

**US 10-year Treasury yield ↔ India 10-year G-Sec ↔ rate-sensitives.** Global yields set the risk-free anchor. When the US 10Y (`TVC:US10Y`) rises sharply, the yield differential with India narrows, making the carry trade less attractive; FPIs in debt and equity trim exposure. India's own 10-year G-Sec yield (around 6.4–7.0% in the 2024–26 window) drives banks, NBFCs, real estate and autos. Falling yields = cheaper money = rate-sensitive rally. Rising yields compress valuations of high-P/E growth names (IT, new-age tech) the most.

**Gold (MCX Gold) ↔ risk sentiment & real yields.** Gold is the fear-and-real-yield asset. It rises when real yields fall, when the dollar weakens, and when geopolitical or systemic fear spikes. For the Indian trader gold is both a macro barometer and a tradeable MCX instrument. A gold breakout to new highs alongside a falling DXY and rising equities is the "everything rally" of debased-money regimes; gold rising while equities fall is classic risk-off flight to safety.

**FPI/DII flows ↔ Nifty & Bank Nifty.** This is India's own intermarket layer. FPI daily/monthly cash-market figures (published by NSDL and exchanges) are the closest thing to a flow gauge. Sustained FPI selling (₹10,000–30,000 cr in a month) usually caps rallies and weakens the rupee; DII buying (SIP-driven, sticky) provides a floor. Bank Nifty is the highest-beta expression of FPI flows because financials are the largest FPI holding. When you see FPIs selling but Nifty holding, DIIs are absorbing — a tell that dips are being bought.

## Mechanics — how to read and quantify the linkages

Intermarket analysis is done two ways: visually (overlay and ratio charts) and quantitatively (rolling correlation).

**Overlay charts.** On TradingView, add a comparison symbol: pull up Nifty, then "Compare" and add `TVC:DXY` inverted, or `TVC:UKOIL`. Watch for divergence — when two normally-linked markets pull apart, a resolution is coming.

**Ratio charts.** Ratios strip out the broad market and reveal relative strength. Key India ratios to keep on a watchlist:
- **Bank Nifty / Nifty** — when rising, financials lead and the rally is broad and healthy; when falling, leadership is narrow (often IT/pharma defensives leading).
- **Nifty / Gold (in ₹)** — equities vs. hard money. Rising = risk-on, real-economy optimism.
- **Nifty Auto / Nifty** and **Nifty IT / Nifty** — sector rotation gauges.
- **Midcap / Nifty (or Nifty Next 50 / Nifty)** — breadth and risk appetite. Rising midcap ratio = risk-on froth; falling = flight to large-cap quality.

**Rolling correlation.** Add the "Correlation Coefficient" indicator on TradingView (built-in), set the source symbol to `TVC:DXY` and length to 20 or 50. When the reading sits at −0.6 to −0.8, the inverse DXY–Nifty relationship is "on" and can be traded. When it drifts to zero, the relationship has decoupled — do not lean on it. This is the single most important discipline in intermarket work: **verify the correlation is active before you use it.**

## Worked India example (levels & ₹)

Consider a reconstructed setup from a typical 2024–25 risk-off episode (verify exact levels on your charts; these are approximate).

Nifty is trading at 24,300 after a run to an all-time high near 24,850. Over ten sessions the following stack builds:

- **DXY** rises from 104.2 to 106.5 — a decisive break above its 100-day average.
- **USDINR** climbs from 83.4 to 84.3, a fresh record, confirming rupee weakness.
- **Brent** jumps from $78 to $88 on a Middle-East flare-up.
- **US 10Y** ticks up from 4.1% to 4.4%.
- **FPI cash data** shows nine straight sessions of net selling totalling roughly ₹28,000 cr.

Each factor individually is a mild negative; stacked, they form a coherent risk-off intermarket signal. The rolling DXY–Nifty correlation reads −0.72 — the relationship is active. On the Nifty chart, price is now testing the 24,000 round number and the 50-day EMA (~24,100).

**The intermarket read:** a breakdown below 24,000 is far more likely to follow through than a random dip, because it is being *driven* by dollar strength, crude, rising yields and confirmed FPI selling — not by an isolated candle. This is confluence across four asset classes plus flows.

**The outcome (reconstruction):** Nifty loses 24,000, slides to the 200-day EMA near 23,300 over the next two weeks. The bounce comes only when Brent rolls back under $82, DXY stalls at 106.5, and FPI selling slows — the same intermarket stack that flagged the fall now flags the floor.

## How to trade it (entry / stop / target)

Intermarket analysis rarely gives you the precise entry candle — it gives you *bias and conviction*. You still execute on the price chart. The workflow:

1. **Set macro bias from the intermarket stack.** Score the four-to-five relationships as risk-on (+1), neutral (0) or risk-off (−1). A net score of −3 or worse means fade rallies and size shorts fuller; +3 or better means buy dips with conviction.
2. **Wait for the price trigger on Nifty/Bank Nifty** that agrees with the bias — a break of a level, a candle signal, an EMA reclaim.
3. **Entry:** on the price trigger, in the direction of the macro stack. In the example above: short Nifty futures on the close below 24,000, or buy 24,000 puts / put spreads.
4. **Stop:** above the invalidation of the price structure (e.g., 24,350, back above the 50-EMA), *and* mentally invalidate if the intermarket stack flips — Brent collapses, DXY reverses hard.
5. **Target:** the next structural level supported by the flows — 23,300 (200-EMA) in the example, trailing if the stack stays risk-off.

**Position sizing scales with intermarket confluence.** A price setup with the full macro stack behind it earns a larger position than the same setup fighting the tape.

## Confluence (including OI)

Intermarket signals become high-probability when they align with the domestic derivatives picture.

**Option chain confluence.** In the risk-off example, check the Nifty option chain: if max pain is drifting lower, put writers are unwinding at 24,000 (support giving way) and call writing is stacking at 24,000–24,200 (resistance forming just overhead), the OI structure *confirms* the intermarket-driven downside. Heavy call OI addition at a level that intermarket analysis flags as resistance is a powerful double-confirmation. Conversely, if put writers are aggressively defending 24,000 even as the macro stack turns risk-off, expect a fight — reduce size.

**India VIX.** VIX rising through 14–16 alongside a risk-off intermarket stack tells you the options market agrees fear is building; VIX crushed under 12 during a risk-off stack is a warning that the equity market is complacent and the eventual move may be sharp.

**Sector selection via intermarket.** Once bias is set, use intermarket logic to pick the *instrument*. Risk-off from crude? Short auto/aviation/paints, avoid oil marketers. Risk-off from rising yields? Short high-P/E IT and new-age names, favour or hedge with defensives. A weak rupee? Long IT and pharma exporters (they earn in dollars) as a relative-strength trade even in a soft tape — a classic intermarket pairs idea (long Nifty IT / short Nifty on a weak-rupee, weak-market day).

## Pitfalls

**Assuming correlations are constant.** The dollar–Nifty inverse relationship weakens or flips for stretches. In some phases a strong dollar coexists with a rising Nifty because the strength is driven by US growth (good for global risk) rather than US stress. Always check the rolling correlation before trading the assumption.

**Lag and lead confusion.** Bonds often lead stocks; commodities can lead bond yields. But leads shift by regime. Do not mechanically assume "yields up therefore stocks down today" — the transmission can take weeks and can be overwhelmed by earnings or liquidity.

**Over-fitting a narrative.** It is easy to construct a story where every market confirms your bias. Discipline: require the *majority* of relationships to align and the correlation to be statistically live. One asset moving your way is a data point, not a thesis.

**Ignoring domestic flows.** Global intermarket signals in India are routinely absorbed by sticky DII/SIP flows. A textbook risk-off global tape has repeatedly failed to break Nifty because domestic buying is structural. Weight FPI-vs-DII net flow heavily.

**Timeframe mismatch.** Intermarket relationships are strongest on daily/weekly charts. Using them to time a 5-minute Bank Nifty scalp is noise. Match the intermarket timeframe to your trade horizon.

**Data timing.** FPI cash figures are provisional intraday and final next day; the DXY and crude trade in different sessions. Be aware you are stitching together markets that close at different times, so overnight gaps carry intermarket information.

## Building an intermarket dashboard

Keep a single TradingView layout or watchlist with, at minimum: Nifty, Bank Nifty, `TVC:DXY`, `FX_IDC:USDINR`, `TVC:UKOIL` (Brent), `MCX:GOLD1!`, `TVC:US10Y`, India 10Y G-Sec yield, India VIX, and the Bank Nifty/Nifty and Midcap/Nifty ratios. Add rolling-correlation panes for DXY-vs-Nifty and Crude-vs-Nifty. Glance at it every morning before the open and score the risk-on/risk-off stack. This 60-second ritual reframes every intraday decision: you now know whether you are trading with the global tide or against it.

Layer on the flow data weekly: FPI vs DII net equity numbers, FPI debt flows, and the FPI derivatives long-short ratio (the index-futures net position of FIIs, available in the daily participant-wise OI report). When FIIs are net-long index futures and buying cash, and the intermarket stack is risk-on, that is your highest-conviction long environment. When they are net-short futures, selling cash, and the stack is risk-off, fade every rally.

## Interview-ready summary

Intermarket analysis reads equities in the context of currencies, bonds and commodities because global capital is fungible and flows to the best risk-adjusted return. For India the key linkages are: a strong US Dollar (DXY) and weak rupee pressuring Nifty via FPI outflows; high crude (Brent >$90) widening the deficit and hurting rate-sensitives, autos, paints and aviation; rising US and Indian 10-year yields compressing valuations, especially of high-P/E growth names; and gold acting as the real-yield and fear barometer. Domestically, FPI-vs-DII flows are the decisive overlay — sticky SIP-driven DII buying repeatedly absorbs global risk-off. The core discipline is to verify the correlation is *active* (rolling correlation of −0.6 to −0.8, say, for DXY–Nifty) before trading the assumption, because these relationships are regime-dependent, not constant. In practice, intermarket analysis sets *bias and position size*, not the exact entry: score the four or five relationships risk-on/risk-off, wait for a price trigger on the chart that agrees, confirm with the option chain (call/put OI at the flagged levels) and India VIX, and size up when the macro stack, the price structure and the OI all point the same way. The classic worked case: DXY breaking higher, USDINR at record, Brent spiking, US 10Y rising and FPIs selling nine sessions straight, all while the DXY–Nifty correlation reads −0.72 — a coherent risk-off stack that turns a routine test of 24,000 into a high-probability breakdown toward the 200-EMA. Read the whole room, not one chart.
