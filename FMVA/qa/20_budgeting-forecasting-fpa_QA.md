# Q&A — Budgeting, Forecasting and FP&A

Practice bank for Chapter 20. Work each question before reading the answer. The chapter's engine is one loop — *set a frozen budget, track actuals, keep a live forecast, and explain every gap with additive, reconciling causes*. Every build is reproducible cell-for-cell in Excel, with arithmetic shown so each answer self-checks.

---

## Section A — Concept Checks (test the WHY)

**A1. In one sentence each, what question does the budget answer versus the forecast, and why must one stay frozen while the other moves?**

The **budget** answers *"what did we commit to, and are we accountable to it?"* — so it must stay frozen to remain a fair scorecard. The **forecast** answers *"where will we actually land?"* — so it must move to stay useful. Let the budget drift and you can no longer measure performance against a promise; refuse to update the forecast and you steer using numbers you know are wrong. You keep both *because* they conflict.

**A2. Why is FP&A a fundamentally different discipline from deal modeling, even though the Excel skills overlap?**

A deal model prices a business *once*, from the outside, then gets thrown at a decision. An FP&A model never "closes" — a controller updates it every month for the life of the company. So FP&A prizes *maintainability* (someone else runs it next month) over cleverness, its cadence is monthly not one-shot, and its audience is internal management. Treating an FP&A model like a deal model — over-clever formulas only you understand — is a liability, not a flex.

**A3. Why build revenue from drivers (units × price) instead of typing a growth percentage?**

Because financial outcomes are downstream of physical reality: revenue *is* quantity sold times price. Driver-level assumptions are things a business owner can debate and control ("can we really raise price 3%?") rather than an abstract percentage nobody owns. It also localizes error — when you miss, you know *which* driver was wrong — and makes the plan re-forecastable: swap the new unit assumption and the plan re-flows.

**A4. Why is variance decomposition (price + volume + mix) guaranteed to reconcile to the total, and why is that both the power and the self-check?**

The three effects are mutually exclusive and collectively exhaustive — each isolates one thing changing while holding the others at a fixed reference. Built correctly they *must* sum to the total variance. That is the analytical power (a scary aggregate becomes three named causes) and the proof of correctness at once: if the bridge doesn't tie to the total, the bridge is wrong, not reality.

**A5. Why does a rolling forecast beat the "annual lock"?**

A fixed annual plan has a decaying information horizon — in December you see 12 months ahead; by November only 1. A rolling forecast always re-extends to a constant horizon (say the next 12–18 months), so management always has the same-quality forward view and is never coasting on the stale tail of last year's plan. The cost is analyst effort (you re-forecast every month); the payoff is a plan that never goes stale.

**A6. A company is profitable every single month yet runs out of cash. How is that possible, and which artifact reveals it?**

Profit is an opinion; cash is a fact. Rising revenue inflates receivables and inventory faster than profit generates cash — you fund growth before you collect on it, so the P&L looks fine while the bank balance craters. Only a **cash-flow forecast that models working-capital timing** reveals the "growing broke" trap; the income statement structurally cannot.

**A7. AR, Inventory, and AP all use a "days" ratio — why is the base different for AR than for the other two?**

Accounts receivable is what customers owe you, so it scales off **revenue** (`Rev/days × DSO`). Inventory and payables are cost-side — goods you hold, suppliers you owe — so both scale off **COGS** (`COGS/days × DIO` and `× DPO`). Running Inventory or AP off revenue inflates them by the whole gross margin and corrupts every downstream cash number.

**A8. What is the sign convention for changes in working capital, and why does one wrong sign matter so much?**

An **increase in AR or Inventory uses cash** (negative in the cash build); an **increase in AP provides cash** (positive). Getting one sign backward doesn't just shrink a number — it can flip a cash crunch into an apparent surplus, reversing the decision the forecast should drive.

---

## Section B — Build / Computational Problems

Reproduce each in Excel; arithmetic is shown so it self-checks.

**B1. Single-product price/volume variance.** Budget: 10,000 units at ₹50. Actual: 11,000 units at ₹48. Decompose the revenue variance.

Budget revenue = 10,000 × 50 = 500,000. Actual = 11,000 × 48 = 528,000. **Total variance = +28,000 F.**

- **Volume variance** = (Act Q − Bud Q) × **Bud Price** = (11,000 − 10,000) × 50 = **+50,000 F**
- **Price variance** = (Act P − Bud P) × **Act Q** = (48 − 50) × 11,000 = **−22,000 U**

