# DXY & US Yields for Indian Traders

Every Indian trader eventually learns a humbling truth: the most important charts for Nifty are often not Nifty charts at all. They are two American instruments — the **US Dollar Index (DXY)** and the **US 10-year Treasury yield (US10Y)** — plus their derivative, **USDINR**. These are the "weather system" above the Indian market. You can be a brilliant chart-reader of Reliance or Bank Nifty and still get run over because a macro front moved in overnight while you slept. This chapter is about reading that weather: what DXY and US yields *are* from a trader's lens, how they transmit into Indian equities, currency and gold, and how to build a simple, repeatable intermarket bias so that you stop being surprised by gap-downs that "came out of nowhere."

This is not economics theory. It is a technical, intermarket playbook. We stay India-first throughout: Nifty, Bank Nifty, FII flows, USDINR on the NSE currency segment, MCX gold, and the levels that actually matter in 2026.

## What DXY and US10Y are, and why an Indian trader cares

**DXY (US Dollar Index)** measures the dollar against a basket of six currencies — euro (~57.6% weight), yen, pound, Canadian dollar, Swedish krona, Swiss franc. Critically, **the rupee is not in the basket.** So DXY is not a direct USDINR chart. It is a *global dollar strength gauge*. When DXY rises, the dollar is strong against the developed world; capital tends to rotate toward dollar assets and away from emerging markets like India. When DXY falls, the dollar is weak, risk appetite improves, and money flows back into EM equities.

**US10Y (US 10-year Treasury yield)** is the world's benchmark "risk-free" rate — the price of money for the planet. When the US 10-year yield rises, holding safe US government paper pays more, which makes risky assets (including Indian equities, which are a long-duration risk asset) relatively less attractive. Rising yields also strengthen the dollar (higher US rates pull capital in), so DXY and US10Y usually move *together*. Falling yields do the reverse — cheaper global money, weaker dollar, tailwind for EM.

The logic chain for an Indian trader:

- **DXY up + US10Y up** → dollar strong, global money leaves EM → **FIIs sell Indian equities**, USDINR rises (rupee weakens) → **headwind for Nifty**, especially for rate-sensitive and high-valuation sectors.
- **DXY down + US10Y down** → dollar weak, risk-on → **FIIs buy**, USDINR falls/stabilises → **tailwind for Nifty**, gold and metals often rally.

Why does this matter *technically*? Because FIIs are the marginal price-setters at the index level in India. Domestic institutions (DIIs — mutual funds, insurers, SIP flows) provide a persistent bid, but the *swings* — the sharp trend changes in Nifty and especially Bank Nifty — are dominated by foreign flows, and those flows respond to the global dollar and rate picture. Read the weather system, and you understand the tide underneath your candlestick patterns.

## Construction and reading: the levels and relationships that matter

You do not need to build DXY or US10Y — TradingView carries them as `TVC:DXY` and `TVC:US10Y` (also `US02Y`, `US30Y`). What you need is a **reading framework**: key levels, regime zones, and the correlation lens.

### DXY regime zones (a practical 2026 map)

| DXY zone | Regime read | Typical India effect |
|---|---|---|
| Below ~100 | Weak dollar, strong risk-on | FII inflows likely; Nifty tailwind; gold/metals strong |
| 100–104 | Neutral / balanced | India trades on its own fundamentals; flows two-way |
| 104–107 | Dollar firming, caution | FII selling risk rises; USDINR pressure; be defensive |
| Above ~107 | Strong dollar, risk-off | FII outflows, rupee weakness, Nifty headwind; IT/pharma (dollar earners) relatively cushioned |

These are *zones*, not magic lines. The point is direction and momentum within the zone, not a two-decimal print.

### US10Y regime zones

| US10Y zone | Read | India effect |
|---|---|---|
| Below ~3.5% | Easy global money | Strong EM tailwind; growth/valuation stocks re-rate up |
| 3.5%–4.2% | Comfortable | Neutral; India trades on domestic factors |
| 4.2%–4.7% | Yields elevated | Valuation compression risk; caution on expensive names |
| Above ~4.7–5.0% | Yield stress | Global risk-off; FIIs de-risk EM; sharp Nifty drawdown risk |

The **rate of change** matters more than the level. A 10Y grinding from 4.0% to 4.3% over two months is digestible. The same 30 bps in four sessions is a shock that gaps Nifty down and spikes India VIX. Traders should watch **weekly momentum** on US10Y: a fast breakout above a prior swing high is a warning flag for Indian longs regardless of how bullish the Nifty daily chart looks.

### The correlation lens

Pull up three charts side by side: DXY, US10Y, and USDINR (`FX_IDC:USDINR` or the NSE currency future). Over most of the last decade:

- **DXY and USDINR** are positively correlated — strong dollar → weaker rupee. But USDINR has its own domestic drivers (crude oil prices, RBI intervention, trade deficit), so it does *not* track DXY tick for tick.
- **US10Y and USDINR** are positively correlated — higher US yields → capital outflow → rupee down.
- **DXY and Nifty** are usually *negatively* correlated at turning points. When you see DXY breaking out to new highs, treat aggressive Nifty long setups with suspicion.

A clean way to quantify this: put a **20-period rolling correlation** indicator between Nifty and DXY on TradingView. When correlation is deeply negative (say below −0.5), the intermarket signal is "live" and DXY is genuinely driving Nifty; when it hovers near zero, India is trading on its own story and DXY noise can be discounted.

## Worked India example: reading a dollar/yield squeeze into Nifty

Let's construct a realistic 2026-style sequence to show the mechanics.

**Setup.** Nifty is at 24,800, grinding up for three weeks on steady DII/SIP buying. The daily chart looks constructive — higher highs, 20-DMA rising, RSI ~62. A pure price-action trader is long and comfortable. But the weather is changing:

- DXY has been basing near 103 and now closes above 104.5 on a wide-range candle after a hot US jobs print.
- US10Y jumps from 4.15% to 4.42% in three sessions — a fast, momentum breakout above its prior swing high.
- USDINR (NSE Sep future) grinds from 86.20 to 86.75, making fresh highs.

**The intermarket read.** All three fronts are aligned bearish for India: dollar breaking out, yields spiking fast, rupee weakening. This is a classic "risk-off cocktail." Even though the Nifty *daily* still looks fine, the odds have shifted. The mechanism: a spiking 10-year and a strong dollar pull global capital toward US paper; FIIs, who are already marginal sellers in Indian cash, accelerate. The FII cash-segment data that evening shows −₹4,200 crore net sold; DII buying of +₹3,100 crore only partially offsets it.

**What happens next (the typical resolution).** Two sessions later, an overnight further spike in US10Y (to 4.55%) and a green DXY candle produce a **gap-down opening** in Nifty to 24,540. Bank Nifty, the most FII-sensitive, gaps harder (banks are rate- and flow-sensitive) and slices through its 20-DMA. India VIX pops from 12 to 15.

**The lesson.** A trader watching only the Nifty candle got blindsided. A trader watching the weather saw the setup 48 hours early: DXY breakout + fast 10Y spike + rupee at new highs = trim longs, tighten stops, don't add, and be ready to play the gap-down. The intermarket chart was the leading indicator; the Nifty gap was the lagging confirmation.

**The mirror image.** Run it in reverse. DXY rolls over from 107 back below 104, US10Y peaks and starts falling from 4.8% toward 4.4%, and USDINR eases from 87.0 to 86.3. FII cash flows flip to net buying for five straight sessions. *This* is the environment where Nifty breakouts have follow-through, where beaten-down high-beta and rate-sensitive names (NBFCs, realty, midcap financials) rip, and where you want to be aggressively long. The dollar peaking is one of the most reliable "green light" signals for Indian equities.

## How to use it for bias and timing

Intermarket analysis is a **bias tool and a timing filter**, not an entry trigger. You still enter on your own price setups (breakouts, pullbacks, level reclaims). DXY and yields tell you *which direction to lean* and *how much size to carry.*

**The three-front bias score.** Each morning before the India open, score three fronts as +1 (India-bullish), 0 (neutral), or −1 (India-bearish):

| Front | Bullish (+1) | Bearish (−1) |
|---|---|---|
| DXY | Falling / below its 20-DMA / breaking support | Rising / above 20-DMA / breaking out |
| US10Y | Falling or stable | Rising fast, breaking swing highs |
| USDINR | Falling / rupee strengthening | Rising / rupee weakening to new highs |

Sum the score:

- **+2 to +3:** Green light. Favour longs, carry full size, buy dips aggressively, trust breakouts.
- **+1 to −1:** Neutral. Trade the India chart on its own merits; normal size; both directions valid.
- **−2 to −3:** Red light. Favour shorts or cash, cut long size, don't chase breakouts, respect gap-down risk, keep hedges (long puts / short futures against your cash portfolio).

This single number, computed in two minutes from three charts, will save you from the most painful category of loss: being maximally long into a global risk-off.

**Timing overnight risk.** US markets and yields move while India sleeps. The US10Y and DXY *close* (roughly 2:30 AM IST) and the overnight move in US equity futures and yields set the tone for the SGX/GIFT Nifty gap. If you carry positional trades, glance at DXY/US10Y and GIFT Nifty before the 9:15 open — a fast overnight yield spike is your single best predictor of a gap-down open.

