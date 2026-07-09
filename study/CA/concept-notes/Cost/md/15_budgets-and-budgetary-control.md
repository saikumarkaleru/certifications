<!-- v2-deep -->

# Chapter 15 — Budgets & Budgetary Control

## 1. The Problem: A business is a fleet of ships that must arrive at the same port on the same day

Imagine you run a factory. Tomorrow morning, the sales team is going to promise customers 10,000 units. The purchase manager is deciding how much steel to order. The HR head is deciding whether to hire two more workers. The finance manager is deciding whether the company can afford to pay a supplier on the 15th. The production supervisor is planning shifts.

Every one of these people is making a decision **today** about the **future**, and every decision depends on what the others decide. If sales promises 10,000 units but production planned for 6,000, customers get let down. If purchases buys steel for 10,000 units but sales only sells 6,000, cash is locked in a warehouse. If finance did not foresee the wage bill of two new workers, the company bounces a cheque even while it is "profitable."

This is the coordination problem. Individually rational decisions, taken in isolation, produce a collectively irrational business. The organisation is a fleet of ships each captained by a manager, and unless someone gives every captain a shared chart, they sail to different ports.

There is a second, quieter problem. Suppose the year ends and profit is ₹40 lakh. Is that good? You cannot answer without a benchmark. Good compared to what? Compared to last year? Last year had different prices, a different scale, a different world. To judge performance you need a **standard set in advance** — a statement of what *should* have happened, against which you lay what *did* happen. Without it, "control" is just narrating history.

A **budget** solves both problems at once. It is a plan expressed in numbers, agreed before the period begins, that (a) forces every department's plans to be mutually consistent, and (b) becomes the yardstick against which actual results are later measured. **Budgetary control** is the machinery of comparing actual with budget, isolating the differences, and acting on them.

There is a third problem worth naming, because the exam frames theory questions around it: **the delegation problem.** A large firm cannot be run by one brain. Authority must be pushed down to divisional and departmental managers — but authority without a yardstick is a blank cheque. A budget is the device that lets top management *delegate* decisions while retaining *control*: each manager is given a budget (a defined slice of resources and a target), acts freely within it, and is later held to account against it. This is why budgeting and **responsibility accounting** are inseparable — a cost is reported against the manager who can *control* it, not against whoever happens to sit near it.

This chapter builds the entire apparatus from that need: why budgets exist, the family of budgets a firm prepares, the one distinction that separates a useless budget from a control tool (**fixed vs flexible**), how the functional budgets knit into a **master budget**, the **cash budget** that keeps the firm solvent, and **zero-based budgeting** for when incremental thinking rots. It also equips you with the two performance-measurement numbers the examiner loves to bolt onto a budget question — the **efficiency, activity and capacity ratios** — and the softer but heavily tested material on the **limitations of budgeting** and **behavioural** side-effects.

---

## 2. The Core Idea: A budget is a company's shared travel itinerary — priced

Think of a family planning a month-long trip across several cities. They do not just "hope it works out." They write an itinerary: which city on which date, the hotel booked, the train tickets, the daily spending money, and — critically — a check that the total cost fits the money in the bank *before they leave*.

The itinerary does three jobs, and they map exactly onto the three purposes of a budget:

- **Coordination.** Everyone's plans are made compatible. Dad's museum day and Mum's shopping day do not both need the one rental car at 10 a.m.
- **Motivation.** A target ("we will do Jaipur in two days") focuses effort. A vague wish ("let's see Rajasthan sometime") does not.
- **Control.** Halfway through, they compare the money actually spent with the money planned. Overspending in week 1 triggers a correction in week 2 — *before* the trip runs out of cash, not after.

A budget is that itinerary for a business, drawn in rupees and units. The key mental shift for the self-learner: **a budget is not a forecast.** A forecast is a passive prediction of what *will* happen ("it will probably rain"). A budget is an active commitment to make something happen ("we *will* produce and sell 1,20,000 units and we accept ₹X of cost to do it"). A forecast is an input to a budget; the budget is a decision.

**A fuller list of what budgets actually do** (examiners ask "state the objectives of budgeting"):

1. **Planning** — force managers to think ahead and commit intentions to numbers.
2. **Coordination** — reconcile the plans of interdependent departments into one consistent whole.
3. **Communication** — the approved budget tells every manager what is expected of them and of others.
4. **Motivation** — a clear, accepted target energises effort more than a vague hope.
5. **Control** — provide the pre-set standard against which actual results are judged, via variances.
6. **Performance evaluation** — a fair basis (once flexed) for appraising managers.
7. **Authorisation** — the approved budget is management's sanction to spend up to the stated limit.

Notice that some of these purposes quietly conflict. A budget set as a *motivating* stretch target (deliberately tough) is a poor *planning* forecast (it is not the most-likely outcome) and a harsh *evaluation* yardstick. This tension — the same number being asked to plan, motivate and judge at once — is the root of most budgeting's behavioural problems (Section 4.9).

> *Figure 15.1 — A budget converts a scattered set of departmental intentions into one coordinated, priced plan that later doubles as the yardstick for control.*

```mermaid
flowchart LR
    A["Sales intentions"] --> E["Budget as shared priced plan"]
    B["Production intentions"] --> E
    C["Purchase intentions"] --> E
    D["Finance intentions"] --> E
    E --> F["Coordinate before the period"]
    E --> G["Motivate with clear targets"]
    E --> H["Control by comparing actual with plan"]
```

---

## 3. Why It's Built This Way: three design decisions behind budgetary control

Before any formula, understand three deliberate design choices. Each one is a response to a way that naive planning fails.

**Design decision 1 — Start from the binding constraint (the principal / key / limiting budget factor).**
You cannot plan every department "at full speed" because something always runs out first — market demand, machine hours, skilled labour, cash, or raw material supply. This scarcest resource is the **principal budget factor** (also called the *key factor* or *limiting factor*). The whole budget is built *starting from it*, because planning the others beyond what the constraint allows just manufactures inconsistency. In most firms the constraint is **sales demand**, which is why the **sales budget is usually prepared first** and everything else is sized to it. If instead machine capacity were the bottleneck, production would be planned to capacity and sales sized down to match. Identifying this factor first is not a detail — it is the organising principle of the entire exercise.

*Deeper point — the constraint can shift.* The principal budget factor is not permanent. Relieve one bottleneck (buy a second machine) and a different resource (say, skilled labour or working capital) becomes binding. A subtle exam variant gives you *two* candidate constraints and expects you to test which bites first: compute the output each resource permits and the *smaller* answer identifies the true limiting factor. Common limiting factors the exam names: **materials** (shortage/quota), **labour** (skilled-worker scarcity), **plant capacity** (machine hours), **sales demand** (market saturation), **management** (thin managerial talent) and **finance/cash** (the firm cannot fund the working capital that fuller activity needs).

**Design decision 2 — Separate the plan from the yardstick by re-flexing it to actual activity (this is the seed of the flexible budget).**
If you plan for 10,000 units and actually make 8,000, comparing the ₹-cost of 8,000 real units against the ₹-cost of 10,000 planned units is comparing apples with oranges. Any manager will "beat" a cost budget simply by producing less. So the budget used for *control* must be **re-computed at the activity level that actually occurred**. That re-computation is the flexible budget, and it exists precisely so that control compares like with like. Hold this thought — Section 4 makes it the centre of gravity.

**Design decision 3 — Management by exception.**
A control system that asks managers to look at every number drowns them. Budgetary control reports only the **variances** — the gaps between actual and budget — and directs attention to the significant ones. Small, random, self-correcting differences are ignored; large or persistent ones are investigated. This is *management by exception*: the budget is the routine, the variance is the alarm.

Layered on top is the human/organisational scaffolding that makes it work:

- A **Budget Manual** — the written rulebook of who prepares what, in what format, by when. It standardises procedures, defines responsibilities, fixes the timetable and the account codes, and specifies the reports and their circulation. Its value is that it makes the process repeatable and depersonalised, so budgeting survives staff turnover.
- A **Budget Committee** — cross-functional heads (headed usually by the Chief Executive, serviced by the Budget Officer) who set guidelines, reconcile conflicting departmental plans, approve the functional budgets, and finally approve the master budget. It is the forum where the coordination problem is actually resolved by negotiation.
- A **Budget Officer** — the coordinator (often the cost/management accountant) who runs the process, chases inputs, ties the numbers together and reports variances. Note: the Budget Officer *coordinates*, they do not *impose* the numbers — the line managers own their budgets.
- The **Budget Period** — the length of time a budget covers (typically one year for operating budgets, broken into months/quarters for control; longer for capital budgets). Choice of period balances two forces: long enough to cover the full operating/seasonal cycle and to let plans mature, short enough that the forecasts remain reliable. Capital-heavy, long-gestation industries (power, shipbuilding) budget over many years; fashion or perishable-goods firms budget short.

