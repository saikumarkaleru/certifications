# Mean-Reversion Systems

## Origin & idea

Momentum and mean-reversion are the two opposing engines of the market, and a complete technical toolkit needs both. Momentum says "what has moved will keep moving." Mean-reversion says "what has stretched too far will snap back." The trick — and the reason most traders fail at one or the other — is that these edges live on *different timescales* and in *different regimes*. Momentum dominates over months. Mean-reversion dominates over days and in range-bound, high-liquidity conditions. Run a mean-reversion system in a runaway trend and it will hand you your account.

The intellectual origin runs deep. In 1985, De Bondt and Thaler showed that extreme stock losers over 3–5 years outperformed extreme winners over the next few years — long-horizon reversal driven by over-reaction. But the tradable, high-Sharpe version of mean-reversion lives at the *short* end: 1–5 day reversals in liquid instruments. When a liquid stock or index gaps down hard on no fundamental change, short-term liquidity providers and dip-buyers step in, and price often "reverts to the mean" — typically a short moving average or the prior range. The behavioural driver is over-reaction and forced selling (margin calls, stop cascades, panic), which temporarily pushes price below fair value; the mechanical driver is that market-makers and arbitrageurs are paid to lean against extremes.

Larry Connors turned this into a cottage industry of rules — RSI(2), the "%b" band trades, the "3-day high/low" systems — most of which share one DNA: buy short-term weakness *inside* a longer-term uptrend, sell the bounce. That "buy the dip, but only in an uptrend" nuance is everything. It is the filter that separates a profitable system from catching a falling knife.

For India, mean-reversion has a natural home: the index and its most liquid large-caps. Nifty 50, Bank Nifty, and the top F&O stocks are deep enough that panic dips genuinely over-shoot and snap back, and F&O gives you clean, cheap ways to express the trade with defined risk. This chapter builds mean-reversion into an exact, tradable system.

## The logic and its preconditions

A mean-reversion edge exists only when three conditions hold, and you must build the system to enforce all three.

1. **Liquidity.** Reversion needs someone to lean against the extreme. In illiquid small-caps, a "dip" is often the start of a repricing — there is no one to catch it. Trade only Nifty, Bank Nifty, Fin Nifty, and the top ~30 F&O large-caps.
2. **A longer-term uptrend (for long trades).** You buy dips *within* an uptrend because the drift is your tailwind. Buying dips in a downtrend is just being early to a crash. The classic filter: price above the 200-DMA.
3. **A genuine short-term stretch.** Not just "a red day" — a statistically unusual move: RSI(2) below 5, or a close two standard deviations below a short mean, or a close below the lower Bollinger band. The rarer the stretch, the better the reversion odds.

The mirror image applies to shorts: sell short-term over-extension *within* a downtrend. In Indian equities, structural upward drift and the difficulty/cost of shorting cash stock mean the long side is usually the bread-and-butter; shorts are best expressed on the index via futures/options.

## Exact rules — an RSI(2) index mean-reversion system

Here is a fully specified system on Nifty and Bank Nifty, the two cleanest instruments.

### Universe & vehicle

| Component | Choice |
|---|---|
| Instruments | Nifty 50 and Bank Nifty (index) |
| Vehicle | Long via near-month futures, or long ATM/ITM call debit spread for defined risk |
| Timeframe | Daily bars; intraday for entry refinement |

### Signal construction

RSI(2) is a 2-period Wilder RSI — an extremely fast oscillator that spends most of its time near 50 and only spikes to extremes on genuine short-term exhaustion.

| Parameter | Value |
|---|---|
| Trend filter | Close > 200-DMA (longs only) |
| Setup trigger | RSI(2) < 5 (deep oversold) |
| Secondary confirm | Close below lower Bollinger Band (20, 2.0) |
| Entry | Buy on the close of the trigger day, or next-open |
| Exit (primary) | Close > 5-DMA (mean recaptured) |
| Time stop | Exit after 5 trading days regardless |
| Hard stop | Close below the trigger day's low − 1×ATR(10) |

### Position sizing

