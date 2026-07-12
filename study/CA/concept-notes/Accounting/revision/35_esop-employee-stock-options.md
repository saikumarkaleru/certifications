# Chapter 35 — Employee Stock Option Plans (ESOP)

## Snapshot
ESOP = right granted to employees to buy shares at a concessional price later, conditional on service/performance. The cost of services paid in equity is a **real (non-cash) expense** — measured at **fair value of the option at grant date**, spread over the **vesting period**, credited to **Employee Stock Options Outstanding A/c (ESOO)**, an equity item. Governed by ICAI **Guidance Note on Accounting for Employee Share-based Payments** (fair value method) + **SEBI SBEB & Sweat Equity Regulations 2021** (listed) + **Sec 62(1)(b)**. (Ind AS entities → Ind AS 102.)

## Core concepts
- Option has value **at grant**, not just exercise (intrinsic + time value).
- Three dates: **Grant** (measure FV — NO entry) → **Vesting** (estimate becomes fact) → **Exercise** (cash in; ESOO → capital + premium).
- Counterparty test: **employees** → measure at FV of options; **non-employees/suppliers** → FV of goods/services received first.

## Key provisions / conditions & limits

### Measurement & spreading (fair value method)
- **Total expected cost = Options expected to vest × FV per option at grant.**
- **Cumulative expense to date = Total expected cost (latest estimate) × (vesting years elapsed ÷ total vesting years).**
- **Expense for year = Cumulative to date − cumulative recognised in prior years.**
- Uses **latest** estimate of number vesting → catch-up auto-corrects; **never restate prior years**. At vesting, "expected" → "actual".

### Fair value vs intrinsic value
- **Intrinsic value = max(Market price − Exercise price, 0)** (ignores time value).
- **Fair value = intrinsic + time value** (given in exam via Black-Scholes).
- GN prefers **fair value**. If intrinsic used → mandatory **pro-forma** disclosure of profit & EPS as if FV used. (Strict intrinsic method may require remeasurement each reporting date — prices given every year → remeasure.)

### The asymmetry — true-up rules (KEY)
| Condition | In FV at grant? | True-up number? | If ultimately fails |
|---|---|---|---|
| **Service** (stay employed) | No | **Yes** | Reverse cost (forfeiture) |
| **Non-market performance** (IPO, ₹X sales) | No | **Yes** | Reverse cost |
| **Market performance** (share price ≥ ₹X, TSR) | **Yes** | **No** | **Cost STAYS** — do not reverse |

Missed **market** condition → employee gets nothing but **expense remains**. Missed **non-market** → number expected → 0, **entire cost reversed**.

### Attrition arithmetic
- "**X% leave over the period**" → survivors = grant × (1 − X%), multiply once.
- "**X% per annum**" → survivors = grant × (1 − X%)ⁿ (compound). E.g. (0.95)³ = 0.857375.

### Modification / cancellation ("add, never subtract")
- Modification **increasing** FV → recognise **incremental FV** (new − old at modification date) over **remaining vesting period**, on top of original charge (unchanged).
- Modification **decreasing** FV → **ignore**; keep original charge.
- **Cancellation/settlement during vesting** → **accelerate**: recognise all remaining unamortised cost **immediately**.

## Journal entries
| Event | Entry |
|---|---|
| Grant | **No entry** |
| Each vesting year | Employee Compensation Expense A/c Dr; To ESOO Outstanding A/c |
| Year-end close | P&L A/c Dr; To Employee Compensation Expense A/c |
| Exercise | Bank A/c Dr (N × EP) + ESOO A/c Dr (N × FV); To Equity Share Capital (N × Face); To Securities Premium (**balancing figure**) |
| Forfeiture (pre-vest) | Auto via cumulative formula (may credit-reverse expense) |
| Lapse (vested, unexercised) | ESOO A/c Dr; To **General Reserve** A/c (**expense NOT reversed**) |

- On exercise, Securities Premium = employee's cash premium **+** compensation routed via ESOO.
- Optional gross presentation: set up ESOO with contra-equity **Deferred Employee Compensation Expense**, amortised over vesting — same net result; do **not** double-count.

## Worked mini-example
XYZ Ltd, 1 Apr 2023: 100 options each to 500 employees (50,000), vest after 3 yrs, FV ₹20, EP ₹60, face ₹10. Forfeiture estimates: Yr1 20% leave; Yr2 revised 25%; Yr3 actual 28% left.

| Yr | Expected to vest | Total cost @₹20 | Cumulative (×yr/3) | Prior | Expense |
|---|---|---|---|---|---|
| 1 | 40,000 | 8,00,000 | 2,66,667 | 0 | **2,66,667** |
| 2 | 37,500 | 7,50,000 | 5,00,000 | 2,66,667 | **2,33,333** |
| 3 | 36,000 (actual) | 7,20,000 | 7,20,000 | 5,00,000 | **2,20,000** |

Total = ₹7,20,000 = 36,000 vested × ₹20 ✓. Yr1 not restated.
Exercise 34,000 @ ₹60: Bank Dr 20,40,000 + ESOO Dr 6,80,000 → Share Capital 3,40,000 + Sec. Premium 23,80,000. Lapse of 2,000 vested: ESOO Dr 40,000 → General Reserve 40,000.

## Exam traps & must-remember
1. **Never true-up equity-settled cost for share-price movements** — baked into grant FV. Only forfeitures change the number.
2. Lapse after vesting → expense **stays**; move ESOO → **General Reserve** (not P&L).
3. **Graded vesting front-loads** cost (each tranche own period); not equal per year.
4. **No entry at grant** — first entry end of Year 1.
5. Cumulative method — never restate prior years.
6. Equity-settled credit = **equity (ESOO)**, never a liability. Only **cash-settled SARs** = liability.
7. Exercise split: Cash = N × **exercise** price; Share Capital = N × **face**; Sec. Premium = **balancing figure** (includes ESOO).
8. Intrinsic without disclosure → wrong; give pro-forma FV profit/EPS.
9. FV = intrinsic + time value; below-EP share → intrinsic 0 but FV positive.
10. **Market vs non-market** missed target — opposite accounting (stays vs reverses).
11. Compounding vs flat attrition — read wording.
12. Beneficial-to-company modification never cuts original cost; "add, never subtract".
13. Don't double-count under Deferred Compensation presentation.
14. Cancellation during vesting = **acceleration** (all remaining cost now).

**Equity-settled vs Cash-settled (SAR):** SAR settled in cash = share appreciation; credit = **liability**, remeasured to FV **every reporting date** until settlement; both forfeiture & price changes hit P&L. Equity-settled = measure once at grant, move only for leavers.

**Presentation/law:** ESOO under Reserves & Surplus (equity); Employee Compensation Expense under Employee Benefits in P&L; options are dilutive → **diluted EPS (AS 20)**. Sec 62(1)(b) (special resolution listed; Rule 12 ordinary resolution unlisted); **minimum 1-year grant-to-vest gap**; independent directors and >10% holders/promoters generally excluded.

## One-line recall
- Total cost = options expected to vest × FV at grant; spread over vesting via cumulative formula.
- Grant: no entry. Vesting: Dr Expense, Cr ESOO. Exercise: Dr Bank + Dr ESOO → Capital + Premium. Lapse: Dr ESOO → General Reserve (expense stands).
- True-up for **leavers** (service/non-market); **never** for share price/market.
- Equity-settled → equity credit, measure once; cash-settled SAR → liability, remeasure yearly.
- Attrition: "over period" multiply once; "per annum" compound (1−r)ⁿ.
