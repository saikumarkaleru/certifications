# Silver TA (Deep)

If gold is the patient monarch of the commodity screen, silver is its volatile younger sibling — same royal bloodline, half the discipline. Silver moves with gold, but harder, later, and with far more whipsaw. On the MCX it is the instrument that makes the fastest fortunes and destroys the most over-leveraged accounts, because traders who learned position sizing on gold walk into silver's double-the-volatility world and get run over. This chapter treats silver on its own terms: its dual identity as precious-and-industrial metal, the levels and behaviour that repeat, the setups that work, a full worked trade, and the risk architecture silver demands.

## The instrument's character and its real drivers

MCX Silver is quoted in rupees per kilogram. The big contract (SILVER) is 30 kg — one rupee of price move is 30 rupees P&L, and near 2026 prices around 90,000-1,10,000 per kg, a 30 kg lot is roughly 27-33 lakh rupees of notional. That is enormous leverage for a retail account. The mini contracts are essential: **SILVERM (SilverMini, 5 kg)** where one rupee = 5 rupees P&L, and **SILVERMIC (SilverMicro, 1 kg)** where one rupee = 1 rupee — the correct starting size for almost everyone.

Like gold, MCX silver is a derived price:

```
MCX Silver (per kg)  ≈  Spot Silver ($/oz) × USDINR × (1000 / 31.1035) × (1 + duty + premium)
```

So the same three forces apply — dollar silver, USDINR, and duty. But silver has a **fourth driver that gold lacks: industrial demand.** Roughly half of silver's demand is industrial — solar photovoltaic panels, electronics, electric-vehicle wiring, batteries, and increasingly the whole green-energy build-out. This gives silver a split personality:

- **Precious-metal mode.** It follows gold, real yields, and the dollar as a monetary/safe-haven asset.
- **Industrial mode.** It follows the manufacturing cycle, global growth expectations, copper, and the solar/EV story. Strong global PMIs and a copper rally can lift silver even when gold is flat.

Because of this dual demand and a much smaller, thinner global market than gold, silver is **structurally more volatile** — its daily percentage ranges routinely run 1.5x to 2x gold's. It also has a defining behavioural quirt on the ratio.

**The Gold-Silver Ratio (GSR)** is the single most useful silver-specific tool. It is simply:

```
GSR = Price of Gold (per oz) / Price of Silver (per oz)
```

Historically the GSR oscillates roughly between 50 (silver expensive relative to gold) and 90-100 (silver cheap relative to gold), with extreme spikes above 100 in panics. The trader's read: a **high GSR (85-100+) signals silver is historically cheap versus gold** — a mean-reversion tailwind for silver longs, especially when precious metals as a group are turning up. A **low GSR (below 55-60) signals silver is rich** and often precedes silver underperformance. Silver's biggest rallies happen when gold is rising AND the GSR is falling — silver outrunning gold to the upside, the classic "silver catches up and overtakes" move.

## Key levels and behaviour you must respect

- **Silver leads and lags gold, rarely trades in step.** In the early stage of a precious-metals rally, gold moves first and silver lags (skeptics call it "silver isn't confirming"). Then, late in the move, silver explodes and outpaces gold — the GSR collapses. Watching *both* charts tells you which stage you are in.
- **Whipsaw is the base case.** Silver fakes out of ranges far more than gold. A breakout that would be reliable on gold needs a *closing* confirmation and volume on silver, or you are the exit liquidity for a stop-run.
- **Round numbers on MCX** — 90,000, 1,00,000, 1,10,000 per kg — and international marks like $30, $35, $40 per ounce act as magnets and psychological battle zones. The $30/oz and the ₹1,00,000/kg levels in particular have been decade-defining shelves.
- **Overnight gaps are larger than gold's** because silver's overnight international range is bigger. The 9:00 AM MCX catch-up to COMEX silver can be violent.
- **The evening US-data window (5:00-9:00 PM IST)** is where silver's fireworks happen, amplified versus gold by the industrial-plus-monetary double sensitivity — silver reacts to US CPI/FOMC *and* to global growth data and copper.
- **ATR is your master variable.** Silver's ATR can double in a themed week. A rupee-stop that is prudent in a quiet fortnight is a coin-flip in an active one. Size off ATR, always.

## The best setups on silver

**Setup 1 — GSR mean-reversion swing.** When the GSR is stretched high (say 88-95) and precious metals are basing or turning up on the daily, go long silver (SILVERM/SILVERMIC) as the ratio compression play. This is a multi-day-to-multi-week positional trade. Confirmation: gold holding its daily 50 EMA, silver reclaiming its 20 EMA, GSR rolling over from its high. Stop below the recent silver swing low; the target is a lower GSR (silver outperforming), not just a rupee number.

**Setup 2 — Silver-catches-up momentum.** Mid-rally, when gold has already broken out and silver is coiling below its own resistance, position for the lagging-metal breakout. Silver's late-stage moves are its biggest. Enter on a *closing* break of the consolidation with expanding volume; trail aggressively because these moves are fast and reverse fast.

**Setup 3 — Event breakout-and-retest (evening).** Identical structure to gold's event play but with wider stops and smaller size because silver's reaction candles are larger. Let the CPI/FOMC candle print, wait for the retest of the broken level, enter on confirmation, stop beyond the spike.

**Setup 4 — Range fade with a hard flip rule.** In balanced macro, silver rotates in a wide rupee range. Fade the edges — but silver's range fades fail more often than gold's, so keep stops tight beyond the boundary and *flip to breakout* the instant a daily closes outside on volume. Never average into a losing silver range trade; that is the classic account-killer.

