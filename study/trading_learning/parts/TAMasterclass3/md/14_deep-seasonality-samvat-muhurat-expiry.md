# Deep Seasonality: Samvat, Muhurat, Expiry-Week & Monthly Effects

Seasonality is the study of *calendar-linked* tendencies in returns — patterns that recur not because of a chart shape but because of the date. Indian markets are unusually rich in these effects because two calendars overlap: the global financial calendar (month-ends, quarter-ends, F&O expiry, US data) and the Hindu festival/Samvat calendar (Diwali, Muhurat trading, the new Samvat year). Layer on India-specific institutional flows — the March fiscal-year close, SIP inflows on fixed dates, index rebalancing — and you get a dense map of recurring windows.

This chapter treats seasonality with the same honesty as the rest of the book: these are *statistical tendencies*, not laws. Many are real but small; some are folklore that dissolves under proper testing; all are conditional and must never override price, trend, and risk management. We will map the major Indian seasonal windows, quantify what is credible, show how to trade them with confluence, and be explicit about the traps — small samples, survivorship, and data-mining.

## What it is & the logic

A seasonal effect exists when returns conditioned on a calendar marker differ *reliably and for a structural reason* from unconditional returns. The reason matters. A pattern with a mechanism (tax-year flows, expiry-day option pinning, festival buying, index-fund rebalancing) is more trustworthy than a pattern that is merely a coincidence someone found by slicing the data enough ways.

Three mechanism families drive Indian seasonality:

1. **Institutional/flow calendar.** Fiscal year ending 31 March, quarter-end window dressing, monthly SIP inflows (~₹25,000+ crore a month in recent years, credited around fixed dates), FII/DII allocation cycles, and index rebalancing (NSE reviews) all inject or withdraw flow on predictable dates.
2. **Derivatives calendar.** The monthly F&O expiry (last Thursday, now with weekly index expiries) creates option-writing pins, gamma effects, and a distinctive expiry-week character. This is arguably the *most* reliable seasonal structure because it is mechanically enforced by settlement.
3. **Behavioural/festival calendar.** Diwali, Muhurat trading, the Samvat new year, the "sell in May" northern-hemisphere echo, and month-turn optimism reflect sentiment and habit. Softer mechanisms, so weaker and noisier effects — but culturally entrenched enough to matter for sentiment.

The core logic to internalise: **seasonality shifts the odds, not the outcome.** A window that has been "up 70% of years" is still down 30% of the time, and those down years can be brutal (2008's Samvat, 2020's March). You trade the *tilt* with defined risk, not with blind conviction.

## The India seasonal map

### Samvat & Muhurat trading

The Hindu accounting/Vikram Samvat year turns around Diwali. On Diwali evening the exchanges hold a special one-hour **Muhurat trading** session — an auspicious symbolic session to begin the new Samvat. Key facts and tendencies:

- **Muhurat session itself:** typically a small, positive, low-volume, sentiment-driven session. The historical hit-rate of a green Muhurat session is high (a clear majority of years), but the *magnitude* is small — often a fraction of a percent to ~1%. It is a symbolic buy, not an alpha engine. Many long-term investors make a token purchase for tradition.
- **Samvat-to-Samvat return:** the full-year return from one Diwali to the next is, unsurprisingly, just the market's annual return dressed in festival clothing — positive in most years because equity drifts up over time, but with the same fat left tail (a recessionary or crisis Samvat can be sharply negative).
- **Practical read:** treat Muhurat as a sentiment marker and a tradition, not a signal to size up. The useful edge nearby is the *pre-Diwali festive drift* (see below), not the one-hour session.

### The festive / pre-Diwali window

There is a widely observed tendency for a constructive tone into the festival season (roughly the Navratri–Dhanteras–Diwali stretch, September–November), tied to consumption, gold buying, and positive seasonal sentiment. It is real in the *sense* of appearing in many years, but it is noisy and regime-dependent — a global risk-off (2018, 2008) overrides it completely. Trade it as a mild long tilt *only with trend confirmation*, never as a standalone reason to buy.

### March / fiscal-year-end effects

India's fiscal year ends **31 March**. Around it:

- **Advance-tax outflows** (mid-March) can tighten liquidity and create short-term softness.
- **Window dressing** by funds into quarter/year-end can support quality large-caps.
- **April optimism / new-FY allocation** frequently produces a firm start to the new fiscal year as fresh allocations deploy. The "April tends to be constructive" tendency is one of the more commonly cited Indian monthly effects.

### Monthly turn-of-month effect

