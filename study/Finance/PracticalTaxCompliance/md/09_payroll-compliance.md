# Payroll & compliance basics

## What it is & where it's used

Payroll is the monthly process of converting an employee's CTC into a **net-pay number in their bank account**, while simultaneously deducting and depositing the right taxes and social-security contributions with the government — TDS, PF, ESI, Professional Tax. Get it wrong and you don't just annoy staff; you trigger interest, penalties, and a personal liability on the "principal officer" for TDS defaults.

Roles that live in this:

- **Payroll executive / HR-Ops** — runs the monthly cycle, files challans.
- **Accounts / Finance associate** — books the payroll journal, reconciles the salary-payable and statutory-dues ledgers.
- **Tax associate** — computes TDS on salary (Sec 192), issues Form 16, files Form 24Q.
- **Consultant / articleship (CA)** — verifies client payroll, catches PF/ESI wage-base errors in audit.

Even if you never "do payroll," every finance person books the salary journal and answers the auditor's question: *"Does statutory dues payable tie to what was actually deposited?"*

## The gap: why companies want this (and college didn't teach it)

MBA and CA-Inter teach you that "salary is an expense" and that "Section 192 requires TDS." What they don't teach:

- The difference between **CTC, gross, and take-home** — three numbers that confuse every fresher and every new joiner you'll have to explain it to.
- That PF is on **Basic + DA** (capped at ₹15,000 wage), ESI is on **gross ≤ ₹21,000**, and PT is a **slab by state** — three different wage bases, three different rules.
- The **old vs new tax regime** choice and how it changes monthly TDS.
- That TDS on salary is deposited by the **7th**, PF by the **15th**, ESI by the **15th**, and the quarterly **24Q** return is what actually populates the employee's Form 26AS/AIS.

Colleges test definitions; employers test whether you can produce a payroll register, a challan, and a Form 16 that reconciles. That reconciliation muscle is the gap.

## What "proficient" looks like

A job-ready person can, unaided:

- Build a **salary structure** from a CTC number, splitting Basic/HRA/allowances correctly.
- Compute **monthly TDS** under both regimes by annualising, applying deductions, and dividing tax by remaining months.
- Calculate **PF (12%+12%), ESI (0.75%+3.25%), PT** on the correct wage bases.
- Produce a **payroll register**, pass the **journal entry**, and reconcile statutory-dues ledgers to challans paid.
- Know the **due dates** and the **forms** (24Q, ECR, ESI return, Form 16 Part A + B).

## Hands-on: how to actually do it

### 1. Salary structure from CTC (Excel)

A common ₹9,00,000 CTC split. Layout with formulas (Basic = 40% of CTC is a typical policy):

| Component | Formula (cell refs) | Monthly | Annual |
|---|---|---|---|
| Basic | `=ROUND(CTC*0.40/12,0)` | 30,000 | 3,60,000 |
| HRA | `=ROUND(Basic*0.50,0)` (metro) | 15,000 | 1,80,000 |
| Special allowance | balancing figure | 20,500 | 2,46,000 |
| Employer PF | `=ROUND(MIN(Basic,15000)*0.12,0)` | 1,800 | 21,600 |
| **CTC** | `=SUM(...)` | **75,000** | **9,00,000** |

Gross = Basic + HRA + Special = ₹65,500/month. Employer PF is part of CTC but **not** part of gross.

### 2. Statutory deductions (the three wage bases)

```excel
Employee PF   =ROUND(MIN(Basic_DA,15000)*0.12,0)        ' 1,800
ESI (if gross<=21000) =ROUND(Gross*0.0075,0)            ' 0 here, gross>21k
PT (Karnataka) =IF(Gross>=25000,200,0)                  ' 200
```

ESI applies only when gross ≤ ₹21,000 (₹25,000 for disabled). Employer ESI = 3.25% of gross.

### 3. Monthly TDS on salary — the annualise-and-divide method