## A worked India example

It is a stretch of 2026 where precious metals are basing after a correction. Gold has stabilised above its daily 50 EMA. The GSR is elevated at ~90 — silver is historically cheap versus gold. Bias: *long silver for ratio compression.*

- **The read.** Spot silver $34.50, USDINR 87.4. SILVERM (5 kg) trading ~96,500 per kg. On the daily, silver has reclaimed its 20 EMA and printed a higher low. Gold is quietly grinding up. GSR at 90 and just starting to tick down — the compression trigger.
- **The entry.** Silver has been consolidating 95,800-97,200 for eight sessions. You buy SILVERM on a closing break above 97,200 at 97,350, on a day where volume expands and gold also closes up. Stop at 95,600 (below the consolidation and the 20 EMA). Risk = 1,750 points × 5 rupees = 8,750 rupees per SILVERM lot. (Note: this is already a large risk — a small account uses SILVERMIC at 1 rupee/point, risking 1,750 rupees instead.)
- **The move.** Over the next nine sessions the "silver catches up" dynamic plays out. Gold adds ~2%; silver adds ~7% as the GSR compresses from 90 toward 84. SILVERM runs 97,350 → 1,03,800.
- **Management.** You trail under the rising daily 10 EMA. First scale-out at 1,01,000 (2R), remainder trailed. A sharp two-day pullback to 1,01,900 holds above the 10 EMA. The trail finally triggers at 1,02,900 on a daily close below the 10 EMA after the GSR flattens near 84 — the compression thesis is complete, so you exit rather than hope.
- **Result.** Roughly +3,650 and +5,550 points on the two portions — around 24,000 rupees on 8,750 risk, ~2.7R, from a trade whose *edge was the ratio*, not a chart line in isolation.

The teaching point: the same chart break, taken when the GSR was already *low* (silver rich), would likely have fizzled or reversed. Silver breakouts are only high-probability when the intermarket context — gold's trend and the GSR's position — is on your side. Silver TA that ignores the GSR is half-blind.

## How to use silver for bias and timing

Silver is a **risk and reflation barometer.** Silver strongly outperforming gold (falling GSR) alongside a rising copper and firm global PMIs signals a *reflationary, growth-and-easing* regime — friendly to industrial and metal equities on the NSE (think metals, capital goods). Silver *underperforming* gold (rising GSR) while gold holds up is a *defensive* signal — safe-haven money is in gold but not yet chasing the industrial story, often a late-cycle or risk-off tell. So the GSR is not just a silver-trading tool; it is a macro regime gauge for your whole book.

For timing precious-metal moves, use the two-metal handshake: a rally you trust is one where gold leads *and* silver eventually confirms and outperforms. A precious-metals move where silver refuses to confirm is suspect and prone to failure.

## Pitfalls and risk notes specific to silver

- **Volatility is the whole game.** Silver's 2x-gold volatility means the *same rupee stop* is far more likely to be hit. Traders who size silver like gold blow up. Halve your gold size, at least, and size off silver's ATR.
- **Whipsaw and false breakouts.** Silver stop-runs both boundaries of a range before choosing a direction. Demand closing confirmation and volume; never trade silver breakouts on wicks.
- **Overnight gap risk is amplified.** Larger overnight international ranges mean larger MCX open gaps. A stop that looks safe at 11:00 PM can be leapfrogged at 9:00 AM. Size for the gap.
- **Liquidity is thinner than gold.** Spreads widen fast, especially in the big 30 kg SILVER contract late at night and near expiry. Use SILVERM/SILVERMIC and limit orders.
- **The industrial swing.** A collapse in global growth expectations (weak China PMI, recession fear) can crush silver even while gold holds on safe-haven demand — the GSR spikes and silver longs bleed. Watch copper and PMIs, not just the Fed.
- **Duty and Budget risk** apply exactly as with gold — an import-duty change reprices MCX silver overnight regardless of world silver.
- **Don't average down.** Silver's speed makes averaging into losers catastrophically fast. One planned entry, one stop, defined risk.
- **Expiry/rollover.** MCX silver contracts expire on a monthly cycle; roll to the liquid front month and avoid the thin last days.

## Interview-ready summary

MCX Silver is a rupee-denominated derivative of dollar-denominated global silver, driven by the same three forces as gold — spot silver, USDINR, and import duty — plus a decisive fourth: industrial demand (solar, EV, electronics). This dual precious-plus-industrial identity, combined with a smaller, thinner global market, makes silver structurally 1.5-2x more volatile than gold and far more prone to whipsaw and false breakouts. The indispensable silver-specific tool is the Gold-Silver Ratio: a high GSR (85-100+) flags silver as historically cheap and sets up mean-reversion longs, while silver's largest rallies come when gold is rising and the GSR is falling — the "silver catches up and overtakes" dynamic. Silver typically lags gold early in a precious-metals rally and outruns it late, so the two-metal handshake is your timing tool. Best setups: GSR mean-reversion swings, the lagging-metal catch-up breakout, event breakout-and-retest, and cautious range fades with a hard flip-to-breakout rule. The defining risks are silver's own volatility (never size it like gold), amplified overnight gaps and whipsaw, thinner liquidity, the industrial-demand swing that can decouple it from gold, and Budget-day duty shocks. Trade silver only when gold's trend and the GSR are on your side, size off ATR in the mini/micro contracts, demand closing confirmation, and never average a losing silver position.