Globally documented and visible in India: returns cluster around the **turn of the month** — roughly the last 1–2 trading days of a month plus the first 3 of the next — driven by SIP inflows, salary-cycle investing, and institutional rebalancing. The rest of the month contributes proportionally less. This is one of the more robust, mechanism-backed calendar effects and blends naturally with the F&O expiry (last Thursday) that sits just before month-end.

### "Sell in May and go away"

The northern-hemisphere adage (weak May–October, strong November–April) has a *weak, inconsistent* echo in India. It is more an artifact of global risk cycles and monsoon uncertainty than a dependable Indian rule, and in several recent years it simply failed. File it under "aware of, not trading."

### Budget & event seasonality

The **Union Budget (1 February)** creates a recurring high-volatility window: elevated India VIX into the date, sector rotation on announcements (infra, defence, railways, consumption, capital-gains-tax sensitivity), and frequently a sharp intraday reversal on Budget day itself. This is not a directional seasonal so much as a *volatility* seasonal — you trade the vol expansion and sector dispersion, and you respect that direction is a coin-flip until the speech lands.

## Expiry-week & expiry-day effects (the derivatives seasonal)

This is the most mechanically reliable seasonal structure in Indian markets, because it is enforced by settlement.

### Structure

- **Monthly F&O expiry:** last Thursday of the month (shifted for holidays). Stock options and monthly index contracts settle.
- **Weekly index expiries:** Nifty, Bank Nifty, Fin Nifty and others expire on staggered weekdays through the month (exchange schedules have shifted over time — always check the current NSE circular).

### Observed tendencies

1. **Max-pain / pin effect.** Into expiry, heavy option *writing* tends to pull the index toward the strike where the largest option value would expire worthless (loosely, "max pain"). On many expiry days Nifty gravitates toward a round strike with dense OI. The effect is a *tendency*, strongest when there is no strong trend or event; a trending or news day overwhelms it.
2. **Expiry-week compression then release.** The days *before* monthly expiry often show range compression as writers defend strikes; the *rollover* and the following week can then trend as fresh positioning builds.
3. **Volatility crush intraday on expiry.** Option premiums (especially weeklies) decay violently through expiry day — theta on the final day is enormous. This defines the dominant *strategy* seasonality: expiry day favours option *sellers* / spreads over naked buyers.
4. **Rollover reads.** Rollover percentage and the cost of carry into the next series give a sentiment gauge — high rollovers with rising price = bullish continuation bias into the new series.

### How to use it (with F&O specifics)

- **Expiry-day range-bound bias:** on a quiet expiry with the index near a heavy-OI strike, iron-fly / iron-condor / short-strangle structures around the pin can harvest theta — with strict stops, because a break of the pin (news, momentum) turns the pin trade into a fast loser.
- **Support/resistance from OI walls:** the strikes with the largest Put OI (support) and Call OI (resistance) define the expiry-week range; buy toward the Put wall, fade toward the Call wall — but only while the walls hold.
- **Avoid naked long options on expiry day** unless you have a strong directional catalyst — theta and the pin are both working against you.

## Worked India example (levels & ₹)

**Turn-of-month + expiry confluence on Nifty.** Suppose it is the final week of a month. Monthly expiry is Thursday; month-end SIP inflows land Friday–Tuesday. Nifty is consolidating at **23,400** with the **23,400 strike** carrying the heaviest combined OI, the **23,200 strike** holding the largest Put OI (support), and **23,600** the largest Call OI (resistance).

Seasonal read:
- Expiry-week compression pins price near 23,400 (the max-pain zone).
- Turn-of-month inflows bias the *following* few sessions gently up.

Trade construction:
1. **Into expiry (Wed–Thu):** sell an iron-fly centred at 23,400 — short 23,400 straddle, long wings at 23,200/23,600 for defined risk. Collect, say, ₹180 net credit per lot (lot 25 → ₹4,500 credit), max loss capped by the wings (₹500 wing − ₹180 credit = ₹320 → ₹8,000 per lot). Profit if Nifty expires near 23,400. **Stop discipline:** exit if Nifty decisively breaks 23,200 or 23,600, because the pin has failed.
2. **Into the turn-of-month (Fri onward):** flip to a *long* tilt — buy a Nifty 23,500 call debit spread (long 23,500 / short 23,800) for the SIP-inflow drift, defined risk, targeting a move to the 23,600–23,800 Call wall as fresh flow deploys. Risk the debit only.
3. **Confluence check:** align with the daily trend (only take the long-drift leg if the 20-DMA is rising and price is above it) and with India VIX (a calm VIX supports the theta-harvest; a rising VIX warns of an event that breaks the pin).