```
Step 1  Projected annual gross          = monthly gross × 12  (+ bonus already known)
Step 2  Less: exemptions (HRA, std ded ₹50k)
Step 3  Less: Chapter VI-A (80C, 80D…) — only if OLD regime
Step 4  = Taxable income → apply slab   → gross tax
Step 5  + 4% cess                       → total tax liability
Step 6  Monthly TDS = (total tax − TDS already deducted) / months remaining
```

Excel slab tax (new regime FY 2024-25) using a helper approach:

```excel
=ROUND(
  MAX(0,MIN(TI,700000)-300000)*0.05
 +MAX(0,MIN(TI,1000000)-700000)*0.10
 +MAX(0,MIN(TI,1200000)-1000000)*0.15
 +MAX(0,MIN(TI,1500000)-1200000)*0.20
 +MAX(0,TI-1500000)*0.30 ,0)
```
Then `Tax_with_cess = Tax*1.04`, and apply the **87A rebate** (nil tax if taxable ≤ ₹7,00,000 under new regime).

### 4. The payroll journal entry

For total gross ₹6,55,000, employee PF ₹18,000, TDS ₹40,000, ESI ee ₹0, PT ₹2,000, plus employer PF ₹18,000:

| Account | Dr | Cr |
|---|---|---|
| Salaries & Wages A/c | 6,55,000 | |
| Employer PF Contribution A/c | 18,000 | |
| &nbsp;&nbsp;To TDS Payable (Sec 192) | | 40,000 |
| &nbsp;&nbsp;To PF Payable (ee 18,000 + er 18,000) | | 36,000 |
| &nbsp;&nbsp;To PT Payable | | 2,000 |
| &nbsp;&nbsp;To Salary Payable (net) | | 5,95,000 |

On payment of net salary: `Salary Payable Dr / To Bank`. On depositing each statutory due: `PF Payable Dr / To Bank`, etc. The payable ledgers should hit **zero** after deposit — that is your reconciliation.

### 5. Portal click-paths (compliance run)

- **TDS challan (ITNS 281):** incometax.gov.in → e-Pay Tax → New Payment → *TDS on Salary (192)* → Assessment Year → fill tax/interest → pay → save the **CIN/BSR + challan no.** By the **7th**.
- **PF (ECR):** unifiedportal-emp.epfindia.gov.in → Payments → ECR Upload → upload text file → verify → Prepare Challan → Pay. By the **15th**.
- **ESI:** esic.in → File Monthly Contribution → enter wages → Submit → Pay online. By the **15th**.
- **Form 24Q (quarterly):** prepare via RPU utility → validate with FVU → upload on TRACES/e-filing → download **Form 16 Part A** from TRACES after processing.

## Worked example / mini-project

**Rohan, ₹9,00,000 CTC, joins 1 Apr, new regime, no 80C.** Reproduce his year:

- Monthly gross = ₹65,500 → annual gross = ₹7,86,000.
- Less standard deduction ₹50,000 → **taxable = ₹7,36,000**.
- Slab tax (new): 3–7L @5% = ₹20,000; 7–7.36L @10% = ₹3,600 → ₹23,600.
- 87A rebate: taxable > ₹7,00,000, so **no rebate**. Tax = ₹23,600.
- Cess 4% = ₹944 → **annual tax = ₹24,544**.
- **Monthly TDS = 24,544 / 12 = ₹2,045** (round; adjust in March).

Monthly deductions: PF ₹1,800 + PT ₹200 + TDS ₹2,045 = ₹4,045.
**Take-home = 65,500 − 4,045 = ₹61,455.**

Now build the full 12-row payroll register in Excel with columns *Basic, HRA, Special, Gross, PF, PT, TDS, Net*, sum the TDS column (₹24,540) and confirm it matches the four 24Q quarterly returns and Rohan's Form 16 Part B. If they tie, your compliance run is clean.

## How it's tested

