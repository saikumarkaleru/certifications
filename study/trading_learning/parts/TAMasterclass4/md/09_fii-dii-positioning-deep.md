# FII/DII Positioning & Flow Analysis (Deep)

If technical analysis tells you *what* price is doing, flow analysis tells you *who* is doing it — and in the Indian market, "who" comes down to two great tectonic plates grinding against each other: Foreign Institutional Investors (FIIs, now formally FPIs) and Domestic Institutional Investors (DIIs — mutual funds, insurers led by LIC, pension funds, banks). Retail and HNIs sit on top of these plates, but the plates set the terrain. A trader who reads only candlesticks and ignores flow is reading the weather without knowing the season. This chapter goes deep on how to read FII/DII cash flows, the far more important F&O positioning data, and how to fold both into a genuine directional bias — with full honesty that flow is a *contextual* edge, not a same-day timing machine.

## What FII/DII Flow Is and Why It Moves India

**FIIs/FPIs** are foreign funds — sovereign wealth funds, global EM funds, hedge funds, ETFs tracking MSCI EM — allocating into Indian equities. They are the *marginal price-setter* at the index level historically because their tickets are large and their entries/exits are concentrated. Critically, FII behaviour is driven by *global* factors as much as Indian fundamentals: the US dollar index (DXY), US 10-year yields, the Fed's rate path, global risk appetite, crude oil, and the rupee. When DXY strengthens and US yields rise, capital flows *out* of emerging markets including India — "risk-off" — regardless of how good Indian earnings look. This is why FII selling can drag Nifty down even in a domestically strong quarter.

**DIIs** are domestic — driven overwhelmingly by *retail SIP flows* into mutual funds (a structurally rising tide in 2026, with monthly SIP inflows a powerful stabiliser), plus LIC and EPFO deployment. DIIs are typically *value-oriented, counter-cyclical buyers*: they buy when FIIs dump and prices fall, because SIP money arrives every month regardless of sentiment and fund managers deploy it into weakness. This structural DII buying has, over the past several years, repeatedly cushioned FII outflows and is the single biggest reason Indian market drawdowns have been shallower than pure FII flow would suggest.

The core dynamic to internalise: **FIIs and DIIs are frequently on opposite sides.** The daily provisional figure (published by NSE/BSE after market close, e.g. "FII net sold ₹3,200 cr, DII net bought ₹2,800 cr") is a tug-of-war scoreboard. Who *wins* that tug-of-war over days and weeks, and — more importantly — what FIIs are doing in the *derivatives* market, sets the medium-term trend.

## The Data Sources and What Each Reveals

There are three distinct FII/DII datasets, and confusing them is the amateur's mistake.

**1. Cash market provisional/final flows.** The daily net buy/sell in the *cash* (delivery) segment. Provisional numbers come at ~5 pm; final (including the real FPI custodial data) a day later. This is the headline everyone quotes. It is useful but *lagging and blunt* — it tells you net cash direction but nothing about leverage, hedging, or conviction.

| Segment | Publisher | Timing | What it shows |
|---|---|---|---|
| Cash provisional | NSE/BSE | ~5:00 pm same day | Rough net cash buy/sell |
| Cash final (FPI) | NSDL/CDSL | T+1 | Accurate FPI cash flows |
| F&O participant-wise OI | NSE | ~6:00 pm same day | FII/DII/Pro/Client positioning in futures & options |

**2. F&O participant-wise open interest — the crown jewel.** NSE publishes daily, category-wise (FII, DII, Pro, Client), the open interest in **index futures, index options, stock futures, and stock options**, split into long and short. *This is the single most valuable flow dataset in Indian TA* and the one most retail traders never look at. It shows you not just direction but *leverage and conviction*. The key derived metric:

**FII Long-Short Ratio in Index Futures** = (FII index-future long contracts) / (FII index-future short contracts).

- Ratio well above 1 (say > 2.5-3): FIIs heavily net long index futures — strongly bullish positioning.
- Ratio well below 1 (say < 0.4-0.5): FIIs heavily net short — strongly bearish/hedged.
- Around 1: neutral/balanced.

This ratio is far more predictive of medium-term trend than the cash number, because index-future positioning is a *directional bet with leverage* — FIIs don't build a huge net-short book unless they mean it.

