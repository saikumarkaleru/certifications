# Gold, Silver, Crude & Nat-Gas TA (MCX)

For the Indian technical trader, MCX (the Multi Commodity Exchange) opens a whole second market with a different clock, different drivers, and a different character from equities. Here you trade the physical world — the metal that central banks hoard, the fuel that runs the global economy — through rupee-denominated futures. The four giants are **Gold, Silver, Crude Oil, and Natural Gas.** Each is a distinct beast. This playbook covers what moves them, how the MCX contract works, the setups that repeat, and the confluences (global charts, the dollar, inventory data) that make MCX TA work. India-first, rupee-denominated, honest about risk.

## Why MCX is a different game

Three structural facts change how you must trade MCX versus Nifty:

1. **Extended hours.** MCX runs until late — the evening session historically extends to around 11:30 pm (11:55 pm in US daylight-saving months) for the internationally-linked commodities. This means MCX prices react in real time to the US session: the London gold fix, the NYMEX crude open, the US EIA inventory reports, and the US Fed. The most tradable moves in gold and crude often happen in the *evening* on MCX, not the morning. This is a night-owl's market.

2. **MCX is a rupee wrapper on a dollar asset.** MCX gold is essentially international gold (COMEX/spot, priced in USD per ounce) converted to rupees per 10 grams, adjusted for import duty and the USDINR rate. So an MCX gold chart embeds *two* variables: the global gold price **and** the rupee. Gold can be flat in dollars but rise on MCX purely because the rupee weakened. You must watch the international chart *and* USDINR to know which is driving your MCX candle.

3. **Contract sizes and leverage differ wildly by commodity.** The rupee-value-per-point and the lot size mean crude and natural gas can move your P&L far faster than gold per lot. Position sizing must be recomputed per commodity — a "normal" gold position size applied to natural gas is a blow-up waiting to happen.

## The MCX contracts, in brief

- **Gold** — the main contract is 1 kg (with Gold Mini 100 g and Gold Guinea/Petal for smaller sizes). Priced in rupees per 10 grams. The steadiest of the four — trends smoothly, respects levels, low intraday whip relative to the energies.
- **Silver** — main contract 30 kg (with Silver Mini 5 kg and Silver Micro 1 kg). Priced in rupees per kg. Silver is gold's high-beta cousin: it does what gold does, but 1.5-2.5x as violently, with a dual identity as both a monetary and an *industrial* metal.
- **Crude Oil** — 100 barrels per lot (Crude Mini 10 barrels). Priced in rupees per barrel, tracking WTI/NYMEX. The most headline-driven and geopolitically explosive of the four.
- **Natural Gas** — 1,250 mmBtu per lot (Natural Gas Mini 250 mmBtu). Priced in rupees per mmBtu, tracking Henry Hub. The wildest, most mean-reverting, most dangerous contract on the exchange — nicknamed "the widow-maker" globally for good reason.

## Gold: the trend-respecting store of value

Gold is the macro-anxiety and monetary asset. What drives it, in rough order:

- **US real interest rates and the Fed.** Gold pays no yield, so it competes with real (inflation-adjusted) bond yields. Falling real yields and dovish Fed expectations lift gold; rising real yields and hawkish Fed weigh on it. Fed decisions and US CPI prints are gold's biggest scheduled catalysts.
- **The US dollar (DXY).** Broadly inverse — a weaker dollar lifts dollar-priced gold.
- **Safe-haven demand.** Geopolitical crises, banking stress, and equity crashes send money into gold.
- **Central-bank buying** (a structural, multi-year bid) and **Indian festival/wedding demand** (a seasonal physical bid around Dhanteras, Diwali, and the wedding season).

Technically, gold is the **cleanest trender** on MCX. It respects moving averages, trendlines, and horizontal levels beautifully, and it forms textbook multi-week bases and breakouts.

### Worked gold example (approximate reconstruction — verify on your charts)

MCX Gold has been consolidating in a broad range, roughly ₹71,000-₹74,000 per 10 g, for several weeks, coiling above a rising 50-DEMA near ₹71,500. Internationally, spot gold is pressing a multi-month resistance, and the market expects a dovish Fed. On the Fed decision, spot gold breaks out; DXY drops; and MCX Gold gaps and closes above ₹74,000 on heavy evening-session volume — a base-breakout on a macro catalyst, with the rupee stable so the move is genuinely gold-driven.

The trade: enter long on the daily close above **₹74,000**, or on a controlled retest of it in the evening session, stop below **₹72,800** (back inside the range), first target the measured move of the ₹3,000 range projected to **₹77,000**, then trail with the 20-DEMA. Confluence: international spot gold confirming the breakout, DXY in a downtrend, real yields falling, and — for a positional hold — festival/wedding seasonal demand supportive. Because gold trends smoothly, this is a hold-and-trail trade, not a scalp. The main risk is a hawkish surprise reversing the Fed narrative, which would send you back inside the range fast.