**Sector rotation from the dollar.** The dollar picture also tells you *what to own inside India*:

- **Strong dollar / rupee weak** → tailwind for **IT and pharma** (they earn in dollars, so a weak rupee inflates rupee revenue). If you must be long into dollar strength, lean toward Nifty IT.
- **Weak dollar / rupee strong / risk-on** → tailwind for **banks, NBFCs, realty, metals, high-beta midcaps**. Metals specifically love a weak dollar because global commodities are priced in dollars.
- **Rising yields** → headwind for **long-duration, high-valuation names** (expensive new-age tech, richly-valued consumption) and for **rate-sensitives** at the margin.

## Pitfalls

**1. Treating DXY as USDINR.** The rupee is not in the DXY basket. DXY can fall (dollar weak vs euro/yen) while USDINR still rises (rupee weak due to crude spiking or trade deficit). Always confirm on the actual USDINR chart; DXY is the *global* backdrop, USDINR is the *India-specific* reality.

**2. Correlation is regime-dependent, not constant.** The Nifty–DXY inverse correlation tightens in risk-off panics and loosens when India has a strong domestic narrative (heavy SIP inflows, a reform rally, an election tailwind). Use the rolling-correlation indicator to know whether the signal is "live." Don't short Nifty just because DXY ticked up during a phase when the two are decoupled.

**3. Confusing level with momentum.** DXY at 105 grinding sideways is different from DXY *rocketing* through 105. The market cares about the impulse. A fast, expanding-range breakout in DXY or US10Y is the signal; a slow drift is background noise.

**4. Fighting the tape on a "should."** "US yields are too high, they must fall, so I'll buy Nifty." Maybe — but the market can stay irrational longer than your stop-loss can survive. Trade the *observed* trend in DXY/yields, not your forecast of where they *ought* to go.

**5. Ignoring RBI's hand in USDINR.** The RBI actively manages rupee volatility via intervention. USDINR can look coiled and unnaturally calm even when DXY is volatile, because the RBI is capping the move. When that cap eventually releases, USDINR can move sharply. Don't assume a quiet rupee means a safe backdrop.

**6. Over-trading the macro.** Intermarket analysis is a *positional and swing* tool. Do not let a mid-session wiggle in US10Y futures make you flip your intraday scalp. Use it to set the day's bias, then trade your India levels.

## A weekly and daily routine to internalise this

**Weekend (30 minutes).** Open weekly charts of DXY, US10Y, and USDINR. Mark the trend, key levels, and any breakouts/breakdowns. Write one sentence: *"Dollar regime this week: strong/weak/neutral; yields: rising/falling/stable; India lean: long/short/neutral."* Pin it above your desk.

**Daily pre-open (5 minutes).** Check overnight DXY and US10Y closes and GIFT Nifty. Compute the three-front bias score. Note FII/DII cash flows from the previous session (available each evening on NSE). Decide your maximum long/short size for the day from the score.

**Intraday.** Trade your India setups, but let the bias score govern *aggression* — full size with the score, half size against it, hedged into red-light regimes.

## Interview-ready summary

- **DXY** is the dollar vs a six-currency developed-market basket (euro-heavy, no rupee). It gauges *global* dollar strength. **US10Y** is the world's benchmark risk-free rate. They usually move together; rising dollar + rising yields = global risk-off.
- For India, the transmission is **FII flows and USDINR**: strong dollar / rising yields → FIIs sell Indian equities and the rupee weakens → **Nifty and especially Bank Nifty face headwinds**. Weak dollar / falling yields → FII inflows, rupee stable, **Nifty tailwind**, metals and high-beta names lead.
- DXY is **not** USDINR — the rupee isn't in the basket, and crude/trade-deficit/RBI intervention drive USDINR independently. Always confirm on the USDINR chart.
- Use a **three-front bias score** (DXY, US10Y, USDINR each ±1) to set daily lean and size: +2/+3 favour longs, −2/−3 favour cash/shorts and hedges.
- **Momentum beats level:** a fast breakout in DXY or a rapid US10Y spike is the actionable signal; a slow drift is noise. Correlation is regime-dependent — verify it's "live" with a rolling-correlation indicator before acting.
- Sector tilt: dollar strength cushions **IT and pharma** (dollar earners); dollar weakness powers **banks, metals, realty, and high-beta midcaps**. Rising yields hurt **long-duration, high-valuation** names most.
- The honest bottom line: these instruments don't give you a crystal ball, they give you *odds and context*. Their real value is defensive — they warn you when to stop being aggressively long, which is precisely when most retail traders get hurt.
