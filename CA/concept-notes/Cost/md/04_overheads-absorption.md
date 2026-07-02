# Chapter 04 — Overheads (Absorption Costing)

## 1. The Problem — the cost that refuses to attach itself to a product

Imagine you run a workshop that makes two things: heavy steel gates and delicate steel window grills. When a customer asks "what did *my* gate cost?", some answers are easy. You can walk to the steel rack, weigh the bars that went into that gate, and read the price tag. You can look at the job card and see the welder spent four hours on it at ₹150 an hour. Steel and welder wages are **direct** — they physically point at one gate. No argument possible.

But the workshop also incurs costs that stubbornly refuse to point at any single gate:

- The factory rent of ₹40,000 a month.
- The supervisor's salary of ₹30,000 — he watched over both gates and grills.
- Electricity of ₹18,000 running lights, cranes and machines.
- Depreciation on the welding machines, the grinder, the paint booth.
- Cotton waste, lubricants, small tools, the storekeeper's wages, the timekeeper.

These are **overheads** — indirect material + indirect labour + indirect expenses. The month's total is real money that must be recovered from customers or the business dies. Yet not one rupee of it announces which gate it belongs to. The rent does not shrink if you make one less gate this Tuesday. The supervisor's ₹30,000 is a single lump watching over hundreds of jobs.

Here is the managerial pain in one sentence: **the price you quote, the profit you report, and the "which product should we push?" decision all depend on a per-unit cost — but a huge slice of cost has no natural per-unit.** Financial accounting shrugs; it only needs the *total* factory cost for the P&L and one closing-stock figure. It never has to say what one gate cost. Cost accounting must, because a manager cannot quote a price on "the factory spent ₹1,08,000 this month."

So the entire machinery of this chapter exists to solve one decision-problem:

> **Given a pile of indirect cost that belongs to no single product, how do we fairly and defensibly load a slice of it onto each unit — so we can price, value stock, and judge product profitability?**

Everything that follows — allocation, apportionment, re-apportionment of service departments, overhead rates, under/over-absorption — is a step in dragging that shapeless pile of indirect cost down onto the cost of one gate.

---

## 2. The Core Idea — the restaurant bill split among friends

Six friends eat dinner. Three ordered individual dishes they can point to — that is *direct* cost, billed to the person. But the table shared two pizzas, a pitcher of juice, and the restaurant added a service charge and GST. Nobody "owns" the service charge. How do you split it?

You wouldn't split the shared items *equally per head* if one friend only sipped water — that's unfair. You look for a **fair basis**: split the pizza by slices eaten, the service charge in proportion to each person's own bill. You are searching for the driver that *causes* the shared cost, and you split in proportion to that driver.

That is the whole philosophy of overhead absorption:

1. **Allocation** — some shared costs actually do belong wholly to one table (a birthday cake ordered for table 4). Charge it there directly.
2. **Apportionment** — costs shared across tables (the AC electricity) are split among tables on a *fair basis* (floor area, number of diners).
3. **Absorption** — finally, each table's share is divided among the diners at that table so each person pays a per-plate amount.

Notice the two-stage descent: shapeless total → department → product. Overheads flow **from the whole factory, into cost centres, then into units**. Keep this staircase image in your head; the technical terms are just the named steps of this staircase.

*Figure 1 — the descent of overhead cost from a factory-wide pile down to a single unit.*

```mermaid
flowchart TD
    A["Total factory overheads for the period"] --> B["Cost centres via Allocation and Apportionment"]
    B --> C["Production Departments"]
    B --> D["Service Departments"]
    D -->|"Re-apportionment"| C
    C --> E["Individual product units via Absorption"]
    E --> F["Cost per unit for pricing and stock valuation"]
```

---

## 3. Why it's built this way — the logic behind the machinery

Before any formula, understand *why the method has the shape it has*. Four design decisions drive everything.

**Design decision 1 — Why go through departments at all? Why not dump total overhead ÷ total units?**
Because products don't consume the factory uniformly. A gate hogs the welding department; a grill hogs the assembly bench. If we averaged all overhead over all units blindly, the cheap-to-make grill would subsidise the machine-hungry gate, and vice versa. **Routing overhead through departments lets each product pick up cost only from the departments it actually passes through, and in proportion to how heavily it uses them.** Fairness requires the department detour.

**Design decision 2 — Why separate "production" from "service" departments?**
A production department (Machining, Assembly) directly works on the product — units flow through it, so units can absorb its cost. A **service department** (Stores, Maintenance, Canteen, Power House) never touches the product; it *serves the other departments*. Units cannot absorb Maintenance cost directly because no product "passes through" Maintenance. So service-department cost must first be pushed onto the production departments it serves, and only then reach the product. This is **secondary distribution / re-apportionment**, and it exists purely because service departments have no units of their own to soak up cost.