Mean-reversion has a specific risk shape: many small wins, occasional large losses when a "dip" becomes a trend break. So size for the tail, not the average.

Risk per trade = 0.75% of capital. Position size = (0.75% × capital) / (stop distance in points × point value). On Nifty futures (lot value large), you may need the options version to size down to 0.75% on a small account.

### The full rule table

| Step | Long rule |
|---|---|
| 1. Regime | Nifty close > 200-DMA |
| 2. Trigger | RSI(2) < 5 |
| 3. Confirm | Close < lower Bollinger(20,2) |
| 4. Entry | Buy near close / next open |
| 5. Stop | Trigger low − 1×ATR(10) |
| 6. Target | Close > 5-DMA → exit |
| 7. Time stop | 5 bars max |
| 8. Sizing | Risk 0.75% of capital |

The elegance is that there is no fixed profit target in points — you exit when the *reason* for the trade (price below its short mean) is resolved. Mean-reversion trades should be *short in duration*; a reversion trade that is still open after a week has usually failed.

## Worked India example

Nifty is in a clear uptrend, trading at 24,600, comfortably above a 200-DMA around 22,800. Over three sessions a global risk-off spooks the market: Nifty falls from 24,900 to 24,150, closing near the day's low. That third day:

- RSI(2) has collapsed to ~3 (below the 5 threshold). ✔
- The close of 24,150 is below the lower Bollinger band (20,2), which sits around 24,300. ✔
- Regime filter: 24,150 is still well above the 200-DMA at 22,800. ✔

All three conditions align. You enter long.

- **Vehicle (defined risk):** buy a Nifty 24,200/24,400 call debit spread expiring the following week for a net debit of, say, ₹90 (×50 = ₹4,500 per lot risk). Or, for a futures trade, go long one lot near 24,150.
- **Stop (futures version):** trigger day low was 24,120; ATR(10) ≈ 220. Stop = 24,120 − 220 = 23,900 on a *closing* basis. Point risk ≈ 250 points.
- **Sizing:** on a ₹10 lakh account, 0.75% = ₹7,500 risk. Nifty futures at ₹250/point risk means ~₹12,500 risk per lot — too big; use the spread version (risk ₹4,500/lot) and take 1 lot, or trade the mini/adjust. This is exactly why the options expression matters for retail sizing.
- **Management:** two days later, the panic exhausts, buyers step in, Nifty rallies to 24,550 and closes above its 5-DMA (~24,450). The exit trigger fires. Close the trade. The debit spread, near max value, is worth ~₹180 (×50 = ₹9,000), a ₹4,500 gain on ₹4,500 risk — roughly +1R in three days.

Now the failure case, which you must rehearse: instead of bouncing, the next day gaps down and Nifty closes 23,850 — below your 23,900 stop. You exit at the close for a −1R loss. No revenge trade, no averaging down. The whole system's profitability depends on taking that stop mechanically, because the losses that kill mean-reversion traders are the ones they refuse to cut, hoping for "the bounce that always comes." It does not always come.

## Backtest / edge notes & realistic costs

Short-term index mean-reversion on liquid instruments historically shows a high hit rate (often 65–75% of trades win) with small average wins and larger occasional losses — a classic "picking up coins" profile with positive but lumpy expectancy. Several honest caveats:

**The win rate is seductive and dangerous.** A 70% win rate makes traders over-confident and over-size. Then one −4R gap-down (the system's characteristic tail) wipes out ten wins. The edge is real only if you respect the stop and size for the tail. Mean-reversion blows up accounts far more often through *sizing* than through bad signals.

**Costs matter, but less than in momentum.** These are index trades held 1–5 days, not high-frequency churn. Round-trip on Nifty futures is cheap relative to the point-move captured. Options spreads cost more in bid-ask but cap the tail. Because trades are few (maybe 2–5 setups a month per instrument) and directional edge per trade is decent, cost drag is modest — perhaps 0.05–0.15R per trade.

**Regime is destiny.** The single biggest determinant of whether this system prints money this year is whether the market is *ranging/choppy* (mean-reversion heaven) or *trending hard* (mean-reversion hell — every dip in a runaway rally gets bought too early, and every over-extended reading in a crash keeps extending). The 200-DMA filter helps but does not immunise you. In a March-2020-style waterfall, RSI(2) is oversold for two straight weeks while price halves; the filter (price below 200-DMA) correctly blocks longs, which is the point — but a naive version without the filter would have been destroyed. Build the regime filter and trust it.

## Adaptations for NSE / F&O

- **Sell puts instead of buying futures.** A cleaner Indian expression of "buy the oversold dip" is to *sell* an out-of-the-money put on the oversold index/stock, collecting the fat premium that panic inflates (IV spikes on down-moves). You get paid for the reversion via elevated implied volatility. Manage as a defined-risk put spread to cap tail risk.
- **Stock-specific reversion.** Apply the same RSI(2)+200-DMA logic to the top F&O large-caps (Reliance, HDFC Bank, ICICI, Infosys, etc.) for a diversified basket of small mean-reversion trades — diversification smooths the lumpy equity curve materially.
- **Bank Nifty is higher-octane.** Bank Nifty mean-reverts sharply but also *trends* violently; tighten the regime filter and reduce size versus Nifty.
- **Expiry-week distortions.** Around weekly/monthly expiry, index behaviour is dominated by option positioning, not clean reversion. Either skip signals in the last two sessions before expiry or size down.

## Confluence — sharpening the edge

- **Support confluence:** a reversion trigger that also lands on a prior swing low, a big round number (Nifty 24,000), or the VWAP-anchored value area has better odds.
- **Breadth washout:** an oversold trigger accompanied by a breadth extreme (very high % of stocks below their 10-DMA, a spike in the India VIX) marks genuine capitulation — the best reversion setups.
- **Divergence:** price making a lower low while RSI(2)/RSI(14) makes a higher low signals selling exhaustion and strengthens the long.
- **Avoid news craters:** a dip caused by a specific structural shock (a bank blowing up, a policy shock) is not the noise-driven over-reaction the system is built for. Reversion assumes *no change in fundamentals* — respect that assumption.

## Pitfalls

- **Catching knives.** Removing the trend filter to "buy cheaper" is the classic account-killer. The filter is non-negotiable.
- **Averaging down.** Adding to a losing reversion trade converts a defined −1R into an undefined disaster. Never scale into a loser here.
- **Holding past the time stop.** A reversion trade that hasn't reverted in 5 days is a failed trade wearing a disguise. Exit on time.
- **Over-sizing on the high win rate.** The math of a 70% win / large-tail-loss system is unforgiving to leverage. 0.75% risk, tops.
- **Trading illiquids.** Small-caps do not reliably revert — they gap and repricing. Liquid instruments only.
- **Ignoring IV.** In options expressions, buying premium *after* IV has spiked on the panic can mean you're right on direction and still lose to IV crush. Prefer selling premium or using spreads when IV is elevated.

## Interview-ready summary

Mean-reversion systems monetise short-term over-reaction: liquid instruments that stretch too far from a short mean tend to snap back within days. The tradable, high-Sharpe version lives at the 1–5 day horizon, not the multi-year De Bondt–Thaler horizon. The canonical rules — Connors-style — are: buy short-term oversold (RSI(2) < 5, close below the lower Bollinger band) *only within a longer-term uptrend* (price > 200-DMA), enter near the close, exit when price recaptures its 5-DMA, with a hard ATR-based stop and a 5-bar time stop. The trend filter that restricts you to buying dips inside uptrends is the whole edge — it is what stops you catching falling knives. On NSE you express it on Nifty and Bank Nifty via futures or, better for retail sizing and tail control, via call debit spreads or by selling puts into the IV spike. The profile is a high win rate with a fat left tail, so the account-preserving discipline is small size (~0.75% risk), a respected stop, and no averaging down. Its performance is regime-dependent: it thrives in choppy/ranging markets and suffers in strong trends, which is exactly why every serious book pairs a mean-reversion system with a momentum system — the two harvest opposite regimes.
