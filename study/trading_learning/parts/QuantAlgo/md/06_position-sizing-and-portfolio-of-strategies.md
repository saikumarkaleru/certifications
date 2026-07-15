# Position Sizing & Portfolio of Strategies

## Why this matters

You can be right on direction and still go broke. Retail traders obsess over *entries*; professionals know that **position sizing and portfolio construction dominate long-run returns and survival**. Two traders with the identical signal — one sizing 2% risk per trade, the other going "full margin" — have completely different fates: one compounds, the other blows up on the first 6-loss streak that any real edge inevitably produces. In Indian F&O, where SPAN+Exposure margin is fully upfront and peak-margin is enforced, sizing is also a *hard constraint*: you literally cannot deploy what the margin system won't let you. And once you run more than one strategy (previous chapter), the question shifts from "how big is this trade" to "how much of my capital does each *system* get, given how they correlate." That portfolio question is where the free lunch of diversification lives.

## The essentials

**Fixed-fractional (risk-per-trade).** Risk a fixed fraction *f* of equity per trade. Position size = (equity × f) ÷ (per-unit risk to stop). Typical f = 0.5%–2%. This auto-scales: you bet more as you win, less as you lose. It is the retail-safe default.

**Volatility targeting.** Instead of fixed rupees, size so each position contributes the same *risk*. Target an annualised portfolio vol (say 15%). Position notional = (target vol ÷ instrument's realised vol) × capital ÷ n. When Bank Nifty's vol doubles, you halve the lots — this keeps risk stable across calm and stormy regimes, and is how most pro futures books run.

**Kelly criterion.** The growth-optimal fraction. For a simple bet, `f* = edge/odds = p − (1−p)/b` where p = win prob, b = win/loss payoff ratio. Kelly *maximises long-run compounding* but is wildly volatile — full Kelly routinely draws down 50%+. Because your estimated edge is uncertain and Kelly is brutal when you overestimate it, pros use **fractional Kelly**: half-Kelly or quarter-Kelly. Half-Kelly keeps ~75% of the growth for ~half the volatility. Nobody serious trades full Kelly.

**Correlation between strategies.** Diversification benefit depends on correlation ρ. Two strategies each with vol σ, combined 50/50, have portfolio vol `σ·√((1+ρ)/2)`. At ρ=0 that's σ×0.71 (29% vol reduction for free). At ρ=1 you get nothing. This is *the* reason to run trend + mean-reversion together — they're often negatively correlated.

**Capital allocation & risk parity.** Naive allocation splits *capital* equally; **risk parity** splits *risk* equally, so each strategy contributes the same volatility to the book. A low-vol pairs system then gets more capital than a high-vol momentum system, so one doesn't dominate the P&L.

| Method | Sizes on | Best for | Watch out |
|---|---|---|---|
| Fixed-fractional | Distance to stop | Single discretionary/systematic trader | Ignores changing vol |
| Vol targeting | Realised volatility | Futures/multi-instrument books | Needs a vol estimate; lags jumps |
| Fractional Kelly | Edge & odds | Known, stable edge | Overestimating edge → ruin |
| Risk parity | Each strategy's vol | Portfolio of systems | Correlations drift/spike in crises |

*All margin/tax mechanics as of July 2026 — verify on NSE/SEBI/your broker; rules change.*

## Worked example

**Capital ₹15,00,000. Fixed-fractional at f = 1% → ₹15,000 risk per trade.** Bank Nifty future, lot = 15 units, spot 52,000. Your system's stop is 300 points away → per-lot risk = 300 × 15 = ₹4,500. Lots = ₹15,000 ÷ ₹4,500 = 3.3 → **3 lots**. SPAN+Exposure margin ≈ ₹1.6–1.9 lakh/lot, so 3 lots ≈ ₹5.4 lakh margin — comfortably within ₹15 lakh. Note the *risk* (₹13,500) is far below the *margin* (₹5.4 lakh): margin is a collateral requirement, risk is what you actually stand to lose to your stop. Confusing the two is a classic error.

**Fractional Kelly check.** Suppose the system wins 45% of the time with a 2:1 payoff (b=2). Full Kelly f* = 0.45 − 0.55/2 = 0.45 − 0.275 = **0.175 (17.5%)**. That is insanely aggressive — a 17.5% risk-per-bet system will have gut-wrenching 50%+ drawdowns. Quarter-Kelly = **~4.4%**, still above our 1% choice. So 1% is conservative relative to Kelly — deliberately, because the 45%/2:1 estimate is itself uncertain.

**Portfolio of two systems, risk parity.** System A (trend, index futures) vol 20% p.a.; System B (mean-reversion) vol 12% p.a.; correlation ρ = −0.2. Risk-parity weights ∝ 1/vol → A : B = (1/20):(1/12) = 0.375 : 0.625. Combined vol with ρ=−0.2 is roughly `√(wA²·20² + wB²·12² + 2·wA·wB·20·12·(−0.2))` ≈ √(56.25 + 56.25 − 22.5) ≈ √90 ≈ **9.5% p.a.** — *lower than either standalone system*. Same expected return, one-third less volatility: that is the diversification free lunch, and why allocating across uncorrelated families beats leveraging one.

## How pros do it / common mistakes

- **Pros size on risk, not on margin or "conviction."** They compute rupees-at-risk to the stop first, then check margin as a constraint.
- **They cap total portfolio risk**, e.g. no more than 6% of equity at risk across all open positions, and a per-strategy cap so no single system can sink the book.
- **They use fractional Kelly** and treat their estimated edge as optimistic. If in doubt, they *underbet*: half-Kelly loses little growth, full-Kelly plus a bad estimate is ruin.
- **They monitor correlation, knowing it spikes in crises.** Diversification that shows ρ=0 in calm markets can jump toward 1 in a crash — so they stress-test with correlations forced to +0.5.
- **Retail mistakes:** sizing to max margin ("3 lots because I can afford 3 lots"); adding to losers (anti-Kelly); running two "different" strategies that are secretly the same momentum bet (ρ≈0.9, zero diversification); ignoring that a 2% edge with 5% sizing blows up on a normal losing streak.
- **Red flags:** any single trade risking >2–3% of equity; total open risk you can't state in rupees; a "diversified" book where all systems drop together.

## Checklist / drill

1. What is my **rupees-at-risk per trade** (equity × f ÷ per-unit stop distance)?
2. Is that within my **per-trade cap** (≤2%) and **total portfolio cap** (≤6%)?
3. Does **margin** allow the position — and am I not confusing margin with risk?
4. If sizing by Kelly, am I using **≤half-Kelly** and treating my edge estimate as optimistic?
5. Across strategies, what are the **pairwise correlations**, and does the book survive them all going to +0.5?

**Drill:** Take two of your backtested systems' daily-return series. Compute each one's volatility and their correlation. Build (a) equal-capital and (b) risk-parity portfolios; compare portfolio vol and max drawdown. Then re-run with correlation forced to +0.5 to see how much of the "diversification" was real. Feeling the equity curve smooth out at low correlation — and roughen at high — is the entire lesson.