**Design decision 3 — Why an absorption *rate* fixed in advance?**
Because managers must quote prices *before* the month ends, when actual overhead and actual output are still unknown. You cannot tell a customer "come back on the 31st and I'll compute the real overhead." So we compute a **pre-determined rate** = *budgeted* overhead ÷ *budgeted* activity, and apply it to every job as it happens. Speed and consistency beat perfect accuracy. The price of using a pre-fixed rate is that it will never exactly match actuals — which is precisely the source of **under/over-absorption** (Section 4.6). That "error" is not a mistake; it is the unavoidable cost of being able to price in real time.

**Design decision 4 — Why choose the absorption *basis* carefully (labour hours vs machine hours vs %)?**
Because the basis is our theory of *what causes the overhead*. In a hand-welding shop, overhead rises with labour hours — so absorb on labour hours. In an automated CNC shop, overhead (power, depreciation, maintenance) rises with machine running time — so absorb on machine hours. Pick the basis that best mirrors cause-and-effect, or you systematically over-charge one product and under-charge another.

*Figure 2 — the two families of departments and why service cost must take a detour.*

```mermaid
graph LR
    S1["Stores"] --> P1["Machining"]
    S2["Maintenance"] --> P1
    S2 --> P2["Assembly"]
    S1 --> P2
    P1 --> U["Product units absorb here"]
    P2 --> U
    S1 -. "cannot reach units directly" .-> U
```

---

## 4. Full Technical Content

### 4.0 Vocabulary — nail these three verbs first

| Term | Meaning | Test to identify it |
|---|---|---|
| **Allocation** | Charging the *whole* of an overhead item to *one* cost centre, because it was incurred *wholly* for that centre. | "Can I trace 100% of this item to one department?" If yes → allocate. E.g. salary of the Machining foreman → Machining. |
| **Apportionment** | Splitting an overhead item that is *common* to several cost centres among them on a *fair basis*. | "Is this shared by many departments?" If yes → apportion. E.g. factory rent shared by all departments on floor-area. |
| **Absorption** | Charging the overhead of a *production* department onto the *units/jobs* passing through it, via an overhead rate. | The final step: department overhead → per unit. |

Mnemonic: **Allocate whole, Apportion shared, Absorb into units.** Allocation and apportionment together are called **primary distribution**. Re-apportionment of service departments is **secondary distribution**.

### 4.1 Classification recap — what counts as overhead

Overhead = **Indirect Material + Indirect Labour + Indirect Expenses**. It is classified three ways, and the exam expects you to know *why each classification exists*:

- **By function:** Factory (works) OH, Administration OH, Selling & Distribution OH. *Why:* different functions are recovered differently — factory OH goes into product cost and stock; S&D OH does not touch stock, it is charged when goods are sold.
- **By behaviour:** Fixed, Variable, Semi-variable. *Why:* only variable OH truly changes with output; fixed OH per unit is a fiction that depends on volume — the seed of under/over-absorption.
- **By element/control:** Controllable vs uncontrollable at a given level. *Why:* for responsibility accounting — you only blame a manager for what he can control.

### 4.2 Primary distribution — building the overhead distribution summary

**The task:** take every item of factory overhead and spread it across *all* cost centres (production + service) using allocation where possible and apportionment (on a fair basis) where not.

**Choosing the apportionment basis — the "why" behind each:**

| Overhead item | Fair basis of apportionment | Reason (cause-and-effect) |
|---|---|---|
| Rent, rates, building repairs, building depreciation | Floor area (sq. ft.) | Space consumed causes the cost |
| Lighting, heating | Floor area or number of light points | Roughly space-driven |
| Power / electricity (machine) | HP × machine hours, or metered KWH | Machine load causes power draw |
| Depreciation, insurance of plant | Capital value of plant / machinery | Costlier plant depreciates more |
| Supervision, canteen, welfare, ESI, PF, labour welfare | Number of employees | People-driven cost |
| Stores service, material handling | Value or weight of materials issued | Material throughput drives it |
| Indirect wages, general OH | Direct wages / direct labour hours | Labour intensity |

**The Primary Distribution Summary** is a table: rows = overhead items, columns = departments, plus a Basis column. Allocated items sit in one column; apportioned items are split across columns by the ratio.

### 4.3 Secondary distribution — re-apportioning service departments

Now the service-department totals (from primary distribution) must be pushed onto production departments, because units can only absorb from production departments. There are four methods; the exam favours the last two.

**(a) Direct re-distribution method.** Service department cost is apportioned *only to production departments*, ignoring service-to-service usage. Simplest, least accurate. Use when the question says to ignore inter-service work.

**(b) Step-ladder (step) method.** Rank service departments by how many others they serve (the one serving the most goes first). Re-apportion the first service department to *all* remaining departments (production **and** the other service departments), then the next, and so on — but once a service department is "closed," nothing comes back to it. Handles one-way service but not mutual service.

