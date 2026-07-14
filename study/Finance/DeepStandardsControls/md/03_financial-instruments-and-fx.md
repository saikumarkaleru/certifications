# Financial Instruments & Foreign Currency: IFRS 9 / Ind AS 109, IAS 21

## What you'll be able to do

Classify a financial asset into the right measurement bucket (amortised cost / FVOCI / FVTPL) by running the two tests employers expect you to know — the **business model** test and the **SPPI** (solely payments of principal and interest) test — and book the right entries. Compute an **expected credit loss (ECL)** allowance and move a loan through the three stages. Set up a basic **hedge accounting** relationship (cash-flow and fair-value) with entries. And translate foreign-currency items under **IAS 21 / Ind AS 21**, correctly splitting **monetary vs non-monetary** and identifying **functional currency**.

## The essentials

**Classification & measurement (IFRS 9 / Ind AS 109) — debt instruments:**

| Business model | Cash-flow test (SPPI) | Measurement |
|---|---|---|
| Hold to collect | Passes SPPI | **Amortised cost** |
| Hold to collect **and** sell | Passes SPPI | **FVOCI** (interest & impairment in P&L; FV changes in OCI, recycled on sale) |
| Other (trading) / fails SPPI | — | **FVTPL** |

- **Equity instruments:** default **FVTPL**; irrevocable option at inception to present FV changes in **OCI (no recycling)** for non-held-for-trading equities.
- **Financial liabilities:** mostly amortised cost; FVTPL by election, with own-credit-risk changes to OCI.

**Impairment — the 3-stage ECL model** (forward-looking, applies to amortised-cost & FVOCI debt, lease receivables, contract assets):

| Stage | Credit risk since origination | Loss allowance | Interest revenue on |
|---|---|---|---|
| **1** | Not significantly increased | **12-month ECL** | Gross carrying amount |
| **2** | **Significantly increased** (SICR) | **Lifetime ECL** | Gross carrying amount |
| **3** | **Credit-impaired** (default) | **Lifetime ECL** | **Net** carrying amount |

Trade receivables use the **simplified approach** — lifetime ECL always (provision matrix). Note: US GAAP's **CECL (ASC 326)** books lifetime losses from day one with **no staging** — a key contrast.

**Hedge accounting (optional, needs documentation + effectiveness):**
- **Fair-value hedge:** re-measure hedged item for the hedged risk through P&L; hedging instrument at FV through P&L — the two offset.
- **Cash-flow hedge:** effective portion of the derivative's gain/loss to **OCI (cash-flow hedge reserve)**, recycled to P&L when the hedged forecast transaction hits earnings.

**Foreign currency (IAS 21 / Ind AS 21):**
- **Functional currency** = currency of the primary economic environment (where sales prices, costs, financing are denominated). Determined first; **presentation currency** can differ.
- At each reporting date: **monetary items** (cash, receivables, payables, loans) → **closing rate**, differences to **P&L**. **Non-monetary items at historical cost** (PP&E, inventory) → **historical rate**, no re-translation. Non-monetary at fair value → rate at valuation date.

## Hands-on — step by step

### Part A — Classification (worked)

BankCo buys a ₹1,00,00,000 corporate bond, 8% coupon, intends to hold to maturity to collect contractual cash flows; cash flows are principal + interest.
- Business model = hold to collect; SPPI passes → **amortised cost**.
- Entry: `Dr Investment 1,00,00,000 / Cr Bank 1,00,00,000`; interest accrued via effective interest.

### Part B — ECL (worked)

Loan book: gross carrying **₹1,00,00,000**, all Stage 1 at origination.
- **12-month PD** = 2%, **LGD** = 40%, **EAD** = ₹1,00,00,000.
- **12-month ECL** = PD × LGD × EAD = 0.02 × 0.40 × 1,00,00,000 = **₹80,000**.

Entry (Year 0):
```
Dr Impairment loss (P&L)     80,000
   Cr Loss allowance (ECL)           80,000
```

**Year 1 — borrower's credit deteriorates (SICR) → Stage 2.** Now use **lifetime** PD = 15%.
- Lifetime ECL = 0.15 × 0.40 × 1,00,00,000 = **₹6,00,000**. Allowance must rise from ₹80,000 to ₹6,00,000.

Entry:
```
Dr Impairment loss (P&L)   5,20,000
   Cr Loss allowance                5,20,000
```

**Year 2 — borrower defaults → Stage 3.** Interest now accrues on the **net** carrying amount (gross − allowance), and the loan is credit-impaired. Further allowance top-up flows through P&L; on write-off, `Dr Loss allowance / Cr Loan`.

### Part C — Cash-flow hedge (worked, brief)