## Silver: gold on steroids, plus an industrial pulse

Silver moves with gold but exaggerates every move, and adds a second driver: **industrial demand** (solar panels, electronics, EVs). This dual nature makes silver:

- **High beta to gold.** In a precious-metals rally, silver typically outruns gold; in a selloff, it falls harder. The **gold/silver ratio** (how many ounces of silver equal one ounce of gold) is the key relative tool — a historically high ratio suggests silver is cheap relative to gold and may outperform on the next up-leg; a low ratio suggests the reverse.
- **Sensitive to global growth.** Because ~half of silver demand is industrial, a strong-growth/reflation narrative gives silver an extra tailwind gold lacks.

Technically silver trends like gold but with wider ranges, sharper spikes, and more violent shakeouts. It rewards the same base-breakout and DEMA-pullback setups, but demands wider stops and smaller size to survive the noise.

### Worked silver example (approximate reconstruction — verify on your charts)

Gold has just broken out (as above). The gold/silver ratio is historically stretched, implying silver has room to catch up. MCX Silver, which had lagged, breaks its own multi-week base above ₹92,000 per kg with a violent volume spike as the industrial-plus-monetary bid combines. Enter on the breakout above **₹92,000**, stop wider than you would for gold — below **₹88,500** to survive silver's whip — targeting a fast measured move to **₹98,000** and then ₹1,02,000 if gold's leg extends. Because silver is high-beta, position size must be *smaller* than gold for the same rupee risk, and you must accept larger adverse swings. The gold/silver ratio compressing (silver outperforming) confirms the catch-up trade is working.

## Crude Oil: geopolitics, inventories, and OPEC

MCX Crude tracks WTI and is the most *event-driven* commodity. Its drivers:

- **OPEC+ supply decisions.** Production-cut or production-increase announcements gap crude instantly and set multi-month trends.
- **Geopolitics.** Middle East conflict, shipping-lane disruptions (Strait of Hormuz, Red Sea), and sanctions spike crude on a risk premium — sharp, sometimes short-lived.
- **US inventories — the weekly EIA report.** Every Wednesday night (India time), the US EIA crude-inventory data drops during the MCX evening session. A large draw (inventories falling) is bullish; a build (rising) is bearish. This is the single most reliable scheduled volatility event for MCX crude traders — the evening session around the EIA release is where crude's tradable range often gets made.
- **Global demand/growth** (China especially) and the dollar.

Technically crude respects levels but *spikes* on news, producing frequent false breakouts around headlines. It is best traded around its scheduled catalysts (EIA, OPEC) and its well-defined support/resistance shelves.

### Worked crude example (approximate reconstruction — verify on your charts)

MCX Crude is ranging ₹6,300-₹6,700 per barrel. It is Wednesday evening; the market positions ahead of the EIA report. The consensus expects a modest build, but the actual print shows a large *draw* (bullish surprise). Crude spikes off the ₹6,450 area, breaks ₹6,700 on huge volume within minutes of the release, and holds above it. The setup: **EIA-surprise breakout.** Rather than chasing the first spike (dangerous — crude whips), wait for a 15-minute close to *hold* above **₹6,700**, then enter, stop below **₹6,580**, target ₹6,950 and then the prior swing high. Confluence: WTI internationally confirming the same breakout, no offsetting dollar spike, and — for a hold — a constructive OPEC/geopolitical backdrop. The discipline that saves crude traders: never trade the first tick of the EIA release; let the initial spike-and-fade resolve, then trade the *confirmed* direction on the 15-minute close.

## Natural Gas: the widow-maker

MCX Natural Gas (Henry Hub-linked) is the most dangerous, most mean-reverting instrument on the exchange. Treat it with extreme respect.

- **Weather is king.** US heating demand (winter cold snaps) and cooling demand (summer heat) drive gas more than anything. Weather-forecast revisions gap gas violently. This is a *meteorology* trade as much as a chart trade.
- **The weekly EIA storage report** (Thursday night, India time) is the scheduled bomb — the storage build/draw versus expectations can move gas several percent in seconds.
- **Extreme volatility and mean-reversion.** Natural gas can move 5-10% in a session, spike on a forecast, then collapse just as fast. It does NOT trend as cleanly as gold or crude — it whips, spikes, and reverts. Trend-following gets whipsawed; disciplined range-and-reversion trading with tight risk fares better.

The honest warning: natural gas destroys more retail MCX accounts than any other contract. Its cheap-looking price per lot lures traders into oversized positions, and its violence then wipes them out. If you trade it at all, trade the *mini* contract, size tiny, use hard stops, and never average down.

