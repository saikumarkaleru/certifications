# PCR Variants & Sentiment Indicators

The Put-Call Ratio is the most quoted and most misunderstood sentiment gauge in the Indian retail world. Every second Telegram channel screams "PCR is 1.5, market is bullish!" or "PCR crashed to 0.6, get ready for a fall!" — and roughly half of them have the interpretation backwards, because PCR is a *contrarian* indicator in some contexts and a *trend-confirming* one in others, and the difference depends entirely on which PCR variant you are reading and where the market sits in its cycle. This chapter dissects every variant that matters on the NSE, gives you the exact construction, and builds them into a sentiment dashboard that has real, honest edge — while being clear that sentiment is a *bias* input, never a standalone trade trigger.

## What PCR Is and the Logic Beneath It

The Put-Call Ratio measures the relative activity or positioning in puts versus calls. The core intuition: puts are (broadly) instruments of bearishness or protection, calls of bullishness or speculation. A high PCR means puts dominate — the crowd is fearful or heavily hedged. A low PCR means calls dominate — the crowd is greedy or complacent.

The contrarian logic follows from a truth every seasoned trader learns painfully: **the crowd is usually wrong at extremes.** When *everyone* has bought puts (PCR very high), the marginal bear has already sold; there is no one left to push the market down, and any good news triggers a violent short-covering rally. When *everyone* has bought calls (PCR very low), the marginal bull is exhausted, and the market is primed to fall. So at *extremes*, PCR is contrarian. In the *middle* of its range, however, a rising PCR during an uptrend can simply reflect healthy hedging and confirm the trend. Context is everything, and the single biggest error is applying the contrarian reading to a mid-range value.

Crucially, in India there is a structural nuance: **retail traders are net option buyers; the smart money (FIIs, prop desks, institutions) are net option sellers.** So a spike in put *buying* (which lifts volume PCR) often represents retail fear — a contrarian bullish tell — while what the sellers are doing is better read through *open interest* and the change in OI. This retail-buyer / institutional-seller split is why you must read PCR variants together, not in isolation.

## The Variants: Construction and What Each Actually Measures

There is no single PCR. There are at least five, and they answer different questions.

**1. PCR (Volume) — PCR-V**

$$\text{PCR-V} = \frac{\text{Total put contracts traded today}}{\text{Total call contracts traded today}}$$

This measures *today's flow* — the intensity of intraday put vs call activity. It is fast, noisy, and best for intraday sentiment and spotting panic. A sudden intraday surge in PCR-V (say from 0.9 to 1.4 within an hour) signals a burst of put buying — often capitulation or a fear spike. Because it resets daily, it is a *momentum-of-sentiment* gauge, not a positioning gauge.

**2. PCR (Open Interest) — PCR-OI**

$$\text{PCR-OI} = \frac{\text{Total put open interest}}{\text{Total call open interest}}$$

This is the most-watched variant. It measures *accumulated positioning* — the standing book of puts vs calls across all strikes. Because OI accumulates, it is smoother and more meaningful for swing bias than PCR-V. On the NSE, Nifty PCR-OI typically oscillates between roughly 0.7 and 1.5 in normal conditions.

**3. PCR by Strike / Max-Pain-adjacent reading**

Rather than one aggregate number, read the OI *distribution*. Where are the fat put walls (support) and fat call walls (resistance)? The **Put-Call OI at specific strikes** tells you where the option-selling institutions expect the index to be pinned. High put OI at 24,500 means sellers are betting Nifty holds above 24,500 — a support shelf. High call OI at 25,000 means sellers expect it capped below 25,000 — a resistance ceiling. The *ratio* of put-to-call OI within the near strikes is a more surgical sentiment read than the aggregate.

**4. Change-in-OI PCR (ΔPCR-OI)**

$$\Delta\text{PCR-OI} = \frac{\text{Change in put OI today}}{\text{Change in call OI today}}$$

This is the sharpest variant for intraday and next-day bias because it captures *what positioning was added or removed today*, not the stale accumulated book. Fresh put writing (put OI rising while price rises) is bullish — sellers confident of support. Fresh call writing (call OI rising while price stalls) is bearish — sellers capping the move. Reading the *change* separates today's conviction from last week's leftover positions.

**5. Stock-level and sectoral PCR**

The same ratios computed on individual F&O stocks (Reliance, HDFC Bank, SBI, Infosys) and on Bank Nifty. Bank Nifty PCR-OI is more volatile and mean-reverts faster than Nifty's. Stock PCR is thinner and noisier but occasionally flags a single-name squeeze.

