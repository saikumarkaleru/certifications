# Financial Functions

## What it is & where it's used

Excel's financial functions turn cash-flow logic into one-line formulas. Instead of building a discounting table by hand, you write `=XNPV(...)` and get the present value of any dated cash-flow stream. These functions are the arithmetic engine behind every model that answers "is this worth doing?" or "what's the EMI?" or "what return did we actually earn?"

The core set, and the questions each answers:

| Function | Answers |
|---|---|
| `PV` / `FV` | What is a lump sum worth today / in future? |
| `NPV` / `XNPV` | What is a stream of cash flows worth today? |
| `IRR` / `XIRR` | What annual return does a cash-flow stream deliver? |
| `PMT`, `IPMT`, `PPMT` | What is the EMI, and its interest/principal split? |
| `RATE` | What interest rate is baked into a loan or deposit? |

Where it shows up on the job: **corporate finance / FP&A** (capex approvals, project NPV/IRR), **investment banking / PE / VC** (deal IRR, LBO returns), **credit & banking** (loan schedules, effective rates), **treasury** (deposit/bond valuation), **CA practice** (lease accounting under Ind AS 116, effective interest under Ind AS 109, EMI schedules for clients), and **equity research** (DCF valuation). If a role touches "return", "yield", "EMI", or "valuation", these functions are the daily bread.

## The gap: why companies want this (and college didn't teach it)

MBA and CA courses teach the *theory* of time value of money — the `1/(1+r)^n` factor, PV of annuity formulas, the definition of IRR. What they almost never teach is the **execution discipline** that separates a correct model from a plausible-looking wrong one:

- **Sign conventions.** Textbooks compute NPV with all-positive numbers and add a minus sign for the outflow "in your head". Excel forces you to be explicit: money *out* is negative, money *in* is positive. Get one sign wrong and IRR silently returns garbage or `#NUM!`.
- **`NPV` does NOT include period zero.** The single most common real-world error. Excel's `NPV()` assumes the first cash flow is one period away. The initial investment (today) must be added *outside* the function. Nobody tells you this in class.
- **Irregular dates.** Real cash flows don't arrive in tidy annual buckets. A capex outflow in April, a receipt in July, another in December — `NPV`/`IRR` (which assume equal periods) are wrong here; you need `XNPV`/`XIRR`. Colleges teach only the equal-period version.
- **The interest/principal split.** Accountants and lenders need to know how much of each EMI is interest (P&L / tax) vs principal (balance sheet). `IPMT`/`PPMT` do this instantly; most graduates build clumsy manual amortization tables and get the closing balance off by rupees.

Employers pay for the person who never ships a model with the period-zero bug and who reaches for `XIRR` without being told.

## What "proficient" looks like

A job-ready person can, unaided:

1. Value any dated cash-flow stream with `XNPV`/`XIRR` and defend the discount rate used.
2. Explain and apply the sign convention correctly on the first try.
3. Build a full loan amortization schedule with `PMT`/`IPMT`/`PPMT` where the closing balance ties to zero at the last row.
4. Know exactly why `IRR` returned `#NUM!` (no sign change, or bad guess) and fix it.
5. Reconcile `NPV` (equal periods, remembering to add CF0 outside) vs `XNPV` (actual dates) and say which is appropriate.
6. Back out an implied rate with `RATE` (e.g., the effective interest rate on a "no-cost EMI" that isn't).

## Hands-on: how to actually do it

### Sign convention (memorise this)
> **Cash OUT of your pocket = negative. Cash IN = positive.**

Every function below obeys it. A loan you *take* is `+` (cash in); the EMIs you *pay* are `−`. A deposit you *make* is `−`; the maturity you *receive* is `+`.

### PV and FV

```
=FV(rate, nper, pmt, [pv], [type])
=PV(rate, nper, pmt, [fv], [type])
```
`type` = 0 (default) end-of-period, 1 = beginning.

```excel
' ₹1,00,000 today, 8% p.a., 5 years — future value
=FV(8%, 5, 0, -100000)            ' → 146,932.81

' Deposit ₹10,000 at end of every year, 7%, 10 yrs
=FV(7%, 10, -10000)               ' → 138,164.48  (annuity FV)

' What lump sum today grows to ₹5,00,000 in 6 yrs at 9%?
=PV(9%, 6, 0, -500000)            ' → 298,144.66
```

### NPV vs XNPV — the period-zero trap

`NPV(rate, value1, value2, …)` discounts value1 by **one** period. So put CF0 (today's outflow) **outside**:

```excel
' Rate 12%. CF0=-500000 today; then 150k,180k,200k,220k at years 1-4
=NPV(12%, 150000,180000,200000,220000) + (-500000)
' → 51,894.63   (positive ⇒ accept)
```

`XNPV`/`XIRR` take a rate, a values range, and a **dates** range. CF0's date is the anchor (discount factor 1), so CF0 goes *inside* here:

```excel
' A2:A5 = dates, B2:B5 = cash flows
' A2 2026-04-01  B2 -500000
' A3 2026-08-15  B3  200000
' A4 2027-01-10  B4  250000
' A5 2027-06-30  B5  180000
=XNPV(12%, B2:B5, A2:A5)          ' → ~86,000 (actual/365 day-count)
```

### IRR vs XIRR

```excel
=IRR(values, [guess])             ' equal periods, values must include CF0
=XIRR(values, dates, [guess])     ' actual dates — use this in real work
```

```excel
' C2:C6 = -500000,150000,180000,200000,220000  (year 0..4)
=IRR(C2:C6)                       ' → 16.4%
=XIRR(B2:B5, A2:A5)               ' dated version, → ~19% for above stream
```
Rule: IRR needs **at least one sign change** in the stream or it errors. Add a `guess` (e.g. 0.1) if it returns `#NUM!` on unusual cash flows.

### PMT / IPMT / PPMT (loan EMI + split)

```
=PMT(rate_per_period, nper, pv, [fv], [type])
=IPMT(rate, per, nper, pv)        ' interest portion of payment #per
=PPMT(rate, per, nper, pv)        ' principal portion of payment #per
```

```excel
' ₹20,00,000 home loan, 9% p.a., 20 years (monthly)
=PMT(9%/12, 20*12, 2000000)       ' → -17,995.32  (EMI, negative = you pay)

' Interest inside EMI #1 and #12
=IPMT(9%/12, 1, 240, 2000000)     ' → -15,000.00
=PPMT(9%/12, 1, 240, 2000000)     ' →  -2,995.32
' IPMT + PPMT = PMT for every period
```

### RATE (back out the hidden rate)

```
=RATE(nper, pmt, pv, [fv], [type], [guess]) * 12   ' ×12 → annual for monthly
```

```excel
' "No-cost" phone: ₹60,000 price, pay ₹5,400/mo for 12 mo
=RATE(12, -5400, 60000)*12        ' → ~15.9% p.a. real cost
```

## Worked example / mini-project

**Capex decision + loan funding, India context.** A manufacturer evaluates a ₹50,00,000 machine that generates net cash inflows over 5 years, funded partly by a bank loan. Reproduce this in a blank sheet.

**Part A — Project viability (XIRR/XNPV):**

| Date | Cash flow (₹) |
|---|---|
| 01-Apr-2026 | -50,00,000 |
| 31-Mar-2027 | 12,00,000 |
| 31-Mar-2028 | 15,00,000 |
| 31-Mar-2029 | 16,00,000 |
| 31-Mar-2030 | 14,00,000 |
| 31-Mar-2031 | 13,00,000 |

```excel
' dates in A2:A7, cash flows in B2:B7, hurdle rate 13% in D1
=XNPV(D1, B2:B7, A2:A7)   ' → ₹2,42,000 approx  (>0 ⇒ accept)
=XIRR(B2:B7, A2:A7)       ' → ~14.9%  (> 13% hurdle ⇒ accept)
```
Both signals agree: NPV positive and IRR above the hurdle. Proceed.

**Part B — Amortization schedule for the ₹30,00,000 loan** (10% p.a., 5 yrs, monthly). Build columns and drag down 60 rows:

| Col | Header | Formula (row for period n, n in A) |
|---|---|---|
| A | Period | 1,2,3… |
| B | Opening | `=B_prev_closing` (row1 = 3000000) |
| C | EMI | `=PMT(10%/12,60,3000000)` (fixed) |
| D | Interest | `=IPMT(10%/12,A2,60,3000000)` |
| E | Principal | `=PPMT(10%/12,A2,60,3000000)` |
| F | Closing | `=B2+E2` |

EMI = **-63,741** per month. In row 60, Closing must read **0.00** (a few paise of rounding is normal — pros round the final principal to force it to zero). Total interest paid = `=SUM(D2:D61)` ≈ ₹8,24,000. This is the number the accountant books to the P&L and the borrower sees as the true cost of the loan.

## How it's tested

**Interview questions:**
- "What's the difference between NPV and XNPV?" (Equal periods vs actual dates; and NPV excludes period zero.)
- "Why did your IRR come back as an error?" (No sign change / bad guess.)
- "A project has two IRRs — how?" (Non-conventional cash flows with multiple sign changes; use NPV or MIRR instead.)
- "IRR says 20%, NPV says reject at a 25% hurdle — which do you trust and why?" (NPV; IRR assumes reinvestment at IRR.)

**Practical / timed tests companies give:**
1. **The 20-minute Excel screen:** given a raw cash-flow table with dates, compute NPV, XNPV, IRR, XIRR and recommend go/no-go. The trap is baked in — they hand you a stream where naive `NPV()` double-counts or omits CF0.
2. **Build an amortization schedule** for a given loan and report total interest and the balance at month 24. Tests `PMT`/`IPMT`/`PPMT` and whether your closing ties to zero.
3. **"No-cost EMI" reverse-engineer:** given the sticker price and EMI, find the true annual rate with `RATE`. Tests sign discipline.

## Common mistakes & how pros avoid them

| Mistake | Fix |
|---|---|
| Putting CF0 *inside* `NPV()` | Add CF0 **outside**: `=NPV(r, CF1:CFn) + CF0` |
| Mixing signs wrongly → `#NUM!` in IRR | Outflows negative, inflows positive; ensure ≥1 sign change |
| Using `IRR`/`NPV` on irregular dates | Switch to `XIRR`/`XNPV` |
| Annual rate in a monthly `PMT` | Always divide: `rate/12`, and `years*12` for nper |
| Forgetting `RATE` returns *per-period* | Multiply by 12 for annual |
| Trusting IRR alone on weird cash flows | Cross-check with NPV; use MIRR for multiple sign changes |
| Closing balance not tying to zero | Use `PPMT` (not manual subtraction); round last principal |
| `XIRR` on a stream with no CF0 or no sign change | Include the initial outflow with its date |

Pros also **label the discount rate in a named cell** and reference it, never hard-code it inside the formula — so a reviewer can flex the assumption instantly.

## Learn-it roadmap & resources

**Time to proficiency:** 1-2 focused days to fluency on all nine functions; 1 week to reliably ace a timed test including a clean amortization build.

- **Day 1:** PV/FV, then NPV vs XNPV (drill the period-zero trap 5×). 
- **Day 2:** IRR/XIRR sign discipline + build one full amortization schedule from scratch with `PMT`/`IPMT`/`PPMT`, then `RATE` reverse-engineering.

Resources:
- **Free:** Microsoft's function docs (`support.microsoft.com`), Corporate Finance Institute free Excel lessons, ICAI FM/SM study material (Indian context, EMI and capital budgeting).
- **Paid / certification:** CFI's FMVA (financial modeling), Wall Street Prep, Coursera "Finance & Quantitative Modeling". For CA aspirants, the FM paper and Ind AS 116/109 practical questions directly exercise these functions.
- **Practice:** rebuild any real home/car loan statement in Excel and match the bank's EMI to the paisa — the fastest confidence builder.

## Quick-reference

```excel
=PV(rate, nper, pmt, [fv], [type])          ' present value
=FV(rate, nper, pmt, [pv], [type])          ' future value
=NPV(rate, cf1, cf2, …) + cf0               ' NPV — cf0 OUTSIDE!
=XNPV(rate, values, dates)                  ' dated NPV — cf0 inside
=IRR(values_incl_cf0, [guess])              ' equal-period IRR
=XIRR(values, dates, [guess])               ' dated IRR (use in real work)
=PMT(rate, nper, pv, [fv], [type])          ' EMI / instalment
=IPMT(rate, per, nper, pv)                   ' interest part of payment #per
=PPMT(rate, per, nper, pv)                   ' principal part of payment #per
=RATE(nper, pmt, pv, [fv], [type]) * 12     ' back out annual rate (monthly)
```

| Rule | Remember |
|---|---|
| Sign | OUT = negative, IN = positive |
| NPV | first arg is 1 period away → CF0 goes outside |
| XNPV/XIRR | need a dates range; CF0 date = anchor |
| IRR error | needs ≥1 sign change; add a `guess` |
| Monthly loan | `rate/12`, `years*12`, `RATE()*12` |
| Check | `IPMT + PPMT = PMT` every period; closing balance → 0 |
| Decision | NPV > 0 **and** IRR > hurdle rate ⇒ accept |