### Worked natural gas example (approximate reconstruction — verify on your charts)

MCX Natural Gas has spiked from ₹180 to ₹230 per mmBtu on a cold-weather forecast, RSI screaming overbought at 82, price extended far above its 20-DEMA. The forecast then moderates. The setup here is *not* a breakout chase — it is a **mean-reversion fade** of an exhausted spike: short near ₹228 as it fails to make new highs and rolls over below the prior 15-minute low, with a hard stop above **₹235** (small size, non-negotiable stop), targeting reversion toward the 20-DEMA near ₹205 and then ₹195. Confluence: overbought RSI, price stretched from the mean, weather forecast softening, and Henry Hub internationally rolling over. Because gas is a widow-maker, the position is *small* and the stop is *hard* — you are trading probability with strict risk, accepting that any single gas trade can gap through a stop.

## The MCX setups, side by side

| Setup | Best commodity | Trigger | Stop | Target | Regime |
|---|---|---|---|---|---|
| Macro-catalyst base breakout | Gold, Silver | Daily close beyond multi-week base on Fed/DXY catalyst | Back inside base | Measured move of the range, trail 20-DEMA | Dovish Fed / weak dollar |
| Gold/silver ratio catch-up | Silver | Ratio stretched, silver breaks its base as gold leads | Wider than gold, below base | Fast measured move | Precious-metals rally |
| EIA-surprise breakout | Crude | 15-min close holds beyond level after inventory surprise | Other side of the level | Prior swing high, trail | Wed-night EIA event |
| Overbought spike fade | Natural Gas | Exhausted spike, overbought RSI, rolls below prior 15-min low | Hard, just above spike high | Reversion to 20-DEMA | Post-forecast/EIA extension |
| DEMA-pullback trend | Gold | Bounce off rising 20/50-DEMA in an uptrend | Below next-lower DEMA | Prior high, trail | Established gold trend |

## Confluence layers for MCX

- **Always overlay the international chart.** MCX gold without a spot-gold overlay, MCX crude without WTI, MCX gas without Henry Hub — you are trading a shadow without watching the object casting it.
- **Watch USDINR on the metals.** An MCX gold move can be a rupee move in disguise. Decompose the candle: is gold rising in dollars, or is the rupee falling?
- **Track the dollar index (DXY).** Broadly inverse to gold, silver, and (looser) crude.
- **Respect the scheduled catalysts.** Fed and US CPI for gold; OPEC and Wednesday-night EIA for crude; Thursday-night EIA storage and weather forecasts for gas. Plan around these, don't get ambushed by them.
- **Trade the evening session for the internationally-linked moves.** Gold and crude's most tradable ranges are frequently made after the US session opens, in MCX's extended evening hours.

## Pitfalls

- *Ignoring the rupee on metals.* Attributing a rupee-driven MCX gold move to "gold strength" leads to wrong-way trades when the rupee reverses.
- *Chasing the first tick on EIA/Fed releases.* The initial spike routinely fakes out; wait for the 15-minute close to trade the confirmed direction.
- *Applying gold-sized positions to natural gas or crude.* Recompute size per contract's rupee-per-point and volatility; the energies move P&L far faster.
- *Trend-following natural gas.* Gas whips and mean-reverts; treating it like trending gold is how the widow-maker earns its name.
- *Trading MCX without the international overlay.* You are always trading a global asset wrapped in rupees — watch the global chart, the dollar, and the currency.
- *Averaging down on a losing MCX position.* On leveraged, gap-prone commodities, averaging into a loser is account-ending; use hard stops and accept them.

## Interview-ready summary

MCX is a second market with a different clock, extended into the US-session evening where the internationally-linked commodities make their real moves. Every MCX contract is a **rupee wrapper on a dollar asset**, so you must always overlay the international chart, the dollar index, and — for metals — USDINR to know what is truly driving your candle. **Gold** is the clean trender: a Fed-and-dollar-driven store of value best traded with macro-catalyst base breakouts and DEMA-pullback continuations, held and trailed. **Silver** is gold's high-beta, part-industrial cousin — same setups, wider stops, smaller size, with the gold/silver ratio as the catch-up signal. **Crude** is the geopolitics-and-inventory contract — trade its scheduled catalysts (OPEC, Wednesday-night EIA) on confirmed 15-minute closes, never the first spike. **Natural gas** is the widow-maker — weather- and storage-driven, wildly volatile and mean-reverting, to be traded tiny, with hard stops, via mean-reversion fades rather than trend-chasing, if at all. Across all four, size per contract, respect the scheduled events, watch the global object not just its rupee shadow, and remember that leverage plus gaps means discipline on stops is not optional — it is survival.