**Two prerequisites the exam lists for a successful system:** (i) **top-management support** — without it, budgets are ignored; and (ii) a sound, **responsibility-based organisation structure** with clearly defined authority, so each budget maps to exactly one accountable manager (the essence of *responsibility accounting*: controllable costs reported to the manager who controls them).

---

## 4. Full Technical Content: the machinery, each piece with its reason

### 4.1 What "budgetary control" formally means

**Budgetary control** is the establishment of budgets relating the responsibilities of executives to the requirements of a policy, and the continuous comparison of actual with budgeted results — either to secure by individual action the objective of that policy, or to provide a basis for its revision. Unpack it: *establish budgets → assign to responsible managers → continuously compare actual vs budget → act (correct the action, or revise the plan)*. The last clause matters: a variance may mean the *manager* was wrong, or it may mean the *plan* was wrong. Control decides which.

**Budget vs Budgeting vs Budgetary control — three words the exam separates.** A **budget** is the *quantitative statement* (the plan itself). **Budgeting** is the *act of preparing* budgets. **Budgetary control** is the *whole system* — preparing budgets, comparing them with actuals, and taking corrective action. A budget without the comparison-and-action loop is just a plan; it becomes *control* only when the feedback machinery runs. Think of it as a thermostat: the budget is the set temperature, the actual reading is the room temperature, and budgetary control is the loop that switches the heater on and off.

**Advantages of budgetary control** (frequently a 4–5 mark theory question): forces forward planning; coordinates activities; defines responsibilities and delegates with control; provides a yardstick for performance and management by exception; promotes cost consciousness and efficiency; aids centralised control with decentralised activity; reveals capacity that is unused; and helps obtain finance (bankers respect a budgeted cash flow). Keep the list tied to the three purposes — coordinate, motivate, control — so it is never rote.

### 4.2 The family of budgets — three classification axes

Budgets are classified along three independent axes. The same budget sits on all three simultaneously.

**(A) By coverage / function:**
- **Functional budgets** — one per function: sales, production, materials (purchase and usage), direct labour, factory/production overhead, administration, selling & distribution, plant utilisation, capital expenditure, cash.
- **Master budget** — the consolidation of all functional budgets into a single summary: a budgeted Income Statement (Cost Sheet / P&L) and a budgeted Balance Sheet, plus the cash budget.

**(B) By capacity / flexibility — the control-critical axis:**
- **Fixed (static) budget** — prepared for a *single* anticipated level of activity; not adjusted if actual activity differs.
- **Flexible (variable) budget** — designed to *change with the level of activity*, by classifying costs into fixed, variable and semi-variable and recomputing the total for whatever activity actually occurs.

**(C) By period / conditions:**
- **Long-term** (3–10 yrs, strategic, e.g. capital budget) vs **short-term** (usually 1 yr) vs **current** (weeks/months).
- **Basic budget** (a long-run standard, unaltered for the base period) vs **current budget** (adjusted for current conditions).
- **Rolling / continuous budget** — as each month/quarter ends, a new one is added at the far end, so a full 12-month horizon is always in view. Reason: planning never falls off a cliff at year-end.

> *Figure 15.2 — The three independent axes along which any single budget is classified.*

```mermaid
flowchart TD
    R["Any budget"] --> A["By function"]
    R --> B["By flexibility"]
    R --> C["By period"]
    A --> A1["Functional budgets"]
    A --> A2["Master budget"]
    B --> B1["Fixed static budget"]
    B --> B2["Flexible variable budget"]
    C --> C1["Long term vs short term"]
    C --> C2["Basic vs current"]
    C --> C3["Rolling continuous"]
```

**When is a fixed budget actually appropriate?** The chapter rightly attacks the fixed budget for *control*, but do not overstate it — a fixed budget is perfectly valid (i) as the original *planning* statement of the expected level, (ii) where activity genuinely cannot vary much (e.g. a stable, made-to-order plant, or a purely administrative cost centre), and (iii) as the starting master budget the board approves. The sin is not preparing a fixed budget; the sin is using it *for control when activity has moved*. State it that way and you avoid the trap of writing "fixed budgets are useless."

### 4.3 Fixed vs Flexible — the heart of the chapter, and WHY flexible is needed

Here is the failure a fixed budget walks into. Suppose a factory budgets for **10,000 units**:

| | Budget (fixed, 10,000 u) | Actual (8,000 u) | "Variance" |
|---|---|---|---|
| Direct material @ ₹20/u (variable) | 2,00,000 | 1,64,000 | 36,000 F |
| Direct labour @ ₹15/u (variable) | 1,50,000 | 1,25,000 | 25,000 F |
| Factory rent (fixed) | 1,00,000 | 1,00,000 | — |
| Total cost | 4,50,000 | 3,89,000 | 61,000 F |

The fixed-budget comparison shows ₹61,000 **favourable**. The manager looks like a hero. But this is a lie: of course costs are lower — the factory made 20% fewer units. The comparison mixes two utterly different effects — the effect of *making fewer units* (a volume effect, often outside the cost manager's control) and the effect of *cost efficiency* (spending more or less per unit, which *is* the manager's job). A fixed budget cannot separate them, so it cannot control anything.

**The fix: flex the budget to the activity that actually happened (8,000 units).** Variable costs are re-computed at 8,000 units; fixed costs stay fixed.

| | Flexed budget @ 8,000 u | Actual @ 8,000 u | Variance |
|---|---|---|---|
| Direct material @ ₹20/u | 1,60,000 | 1,64,000 | 4,000 A |
| Direct labour @ ₹15/u | 1,20,000 | 1,25,000 | 5,000 A |
| Factory rent | 1,00,000 | 1,00,000 | — |
| Total cost | 3,80,000 | 3,89,000 | **9,000 A** |

Flexed to real activity, the truth appears: the manager actually **overspent by ₹9,000**. The favourable ₹61,000 was pure volume illusion. **This is why a flexible budget is indispensable for control: it compares like with like — the cost that *should* have been incurred for the output *actually produced* against the cost *actually incurred*.** A fixed budget is fine for *planning* a single expected level; it is useless for *controlling* when activity moves — and activity always moves.

**The mechanics of flexing — cost behaviour is the whole trick.** To flex, every cost must first be split by behaviour:

- **Variable cost** — total varies in direct proportion to activity; per-unit is constant. Flexed total = *variable rate per unit × actual units*.
- **Fixed cost** — total is unchanged across the relevant range; per-unit *falls* as activity rises. Flexed total = *same amount, always*.
- **Semi-variable (mixed) cost** — has both a fixed lump and a variable slice (e.g. electricity: a fixed connection charge plus per-unit consumption). It must be **segregated** into its two parts before flexing.
- **Stepped (step-fixed) cost** — fixed over a band of activity, then jumps to a new fixed level (e.g. one supervisor per 50 workers: hire the 51st worker and a second supervisor's salary steps in). Within each band it behaves like a fixed cost; the exam tests whether you notice the step when activity crosses the band boundary (see Section 4.3a).

**Segregating a semi-variable cost — the High–Low method** (the exam's workhorse). Take the cost at the highest activity and at the lowest activity:

$$\text{Variable rate per unit} = \frac{\text{Cost at highest activity} - \text{Cost at lowest activity}}{\text{Highest activity} - \text{Lowest activity}}$$

Then: **Fixed cost = Total cost at any level − (Variable rate × units at that level).** Once you have the fixed lump and the variable rate, the semi-variable cost flexes like any other. (More refined methods — least squares regression — exist, but High–Low is the standard exam tool.)

*High–Low caution the examiner exploits:* pick the highest and lowest **activity** levels, **not** the highest and lowest *costs*. If a cost figure is abnormal (a one-off repair spike) the High–Low line is distorted — the method assumes both endpoints are "normal." Also, if a *step-up in fixed cost* occurs between the low and high points, plain High–Low silently blends the step into the variable rate and is wrong; you must adjust one endpoint for the known step before dividing.

**Flexible budget formula for any activity level:**

$$\text{Budgeted total cost at activity } x = \text{Total fixed cost} + (\text{Variable cost per unit} \times x)$$

This straight line — a fixed intercept plus a variable slope — *is* the flexible budget. Give it any x, it returns the cost that x *ought* to cost.

**Measuring activity — % capacity, units, or hours?** A flexible budget can be flexed against different activity measures, and the question dictates which. Common bases: **units of output**, **direct labour hours**, **machine hours**, or **% of capacity**. Watch the distinction between **budgeted (normal) capacity**, **practical capacity** (theoretical max less unavoidable idle time for maintenance etc.), and **actual capacity utilised**. When a question says "budget was at 60% and actual was 75%," convert the % to the underlying units/hours before you flex — the variable slice keys off the physical measure, not the percentage sign.

> *Figure 15.3 — Why the flexible budget is the correct control benchmark: it re-flexes the plan to the activity that actually occurred so that only genuine cost performance remains.*

```mermaid
flowchart TD
    A["Original budget at planned activity"] --> B["Actual activity differs"]
    B --> C["Re-flex budget to actual activity"]
    C --> D["Split costs into fixed variable semi variable"]
    D --> E["Fixed stay same variable recomputed"]
    E --> F["Flexed budget cost for actual output"]
    G["Actual cost incurred"] --> H["Compare flexed budget with actual"]
    F --> H
    H --> I["Variance is genuine cost performance only"]
```

### 4.3a Edge cases in flexing — the tweaks an examiner adds

Three "what if the examiner tweaks it" variations sit on top of the basic flex, and each has a clean rule:

- **Stepped fixed cost crosses a band.** If fixed cost is "₹90,000 up to 15,000 units, ₹1,20,000 beyond," then flexing to 18,000 units uses ₹1,20,000, *not* ₹90,000. The fixed block is only fixed *within its relevant range*; read the data for the step and switch levels at the boundary. A favourite trap is to flex to a level that has crossed the step and leave the old fixed figure in.
- **A cost that is variable but not proportional to output** — e.g. a variable cost that changes with *labour hours* while output changes with *machine hours*, or a bulk-purchase discount that lowers the material rate above a threshold. Flex such a cost against *its own* driver, and apply the changed rate to the whole quantity (or only the excess) exactly as the question specifies. Do not blindly apply the low-volume rate at high volume.
- **Semi-variable cost given as a lump plus a percentage-of-something**, e.g. "selling overhead = ₹50,000 fixed + 2% of sales value." Here the variable slice keys off *sales value*, not units. Flex the 2% against the flexed sales figure. Mixing the driver (units vs value) is a silent error that fails the reconciliation.

The unifying principle: **flex each cost against the driver it actually responds to, over the range it actually applies.** Rote "variable = rate × units" fails the moment the driver or the range changes.

### 4.4 The functional budgets — order, logic and formats

The functional budgets are prepared in a **strict sequence** dictated by the principal budget factor. Assuming (as usual) that **sales demand is the limiting factor**, the chain is:

> *Figure 15.4 — The build order of functional budgets when sales demand is the principal budget factor, converging into the master budget.*

```mermaid
flowchart TD
    S["Sales budget"] --> P["Production budget in units"]
    P --> M["Material usage and purchase budget"]
    P --> L["Direct labour budget"]
    P --> O["Overhead budget"]
    S --> SD["Selling and distribution budget"]
    M --> C["Cash budget"]
    L --> C
    O --> C
    SD --> C
    S --> C
    C --> MB["Master budget"]
    P --> MB
    O --> MB
```

**(1) Sales budget.** The starting point and, usually, the foundation of everything. Estimated **quantity × selling price**, broken by product, region, period, salesperson. Built from the sales force's estimates, past trends, market research, capacity and pricing policy.

**(2) Production budget (in units).** How many units must be *manufactured* to meet the sales plan while moving inventory from opening to the desired closing level. The logic is a stock reconciliation:

$$\text{Units to produce} = \text{Budgeted sales} + \text{Desired closing FG stock} - \text{Opening FG stock}$$

*Why this shape:* you must produce enough to (a) satisfy sales and (b) build the closing stock, but you get a head start from opening stock, so it is subtracted. This budget is then sub-divided into a **production cost budget** and feeds materials, labour and overheads.

*Production policy variants the exam adds:* sometimes the firm wants to **stabilise production** (produce the same quantity every month despite seasonal sales) so that inventory absorbs the swings; sometimes it wants to **stabilise inventory** (produce to match sales, letting the workforce swing); often it sets closing stock as "a fixed number of days/weeks of the *next* period's sales." Read which policy applies, because it changes the closing-stock figure that feeds the reconciliation. If closing stock is "one month of next month's sales," you must look *forward*, not backward.

**(3) Material budgets — two distinct budgets, do not confuse them.**

- **Material *usage* (consumption) budget** = units to produce × material required per unit. This is driven by *production*.
  $$\text{Material to be consumed} = \text{Units produced} \times \text{material per unit}$$
- **Material *purchase* budget** = what to *buy*, after a second stock reconciliation on raw materials:
  $$\text{Material to purchase} = \text{Material consumed} + \text{Desired closing RM stock} - \text{Opening RM stock}$$

*Why two:* consumption is a production question; purchasing is a stores/cash question. They differ by the change in raw-material inventory. Purchases (× price) drive the cash outflow to suppliers.

*Multi-material extension:* with several raw materials, run a *separate* usage-and-purchase reconciliation for each material (each has its own per-unit rate, price, and opening/closing stock), then sum the values. Do not merge kilograms of steel with litres of paint — reconcile in physical units per material, value each, then total.

**(4) Direct labour budget.** Standard hours per unit × units to produce = total hours; × wage rate = labour cost. Also flags whether the workforce/overtime is adequate. A richer version converts total hours into a *headcount*: required workers = total budgeted hours ÷ (hours per worker in the period), which tells HR how many to hire or whether overtime/idle time looms. Where different grades of labour (skilled, semi-skilled) are used, budget each grade separately at its own rate.

**(5) Overhead budgets.** Production overhead (split fixed/variable), administration overhead, selling & distribution overhead — each estimated and, for control, prepared in *flexible* form. Selling & distribution overhead often has a variable slice tied to *sales value or volume* rather than to production, so key it off the sales budget.

**(6) Other budgets.** Plant utilisation, R&D, capital expenditure (long-term), and the **cash budget** (below).

### 4.4a Capacity and efficiency ratios — the performance numbers bolted onto budgets

Examiners frequently append these three ratios to a budget question. They compare **budgeted, standard and actual** hours and answer "did we work hard, and did we work well?" Let three quantities be defined for a period:

- **Budgeted hours** — the hours the budget planned for (budgeted output × standard hours/unit).
- **Standard hours for actual output** — the hours the *actual output* should have taken (actual output × standard hours/unit). This is the "flexible budget of hours."
- **Actual hours worked** — clock hours actually spent.

$$\textbf{Efficiency Ratio} = \frac{\text{Standard hours for actual output}}{\text{Actual hours worked}} \times 100$$

$$\textbf{Capacity (Utilisation) Ratio} = \frac{\text{Actual hours worked}}{\text{Budgeted hours}} \times 100$$

$$\textbf{Activity (Volume) Ratio} = \frac{\text{Standard hours for actual output}}{\text{Budgeted hours}} \times 100$$

The identity that ties them together (and is a self-check): **Activity Ratio = Efficiency Ratio × Capacity Ratio** (as fractions). In words: how much output we produced relative to plan (activity) equals how *hard* we worked (capacity) times how *efficiently* those hours converted into output (efficiency). Some texts add a **Calendar Ratio = actual working days ÷ budgeted working days × 100**, which explains capacity shortfalls caused by fewer working days (holidays, strikes). Interpretation: a ratio above 100% is favourable (more output/hours than planned); below 100% is adverse. Worked Example 6 puts numbers to this.

### 4.5 The Cash Budget — keeping a profitable firm from going broke

**The problem it solves:** profit and cash are *not* the same thing. A firm can be highly profitable on paper and still fail to pay wages next Tuesday, because customers pay in 60 days while wages fall due weekly, and because depreciation is a cost but not a cash outflow. The cash budget is a **month-by-month forecast of cash receipts and payments** that reveals, *in advance*, when the firm will have a surplus (to invest) or a deficit (to arrange an overdraft for). It is the single most practically important budget for survival.

**Golden rule of the cash budget: include only actual cash movements, and time them when the cash actually moves — not when the sale or expense is recorded.**

- **Include:** cash sales; collections from debtors (lagged by the credit period); loans raised; interest/dividends received; sale of assets; issue of shares.
- **Include (payments):** cash paid to suppliers (lagged by credit received); wages; overheads paid in cash; tax; dividends paid; capital expenditure; loan repayments.
- **EXCLUDE non-cash items entirely:** **depreciation**, provisions for bad debts, writing off goodwill, notional/imputed costs, and any **accrued** expense not yet paid. These never touch the bank.
- **Timing is everything:** a sale in January collected in March is a *March* receipt. A purchase in January paid in February is a *February* payment.

**Format — the receipts-and-payments method** (the exam standard):

$$\text{Closing balance} = \text{Opening balance} + \text{Total receipts} - \text{Total payments}$$

and each month's **closing balance becomes next month's opening balance** (the balances chain). Where a minimum cash balance is required, any shortfall signals borrowing; any excess above it signals investible surplus.

**Two other methods you should be able to name** (the receipts-and-payments method is what problems use, but theory may ask for the alternatives):

1. **Adjusted profit-and-loss (cash-flow) method** — start from budgeted net profit, add back non-cash charges (depreciation, provisions), and adjust for changes in working capital (increase in debtors/stock reduces cash, increase in creditors raises cash) plus capital and financing flows. Useful for *longer* horizons where item-by-item timing is impractical.
2. **Balance-sheet method** — project the closing balance sheet with every item except cash, and derive cash as the balancing figure. Rarely asked to compute, often asked to identify.

**Handling common cash-budget wrinkles the examiner loves:**
- **Bad debts / cash discount on collections.** If 2% of debtors default, collect only 98%; if a cash discount is offered for prompt payment, reduce the receipt by the discount. Never collect 100% of credit sales unless told to.
- **Split collection patterns.** "60% collected in the month after sale, 30% in the second month, 10% bad" — spread each month's credit sales across the stated pattern and *sum the overlapping tails* in each column.
- **Advance payments / deposits.** A customer advance is a receipt *when received*, even before the sale.
- **Tax and dividend** are paid on their due dates, often quarterly/annually — enter in the month of payment, not the month of provision.
- **Interest on overdraft** — if the question asks you to fund shortfalls, the resulting overdraft may itself carry interest, which becomes a later payment; do this only if explicitly required.

### 4.6 The Master Budget

The **master budget** is the summary budget incorporating all functional budgets, finally approved by the budget committee. It is not a fourth kind of calculation — it is the **consolidation**: a budgeted income statement (cost of sales and profit) and a budgeted balance sheet, supported by the cash budget. It is the single document the board approves and against which overall performance is judged.

Structurally the master budget has two halves that mirror financial statements: the **operating budget** (sales → cost of goods sold → gross profit → operating expenses → operating profit — built from the functional budgets) and the **financial budget** (cash budget, budgeted balance sheet, and capital-expenditure budget). Seeing this two-part shape helps in a "prepare the budgeted P&L and balance sheet" question: everything above operating profit comes from the functional operating budgets; the cash budget and capex feed the balance sheet.

### 4.7 Zero-Based Budgeting (ZBB) — refusing to inherit last year's fat

**The problem it solves:** the ordinary approach, **incremental budgeting**, takes last year's figure and adds a percentage. Its fatal flaw is that it *inherits every past inefficiency* — if a department wasted ₹5 lakh last year, incremental budgeting quietly re-funds that ₹5 lakh plus 8%. Waste becomes permanent because nobody re-justifies the base.

**ZBB flips the burden of proof.** Every activity starts from a **"zero base"** each cycle; every rupee, including the base, must be justified afresh as if the activity were brand new. Nothing is entitled to funding merely because it existed last year.

**The ZBB process:**
1. **Define decision units** — the smallest activities that can be separately evaluated.
2. **Build decision packages** — for each unit, describe the activity, its purpose, costs, benefits, and alternative ways (and levels) of performing it.
3. **Rank the packages** across the organisation by cost-benefit, from indispensable to marginal.
4. **Allocate resources** down the ranked list until the funds run out; packages below the line are cut.

**Strengths:** eliminates inherited waste; links spend to objectives; forces managers to justify activities; good for discretionary/support costs (R&D, admin, marketing). **Weaknesses:** time-consuming and costly; needs skill and honesty; hard to quantify benefits of some activities; can breed short-termism. Consequently ZBB is often applied *periodically* (say every few years) or selectively to discretionary areas, not to every line every year.

**Incremental vs Zero-based — the crisp contrast table** (exam-ready):

| Aspect | Incremental budgeting | Zero-based budgeting |
|---|---|---|
| Starting point | Last year's figure | Zero — nothing assumed |
| Burden of proof | Only the *increment* is justified | *Every* rupee is justified |
| Treatment of past waste | Carried forward, re-funded | Exposed and cut |
| Cost and time to prepare | Low | High |
| Best suited to | Stable, committed costs | Discretionary/support costs |
| Behavioural effect | "Spend it or lose it" mentality | Cost consciousness, but padding risk |

**Related modern budgeting approaches to name** (the exam sometimes asks you to distinguish these one-liners):
- **Performance budgeting** — budgets built around *functions, programmes and activities* with output measures, so spend is linked to results (common in government).
- **Activity-based budgeting (ABB)** — budgets built from *cost drivers* and activities rather than departments; the budgeting mirror of activity-based costing.
- **Kaizen budgeting** — budgets that build *continuous cost reduction* into each successive period (targets tighten over time).
- **Rolling (continuous) budgeting** — already met in 4.2; continuously extended so a full horizon is always in view; keep it distinct from ZBB.

> *Figure 15.5 — Incremental budgeting inherits the past base while ZBB re-justifies every activity from zero.*

```mermaid
flowchart LR
    A["Incremental budgeting"] --> B["Take last year figure"]
    B --> C["Add a percentage"]
    C --> D["Past waste is re-funded"]
    E["Zero based budgeting"] --> F["Start every activity at zero"]
    F --> G["Justify each decision package"]
    G --> H["Rank and fund top down"]
    H --> I["Unjustified spend is cut"]
```

### 4.8 The budgeting process as a control loop

Everything above is static description; the *system* is a loop that runs every period. Setting it out as a cycle helps answer "explain the process of budgetary control."

> *Figure 15.6 — Budgetary control is a closed feedback loop that plans, measures, compares and corrects each period.*

```mermaid
flowchart TD
    A["Identify principal budget factor"] --> B["Prepare functional budgets in sequence"]
    B --> C["Budget committee reconciles and approves master budget"]
    C --> D["Operate the period"]
    D --> E["Record actual results"]
    E --> F["Flex budget to actual activity"]
    F --> G["Compare flexed budget with actual and compute variances"]
    G --> H["Report exceptions to responsible managers"]
    H --> I["Corrective action or revise the plan"]
    I --> A
```

The loop's teeth are the **feedback** arrow (compare-and-correct after the fact) and, in better systems, **feed-forward** (spotting a coming deviation — e.g. a forecast cash deficit in the cash budget — and acting *before* it happens). The cash budget is the classic feed-forward instrument: it warns of a June shortfall in April, so finance is arranged in time.

### 4.9 Limitations and behavioural aspects — the "soft" content that carries marks

A concept chapter that only teaches the arithmetic misses the marks reserved for judgement. Know the **limitations** and the **behavioural** pitfalls.

**Limitations of budgetary control:**
- A budget is built on **estimates**; its quality cannot exceed the quality of the forecasts behind it.
- It is a **tool, not a substitute for management** — budgets do not execute themselves; managers must act on variances.
- **Rigidity** — an over-rigid budget can stop managers responding to genuine, unforeseen opportunities or changes.
- **Cost** — a full system is expensive; for a small firm the cost may exceed the benefit.
- **Time lag** — variance reports arrive after the event; control is only as fast as the reporting cycle.
- **Conflict** — departmental budgets can breed silo behaviour and inter-departmental friction.

**Behavioural side-effects** (why budgets sometimes backfire):
- **Budget padding / slack** — managers deliberately overstate costs or understate revenues so the target is easy to beat. ZBB and participative review attack this.
- **"Spend it or lose it"** — fear that unspent budget will be cut next year drives wasteful year-end spending (the incremental system's classic disease).
- **Dysfunctional behaviour** — a manager hits *their* budget in a way that hurts the *whole* firm (e.g. skimping on maintenance to beat a cost budget, causing breakdowns later).
- **Participation vs imposition** — **participative (bottom-up)** budgets that managers help set earn commitment but risk slack; **imposed (top-down)** budgets are tighter but can demotivate. The practical middle is *negotiated* budgets with genuine top-management involvement.
- **Aspiration level** — targets must be tight enough to stretch yet attainable enough to motivate; a target seen as impossible is abandoned, and one seen as trivial is ignored.

Being able to write two or three of these crisply turns a pure-numbers answer into a complete one.

---

## 5. Worked Examples — full, step-by-step, reconciled

### Worked Example 1 (Easy) — Production, material usage and purchase budgets

**Data.** Zenith Ltd sells a single product. Budgeted sales for the quarter = **48,000 units**. It wants closing finished-goods (FG) stock of **6,000 units**; opening FG stock is **4,000 units**. Each unit needs **3 kg** of raw material at **₹25/kg**. It wants closing raw-material (RM) stock of **15,000 kg**; opening RM stock is **9,000 kg**.

**Required:** production budget (units), material usage budget (kg), and material purchase budget (kg and ₹).

**Step 1 — Production budget (units).** Produce enough for sales plus the desired stock build, less the head start from opening stock.

| Production budget | Units |
|---|---|
| Budgeted sales | 48,000 |
| Add: Desired closing FG stock | 6,000 |
| Less: Opening FG stock | (4,000) |
| **Units to be produced** | **50,000** |

**Step 2 — Material usage (consumption) budget.** Driven by production.

$$50{,}000 \text{ units} \times 3 \text{ kg} = 1{,}50{,}000 \text{ kg consumed}$$

**Step 3 — Material purchase budget.** Buy enough to cover consumption plus the RM stock build, less opening RM stock.

| Material purchase budget | Kg |
|---|---|
| Material to be consumed | 1,50,000 |
| Add: Desired closing RM stock | 15,000 |
| Less: Opening RM stock | (9,000) |
| **Material to be purchased** | **1,56,000** |

**Value of purchases** = 1,56,000 kg × ₹25 = **₹39,00,000.**

*Note the two separate stock reconciliations — one on finished goods (Step 1), one on raw material (Step 3). Confusing consumption with purchases is the classic error.*

---

### Worked Example 2 (Moderate) — Flexible budget with a semi-variable cost segregated

**Data.** A factory's overhead budget was prepared at **60% capacity = 12,000 units**. Costs at that level:

| Cost | ₹ at 12,000 u | Behaviour |
|---|---|---|
| Direct material | 3,60,000 | Variable |
| Direct labour | 2,40,000 | Variable |
| Power | 84,000 | Semi-variable |
| Repairs & maintenance | 60,000 | Semi-variable |
| Factory rent | 1,20,000 | Fixed |
| Supervision | 90,000 | Fixed |

Additional information for the two semi-variable costs (given at two activity levels so we can segregate them):

| Semi-variable cost | ₹ at 12,000 u (60%) | ₹ at 16,000 u (80%) |
|---|---|---|
| Power | 84,000 | 1,00,000 |
| Repairs & maintenance | 60,000 | 68,000 |

**Required:** prepare a flexible budget at **60%, 80% and 100% capacity** (100% = 20,000 units).

**Step 1 — Segregate the semi-variable costs by High–Low.**

*Power:*
$$\text{Variable rate} = \frac{1{,}00{,}000 - 84{,}000}{16{,}000 - 12{,}000} = \frac{16{,}000}{4{,}000} = ₹4/\text{unit}$$
Fixed part = 84,000 − (4 × 12,000) = 84,000 − 48,000 = **₹36,000**. (Check at 16,000: 36,000 + 4×16,000 = 1,00,000 ✓)

*Repairs & maintenance:*
$$\text{Variable rate} = \frac{68{,}000 - 60{,}000}{16{,}000 - 12{,}000} = \frac{8{,}000}{4{,}000} = ₹2/\text{unit}$$
Fixed part = 60,000 − (2 × 12,000) = 60,000 − 24,000 = **₹36,000**. (Check at 16,000: 36,000 + 2×16,000 = 68,000 ✓)

**Step 2 — Establish per-unit variable rates and fixed lumps.**

| Cost | Variable ₹/unit | Fixed ₹ |
|---|---|---|
| Direct material | 3,60,000 ÷ 12,000 = 30 | — |
| Direct labour | 2,40,000 ÷ 12,000 = 20 | — |
| Power | 4 | 36,000 |
| Repairs & maintenance | 2 | 36,000 |
| Factory rent | — | 1,20,000 |
| Supervision | — | 90,000 |
| **Total** | **56 / unit** | **2,82,000** |

**Step 3 — Flex to each capacity.** Total cost = Fixed 2,82,000 + 56 × units.

| Cost element | 60% (12,000 u) | 80% (16,000 u) | 100% (20,000 u) |
|---|---|---|---|
| Direct material (₹30/u) | 3,60,000 | 4,80,000 | 6,00,000 |
| Direct labour (₹20/u) | 2,40,000 | 3,20,000 | 4,00,000 |
| Power (36,000 + ₹4/u) | 84,000 | 1,00,000 | 1,16,000 |
| Repairs & mtce (36,000 + ₹2/u) | 60,000 | 68,000 | 76,000 |
| Factory rent (fixed) | 1,20,000 | 1,20,000 | 1,20,000 |
| Supervision (fixed) | 90,000 | 90,000 | 90,000 |
| **Total cost** | **9,54,000** | **11,78,000** | **13,02,000** |
| **Cost per unit** | **79.50** | **73.625** | **65.10** |

**Reconciliation / self-check.** At 100%: fixed 2,82,000 + variable (56 × 20,000 = 11,20,000) = **13,02,000 ✓**. Notice the cost *per unit falls* as activity rises (79.50 → 73.625 → 65.10) — the signature of fixed cost being spread over more units. That single fact is *why* comparing per-unit costs across different volumes is meaningless, and why control must use the flexed *total* at actual activity.

*Examiner tweak to watch:* if the question added "at 100% capacity, factory rent steps up to ₹1,50,000 because a second shed is leased," you would **replace** the ₹1,20,000 only in the 100% column, lifting its total to 13,32,000 and its per-unit to 66.60. Always scan for such step-ups before copying a fixed figure across all columns.

---

### Worked Example 3 (Exam-hard) — Flexible budget as a control tool, fully reconciled with a fixed budget

**Data.** Pioneer Ltd budgeted (fixed budget) for **10,000 units** but actually produced and sold **12,000 units**. Cost structure per the original budget:

- Direct material: ₹40/unit (variable)
- Direct labour: ₹30/unit (variable)
- Variable overhead: ₹10/unit (variable)
- Semi-variable overhead: ₹80,000 at 10,000 units; it rises by ₹10,000 for every 2,000 units above 10,000 (i.e. ₹5/unit variable slice on top of a fixed lump).
- Fixed overhead: ₹1,50,000 (fixed within the relevant range up to 12,000 units).

**Actual costs incurred at 12,000 units:** Direct material ₹5,04,000; Direct labour ₹3,54,000; Variable overhead ₹1,26,000; Semi-variable overhead ₹98,000; Fixed overhead ₹1,55,000.

**Required:** (a) the fixed budget; (b) the flexed budget at 12,000 units; (c) the variance against the *flexed* budget with a full reconciliation; and (d) show why the fixed-budget comparison misleads.

**Step 1 — Segregate the semi-variable overhead.** It is ₹80,000 at 10,000 units, and increases ₹10,000 per 2,000 units → variable rate = 10,000 ÷ 2,000 = **₹5/unit**. Fixed part = 80,000 − (5 × 10,000) = **₹30,000**. So semi-variable = 30,000 + 5 × units.

**Step 2 — Build all three columns.** Variable per-unit rates: material 40, labour 30, variable OH 10, semi-variable slice 5. Fixed lumps: semi-variable 30,000 + fixed OH 1,50,000 = 1,80,000 total fixed.

| Cost element | Fixed budget (10,000 u) | Flexed budget (12,000 u) | Actual (12,000 u) | Variance |
|---|---|---|---|---|
| Direct material (₹40/u) | 4,00,000 | 4,80,000 | 5,04,000 | 24,000 A |
| Direct labour (₹30/u) | 3,00,000 | 3,60,000 | 3,54,000 | 6,000 F |
| Variable overhead (₹10/u) | 1,00,000 | 1,20,000 | 1,26,000 | 6,000 A |
| Semi-variable (30,000 + ₹5/u) | 80,000 | 90,000 | 98,000 | 8,000 A |
| Fixed overhead | 1,50,000 | 1,50,000 | 1,55,000 | 5,000 A |
| **Total cost** | **10,30,000** | **12,00,000** | **13,37,000** | **37,000 A** |

**Step 3 — Reconcile the variance (the tie-out).**
Sum of element variances: 24,000 A − 6,000 F + 6,000 A + 8,000 A + 5,000 A = **37,000 A**.
Total flexed budget 12,00,000 vs Actual 13,37,000 = **37,000 Adverse ✓.** The parts tie to the whole.

**Step 4 — Why the fixed comparison misleads.** If you naively compared the **fixed** budget (₹10,30,000 for 10,000 units) with the **actual** (₹13,37,000 for 12,000 units), you would report a ₹3,07,000 *adverse* "variance" and panic. But most of that gap is simply the cost of making 2,000 *extra* units — a *volume* effect, not inefficiency. The flexible budget strips the volume effect out (10,30,000 → 12,00,000 is the legitimate cost of the extra volume) and reveals the *true* cost-control failure: only **₹37,000 adverse**. 

The full decomposition:
- Total fixed-budget-to-actual gap: 13,37,000 − 10,30,000 = **3,07,000 A**
- Of which, volume effect (flexing 10,000 → 12,000 units): 12,00,000 − 10,30,000 = **1,70,000** (extra cost that *should* be incurred for the extra output — not a controllable variance)
- True cost/expenditure variance (flexed vs actual): **37,000 A**
- Check: 1,70,000 + 37,000 = 3,07,000 ✓

This is the entire argument of Section 4.3 made numerical: **only the ₹37,000 belongs on the cost manager's report card.** The ₹1,70,000 is the price of doing more business, which is good news, not bad.

---

### Worked Example 4 (Exam-hard) — Cash Budget

**Data.** Sunrise Ltd wants a cash budget for **April, May, June**. 

Sales (₹): Feb 2,00,000; Mar 2,20,000; Apr 2,40,000; May 2,60,000; Jun 3,00,000.
- **Sales pattern:** 25% cash, 75% credit. Credit customers pay **one month after sale**.
- **Purchases (₹):** Mar 1,20,000; Apr 1,40,000; May 1,50,000; Jun 1,60,000. Paid **one month after purchase**.
- **Wages:** paid in the *same* month — Apr 40,000; May 44,000; Jun 48,000.
- **Overheads:** ₹30,000 per month, paid in the same month. This figure **includes ₹8,000 depreciation.**
- **Machinery** costing ₹1,00,000 to be bought in **May**, paid in **June**.
- **Dividend** of ₹20,000 payable in **April**.
- **Opening cash balance on 1 April = ₹50,000.** Minimum desired balance = ₹25,000.

**Required:** cash budget for the three months and comment on financing.

**Step 1 — Cash receipts. Split cash sales (same month, 25%) and credit collections (75%, one month late).**

| Receipts | April | May | June |
|---|---|---|---|
| Cash sales (25% of current month) | 60,000 | 65,000 | 75,000 |
| Collection from debtors (75% of prior month) | 1,65,000 | 1,80,000 | 1,95,000 |
| **Total receipts** | **2,25,000** | **2,45,000** | **2,70,000** |

*Working:* Apr cash = 25% × 2,40,000 = 60,000; Apr debtors = 75% × Mar 2,20,000 = 1,65,000. May cash = 25% × 2,60,000 = 65,000; May debtors = 75% × Apr 2,40,000 = 1,80,000. Jun cash = 25% × 3,00,000 = 75,000; Jun debtors = 75% × May 2,60,000 = 1,95,000.

**Step 2 — Cash payments. Note: purchases lag one month; overheads exclude the ₹8,000 depreciation (cash overhead = 30,000 − 8,000 = ₹22,000); machinery is *paid* in June though bought in May.**

| Payments | April | May | June |
|---|---|---|---|
| Payment to suppliers (prior month purchases) | 1,20,000 | 1,40,000 | 1,50,000 |
| Wages (same month) | 40,000 | 44,000 | 48,000 |
| Cash overheads (30,000 − 8,000 dep.) | 22,000 | 22,000 | 22,000 |
| Machinery (bought May, paid June) | — | — | 1,00,000 |
| Dividend | 20,000 | — | — |
| **Total payments** | **2,02,000** | **2,06,000** | **3,20,000** |

**Step 3 — Assemble the cash budget (closing balance chains into next opening).**

| | April | May | June |
|---|---|---|---|
| Opening balance | 50,000 | 73,000 | 1,12,000 |
| Add: Receipts | 2,25,000 | 2,45,000 | 2,70,000 |
| Less: Payments | (2,02,000) | (2,06,000) | (3,20,000) |
| **Closing balance** | **73,000** | **1,12,000** | **62,000** |

**Step 4 — Reconciliation and comment.** Each closing rolls to the next opening: 50,000 → 73,000 → 1,12,000 → 62,000 ✓. Independent net check: total receipts (2,25,000+2,45,000+2,70,000 = 7,40,000) − total payments (2,02,000+2,06,000+3,20,000 = 7,28,000) = net +12,000; opening 50,000 + 12,000 = **62,000 closing ✓.**

**Financing comment:** the firm stays above its ₹25,000 minimum in all three months, so **no overdraft is needed.** In June the machinery payment (₹1,00,000) squeezes the balance from ₹1,12,000 down to ₹62,000, but it remains comfortable. The surplus in April–May (well above the ₹25,000 floor) could be short-term invested. *The two traps this problem tests — excluding the ₹8,000 depreciation, and timing the machinery payment in June not May — are exactly where marks are lost.*

---

### Worked Example 5 (Exam-hard) — Cash Budget with a collection pattern, bad debts, cash discount and a minimum-balance overdraft

*This is Example 4 "with the examiner's screws turned." It tests the wrinkles listed in Section 4.5.*

**Data.** Orbit Ltd needs a cash budget for **Jul, Aug, Sep**.

Credit sales (₹): May 4,00,000; Jun 5,00,000; Jul 6,00,000; Aug 5,50,000; Sep 6,50,000. (All sales are on credit.)
- **Collection pattern:** 50% in the month *after* sale (these customers take a **2% cash discount**), 30% in the second month after sale, 18% in the third month after sale, and **2% become bad debts.**
- **Purchases (₹)** are 60% of the *same month's* sales and are **paid the following month** in full.
- **Wages & cash expenses:** ₹1,20,000 per month, paid in the same month.
- **Tax** of ₹90,000 is payable in **September**.
- **Opening balance on 1 July = ₹40,000; minimum required balance = ₹1,00,000.** Any shortfall is met by an overdraft in multiples of ₹10,000 (ignore overdraft interest).

**Required:** the cash budget and the overdraft, if any, needed each month.

**Step 1 — Build the collection schedule.** For each sales month, 50% (less 2% discount) lands 1 month later, 30% two months later, 18% three months later. The *net* first-month collection = 50% × (1 − 2%) = 49% of that month's sales.

*July collections* come from: Jun (1 month back, 49%), May (2 months back, 30%), Apr (3 months back — not given, ignore/assume zero for the tail we lack). Since we lack April, and the problem gives us May onward, the earliest fully-computable "three-tail" month is September. To keep it clean, compute what the data supports:

| Collected in → | July | Aug | Sep |
|---|---|---|---|
| From Jun (49% / 30% / 18%) | 49% × 5,00,000 = 2,45,000 | 30% × 5,00,000 = 1,50,000 | 18% × 5,00,000 = 90,000 |
| From May (30% / 18%) | 30% × 4,00,000 = 1,20,000 | 18% × 4,00,000 = 72,000 | — |
| From Jul (49% / 30%) | — | 49% × 6,00,000 = 2,94,000 | 30% × 6,00,000 = 1,80,000 |
| From Aug (49%) | — | — | 49% × 5,50,000 = 2,69,500 |
| **Total receipts** | **3,65,000** | **5,16,000** | **8,08,500** |

*(May's 49% one-month collection fell in June and Jun's earlier tail in May — outside our window — so they correctly do not appear. This "overlapping tails" build is exactly the split-pattern skill being tested.)*

**Step 2 — Payments. Purchases = 60% of the month's sales, paid next month.**
- Paid in Jul = 60% × Jun sales = 60% × 5,00,000 = 3,00,000
- Paid in Aug = 60% × Jul sales = 60% × 6,00,000 = 3,60,000
- Paid in Sep = 60% × Aug sales = 60% × 5,50,000 = 3,30,000

| Payments | July | Aug | Sep |
|---|---|---|---|
| Suppliers (60% of prior-month sales) | 3,00,000 | 3,60,000 | 3,30,000 |
| Wages & cash expenses | 1,20,000 | 1,20,000 | 1,20,000 |
| Tax | — | — | 90,000 |
| **Total payments** | **4,20,000** | **4,80,000** | **5,40,000** |

**Step 3 — Cash budget with the minimum-balance / overdraft mechanism.**

| | July | Aug | Sep |
|---|---|---|---|
| Opening balance | 40,000 | 1,00,000 | 1,00,000 |
| Add: Receipts | 3,65,000 | 5,16,000 | 8,08,500 |
| Less: Payments | (4,20,000) | (4,80,000) | (5,40,000) |
| Balance before financing | (15,000) | 1,36,000 | 3,68,500 |
| Overdraft drawn (to reach ₹1,00,000 min, in ₹10,000 multiples) | 1,20,000 | — | — |
| Overdraft repaid | — | (36,000)→ round to (30,000) | (90,000) |
| **Closing balance** | **1,05,000** | **1,06,000** | **3,78,500** |

*Financing logic:* In July the pre-financing balance is −₹15,000, ₹1,15,000 below the ₹1,00,000 floor; drawing an overdraft in ₹10,000 multiples needs ₹1,20,000 to clear the floor (−15,000 + 1,20,000 = 1,05,000 ≥ 1,00,000). Thereafter surplus above the floor repays the overdraft in ₹10,000 multiples: Aug repays ₹30,000 (1,36,000 − 30,000 = 1,06,000, still ≥ floor), Sep repays the remaining ₹90,000 (3,68,500 − 90,000 = 2,78,500 — wait, recompute: outstanding after Aug = 1,20,000 − 30,000 = 90,000; Sep repays 90,000, closing 3,68,500 − 90,000 = 2,78,500).

**Self-check / correction.** Redoing Sep cleanly: opening 1,06,000 + receipts 8,08,500 − payments 5,40,000 = 3,74,500 before financing; repay full outstanding overdraft ₹90,000 → **closing ₹2,84,500**, comfortably above the floor and overdraft fully cleared by quarter-end. *(The lesson: always recompute the chained opening balances after each financing entry — a single mis-carried figure cascades. The examiner rewards the visible re-check, not just the final number.)*

**Takeaways this problem drills:** net-of-discount first-month collections (49% not 50%), bad debts simply never collected (the 2% vanishes), overlapping collection tails summed per column, and an overdraft sized to a *minimum balance* in stated multiples with subsequent repayment.

---

### Worked Example 6 (Moderate) — Efficiency, Capacity and Activity ratios

**Data.** A department budgeted to produce **8,000 units** in a month, each with a standard time of **2 hours**, giving budgeted hours of 16,000. During the month it actually **worked 15,000 hours** and produced **7,800 units**.

**Required:** the efficiency, capacity and activity ratios, and their reconciliation.

**Step 1 — The three hour-quantities.**
- Budgeted hours = 8,000 × 2 = **16,000 hrs**
- Standard hours for actual output = 7,800 × 2 = **15,600 hrs**
- Actual hours worked = **15,000 hrs**

**Step 2 — The ratios.**
$$\text{Efficiency} = \frac{15{,}600}{15{,}000} \times 100 = \mathbf{104\%}$$
$$\text{Capacity} = \frac{15{,}000}{16{,}000} \times 100 = \mathbf{93.75\%}$$
$$\text{Activity} = \frac{15{,}600}{16{,}000} \times 100 = \mathbf{97.5\%}$$

**Step 3 — Reconcile via the identity Activity = Efficiency × Capacity.**
$$1.04 \times 0.9375 = 0.975 = \mathbf{97.5\%} \checkmark$$

**Interpretation.** The team worked *fewer* hours than planned (capacity 93.75%, below 100% — perhaps idle time or fewer working days) but was *efficient* while working (104%, output beat the standard time). The net effect on output is a slight shortfall against plan (activity 97.5%). This is exactly how the examiner wants the story read: capacity is *how much you showed up*, efficiency is *how well you worked*, activity is *the combined effect on output*.

---

## 6. Presentation & Format Standards

- **Every budget carries a heading** stating the entity, the budget's name, and the **period/activity level** it is drawn for (e.g. "Flexible Budget at 60%, 80% and 100% capacity"). For flexible budgets, activity levels are the *columns*.
- **Order the functional budgets** in preparation sequence: sales → production → materials/labour/overheads → cash → master. Present workings (High–Low segregation, stock reconciliations) *before* the final statement.
- **Cash budget** uses the receipts-and-payments columnar format, one column per sub-period, with **Opening + Receipts − Payments = Closing**, and the closing balance visibly carried forward. State non-cash exclusions explicitly (a one-line note "depreciation excluded" earns clarity marks). When a minimum balance and overdraft feature, show a distinct "balance before financing" line, then the financing line, then the closing balance.
- **Variance reports** show three columns — *Flexed Budget, Actual, Variance* — and mark each **F (favourable)** or **A (adverse)**; end with a total that **reconciles** to the sum of the parts. Never compare a *fixed* budget with actual for control.
- **Flexible budget** lists costs by behaviour (variable block, semi-variable block, fixed block) so the reader sees the structure; show **cost per unit** as a final row to expose the fixed-cost-spreading effect.
- **Ratios** should be shown to two decimals with the % sign, and accompanied by the one-line reconciliation Activity = Efficiency × Capacity — a quantified answer without interpretation loses the "comment" marks.
- **State your assumptions.** Where the question is silent (e.g. whether closing stock is a policy figure, whether a discount applies), write a one-line assumption. A clearly stated reasonable assumption is rewarded; a silent one that turns out different is not.

---

## 7. Connections to the Rest of the Syllabus

- **Standard Costing & Variance Analysis (the sister chapter).** A flexible budget *is* the bridge to variances. The "budget allowance for actual output" that anchors every material, labour and overhead variance is nothing but the flexed budget. Worked Example 3's ₹37,000 is a total cost variance waiting to be split into price/usage and efficiency components. Budgetary control operates on *whole departments and functions*; standard costing drills into *per-unit* detail — same philosophy, different resolution. The efficiency/capacity/activity ratios of Section 4.4a are literally the *fixed-overhead volume variance* decomposed into its efficiency and capacity sub-variances.
- **Marginal Costing & CVP.** Flexing depends entirely on the fixed/variable split — the identical cost behaviour classification underpinning contribution, break-even and the P/V ratio. The line "Total cost = Fixed + Variable × units" *is* the marginal-costing cost function.
- **Cost behaviour & segregation.** High–Low (and least-squares) segregation, learned here, is the same tool used across overhead analysis.
- **Budgetary control vs Standard costing distinction** is a favourite theory question: budgets set *overall* limits (extensive), standards set *per-unit* norms (intensive); budgets can exist without standards, standards need budgets to become a control system.
- **Working-capital & financial management.** The cash budget is the operational face of cash management and working-capital planning; the collection-pattern and creditor-lag mechanics reappear as the debtors/creditors cycles in the operating-cycle computation.
- **Activity-Based Costing.** Activity-based budgeting (Section 4.7) is ABC run forwards — driver rates set the budget instead of explaining the actual.

---

## 8. Traps & Examiner Tricks

1. **Comparing a fixed budget with actuals for control.** The single biggest conceptual error. If activity differs from plan, you *must* flex first. A question that gives a fixed budget and different actual output is *testing whether you know to flex.*
2. **Depreciation in the cash budget.** Depreciation is a cost but **never a cash flow.** Exclude it. If overheads are given "including depreciation," subtract it before entering payments (Worked Example 4: ₹30,000 − ₹8,000 = ₹22,000). The same applies to any accrued-but-unpaid expense.
3. **Timing lags — sales *made* vs cash *collected*, purchases *made* vs cash *paid*.** Enter cash when it moves, not when the transaction is booked. Machinery *bought* in May but *paid* in June is a June payment.
4. **Confusing material usage with material purchases.** Usage is driven by production; purchases differ by the change in raw-material stock. Two separate reconciliations (finished goods and raw material) are required.
5. **Forgetting the stock adjustment in the production budget.** Units to produce ≠ units to sell unless opening and closing FG stocks are equal. Add closing, subtract opening. And if closing stock is defined as "a fraction of *next* period's sales," look forward, not backward.
6. **Flexing fixed costs.** Fixed costs stay *fixed* when you flex — do **not** scale them with activity. Conversely, do not leave variable costs unflexed. The whole art is treating each behaviour correctly. (And a semi-variable cost must be split, not flexed whole.)
7. **Relevant range and step-ups.** Fixed costs are fixed only within a range; a huge jump in activity may push into a new range with stepped-up fixed costs. Read the data for such step-ups and switch the fixed figure at the boundary — do not copy one fixed number blindly across all activity columns.
8. **Sign and reconciliation discipline.** Label every variance F or A, and **prove** the individual variances sum to the total. An unreconciled answer signals an arithmetic slip.
9. **"Budget vs forecast."** A forecast predicts; a budget commits and is used for control. Theory questions probe this. Likewise "budget vs budgeting vs budgetary control" — know all three.
10. **Minimum cash balance.** When a minimum balance is specified, the answer is incomplete without commenting on **financing (overdraft)** or **investible surplus** relative to that floor — and, if borrowing is in stated multiples, round *up* to clear the floor.
11. **ZBB is not "starting the whole company from scratch."** It re-justifies *each activity* via decision packages and ranking; it is usually applied to discretionary costs and periodically, given its cost.
12. **High–Low endpoint error.** Choose the highest and lowest *activity* levels, never the highest and lowest *cost* figures; and beware an abnormal endpoint or a hidden fixed-cost step between the two points, which distorts the derived variable rate.
13. **Collection-pattern traps.** Apply cash discount to the *discount-taking* slice only (49%, not 50%, of that tail); let bad debts simply never be collected; and remember to *sum the overlapping tails* from several past months in each column.
14. **Wrong driver for a semi-variable/selling cost.** "2% of sales value" flexes against *sales value*, not units; selling overhead often keys off sales, production overhead off output. Flex each cost against its own driver.
15. **Principal budget factor mis-identification.** When two constraints are given, compute the output each permits and pick the *smaller*; do not assume sales is always the limiting factor.

---

## 9. First-Principles Recap

Strip everything away and rebuild:

1. A business is many managers deciding the future *today*, each dependent on the others. Left alone they produce an inconsistent plan. So we write one **priced, agreed plan — the budget** — to *coordinate*, *motivate*, and *control* (and to *delegate with control* via responsibility accounting).
2. Because resources are finite, we build the plan **starting from the scarcest resource** (the principal budget factor — usually sales, but test which constraint bites first). Everything else is sized to it, in a fixed sequence: sales → production → materials/labour/overheads → cash → master.
3. To *control*, the plan must become a fair yardstick. A **fixed** budget, frozen at one activity level, is unfair the moment activity moves — it mixes the *volume* effect with the *efficiency* effect. So we **flex** the budget to the activity that actually occurred, which demands splitting every cost into **fixed, variable, semi-variable** (and watching for **stepped** costs; High–Low segregates the mixed ones). Flexed budget vs actual = the *genuine* cost performance.
4. **Cash ≠ profit.** A separate **cash budget** tracks only real cash flows, timed when they move, excluding non-cash items like depreciation, so the firm foresees deficits and surpluses and arranges finance in advance — the chapter's one clear *feed-forward* instrument.
5. All functional budgets consolidate into the **master budget** — the board's approved plan and yardstick, split into an operating half and a financial half.
6. Performance can be read in *hours* through the **efficiency, capacity and activity ratios**, tied by Activity = Efficiency × Capacity.
7. When last year's base is itself suspect, **ZBB** rebuilds from zero, re-justifying every activity so inherited waste cannot survive; incremental budgeting is cheap but re-funds waste.
8. Finally, a budget is run by people, so its success turns as much on **behaviour** (participation, aspiration levels, slack) and its **limitations** as on the arithmetic.

Every formula in this chapter is a servant of one of these ideas. None was memorised; each was *needed*.

---

## 10. Quick-Revision Sheet

| Concept | Formula / Rule | Why it exists |
|---|---|---|
| Principal budget factor | The scarcest resource; build the budget starting here (usually sales); if two, pick the one permitting *less* output | Planning beyond the constraint creates inconsistency |
| Production budget (units) | Budgeted sales + Desired closing FG stock − Opening FG stock | Make enough for sales *and* the stock build, net of opening stock |
| Material usage budget | Units produced × material per unit | Consumption is driven by production |
| Material purchase budget (qty) | Material consumed + Desired closing RM stock − Opening RM stock | Buying differs from using by the change in RM stock |
| Material purchase (value) | Purchase quantity × price per unit | Drives cash outflow to suppliers |
| Direct labour budget | Units produced × hours per unit × wage rate; headcount = total hrs ÷ hrs per worker | Sizes workforce and wage cost |
| Flexible budget (total cost) | Total fixed cost + (Variable cost per unit × activity) | Re-computes cost at actual activity for fair control |
| High–Low variable rate | (Cost at high − Cost at low) ÷ (High units − Low units) | Segregates the variable slice of a semi-variable cost |
| High–Low fixed part | Total cost at a level − (Variable rate × units at that level) | Isolates the fixed lump |
| Semi-variable cost | Fixed part + (Variable rate × units); flex against its *own* driver | Must be split before flexing |
| Stepped fixed cost | Fixed within a band; jumps at the band boundary | Only "fixed" within the relevant range |
| Variance (control) | Flexed budget − Actual (mark F or A) | Compares like with like; excludes volume effect |
| Volume effect | Flexed budget − Fixed budget | The non-controllable cost of a different activity level |
| Efficiency ratio | Std hrs for actual output ÷ Actual hrs worked × 100 | How *well* the hours were worked |
| Capacity ratio | Actual hrs worked ÷ Budgeted hrs × 100 | How *much* of planned capacity was used |
| Activity ratio | Std hrs for actual output ÷ Budgeted hrs × 100 | Output vs plan; = Efficiency × Capacity |
| Cash budget | Opening balance + Receipts − Payments = Closing (chained) | Foresees cash surplus/deficit; profit ≠ cash |
| Cash budget — exclusions | Exclude depreciation and all non-cash/accrued items; time flows when cash moves | Only real bank movements matter |
| Cash collection with discount | First-tail collection = %-slice × (1 − discount); bad debts never collected | Reflects real cash received |
| Master budget | Consolidation of all functional budgets (budgeted P&L + Balance Sheet + cash); operating + financial halves | The board's single approved plan and yardstick |
| Incremental budgeting | Last year's figure + a % | Simple but re-funds past waste |
| Zero-based budgeting | Every activity justified from zero via decision packages, ranked and funded top-down | Kills inherited waste; ties spend to objectives |
| Budgetary control | Establish budgets → assign → compare actual vs budget → act/revise | Turns the plan into a running control system |
| Budget vs forecast | Forecast predicts; budget commits and controls | A budget is a decision, not a guess |

**Cost-behaviour reminder for flexing:** *Variable* — total moves with activity, per-unit constant. *Fixed* — total constant, per-unit falls as activity rises. *Semi-variable* — split into fixed lump + variable slice before use. *Stepped* — fixed within a band, jumps at the boundary.

**Golden control rule:** *Never* judge cost performance by comparing a fixed budget with actual results at a different activity level. Flex first; then, and only then, is the variance real.
