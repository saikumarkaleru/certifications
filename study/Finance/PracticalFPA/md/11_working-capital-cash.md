# Working-capital & cash-flow management

## What it is & where it's used

Working capital is the money trapped inside the operating engine of a business: cash tied up in **receivables** (customers who owe you), **inventory** (stock sitting in a warehouse), minus the free financing you get from **payables** (suppliers you haven't paid yet). Manage it well and you release crores of cash without raising a single rupee of debt. Manage it badly and a profitable company runs out of cash and dies — the classic "profitable but insolvent" trap.

The **cash-conversion cycle (CCC)** measures how many days a rupee stays trapped: `CCC = DIO + DSO − DPO`. The **13-week cash-flow forecast** is the tactical instrument treasurers and CFOs live by — a rolling week-by-week view of every rupee coming in and going out for the next quarter.

Roles that pay for this skill:
- **FP&A / Treasury analyst** — builds and owns the 13-week model, flags cash crunches.
- **Credit control / AR analyst** — attacks DSO, chases overdue invoices.
- **Corporate finance / CFO office** — negotiates supplier terms (DPO), decides on invoice discounting or a cash-credit limit.
- **Financial controllers** — reconcile the forecast to the actual bank balance every Monday.

## The gap: why companies want this (and college didn't teach it)

College teaches you that "working capital = current assets − current liabilities" and moves on. Nobody shows you that this single ratio hides three independent levers, each owned by a different department, each negotiable, each worth real cash. Your MBA taught you accrual accounting — revenue when earned, expense when incurred. But cash doesn't move on accruals. A ₹1 crore sale booked in March that gets collected in July does nothing for June's payroll.

Employers pay because the gap is *cash timing*, not profit. A founder can read a P&L. What they can't do is answer "will we make payroll in week 6?" — and that answer requires a bottoms-up 13-week model that no textbook builds. This is the skill that gets a 26-year-old into the room where the CFO decides whether to draw down the working-capital loan.

## What "proficient" looks like

A job-ready person can, unaided:

1. Compute DSO, DPO, DIO and the CCC from a trial balance or Tally export, and explain what each day is worth in rupees.
2. Build a rolling 13-week cash-flow forecast in Excel from AR/AP ageing, payroll, GST, and loan schedules — with a live bank-balance line that flags any week going negative.
3. Run a **collections waterfall**: take an AR ageing and predict when each bucket actually converts to cash based on historical collection %.
4. Recommend a concrete lever — "cut DSO by 8 days via 2/10 net-45 terms, releases ₹1.4 cr" — with the number to back it.
5. Reconcile last week's forecast to the actual bank statement and explain the variance (a "cash bridge").

## Hands-on: how to actually do it

### The three ratios (Excel)

Assume an annual model. Put revenue, COGS, and closing balances on a sheet:

```
DSO  = Accounts Receivable / Revenue        * 365
DPO  = Accounts Payable    / COGS (or Purchases) * 365
DIO  = Inventory           / COGS             * 365
CCC  = DIO + DSO - DPO
```

Excel, with cells named:
```excel
=(_AR/_Revenue)*365          ' DSO
=(_AP/_COGS)*365             ' DPO
=(_Inventory/_COGS)*365      ' DIO
=DIO+DSO-DPO                 ' CCC
```

**Rupee value of one DSO day** = `Revenue / 365`. If revenue is ₹120 cr, one day of DSO = ₹32.9 lakh of cash. Cut DSO by 10 days → release **₹3.29 cr**.

### Collections waterfall from an AR ageing (Excel)

Historical collection profile: of a month's sales, 40% collects in the current month, 35% at 30 days, 20% at 60 days, 5% at 90. Lay sales across rows, apply the profile with a shifted `SUMPRODUCT`:

```excel
=SUMPRODUCT($B2:$B13, INDEX($Profile,ROW()-...))  ' shift each cohort by its lag
```
Simpler, most analysts use a diagonal drag of `=Sales_MonthN * Collect%_bucket` and sum each week's column.

### DSO/DPO/DIO levers — what to actually pull

| Lever | Tactic | Cash effect |
|---|---|---|
| **DSO ↓** | 2/10 net-30 early-pay discount; auto-reminders at day −3, 0, +7; stop-supply at 60 dpd; invoice same-day not month-end | Pulls cash forward |
| **DPO ↑** | Renegotiate supplier terms 30→45; pay on due date not early; use dynamic discounting only if return beats your cost of capital | Pushes cash back |
| **DIO ↓** | ABC analysis, cut slow-movers, JIT on A-items, consignment stock | Frees inventory cash |

### Pulling the numbers from Tally

Ratios need AR, AP, Inventory, Revenue, COGS. In TallyPrime:
- **AR ageing**: `Gateway of Tally → Display More Reports → Statements of Accounts → Ageing Analysis → Ledger` (or `Bills Receivable → F6: Ageing`). Set ageing periods 0-30 / 31-60 / 61-90 / 90+.
- **AP ageing**: same path, `Bills Payable`.
- **Closing stock**: `Stock Summary`. Revenue/COGS: `Profit & Loss A/C`.
- Export each with `Alt+E → Excel (Spreadsheet)` and pull into the model.

### The 13-week forecast — Python skeleton

When AR/AP ageings are large, a Python roll is faster than dragging Excel:

```python
import pandas as pd, numpy as np

weeks = pd.date_range("2026-07-06", periods=13, freq="W-MON")
cf = pd.DataFrame(index=weeks)

# Inflows
cf["collections"]   = [1.20,0.95,1.40,1.10,0.80,1.05,1.30,0.90,1.15,1.00,1.25,0.85,1.10]  # cr
cf["other_inflow"]  = 0.0

# Outflows (negative)
cf["payables"]      = [-0.70,-0.55,-0.90,-0.60,-0.75,-0.50,-0.80,-0.65,-0.70,-0.60,-0.85,-0.55,-0.70]
cf["payroll"]       = np.where(cf.index.day <= 7, -0.45, 0.0)   # 1st-of-month payroll
cf["gst_tds"]       = np.where(cf.index.day.isin(range(18,26)), -0.35, 0.0)  # 20th GST
cf["loan_emi"]      = -0.12
cf["capex"]         = 0.0

cf["net"]        = cf.drop(columns=[]).sum(axis=1)
opening          = 0.60   # cr, this Monday's bank balance
cf["closing"]    = opening + cf["net"].cumsum()
print(cf[["collections","payables","payroll","gst_tds","net","closing"]].round(2))

crunch = cf[cf["closing"] < 0]
if not crunch.empty:
    print("CASH CRUNCH in week(s):", list(crunch.index.date))
```

### Cash-flow classification (accounting anchor)

The 13-week model is *direct-method* operating cash. Contrast with AS-3 / Ind AS 7 indirect method used in statutory accounts:

| Activity | Examples |
|---|---|
| Operating | Collections, supplier payments, payroll, GST, TDS |
| Investing | Capex, asset sale, investments |
| Financing | Loan drawdown/EMI, equity, dividend |

### Journal entries behind the levers

Recording an early-payment discount **given** to a customer (2/10 net-30, ₹1,00,000 invoice, they pay in 10 days):

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| Bank | 98,000 | |
| Discount Allowed | 2,000 | |
| To Debtors (Customer A) | | 1,00,000 |

Discount **received** by taking a supplier's early-pay offer:

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| Creditors (Supplier B) | 50,000 | |
| To Bank | | 49,000 |
| To Discount Received | | 1,000 |

## Worked example / mini-project

**Prakash Fabricators Pvt Ltd**, FY26. Revenue ₹120 cr, COGS ₹90 cr. Closing AR ₹22 cr, Inventory ₹15 cr, AP ₹11 cr.

```
DSO = 22/120 * 365 = 66.9 days
DIO = 15/90  * 365 = 60.8 days
DPO = 11/90  * 365 = 44.6 days
CCC = 60.8 + 66.9 - 44.6 = 83.1 days
```

83 days of operating cash is locked up. **One DSO day = ₹120cr/365 = ₹32.9 lakh.**

**The ask:** the CFO wants to fund a ₹6 cr machine from internal cash, no new loan. Target the levers:

| Lever | Move | Days | Cash released |
|---|---|---|---|
| DSO | 67 → 55 (credit control + 2/10 terms) | −12 | 12 × 0.329 = ₹3.95 cr |
| DIO | 61 → 52 (ABC + cut slow SKUs) | −9 | 9 × (90cr/365) = ₹2.22 cr |
| DPO | 45 → 52 (renegotiate top 5 vendors) | +7 | 7 × (90cr/365) = ₹1.73 cr |

Total released ≈ **₹7.9 cr** — machine funded, CCC drops from 83 to **55 days**.

**13-week check.** Feed the new (faster) collections profile into the Python model above. Week 5 previously dipped to −₹0.15 cr (a crunch) because of clustered GST + payroll. After pulling DSO forward, week-5 closing goes to +₹0.42 cr — the crunch disappears without drawing the cash-credit limit. That single chart — closing balance line staying above zero for 13 weeks — is the deliverable a CFO signs off on.

## How it's tested

**Interview questions**
- "A company is profitable but keeps running out of cash. Walk me through why." (Answer: CCC too long — cash trapped in AR/inventory; growth funds working capital.)
- "What's the difference between the direct and indirect cash-flow method?"
- "DSO went from 45 to 60 days QoQ. Give me three causes and how you'd investigate." (Deteriorating collections, a few large late accounts, revenue-recognition timing, channel-mix shift to slow payers.)
- "How would you build a 13-week cash forecast from scratch? What are your inputs?"
- "One DSO day — how much cash is that for a ₹500 cr revenue company?" (≈₹1.37 cr.)

**Practical / assessment tests**
- **Timed Excel case (45–60 min):** given an AR ageing + AP ageing + payroll and GST schedule, build a 13-week forecast with a flagged negative-week and a one-paragraph recommendation.
- **Ratio drill:** from a trial balance, compute DSO/DPO/DIO/CCC and the rupee value of a 10-day DSO cut.
- **Collections-waterfall test:** apply a historical collection % profile to a sales forecast to project weekly cash inflow.
- **Variance / bridge:** reconcile last week's forecast to the actual bank statement, explain the gap.

## Common mistakes & how pros avoid them

- **Forecasting on invoice date, not collection date.** A ₹50 lakh March invoice is *not* March cash. Pros apply a collection lag profile.
- **Using annual DPO/DSO on a weekly model.** Ratios are diagnostic; the 13-week model needs actual dated line items (specific EMIs, the 20th GST payment, the 7th payroll).
- **Forgetting GST/TDS timing.** GST is due by the 20th, TDS by the 7th. These are large, clustered, non-negotiable outflows that cause the classic mid-month crunch.
- **Chasing DPO by simply paying suppliers late.** That destroys supplier relationships and forfeits discounts. Pros *negotiate* longer terms and only stretch to the agreed due date.
- **No rolling refresh.** A forecast built once and never updated is dead in a week. Roll it every Monday: drop the past week, add week 14, re-anchor opening cash to the actual bank balance.
- **Confusing profit with cash.** Depreciation, accruals, and prepaid items break the link. The 13-week model ignores accruals entirely — it's pure cash in/out.
- **Not reconciling to the bank.** If your model's opening balance doesn't tie to the bank statement to the rupee, nobody trusts the closing line.

## Learn-it roadmap & resources

**Time to proficiency:** ~4–6 weeks part-time if you already know Excel and basic accounting. Week 1: ratios + CCC. Weeks 2–3: build one real 13-week model end-to-end. Week 4: collections waterfall + variance bridge. Weeks 5–6: automate the roll in Python/Power Query.

| Resource | Type | Focus |
|---|---|---|
| CFI "Cash Flow Forecasting" course | Paid | 13-week model, treasury view |
| Wall Street Prep / Breaking Into Wall Street WC modeling | Paid | Working-capital schedule in a 3-statement model |
| ICAI FM study material (working-capital management) | Free | India-context, exam rigour |
| ACCA / CIMA treasury notes | Free/Paid | Globally-portable practice |
| CTP (Certified Treasury Professional, AFP) | Cert | Treasury/cash-management gold standard |
| Excel `SUMPRODUCT`, `EOMONTH`, `WORKDAY` mastery | Free | The engine of every model |

Build a real one for a friend's business or from a public annual report — that single artifact beats any certificate in an interview.

## Quick-reference

```
DSO = AR / Revenue      * 365     One DSO day = Revenue / 365
DPO = AP / COGS         * 365     One DIO/DPO day = COGS / 365
DIO = Inventory / COGS  * 365
CCC = DIO + DSO - DPO             Lower = better
```

| Lever | Direction | Effect on cash |
|---|---|---|
| DSO | ↓ | Releases cash (collect faster) |
| DPO | ↑ | Releases cash (pay later) |
| DIO | ↓ | Releases cash (less stock) |

**13-week model checklist:** opening bank = actual balance · collections on *collection* date · payables on due date · payroll (7th) · GST (20th) · TDS (7th) · loan EMIs · capex · closing = opening + Σnet · flag any week < 0 · roll every Monday · reconcile to bank.

**India timing anchors:** GST payment by 20th · TDS deposit by 7th · Advance tax 15 Jun/Sep/Dec/Mar · typical B2B terms 30–90 days.
