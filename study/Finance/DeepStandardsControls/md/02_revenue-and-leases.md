# Revenue & Leases: ASC 606 / IFRS 15 / Ind AS 115 and ASC 842 / IFRS 16 / Ind AS 116

## What you'll be able to do

Take a signed customer contract and *recognise the revenue correctly* — identify the performance obligations, allocate the price, decide point-in-time vs over-time, and book the journal entries with a contract-asset / deferred-revenue schedule that ties out. Take a lease and *put it on the balance sheet* — compute the lease liability as a present value, set up the right-of-use (ROU) asset, and roll a full amortisation schedule with the interest-and-principal split and the depreciation entry. You'll also know the two or three US-GAAP-vs-IFRS differences a reviewer will test you on.

## The essentials

**Revenue — the single 5-step model** (identical logic in ASC 606 / IFRS 15 / Ind AS 115):

1. **Identify the contract** — approved, rights identifiable, commercial substance, collection probable.
2. **Identify performance obligations (POs)** — distinct promised goods/services.
3. **Determine the transaction price** — including variable consideration (constrained to the amount "highly probable" of not reversing).
4. **Allocate** the price to POs by **standalone selling price (SSP)**.
5. **Recognise** revenue when (point in time) or as (over time) each PO is satisfied — i.e., when control transfers.

**Over-time** recognition if any one holds: customer consumes as you perform; you create/enhance an asset the customer controls; or the asset has no alternative use *and* you have an enforceable right to payment for work done. Otherwise **point in time**.

**Leases — lessee model** (ASC 842 / IFRS 16 / Ind AS 116). Both put nearly all leases on the balance sheet:
- **Lease liability** = PV of remaining lease payments, discounted at the rate implicit in the lease, else the **incremental borrowing rate (IBR)**.
- **ROU asset** = lease liability + initial direct costs + prepaid rent − lease incentives.

**The one big difference — lessee P&L pattern:**

| | IFRS 16 / Ind AS 116 | ASC 842 |
|---|---|---|
| Lease classification (lessee) | **Single model** — all finance-type | **Two types:** finance vs **operating** |
| P&L for an operating lease | n/a (all leases: depreciation + interest, **front-loaded** total cost) | **Single straight-line** lease expense |
| Balance sheet | ROU + liability | ROU + liability (both types) |

So under IFRS/Ind AS every lease looks like a finance lease (interest is front-loaded, expense declines over time). Under US GAAP, an *operating* lease keeps a flat straight-line expense even though the asset and liability are on the balance sheet. Lessor accounting stays broadly the classification-based model in all three.

## Hands-on — step by step

### Part A — Revenue (worked)

**Contract:** SoftServe Ltd sells a software licence **plus** 12 months of support for a bundled **₹12,00,000**, signed 1 Jan. SSPs: licence ₹10,00,000; support ₹5,00,000 (total SSP ₹15,00,000). Licence transfers at a point in time (day 1); support is over time (evenly).

**Step 1–2:** One contract; **two POs** — licence (distinct) and support (distinct).

**Step 3:** Transaction price ₹12,00,000 (no variable consideration).

**Step 4 — allocate by SSP ratio:**
- Licence: 12,00,000 × (10/15) = **₹8,00,000**
- Support: 12,00,000 × (5/15) = **₹4,00,000**

**Step 5 — recognise:** Licence ₹8,00,000 on 1 Jan; support ₹4,00,000 straight-line = **₹33,333/month**.

**Entries (₹):**

At signing / invoice (assume full ₹12,00,000 billed and received 1 Jan):
```
Dr Bank                     12,00,000
   Cr Revenue – licence                8,00,000
   Cr Contract liability (deferred)    4,00,000
```
Each month for support:
```
Dr Contract liability          33,333
   Cr Revenue – support                 33,333
```
After 12 months the ₹4,00,000 deferred is fully recognised.

