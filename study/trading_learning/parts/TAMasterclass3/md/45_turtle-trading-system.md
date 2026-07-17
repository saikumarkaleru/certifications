# The Turtle Trading System

The Turtle Trading System is the most famous fully-mechanical trend-following system ever made public, and it is the ideal teaching system because every rule is precise, testable, and free of discretion. Its origin is a 1983 bet between two legendary commodities traders, Richard Dennis and William Eckhardt. Dennis believed trading could be *taught* — that great traders are made, not born. Eckhardt disagreed. To settle it, Dennis recruited a group of novices (a lawyer, a card-counter, a security guard, a fantasy-game designer), taught them a complete rule set over two weeks, funded them with real money, and let them trade. He called them "Turtles," after turtle farms he had seen in Singapore ("we're going to grow traders just like they grow turtles"). Dennis won the bet decisively: the Turtles reportedly earned aggregate returns in the tens of millions over the following years, and several went on to run their own funds. The full rules were later disclosed publicly (notably in Curtis Faith's writings and the free "Original Turtle Trading Rules" document), which is why we can study the exact system rather than a reconstruction.

For a technical trader, the Turtle system is a masterclass in how the *whole package* — entry, exit, position sizing, pyramiding, portfolio risk, and correlation limits — matters far more than any single signal. The entries themselves are almost trivially simple **Donchian channel breakouts**. What made the Turtles work was the **risk management architecture** wrapped around those breakouts. This chapter lays out the exact rules, adapts them for Indian markets (Nifty and Bank Nifty futures, MCX crude/gold/silver, liquid F&O stocks), works a full numeric example in rupees, and is honest about the drawdowns and the reasons pure Turtle rules have decayed.

## Origin and idea

The animating idea is **trend following with positive skew**: take many small losses and a few enormous gains. Turtles expected to be *wrong* on well over half their trades. Their edge came entirely from the asymmetry — cutting losers fast at a defined risk unit while letting winners run for months and pyramiding into them. Dennis's second insight was that **volatility must govern position size**. A rupee stop that is fixed in price terms treats a calm market and a violent market identically, which is nonsense. The Turtles normalised every position by the instrument's own volatility (via a measure they called "N," essentially the Average True Range), so that one Nifty contract and one crude contract carried roughly the *same* risk in account terms. That single idea — volatility-based sizing — is arguably the Turtles' most enduring contribution to technical trading and is now standard in professional CTAs.

## Exact rules

### Markets (universe)

The original Turtles traded highly liquid US futures: bonds, currencies, gold, silver, crude, coffee, sugar, and stock-index futures. The principle: **only liquid, trending markets**; avoid illiquid contracts where slippage destroys the edge.

**Indian adaptation:** Nifty 50 futures, Bank Nifty futures, Fin Nifty futures, liquid single-stock futures (Reliance, HDFC Bank, ICICI, Infosys, etc.), and MCX commodities (Crude Oil, Gold, Silver, Natural Gas, Copper). USDINR futures on NSE currency segment also qualify. Avoid thin far-month contracts and illiquid stock futures.

### Volatility: N (the ATR)

**N** is a 20-day exponential moving average of the True Range. True Range (TR) for a day = the greatest of:
- Current High − Current Low
- |Current High − Previous Close|
- |Previous Close − Current Low|

The recursive update the Turtles used:

```
N = (19 × PDN + TR) / 20
```

where PDN is the previous day's N. (Seed with a 20-day simple average of TR.) N is expressed in **points**; multiply by the contract's rupee-per-point to get rupee volatility.

**Dollar/Rupee Volatility** of one contract = `N × (rupees per point)`. For Nifty futures, ₹ per point = **lot size = 75** (as of 2025). So if Nifty's N = 180 points, one contract's rupee volatility = 180 × 75 = ₹13,500.

### Position sizing — the "Unit"

The Turtles sized every trade so that **1 N of adverse move = 1% of account equity**. One "Unit" is:

```
Unit = (0.01 × Account Equity) / (N × rupees per point)
```

**Example:** Account = ₹20,00,000. Nifty N = 180, ₹/point = 75.
Unit = (0.01 × 20,00,000) / (180 × 75) = 20,000 / 13,500 = **1.48 → 1 contract** (round down).

So on this account you trade **1 Nifty lot per Unit**. A more volatile or higher-priced instrument yields fewer contracts per Unit; a calmer one yields more — exactly the volatility-normalisation intended.

### Entries — two Donchian breakout systems

The Turtles ran two systems simultaneously:

| | System 1 (short-term) | System 2 (long-term) |
|---|---|---|
| Entry long | Break of **20-day high** | Break of **55-day high** |
| Entry short | Break of **20-day low** | Break of **55-day low** |
| The filter | Skip the signal if the **last 20-day breakout would have been a winner** | **No filter** — always take the 55-day breakout |
| Exit | Opposite **10-day** extreme | Opposite **20-day** extreme |

The **last-trade filter** on System 1 is subtle and important: if the previous 20-day breakout (whether taken or notional) was profitable, you **skip** the next 20-day signal, entering instead on the 55-day breakout so you never miss a big trend. The logic is that consecutive breakouts often chop; skipping after a winner avoids whipsaw. If the last breakout was a loser, you take the 20-day signal.

### Adding units (pyramiding)

The Turtles did not enter their full size at once. They added Units as the trend moved **in their favour by ½N**, up to a maximum of **4 Units** per market.

**Example (long Nifty), N = 180, so ½N = 90 points.** Suppose entry (first Unit) at 20-day high = **22,000**:

| Unit | Add price | Stop after adding (2N below the *last* fill) |
|---|---|---|
| 1st | 22,000 | 21,640 |
| 2nd | 22,090 | 21,730 |
| 3rd | 22,180 | 21,820 |
| 4th | 22,270 | 21,910 |

Each add is ½N (90 points) above the prior fill. After each add, the Turtles moved the **stop for the entire position** to 2N below the most recent Unit's entry, so all units share a common stop that ratchets up.

### Stops

The hard stop for any Unit is **2N below entry** (for longs). With N = 180, 2N = 360 points. First Unit at 22,000 → stop 21,640. Because each Unit risks 1N (= 1% of equity by construction) and the stop is 2N, the *initial* risk per Unit is 2% — but pyramiding and the common ratcheting stop keep total open risk controlled. A fully-loaded 4-Unit position, after ratcheting, risks roughly 2% of equity, not 8%, because the stop has moved up with the adds.

### Exits

- **System 1:** exit longs on a break of the **10-day low**; exit shorts on a break of the 10-day high.
- **System 2:** exit longs on a break of the **20-day low**; exit shorts on the 20-day high.

These are **trend-following exits** — you give back some open profit to stay in the trend. This is emotionally the hardest rule: exiting a winner not at a target but only when the trend structurally reverses.

### Portfolio risk caps

To stop correlated positions from blowing up the account, the Turtles capped Units:

| Level | Cap |
|---|---|
| Single market | **4 Units** |
| Closely correlated markets (e.g., Gold + Silver; Nifty + Bank Nifty) | **6 Units** |
| Loosely correlated markets | **10 Units** |
| Single direction (all longs or all shorts) | **12 Units** |

And the "**Whipsaw**" drawdown rule: **cut Unit size by 20% for every 10% drawdown** in account equity, rebuilding size as equity recovers. This deleveraging in losing streaks is a key survival mechanism.

## Worked India example (levels and ₹)

Let's trade **Nifty futures**, account = ₹20,00,000, System 2 (55-day).

1. **State:** Nifty consolidating; 55-day high = **22,000**. N = 180 points. ₹/point = 75. Unit = 1 contract.
2. **Entry:** Nifty breaks 22,000 → **buy 1 lot at 22,010**. Stop = 2N below = 22,010 − 360 = **21,650**. Rupee risk = 360 × 75 = ₹27,000 (~1.35% of equity — slightly above 1% because we rounded Unit to a whole lot).
3. **Add 2nd Unit** at +½N: 22,010 + 90 = **22,100**. Move whole-position stop to 2N below 22,100 = 21,740.
4. **Add 3rd** at 22,190, **4th** at 22,280; final common stop = 22,280 − 360 = **21,920**. Now long 4 lots (300 shares-equivalent × ... i.e., 4 × 75 = 300 Nifty units) with average entry ≈ 22,145.
5. **Trend runs.** Over six weeks Nifty rises to **24,600**. The 20-day low (System 2 exit) trails up to **23,900**.
6. **Exit:** Nifty pulls back and breaks the 20-day low at 23,900 → **sell all 4 lots at ~23,880**.
7. **P&L:** average entry 22,145, exit 23,880 → 1,735 points × 75 × 4 = **₹5,20,500** gross (~26% on the account) from one trend. Against this, expect a string of prior −₹27,000 whipsaw losses when breakouts failed — that is the negative-skew tax you pay for the occasional 26% winner.

Contrast a **failed breakout:** Nifty breaks 22,000, you buy at 22,010, it reverses to 21,650, stop hit → −₹27,000 (−1.35%). You take this loss cleanly, often several times, waiting for the trend that pays for them all.

## Backtest / edge notes and realistic costs

The Turtle system's historical edge in the 1980s was real and large, but you must be honest about several things:

- **Positive skew, low win rate.** Expect **35-45% winners**. Psychological tolerance for long losing streaks (10-15 consecutive small losses is normal) is the actual barrier, not the rules.
- **Deep drawdowns.** Even in its heyday the system saw **30-40%+ drawdowns**. The Turtles traded through gut-wrenching equity dips. Any backtest that hides this is lying.
- **Edge decay.** Pure Donchian breakout trend-following has **degraded substantially since the 1990s**. As trend-following capital exploded and markets became more mean-reverting/whipsaw-prone (central-bank intervention, faster information, more counter-trend algos), classic 20/55-day breakouts now show much thinner, choppier returns. This is one of the most-documented cases of alpha decay in public. Treat the *architecture* (volatility sizing, pyramiding, correlation caps) as timeless and the *specific parameters* as a starting point to be tested, not gospel.
- **Costs matter more in India.** Model realistically: brokerage, exchange fees, **STT** (Securities Transaction Tax — on futures it is charged on the sell side), stamp duty, GST on charges, and **slippage** on breakout fills (you are buying strength, so you often pay up). On MCX and index futures the round-trip friction is modest per trade but accumulates across the many small whipsaw trades — a system with a 40% hit rate does a *lot* of trades. Also budget for **overnight gap risk**: Turtle stops are on closing/level basis, and Indian markets can gap through your 2N stop on global news, giving worse-than-modelled fills.
- **Capital requirement.** Proper Turtle diversification needs enough capital to hold Units across many uncorrelated markets. On a small account you cannot diversify and the drawdowns become intolerable relative to size. Undersized accounts are the most common reason retail Turtle attempts fail.

## Adaptations for NSE / F&O

- **Instruments:** index futures (Nifty/Bank Nifty/Fin Nifty), liquid stock futures, MCX commodities, USDINR. Match lot sizes and ₹/point carefully when computing Units.
- **Expiry/rollover:** Indian F&O expires monthly (indices now weekly too). You must **roll** open trend positions to the next series before expiry, choosing liquid contracts and accounting for roll cost — the original Turtles handled this with continuous contracts.
- **Correlation caps are critical here:** Nifty, Bank Nifty, and most large-cap stock futures are highly correlated. A naive Turtle could end up 12 Units long the *same beta*. Enforce the 6-Unit correlated cap strictly, and treat "all index + bank + large-cap longs" as one correlated cluster.
- **Options overlay:** some Indian trend-followers replace the futures leg with **long options or debit spreads** to cap gap risk on the stop side — you lose some trend capture to theta but bound the disaster scenario. This is a defensible modern adaptation, not original Turtle.
- **Parameter re-tuning:** given edge decay, many run **longer channels** (e.g., 40/80 or 55/100) to cut whipsaw, add a **trend filter** (only take longs above the 200-day), or a **volatility regime filter** (stand aside when N is spiking chaotically). Backtest any change honestly, out-of-sample.

## Pitfalls

- **Skipping the risk rules, keeping the entries.** People love the "buy 20-day high" part and ignore the sizing, pyramiding, and correlation caps — which is where 90% of the value lives. Without volatility-based Units you will over-risk volatile instruments and blow up.
- **Under-capitalisation.** Can't diversify → concentrated drawdowns → you quit at the worst time.
- **Abandoning the system in a drawdown.** Trend systems make their money in a few months a year; quitting during the (frequent, long) flat/losing stretches guarantees you miss the payoff trends.
- **Taking profits early / setting targets.** The exits are structural (10/20-day channel), not price targets. Cutting winners at +20% to "book profit" destroys the positive skew that *is* the edge.
- **Ignoring gap and roll risk** in Indian F&O.
- **Curve-fitting the parameters** to recent data to make the equity curve pretty — the fastest way to a system that fails live.

## Interview-ready summary

The Turtle Trading System is Richard Dennis's fully-mechanical trend-following program (from the 1983 Dennis-Eckhardt "can trading be taught?" bet) built on **Donchian channel breakouts** wrapped in rigorous risk management. Entries: **System 1** buys/sells the **20-day** high/low (with a filter skipping the signal if the last breakout won) exiting on the **10-day** opposite extreme; **System 2** trades the **55-day** breakout (no filter) exiting on the **20-day** extreme. Position size is volatility-normalised: **N** = 20-day ATR, one **Unit** sized so 1N of adverse move ≈ 1% of equity, `Unit = 0.01×Equity / (N × ₹per point)`. You **pyramid** up to 4 Units, adding every **½N**, with a hard stop **2N** below entry that ratchets up with each add. Portfolio caps (4 per market, 6 correlated, 10 loosely correlated, 12 per direction) plus a 20%-size-cut-per-10%-drawdown rule control ruin. The edge is **positive skew**: ~40% win rate, many small losses, a few huge trends. Be honest: deep 30-40% drawdowns are normal, and **classic breakout parameters have decayed** since the 1990s — so keep the *architecture* (volatility sizing, pyramiding, correlation limits) and re-test the *parameters* for today's Nifty, Bank Nifty, and MCX markets, budgeting for STT, slippage, gaps, and F&O rollover.