**(c) Reciprocal service methods — for mutual service.** When service departments serve *each other* (Maintenance services the Power House, and the Power House powers Maintenance), we need to recognise the two-way flow. Two techniques:

- **Simultaneous equation method** — set up an equation for each service department's *total* cost = its own primary cost + share received from the other service department(s). Solve the simultaneous equations, then distribute the solved totals to production departments. Best for exactly two service departments.
- **Repeated distribution method** — keep re-apportioning the service departments' balances back and forth across *all* departments in the given ratios, round after round; the service-department figures shrink each cycle until they are negligible (round off). Best when there are two or more mutually-serving service departments and the examiner says "repeated distribution."

*Figure 3 — decision tree for which secondary-distribution method to use.*

```mermaid
flowchart TD
    A["Do service departments serve each other?"] -->|"No"| B["Do they serve other service depts one-way?"]
    A -->|"Yes mutual"| C["Reciprocal method needed"]
    B -->|"No"| D["Direct re-distribution"]
    B -->|"Yes one-way"| E["Step ladder method"]
    C --> F["Exactly two service depts"]
    C --> G["Two or more service depts"]
    F --> H["Simultaneous equations"]
    G --> I["Repeated distribution"]
```

**Simultaneous equation setup (the reasoning).** Let X and Y be the *final total* overhead of the two service departments after they absorb each other's share. If department X's own primary overhead is a, and it receives p% of Y, then:

```
X = a + p·Y
Y = b + q·X
```

Substitute and solve. The logic: X's true cost isn't just its own — it includes the slice Y dumps onto it, which itself depends on X. That circularity is exactly what the simultaneous equations untangle.

### 4.4 Absorption — turning department overhead into a per-unit rate

Once every production department holds its full overhead (own + service share), we absorb it into units. **Overhead absorption rate:**

```
Overhead Absorption Rate = Overhead of the production department ÷ Total quantity of the chosen base
```

The six standard bases, each with its "when to use it and why":

| Method | Formula | Use when / why |
|---|---|---|
| **1. Percentage of Direct Material cost** | (Prod OH ÷ Direct Material) × 100 | Rarely fair — material price swings distort it; only if material and OH move together |
| **2. Percentage of Direct Wages** | (Prod OH ÷ Direct Wages) × 100 | When labour rates are uniform and time-driven OH dominates; simple but ignores that a high-paid worker isn't slower |
| **3. Percentage of Prime Cost** | (Prod OH ÷ Prime Cost) × 100 | Blends the flaws of the two above; seldom ideal |
| **4. Labour Hour Rate** | Prod OH ÷ Direct Labour Hours | **Best for labour-intensive** work — OH driven by *time* spent, not wage rate |
| **5. Machine Hour Rate** | Prod OH ÷ Machine Hours | **Best for machine-intensive** work — power, depreciation, maintenance track running time |
| **6. Rate per Unit of output** | Prod OH ÷ Units produced | Only when output is *homogeneous* (one product) |

**Why labour-hour and machine-hour rates are preferred:** overhead is fundamentally *time-related* (rent accrues by the hour, depreciation by usage, supervision by shift-length). Money-based bases (% of material/wages) get distorted by price fluctuations that have nothing to do with overhead consumption. Time-based rates track the real cause.

**Machine Hour Rate — the composite build-up.** MHR is often built by summing standing charges and running charges per machine hour:

- *Standing / fixed charges* (rent, supervision, insurance for the machine) → apportioned to the machine, then ÷ machine hours.
- *Machine expenses* (power, depreciation, repairs) → per machine hour directly.

MHR = (Standing charges per hour) + (Machine expenses per hour). This is the "**comprehensive machine hour rate**" if it also loads the operator's wages and setup.

### 4.5 Blanket rate vs Departmental rate — one rate or many?

A **blanket (single) overhead rate** = total factory overhead ÷ total factory base (e.g., total labour hours), one rate for the *whole* factory.

A **departmental rate** = a *separate* rate for each production department.

**Why departmental rates are almost always better:** a blanket rate is only fair if *every* product spends the *same proportion* of time in *every* department. Real products don't. A gate that lives in the expensive Machining department but skips Assembly would, under a blanket rate, be undercharged (it dodges Machining's high rate) while a grill that lives in cheap Assembly gets overcharged. **Blanket rates are acceptable only when there is a single product, or all products flow uniformly through all departments.** Otherwise use departmental rates. This is examinable as a theory question — know the one-line justification.

### 4.6 Under- and Over-absorption — the inevitable gap, and what to do with it

Because we absorb using a **pre-determined rate** (budgeted OH ÷ budgeted activity) but reality delivers **actual OH** and **actual activity**, the amount absorbed almost never equals the actual overhead incurred.

