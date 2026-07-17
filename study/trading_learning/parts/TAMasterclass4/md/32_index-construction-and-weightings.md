# Index Construction, Weightings & TA Implications

Most technicians trade the Nifty and Bank Nifty every day without ever asking *what the number is made of*. That is a mistake, because the construction of an index — how it is weighted, which stocks dominate it, how and when it is rebalanced, and how the futures relate to the spot — quietly determines how the chart behaves. A technical signal on the Nifty is really a weighted-average signal on 50 businesses, and the weighting is lopsided enough that a handful of stocks *are* the index. If you understand the machinery, you can read divergences that a pure chartist cannot see, anticipate the mechanical flows around rebalancing, and stop being surprised when the index and "the market" disagree. This chapter is the plumbing manual: what the indices are made of, how weightings shape the tape, and the concrete TA implications for the Indian trader.

## What the index actually is — free-float market-cap weighting

The Nifty 50, Bank Nifty, Fin Nifty, and the sectoral indices are all **free-float market-capitalisation weighted**. Each constituent's weight is proportional to its *investible* market cap — total shares outstanding, minus promoter and strategic locked-in holdings (the non-free-float), times price, times an IWF (Investible Weight Factor). The formula in essence:

> Index level = (Σ free-float market cap of constituents ÷ base free-float market cap) × base index value

Two consequences fall straight out of this and matter for every chart you read:

1. **Price-weighted the index is not.** Unlike the Dow, a high *priced* stock does not dominate; a high *market-cap* stock does. MRF at ₹1,30,000 a share has trivial index weight; a mega-cap at ₹1,500 can dominate.
2. **Weight tracks price in real time.** As a stock rises, its market cap and therefore its weight rise, so it contributes *more* to the index the higher it goes — a momentum feedback loop baked into the maths. The winners increasingly *are* the index.

The free-float adjustment is why two companies of identical total market cap can have very different index weights: a PSU with 60% government holding has a small free float and a small weight, while a widely-held private name of the same size carries a much larger weight. This is why the private banks and Reliance dominate the Nifty far beyond what their headline market cap alone would suggest.

## The concentration problem — a few stocks are the index

Here is the single most important table for an index technician. Approximate Nifty 50 weights (2025-26 regime, illustrative — verify live on the NSE factsheet):

| Stock | Approx Nifty weight | Notes |
|---|---|---|
| HDFC Bank | ~13% | Largest single weight, dominates with ICICI |
| ICICI Bank | ~8% | Second banking heavyweight |
| Reliance | ~8% | Energy/telecom/retail conglomerate |
| Infosys | ~5% | Largest IT weight |
| TCS | ~4% | Second IT heavyweight |
| Bharti Airtel, L&T, ITC, SBI, Axis | ~3-4% each | Next tier |
| **Top 10 combined** | **~55-60%** | Ten stocks move more than half the index |
| Financials (sector) | ~35-38% | The single dominant sector |

The takeaways for a chartist:

- **The Nifty is a financials index with extras.** Banks and NBFCs are ~35-38% of the weight. If Bank Nifty is weak, the Nifty struggles to rally regardless of what the other 40 stocks do. Watching the Nifty without watching the banks is watching the passenger, not the driver.
- **Ten stocks decide the trend.** The top-10 at ~55-60% means a genuine Nifty breakout *requires* the heavyweights to participate. A "breakout" carried by mid-weight names while HDFC Bank and Reliance lag is fragile — it is the tail wagging.
- **Bank Nifty is even more concentrated.** Its top 3-4 private banks (HDFC Bank, ICICI Bank, Axis, SBI, Kotak) are the overwhelming majority of the weight, which is exactly why Bank Nifty is more volatile and trends harder than the Nifty — fewer, higher-beta components with less internal diversification to dampen moves.

## The TA implication that matters most — construction-based divergence

Because a few stocks dominate, the most powerful and *underused* index-TA technique is comparing the **cap-weighted index against its own breadth and against an equal-weight view.**

