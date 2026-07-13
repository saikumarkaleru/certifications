# International tax & transfer pricing basics

## What it is & where it's used

Cross-border money movement triggers a second layer of tax rules on top of domestic law. Three things dominate day-to-day practice:

1. **Withholding tax (WHT) on foreign payments** — when an Indian company pays a non-resident (software licence, consultancy, interest, royalty, dividend), it must deduct tax at source under **Section 195** before remitting, and file **Form 15CA/15CB**.
2. **DTAA (Double Taxation Avoidance Agreement)** — treaties India signs with ~95 countries that cap those WHT rates and decide *which* country gets to tax.
3. **Transfer pricing (TP)** — when two related entities (an Indian arm and its US/UAE/Singapore parent) trade with each other, the price must be **arm's length** (what unrelated parties would charge), documented, and reported.

**Who does this:** International tax analysts and TP associates in Big 4 and MNC in-house teams; finance/AP staff at any GCC (Global Capability Centre) or exporter who process foreign vendor invoices; treasury; and CA-firm associates. If you are targeting a GCC in Bengaluru/Hyderabad/Pune or an MNC shared-services role, this is a core, screened skill.

## The gap: why companies want this (and college didn't teach it)

An MBA teaches "double taxation is bad, treaties exist." Employers pay for the *mechanics*: **which rate applies, which form to file, and by when.** Every foreign vendor payment a GCC makes stops at the finance desk asking: *do we withhold, how much, and is a 15CB certificate needed?* Get it wrong and the company either over-deducts (vendor screams) or under-deducts (30% disallowance under **Section 40(a)(i)** plus interest and penalty).

The specific gaps:
- Nobody teaches the **195 → DTAA → 15CA/15CB decision tree**.
- College never mentions **Tax Residency Certificate (TRC)** and **Form 10F** — the two documents without which you *cannot* apply the lower treaty rate.
- TP is taught as economics; industry wants **benchmarking, the five methods, Form 3CEB, and a Local File** — deadlines and documentation, not theory.
- **PE (Permanent Establishment)**, **BEPS**, **GAAR**, and now **Pillar Two 15% global minimum tax** are interview-live but classroom-absent.

## What "proficient" looks like

A job-ready person can, unaided:

- Take a foreign vendor invoice and determine **taxability, section, DTAA article, and rate** — and explain *why*.
- Fill **Form 15CA (Part A/B/C/D)** and know when a CA's **Form 15CB** is mandatory.
- Apply a **treaty rate** correctly, insisting on **TRC + Form 10F + no-PE declaration** on file.
- Gross-up when the contract is **"net of tax."**
- Explain the **five TP methods** and pick the right one; read a **benchmarking study** and its arm's-length range (inter-quartile).
- Know the **Form 3CEB / Master File (3CEAA) / CbCR (3CEAD)** thresholds and due dates.

## Hands-on: how to actually do it

### Step 1 — The Section 195 decision tree

```
Is the payee a non-resident?  ── No ──> use normal TDS (194J etc.)
        │ Yes
Is the income taxable in India (Sec 5/9 – source rule)?  ── No ──> no WHT (but 15CA Part D)
        │ Yes
Rate = LOWER of  (a) Income-tax Act rate  and  (b) DTAA rate
        │  (DTAA only if payee gives TRC + Form 10F + no-PE declaration)
Deduct, deposit by 7th of next month, file 15CA (+15CB if remittance is taxable & > ₹5 lakh/yr)
```

### Step 2 — Common Act vs treaty rates (add surcharge + 4% cess to Act rates)

| Payment | Act rate (Sec) | Typical DTAA rate |
|---|---|---|
| Royalty / FTS (fees for technical services) | 20% (115A) | 10–15% |
| Interest | 20% (194LC etc.) | 10–15% |
| Dividend | 20% (115A) | 5–15% |

### Step 3 — WHT calculation in Excel

```excel
# B2 = invoice (foreign, gross), B3 = Act rate, B4 = DTAA rate
# WHT rate actually applied:
=MIN(B3,B4)
# WHT amount (treaty, no surcharge/cess on treaty rate):
=B2*MIN(B3,B4)
# If contract is "NET OF TAX" — gross up:
=B2/(1-MIN(B3,B4))          # grossed-up amount
=B2/(1-MIN(B3,B4))-B2       # tax borne by payer
```

**Worked gross-up:** vendor must *receive* $10,000 net, treaty rate 10% → gross = 10000/(1−0.10) = **$11,111.11**, WHT = **$1,111.11**.

