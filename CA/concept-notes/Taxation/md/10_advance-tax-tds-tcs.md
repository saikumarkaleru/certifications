# Chapter 10 — Advance Tax, TDS & TCS

> *Flag: All rates, thresholds and instalment percentages below reflect the law as commonly examined for AY 2025-26. Always re-verify the exact figures and the applicable Assessment Year against current ICAI study material before the exam, as thresholds (especially in the 194-series) are amended almost every Finance Act.*

---

## 1. The Problem

Imagine you are the Government of India. Your entire machinery — defence, roads, salaries of civil servants, subsidies — runs on a **daily** cash outflow. Money leaves the treasury every single day.

Now look at how income tax "naturally" arrives. A person earns income throughout the year (April to March). Under the pure structure of the Act, they compute total income *after* the year ends, and file a return by 31st July (or later). Tax would then trickle in as one lump sum, **many months after** the income was earned.

This creates three brutal problems:

1. **A cash-flow mismatch for the State.** The government spends continuously but would receive tax only once a year, in arrears. It would have to borrow to bridge every month — expensive and unstable.
2. **A collection risk.** Give a person 15 months between earning ₹50 lakh and paying tax on it, and a large fraction of that money is gone — spent, invested illiquidly, or deliberately hidden. A promise to pay later is worth far less than money taken today.
3. **An information / evasion problem.** If the *only* touchpoint between the taxpayer and the department is a self-declared return, the department is blind. It has no independent record of who earned what. The informal economy simply never shows up.

So the core problem is this: **How does the State get a steady, reliable, hard-to-evade stream of tax — instead of a delayed, dodgeable lump sum?**

The answer is a philosophy: **do not wait for the year to end and do not rely on the taxpayer alone.** Collect tax *as income arises* (during the year, in instalments), and collect it *where income arises* (at the point a payment is made, from a third party who has no incentive to hide it). This chapter is the machinery of that philosophy: **Advance Tax, TDS, and TCS.**

---

## 2. The Core Idea

There are exactly three mechanisms, and they differ on **who** pays and **when**:

| Mechanism | Who deposits the tax | When | Governing sections |
|---|---|---|---|
| **Advance Tax** | The **taxpayer himself**, on his *own estimated* income | *During* the year, in 4 instalments | Sec 207–211, 234B, 234C |
| **TDS (Tax Deducted at Source)** | The **payer** deducts before paying the recipient | *At the moment of payment/credit* | Sec 192–196, 234E, 271H |
| **TCS (Tax Collected at Source)** | The **seller** collects extra from the buyer | *At the moment of sale/receipt* | Sec 206C |

The unifying idea — the one sentence to hold in your head — is:

> **"Pay-as-you-earn" and "pay-where-you-earn."** Advance tax is the taxpayer prepaying on his own estimate; TDS/TCS is a *third party* skimming tax off a transaction and depositing it on the taxpayer's behalf.

Everything else — every rate, every threshold, every due date — is just detail hung on this skeleton. The final settlement happens when the return is filed: the taxpayer computes actual total tax, subtracts everything already paid (advance tax + TDS + TCS, all visible in **Form 26AS / the Annual Information Statement**), and pays the balance (self-assessment tax u/s 140A) or claims a refund.

*Figure 10.1 — The three streams all feed one reservoir: the taxpayer's final liability.*

```mermaid
flowchart TD
    A["Income arises during the year"] --> B["Taxpayer estimates own income"]
    A --> C["A payer makes a payment to taxpayer"]
    A --> D["A seller sells specified goods to taxpayer"]
    B --> E["Advance Tax in 4 instalments"]
    C --> F["Payer deducts TDS and deposits"]
    D --> G["Seller collects TCS and deposits"]
    E --> H["Total prepaid tax credited in Form 26AS"]
    F --> H
    G --> H
    H --> I["Return filed - actual tax minus prepaid = balance or refund"]
```

---

## 3. Why It's Built This Way