Here is a comparison table of what each variant is good for:

| Variant | Timeframe | Best use | Noise level | Reading |
|---|---|---|---|---|
| PCR-V (volume) | Intraday | Panic/capitulation spikes | High | Contrarian at extremes |
| PCR-OI | Swing/positional | Standing bias, S/R walls | Low | Contrarian at extremes, trend-confirm mid-range |
| PCR by strike | Any | Precise support/resistance | Medium | Structural (walls) |
| ΔPCR-OI | Intraday/next-day | Fresh conviction | Medium | Directional (who's writing) |
| Stock/Bank PCR | Positional | Single-name/sector squeeze | High (stock) | Contrarian/structural |

## Worked India Example: Reading a Full PCR Picture

Nifty spot 24,700, mid-cycle, a mild uptrend of the past two weeks. You pull the option chain at 2 pm.

- **PCR-OI aggregate: 1.32** — moderately elevated, puts outnumber calls. In a *rising* market, this is *not* a contrarian sell signal; it reflects heavy put *writing* by institutions confident the uptrend holds. Put writers add OI on the put side, mechanically lifting PCR-OI. High-and-rising PCR-OI *within a trend* is bullish confirmation.
- **PCR-V today: 0.85** — today's flow is call-heavy, consistent with the up day.
- **Strike distribution:** biggest put OI at 24,500 (2.1 crore shares equivalent) and 24,600; biggest call OI at 25,000. So the market is *bracketed*: support 24,500-24,600 (put wall), resistance 25,000 (call wall). Max-pain sits around 24,700 — right at spot, typical near expiry.
- **ΔPCR-OI: 1.9** — fresh put writing dominated today. Put sellers *added* aggressively at 24,500 and 24,600. This is the strongest bullish micro-signal: institutions are defending 24,500 with fresh money.

**The synthesis:** the trend is up, put writers are defending 24,500, resistance is 25,000. Bias: bullish while above 24,600, targeting 25,000 where the call wall caps. A dip toward 24,600 is a buy-the-support setup, not a sell. This is *trend-confirming* PCR — mid-range, rising, backed by fresh writing.

**Now the extreme contrarian case.** Two days later, a global risk-off gap sends Nifty to 24,050. You pull the chain:

- **PCR-OI: 1.85** — spiking to an extreme (top decile of its 1-year range).
- **PCR-V: 1.7** — heavy intraday put *buying* (retail panic-hedging).
- **ΔPCR-OI: 2.4** but driven by put *buying* not writing — and simultaneously call OI is being *unwound* (longs exiting).
- **India VIX** jumped from 13 to 22.

Here the reading flips to contrarian. Extreme PCR-OI in the top decile, retail panic put buying (PCR-V spike), and a VIX spike together mark a *fear extreme*. The crowd has bought its insurance; the marginal seller is gone. Historically, Nifty PCR-OI above roughly 1.7-1.8 combined with a VIX spike has been a high-probability short-term bounce zone. The system trade: defined-risk bullish (bull put spread selling the now-fat 23,800 puts), *not* naked, because in a genuine regime break the extreme can get more extreme.

## Beyond PCR: The Full Sentiment Dashboard

PCR alone is a one-legged stool. Combine it with these India-specific sentiment reads:

**Max Pain.** The strike at which the *most* option premium would expire worthless — i.e., where option *sellers* (the winners, statistically) profit most. Price often gravitates toward max pain into expiry (the "pinning" effect), especially on low-event weeks. Not a law, a tendency — driven by delta-hedging flows of the big sellers. Use it as a magnet estimate near Thursday, never as a standalone directional bet.

**FII Index Options / Futures positioning** (from the NSE F&O participant-wise OI data, published daily). This is the gold standard because it shows what the *smart money* is actually doing, not what the crowd's PCR implies. When FIIs are net-long index futures and the retail-driven PCR is screaming fear, the divergence is a powerful contrarian long. (Covered in depth in the FII/DII chapter — but it belongs in your sentiment dashboard.)

**Advance-Decline & breadth** (covered in the breadth chapter) — sentiment confirmation from the broad market.

**India VIX & term structure** (previous chapter) — the price of fear.

**Rollover data** (near expiry) — how much OI rolled to the next series and at what cost, revealing whether longs or shorts have conviction to carry positions forward.

A practical **sentiment scorecard** for daily bias:

| Signal | Bullish reading | Bearish reading | Weight |
|---|---|---|---|
| PCR-OI vs range | Extreme high (contrarian) or rising-in-uptrend | Extreme low (contrarian) or falling-in-downtrend | High |
| ΔPCR-OI | Fresh put writing at support | Fresh call writing at resistance | High |
| FII futures net | Net long / adding longs | Net short / adding shorts | Very high |
| India VIX | Spiking then falling | Rising steadily from lows | Medium |
| Max pain vs spot | Spot below max pain (pull-up) | Spot above max pain (pull-down) | Low-Medium |
| Breadth | A/D positive, broad participation | A/D negative, narrow | Medium |

Score each +1/0/-1, weight, and you get a *bias*, not a signal. The trade trigger still comes from price and structure. Sentiment tells you which side to lean; price tells you when.

## How to Use It for Bias and Timing

- **Trend markets:** read PCR-OI and ΔPCR-OI as *confirmation*. Rising PCR-OI with fresh put writing at rising support = healthy uptrend, buy dips. Rising call writing capping every bounce = downtrend, sell rips.
- **Range markets:** the put wall and call wall from strike-level OI *are* the range. Trade the edges — sell resistance near the call wall, buy support near the put wall — with the OI walls as your invalidation levels. When a wall *breaks* (OI at that strike gets blown through and unwinds), that is a genuine breakout signal.
- **Extremes:** only at genuine extremes (top/bottom decile of the 1-year PCR range) plus a VIX confirmation do you flip to full contrarian. Everywhere else, PCR confirms rather than contradicts.
- **Expiry weeks:** weight max pain and pinning more; PCR-OI gets distorted as positions square off.

## Pitfalls

- **Backwards contrarian application.** Applying "high PCR = buy" to a *mid-range* value of 1.2 in a trending market is the classic retail error. 1.2 in an uptrend is confirmation, not contrarianism. Only *extremes* are contrarian.
- **Ignoring buyer vs seller.** A high PCR-V from retail put *buying* means something opposite to a high PCR-OI from institutional put *writing*. One is fear (contrarian bullish); the other is confident support-building (trend bullish). You must know *who* is on the trade — and change-in-OI plus price action tells you.
- **Stale OI.** Aggregate PCR-OI includes days-old positions. ΔPCR-OI is what changed *today* and is far more actionable for near-term bias. Never trade the aggregate without the delta.
- **Thin-strike noise.** Stock PCR and far-OTM strike OI can be dominated by a single large order. Cross-check volume and bid-ask; don't build a thesis on an illiquid strike.
- **Expiry distortion.** In the last two sessions before expiry, near-month OI collapses as positions roll; PCR readings whipsaw for mechanical reasons. Shift to the next series.
- **Treating sentiment as a trigger.** The deepest pitfall: PCR is a *bias* input. Buying purely because "PCR is high" with no price confirmation is how traders catch falling knives. Sentiment leans you; price and structure pull the trigger. And honestly — most retail traders lose precisely because they invert this, trading the sentiment number and ignoring price.

## Interview-Ready Summary

The Put-Call Ratio comes in variants that answer different questions: **PCR-Volume** (today's flow, fast and noisy, best for intraday panic spikes), **PCR-Open-Interest** (accumulated positioning, the standard swing gauge, ~0.7-1.5 range on Nifty), **strike-level PCR** (locating put walls = support and call walls = resistance), **change-in-OI PCR** (the sharpest read of *fresh conviction* — who is writing where today), and **stock/Bank Nifty PCR**. The interpretation rule is the one most retail traders get wrong: PCR is **contrarian only at extremes** (top/bottom decile — everyone's already positioned, so the market reverses) and **trend-confirming in the mid-range** (a rising PCR-OI in an uptrend reflects institutional put *writing* that defends support, which is bullish). The critical nuance in India is the **retail-buyer / institution-seller split**: a PCR-V spike from retail put *buying* is fear (contrarian bullish), while a PCR-OI rise from institutional put *writing* is confident support-building (trend bullish) — so you must read *who* is on the trade via change-in-OI and price. PCR sits inside a fuller sentiment dashboard alongside **max pain** (the pinning magnet into expiry), **FII futures/options positioning** (the smart-money gold standard), **India VIX** (the price of fear), **breadth**, and **rollover data** — each scored and weighted into a directional *bias*. The unbreakable discipline: sentiment is a bias input, never a standalone trigger; price and structure fire the trade, sentiment only tells you which side to lean, and inverting that order is exactly how the losing majority trades.