```
Overhead absorbed = Pre-determined rate × Actual base achieved
Under/Over absorption = Overhead absorbed − Actual overhead incurred
```

- If **absorbed > actual** → **over-absorption** (we loaded products with more OH than we actually spent; profit understated by cost accounts, needs adding back).
- If **absorbed < actual** → **under-absorption** (products didn't carry enough OH; profit overstated in cost accounts, needs charging).

**Why does the gap arise? Two independent causes — you must be able to name them:**
1. **Cost variance:** actual overhead spent ≠ budgeted overhead (spent more/less than planned).
2. **Volume variance:** actual activity (hours/units) ≠ budgeted activity — this alone moves the *fixed* overhead recovery, because the fixed OH per unit was calculated on budgeted volume.

**Treatment — three routes, and WHY each is chosen (ICAI):**

| Situation | Treatment | Reasoning |
|---|---|---|
| Small amount, due to *normal* reasons | Transfer to **Costing P&L Account** | Not worth re-working every cost; write off the normal, expected slippage |
| Large amount, due to *normal* reasons (wrong estimate of rate/volume) | Use a **supplementary rate** to adjust WIP, finished goods and cost of sales | The products were mis-costed; fairness demands going back and correcting stock values and cost of sales pro-rata |
| Any amount due to **abnormal** reasons (strike, fire, breakdown, idle capacity) | Transfer to **Costing P&L Account** | Abnormal costs must never distort product cost or stock; they are period losses |

**Supplementary rate** = amount of under/over-absorption ÷ actual base, applied to spread the correction across closing WIP + finished goods + cost of goods sold. Under-absorption → *positive* supplementary rate added to costs; over-absorption → *negative* rate deducted.

*Figure 4 — treatment logic for under/over-absorbed overhead.*

```mermaid
flowchart TD
    A["Under or Over absorption arises"] --> B["Is the cause abnormal e.g. strike fire idle capacity"]
    B -->|"Yes"| C["Write off to Costing Profit and Loss Account"]
    B -->|"No it is normal"| D["Is the amount large or small"]
    D -->|"Small"| E["Transfer to Costing Profit and Loss Account"]
    D -->|"Large"| F["Apply Supplementary Rate to WIP Finished Goods and Cost of Sales"]
```

---

## 5. Worked Examples

### Example 1 (warm-up) — Machine Hour Rate from first principles

**Problem.** A machine in the Machining department has the following annual data. Compute the machine hour rate.

- Cost of machine ₹2,40,000; scrap value ₹20,000; life 10 years.
- Rent of the department ₹36,000 p.a.; the machine occupies 1/4 of the floor area.
- Supervision ₹48,000 p.a.; the machine is 1 of 4 identical machines supervised.
- Power: machine consumes 5 units/hour at ₹6 per unit.
- Repairs & maintenance ₹11,000 p.a.
- The machine runs 2,200 hours a year (effective).

**Step 1 — sort each cost into standing charge or running charge, and get it per year.**

| Item | Amount to this machine (₹ p.a.) | Basis | Working |
|---|---|---|---|
| Depreciation | 22,000 | (Cost − scrap) ÷ life | (2,40,000 − 20,000)/10 |
| Rent | 9,000 | 1/4 of ₹36,000 (floor area) | 36,000 × 1/4 |
| Supervision | 12,000 | 1 of 4 machines | 48,000 × 1/4 |
| Repairs & maintenance | 11,000 | Allocated to this machine | — |
| **Total standing + fixed running (excl. power)** | **54,000** | | |

**Step 2 — standing/fixed charge per machine hour.**
= 54,000 ÷ 2,200 hours = **₹24.545 per hour**.

**Step 3 — power (a pure running charge) per hour.**
= 5 units × ₹6 = **₹30 per hour**.

**Step 4 — Machine Hour Rate.**
= 24.545 + 30 = **₹54.55 per machine hour** (rounded).

**Check:** total annual overhead recovered = 54.545 × 2,200 = ₹1,20,000, which equals fixed 54,000 + power (30 × 2,200 = 66,000) = ₹1,20,000. ✔ Reconciles.

---

### Example 2 (core) — Full primary + secondary distribution (repeated distribution + simultaneous equation)

**Problem.** A factory has two production departments **P1, P2** and two service departments **S1 (Stores)** and **S2 (Maintenance)**. Overheads and data:

| Overhead item | Amount (₹) | Basis |
|---|---|---|
| Rent | 20,000 | Floor area |
| Depreciation of plant | 30,000 | Value of plant |
| Supervision | 24,000 | Number of employees |
| Indirect materials | 6,000 | Allocated (given) |

Allocated indirect materials: P1 ₹2,500, P2 ₹2,000, S1 ₹900, S2 ₹600 (totals 6,000).

Departmental data:

| | P1 | P2 | S1 | S2 | Total |
|---|---|---|---|---|---|
| Floor area (sq. m) | 3,000 | 2,000 | 500 | 500 | 6,000 |
| Value of plant (₹'000) | 60 | 40 | 12 | 8 | 120 |
| Number of employees | 40 | 30 | 6 | 4 | 80 |

Service department usage (how each service dept's work is consumed):

- **S1 (Stores)** serves: P1 40%, P2 40%, S2 20%.
- **S2 (Maintenance)** serves: P1 30%, P2 40%, S1 30%.

Because S1 serves S2 *and* S2 serves S1, this is **mutual/reciprocal** service. We'll do the primary distribution, then solve by both **simultaneous equations** and **repeated distribution** to show they agree.

---

**Step 1 — Primary distribution summary.**

*Rent* by floor area 3000:2000:500:500 = 6:4:1:1 (of 12). 20,000/12 = 1,666.67 per part.
- P1 10,000; P2 6,666.67; S1 1,666.67; S2 1,666.67.

*Depreciation* by plant value 60:40:12:8 (of 120). 30,000/120 = 250 per unit.
- P1 15,000; P2 10,000; S1 3,000; S2 2,000.

*Supervision* by employees 40:30:6:4 (of 80). 24,000/80 = 300 per employee.
- P1 12,000; P2 9,000; S1 1,800; S2 1,200.

*Indirect materials* allocated: P1 2,500; P2 2,000; S1 900; S2 600.

| Item | Basis | P1 | P2 | S1 | S2 | Total |
|---|---|---|---|---|---|---|
| Rent | Floor area | 10,000.00 | 6,666.67 | 1,666.67 | 1,666.67 | 20,000 |
| Depreciation | Plant value | 15,000.00 | 10,000.00 | 3,000.00 | 2,000.00 | 30,000 |
| Supervision | Employees | 12,000.00 | 9,000.00 | 1,800.00 | 1,200.00 | 24,000 |
| Indirect material | Allocated | 2,500.00 | 2,000.00 | 900.00 | 600.00 | 6,000 |
| **Primary total** | | **39,500.00** | **27,666.67** | **7,366.67** | **5,466.67** | **80,000** |

Cross-check: 39,500 + 27,666.67 + 7,366.67 + 5,466.67 = **80,000**. ✔

---

**Step 2 — Secondary distribution by SIMULTANEOUS EQUATIONS.**

Let **S1** = total overhead of Stores after receiving Maintenance's share, and **S2** = total overhead of Maintenance after receiving Stores' share.

- S1 receives 30% of S2 (Maintenance gives 30% to Stores).
- S2 receives 20% of S1 (Stores gives 20% to Maintenance).

```
S1 = 7,366.67 + 0.30 S2      ...(i)
S2 = 5,466.67 + 0.20 S1      ...(ii)
```

Substitute (ii) into (i):
S1 = 7,366.67 + 0.30 (5,466.67 + 0.20 S1)
S1 = 7,366.67 + 1,640.00 + 0.06 S1
S1 − 0.06 S1 = 9,006.67
0.94 S1 = 9,006.67 → **S1 = 9,581.56**

Then S2 = 5,466.67 + 0.20 × 9,581.56 = 5,466.67 + 1,916.31 = **S2 = 7,382.98**.

**Now distribute the solved totals to production departments only** (each dept's share of the *whole* solved figure, using the given percentages):

Stores S1 = 9,581.56 → P1 40%, P2 40% (the 20% to S2 is already captured in the equations):
- To P1: 0.40 × 9,581.56 = 3,832.62
- To P2: 0.40 × 9,581.56 = 3,832.62

Maintenance S2 = 7,382.98 → P1 30%, P2 40%:
- To P1: 0.30 × 7,382.98 = 2,214.89
- To P2: 0.40 × 7,382.98 = 2,953.19

| | P1 (₹) | P2 (₹) |
|---|---|---|
| Primary total | 39,500.00 | 27,666.67 |
| From S1 (Stores) | 3,832.62 | 3,832.62 |
| From S2 (Maintenance) | 2,214.89 | 2,953.19 |
| **Total overhead** | **45,547.51** | **34,452.48** |

**Reconciliation:** 45,547.51 + 34,452.48 = **79,999.99 ≈ 80,000**. ✔ (rounding). The whole ₹80,000 has landed on the two production departments — exactly what secondary distribution must achieve.

---

**Step 3 — Verify by REPEATED DISTRIBUTION (same data).**

Start with service balances S1 = 7,366.67, S2 = 5,466.67 and keep re-apportioning until they vanish. Percentages: S1 → P1 40, P2 40, S2 20; S2 → P1 30, P2 40, S1 30.

| Round | P1 | P2 | S1 | S2 |
|---|---|---|---|---|
| Opening (primary) | 39,500.00 | 27,666.67 | 7,366.67 | 5,466.67 |
| Distribute S1 (7,366.67): 40/40/–/20 | +2,946.67 | +2,946.67 | (7,366.67) | +1,473.33 |
| S2 now = 5,466.67+1,473.33 = 6,940.00; distribute 30/40/30 | +2,082.00 | +2,776.00 | +2,082.00 | (6,940.00) |
| S1 now = 2,082.00; distribute 40/40/20 | +832.80 | +832.80 | (2,082.00) | +416.40 |
| Distribute S2 = 416.40: 30/40/30 | +124.92 | +166.56 | +124.92 | (416.40) |
| S1 = 124.92; distribute 40/40/20 | +49.97 | +49.97 | (124.92) | +24.98 |
| Distribute S2 = 24.98: 30/40/30 | +7.49 | +9.99 | +7.49 | (24.98) |
| S1 = 7.49; distribute 40/40/20 | +3.00 | +3.00 | (7.49) | +1.50 |
| Distribute S2 = 1.50 (round off to P1/P2) | +0.75 | +0.75 | — | (1.50) |
| **Totals** | **≈45,547.60** | **≈34,452.41** | 0 | 0 |

Both methods land P1 ≈ ₹45,548 and P2 ≈ ₹34,452, totalling ₹80,000. ✔ **The two reciprocal methods agree** — the small differences are pure rounding. This is your self-check discipline: if simultaneous equations and repeated distribution disagree by more than rounding, you made an arithmetic slip.

---

### Example 3 (exam-hard) — Absorption rate, application, and under/over-absorption with supplementary rate

**Problem.** Continuing the factory, department **P1** is **machine-intensive** and **P2** is **labour-intensive**. For the year:

| | P1 | P2 |
|---|---|---|
| Budgeted overhead (₹) | 45,548 | 34,452 |
| Budgeted machine hours | 22,000 | — |
| Budgeted labour hours | — | 17,000 |

At year-end, **actuals** turned out:

| | P1 | P2 |
|---|---|---|
| Actual overhead incurred (₹) | 48,000 | 33,000 |
| Actual machine hours | 21,000 | — |
| Actual labour hours | — | 18,000 |

Additional: of P1's under/over-absorption, ₹1,000 of the actual overhead excess was due to an **abnormal machine breakdown**. At year-end, output that carried P1's overhead sits as: Finished goods 60%, Closing WIP 15%, Cost of goods sold 25% (by absorbed-overhead value). Required: (a) absorption rates, (b) overhead absorbed, (c) under/over-absorption and its split into normal/abnormal, (d) treatment including a supplementary rate for the normal part in P1.

---

**Part (a) — choose base and compute pre-determined rates.**

P1 is machine-intensive → **Machine Hour Rate**:
Rate = 45,548 ÷ 22,000 = **₹2.0704 per machine hour**.

P2 is labour-intensive → **Labour Hour Rate**:
Rate = 34,452 ÷ 17,000 = **₹2.0266 per labour hour**.

*Why these bases:* P1's overhead (power, depreciation) tracks machine running time; P2's tracks operator time. Using the cause-driven base keeps each product's charge fair.

**Part (b) — overhead absorbed = pre-determined rate × ACTUAL base.**

- P1 absorbed = 2.0704 × 21,000 = **₹43,478.40**.
- P2 absorbed = 2.0266 × 18,000 = **₹36,478.80**.

**Part (c) — under/over-absorption = absorbed − actual.**

- P1: 43,478.40 − 48,000 = **−₹4,521.60 → UNDER-absorbed** (absorbed less than spent; products under-charged).
- P2: 36,478.80 − 33,000 = **+₹3,478.80 → OVER-absorbed** (absorbed more than spent).

*Split P1's under-absorption into normal and abnormal:*
- Abnormal (machine breakdown) = **₹1,000** of the actual overhead was abnormal.
- The abnormal portion of the under-absorption is that ₹1,000 (extra actual cost that should never touch product cost).
- Normal under-absorption = 4,521.60 − 1,000 = **₹3,521.60**.

**Part (d) — treatment.**

*Abnormal ₹1,000 (P1):* transfer straight to **Costing P&L Account** — abnormal losses must not distort stock or product cost.

*P2 over-absorption ₹3,478.80:* the question gives no abnormal cause and the amount is modest relative to overhead; treat as normal and transfer (credit) to **Costing P&L Account** (over-absorption increases costing profit). *Note:* if the examiner labelled it "significant," you would instead spread it via a negative supplementary rate.

*Normal under-absorption ₹3,521.60 (P1) — large, correct via SUPPLEMENTARY RATE across WIP + FG + COGS:*

Supplementary rate is applied on the absorbed-overhead value carried by each stock category. Split ₹3,521.60 in the ratio FG 60 : WIP 15 : COGS 25.

| Where P1 overhead sits | % | Additional charge (₹) | Working |
|---|---|---|---|
| Finished goods | 60% | 2,112.96 | 3,521.60 × 0.60 |
| Closing WIP | 15% | 528.24 | 3,521.60 × 0.15 |
| Cost of goods sold | 25% | 880.40 | 3,521.60 × 0.25 |
| **Total** | 100% | **3,521.60** | ✔ |

*Why spread it, not just write it off?* The ₹3,521.60 means every unit that passed through P1 this year was under-costed. Fairness (and true stock valuation) demands we go back and raise the cost of the units still in stock (FG + WIP) as well as those already sold (COGS). Writing the whole lot to P&L would leave closing stock understated — misstating both this year's profit and next year's opening cost.

**Final reconciliation of P1's ₹4,521.60 under-absorption:**
- Abnormal → P&L: 1,000.00
- Normal → supplementary rate (FG 2,112.96 + WIP 528.24 + COGS 880.40): 3,521.60
- **Total 4,521.60** ✔ Fully accounted for.

---

## 6. Presentation / Format — how to lay it out in the exam

1. **Primary Distribution Summary** — always a table: first column *Item*, second column *Basis of apportionment*, then one column per department (production first, service last), final *Total* column. Show the *ratio* of apportionment in the basis column (e.g., "Floor area 6:4:1:1"). Cross-total the last row and tick it against the grand total.
2. **Secondary Distribution** — continue the same table downward: add rows "Redistribution of S1," "Redistribution of S2." Put the department being closed in *brackets* (negative). End with a bold "Total overhead of production departments" row that must equal the grand total.
3. **Simultaneous equations** — write the two equations explicitly, show substitution, state S1 and S2 clearly before distributing.
4. **Overhead rates** — state the base chosen *and one line of justification* ("machine-intensive → machine hour rate"). Examiners award marks for the justification.
5. **Under/over-absorption** — always present as `Absorbed − Actual`, then label under vs over in words, then the treatment with reasoning.
6. Round money to two decimals; round the *last* repeated-distribution cycle to close service departments to nil.

---

## 7. Connections — where this sits in the wider syllabus

- **← Chapter 03 (Material & Labour):** direct material and direct labour were traceable; this chapter handles everything that *isn't* traceable. Prime cost (from Ch. 3) + factory overhead (this chapter) = **Works/Factory cost** in the cost sheet (Ch. 02).
- **→ Cost Sheet:** the absorbed factory overhead is the line that turns prime cost into works cost. Administration and S&D overheads (same allocation logic) come later in the sheet.
- **→ Job & Batch Costing:** the overhead absorption *rate* computed here is exactly what a job card uses to load overhead onto each job.
- **→ Standard Costing & Variance Analysis:** under/over-absorption is the seed of **fixed overhead volume and expenditure variances** — the "cost variance" and "volume variance" causes named in 4.6 become formal variances later.
- **→ Marginal Costing:** marginal costing *refuses* to absorb fixed overhead into product cost at all — understanding absorption here is what lets you appreciate the contrast (and the reconciliation of profits under the two systems).
- **→ Reconciliation of Cost & Financial Accounts:** under/over-absorbed overhead is a classic reconciling item between costing profit and financial profit.

---

## 8. Traps & Examiner Tricks

1. **Absorbed vs actual base confusion.** Overhead *absorbed* = pre-determined rate × **actual** base (not budgeted base). A very common slip is multiplying by budgeted hours. Pre-determined rate uses *budgeted* figures; application uses *actual* activity.
2. **Direction of under vs over.** Absorbed **>** actual = **over**-absorbed (add back to profit). Absorbed **<** actual = **under**-absorbed (charge to profit). Memorise via: "over-absorbed = we over-charged products = costing profit understated = credit P&L."
3. **Distributing the SOLVED service total, not the residual.** In the simultaneous-equation method, after solving S1 and S2, distribute the *full solved figure* using the original percentages to production departments. Students wrongly distribute only the primary total.
4. **Service-to-service percentages in reciprocal method.** The 20% Stores→Maintenance and 30% Maintenance→Stores must be *included* in the equations; they are the whole point. Dropping them silently converts it to the (wrong) direct method.
5. **Step method ordering.** Start with the service department that serves the *most* other departments (or has the largest overhead if tied), and never send cost back to a closed department.
6. **Abnormal causes always go to Costing P&L** — strike, fire, idle capacity, breakdown. Never spread abnormal amounts via a supplementary rate. Examiners plant an "abnormal" clause to test this.
7. **Supplementary rate must hit WIP too**, not just finished goods and COGS. Forgetting closing WIP is a classic error.
8. **Blanket rate justification.** If asked *when* a blanket rate is acceptable, the answer is "single product, or all products pass uniformly through all departments" — not "when it's convenient."
9. **Basis mismatch.** Depreciation apportioned on *floor area* (wrong) instead of *plant value* (right); supervision on plant value (wrong) instead of *employees* (right). Match the basis to the cost driver.
10. **Power apportionment.** Power is apportioned on **HP × machine hours** (or KWH), not on floor area or headcount — it is machine-load-driven.

---

## 9. First-Principles Recap

Strip away the vocabulary and this chapter is one idea stretched over four moves:

- **The core dilemma:** indirect cost is real money that points at no single product, yet managers need a per-unit cost to price and value stock. Financial accounting never faces this; cost accounting must.
- **Move 1 — Primary distribution.** Spread all factory overhead across every cost centre: *allocate* what belongs wholly to one, *apportion* the shared items on a basis that mirrors the cost's cause (area for rent, plant value for depreciation, headcount for welfare, machine-load for power).
- **Move 2 — Secondary distribution.** Service departments have no units to absorb their cost, so push them onto production departments. When services serve each other, untangle the circularity with simultaneous equations or repeated distribution — both must land the *entire* total on production departments and agree with each other.
- **Move 3 — Absorption.** Convert each production department's overhead into a per-unit rate using a *time-based* base (machine hours for machine-intensive, labour hours for labour-intensive) because overhead is fundamentally time-related. Use *departmental* rates unless products flow uniformly, in which case a blanket rate is tolerable.
- **Move 4 — Reconcile reality.** Because we priced with a pre-determined rate, absorbed ≠ actual. That gap (under/over-absorption) is not an error but the price of real-time pricing. Write off small/abnormal gaps to Costing P&L; correct large normal gaps with a supplementary rate across WIP, finished goods and cost of sales — because those units were genuinely mis-costed and stock values must be put right.

Every formula in the quick-revision sheet is just one of these four moves made arithmetic.

---

## 10. Quick-Revision Sheet

**Core flow:** Total OH → (Allocation + Apportionment = Primary) → Cost centres → (Re-apportionment = Secondary) → Production depts → (Absorption) → Units.

| Concept | Formula / Rule |
|---|---|
| Overhead | Indirect Material + Indirect Labour + Indirect Expenses |
| Allocation | Whole item → one centre (100% traceable) |
| Apportionment | Shared item → many centres on fair basis |
| **Absorption rate (general)** | Production dept overhead ÷ Total base quantity |
| % of Direct Material | (Prod OH ÷ Direct Material) × 100 |
| % of Direct Wages | (Prod OH ÷ Direct Wages) × 100 |
| % of Prime Cost | (Prod OH ÷ Prime Cost) × 100 |
| **Labour Hour Rate** | Prod OH ÷ Direct Labour Hours (labour-intensive) |
| **Machine Hour Rate** | Prod OH ÷ Machine Hours (machine-intensive) |
| Rate per unit | Prod OH ÷ Units produced (homogeneous output) |
| MHR build-up | Standing charges/hr + Machine running expenses/hr |
| **Overhead absorbed** | Pre-determined rate × **Actual** base |
| **Pre-determined rate** | Budgeted OH ÷ Budgeted base |
| **Under/Over absorption** | Absorbed − Actual overhead |
| → Over-absorbed | Absorbed > Actual (credit Costing P&L) |
| → Under-absorbed | Absorbed < Actual (debit Costing P&L) |
| **Supplementary rate** | Under/over amount ÷ Actual base; apply to WIP + FG + COGS |

**Apportionment bases (memorise the pairing):**

| Overhead | Basis |
|---|---|
| Rent, rates, building dep./repairs, lighting, heating | Floor area |
| Depreciation & insurance of plant | Value / capital of plant |
| Power | HP × machine hours (or KWH) |
| Supervision, canteen, welfare, ESI, PF | Number of employees |
| Stores / material handling | Value or weight of material issued |
| General / indirect wages | Direct wages or direct labour hours |

**Secondary distribution method chooser:**

| Situation | Method |
|---|---|
| Ignore inter-service work | Direct re-distribution |
| One-way service between service depts | Step-ladder |
| Mutual service, exactly 2 service depts | Simultaneous equations |
| Mutual service, 2+ service depts | Repeated distribution |

**Treatment of under/over-absorption:**

| Cause / size | Treatment |
|---|---|
| Abnormal (strike, fire, idle capacity, breakdown) | Costing P&L Account |
| Normal & small | Costing P&L Account |
| Normal & large | Supplementary rate → WIP + FG + COGS |

**Blanket rate acceptable only when:** single product OR all products pass uniformly through all departments; otherwise use **departmental rates**.

**Reciprocal simultaneous-equation template:** `S1 = a + p·S2 ; S2 = b + q·S1` → solve → distribute solved totals to production departments in given percentages. Always cross-check the total lands wholly on production departments and equals the primary grand total.