Before any section numbers, let us derive *why* each design choice exists. If you understand the WHY, the numbers become obvious rather than memorised.

**Why instalments for advance tax, and why front-loaded?**
The government needs steady cash across the year, so one payment won't do. But why is the schedule *back-loaded* toward larger cumulative percentages later (15% → 45% → 75% → 100%)? Because early in the year the taxpayer genuinely *cannot* know his income well — a businessman in June has little idea of his March profit. So the law asks for only 15% by June, then progressively more as the picture clarifies, reaching 100% by 15th March, two weeks before year-end. It balances the State's cash need against the fairness of not demanding tax on income that hasn't crystallised.

**Why does TDS exist at all when advance tax already covers "pay as you earn"?**
Because advance tax relies on the taxpayer's *honesty and diligence*. TDS removes both from the equation. When your employer pays your salary, *he* deducts the tax — you never touch it. The person with the incentive to comply (the payer, who faces penalties and disallowance) is different from the person with the incentive to evade (the recipient). This separation is the genius of source-based collection. It also generates a **paper trail**: every TDS entry tells the department "X paid Y this much," widening the tax net to people who would never have filed.

**Why thresholds (e.g., no TDS on rent below a limit)?**
If every ₹100 payment triggered TDS, the compliance cost (deduct, deposit, file quarterly returns, issue certificates) would crush small payers and clog the system for trivial revenue. Thresholds are a **cost-benefit cutoff**: deduct only where the amount is large enough that the revenue justifies the friction.

**Why different rates for different payments (1%, 2%, 5%, 10%, 30%)?**
TDS is only an *estimate* of final liability, deducted by someone who doesn't know the recipient's full tax position. So the rate roughly tracks the *expected effective tax* on that stream. A contractor's gross receipt is mostly turnover with thin margins → low rate (1–2%). Professional fees are almost pure income → higher rate (10%). Salary → the *actual* slab rate, because the employer *can* compute it precisely. Lottery winnings → flat 30%, because they are taxed at the maximum flat rate anyway.

**Why TCS (collect at source) in addition to TDS (deduct at source)?**
TDS works when someone *pays* the taxpayer. But what about a person who *spends* big — buying a car, buying liquor-vending rights, remitting money abroad? There is no incoming payment to deduct from. So the mirror-image tool: the **seller collects** an extra slice from the buyer. It catches high-value spenders and traders in sectors historically prone to under-reporting (scrap, minerals, alcohol).

*Figure 10.2 — TDS vs TCS are mirror images around the transaction.*

```mermaid
flowchart LR
    P["Payer / Deductor"] -->|"pays amount MINUS tax"| R["Recipient - the taxpayer"]
    P -->|"deposits TDS"| G1["Government"]
    B["Buyer - the taxpayer"] -->|"pays amount PLUS tax"| S["Seller / Collector"]
    S -->|"deposits TCS"| G2["Government"]
```

---

## 4. Full Technical Content

### 4A. ADVANCE TAX (Sections 207–211, 234B, 234C)

**Sec 207 — Liability.** Advance tax is payable on the **current income** (income of the year for which it is being computed), estimated by the assessee.

**Sec 208 — The threshold (the WHY of ₹10,000).** Advance tax is payable only if the **estimated tax liability for the year is ₹10,000 or more**. Reason: for tiny liabilities, the machinery of four instalments is disproportionate; a small taxpayer can settle at return-filing without harming the State's cash flow.

**The senior-citizen relief (Sec 207(2)).** A **resident individual aged 60 or above** who does **NOT** have income under the head "Profits and Gains of Business or Profession (PGBP)" is **exempt from advance tax entirely**. Why? A retired senior's income is mostly interest/pension, on which TDS already applies, and asking a pensioner to run quarterly estimates is an unfair burden. Note the two conditions — *resident* + *no business income*. A senior with business income is NOT exempt.