Check: 50,000 − 22,000 = **+28,000** ✓ ties to total. We beat on volume, lost on price — the "+28k, great" headline hid a margin story.

**B2. Two-product volume/mix split (prices held at budget).**

| Product | Bud Q | Bud P | Act Q | Act P |
|---|---:|---:|---:|---:|
| Standard | 8,000 | 40 | 7,000 | 40 |
| Premium | 2,000 | 100 | 5,000 | 100 |
| **Total** | **10,000** | | **12,000** | |

Budget revenue = 8,000×40 + 2,000×100 = 320,000 + 200,000 = **520,000**. Actual = 7,000×40 + 5,000×100 = 280,000 + 500,000 = **780,000**. **Total variance = +260,000 F** (price variance = 0 since prices held).

Budget mix: Standard 80%, Premium 20%. Total actual units 12,000, so at-budget-mix = Standard 9,600, Premium 2,400.

**Pure volume effect** = (at-budget-mix Q − Bud Q) × Bud Price:
- Standard: (9,600 − 8,000) × 40 = +64,000
- Premium: (2,400 − 2,000) × 100 = +40,000 → **Volume = +104,000 F**

**Mix effect** = (Act Q − at-budget-mix Q) × Bud Price:
- Standard: (7,000 − 9,600) × 40 = −104,000
- Premium: (5,000 − 2,400) × 100 = +260,000 → **Mix = +156,000 F**

Check: 104,000 + 156,000 = **+260,000** ✓. *Reading:* growth was only partly about selling more (+104k); the bigger driver was customers trading up to Premium (+156k) — invisible without the split.

**B3. Full three-effect bridge (price moves too).** Same two products, but Standard actual price is ₹38 (not 40) and Premium actual price is ₹105 (not 100). Units unchanged from B2. Build price + volume + mix = total.

Actual revenue = 7,000×38 + 5,000×105 = 266,000 + 525,000 = **791,000**. Budget still 520,000. **Total variance = +271,000 F.**

- **Price variance** = Σ (Act P − Bud P) × Act Q = (38−40)×7,000 + (105−100)×5,000 = −14,000 + 25,000 = **+11,000 F**
- **Volume + Mix** (at budget prices, from B2) = +104,000 + 156,000 = **+260,000 F**

Check: 11,000 + 104,000 + 156,000 = **+271,000** ✓ ties. The volume and mix legs are unchanged from B2 because they are computed at *budget* prices by construction — proving the effects are cleanly separable.

**B4. Working-capital balances from days ratios.** Assume 30-day months. Revenue Jan/Feb/Mar = 300,000 / 360,000 / 300,000; COGS = 180,000 / 216,000 / 180,000. DSO 45, DIO 30, DPO 30.

- AR = Rev/30 × 45 → 300k/30×45 = **450,000**; 360k/30×45 = **540,000**; 300k/30×45 = **450,000**
- Inventory = COGS/30 × 30 → **180,000 / 216,000 / 180,000**
- AP = COGS/30 × 30 → **180,000 / 216,000 / 180,000**

AR exceeds revenue because 45 days > one 30-day month; Inventory and AP equal COGS because 30 days = one month.

**B5. Indirect monthly cash build.** Opening AR 400,000, Inventory 180,000, AP 180,000, cash 50,000. D&A 10,000/month, no capex or debt. Net income Jan/Feb/Mar = 30,000 / 40,000 / 30,000. Use the B4 balances.

Cash from ops = NI + D&A − ΔAR − ΔInv + ΔAP:

| | Jan | Feb | Mar |
|---|---:|---:|---:|
| Net income | 30,000 | 40,000 | 30,000 |
| + D&A | 10,000 | 10,000 | 10,000 |
| − ΔAR | −(450−400)=−50,000 | −(540−450)=−90,000 | −(450−540)=+90,000 |
| − ΔInv | −(180−180)=0 | −(216−180)=−36,000 | −(180−216)=+36,000 |
| + ΔAP | +(180−180)=0 | +(216−180)=+36,000 | +(180−216)=−36,000 |
| **Cash from ops** | **−10,000** | **−40,000** | **+130,000** |
| Beginning cash | 50,000 | 40,000 | 0 |
| **Ending cash** | **40,000** | **0** | **130,000** |

Verify Feb: 40,000 + 10,000 − 90,000 − 36,000 + 36,000 = −40,000; 40,000 − 40,000 = **0** ✓. **Cash is tightest in February (₹0) despite positive profit every month** — the growing-broke trap. In March the working-capital swings unwind and the balance recovers to 130,000.

