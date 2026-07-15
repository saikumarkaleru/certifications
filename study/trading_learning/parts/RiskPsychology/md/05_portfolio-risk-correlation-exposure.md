# Portfolio Risk: Correlation, Concentration & Exposure

## Why this matters — the pro vs retail gap this closes

Retail traders size one trade at a time. They set a neat 1% risk on a Reliance long, a 1% risk on an HDFC Bank long, a 1% risk on a Bank Nifty call — and believe they are risking 3%. They are not. On a bad day for the market those three positions move together, and the "3%" turns into a 6-8% hole in minutes. The single most common way a disciplined, stop-loss-following trader still blows up is not a bad trade — it is a *book* full of the same bet wearing different names.

Professionals think at the book level first and the trade level second. Before they ask "is this a good entry?" they ask "what is my total directional exposure, how correlated is it, and what happens to the whole book if Nifty gaps 2%?" This chapter closes that gap: gross vs net exposure, correlation as hidden concentration, position and sector limits, and hedging the tail. (Rules and STT figures below are as of 13-Jul-2026 — verify on NSE/SEBI/your broker, rules change.)

## The essentials — mechanics of book-level risk

**Gross vs net exposure.** Take capital of Rs 10,00,000.
- **Gross exposure** = sum of the *absolute* notional of every position (longs + shorts). It measures how much market you are touching and how much charge/slippage you generate.
- **Net exposure** = long notional minus short notional. It measures your directional bet.

Two books can have the same net but wildly different gross. A pure Rs 5L long is net +50%, gross 50%. A Rs 8L long / Rs 3L short book is *also* net +50% but gross 110% — far more sensitive to single-stock shocks and far more expensive to run.

**Correlation is hidden concentration.** Positions with correlation near +1 are effectively *one* position. In the Indian market the correlations that quietly kill books:

| Cluster | Why they move together |
|---|---|
| Bank Nifty + HDFC Bank + ICICI + SBI + Kotak | The index *is* these names; a long in all is 5x one bet |
| Nifty long + long index futures + short PE | All bullish delta on the same underlying |
| Metals: Tata Steel + JSW + Hindalco + Vedanta | Global commodity cycle, USD, China |
| IT: TCS + Infy + Wipro + HCL | USDINR and US demand |
| "Rate-sensitives" (banks, autos, realty) | Move on the same RBI/yield news |

**Concentration limits (a workable retail frame).** Cap **single-position risk at 1-2% of capital**, **single-underlying at ~5%**, and **one-sector/one-correlated-cluster net risk at ~6%**. Cap **total net risk-on-a-2%-market-move at ~10%** of capital. These are risk-of-loss caps (stop distance x size), not notional.

**Beta-weighting.** Convert everything to Nifty-equivalent delta so you see the true bet. A Rs 3L long in a 1.4-beta stock (say a PSU bank) carries the directional punch of Rs 4.2L of Nifty. Kite/most platforms won't compute this — a simple sheet will.

**Tail hedge.** A cheap far-OTM Nifty/Bank Nifty put (or a put spread) turns an uncapped gap-down into a known cost. You are not trying to profit from it; you are buying a floor on the *book*.

## Worked example — an exposure check on a real book

Capital: **Rs 10,00,000.** Lot sizes used (verify on NSE — they change): Nifty 75, Bank Nifty 35, Reliance 500.

Current positions (13-Jul-2026 hypothetical prices):
1. Long 1 lot Nifty futures @ 24,800 → notional 75 x 24,800 = **Rs 18,60,000**
2. Long 1 lot Bank Nifty futures @ 52,000 → 35 x 52,000 = **Rs 18,20,000**
3. Long 1 lot Reliance futures @ 3,000 → 500 x 3,000 = **Rs 15,00,000**

**Gross exposure** = 18.6 + 18.2 + 15.0 = **Rs 51.8L = 518% of capital.** **Net exposure** = also +518% (all long). This already screams: five-times-levered and one-directional.

**Beta-weight to Nifty.** Bank Nifty beta ~1.15, Reliance beta ~1.1:
- Nifty leg: 18.6L
- Bank Nifty: 18.2 x 1.15 = 20.9L Nifty-equivalent
- Reliance: 15.0 x 1.1 = 16.5L
- **Total Nifty-equivalent long ≈ Rs 56L.**

**Stress test: Nifty −2% day.** Beta-weighted loss ≈ 2% x 56L = **Rs 1,12,000 ≈ 11.2% of capital in a single ordinary down day.** A −4% event (which India has seen on budget/global shocks) ≈ **Rs 2,24,000, −22%.** And note: all three are financial/large-cap high-beta — correlation in a selloff runs toward +0.9, so there is *no* diversification cushion. This is one leveraged bullish bet.

**The fix.**
- Cut to what the limit allows. If the cap is 10% book loss on a 2% move, target ~Rs 50L Nifty-equivalent → drop one leg (exit Reliance; it overlaps Nifty anyway).
- **Buy a tail hedge:** one lot Bank Nifty 50,000 PE, ~30 days out, say premium Rs 300 x 35 = **Rs 10,500** (0.9-1.1% of capital, verify live). Options STT (from 01-Apr-2026) is ~0.15% on premium on the sell/exercise side — on a Rs 10,500 buy the entry STT is negligible; budget exit costs. This caps a gap-down instead of praying through it.
- After the hedge, a −4% day loss shrinks from ~Rs 2.24L toward ~Rs 1.2-1.4L — the put's payoff offsets the crash leg.

## How pros do it / common mistakes

- **They read gross AND net every morning.** High gross with low net still bleeds on charges (brokerage + STT + exchange txn + 18% GST + stamp) and single-name gaps.
- **They collapse correlated names into one line.** "I own five private banks" = "I own Bank Nifty, 5x." Pros would rather express that view *as* Bank Nifty and control size.
- **Classic retail errors:** (1) Counting 5 correlated 1% trades as "5% diversified" — it's one 5% bet. (2) Adding a "hedge" that's actually another bullish position (long Nifty + short PE is *more* long, not hedged). (3) Averaging down a losing sector across three stocks — tripling concentration at the worst time. (4) No plan for a gap: stops don't fill at your price when Nifty opens −3%. (5) Ignoring USDINR/global overnight risk on IT and metals books.
- **Red flags:** every position green together on green days and red together on red days (zero internal diversification); margin utilisation >70% leaving no room for MTM swings; "I'll hedge if it drops" (you won't — do it in advance).

## Checklist / drill

Run this before the market opens, every day:

1. **List every position** with notional and direction.
2. **Gross** = Σ|notional|. **Net** = Σ signed notional. Both as % of capital.
3. **Beta-weight** everything to Nifty-equivalent delta.
4. **Cluster check:** tag each by sector/factor. Any cluster's net risk > ~6% of capital? Trim.
5. **Single-underlying** net risk > ~5%? Trim.
6. **Stress the book:** loss on Nifty −2% and −4%. Is −2% loss ≤ your book cap (e.g., 10%)?
7. **Tail:** if net long/short exceeds your comfort, is a cheap OTM index put/put-spread on? Note its cost as % of capital.
8. **Margin headroom:** utilisation ≤ ~70% so MTM swings don't trigger a forced square-off.

Drill: take your current book, do steps 1-6 on paper, and find the *one* number — beta-weighted net — you were previously ignoring. That number, not any single entry, is what will actually move your account.
