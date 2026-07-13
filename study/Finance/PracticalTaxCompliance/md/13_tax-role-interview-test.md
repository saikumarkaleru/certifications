# The Tax Role Interview & Practical Test

## What it is & where it's used

The tax role interview is a two-part gate: a **conceptual conversation** ("explain input tax credit blocking") and a **practical test** where you actually *do the work* — compute a GST liability, calculate TDS on a vendor bill, or reconcile GSTR-2B against the purchase register in Excel. This is where 60% of MBA-Finance candidates lose the offer: they can define ITC but freeze when handed a messy purchase dump and told "reconcile this, you have 30 minutes."

Roles that run this gate: **Tax Executive / Analyst** (Big 4 compliance teams, mid-tier CA firms), **Accounts Payable with TDS ownership**, **GST Compliance Associate**, **Finance Executive** at any company above ~₹5 crore turnover, and offshore **India-tax delivery centres** (EY GDS, Deloitte USI, PwC AC). Globally, the equivalent is a VAT/sales-tax analyst or an indirect-tax associate — same muscle, different rate tables.

## The gap: why companies want this (and college didn't teach it)

College teaches you the *Income Tax Act sections* and the *CGST Act charging provisions*. It never makes you file a single GSTR-3B or match a single invoice. The gap is **execution under real-world mess**:

| College taught | The job actually needs |
|---|---|
| "TDS u/s 194J is 10%" | Vendor bill has GST — do you deduct TDS on the base or the gross? |
| "ITC is available on inputs" | 2B shows the invoice but your vendor filed late — claim now or defer? |
| Definition of RCM | Booking the RCM self-invoice and the offsetting ITC in Tally |
| "File GSTR-3B monthly" | Reconciling 2B vs books, finding the 12 mismatches, and drafting the follow-up email |

Employers pay for someone who closes a period **without supervision** and **without penalty-triggering errors**. That skill is invisible on a marksheet, so they test it live.

## What "proficient" looks like

The concrete bar a job-ready candidate clears unaided:

- Given a vendor invoice, compute **GST (correct place-of-supply → CGST+SGST vs IGST)** and **TDS on the base value excluding GST**, and state both due dates.
- Take a raw purchase register + a downloaded **GSTR-2B JSON/Excel** and produce a reconciliation flagging: matched, in-books-not-in-2B, in-2B-not-in-books, and value/GSTIN mismatches.
- Pass the **220-day / rule-37 / Section 16(4)** ITC eligibility tests from memory.
- Write the **journal entries** for a purchase with ITC, an RCM transaction, and a TDS deduction.
- Know the **return calendar** cold: GSTR-1 (11th), GSTR-3B (20th), TDS payment (7th), TDS return (quarterly, 31st of next month).

## Hands-on: how to actually do it

### 1. Compute GST + TDS on a vendor bill

A professional-services vendor in the same state bills you **₹1,00,000 + 18% GST**.

```
Base value        = 1,00,000
GST @ 18% (9+9)   =   18,000   → CGST 9,000 + SGST 9,000 (intra-state)
Invoice total     = 1,18,000

TDS u/s 194J @10% = 10,000   ← on BASE (₹1,00,000), NOT on ₹1,18,000
Net payable       = 1,18,000 - 10,000 = 1,08,000
```

The single most-tested trap: **TDS is deducted on the value excluding GST** when GST is shown separately (CBDT Circular 23/2017). Interstate? The ₹18,000 becomes IGST instead of CGST+SGST.

### 2. Excel formulas the test uses

Place-of-supply logic (auto-split CGST/SGST vs IGST):

```excel
=IF([@SupplierState]=[@BuyerState], [@Taxable]*[@Rate]/2, 0)   → CGST
=IF([@SupplierState]=[@BuyerState], [@Taxable]*[@Rate]/2, 0)   → SGST
=IF([@SupplierState]<>[@BuyerState], [@Taxable]*[@Rate], 0)    → IGST
```

TDS with threshold and section rate lookup:

