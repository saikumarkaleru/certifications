# Market Breadth, Intermarket & Sector Rotation

## What it is & why it works

Price on a chart tells you what a single instrument did. **Breadth, intermarket analysis, and sector rotation** tell you *how the whole market is doing underneath* that price — whether an index move is broad and healthy or narrow and hollow, whether money is flowing *into* risk or *out* of it, and *which* pockets of the market are being accumulated versus abandoned. These are the tools of the trader who refuses to look at Nifty in isolation.

**Market breadth** measures participation. The Nifty 50 is a capitalisation-weighted index, so on any given day a handful of heavyweights — Reliance, HDFC Bank, ICICI Bank, Infosys, TCS — can drag the headline number up or down while the *other 45 stocks* do the opposite. Breadth strips away that weighting and asks a democratic question: of all the stocks, how many are actually advancing? How many are making new highs? How many trade above their 200-DMA? A rally where 42 of 50 Nifty stocks advance is structurally different from one where the index is green but only 18 stocks are up. The first is a broad tide; the second is a few whales making waves in a draining pool.

The reason breadth *works* as an analytical edge is that **major tops are processes, not events**. Distribution begins in the weakest sectors first — mid-caps roll over, then small-caps, then the second-line large-caps — while the index-heavy leaders keep the headline number afloat. Breadth captures this internal decay *before* it shows up in price. The classic warning is a **bearish breadth divergence**: Nifty prints a marginal new high, but the number of advancing stocks, new 52-week highs, or stocks above their 200-DMA is markedly lower than at the prior high. Fewer and fewer soldiers are carrying the flag forward. Bottoms show the mirror image — a **breadth thrust**, where after a washout, an overwhelming majority of stocks surge together, signalling that fear has flipped to broad accumulation.

**Intermarket analysis** studies the relationships *between* asset classes — equities, bonds/rates, currencies, commodities — because they are linked by capital flows and macro logic. For an India-based trader in 2026 the critical intermarket variables are the **USD/INR exchange rate**, **US 10-year and Indian 10-year G-Sec yields**, **Brent crude**, **gold**, and above all **FII/DII flow** and the **Dollar Index (DXY)**. India is a net crude importer and a recipient of large foreign portfolio flows, so a weakening rupee, spiking crude, and a rising DXY are a textbook risk-off cocktail that pressures Nifty regardless of what any single chart says.

**Sector rotation** is the observable consequence of the business and liquidity cycle: capital does not enter or leave the market uniformly, it *rotates* between sectors depending on where the economy is and where rates are headed. Early in a recovery, rate-sensitives (banks, autos, real estate) lead; mid-cycle, industrials and capital goods and metals take over; late-cycle, energy and commodities; and in a defensive/risk-off phase, FMCG, pharma, and IT (as a rupee-depreciation and dollar-earnings play) outperform. Reading *which* sector index is making new relative highs tells you what phase the market thinks it is in — and where your long book should be concentrated.

Tie them together and you have a **top-down internal dashboard**: intermarket tells you the *risk regime*, breadth tells you the *health* of the current move, and sector rotation tells you *where the money is*. None of them is a precise entry timer — they are context and conviction tools that keep you on the right side of the bigger tide.

## The mechanics — construction, indicators & settings

Breadth and intermarket work is a family of indicators. Here are the ones that matter for Indian markets and exactly how they are built.

**1. Advance-Decline Line (A/D Line).** The cumulative running total of (advancing stocks − declining stocks) each day, computed on a broad universe — ideally the Nifty 500 or the full NSE list, not just the Nifty 50 (too few names).

> A/D Line today = A/D Line yesterday + (Advances − Declines)

The *level* is meaningless; only the *direction and divergence versus the index* matter. On NSE data you can get daily advances/declines from the exchange bhavcopy or from Chartink's market-breadth dashboard.

**2. Percentage above moving average.** The percent of index constituents trading above a given DMA. The two standard readings:

| Metric | What it flags | Rough zones |
|---|---|---|
| % Nifty 500 stocks > 200-DMA | Long-term participation / bull-bear regime | >60% healthy bull, <20% deep bear/washout |
| % Nifty 500 stocks > 50-DMA | Intermediate momentum | >80% overbought/thrust, <10% oversold |

**3. New Highs − New Lows (NH-NL).** Net count of stocks making fresh 52-week highs minus fresh 52-week lows. Expanding new highs confirm a healthy uptrend; a rally with *shrinking* new highs but the index at new highs is a red flag. A spike in new lows during a decline confirms broad distribution.