**3. Sectoral / stock-level FPI holdings.** Monthly/quarterly data on where FPIs are increasing or decreasing holdings by sector (banks, IT, autos). Slower, but tells you the *rotation* — which sectors foreign money is entering or abandoning.

## Reading the F&O Positioning: The Real Signal

Here is the depth most retail analysis misses. The daily NSE participant-wise OI report lets you build a positioning picture across four instruments. Read them *together*:

- **FII Index Futures (long vs short):** the cleanest directional read. A rising long-short ratio = bullish conviction building; a falling ratio = distribution/shorting.
- **FII Index Options:** trickier, because FIIs use options both directionally and as hedges. Rising FII call longs *or* put shorts (writing puts) = bullish; rising put longs = bearish/hedging. Must be read alongside futures.
- **FII Stock Futures:** aggregate long-short here shows appetite for single-stock leverage — a broadening or narrowing of conviction beyond the index.
- **Net notional:** combine to estimate net directional exposure.

The **classic bullish setup:** FIIs *net buying cash* + FII *index-future long-short ratio rising above 2* + FIIs *writing puts* (short put OI rising) = aligned, high-conviction bullish positioning. When cash and futures agree, the signal is strongest.

The **classic bearish/warning setup:** FIIs *selling cash* + index-future long-short ratio *collapsing below 0.5* + FIIs *buying index puts* = coordinated risk-off. Even if DIIs are absorbing the cash selling (holding the index up short-term), a deeply net-short FII futures book is a warning that the smart, global money is positioned for downside. This *divergence* — DII buying propping cash while FII futures turn deeply short — has repeatedly preceded corrections.

## Worked India Example: Reading a Full Flow Picture

A realistic 2026 sequence. Nifty at 24,600, having risen for three weeks.

**Day 1 data:**
- Cash: FII net sold ₹1,800 cr; DII net bought ₹2,400 cr.
- FII index-future long-short ratio: fell from 2.4 to 1.6 over the week.
- FII index options: put longs rising (hedging up).
- Rupee: weakened from 83.2 to 83.6 vs USD; DXY firming.

**The read:** on the surface, Nifty is still up and DIIs are "supporting" it. But underneath, the picture is *deteriorating*. FIIs are selling cash, cutting their futures longs (ratio 2.4 → 1.6), buying protective puts, and the rupee is weakening (a signal of FII outflow pressure). This is **distribution masked by DII absorption** — the index holds because SIP-fed DIIs are catching every FII sale, but the marginal global price-setter is heading for the exit. A technician seeing only a rising Nifty would stay bullish; a flow reader trims longs and tightens stops, because the *quality* of the advance has weakened.

**Day 8 data (a week later):**
- Cash: FII net sold ₹4,500 cr (accelerating); DII net bought ₹3,000 cr (absorbing less than the sale).
- FII index-future long-short ratio: collapsed to 0.45 — FIIs now heavily *net short*.
- Nifty: broke below 24,300, the three-week support.

Now cash selling *exceeds* DII buying, FIIs are aggressively net short futures, and price has broken structure. The flow deterioration that was hidden a week ago has *confirmed in price*. This is the sequence: flow leads, price follows. The bias flips bearish — sell rallies toward 24,300 (now resistance), with the deeply net-short FII book as conviction that the path of least resistance is down until that ratio starts recovering.

**The reversal read (three weeks later).** Nifty has fallen to 23,000. Now:
- Cash: FII selling *decelerating* (₹800 cr net sell vs ₹4,500 earlier); some sessions net buy.
- FII index-future long-short ratio: bottoming and *ticking up* from 0.4 to 0.7.
- India VIX spiked and is now falling; PCR-OI at an extreme high; rupee stabilising as DXY peaks.
- DIIs still buying steadily.

The flow is *turning*. FII selling is exhausting, their futures shorts are beginning to cover (ratio rising), and the global backdrop (DXY) is topping. Combined with the extreme sentiment readings from the previous chapters, this is a high-probability *accumulation* zone. Flow bottoms before price bottoms decisively — the covering of the FII short book is often the fuel for the first sharp rally off the low.

## How to Use It for Bias and Timing

Flow is a **bias and context** layer, layered *on top of* your price structure, not a same-day trigger. Concretely:

1. **Daily routine:** after market close, log four numbers — FII cash net, DII cash net, FII index-future long-short ratio, and the rupee/DXY direction. Track the *trend* of each over 5-10 sessions, not the single day. A single day's cash figure is noise; the *sequence* is signal.
2. **Trend confirmation:** in an uptrend, you want FII cash buying (or at least DII absorbing) *and* a rising or high FII futures long-short ratio. When price rises but the futures ratio is *falling*, treat the advance as suspect (distribution) and reduce size.
3. **Divergence alerts:** the most valuable signal is the divergence between DII-supported cash price and a deteriorating FII futures book. That gap is your early warning of a top; the reverse (FII shorts covering into a washed-out, DII-supported market) is your early bottom.
4. **Global overlay:** always read FII flow against DXY, US 10-year yields, and crude. FII behaviour is a *function* of these. If DXY is breaking out, expect FII outflow pressure regardless of domestic news — and vice versa. This is the intermarket link that makes flow analysis predictive rather than merely descriptive.
5. **Expiry and roll context:** near monthly expiry, read FII *rollover* — how much of their futures position they carry to the next series and the long-short composition of what they roll. Heavy short rollover = conviction to stay bearish.

## Pitfalls

- **Trading the single-day cash number.** The daily provisional figure is blunt and lagging, and it includes index-rebalancing and block flows that aren't directional bets. One day means little; the *multi-day trend* and the *futures positioning* are what matter. Reacting to "FII sold ₹3,000 cr today" as a same-day sell trigger is a classic amateur move — the market often *rises* on heavy FII cash selling because DIIs absorb it.
- **Ignoring the F&O data entirely.** Most retail traders quote only cash flows and never open the participant-wise OI report — throwing away the single richest flow dataset. The cash number without the futures positioning is half the picture.
- **Misreading FII options as directional.** FIIs use index options heavily for *hedging*. A rise in FII put longs might be protection on a long cash book, not an outright bearish bet. Always triangulate options with futures and cash before concluding direction.
- **Forgetting the global driver.** Reading FII flow in a domestic vacuum. If you don't watch DXY, US yields, and the rupee, you'll be blindsided when FIIs sell a fundamentally strong India purely because global risk-off is forcing EM redemptions.
- **Assuming DII support is infinite.** DII buying (SIP-fed) is a powerful stabiliser but not a floor. In a deep global shock, redemption pressure can turn even DIIs into net sellers, and the cushion vanishes. Don't treat "DIIs will catch it" as a guarantee.
- **Same-day causation errors.** Flow *leads* price over days-to-weeks, but on any single day price and flow can diverge for mechanical reasons. Flow is a *contextual* edge that improves your bias and sizing — it is not a precise entry timer, and treating it as one produces whipsaws. As always, the majority of retail traders lose, and over-reading a single flow print is one of the ways they do it.

## Interview-Ready Summary

FII/DII flow analysis reads *who* is moving Indian markets. **FIIs/FPIs** are the historical marginal price-setter, driven as much by *global* factors — DXY, US 10-year yields, Fed policy, crude, the rupee — as by Indian fundamentals; strengthening DXY and rising US yields force EM outflows regardless of domestic strength. **DIIs** (mutual funds via structural SIP inflows, LIC, EPFO) are counter-cyclical value buyers whose monthly flows have repeatedly cushioned FII selling. The two are frequently on opposite sides, and the daily "FII sold X, DII bought Y" print is a tug-of-war scoreboard. There are three datasets and confusing them is the amateur error: **cash provisional flows** (blunt, lagging, headline), **F&O participant-wise open interest** (the crown jewel — daily FII/DII/Pro/Client positioning in index/stock futures and options, showing leverage and conviction), and **sectoral FPI holdings** (rotation). The single most predictive metric is the **FII index-future long-short ratio** — well above 1 is bullish conviction, well below 1 is bearish/hedged — because it is a leveraged directional bet, far richer than the cash number. The highest-value signal is a **divergence**: DII buying propping up cash price while the FII futures book turns deeply net short is *distribution masked by absorption* — an early top warning; the reverse (FII shorts covering into a washed-out, DII-supported, extreme-sentiment market with DXY peaking) is an early bottom, since flow bottoms before price. The discipline: flow is a **multi-day bias and context layer** read against the global intermarket backdrop (DXY/yields/crude/rupee) and folded onto your price structure — it leads price over days-to-weeks but is *not* a same-day trigger, and trading a single cash print as a timing signal is exactly how the losing majority misuses it.
