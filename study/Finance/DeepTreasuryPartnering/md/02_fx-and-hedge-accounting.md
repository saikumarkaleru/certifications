# FX Risk & Hedge Accounting

## What you'll be able to do
Identify the three kinds of FX exposure a company runs, pick the right instrument to hedge each, price and book a forward hedge end to end, and pass the hedge-accounting entries under Ind AS 109 / IFRS 9 for both a cash-flow hedge and a fair-value hedge. You'll compute a forward rate from interest-rate parity, mark the forward to market, test effectiveness, and show where every number lands — OCI, P&L, and the hedging reserve. This is the exact skill a treasury/finance analyst in an Indian exporter or GCC is asked to demonstrate.

## The essentials

**Three exposure types.**

| Exposure | What it is | Hits | Hedge? |
|---|---|---|---|
| **Transaction** | A committed/forecast FX cash flow (an export receivable, an FX loan) | P&L when it settles/reprices | Yes — forwards, options, swaps |
| **Translation** | Restating a foreign subsidiary's net assets into the parent's currency | OCI (FCTR), not cash | Usually left, or net-investment hedge |
| **Economic** | Long-run competitiveness if the currency moves (a rival's costs fall) | Future revenues/margins | Operational, hard to hedge financially |

**Instruments.**
- **Forward** — lock a rate today for a future date. Obligation on both sides. Cheapest, most common. No premium.
- **Currency swap** — exchange principal and/or interest in two currencies; used for FX debt.
- **Option** — right, not obligation, to buy/sell at a strike; costs a premium; keeps upside. Use when the cash flow is uncertain or you want protection with participation.

**Forward pricing — covered interest-rate parity.** The forward isn't a forecast; it's arithmetic:

F = S × (1 + i_quote × t) / (1 + i_base × t)

For USD/INR, INR is the quote (higher rate) so the forward trades at a **premium** to spot. Higher-yield currency trades at a forward discount.

**Hedge accounting (Ind AS 109 / IFRS 9).** Normally derivatives are fair-valued through P&L. That creates a timing **mismatch**: the hedged item (e.g. a forecast sale) isn't yet in P&L, but the derivative swings are. Hedge accounting realigns the timing. Three types:

| Type | Hedges | Effective portion goes to | Reclassified when |
|---|---|---|---|
| **Cash-flow hedge** | Variability in future cash flows (forecast sale, floating-rate debt) | **OCI** (cash-flow hedge reserve) | Hedged item hits P&L |
| **Fair-value hedge** | Change in FV of a recognised asset/liability or firm commitment | **P&L** (and the hedged item is remeasured to P&L too) | n/a — both in P&L now |
| **Net-investment hedge** | FX on a foreign operation's net assets | OCI (FCTR) | On disposal of the operation |

**Qualifying criteria:** formal designation and documentation at inception, an economic relationship between item and instrument, credit risk doesn't dominate, and a defined hedge ratio. IFRS 9 dropped the old 80–125% bright line but you still test effectiveness and record any **ineffectiveness in P&L**.

## Hands-on — step by step
**Scenario.** On 1-Apr-2026 an Indian exporter expects to receive **USD 1,000,000** on 30-Jun-2026 (a highly probable forecast sale). Risk: USD/INR could fall before then. Spot = 86.00. It sells USD forward.

**Step 1 — Price the 3-month forward.** i_INR = 6.5% p.a., i_USD = 4.5% p.a., t = 91/365 = 0.2493.

F = 86.00 × (1 + 0.065×0.2493) / (1 + 0.045×0.2493)
= 86.00 × (1.016205) / (1.011219)
= 86.00 × 1.004931 = **86.424**

Forward premium ≈ 0.424, so it locks **USD/INR 86.42** for 30-Jun. Contracted INR = 1,000,000 × 86.42 = **₹8,64,24,000**.

**Step 2 — Designate.** Document: hedged item = highly probable USD 1m forecast export on 30-Jun; instrument = USD 1m sell forward at 86.42; type = **cash-flow hedge**; ratio 1:1. This designation is what lets gains/losses sit in OCI.

**Step 3 — Mark to market at reporting date (30-Jun-2026 = maturity).** Assume spot on 30-Jun = **84.50** (rupee appreciated — the feared move). Forward now settles at spot.

- Gain on forward (we sold high, buy back low): (86.42 − 84.50) × 1,000,000 = **+₹19,20,000**.
- Loss on the underlying sale vs 1-Apr expectation: the USD 1m now converts at 84.50 = ₹8,45,00,000 vs ₹8,64,24,000 expected → **−₹19,24,000** economic shortfall. The forward gain offsets it.

**Step 4 — Test effectiveness.** Change in FV of hedge = +₹19,20,000; change in value of expected cash flow attributable to FX ≈ −₹19,20,000 (spot move 86.42→84.50 on the designated notional). Offset ≈ 100%, direction opposite → **highly effective**. Any tiny gap (forward-points vs spot method) is ineffectiveness to P&L.

**Step 5 — Book the entries** (cash-flow hedge).

At 30-Jun, before settlement, recognise the forward at fair value with the effective portion in OCI:

```
Dr  Forward asset (derivative)        19,20,000
    Cr  Cash-flow hedge reserve (OCI)          19,20,000
```
On settlement, receive USD 1m, convert at spot 84.50, and net-settle the forward:

```
Dr  Bank (INR from USD sale @84.50)  8,45,00,000
    Cr  Sales / Trade receivable             8,45,00,000

Dr  Bank (forward net settlement)      19,20,000
    Cr  Forward asset                          19,20,000
```
Reclassify the reserve to P&L as the sale is recognised (the "basis adjustment"):

```
Dr  Cash-flow hedge reserve (OCI)      19,20,000
    Cr  Revenue / P&L                          19,20,000
```
Net revenue recognised = 8,45,00,000 + 19,20,000 = **₹8,64,20,000 ≈ the locked ₹8,64,24,000**. The hedge did its job.

**Fair-value hedge variant.** If instead you hedged a **recognised USD receivable** (already on the books), you don't use OCI — you fair-value the forward **through P&L** *and* remeasure the receivable for FX through P&L; the two offset directly, no reserve.

## The output
**Hedge documentation & result summary**

```
Hedged item : USD 1,000,000 highly probable export, 30-Jun-2026
Instrument  : USD 1m sell forward @ 86.42 (priced off CIP)
Hedge type  : Cash-flow hedge (Ind AS 109 / IFRS 9)
Ratio       : 1 : 1        Effectiveness: ~100%, highly effective

At settlement (spot 84.50):
  Spot proceeds on USD 1m            8,45,00,000
  + Forward gain (via OCI→P&L)         19,20,000
  = Effective INR realised           8,64,20,000
  vs Locked forward value            8,64,24,000   (diff = rounding/points)

Accounting effect: forward gain deferred in OCI, reclassified
to revenue when the sale is booked — P&L shows the locked rate,
no volatility from the interim MTM.
```

## Checks, gotchas & red flags
- **Forward ≠ forecast.** The forward premium is interest-rate differential, not a bet on direction. Never explain it as "the market thinks INR will weaken."
- **Higher-rate currency = forward premium on the pair, discount on itself.** Get the parity direction right or your locked rate is upside-down.
- **Cash-flow → OCI; fair-value → P&L.** Mixing these is the classic exam and audit error.
- **"Highly probable" must be real.** If the forecast sale isn't highly probable, the hedge fails designation and everything drops to P&L.
- **Ineffectiveness always to P&L**, even under IFRS 9's relaxed model. Over-hedging (notional > exposure) creates ineffectiveness on the excess.
- **Credit/CVA and forward points** can make offset imperfect — document your method (spot vs forward) up front.
- **Reclassify, don't double count.** The OCI amount moves to P&L; it isn't income on top of the sale.

## Interview drill
**Q: Transaction vs translation exposure — which do you hedge and why?** A: Transaction exposure is committed/forecast FX cash flows that hit P&L and cash on settlement, so it's the priority to hedge with forwards or options. Translation exposure is the non-cash restatement of a foreign subsidiary's net assets into OCI (FCTR); it doesn't affect cash, so most firms leave it or use a net-investment hedge. I'd spend the hedging budget on transaction risk first.

**Q: Why do we need hedge accounting at all?** A: Because derivatives are fair-valued through P&L by default, but the hedged item (a forecast sale, or floating debt interest) isn't in P&L yet — so unhedged, you'd book derivative volatility now against nothing. Hedge accounting parks the effective portion in OCI (cash-flow hedge) and releases it to P&L when the hedged item lands, so the income statement shows the locked economics instead of interim noise.

**Q: A forecast sale hedge — walk the entries.** A: At MTM, Dr forward asset / Cr cash-flow hedge reserve (OCI) for the effective gain; on settlement, book the sale at spot, settle the forward through bank, then Dr OCI reserve / Cr revenue to reclassify — net revenue equals the locked forward value. Any ineffectiveness goes straight to P&L.

## Learn/practise (free)
- **Ind AS 109 / IFRS 9** standard text — ICAI and the IFRS Foundation publish the chapters free; read the hedge-accounting section and the illustrative examples.
- **KPMG / EY / Deloitte "IFRS 9 hedge accounting" guides** — free PDFs with worked cash-flow and fair-value examples.
- **RBI / FEDAI** — free reference for INR forward premia and how Indian banks quote forwards.
- **Rehearse the CIP calc** in Excel: pull today's USD/INR spot and 1M/3M forward from an FBIL/bank page, back out the implied rate differential, and check it against the parity formula.
- **CFA Level II derivatives** readings and Corporate Finance Institute's free FX risk articles cover exposure types and instrument choice.
- **Build the full journal set** for one hedge each quarter (one cash-flow, one fair-value) — that ledger walk is the single most-tested treasury-accounting skill.