**4. Advance-Decline Ratio & TRIN-style measures.** The simple A/D ratio (advances ÷ declines) gauges daily thrust. A reading above ~2.0 on strong up days and expanding volume is a thrust signal; a cluster of days below 0.5 signals broad selling.

**5. Breadth Thrust (Zweig-style).** A 10-day exponential average of Advances ÷ (Advances + Declines). A move from below 0.40 to above 0.615 within about 10 trading sessions is a rare, powerful bottoming signal indicating the market has flipped from broadly oversold to broadly bought.

**6. Intermarket instruments and their India logic:**

| Instrument | Read as | Bullish-for-Nifty when | Bearish-for-Nifty when |
|---|---|---|---|
| USD/INR | Rupee strength/weakness, flow proxy | Falling / stable (~83–84) | Rising sharply (86, 87+) |
| DXY (Dollar Index) | Global risk / EM appetite | Falling | Rising above ~105 |
| Brent crude | India import bill, inflation, CAD | Soft ($70–80) | Spiking ($95+) |
| India 10Y G-Sec yield | Rate regime, cost of capital | Falling / stable | Rising fast |
| US 10Y yield | Global discount rate, FII cost | Falling | Rising toward/above ~4.5–5% |
| Gold | Fear / real-rate hedge | Not needed as tell | Sharp safe-haven spike |
| FII net flow (cash + index futures) | The dominant marginal buyer | Sustained net buying | Sustained net selling |
| India VIX | Volatility / fear | Falling, sub-15 | Spiking above 18–20 |

**7. Relative Strength (RS) line for sector rotation.** For each sector index (Bank Nifty, Nifty IT, Nifty Auto, Nifty FMCG, Nifty Metal, Nifty Pharma, Nifty Realty, Nifty PSU Bank, Fin Nifty) compute:

> RS = Sector index ÷ Nifty 50

Plot it. A *rising* RS line means the sector is outperforming the market (leadership, accumulate); a *falling* RS line means it is lagging (avoid longs). The RS line making new highs while the sector's own price hasn't is an early leadership tell. This is exactly what the **RRG (Relative Rotation Graph)** formalises — plotting RS-Ratio (relative strength) against RS-Momentum on a four-quadrant chart:

| RRG quadrant | Meaning | Action |
|---|---|---|
| Leading (top-right) | Strong RS, positive momentum | Ride / core longs |
| Weakening (bottom-right) | Strong RS, momentum fading | Trim, tighten stops |
| Lagging (bottom-left) | Weak RS, weak momentum | Avoid longs / shorts |
| Improving (top-left) | Weak RS, momentum turning up | Watchlist for rotation-in |

Sectors typically rotate **clockwise**: Improving → Leading → Weakening → Lagging → Improving. Catching a sector as it crosses from Improving into Leading is where the rotation edge lives.

## Reading it — a worked India example

Let us walk a realistic sequence on Nifty across roughly six weeks, the kind of internal-vs-price story that repeats before most meaningful tops.

**Phase 1 — Broad, healthy advance (Nifty ~24,800 → 25,600).** Nifty grinds up over three weeks. Under the surface, breadth confirms every step: on up days the advance-decline ratio on the Nifty 500 runs 2.5:1 to 3:1, the A/D line makes higher highs in lockstep with the index, and **% of Nifty 500 above the 200-DMA sits around 68%**. New 52-week highs expand from ~40 to ~120 a day. Intermarket is benign: USD/INR steady near 83.6, Brent soft around $74, India VIX drifting down to 11.5, and FIIs net buyers roughly Rs 3,000–6,000 crore most sessions. Sector RS lines show Bank Nifty and Nifty Auto leading (RS rising), Fin Nifty firm. This is a *buy dips* tape — the tide is broad and risk-on. A long in a leading bank name here has the wind at its back.

**Phase 2 — The index pushes higher, the internals stop confirming (Nifty 25,600 → 25,950).** Over the next two weeks Nifty adds another ~350 points to a marginal new high at 25,950. But the dashboard quietly deteriorates. The A/D line **fails to make a new high** — it prints a lower peak even as price prints a higher one: a classic bearish A/D divergence. **% above 200-DMA has slipped from 68% to 54%** despite the higher index. Daily new highs have *shrunk* from 120 to about 55, even at the index high. What's holding Nifty up? A close look shows two-three heavyweights (say Reliance and HDFC Bank) doing the heavy lifting while mid-caps and PSU banks have already rolled over. Intermarket adds worry: USD/INR has crept to 84.4, Brent has firmed to $82, DXY is ticking up, and FIIs have flipped to *net sellers* two of the last four sessions. India VIX has stopped falling and bottomed near 11. **Nothing is broken on the price chart yet — but the market is being carried by fewer and fewer stocks.** This is where breadth earns its keep: it tells you to stop adding longs, tighten stops, and stop trusting the headline.