```excel
=IF([@BaseValue]>=VLOOKUP([@Section],ThresholdTbl,2,0),
    ROUND([@BaseValue]*VLOOKUP([@Section],RateTbl,2,0),0), 0)
```

### 3. Reconcile GSTR-2B vs purchase register (the core test)

Match on a composite key of **GSTIN + Invoice No.**, then compare tax values:

```excel
Key:        =[@SupplierGSTIN]&"|"&[@InvoiceNo]
2B Taxable: =XLOOKUP([@Key], TwoB[Key], TwoB[Taxable], "NOT IN 2B")
Status:     =IFS(
   [@[2B Taxable]]="NOT IN 2B","In books, not in 2B",
   ISNA(XLOOKUP([@Key],Books[Key],Books[Key])),"In 2B, not in books",
   ROUND([@BookTaxable],0)<>ROUND([@[2B Taxable]],0),"Value mismatch",
   TRUE,"Matched")
```

### 4. Journal entries

| Transaction | Dr | Cr |
|---|---|---|
| Purchase with ITC | Purchases ₹1,00,000; CGST ITC ₹9,000; SGST ITC ₹9,000 | Vendor ₹1,18,000 |
| TDS on the above (194J) | Vendor ₹10,000 | TDS Payable ₹10,000 |
| RCM (freight ₹10,000) — self-invoice | RCM Expense ₹10,000; IGST ITC ₹1,800 | Vendor ₹10,000; IGST RCM Payable ₹1,800 |

### 5. GST-portal click-path (2B download)

`Services → Returns → Returns Dashboard → select period → GSTR-2B → View / Download → Download Excel`. This is what you'd narrate if asked "walk me through pulling 2B."

## Worked example / mini-project

**Reconcile a month for "Acme Traders" (Maharashtra).** Purchase register (books) vs GSTR-2B:

| Supplier | GSTIN | Inv No | Books Taxable | Books GST | 2B Taxable | 2B GST |
|---|---|---|---|---|---|---|
| Alpha Ltd | 27AAA...1Z5 | INV-101 | 50,000 | 9,000 | 50,000 | 9,000 |
| Beta Co | 27BBB...2Z4 | INV-205 | 30,000 | 5,400 | 30,000 | 5,400 |
| Gamma Inc | 24GGG...3Z3 | INV-88 | 20,000 | 3,600 | — | — |
| Delta LLP | 27DDD...4Z2 | INV-410 | 40,000 | 7,200 | 40,000 | 7,600 |
| Zeta Pvt | 27ZZZ...5Z1 | — | — | — | 15,000 | 2,700 |

Run the `Status` formula:

- **INV-101, INV-205** → *Matched* (claim ITC ₹9,000 + ₹5,400).
- **Gamma INV-88** → *In books, not in 2B* — vendor hasn't filed. **Defer** ITC of ₹3,600 (Sec 16(2)(aa): no 2B, no credit).
- **Delta INV-410** → *Value mismatch* — books GST ₹7,200 vs 2B ₹7,600. Either your invoice-value entry is wrong or vendor over-reported. Investigate; claim only the reconciled amount.
- **Zeta** → *In 2B, not in books* — vendor filed against your GSTIN but you have no bill. Could be a wrong GSTIN by the vendor or a missed booking. Do **not** claim until traced.

**Eligible ITC this month = ₹14,400** (only matched lines). The deliverable is this table plus a one-line follow-up email: *"Gamma & Delta — please confirm GSTR-1 filing / invoice value for INV-88 and INV-410."*

## How it's tested

**Interview questions (verbal):**

1. "Vendor bills ₹1,00,000 + 18% GST for professional fees — how much TDS, on what value?" (Answer: ₹10,000 on the base.)
2. "Invoice is in your books but not in 2B — can you take ITC?" (No — Sec 16(2)(aa).)
3. "Difference between GSTR-2A and 2B?" (2A is dynamic/live; 2B is static, generated 14th, and is the ITC basis.)
4. "What's blocked ITC under Sec 17(5)?" (Motor vehicles, personal consumption, works contract for immovable property, etc.)
5. "RCM on which common expenses?" (GTA/freight, legal fees from advocates, director sitting fees, import of services.)
6. "Due dates for GSTR-1, 3B, TDS payment, TDS return?"

