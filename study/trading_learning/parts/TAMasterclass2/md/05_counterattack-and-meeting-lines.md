# Counterattack & Meeting Lines

Some candlestick patterns are famous because they are dramatic; others are neglected because they look ambiguous. The **Counterattack Line** (also called the *Meeting Line*, Japanese: *deai sen* — "lines that meet") belongs to the second group. It is a subtle two-candle reversal that looks, at first glance, weaker than its more famous cousin the engulfing, yet it captures a very specific and tradeable moment: a session that opens with a violent gap continuing the trend, and then reverses so completely that it closes **right back at the previous candle's close.** The two closes "meet." This chapter dissects the counterattack / meeting line, distinguishes it carefully from the piercing pattern and the dark cloud cover it superficially resembles, and shows how to trade it in Indian equities and indices where gap-and-reverse days are common around events, expiry, and global cues.

## What it is & why it works

There are two forms.

A **Bullish Counterattack (Meeting) Line** appears in a downtrend. The first candle is a long black (red) candle in the direction of the trend. The next day, the market **gaps down sharply** at the open — continuing the panic — and then rallies all day to close **at or very near the previous candle's close.** So you have a long red candle, then a long green candle whose *close* meets the prior *close*, but whose *open* was far lower (the gap).

A **Bearish Counterattack (Meeting) Line** appears in an uptrend. The first candle is a long white (green) candle. The next day gaps up sharply (euphoric continuation), then sells off all day to close **at or near the prior candle's close.** A long green candle, then a long red candle whose close meets the prior close, but which opened far higher.

Why does the "closes meeting" matter? Consider the bullish case. The trend is down; sellers are confident. The gap-down open *rewards* that confidence — shorts are in profit at the open, late longs are panicking. Then, over the session, buyers absorb everything and drive price all the way back up to yesterday's close. By the end of the day, **the entire panic gap has been erased** and price is exactly where it closed yesterday. The message: the sellers threw their best punch (the gap) and it was completely neutralised. That failure of the down-gap to hold is the reversal signal. The pattern's Japanese name — "lines that meet" — captures the idea that the two closes shake hands, signalling a standoff that has broken the trend's momentum.

The counterattack is the "weaker sibling" of two stronger patterns:
- The **Piercing Pattern** (bullish) requires the second candle to close *above the midpoint* of the first candle's body — deeper penetration, stronger signal.
- The **Bullish Engulfing** requires the second candle to close *above the first candle's open* — total domination.

The counterattack only requires the close to return to the *previous close*. So it is the *least* penetrating of the three — which is exactly why it needs strong confirmation and why many traders overlook it. But it has one thing the others lack: the **gap.** A counterattack line demands a genuine gap open in the trend direction that then fails. That gap-and-fail is a specific, high-information event — an intraday exhaustion of the trend — that the engulfing (which need not gap) does not require.

## Mechanics, settings & identification

Strict definition for a **Bullish Counterattack Line:**
- Prior trend: down.
- Candle 1: long red (black) body, in the trend direction.
- Candle 2: opens with a clear **gap down** below Candle 1's low (or at least a sharp gap down from C1's close), then closes back up.
- Candle 2's **close ≈ Candle 1's close** (within a small tolerance, typically a few ticks / < ~0.3-0.5%).
- Both candles are relatively long; small bodies dilute the signal.

For a **Bearish Counterattack Line**, invert: uptrend, long green C1, gap-up open on C2, then C2 closes back down to ≈ C1's close.

**Tolerance for "meeting."** The two closes rarely match to the paisa. In practice, treat closes within ~0.25-0.5% of each other (on a daily stock chart) as "meeting." If you widen the tolerance too far, every reversal looks like a counterattack; too narrow and you'll never find one. On indices, a few points on Nifty (say within ~0.15%) is reasonable.

**Distinguishing from piercing / dark cloud.**
- If C2 closes *at* C1's close → **counterattack.**
- If C2 (green) closes *above the midpoint* of C1's red body → **piercing** (stronger).
- If C2 (green) closes *above* C1's open → **bullish engulfing** (strongest).
The three form a spectrum of penetration. Recognising which one you have tells you how strong the reversal claim is.

**Screening.** Counterattack lines are hard to scan cleanly because "close ≈ prior close" plus "gap open" is a compound condition. On Chartink, approximate the bullish version with: prior candle red and long, latest candle green, latest open < prior low (gap down), and `abs(latest close - prior close) / prior close < 0.004`. Expect few, noisy hits — always eyeball the chart.