ExportCo expects to receive **USD 1,00,000** in 3 months and hedges with a forward. Over the quarter the forward gains **₹50,000** (effective).
```
Dr Forward (derivative asset)   50,000
   Cr Cash-flow hedge reserve (OCI)  50,000
```
When the USD sale is recognised, recycle the ₹50,000 from OCI to P&L (adjusting revenue/FX), so the hedged cash flow lands at the locked rate.

### Part D — IAS 21 FX (worked)

IndiaCo (functional currency INR) has, at year-end:
- **USD receivable 10,000**, booked at ₹82/USD = ₹8,20,000; **closing rate ₹84**.
- **Machine** bought for USD 5,000 at ₹80/USD = ₹4,00,000 (non-monetary, historical cost).

Year-end:
- Receivable (monetary) → 10,000 × 84 = **₹8,40,000**. FX **gain ₹20,000** to P&L:
```
Dr Trade receivable   20,000
   Cr FX gain (P&L)          20,000
```
- Machine (non-monetary at historical cost) → **stays ₹4,00,000**, no re-translation.

## The output

**ECL allowance roll-forward:**
```
Opening (Yr0)             80,000   (Stage 1, 12-mo ECL)
Move to Stage 2 (Yr1)  +5,20,000   (lifetime ECL, SICR)
Closing (Yr1)           6,00,000
```

**FX re-measurement summary (year-end):**
```
Monetary  USD receivable : 8,20,000 → 8,40,000  → +20,000 P&L
Non-monetary machine     : 4,00,000 → 4,00,000  → nil
Net FX gain to P&L       : 20,000
```

**Classification memo (one line each):** "Corporate bond — hold-to-collect + SPPI pass → **amortised cost**; forward on USD receivable — designated **cash-flow hedge**, effective portion in OCI; equity stake in supplier — **FVTPL** (no OCI election taken)."

## Checks, gotchas & red flags

- **SPPI first, business model together — both must be satisfied** for amortised cost/FVOCI. A convertible bond or one with leverage features **fails SPPI** → FVTPL.
- **ECL is forward-looking**, not incurred-loss. Booking a provision only after default (old IAS 39) is wrong under IFRS 9.
- **Stage 3 flips interest to net carrying amount** — a classic exam catch; Stages 1–2 accrue on gross.
- **CECL vs ECL:** don't apply staging to US GAAP — CECL is lifetime from day 1, no stages.
- **Monetary vs non-monetary is the whole game in IAS 21.** Re-translating PP&E at closing rate is a top error; only monetary items and FV-carried non-monetary items move.
- **Functional ≠ presentation currency.** A company can *function* in USD but *present* in INR (translation of results uses average/closing rates, with the translation difference in OCI — the **foreign currency translation reserve**).
- **Ind AS 21 carve-out:** India permits capitalising long-term FX monetary-item differences into asset cost — not allowed under pure IFRS. Flag it in group reporting.
- **Hedge docs:** no contemporaneous documentation + effectiveness assessment = **no hedge accounting**, and the derivative goes straight to P&L (volatility).

## Interview drill

**Q1: "How do you classify a financial asset under IFRS 9?"**
A: Two tests. The **business model** test — hold to collect (amortised cost), hold to collect and sell (FVOCI), or other/trading (FVTPL). And the **SPPI** test — do contractual cash flows represent solely principal and interest? Only if SPPI passes can you use amortised cost or FVOCI; anything that fails SPPI (e.g., equity, convertibles, leveraged returns) goes to FVTPL. Equities are FVTPL by default with an irrevocable FVOCI-no-recycling election.

**Q2: "Loan of ₹1 cr, PD 2%, LGD 40%. What's the Stage 1 allowance, and what changes it to Stage 2?"**
A: 12-month ECL = 2% × 40% × ₹1 cr = **₹80,000**. It moves to Stage 2 on a **significant increase in credit risk (SICR)** since origination — then you switch to **lifetime** ECL (using lifetime PD), so the allowance jumps. Interest still accrues on gross until Stage 3 (default), where it moves to net.

**Q3: "IAS 21 — which items get re-translated at year-end?"**
A: **Monetary items** (cash, receivables, payables, loans) at the **closing rate**, with differences in P&L. **Non-monetary items at historical cost** (PP&E, inventory) stay at the historical rate — no re-translation. Non-monetary items carried at fair value use the rate on the valuation date. Functional currency is determined first and drives all of this.

## Learn/practise (free)

- **IFRS 9 / IAS 21 illustrative examples** — free on the IFRS Foundation site; the ECL and hedge examples are gold.
- **ICAI Ind AS 109 / 21 educational material** — free PDFs, India carve-outs explained.
- **RBI / bank Basel disclosures** — real ECL provision-matrix and staging disclosures to reverse-engineer.
- **Rehearse in Excel:** build a PD × LGD × EAD grid and a stage-transition roll-forward; then a two-column monetary/non-monetary FX re-measurement showing which lines move at closing vs historical rates. Both are exactly the schedules a reviewer asks for.