**Interview questions:**
- "Difference between CTC, gross and net?" (you must draw the three wage bases)
- "What's the TDS due date and what happens if you miss it?" (7th; 1.5%/month interest + Sec 40(a)(ia) disallowance)
- "PF is calculated on what?" (Basic + DA, capped ₹15,000)
- "Old vs new regime — which gives lower TDS for someone with ₹1.5L 80C and ₹2L home-loan interest?"

**Practical assessments:**
- A **timed Excel test**: "Here's a CTC, build the salary structure and compute monthly TDS both regimes." (45 min)
- A **reconciliation case**: "Statutory dues payable shows ₹1,10,000; challans total ₹95,000 — find the ₹15,000 gap." (usually an employer-PF line not deposited or an admin-charge omission)
- "**Prepare Form 16 Part B** from this payroll register."

## Common mistakes & how pros avoid them

| Mistake | Fix |
|---|---|
| PF on gross instead of Basic+DA | Wage base = Basic+DA, `MIN(...,15000)` cap |
| Forgetting **employer** PF/ESI in CTC and in the journal | Employer contributions are a cost + a payable, not just employee side |
| ESI applied above ₹21,000 gross | ESI ceases once gross crosses ₹21,000 (continues till contribution-period end) |
| Depositing TDS but not filing 24Q | No 24Q → nothing in employee's 26AS → Form 16 Part A can't generate |
| Rebate 87A confusion | New regime: nil tax ≤ ₹7L taxable; ₹1 over means full slab tax (marginal relief applies) |
| Standard deduction missed | ₹50,000 (₹75,000 new regime FY24-25) available to all salaried |
| Statutory dues not reconciled to challans | Every payable ledger must zero out post-deposit each month |

Pros keep a **compliance calendar** (7th TDS, 15th PF/ESI, quarter-end 24Q) and never close the month until payable ledgers reconcile to the CIN/challan numbers.

## Learn-it roadmap & resources

**Time to proficiency: 3–4 weeks** if you already know basic accounting.

- Week 1 — Salary structuring + the three wage bases. Build 5 dummy structures in Excel.
- Week 2 — TDS on salary both regimes; reproduce the worked example, then vary 80C/HRA.
- Week 3 — Run one full mock cycle: register → journal → challans → 24Q → Form 16.
- Week 4 — Do it inside **TallyPrime payroll** and on the **EPFO/ESIC demo** flows.

Resources:
- **Free:** ClearTax and TaxAdda salary/TDS guides; EPFO & ESIC official portals; income-tax e-filing help section; RPU utility docs (Protean/NSDL).
- **Paid:** TallyPrime payroll module; Udemy "Indian Payroll & Statutory Compliance" courses; greytHR / Zoho Payroll free trials to see a real SaaS payroll run.
- **Certification:** CA-Inter Taxation already covers Sec 192; NISM has none here, but greytHR Academy and Tally certifications signal payroll-tool fluency.

## Quick-reference

| Item | Rule / Rate | Due date | Form |
|---|---|---|---|
| TDS on salary | Sec 192, avg rate, annualise ÷ months | 7th next month | Challan 281 → 24Q (qtrly) |
| PF | 12% ee + 12% er on Basic+DA (cap ₹15,000) | 15th | ECR |
| ESI | 0.75% ee + 3.25% er on gross ≤ ₹21,000 | 15th | Monthly contribution |
| Professional Tax | State slab (KA/MH ≈ ₹200/mo max ₹2,500/yr) | varies by state | State PT return |
| Form 16 | Part A (TRACES) + Part B (employer) | by 15 Jun | Form 16 |
| Standard deduction | ₹50,000 old / ₹75,000 new (FY24-25) | — | — |
| 87A rebate (new) | Nil tax if taxable ≤ ₹7,00,000 | — | — |
| Late TDS interest | 1% (not deducted) / 1.5% (not paid) per month | — | — |

**Golden checks:** gross = Basic+HRA+allowances (no employer PF); take-home = gross − PF − PT − TDS − ESI(ee); every statutory-payable ledger must zero out after deposit; TDS column total = sum of four 24Q returns = Form 16 Part B.