The seasonal windows did not tell us *where* Nifty must go — they told us *when* compression (into expiry) and *drift* (turn-of-month) were probable, and we expressed each with defined-risk F&O structures.

## Backtest / edge notes & realistic costs

- **Quantify before you trust.** For any claimed window (e.g., "April up," "turn-of-month up," "green Muhurat"), compute the historical **hit-rate, average return, median return, worst year, and standard deviation** over as many years as data allows. A high hit-rate with a small average and a catastrophic worst-year is a *low-conviction* edge.
- **Costs eat small edges.** Turn-of-month and expiry effects are often just a few tenths of a percent. After **STT, brokerage, exchange fees, GST, stamp duty, and slippage** (especially in options, where spreads are wide on far strikes), a seasonal edge of 0.3% can vanish. Only trade seasonals whose gross edge clears costs with margin.
- **Small samples are the enemy.** With ~30 years of liquid-index history you have only ~30 Aprils, ~30 Samvats, ~30 Budgets. That is *tiny*. A pattern "true 22 of 30 years" has wide error bars; treat it as suggestive, not proven.
- **Regime dependence.** Nearly every Indian seasonal breaks in a global crisis year (2008, 2020) or a domestic shock. Always condition on the prevailing trend and VIX regime.

## Adaptations for NSE / F&O

- **Weeklies changed the game.** With weekly Nifty/Bank Nifty expiries, the "expiry-week" character now repeats *every* week for index options, and theta-harvest seasonality is a near-continuous opportunity — but so is the tail risk on trend days. Position size down.
- **Stock vs index.** Stock F&O still settles monthly; the monthly last-Thursday effects are cleaner in single stocks, while index seasonality is now fragmented across weekly expiries.
- **Sector seasonality:** IT (US-fiscal and USDINR sensitive, results-season swings), autos (festive-month sales prints), banks (quarter-end and RBI-policy sensitive), FMCG (monsoon/festive consumption) each carry their own calendar overlays worth mapping for rotation.
- **USDINR & MCX:** USDINR has month-end corporate-flow and RBI-intervention seasonality; gold/silver on MCX carry a strong festive-demand (Dhanteras, Akshaya Tritiya, wedding-season) seasonal into physical buying windows.

## Pitfalls

- **Data-mining / p-hacking.** Slice the calendar enough ways and *some* pattern will look significant by chance. Demand a *mechanism* before believing a window.
- **Survivorship & index reconstitution.** Long backtests on the current Nifty constituents overstate returns because losers were removed. Use point-in-time index data.
- **Overfitting the window.** "Buy 3 days before expiry, sell 1 day after" tuned to history will not hold. Keep rules simple and mechanism-driven.
- **Ignoring the tail.** The average April being green does not protect you in the April that isn't. Always trade with stops and defined risk.
- **Confusing sentiment ritual with edge.** Muhurat buying is tradition; it is not a trading strategy. Don't size up on folklore.
- **Calendar drift.** Expiry days and exchange schedules change (weeklies were added, days shifted). A seasonal rule pinned to an old schedule silently breaks. Re-verify against current NSE circulars.
- **Event collisions.** When a Budget, RBI policy, US FOMC, or election result lands inside a seasonal window, the event dominates — de-weight or stand aside.

## Interview-ready summary

Indian markets carry unusually rich seasonality because the global financial calendar and the Hindu Samvat/festival calendar overlap, layered with India-specific flows (31-March fiscal close, monthly SIP inflows, index rebalancing) and a dense derivatives calendar. The most *mechanically reliable* seasonal is the **F&O expiry structure** — max-pain pinning near heavy-OI strikes, expiry-week compression, and violent theta decay that favours option sellers/spreads over naked buyers — because it is enforced by settlement. The **turn-of-month effect** (SIP and rebalancing inflows) and **April/new-fiscal-year optimism** are credible, mechanism-backed tendencies; **Muhurat trading** is a small, positive, sentiment-driven ritual, not an alpha source; the pre-Diwali festive drift and "sell in May" are real-*ish* but noisy and regime-dependent; the **Budget (1 Feb)** is a volatility seasonal, not a directional one. The professional discipline is to *quantify* every claimed window (hit-rate, average, worst year), demand a mechanism, net out heavy Indian transaction costs, respect tiny sample sizes and regime breaks, and always trade the calendar *tilt* with defined risk and trend/VIX confluence — never letting a date override price and risk management.