### Step 4 — Journal entries (₹, royalty of ₹10,00,000, 10% treaty WHT, payer bears nothing)

| Date | Particulars | Dr (₹) | Cr (₹) |
|---|---|---|---|
| Invoice booked | Royalty expense A/c ...... Dr | 10,00,000 | |
| | To Foreign vendor A/c | | 9,00,000 |
| | To TDS payable (195) A/c | | 1,00,000 |
| Remittance | Foreign vendor A/c ...... Dr | 9,00,000 | |
| | To Bank A/c | | 9,00,000 |
| Deposit TDS (by 7th) | TDS payable (195) A/c ... Dr | 1,00,000 | |
| | To Bank A/c | | 1,00,000 |

### Step 5 — File Form 15CA / 15CB (income-tax portal)

```
incometax.gov.in → login → e-File → Income Tax Forms → File Now
→ Form 15CA
   Part A : taxable remittance ≤ ₹5 lakh in FY
   Part B : taxable, > ₹5 lakh, order/certificate u/s 195(2) obtained
   Part C : taxable, > ₹5 lakh — REQUIRES CA's Form 15CB first
   Part D : NOT taxable in India (no WHT)
→ For Part C: CA fills & e-verifies Form 15CB (DIN, amount, rate, DTAA article)
→ Acknowledgement number goes to the bank (AD) with Form A2 to release funds.
```

### Step 6 — The five transfer-pricing methods

| Method | One-line logic | Best when |
|---|---|---|
| **CUP** (Comparable Uncontrolled Price) | Compare the exact price to a third-party price | Commodities, loans, royalties with public comparables |
| **RPM** (Resale Price) | Work back from resale margin | Distributor buys & resells with no value-add |
| **CPM** (Cost Plus) | Cost + arm's-length markup | Contract manufacturer / service provider on cost |
| **TNMM** (Transactional Net Margin) | Compare *net* operating margin (OP/cost, OP/sales) | Default for GCC/IT/ITeS captives — most used in India |
| **PSM** (Profit Split) | Split combined profit by contribution | Highly integrated, unique intangibles |

**TNMM in Excel** — the arm's-length range from a comparable set:

```excel
# C2:C11 = OP/OC margins of 10 comparables; B2 = tested party's OP/OC
=QUARTILE.INC(C2:C11,1)     # lower quartile (arm's-length floor)
=MEDIAN(C2:C11)             # median
=QUARTILE.INC(C2:C11,3)     # upper quartile (ceiling)
=IF(AND(B2>=QUARTILE.INC(C2:C11,1),B2<=QUARTILE.INC(C2:C11,3)),"Arm's length","ADJUST to median")
```

### Step 7 — TP filing thresholds

| Form | What | Trigger / due date |
|---|---|---|
| **Form 3CEB** | Accountant's report on all int'l & specified domestic transactions | Any int'l related-party txn — due **31 Oct** |
| **Master File (3CEAA)** | Group-level info | Consolidated group revenue > ₹500 cr **and** int'l txn > ₹50 cr — **30 Nov** |
| **CbCR (3CEAD)** | Country-by-country report | Group revenue > **€750 mn** (~₹6,750 cr) |

## Worked example / mini-project

**Setup:** *Nimbus Analytics India Pvt Ltd* is a captive (GCC) doing software development for its US parent, billed **cost + 15%**. Total operating cost FY25-26 = **₹40,00,000**. During the year it also pays **£20,000** to a UK consultant for technical services (contract is net of tax).

**Part 1 — Transfer price (CPM/TNMM):**
- Revenue billed to parent = 40,00,000 × 1.15 = **₹46,00,000**; Operating profit = ₹6,00,000; **OP/OC = 15.0%**.
- Benchmarking set (10 comparable IT captives), OP/OC margins: 11, 12, 12.5, 13, 14, **14.5, 15, 16, 18, 20**.
- Lower quartile ≈ **12.63%**, median **14.25%**, upper quartile **16.5%**.
- Tested margin 15% lies inside 12.63%–16.5% → **arm's length. No adjustment. Report in Form 3CEB.**

**Part 2 — WHT on the UK payment (FTS):**
- India–UK DTAA, FTS/royalty rate = **10%** (10F + TRC + no-PE on file).
- Net of tax → gross up: 20,000 / (1 − 0.10) = **£22,222.22**; WHT = **£2,222.22**.
- At ₹105/£: remit £20,000 (₹21,00,000), deposit WHT ₹2,33,333 by the 7th, file **Form 15CB (CA)** then **15CA Part C** (taxable, > ₹5 lakh), give ack + Form A2 to the bank.