**Phase 3 — Sector rotation turns defensive.** As the leaders narrow, the RS lines rotate. Bank Nifty and Auto RS lines roll over from Leading into Weakening on the RRG. Simultaneously **Nifty FMCG and Nifty Pharma RS lines turn up from the Improving quadrant** — money is quietly rotating from cyclicals into defensives, the tell-tale late-cycle move. A trader watching rotation shifts long exposure out of banks and into the defensives that are being accumulated, or simply raises cash.

**Phase 4 — Price confirms the internals (Nifty 25,950 → 24,900).** Nifty finally cracks. It loses the 25,600 breakout level, then the 20-DMA, and slides to 24,900 over eight sessions. Now breadth goes *with* price and accelerates it: advance-decline ratio flips to 1:4 on down days, new lows expand past 100, % above 200-DMA collapses toward 30%, VIX spikes to 17, USD/INR jumps to 85.1 on FII outflows. The divergence in Phase 2 was the *warning*; Phase 4 is the *event* it predicted. The trader who acted on the internals exited near 25,900 with the crowd still bullish; the one who only watched price got out 1,000 points lower.

## Trading it — entries, stops, targets, management

Breadth and intermarket are primarily **regime filters and conviction modifiers**, not standalone triggers. Here is how to trade with them concretely.

**Setup A — Standing down after a breadth divergence (defensive).**
- *Signal:* Nifty at a new high but A/D line lower high **and** % > 200-DMA down >10 points from the prior swing high **and** new highs shrinking.
- *Action:* Do not initiate new swing longs. Tighten stops on existing longs to just under the last higher-low (e.g. below 25,600). Hedge the book — buy a slightly OTM Nifty put or a put spread, funded partly by writing an upside call you no longer expect to be tested.
- *Invalidation:* Breadth re-confirms — A/D line makes a fresh high with the index and % > 200-DMA turns back up. Then the divergence has failed and you can re-engage longs.

**Setup B — Breadth-thrust entry (aggressive long off a bottom).**
- *Signal:* After a washout, the 10-day breadth-thrust ratio crosses from <0.40 to >0.615 within ~10 days, VIX collapses from a spike, and % > 50-DMA rockets from single digits toward 80%.
- *Entry:* Long Nifty / index-leading sector on the first higher-low pullback after the thrust, not at the vertical. Say the thrust fires with Nifty back at 24,600 after bottoming at 24,050.
- *Stop:* Below the thrust-day low or the pullback low (e.g. 24,300).
- *Target:* Measured — prior range or the swing high that broke down; thrusts often recover the whole prior decline. Trail with the 20-DMA.

**Setup C — Sector rotation long (relative-strength leadership).**
- *Signal:* A sector's RS-vs-Nifty line crosses to a new high / enters the RRG Leading quadrant while the broad regime (breadth + intermarket) is risk-on.
- *Entry:* Buy the strongest 1–2 stocks *within* that sector (not the laggards) on a pullback to support. If Bank Nifty RS is leading, own the private bank breaking out, not the weak PSU name.
- *Stop:* Below the stock's structural swing low.
- *Target:* Ride while the sector RS line keeps rising; exit or trim when RS rolls into the Weakening quadrant even if price is still up — RS peaks *before* price.

**Position sizing by regime.** Let the dashboard scale your risk. Full size when breadth is broad, VIX low, INR stable, FIIs buying. Half size or hedged when breadth is diverging, VIX rising, INR weakening. Flat-to-short bias when breadth, intermarket and rotation *all* point risk-off together — that confluence is when the sharpest declines happen.

## Confluence — combining with other tools and option-chain/OI

Breadth and intermarket are *made* to be combined; they are the context layer beneath your price-based triggers.

**With price structure.** Never short on a breadth divergence alone — wait for price to confirm by losing a key structure level (a higher-low or the breakout base). Breadth tells you the *risk*; the broken level gives you the *entry and the stop*. The Phase-2 divergence above only became tradable short when 25,600 broke in Phase 4.

**With option-chain / OI (this is where India-specific edge compounds).** Overlay breadth with the Nifty and Bank Nifty option chain:
- A breadth divergence *plus* heavy **call writing building at the near strikes** (rising OI at 25,900/26,000 calls) *plus* a falling **Put-Call Ratio** is a powerful confluence for a top — the internals are weakening *and* option writers are betting against further upside, capping the market.
- Conversely, a breadth thrust off a bottom *plus* aggressive **put writing** at lower strikes (OI building at 24,000/24,200 puts, PCR rising from a low) confirms that smart money is selling downside insurance — a floor is forming.
- **Max-pain and the largest-OI strikes** define the magnetic range; breadth tells you whether the market has the internal strength to break out of that range or will pin inside it. Narrow breadth + fat call OI overhead = expect a pin or fade, not a breakout.
- **India VIX** is the bridge: falling VIX with broadening breadth favours selling premium and holding longs; spiking VIX with collapsing breadth favours long options / protective puts.