**B6. Revolver / minimum-cash floor.** Take B5 but impose a minimum cash floor of ₹25,000, funded by a revolver that draws `MAX(0, 25,000 − pre-revolver ending cash)` and repays when cash allows.

Pre-revolver ending cash: Jan 40,000; Feb 0; Mar 130,000.
- Jan: 40,000 ≥ 25,000 → draw 0. Ending 40,000, revolver balance 0.
- Feb: pre-revolver = 40,000 − 40,000 = 0 → draw = MAX(0, 25,000 − 0) = **25,000**. Ending cash 25,000, revolver balance 25,000.
- Mar: pre-revolver = 25,000 + 130,000 = 155,000, floor 25,000 → free cash above floor = 130,000, repay MIN(25,000, 130,000) = **25,000**. Ending cash 155,000 − 25,000 = 130,000, revolver balance 0.

Check: the floor holds every month (40k, 25k, 130k all ≥ 25k) and the revolver nets to zero over the quarter ✓.

**B7. Current-month "AF" switch.** A forecast row has actuals in row 20 (`Jan..Dec`) and estimates in row 21, with a current-month switch in `$B$1 = 7`. Write the July cell formula and state what it returns.

`=IF(MonthNum <= $B$1, Actual, Forecast)` → for July, MonthNum = 7 ≤ 7 → returns the **actual**. August (8 > 7) returns the **forecast**. So the AF row shows actuals Jan–Jul and estimates Aug–Dec, and rolls forward with one keystroke when `$B$1` becomes 8.

**B8. Cash conversion cycle and a DSO improvement.** Using B4's ratios (DSO 45, DIO 30, DPO 30) at the Feb revenue of 360,000, compute the cash conversion cycle and the one-off cash freed by cutting DSO to 30.

CCC = DSO + DIO − DPO = 45 + 30 − 30 = **45 days**. AR at DSO 45 = 360,000/30×45 = 540,000; at DSO 30 = 360,000/30×30 = 360,000. Cash freed = 540,000 − 360,000 = **+180,000** (a one-time working-capital release as AR falls). The CCC would drop to 30 days — 15 fewer days of operations to self-fund.

---

## Section C — Interview-Style Questions (model answers)

**C1. "Walk me through the difference between a budget, a forecast, and actuals."**

Actuals are what really happened, from the general ledger once a month closes. The budget is the approved plan set once at the start of the year — a frozen commitment and scorecard. The forecast is our current best estimate of where the year will land; it updates monthly, typically as a hybrid "Actual + Forecast" view: actuals for closed months, estimates for open ones. The loop is: set the budget, post actuals, run variance analysis against budget, re-forecast the rest of the year, explain the gaps, and feed the lessons into next year's budget.

**C2. "Our revenue came in 8% below budget. How would you investigate?"**

I'd decompose the miss into additive causes rather than treat it as one number. First, price versus volume: fewer units, or the same units at a lower realized price? Volume variance is the unit gap at budget price; price variance is the price gap at actual units. With multiple products I'd add a mix effect — an aggregate volume drop can hide a shift toward cheaper products. I'd build the bridge with a reconciliation row that ties price + volume + mix to the full 8%. That converts "we missed by 8%" into a specific to-do list — "volume held but mix shifted to low-margin SKUs" points at a completely different fix than "we discounted to hit numbers."

**C3. "How do you forecast the cash-flow statement, and why does it matter if the P&L already looks healthy?"**

I use the indirect method: start from forecast net income, add back non-cash D&A, adjust for changes in working capital, subtract capex, and add or subtract financing — which ties to the balance sheet. It matters because profit and cash diverge on *timing*. A growing, profitable company can still hit zero cash: rising revenue inflates receivables and inventory, so you fund the growth before you collect it. The P&L never shows that; only a cash forecast modeling DSO, DIO, and DPO does. I'd add a minimum-cash floor and a revolver that auto-draws below it, so the model flags a breach *before* it happens.

**C4. "What is a rolling forecast and when would you recommend one?"**

A rolling forecast maintains a constant future horizon — say 12 or 18 months. Each time a month closes you drop the oldest period and add a new one at the far end, re-estimating the middle. I'd recommend it whenever the environment moves fast enough that a December-set budget becomes fiction by mid-year — the "annual lock" problem. The trade-off is effort: you re-forecast every month. Many companies run both — a frozen budget for accountability and a rolling forecast for steering.

