# Running Payroll: PF, ESI, PT and the Salary Journal

## The situation

It's the morning of **28 April 2026**. This just landed on your desk: the HR head at **Nirvana Traders & Services Pvt Ltd (NTSPL)** drops the April attendance sheet in your inbox with one line — *"All 15 present full month, no LOP. Please run salaries so the bank file goes out on the 30th and statutory payments are ready."*

You are the accounts executive. "Running salaries" means five separate things must all be right by month-end:

1. Compute each employee's **gross → deductions → net take-home**.
2. Deduct **EPF** (Provident Fund) correctly on the capped wage.
3. Deduct **ESI** only for the staff who are still under the wage ceiling.
4. Deduct **Professional Tax (PT)** per the Telangana slab.
5. Deduct **TDS on salary u/s 192** using each person's estimated annual tax under the new regime.

Then post **one consolidated salary journal**, and later a payment entry when the bank actually pays. Gross monthly payroll is **Rs 9,00,000** across 15 staff. Statutory dues (PF/ESI) must hit the government by the **15th of May**.

> Note on section numbers: the Income-tax Act, 2025 (effective 01-Apr-2026) re-numbers salary TDS under **Sec 392** and other TDS under **Sec 393**. On the job, in TallyPrime and on TRACES, everyone still says **"192"** and **"194x"** — so I flag it once here, then use the familiar numbers throughout.

## What you're given

The raw payroll register for April 2026 (FY2026-27). Three staff are still under the ESI ceiling of Rs 21,000; the rest are above it.

| Employee | Basic | HRA | Special | **Gross** | ESI-eligible? | PT slab |
|---|---:|---:|---:|---:|---|---|
| Priya Rao (sample) | 30,000 | 15,000 | 10,000 | **55,000** | No | Rs 200 |
| 11 other staff (above ceiling) | — | — | — | **6,90,000** (combined) | No | Rs 200 each |
| 3 ESI workers @ 18,000 | — | — | — | **54,000** (combined) | Yes | Rs 200 each |
| **Total** | | | | **9,00,000** | | |

FY2026-27 statutory reference:

- **EPF:** 12% employee + 12% employer, on basic subject to **wage ceiling Rs 15,000**. Employer 12% splits: **EPS 8.33% = Rs 1,250** + **EPF 3.67% = Rs 550**. Deposit by **15th** of next month (ECR on the EPFO portal).
- **ESI:** employee **0.75%** + employer **3.25%**, on gross, **ceiling Rs 21,000**. Deposit by **15th**.
- **PT (Telangana):** wage > Rs 20,000 → **Rs 200/month**; Rs 15,001–20,000 → Rs 150; up to Rs 15,000 → nil.
- **TDS 192:** slab tax on **estimated annual income**, spread over 12 months. New regime is default: 0–4L nil, 4–8L 5%, 8–12L 10%, 12–16L 15%, 16–20L 20%, 20–24L 25%, >24L 30%. **Sec 87A rebate Rs 60,000** (nil tax up to taxable Rs 12L). **Standard deduction Rs 75,000**.

## Do it — step by step

### Step 1 — Priya Rao's payslip

**EPF (employee):** her basic is Rs 30,000 but PF is on the **capped Rs 15,000** → 12% = **Rs 1,800**. Employer also Rs 1,800 (EPS 1,250 + EPF 550).

**ESI:** gross Rs 55,000 > Rs 21,000 → **nil** (not covered).

**PT:** Rs 55,000 > Rs 20,000 → **Rs 200**.

**TDS u/s 192 — estimate her annual tax (new regime):**

| Item | Amount (Rs) |
|---|---:|
| Gross annual (55,000 × 12) | 6,60,000 |
| Less: standard deduction | (75,000) |
| **Taxable income** | **5,85,000** |
| Tax: 0–4L nil; 4L–5.85L @ 5% = 5% × 1,85,000 | 9,250 |
| Less: Sec 87A rebate (taxable ≤ 12L → full relief) | (9,250) |
| **Annual tax** | **NIL** |

Priya's taxable income is below Rs 12L, so **87A wipes out her tax — TDS = Rs 0/month.** This is the **nil-tax case**.

**Priya's payslip:**

| Earnings | Rs | Deductions | Rs |
|---|---:|---|---:|
| Basic | 30,000 | EPF (employee) | 1,800 |
| HRA | 15,000 | PT | 200 |
| Special | 10,000 | TDS (192) | 0 |
| **Gross** | **55,000** | **Total deductions** | **2,000** |
| | | **Net pay** | **53,000** |

### Step 2 — a taxable employee (contrast)

Take a manager, **"Arjun Menon," gross Rs 1,80,000/month** (annual Rs 21,60,000):

| Item | Amount (Rs) |
|---|---:|
| Gross annual | 21,60,000 |
| Less: standard deduction | (75,000) |
| **Taxable income** | **20,85,000** |
| 0–4L nil | 0 |
| 4–8L @ 5% | 20,000 |
| 8–12L @ 10% | 40,000 |
| 12–16L @ 15% | 60,000 |
| 16–20L @ 20% | 80,000 |
| 20L–20.85L @ 25% | 21,250 |
| Tax before cess | 2,21,250 |
| Add: 4% cess | 8,850 |
| **Annual tax** | **2,30,100** |
| **Monthly TDS (÷12)** | **≈ 19,175** |

87A does **not** apply (taxable > Rs 12L). So Arjun's monthly TDS 192 is **Rs 19,175**.

### Step 3 — build the April totals

Across the 15 staff, assume the aggregate monthly statutory numbers come to:

| Head | Employee side | Employer side |
|---|---:|---:|
| EPF (on capped wages) | 21,600 | 21,600 (EPS 15,000 + EPF 6,600) |
| ESI (3 workers, gross 54,000) | 405 (0.75%) | 1,755 (3.25%) |
| PT (15 staff × 200) | 3,000 | — |
| TDS u/s 192 (only taxable staff, e.g. Arjun) | 19,175 | — |

Net salary payable = Gross 9,00,000 − EPF 21,600 − ESI 405 − PT 3,000 − TDS 19,175 = **Rs 8,55,820**.

### Step 4 — the consolidated Salary JV in TallyPrime

Path: **Gateway of Tally → Vouchers → F7 Journal** (date 30-Apr-2026).

```
Dr  Salaries & Wages (Indirect Exp)        9,00,000
Dr  Employer PF Contribution (Exp)           21,600
Dr  Employer ESI Contribution (Exp)           1,755
      Cr  EPF Payable (employee 21,600 + employer 21,600)   43,200
      Cr  ESI Payable (employee 405 + employer 1,755)        2,160
      Cr  Professional Tax Payable                           3,000
      Cr  TDS Payable (192)                                 19,175
      Cr  Salary Payable (net)                            8,55,820
```

Debits 9,23,355 = Credits 9,23,355. The employer PF/ESI are **company costs**, so they're debited to expense and credited to the same payable ledgers (which is why EPF Payable = 43,200, not 21,600).

### Step 5 — the payment entries

On **30-Apr** the bank pays net salaries (F5 Payment, HDFC Current xxxx4567):

```
Dr  Salary Payable          8,55,820
      Cr  HDFC Bank         8,55,820
```

By **15-May-2026**, clear the statutory dues (each a separate challan/ECR):

```
Dr  EPF Payable    43,200   |  Dr  ESI Payable   2,160
Dr  PT Payable      3,000   |  Dr  TDS Payable  19,175  (via ITNS 281)
      Cr  HDFC Bank  (each)
```

## The deliverable

**April 2026 Payroll summary (MIS to management):**

| Line | Amount (Rs) |
|---|---:|
| Gross payroll | 9,00,000 |
| (−) Employee EPF | 21,600 |
| (−) Employee ESI | 405 |
| (−) PT | 3,000 |
| (−) TDS 192 | 19,175 |
| **Net paid to staff** | **8,55,820** |
| Add: Employer EPF | 21,600 |
| Add: Employer ESI | 1,755 |
| **Total cost to company (April)** | **9,23,355** |

**Statutory calendar:** PF ECR + ESI challan by **15-May-2026**; PT by Telangana due date; TDS 192 deposited by **7-May-2026** (challan covered in the next chapter).

## How it's checked

- **JV balances:** debits = credits = Rs 9,23,355. Salaries expense ties to the payroll register.
- **PF ceiling:** reviewer confirms PF is on Rs 15,000 cap, not full basic — Priya's Rs 1,800 (not 12% of 30,000 = 3,600).
- **Employer 12% split** must equal EPS **Rs 1,250** + EPF **Rs 550** per member — EPFO's ECR rejects a wrong split.
- **ESI scope:** only the 3 workers ≤ Rs 21,000 are in ESI; anyone above is out. A single over-ceiling person wrongly included inflates the ESI challan.
- **TDS 192:** annual estimate ÷ 12; 87A applied only where taxable ≤ Rs 12L. Priya = nil, Arjun = Rs 19,175.
- **Bank file** total = Salary Payable Rs 8,55,820, to the rupee.

## Common mistakes & red flags

| Mistake | Consequence | Fix |
|---|---|---|
| PF on full basic (Rs 3,600 for Priya) | Over-deduction, employee complaint | Cap wage at Rs 15,000 → Rs 1,800 |
| ESI on all staff | Wrong challan, refund mess | Apply only to gross ≤ Rs 21,000 |
| Forgetting 87A → deducting TDS on Priya | Wrongful deduction, Form 16 mismatch | Rebate up to taxable Rs 12L → nil |
| Netting employer PF against employee | JV won't balance; understated cost | Employer share is extra expense + payable |
| Missing 15th PF/ESI deadline | Interest + damages; employer PF **disallowed u/s 36(1)(va)** if late | Pay employee PF by 15th, always |

**Red flag:** if an employee's PF isn't deposited by the due date, the employee's own contribution deducted from salary becomes **taxable income of the company** (36(1)(va)/2(24)(x)) with no deduction — a permanent loss, not just interest.

## On the job & in the interview

**The "why":** PF/ESI protect the worker; the wage ceilings keep the schemes targeted (PF caps the mandatory base at Rs 15,000; ESI only covers lower-wage staff ≤ Rs 21,000). PT is a state levy. TDS 192 makes the employer pre-collect the employee's income tax evenly across the year so there's no March shock.

**Jargon:** *ECR* (Electronic Challan-cum-Return, the PF monthly file), *UAN* (Universal Account Number), *ESIC IP number*, *net vs CTC* (CTC includes employer PF/ESI; net is take-home).

**Interview Q&A:**

- *"An employee earns Rs 55,000 gross — how much PF do you deduct?"* → "PF is capped at Rs 15,000 wage, so Rs 1,800 employee and Rs 1,800 employer, not 12% of full basic. ESI is nil since gross exceeds Rs 21,000."
- *"Why is Priya's TDS zero but Arjun's isn't?"* → "New regime: after Rs 75,000 standard deduction Priya's taxable is Rs 5.85L, below Rs 12L, so the Sec 87A rebate of Rs 60,000 fully offsets her Rs 9,250 tax. Arjun's taxable Rs 20.85L exceeds Rs 12L, so no rebate — his annual tax Rs 2,30,100 ÷ 12 = about Rs 19,175/month."
- *"What happens if PF is deposited late?"* → "Interest and damages, plus the employee's share becomes taxable income of the employer with no deduction under 36(1)(va) — so we never miss the 15th."