**With FII/DII flow data.** Breadth divergences carry far more weight when the FII cash + index-futures data shows sustained net selling and a rising long-short ratio unwinding. India moves on the marginal foreign flow; align breadth with flow and you are reading the same story from two angles.

**With intermarket confirmation.** A bearish equity setup is higher-probability when USD/INR is breaking higher, Brent is spiking, DXY is rising and the US 10Y is climbing — the macro tide and the market internals agree. When they disagree (weak breadth but INR strong and FIIs buying), respect the ambiguity and trade smaller.

## Pitfalls & false signals

**Divergences can persist far longer than you can stay short.** This is the cardinal breadth error. A/D and % > 200-DMA can diverge for weeks while a few megacaps melt the index higher. A divergence is a *condition*, not a trigger — it says "raise your guard," not "short now." Always demand price confirmation (a broken structure level) before acting on the short side. Traders who short the first divergence get run over by narrow-but-relentless megacap rallies.

**Wrong universe = garbage breadth.** Computing breadth on just the Nifty 50 is too small a sample and is itself cap-distorted. Use the Nifty 500 or the full NSE universe. Also beware that a handful of newly listed or thinly traded names can skew new-high/new-low counts.

**Index composition and heavyweight distortion.** Because Nifty is cap-weighted and financials + a few names dominate, the index and breadth *routinely* disagree for structural, not predictive, reasons. Confirm that a divergence reflects genuine internal decay (mid-caps and second-line names rolling over) rather than a one-day quirk in two heavyweights.

**Intermarket relationships are regime-dependent, not laws.** The "weak rupee is bearish for Nifty" heuristic breaks when the weakness is dollar-wide and export-heavy sectors (IT, pharma) benefit — Nifty can hold up on IT strength even as INR slides. Crude's impact depends on *why* it's moving (demand-led global growth vs supply-shock). Never apply intermarket rules mechanically; ask *what is driving this and who benefits*.

**Rotation whipsaws and lag.** RS lines and RRG readings are smoothed and can whipsaw in choppy, trendless markets, flipping sectors between quadrants week to week. Rotation signals work best in trending regimes; in a range they generate noise. And RS is *relative* — a "leading" sector can still fall in absolute terms if the whole market drops; it just falls less. Don't mistake relative strength for an absolute long signal without a risk-on regime behind it.

**Data timeliness and holidays.** Breadth needs clean, timely NSE bhavcopy data; stale or partial data (F&O expiry days, truncated sessions, muhurat) can throw off ratios. Cross-check on a second source (Chartink/exchange) before betting on a single reading.

**Thrust rarity.** Genuine Zweig-style breadth thrusts are rare — a few times a decade. Beware software that flags weak imitations; a real thrust needs the full move from deeply oversold to broadly bought in the tight window, ideally with a VIX collapse alongside.

## Interview-ready summary

*"Price is one number; breadth, intermarket and rotation tell me what's underneath it. Breadth measures participation — the advance-decline line, percent of Nifty 500 above the 200-DMA, and new-highs-minus-new-lows. My key signal is divergence: when Nifty makes a new high but the A/D line and % above 200-DMA are lower and new highs are shrinking, the rally is being carried by a few heavyweights and is internally weak — I stop adding longs and hedge, though I wait for price to break a structure level before shorting, because divergences persist. A breadth thrust — the 10-day advance ratio surging from below 0.40 to above 0.615 with VIX collapsing — is my broad bottoming signal. Intermarket sets the risk regime: for India I watch USD/INR, DXY, Brent, the India and US 10-year yields, India VIX and above all FII flow — a rising dollar, spiking crude and FII selling is a risk-off cocktail that pressures Nifty regardless of the chart. Sector rotation, read through relative-strength lines and RRG quadrants, tells me where the money is: cyclicals and banks lead early-cycle, FMCG-pharma-IT lead defensively late-cycle, and I concentrate longs in sectors crossing into the Leading quadrant. I fuse all three with the option chain — a breadth divergence plus heavy overhead call-writing and a falling PCR is a high-conviction top. None of these is a precise entry timer; they're the context layer that keeps me on the right side of the tide and scales my size to the regime."*
