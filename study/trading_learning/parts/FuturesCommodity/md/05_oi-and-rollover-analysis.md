# Open Interest & Rollover Analysis Across F&O

## Why this matters

Price tells you *what* happened. Open interest (OI) tells you *how much money committed to it* and whether that commitment is fresh, being reinforced, or running for the exit. This is the retail-vs-pro gap in derivatives: retail traders stare at candles alone; pros read price *and* OI together, plus the once-a-month rollover ritual that reveals where the smart money is positioning for next month. You already know Greeks and strategies from your options book — this chapter is about the *positioning tape* that sits underneath the whole F&O market, and it is India-specific because our monthly expiry (last Thursday) and rollover cycle create a rhythm you can trade around.

Honest caveat: OI is a lagging, aggregate number. It is a *confirmation and context* tool, not a crystal ball. Anyone selling you "OI = guaranteed direction" is selling you a story.

## The essentials

Open interest = total number of outstanding (not-yet-closed) contracts. It rises when a *new* buyer and a *new* seller create a contract; it falls when existing holders close. Volume counts trades; OI counts live positions. Both matter.

The four canonical OI read-ups combine the direction of **price** and the direction of **OI** in the *futures*:

| Price | OI | Interpretation | Who is aggressive |
|-------|-----|----------------|-------------------|
| Up | Up | **Long build-up** | Fresh longs, bullish |
| Down | Up | **Short build-up** | Fresh shorts, bearish |
| Up | Down | **Short covering** | Shorts exiting (weaker up-move) |
| Down | Down | **Long unwinding** | Longs exiting (weaker down-move) |

Key nuance pros insist on: build-up (OI rising) is *conviction*; unwinding/covering (OI falling) is *position closing*. A rally on short-covering is less trustworthy than a rally on long build-up because covering is finite — once shorts are out, the fuel is gone.

**PCR (Put-Call Ratio)** = total put OI ÷ total call OI (OI-based is standard; a volume-based version also exists). Rough Indian rules of thumb (Nifty): PCR ~0.7–1.0 is neutral; >1.3 crowd is heavily put-heavy (often read as *support* / contrarian-bullish); <0.6 call-heavy (froth / contrarian-bearish). Treat it as sentiment temperature, not a signal on its own.

**Option OI as S/R:** the strike with the highest *call* OI acts as a resistance/ceiling; highest *put* OI acts as support. **Max-pain** is the strike at which the *maximum number of option buyers lose* (i.e., total option-holder payout is minimised); price is often said to drift toward it near expiry. It's a weak, expiry-day tendency — useful as context, not a trade trigger.

**Rollover** happens in the last week before expiry: traders move positions from the near month to the next month. Two numbers matter, published by NSE and brokers:
- **Rollover %** = positions rolled to next month ÷ total near-month positions expiring. High roll % (e.g., Nifty > ~75–80%, stock > 3-month average) = strong conviction to carry the trade forward.
- **Rollover cost / spread** = (next-month price − near-month price), often annualised. A rising positive spread on a stock alongside high roll % = bullish carry (people paying up to stay long).

All figures below are illustrative for method; **verify live OI, PCR, roll % on NSE (nseindia.com) / your broker — rules and lot sizes change.**

## Worked example — reading Bank Nifty futures OI

Assume Bank Nifty futures lot size **15** (verify on NSE — lot sizes are revised periodically). Over a session:

| Time | Fut price | Fut OI | Δ Price | Δ OI | Read |
|------|-----------|--------|---------|------|------|
| 9:20 | 51,000 | 22.0 L | — | — | base |
| 11:00 | 51,350 | 23.6 L | +350 | +7.3% | **Long build-up** — fresh bullish money |
| 13:00 | 51,180 | 23.9 L | −170 | +1.3% | Mild **short build-up** on the dip |
| 15:00 | 51,520 | 22.8 L | +340 | −4.6% | **Short covering** — shorts trapped, squeezed out |

Story: bulls committed in the morning (build-up), bears tried the midday dip (small short build-up), and the late rally was those trapped bears *covering* — a squeeze, not fresh buying. A pro treats the 15:00 pop with suspicion: covering rallies fade once shorts are flat.

Now overlay options for expiry-week context: highest call OI at 52,000 (ceiling), highest put OI at 51,000 (floor), PCR 1.15 (mildly supportive), max-pain 51,300. Bias: range 51,000–52,000, gravity near 51,300. One rupee = one index point; a 500-point favourable move on one lot = 500 × 15 = **₹7,500** gross, before costs.

Cost reality on that Bank Nifty futures lot (~₹51,000 × 15 = ₹7.65 L notional): STT ~0.05% on sell side only (from 01-Apr-2026) ≈ ₹383 on exit; plus brokerage (often flat ₹20/order), exchange txn, SEBI fee, stamp duty, and 18% GST on brokerage+txn. Round-trip friction is small vs a big move but lethal on churned, low-conviction "OI scalps." **Verify current STT/charges on your broker's contract note.**

## How pros do it / common mistakes

**How pros do it**
- Read futures OI *with* price for the *underlying*, then confirm with cash-market volume — never OI in isolation.
- Weight **build-up over unwinding**: a trend backed by rising OI is more durable than one on covering.
- Use rollover week as a *conviction gauge*: high roll % + positive spread + long build-up = carry the direction; poor rolls = the trade is being abandoned.
- Track *changes* intraday and day-over-day, not absolute OI — the delta is the signal.
- Cross-check stock-specific OI against **95% of market-wide** F&O ban-period rules: a stock crossing 95% of market-wide position limit hits an **F&O ban** (only position-reduction allowed) — a huge tell of over-crowding. **Verify ban list daily on NSE.**

**Common retail mistakes**
- Treating max-pain as a price *target* days before expiry (it's a weak expiry-day tendency).
- Reading option OI at a strike as immovable S/R — writers roll and adjust constantly.
- Confusing high volume with high OI (a strike can be heavily *traded* yet net-flat in OI).
- Chasing a short-covering rally as if it were fresh demand.
- Using PCR as a standalone buy/sell trigger.
- Ignoring costs while scalping OI shifts — friction eats the small edge.

## Checklist / drill

Before acting on OI, tick all five:

1. **Direction of underlying price** this session and vs yesterday's close?
2. **Direction of futures OI** — build-up or unwinding? (Map to the 4-box table.)
3. **Options context** — highest call/put OI strikes, PCR, max-pain: does it agree?
4. **Rollover week?** If yes, note roll % vs average and the spread — conviction rising or fading?
5. **Crowding/ban check** — is the stock near F&O ban? Is the move covering (finite) or fresh (durable)?

**Drill (2 weeks):** Each evening, log Nifty & Bank Nifty futures closing price, OI, and PCR in a sheet. Tag each day with one of the four labels. On the following day, note whether the label "worked." You'll quickly learn that build-up days trend and covering days chop — and that OI is context, never a stand-alone signal.

*Rules, STT, lot sizes and margins current as of 2026 — always re-verify on NSE/your broker/SEBI before trading.*