**C5. "Top-down or bottom-up budgeting — which is right?"**

Neither alone. Top-down sets an ambitious leadership target (grow EBIT 15%) but can be disconnected from operating reality; bottom-up builds credible department plans but tends to sandbag — low revenue, padded cost — to guarantee a beat. The right process reconciles them: leadership sets the target, departments build from drivers, and FP&A brokers the gap through iteration, challenging drivers rather than just consolidating. Driver-based budgeting is the practical middle path — more rigorous than last-year-plus incrementalism, far cheaper than full zero-based budgeting every year.

---

## Section D — Common-Error Spotting

Each item shows a broken approach; find the error and give the fix.

**D1.** *An analyst computes the volume variance as `(Act Q − Bud Q) × Act Price` and the price variance as `(Act P − Bud P) × Bud Q`. The two don't sum to the total variance.*

**Error:** the reference bases are swapped, so the interaction ("cross") term is double-counted or dropped. **Fix:** by convention, volume uses **budget price** and price uses **actual units** — `(Act Q − Bud Q) × Bud P` and `(Act P − Bud P) × Act Q`. That folds the interaction cleanly into the price line and guarantees the two sum to the total.

**D2.** *To make the "bear case" plan, an analyst edits the December budget down by 10% so it "matches" the weak start to the year.*

**Error:** editing the budget mid-year destroys accountability — you can no longer measure performance against the original promise. **Fix:** freeze the budget (paste-special as values or protect it) and move the *forecast* instead. Keep the original budget column untouched alongside so you can always show Forecast vs Budget.

**D3.** *A cash model computes `Inventory = Revenue/365 × DIO` and `AP = Revenue/365 × DPO`.*

**Error:** wrong base. Inventory and payables are cost-side and must run off **COGS** — using revenue inflates them by the entire gross margin. **Fix:** `Inventory = COGS/365 × DIO`, `AP = COGS/365 × DPO`. Only AR runs off revenue.

**D4.** *In the cash build, an analyst adds ΔAR and subtracts ΔAP: `Cash = NI + D&A + ΔAR − ΔInv − ΔAP`.*

**Error:** the working-capital signs on AR and AP are backwards. An increase in AR is cash you *haven't collected* (a use), and an increase in AP is cash you're *holding onto* (a source). **Fix:** `Cash from ops = NI + D&A − ΔAR − ΔInv + ΔAP`. A flipped sign here can turn a cash crunch into a phantom surplus.

**D5.** *A model forecasts a healthy, rising net income all year and reports "cash is fine — we're profitable," with no working-capital schedule.*

**Error:** modeling profit but not cash *timing*. Growth ties up cash in receivables and inventory ahead of collection; a profitable P&L can still breach minimum cash. **Fix:** model ΔAR, ΔInv, ΔAP explicitly, chain beginning-to-ending cash, add a minimum-cash trigger.

**D6.** *A revenue line is hard-coded as `=1,200,000` for each month. When leadership asks "what if units are 5% lower," the analyst has to retype every cell.*

**Error:** hard-coding over drivers — the plan can't be re-forecast or explained. **Fix:** build `Revenue = Units × Price` with units in a labeled input row, so one driver change re-flows the whole plan and you can attribute the outcome ("units rose 5%, price held").

**D7.** *A variance bridge shows price −22,000 and volume +50,000 and stops there, with no total row.*

**Error:** no reconciliation. Without a tie-out you can't prove the decomposition is complete — you may have dropped mix or an interaction term. **Fix:** always add a check row: `Price + Volume + Mix = Total variance`. If it doesn't tie, the bridge is wrong, not reality.

**D8.** *A rolling forecast's date headers are typed manually, so when the month rolls the analyst edits twelve labels by hand and one is wrong.*

**Error:** manual, error-prone headers defeat the point of a *rolling* build. **Fix:** key the columns off the current-month switch with `=EDATE($CurrentMonth, ColumnOffset)` so headers regenerate automatically and stay consistent every roll.

---

*Self-check of the reconciling builds: B1 50,000 − 22,000 = 28,000 ✓ · B2 104,000 + 156,000 = 260,000 ✓ · B3 11,000 + 104,000 + 156,000 = 271,000 ✓ · B5 Feb ending cash = 0 ✓ · B6 revolver nets to zero ✓ · B8 CCC 45 → 30 days, ₹180,000 freed ✓. Every bridge ties and every cash chain links.*