**Practical/assessment test (hands-on):**

- A **timed 30-45 min Excel** with a purchase dump and a 2B extract: "reconcile and tell me eligible ITC." (Exactly the mini-project above.)
- "Here's a vendor invoice — compute GST and TDS, give me the net payable and journal entry."
- A **TallyPrime** live task: pass a purchase voucher with ITC and a TDS deduction.
- A **case**: "Vendor filed GSTR-1 late in the next month — how does your reconciliation and ITC treatment change?"

## Common mistakes & how pros avoid them

| Mistake | Fix |
|---|---|
| Deducting TDS on GST-inclusive amount | Deduct on base value when GST is shown separately (Circular 23/2017) |
| Claiming ITC because it's in *books* | ITC follows **2B**, not books — Sec 16(2)(aa) |
| Matching on invoice number alone | Use **GSTIN + Invoice No.** — invoice numbers repeat across vendors |
| Ignoring rounding | `ROUND(...,0)` both sides before comparing; paise differences flag false mismatches |
| Forgetting **Sec 16(4)** time limit | ITC lapses after 30 Nov of next FY / annual return date |
| Treating 2A and 2B as interchangeable | 2B is the static, auditable ITC basis; quote it in the interview |
| Missing RCM self-invoice | RCM creates a liability *and* an offsetting ITC — book both |

Pros also **keep the reconciliation reproducible**: a single key column, `XLOOKUP` not `VLOOKUP` (returns "NOT IN 2B" cleanly), and a status column that speaks in review language ("In books, not in 2B") rather than TRUE/FALSE.

## Learn-it roadmap & resources

**Time to interview-ready: 3-5 weeks** if you already know the concepts.

- **Week 1** — Rebuild the GST computation + place-of-supply logic in Excel; memorise the return calendar and Sec 17(5)/16 rules.
- **Week 2** — Build the 2B reconciliation template from scratch; run it on 3 sample datasets.
- **Week 3** — TDS: section rates, thresholds, Form 26Q, and journal entries; practise 10 vendor-bill computations.
- **Week 4** — TallyPrime vouchers (purchase-with-ITC, TDS, RCM); mock the timed Excel test twice.

**Resources:**
- GST portal (`gst.gov.in`) — file NIL returns on a test/own registration to see the real UI.
- CBIC's *GST Flyers* and Circular 23/2017 (TDS-on-GST) — free, authoritative.
- ICAI Study Material (Taxation) — you already have this via CA Inter.
- ClearTax / TaxGuru blogs for reconciliation walk-throughs.
- **Certification:** ICAI's *Certificate Course on GST*, or a Tally-with-GST certificate — useful signalling for non-CA roles.

## Quick-reference

| Item | Value |
|---|---|
| TDS base | Value **excluding** GST (if GST shown separately) |
| GST intra-state | CGST + SGST (split rate) |
| GST inter-state | IGST (full rate) |
| ITC basis | **GSTR-2B** (static, gen. 14th) |
| ITC condition | Sec 16(2)(aa) — must appear in 2B |
| ITC time limit | Sec 16(4) — 30 Nov of next FY |
| Blocked ITC | Sec 17(5) |
| GSTR-1 due | 11th of next month |
| GSTR-3B due | 20th of next month |
| TDS payment | 7th of next month |
| TDS return (26Q) | Quarterly, 31st of month after quarter |
| Recon key | `GSTIN & "|" & InvoiceNo` |
| Recon function | `XLOOKUP(key, 2B[key], 2B[val], "NOT IN 2B")` |
| Common TDS sections | 194C (1/2%), 194J (10%), 194I (10% rent), 194H (5%) |
| Common RCM | GTA freight, advocate fees, director fees, import of service |