**Sec 209 — Computation.** 
```
Estimated total income  →  Tax on it at applicable rates
+ surcharge + health & education cess (4%)
− relief/rebate (e.g. 87A)
− TDS / TCS deductible on your income
= Advance tax payable
```
The critical logic: you subtract TDS/TCS **that is deductible/collectible** on your income, because that tax is already being handled by someone else. You only prepay the *gap*.

**Sec 211 — Instalments and WHY the schedule looks like this.**

For **all assessees** (except those covered by presumptive taxation below):

| Due date | Cumulative advance tax payable | Logic |
|---|---|---|
| On or before **15 June** | **15%** | Barely into the year; only a rough sense of income |
| On or before **15 September** | **45%** | Half-year visible; catch up |
| On or before **15 December** | **75%** | Three-quarters clear |
| On or before **15 March** | **100%** | Full-year estimate; final top-up before 31 March |

**Presumptive taxpayers (Sec 44AD / 44ADA):** they pay **100% in a single instalment by 15 March**. Why the concession? Their income is a fixed presumptive percentage of turnover, knowable only near year-end, and the whole point of presumptive schemes is *reduced compliance*. Splitting into four would defeat that.

**Memory hook — "15-45-75-100 on the 15th of J-S-D-M":** every instalment falls on the **15th**, in **June, September, December, March**. The cumulative jumps by **30 percentage points** each time after the first (15, +30=45, +30=75, +25=100 — the last step is only 25 because you're already near the top).

**Sec 234B — Interest for default in payment of advance tax.**
- *Trigger:* advance tax paid is **less than 90%** of assessed tax (or no advance tax paid at all, though liable).
- *Rate:* **1% per month or part of a month.**
- *Period:* from **1st April** of the AY to the date of determination of income / payment of self-assessment tax.
- *Base:* on the **shortfall** (assessed tax minus advance tax paid).
- *WHY 90%, not 100%?* Estimating one's own income perfectly is impossible; the law tolerates a 10% margin of error before penalising.

**Sec 234C — Interest for deferment (wrong *timing* of instalments).**
- *Trigger:* an instalment is **short** of the required cumulative percentage on its due date.
- *Rate:* **1% per month.**
- *Period:* **3 months** for the first three instalments (June, Sept, Dec) and **1 month** for the last (March).
- *WHY the tolerance bands?* For the June and September instalments the law only requires you to have paid **12% and 36%** respectively (not 15% and 45%) to escape 234C — because early estimation is hard. No 234C is charged on shortfalls arising from **capital gains, casual income (lottery), or first-time business income** that could not be foreseen — you compute that portion in the instalment *after* it arose.

*Figure 10.3 — Advance tax decision flow.*

```mermaid
flowchart TD
    A["Estimate tax liability for the year"] --> B{"Is estimated tax 10000 or more"}
    B -->|No| Z["No advance tax - pay at return filing"]
    B -->|Yes| C{"Resident senior 60 plus with NO business income"}
    C -->|Yes| Z
    C -->|No| D{"Presumptive under 44AD or 44ADA"}
    D -->|Yes| E["Pay 100 percent by 15 March"]
    D -->|No| F["Pay 15-45-75-100 by 15 Jun Sep Dec Mar"]
    F --> G{"Paid at least 90 percent of assessed tax"}
    G -->|No| H["234B interest applies"]
    G -->|Yes| I{"Each instalment on time"}
    I -->|No| J["234C interest applies"]
    I -->|Yes| K["No interest"]
```

---

### 4B. TDS — Tax Deducted at Source (Sections 192–196)

**The general mechanics (why the timing rule is "payment OR credit, whichever is earlier"):** Most non-salary TDS sections say deduct at the time of **credit to the account of the payee OR payment, whichever is earlier**. Reason: to stop a payer from parking a liability in the books (crediting the payee) while indefinitely delaying the actual cash payment — and thereby delaying TDS. The law grabs tax at the *earlier* event.

**Key sections you must know (rates for AY 2025-26 — verify against current ICAI):**

| Section | Nature of payment | Threshold (no TDS below) | Rate | The WHY of the rate |
|---|---|---|---|---|
| **192** | **Salary** | Basic exemption / where tax payable | **Average rate** (actual slab) | Employer knows full salary → can compute exact tax |
| **192A** | Premature PF withdrawal | ₹50,000 | 10% | Discourages early withdrawal; flat estimate |
| **194A** | Interest (other than securities) — banks, etc. | ₹40,000 (₹50,000 for seniors); ₹5,000 others | 10% | Interest is pure income |
| **194** | Dividend | ₹5,000 | 10% | Dividend is pure income (taxable in shareholder's hands) |
| **194C** | Payment to contractor/sub-contractor | ₹30,000 single / ₹1,00,000 aggregate p.a. | **1%** (individual/HUF payee), **2%** (others) | Mostly turnover, thin margin → low rate |
| **194H** | Commission or brokerage | ₹15,000 | 2% (recently reduced from 5%) | Commission is income but modest margins |
| **194I** | Rent | ₹2,40,000 p.a. | 2% (plant & machinery), 10% (land/building/furniture) | Rent is income; P&M lower as it carries depreciation |
| **194J** | Professional / technical fees, royalty | ₹30,000 | 10% (2% for technical services / call-centres) | Professional fee ≈ pure income → higher rate |
| **194IA** | Transfer of immovable property (not agri land) | ₹50,00,000 | 1% | High-value asset; catch capital gains |
| **194IB** | Rent by individual/HUF (not liable to audit) | ₹50,000 **per month** | 2% | Brings big personal rents into the net |
| **194Q** | Purchase of goods (buyer with turnover > ₹10 cr) | ₹50,00,000 | 0.1% | Mirror of 206C(1H); trade paper trail |
| **194O** | E-commerce operator to participant | ₹5,00,000 (individual/HUF) | 1% | Captures the gig / online economy |
| **194B / 194BB** | Winnings — lottery, crossword, horse races | ₹10,000 (aggregate for 194B) | **30%** | Taxed at max flat rate anyway; windfall |
| **195** | Payment to non-resident | No threshold | Rates in force / DTAA | Non-resident may vanish; catch tax before it leaves India |

**Sec 192 in depth (salary).** The employer must estimate the employee's total salary income for the year, allow eligible deductions (if the employee opts for the old regime and submits proofs), compute tax on the estimate, and deduct **1/12th each month** (the "average rate"). This is the *only* TDS section that uses the actual slab rate rather than a flat rate — because the employer has full information. The employee can report other income (and TDS on it) to the employer under Sec 192(2B) so that one consolidated deduction happens.

**Sec 197 — Lower / Nil deduction certificate.** If TDS at the normal rate would exceed the recipient's actual liability (e.g., a loss-making company still gets TDS on its interest), it can apply to the AO for a certificate to deduct at a lower or nil rate. This fixes the over-deduction problem at source rather than through a slow refund.

**Sec 206AA — No PAN, higher TDS.** If the deductee does not furnish PAN, TDS is deducted at the **higher of** the normal rate **or 20%**. Why? PAN is the thread that links the TDS to a person. No PAN = the department can't trace the credit = it penalises with a punitive rate to force PAN disclosure.

**Due dates for depositing TDS.**
- Tax deducted in **any month (April–February): by the 7th of the next month.**
- Tax deducted in **March: by 30th April.** (Extra time given because the year just closed and books are being finalised.)

**Quarterly TDS returns (statements):** Form 24Q (salary), 26Q (other resident payments), 27Q (non-residents) — filed quarterly, due generally by the end of the month following the quarter (Q4 by 31 May).

**Consequences of TDS default (the enforcement logic — three layers of pain):**

1. **Interest u/s 201(1A):**
   - Failure to **deduct**: **1% p.m.** from the date tax was deductible to the date it is actually deducted.
   - Failure to **deposit** (after deducting): **1.5% p.m.** from the date of deduction to the date of deposit. *Why higher (1.5%)?* Because failing to deposit after deducting means you *held the government's money* — that is far worse than merely failing to deduct, so it is punished harder.
2. **Disallowance u/s 40(a)(ia):** if TDS is not deducted/deposited, **30% of the expenditure is disallowed** while computing the payer's business income (100% for payments to non-residents u/s 40(a)(i)). This is the sharpest teeth — it hits the payer's *own* taxable profit, aligning his incentive with compliance. The disallowance is reversed in the year the TDS is finally paid.
3. **Fee u/s 234E and penalty u/s 271H** for late/non-filing of TDS returns: **₹200 per day** (234E, capped at the TDS amount) plus penalty ₹10,000–₹1,00,000 (271H).

Additionally, **Sec 201** treats a defaulting deductor as an **"assessee in default"**, and failure to deposit tax deducted can attract **prosecution u/s 276B** (rigorous imprisonment). The escalation from interest → disallowance → penalty → prosecution is deliberate: the State makes non-compliance progressively unbearable.

---

### 4C. TCS — Tax Collected at Source (Section 206C)

The seller of certain goods/rights collects an *additional* amount from the buyer at the time of sale/receipt and deposits it. Key items and rates (verify current):

| Item (Sec 206C) | Rate |
|---|---|
| Alcoholic liquor for human consumption | 1% |
| Timber / other forest produce | 2.5% |
| Scrap | 1% |
| Tendu leaves | 5% |
| Minerals (coal, lignite, iron ore) | 1% |
| Motor vehicle above ₹10,00,000 | 1% |
| **206C(1H)** — Sale of goods, seller turnover > ₹10 cr, buyer receipts > ₹50 lakh | 0.1% |
| **206C(1G)** — Remittance under LRS / overseas tour package (above ₹7 lakh) | 5% (20% for tour packages / higher LRS as amended) |

**The logic of the item list:** notice these are historically **cash-heavy, under-reported, or high-value discretionary** categories — liquor, scrap, forest produce, luxury cars, foreign travel. TCS drags them into a documented trail. TCS collected is credited to the buyer and adjusted against his final tax, exactly like TDS.

**Due date to deposit TCS:** within **7 days** from the end of the month of collection. **Quarterly return:** Form 27EQ.

---

## 5. Worked Examples

### Example 1 — Advance tax: basic instalment schedule (easy)

**Facts:** Mr. Arjun (age 40, salaried + FD interest) estimates total tax liability for AY 2025-26 at **₹1,00,000**. TDS already deducted by his bank/employer during the year = **₹40,000**. Compute advance tax and instalments.

**Step 1 — Is advance tax payable?** Net liability after TDS = 1,00,000 − 40,000 = **₹60,000 ≥ ₹10,000** → Yes, advance tax applies (Sec 208).

**Step 2 — Advance tax base (Sec 209).** Advance tax payable = ₹60,000 (tax minus TDS deductible on his income).

**Step 3 — Instalments (Sec 211):**

| Due date | Cumulative % | Cumulative amount | Paid this instalment |
|---|---|---|---|
| 15 Jun | 15% | 9,000 | 9,000 |
| 15 Sep | 45% | 27,000 | 18,000 |
| 15 Dec | 75% | 45,000 | 18,000 |
| 15 Mar | 100% | 60,000 | 15,000 |

**Reconciliation:** 9,000 + 18,000 + 18,000 + 15,000 = **₹60,000** ✓ Matches net liability.

---

### Example 2 — 234C interest for deferment (medium)

**Facts:** Ms. Beena's assessed tax (net of TDS) for AY 2025-26 is **₹2,00,000**. She actually paid advance tax as: 15 Jun — ₹20,000; 15 Sep — ₹60,000; 15 Dec — ₹1,30,000; 15 Mar — ₹2,00,000 (cumulative). No capital gains/casual income. Compute 234C interest.

We test each instalment against the required cumulative amount. (For June/Sept, the 234C "safe harbour" is **12%** and **36%**; if she paid at least that, no interest for that instalment even if below 15%/45%.)

| Instalment | Required cumulative | Safe-harbour cumulative | Actually paid (cum.) | Shortfall? | Interest |
|---|---|---|---|---|---|
| 15 Jun | 15% = 30,000 | 12% = 24,000 | 20,000 | Yes (< 24,000) | 1% × 3 months × shortfall |
| 15 Sep | 45% = 90,000 | 36% = 72,000 | 60,000 | Yes (< 72,000) | 1% × 3 months × shortfall |
| 15 Dec | 75% = 1,50,000 | (75% strict) | 1,30,000 | Yes | 1% × 3 months × shortfall |
| 15 Mar | 100% = 2,00,000 | — | 2,00,000 | No | Nil |

**Shortfall computation** (234C uses the *required %* as the base once the safe-harbour is failed):

- **June:** required 15% = 30,000; paid 20,000; shortfall = 10,000. Interest = 10,000 × 1% × 3 = **₹300**
- **Sept:** required 45% = 90,000; paid 60,000; shortfall = 30,000. Interest = 30,000 × 1% × 3 = **₹900**
- **Dec:** required 75% = 1,50,000; paid 1,30,000; shortfall = 20,000. Interest = 20,000 × 1% × 3 = **₹600**
- **March:** no shortfall → **Nil**

**Total 234C interest = 300 + 900 + 600 = ₹1,800.**

*Note:* Because she paid the full ₹2,00,000 by 15 March, **234B does not apply** (she paid ≥ 90% of assessed tax by year-end). 234C punished only the *timing*.

---

### Example 3 — TDS across multiple sections + 201(1A) interest (exam-hard)

**Facts:** Zenith Pvt. Ltd. made the following payments during FY 2024-25 (AY 2025-26). Determine TDS in each case, then compute interest where a default occurred.

1. Rent for office building: **₹3,60,000** for the year (paid monthly ₹30,000).
2. Fees to a consultant CA (professional): **₹80,000**.
3. Payment to a contractor (a firm) for civil work: single bill **₹1,50,000**.
4. Commission to an agent: **₹40,000**.
5. Interest on a loan from a resident (non-bank): **₹1,00,000**.

**Step 1 — Test each against threshold and apply rate:**

| Payment | Section | Threshold | Crossed? | Rate | TDS |
|---|---|---|---|---|---|
| Rent (building) 3,60,000 | 194I | 2,40,000 | Yes | 10% | **36,000** |
| Professional fee 80,000 | 194J | 30,000 | Yes | 10% | **8,000** |
| Contractor (firm) 1,50,000 | 194C | 30,000 single | Yes | 2% (payee is firm) | **3,000** |
| Commission 40,000 | 194H | 15,000 | Yes | 2% | **800** |
| Interest 1,00,000 | 194A | 5,000 (non-bank) | Yes | 10% | **10,000** |

**Total TDS to be deducted = 36,000 + 8,000 + 3,000 + 800 + 10,000 = ₹57,800.**

**Step 2 — Default scenario.** Suppose Zenith deducted the ₹8,000 (professional fee) on **10 January 2025** but deposited it only on **15 May 2025** (due date was 7 February 2025). Compute 201(1A) interest.

- It *deducted* on time, so the 1% "failure-to-deduct" interest doesn't apply.
- It *failed to deposit* → **1.5% per month** from date of deduction (10 Jan) to date of deposit (15 May).
- Months (part of a month counts as a full month): Jan, Feb, Mar, Apr, May = **5 months**.
- Interest = 8,000 × 1.5% × 5 = **₹600.**

**Step 3 — Consequence beyond interest.** If Zenith had *not deducted at all* on the ₹80,000 professional fee, then u/s 40(a)(ia), **30% of ₹80,000 = ₹24,000 would be disallowed** as a deduction while computing Zenith's business income — inflating its taxable profit — until the TDS is eventually paid. This shows why deductors comply: the disallowance often hurts far more than the TDS itself.

---

### Example 4 — Advance tax with a senior citizen twist + 234B (reconciling)

**Facts:** Mr. Rao, **age 67, resident**, has pension income and bank interest only (**no business income**). Estimated tax for AY 2025-26 = ₹35,000, of which TDS on interest = ₹15,000. Is advance tax payable?

**Answer:** Although net liability (35,000 − 15,000 = 20,000) exceeds ₹10,000, Mr. Rao is a **resident senior citizen (60+) with NO PGBP income** → **exempt from advance tax u/s 207(2)**. He simply pays ₹20,000 as **self-assessment tax** at return filing, and **no 234B/234C interest** applies to him for non-payment of advance tax.

**Contrast:** If Mr. Rao *also* ran a small business, the exemption vanishes — he would owe advance tax and face 234B/234C on default. This single condition ("no business income") is a favourite examiner trap.

---

## 6. Computation Format

**Advance tax computation (Sec 209) — standard format:**

```
Estimated income under each head            XXX
Gross Total Income                          XXX
Less: Chapter VI-A deductions              (XXX)
Total Income                                XXX
------------------------------------------------
Tax on total income at applicable rates     XXX
Add: Surcharge (if applicable)               XXX
Add: Health & Education Cess @ 4%            XXX
Less: Rebate u/s 87A                        (XXX)
------------------------------------------------
Tax liability                               XXX
Less: TDS / TCS deductible on income       (XXX)
------------------------------------------------
ADVANCE TAX PAYABLE                         XXX
   → split 15% / 45% / 75% / 100%
```

**234C interest per instalment:**
```
Interest = Shortfall in instalment × 1% × (3 months for Jun/Sep/Dec, 1 month for Mar)
Shortfall = Required cumulative advance tax − Advance tax actually paid up to that date
(Safe harbour: 12% by Jun, 36% by Sep escapes 234C)
```

**234B interest:**
```
Interest = (Assessed tax − Advance tax paid) × 1% × months from 1 April of AY to date of payment
Applies only if advance tax paid < 90% of assessed tax
```

**201(1A) interest (deductor default):**
```
Not deducted:  Amount × 1%   × months (deductible date → actual deduction)
Not deposited: Amount × 1.5% × months (deduction date → deposit date)
```

---

## 7. Connections

- **To "Computation of Total Income & Tax Liability":** Advance tax/TDS/TCS are *not* new taxes — they are prepayments of the *same* liability computed in earlier chapters. The final tax (Chapter on tax computation) minus these prepayments = balance payable or refund.
- **To PGBP:** Sec 40(a)(ia) disallowance links TDS default directly into business-income computation. A PGBP question can hide a TDS trap.
- **To "Return Filing & Self-Assessment" (Sec 140A):** self-assessment tax is what remains after advance tax + TDS + TCS. Form 26AS / AIS is the reconciliation ledger.
- **To Interest sections 234A/234B/234C:** 234A (late return filing) sits alongside 234B/234C; all are 1% p.m. and often examined together as a combined interest computation.
- **To Assessment / Refunds:** excess TDS is refunded with interest u/s 244A — the mirror of the interest the taxpayer pays.

---

## 8. Traps & Examiner Tricks

1. **Senior-citizen advance-tax exemption needs BOTH conditions:** resident **and** no business income. Examiners give a senior with a small business and expect you to *not* exempt him.
2. **234C safe harbour (12%/36%) vs required (15%/45%):** the tolerance applies only to the *first two* instalments and only decides *whether* interest triggers — once triggered, the shortfall is measured against the **full required %**, not the safe-harbour %.
3. **234B base is 90%:** paying 89% triggers 234B on the *entire* shortfall from assessed tax; paying 90%+ escapes it entirely. A one-percent miss is expensive.
4. **194C two rates:** 1% if payee is **individual/HUF**, 2% otherwise. Also two thresholds: ₹30,000 single bill *or* ₹1,00,000 aggregate in the year.
5. **194I two rates:** 2% for plant & machinery, 10% for land/building/furniture. Candidates apply a single rate and lose marks.
6. **"Credit or payment, whichever is earlier":** TDS liability can arise on *crediting* the payee even before cash is paid. Don't wait for payment.
7. **Deduct vs deposit interest (201(1A)):** 1% for not deducting, **1.5%** for deducting-but-not-depositing. Mixing them up is common.
8. **No PAN → 20% (Sec 206AA):** if a question says the payee didn't give PAN, ignore the normal rate and apply the higher of normal or 20%.
9. **Presumptive taxpayers pay 100% by 15 March** — do NOT split them into four instalments.
10. **TCS is ADDED to the buyer's price; TDS is DEDUCTED from the recipient's payment.** Direction matters in computation.
11. **March TDS deposit deadline is 30 April** (not 7 April) — a deliberate exception.
12. **Threshold is on the payment stream, not per bill for aggregate limits** — e.g., 194C's ₹1,00,000 aggregate catches many small bills that individually escape ₹30,000.

---

## 9. First-Principles Recap

Start from the State's need: **steady, reliable, evasion-proof revenue.** From that single need, everything is derivable:

- Waiting until year-end fails → **collect during the year** → *advance tax*, in instalments front-weighted to reality (15-45-75-100).
- Relying on the taxpayer alone fails → **collect from the payer** → *TDS*, at the earlier of credit/payment, at rates approximating each income stream's tax, above thresholds that justify the friction.
- Some big-money flows are *outgoing* (spending), not incoming → **collect from the seller** → *TCS*, on discretionary/under-reported categories.
- To make all three self-enforcing → **interest (234B/C, 201(1A)) + disallowance (40(a)(ia)) + penalty/prosecution**, escalating in severity, plus **PAN linkage (206AA)** so every rupee is traceable and lands in **Form 26AS/AIS**.

If you can regenerate the schedule, the rates' logic, and the penalty ladder from "the State needs steady, traceable cash," you never have to memorise them.

---

## 10. Quick-Revision Sheet

**Advance Tax**
- Payable if estimated tax **≥ ₹10,000** (Sec 208).
- Exempt: **resident senior (60+) with NO business income** (Sec 207(2)).
- Instalments (Sec 211): **15% / 45% / 75% / 100%** by **15 Jun / Sep / Dec / Mar**.
- Presumptive (44AD/44ADA): **100% by 15 March.**
- **234B:** paid < 90% of assessed tax → 1% p.m. on shortfall from 1 April of AY.
- **234C:** short instalment → 1% p.m. × 3 (first three) / × 1 (last); safe harbour 12%/36% for Jun/Sep.

**TDS — key sections**
- 192 salary (average slab rate); 194A interest (10%, threshold 40k/50k/5k); 194C contractor (1%/2%, 30k/1L); 194H commission (2%, 15k); 194I rent (2% P&M, 10% others, 2.4L); 194J professional (10%, 30k); 194IA property (1%, 50L); 195 non-resident (rates in force, no threshold).
- Timing: **credit or payment, whichever earlier.**
- No PAN → **higher of normal or 20%** (206AA).
- Deposit: **7th of next month**; **March by 30 April.**
- Returns: 24Q/26Q/27Q quarterly.

**TDS default**
- 201(1A): **1%** (not deducted) / **1.5%** (not deposited) p.m.
- 40(a)(ia): **30% expense disallowed** (100% for non-resident u/s 40(a)(i)).
- 234E: ₹200/day; 271H penalty ₹10k–₹1L; 276B prosecution.

**TCS (206C)**
- Liquor 1%, scrap 1%, timber 2.5%, tendu 5%, minerals 1%, motor vehicle > ₹10L 1%.
- 206C(1H) sale of goods 0.1% (turnover > 10cr, buyer > 50L); 206C(1G) LRS/tour 5%/20%.
- **Added** to buyer's price; deposit within **7 days** of month-end; return Form 27EQ.

> *Final reminder: thresholds and 194-series rates change frequently. Before the exam, cross-check every figure here against the ICAI Study Material and the Finance Act applicable to your Assessment Year.*