**Reproduce it:** drop the 10 margins in a column, run the `QUARTILE.INC` formulas, and the gross-up formula for £20,000 — you have re-derived both the TP conclusion and the WHT.

## How it's tested

**Interview questions:**
- "Indian co pays a US company for cloud software — is it royalty/FTS? Do you withhold, at what rate, which form?"
- "What is a PE and why does the parent care about creating one in India?"
- "TRC missing — can you still apply the DTAA rate?" (No — TRC + Form 10F are mandatory.)
- "Which TP method for a captive IT services centre, and why?" (TNMM.)
- "What is the inter-quartile range and what happens if the tested margin falls below it?"
- "One-line on BEPS / Pillar Two 15% minimum tax."

**Practical assessments:**
- **Timed Excel/case:** given an invoice + a mini benchmarking table, compute the WHT, decide the 15CA part, and state whether the TP margin is arm's length.
- **Form-fill drill:** map five vendor invoices to 15CA Part A/B/C/D.
- **Grossing-up test** on a net-of-tax contract (the classic trip-up).
- **Read-a-TP-study:** hand you a benchmarking report, ask you to defend the comparables and the range.

## Common mistakes & how pros avoid them

| Mistake | Fix |
|---|---|
| Applying DTAA rate with no **TRC + Form 10F** on file | No documents → use the higher Act rate; collect docs before remitting |
| Adding **surcharge + cess** on top of the treaty rate | Treaty rate is the ceiling — apply it flat |
| Ignoring **gross-up** on "net of tax" contracts | Always check who bears the tax; divide by (1 − rate) |
| Filing 15CA **Part D** for a taxable remittance | Part D is only for non-taxable; taxable > ₹5L needs Part C + 15CB |
| Choosing comparables with different functions for TNMM | Match FAR (functions, assets, risks); reject product/geography mismatches |
| Missing **3CEB (31 Oct)** — ₹1 lakh penalty | Calendar every related-party client separately |
| Forgetting **equalisation levy / TDS 194-O** on digital/e-com | Screen digital-service payments separately |

## Learn-it roadmap & resources

**Time to job-ready: 8–12 weeks** part-time.

- **Weeks 1–3:** Sections 5, 9, 195; WHT rates; do 20 15CA/15CB mappings. *ICAI International Taxation module* (free PDF) + the income-tax portal sandbox.
- **Weeks 4–6:** DTAA reading — pull the **India–US, India–UK, India–UAE, India–Singapore** treaties from incometaxindia.gov.in; practise finding the royalty/FTS/interest article and rate.
- **Weeks 7–9:** TP — the five methods, TNMM benchmarking, Rule 10B/10D; build one benchmarking sheet end-to-end.
- **Weeks 10–12:** BEPS Action Plans, PE, GAAR, **Pillar Two**; read the **OECD Transfer Pricing Guidelines** (free, skim) and a real Form 3CEB.

**Resources:** ICAI study material (free); OECD TP Guidelines & Model Tax Convention (free); Taxmann/Vinod Singhania *International Taxation* (paid); Big-4 alert emails (free). **Certifications:** ICAI's Diploma in International Taxation; the **ADIT (Advanced Diploma in International Taxation)** by CIOT UK — the gold standard for MNC/GCC international-tax roles.

## Quick-reference

| Item | Value |
|---|---|
| WHT on foreign payment section | **195** |
| Disallowance if not deducted | **40(a)(i)** — 100% |
| TDS deposit due | **7th of next month** |
| Treaty rate needs | **TRC + Form 10F + no-PE declaration** |
| 15CA Part A | taxable ≤ ₹5L/FY |
| 15CA Part C | taxable > ₹5L → needs **15CB** |
| 15CA Part D | not taxable |
| Gross-up (net of tax) | `= amount / (1 − rate)` |
| Arm's-length range | `QUARTILE.INC(range,1)` → `QUARTILE.INC(range,3)` |
| Default captive method | **TNMM** |
| Form 3CEB due | **31 Oct** |
| Master File / CbCR forms | **3CEAA / 3CEAD** |
| Global minimum tax | **Pillar Two — 15%** |

**Golden rule:** *Rate = lower of Act and DTAA — but only if TRC + 10F are on file; when in doubt, withhold higher and let the vendor claim credit.*