**Timeframe.** Most reliable on the **daily** chart where the gap carries overnight information. It also appears intraday on index futures around news spikes (a gap on the 15-minute open that fully reverses to the prior bar's close), but intraday counterattacks are noisier.

## Worked India example (levels & ₹)

**Bullish counterattack — reconstructed on Reliance Industries** (verify on your own chart). Suppose RIL has been sliding on weak global energy cues and broader market weakness, dropping from ₹2,980 to ₹2,820 over a week. Thursday prints a long red candle: open ₹2,845, close ₹2,812 — a decisive down day. Overnight, crude spikes and US markets sell off; Friday RIL **gaps down and opens at ₹2,782** (below Thursday's low), and shorts are jubilant. But through the session, value buyers and delivery-based buying step in; RIL grinds higher all day and closes at **₹2,814** — essentially Thursday's close of ₹2,812. The two closes *meet.*

What happened: the market gapped down 30 points in panic, and buyers erased the entire gap by the close, dragging price back to exactly where it ended the day before. The sellers' strongest move (the gap) failed completely. On above-average volume and near a prior support shelf around ₹2,800, this is a valid **bullish counterattack** flagging a probable short-term bottom. Note it is *weaker* than a piercing line would be — RIL only got back to the prior close, not past the red candle's midpoint — so confirmation (a green day above Friday's high) is essential before committing size.

**Bearish counterattack — reconstructed on Nifty near a top.** Suppose Nifty has rallied from 23,800 to 24,500 into a global risk-on wave. Tuesday prints a long green candle: open 24,420, close 24,495. Wednesday, on a strong SGX/GIFT Nifty lead, Nifty **gaps up and opens at 24,560**, euphoria everywhere. But FIIs sell into strength, and the index falls all day to close at **24,498** — right at Tuesday's close of 24,495. The gap-up was fully reversed; the closes meet. That is a **bearish counterattack** at resistance, warning that the up-gap failed and momentum has stalled. Confirmation would be a red day below Wednesday's low.

## How to trade it — entry, stop, target

Because the counterattack is the *weakest-penetrating* of the reversal trio, discipline around confirmation and stops is non-negotiable.

**Bullish counterattack (long):**

| Element | Rule |
|---|---|
| Trigger | Do **not** buy at C2's close alone. Wait for confirmation: a next-day break **above C2's high** (RIL > Friday's high, say > ₹2,835), or a strong follow-through green candle. |
| Stop | Below **C2's low** (the gap low, ₹2,782) — the lowest point the reversal defended. A break below it means sellers regained the gap. |
| Target 1 | Prior swing / measured move ≈ 1.5-2x risk. If entry ₹2,835 and stop ₹2,780, risk ~₹55, T1 ≈ ₹2,920-2,960. |
| Target 2 | Larger resistance; trail with a moving average. |
| Timeframe | Daily swing. |
| Regime | Best when the broader market is stabilising; a counterattack against a violently trending index is lower-odds. |

**Bearish counterattack (short / exit):**

| Element | Rule |
|---|---|
| Trigger | Confirmation via a break **below C2's low** (Nifty < Wednesday's low). Use it also to exit longs / hedge immediately. |
| Stop | Above **C2's high** (the gap-up high, 24,560). |
| Target | Prior support / measured move; on an index, buy puts or a bear put spread rather than naked shorts. |
| Timeframe | Daily swing. |

The single most important rule: **the counterattack demands confirmation.** Unlike an engulfing (which already shows domination) the counterattack only shows a *standoff.* You are trading the *failure of a gap*, not a proven takeover. Waiting one candle for confirmation filters out the many counterattacks that fail — and there are many.

## Confluence (including OI)

- **Support/resistance & round numbers.** A bullish counterattack whose gap low taps a well-tested support (RIL ₹2,800; Nifty 24,000) is far more reliable. The confluence of "gap into support that then reverses" is much stronger than a counterattack floating in mid-air.
- **Volume.** The reversal candle (C2) should carry above-average volume — it takes real buying to erase a panic gap and drag price back to the prior close. Thin-volume counterattacks are suspect.
- **The gap size.** A meaningful gap that fully reverses is the whole point. If the "gap" is trivial, you don't really have a counterattack — you have two ordinary candles.
- **Momentum divergence.** A bullish counterattack coinciding with a bullish RSI divergence (price lower low, RSI higher low) is a high-conviction combination.
- **Option chain / OI.** On an index bullish counterattack near support, check for heavy **Put writing** at that strike (writers defending the level as the gap reverses up) and **Call unwinding** overhead. On a bearish counterattack at resistance, look for aggressive **Call writing** at the top strike and Put unwinding — sellers pressing the level as the up-gap fails. In F&O stocks, watch futures OI: a bullish counterattack with **short covering** (price up, OI down) can be a quick bounce; with **fresh longs** (price up, OI up) after confirmation it can sustain.

## Pitfalls

1. **Trading it without confirmation.** The cardinal sin. The counterattack is a standoff, not a knockout. Always wait for the follow-through candle.
2. **Loose "meeting" tolerance.** If you let the closes be "roughly near" each other, you'll label half your reversals as counterattacks and dilute the edge. Keep the tolerance tight (≈ ¼-½%).
3. **Confusing it with piercing/engulfing.** People often mis-call a piercing line a counterattack. They're different strengths. If C2 pushed *past* the midpoint or the open, you have a *stronger* pattern — recognise and trade it as such.
4. **No real gap.** Without a genuine trend-direction gap on C2, it isn't a counterattack. The failed gap is the signal.
5. **Illiquid stocks.** In thin names, a "gap and reverse to prior close" can be a print/liquidity artifact, not real order flow. Demand liquidity and volume.
6. **Fighting a strong trend.** A single counterattack rarely reverses a powerful, news-driven trend. In strong trends, treat it as a possible pause, not a reversal, and demand extra confirmation.

## Interview-ready summary

A Counterattack (Meeting) Line is a two-candle reversal in which the second candle **gaps in the trend's direction and then closes back at the previous candle's close** — the two closes "meet." Bullish version: downtrend, red candle, gap-down open that rallies back to the prior close. Bearish version: uptrend, green candle, gap-up open that sells back to the prior close. It signals that the trend's strongest thrust (the gap) failed completely within the session. It is the *weakest-penetrating* member of the reversal family — weaker than piercing (past the midpoint) and engulfing (past the open) — so it **requires confirmation** (a follow-through break of the reversal candle's high/low), a tight "meeting" tolerance, real gap size, volume, and location at support/resistance. Confirm on indices with supportive option-chain OI shifts (put/call writing and unwinding). Trade the confirmation, stop beyond the reversal candle's extreme, and never mistake a standoff for a knockout.