### Divergence 1 — index vs advance-decline / breadth

If the Nifty makes a new high but the advance-decline line does not, the rally is being carried by a few heavyweights while the average stock is already rolling over. This is a classic distribution warning that a pure Nifty candlestick cannot show you, *because the cap-weighting hides the internal rot.* The index looks healthy; the market underneath is sick. This precise divergence marks most major tops.

### Divergence 2 — cap-weight vs equal-weight

The NSE publishes a **Nifty 50 Equal Weight** index. Compare its ratio against the standard Nifty. When the standard (cap-weighted) Nifty *outperforms* the equal-weight version, leadership is narrowing into the mega-caps — a late-cycle, defensive-rotation signal. When equal-weight outperforms, the rally is broad and healthy. This ratio is one of the cleanest breadth reads available and few retail traders watch it.

### Divergence 3 — index vs its dominant sub-sector

Because financials are ~37% of the Nifty, the **Nifty/Bank Nifty ratio** and the behaviour of Bank Nifty relative to Nifty is a leading tell. When Bank Nifty leads the Nifty up, the trend has its engine; when the Nifty is dragged up by IT or energy while banks lag, question the move's durability.

The unifying lesson: **an index signal is only as trustworthy as the participation beneath it.** Construction knowledge turns you from someone who reads one line into someone who reads whether that line is telling the truth.

## Rebalancing and reconstitution — the mechanical flow event

Indices are not static. NSE reviews the Nifty semi-annually (with effect from end-March and end-September), replacing constituents that no longer qualify with those that do, using a six-month average free-float market-cap ranking. There are also weight caps in certain indices (e.g. Fin Nifty and some sectoral/thematic indices cap single-stock and top-3 weights to avoid over-concentration), which force periodic re-weighting.

Why a technician cares:

- **Passive flows are mechanical and predictable.** Every index fund and ETF tracking the Nifty *must* buy the incoming stock and sell the outgoing one at the effective date, in size, regardless of price. This creates a forecastable demand/supply imbalance.
- **The "index inclusion" run-up.** A stock widely expected to be *added* to the Nifty often rallies into the announcement and effective date as traders front-run the passive buying, then frequently sells off *after* inclusion once the mechanical buying is done — a "buy the rumour, sell the news" pattern with an unusually clear catalyst date.
- **Deletion pressure.** The stock being removed faces forced selling into the effective date — often a poor time to be long it technically, as mechanical supply overwhelms the chart.
- **Rebalance-day volatility.** The close on the rebalancing effective date sees a spike in volume and sometimes sharp last-hour moves as funds execute at the reference price. Intraday traders should expect and respect this — it is flow, not information, and it can whipsaw signals.

The practical play: mark the semi-annual review announcement and effective dates on your calendar. Around them, some price action is *mechanical* rather than technical, and knowing which is which stops you from mis-reading a flow-driven move as a genuine breakout or breakdown.

## Spot vs futures — the derivative's own construction

The Nifty you trade in F&O is a *future*, and its construction relative to spot adds another layer:

- **Fair value and basis.** Nifty futures trade at spot plus cost-of-carry (interest) minus expected dividends until expiry. The difference (basis) is normally a small premium. A future trading at an unusual *discount* to fair value signals aggressive hedging/short pressure; an unusual *premium* signals bullish leverage demand. The basis is a sentiment gauge construction gives you for free.
- **Roll and expiry effects.** As monthly (and now the heavily-traded weekly) expiries approach, open interest rolls to the next series. The convergence of futures to spot at expiry, and the pinning of the index near high-open-interest strikes ("max pain"), are construction-driven behaviours that distort the last hours before expiry. A breakout on expiry afternoon is often options-mechanics, not a real move.
- **Dividend and ex-date adjustments.** When a heavyweight goes ex-dividend, the index mechanically drops by the weighted dividend impact — a "gap" on the chart that is not a bearish signal at all, just an accounting adjustment. Misreading an ex-dividend index dip as a technical breakdown is a rookie error.