*If instead billing lagged performance* (you'd earned revenue before the right to invoice), the debit sits in a **contract asset**, not a receivable.

### Part B — Lease (worked)

**Lease:** Office, **3 years**, payment **₹5,00,000 at each year-end**, IBR **10%**, no initial direct costs/incentives. Lessee under **Ind AS 116 / IFRS 16**.

**Step 1 — Lease liability = PV of 3 payments at 10%:**

| Year | Payment | PV factor @10% | PV |
|---|---|---|---|
| 1 | 5,00,000 | 0.9091 | 4,54,545 |
| 2 | 5,00,000 | 0.8264 | 4,13,223 |
| 3 | 5,00,000 | 0.7513 | 3,75,657 |
| | | **Total** | **12,43,426** |

**Step 2 — Initial entry (day 1):**
```
Dr ROU asset            12,43,426
   Cr Lease liability            12,43,426
```

**Step 3 — Amortisation schedule (liability):**

| Yr | Open liab | Interest @10% | Payment | Principal | Close liab |
|---|---|---|---|---|---|
| 1 | 12,43,426 | 1,24,343 | 5,00,000 | 3,75,657 | 8,67,769 |
| 2 | 8,67,769 | 86,777 | 5,00,000 | 4,13,223 | 4,54,545 |
| 3 | 4,54,545 | 45,455 | 5,00,000 | 4,54,545 | 0 |

**Step 4 — ROU depreciation** (straight-line over 3 yrs) = 12,43,426 / 3 = **₹4,14,475/yr**.

**Step 5 — Year-1 entries:**
```
Dr Interest expense       1,24,343
Dr Lease liability        3,75,657
   Cr Bank                          5,00,000
Dr Depreciation           4,14,475
   Cr Accumulated depreciation – ROU 4,14,475
```

**Year-1 total P&L charge** = interest 1,24,343 + depreciation 4,14,475 = **₹5,38,818** (front-loaded; falls each year).

**Under ASC 842, if this were an operating lease:** you'd still book the ₹12,43,426 ROU and liability, but the P&L charge would be a **flat ₹5,00,000/yr** straight-line — the ROU amortisation is the plug that keeps total expense level.

## The output

**Revenue — contract-liability roll-forward (Year 1):**
```
Opening deferred        4,00,000
Recognised (12 × 33,333) (4,00,000)
Closing deferred               0
Total revenue Yr1 = 8,00,000 (licence) + 4,00,000 (support) = 12,00,000
```

**Lease — note disclosure figures (Ind AS 116, Yr 1):**
```
ROU asset (net)     : 12,43,426 − 4,14,475 = 8,28,951
Lease liability     : 8,67,769  (current + non-current split)
Interest expense    : 1,24,343
Depreciation        : 4,14,475
Cash outflow (financing + operating per IFRS 16 split)
```

## Checks, gotchas & red flags

- **SSP must be used for allocation**, not the contract's stated line prices — a "free" item bundled in still gets allocated revenue.
- **Variable consideration constraint:** don't book variable amounts (bonuses, rebates) unless "highly probable" no significant reversal — classic overstatement red flag.
- **Contract asset ≠ receivable.** A receivable is an unconditional right to cash; a contract asset is conditional on further performance.
- **Lease liability uses payments, ROU adds costs** — mixing them (e.g., adding initial direct costs to the *liability*) is the most common error. IDC go into the **ROU asset only**.
- **Discount rate:** implicit rate first; IBR only if implicit rate isn't readily determinable. Using the wrong rate mis-states both sides.
- **Front-loading:** under IFRS 16 total lease cost is higher in early years — don't "expect" a flat charge; that's US-GAAP operating-lease behaviour.
- **Short-term (≤12 months) and low-value lease exemptions** exist under IFRS 16/Ind AS 116 — those stay off balance sheet, expensed straight-line.
- **Tie-out:** liability must amortise to exactly **zero** at lease end; if it doesn't, your PV or schedule is wrong.

## Interview drill

**Q1: "Walk me through allocating price when SSPs don't sum to the contract price."**
A: You allocate the *transaction price* in proportion to standalone selling prices, regardless of the stated total. In the SoftServe case SSPs summed to ₹15L but the deal was ₹12L, so each PO got 12/15 of its SSP — licence ₹8L, support ₹4L. The ₹3L discount is spread pro-rata, not dumped on one obligation (unless evidence shows the discount relates to specific POs).

**Q2: "A tenant signs a 5-year lease. Under IFRS 16, does the income statement charge stay flat?"**
A: No — IFRS 16 uses a single finance-lease model, so the charge is **depreciation (straight-line) plus interest on the liability (declining)**. Total expense is **front-loaded**: higher in year 1, lower by year 5. A flat charge only happens under **ASC 842 operating leases**, where the ROU amortisation flexes to level total expense.

**Q3: "When is revenue recognised over time?"**
A: When one of three criteria is met — the customer simultaneously receives and consumes benefits as you perform (e.g., a cleaning service); you create/enhance an asset the customer controls as it's built; or the asset has no alternative use to you and you have an enforceable right to payment for performance to date. Otherwise it's a point-in-time transfer of control.

## Learn/practise (free)

- **IFRS 15 / IFRS 16 illustrative examples** — free on the IFRS Foundation site; the worked examples mirror exam questions.
- **ICAI Ind AS 115 / 116 educational material** — free PDFs with Indian-context examples and entries.
- **FASB ASC 606 / 842 Basic View** — free registration for the US-GAAP text and the operating-vs-finance test.
- **Rehearse in Excel:** build the lease schedule with `=PV(rate,nper,-pmt)` for the liability, then a manual roll-forward table; prove it amortises to zero. For revenue, build an SSP allocation table and a deferred-revenue waterfall — both are exactly what you'd hand a reviewer.