## A worked example — reading a narrow Nifty top

Assume the Nifty is grinding to a new all-time high at 26,500. A construction-aware technician runs the following checklist rather than simply celebrating the breakout:

1. **Heavyweight participation:** Is HDFC Bank + ICICI Bank + Reliance (≈29% combined) making new highs with the index? Check — if the banks are lagging and only Reliance and IT are pulling the index, the top-10 are not aligned.
2. **Breadth:** Is the advance-decline line confirming, or is it lower while the index is higher? Suppose more stocks are falling than rising on the up day — a bearish breadth divergence.
3. **Equal-weight ratio:** Is cap-weighted Nifty outperforming Nifty Equal Weight? Suppose yes — leadership is narrowing into mega-caps.
4. **Bank Nifty relative strength:** Is Bank Nifty confirming or lagging? Suppose lagging.
5. **Futures basis:** Are Nifty futures at an unusually high premium (crowded longs)? Suppose yes.

The candlestick says "new high, bullish". The construction read says "a narrow, heavyweight-driven, crowded advance with deteriorating breadth" — a textbook distribution top. The construction-aware trader tightens stops and reduces longs while the pure chartist buys the breakout. **This is the entire payoff of understanding index construction: you see the health of the move, not just its direction.**

## How to build this into your process

- **Keep the weightings on your desk.** Know the top-10 Nifty and top-5 Bank Nifty weights and roughly the sector splits. Update them each quarter from the NSE factsheet.
- **Add three breadth panels** to your index template: advance-decline line, cap-weight vs equal-weight ratio, and Bank Nifty vs Nifty ratio. Read them *with* every index signal.
- **Mark the rebalance calendar.** Semi-annual review announcement and effective dates; treat surrounding flow as mechanical.
- **Check the basis before leaning on a futures signal.** An extreme premium or discount changes the meaning of a breakout.
- **Never trade an ex-dividend or expiry-afternoon index move as pure TA** without asking whether it is mechanical.

## Pitfalls

- **Trading the index blind to its drivers.** The commonest error — treating the Nifty as a monolith when it is a lopsided basket. If you do not know that financials are ~37%, you will be repeatedly baffled by why the index "won't go" on days the banks are red.
- **Mistaking mechanical moves for signals.** Ex-dividend drops, rebalance-day closes, and expiry pinning are flow, not information. Reading them as breakouts/breakdowns generates false trades.
- **Ignoring breadth because the index looks fine.** Cap-weighting is designed to be dominated by winners; that same property *hides* internal deterioration. The index can make new highs on a shrinking group of stocks for weeks before it finally rolls — breadth warns you early; price does not.
- **Assuming Bank Nifty and Nifty are interchangeable.** They are not — Bank Nifty's tighter concentration makes it higher-beta and more trend-prone. Position size and stop distance must reflect its larger typical range.

## Interview-ready summary

- Indian indices are **free-float market-cap weighted**, which means (a) weight follows price in a momentum feedback loop, (b) free-float adjustment shrinks the weight of promoter-heavy names, and (c) a few stocks dominate — the Nifty top-10 are ~55-60% and financials ~37%, so the banks and mega-caps *are* the index.
- The killer application is **construction-based divergence**: compare the cap-weighted index against its advance-decline breadth, against the Nifty Equal Weight index, and against Bank Nifty, to see whether a move is broad and healthy or narrow and distributive — something a pure candlestick read cannot show.
- **Respect the mechanics:** semi-annual rebalancing creates forecastable passive flows (inclusion run-ups, deletion pressure, rebalance-day volatility), the spot-futures basis is a free sentiment gauge, and ex-dividend/expiry moves are mechanical, not technical. The construction-aware technician reads the *health* of an index move, not merely its direction — and that is the difference between buying a genuine breakout and buying the last gasp of a narrow top.
