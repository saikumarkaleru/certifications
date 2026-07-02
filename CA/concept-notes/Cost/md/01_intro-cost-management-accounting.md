# Chapter 01 — Introduction to Cost & Management Accounting

## 1. The Problem — A Decision Financial Accounting Refuses to Answer

Imagine you run **Deccan Cycles Ltd.**, a factory in Hyderabad making two models of bicycles: a *City* model and a *Racer* model. Your Chartered Accountant hands you the audited financial statements at year end. They are beautiful. They tell you the company earned a net profit of ₹42 lakh, that trade receivables stand at ₹1.8 crore, and that the balance sheet balances to the last rupee.

Now you sit across from that CA and ask five ordinary questions a manager must answer every single week:

1. A dealer will buy 500 City cycles but only if you drop the price to ₹4,200 each. Your "cost" per cycle in the accounts is ₹4,500. Do you refuse the order — or is ₹4,200 actually *profitable*?
2. The Racer line is "losing money." Should you shut it down? Will profit go *up* or *down* if you do?
3. Your foreman overspent on power this month. Was that his fault, or did the electricity board raise tariffs? Whom do you hold responsible?
4. You can either make brake-cables in-house or buy them from a vendor at ₹90. Which is cheaper — and cheaper by how much?
5. What price should you *quote* tomorrow for a custom order of 200 cycles that has never been made before?

The financial statements are **silent on every one of these.** They were never built to speak. Financial accounting (FA) looks *backward* at the business *as a whole*, aggregates everything into totals, and reports to *outsiders* (shareholders, tax authorities, lenders) under a legal framework (Companies Act, Accounting Standards). Its unit of analysis is the *entire entity over a past period*. That is exactly the wrong lens for the five questions above, because each question is about a **part** of the business (one product, one order, one department), looks *forward*, and is asked by an *insider* who can still change the outcome.

> **The problem cost accounting solves:** managers must make forward-looking decisions about *parts* of a business — pricing, product mix, make-or-buy, cost control, shutdown — and financial accounting, by design, delivers only backward-looking totals for the *whole*. We need a second accounting system whose entire purpose is to attach cost to the *right object* (a product, a job, a process, a department) at the *right time* and in the *right form* for the *specific decision at hand*.

This chapter builds the vocabulary and the classification logic of that second system. Every concept here exists because *some decision needs it*. If you ever catch yourself memorizing a classification without knowing which decision it serves, stop — you have missed the point.

---

## 2. The Core Idea — A Camera vs. an X-Ray, and a Wardrobe of Lenses

Financial accounting is a **group photograph** of the family taken once a year: everyone in one frame, smiling, verified, framed on the wall for visitors. It is truthful and complete — but you cannot use it to diagnose a broken bone.

Cost accounting is the **X-ray machine and the whole diagnostic lab.** It does not care about the pretty group photo. It cares about *this bone*, *this organ*, *this symptom*. It slices the business into thin cross-sections — this product, this batch, this hour of machine time — so a manager can *diagnose and act*.

But here is the deeper idea, the one that unlocks the whole subject:

> **Cost is not a single fixed number. It is a *number-for-a-purpose*. The same rupee of spending gets classified differently depending on the question you are asking.**

Think of cost data as raw light, and each *classification* as a different **lens** you snap onto the same camera:

- Want to trace cost to a product? Use the **direct / indirect** lens.
- Want to predict what happens if volume changes? Use the **fixed / variable** lens.
- Want to fix responsibility on a manager? Use the **controllable / uncontrollable** lens.
- Want to decide on a one-off order? Use the **relevant / sunk** lens.

There is no "true" classification of a factory rent or a foreman's salary in the abstract. There is only "how should I classify this *for the decision in front of me*." Master the wardrobe of lenses and *when to reach for each*, and cost accounting stops being a memory test and becomes a thinking tool.

---

## 3. Why It's Built This Way — The Logic Behind a Separate System

Why not just make financial accounting more detailed and be done with it? Because the *constraints* on FA are incompatible with the *needs* of decision-making. Look at the tensions:

| Constraint on FA | Why it blocks decisions | What cost accounting does instead |
|---|---|---|
| Must follow Accounting Standards / Companies Act | Rules optimize for comparability across firms, not usefulness to *this* manager | Free to use any method that aids the decision — no external rulebook |
| Reports the whole entity | Hides which product or department is the problem | Reports by cost centre / cost unit — the *part* |
| Historical, period-end | A decision is dead by the time year-end arrives | Continuous, real-time, and *future*-oriented (budgets, standards, estimates) |
| Records only actual transactions | A decision often hinges on cost *not* incurred (opportunity, notional) | Can bring in opportunity cost, notional rent/interest, imputed costs |
| Values inventory at total cost | Fine for the balance sheet, misleading for a shutdown or extra-order decision | Splits cost into fixed vs. variable so the *avoidable* part is visible |

The design principle is: **an information system must be shaped by the decision it feeds, not by an external compliance rulebook.** Since managers face many *different* decisions, cost accounting cannot offer one number; it must offer a *classified* number and the discipline to pick the right classification. That is why the beating heart of this whole subject is **cost classification** — and why the CA syllabus makes you learn *many* ways to slice the same cost.

Two definitions to anchor the vocabulary (ICAI, *Cost Accounting Standards / CAS-1*):

- **Cost** — the amount of expenditure (actual or notional) incurred on, or attributable to, a specified thing or activity. Note "notional": cost accounting can count sacrifices FA never records.
- **Costing** — the *technique and process* of ascertaining cost.
- **Cost Accounting** — the *formal application* of costing principles, methods and techniques to the process of determining and controlling costs.
- **Cost Accountancy** — the *widest* term: the science, art and practice of a cost accountant, embracing costing, cost accounting, budgetary control, cost control, and cost audit for managerial decision-making.

Nest these like Russian dolls: **Costing ⊂ Cost Accounting ⊂ Cost Accountancy**, with **Management Accounting** as the outermost layer that *uses* all of them plus financial data to actually advise management.

*Figure 3.1 — Cost concepts nest inside progressively wider disciplines; management accounting sits at the top and consumes the rest.*

```mermaid
flowchart TD
    A["Costing - the technique of ascertaining cost"] --> B["Cost Accounting - applying costing to determine and control cost"]
    B --> C["Cost Accountancy - science art and practice including budgeting and cost audit"]
    C --> D["Management Accounting - uses cost plus financial data to advise management on decisions"]
```

---

## 4. Full Technical Content — Every Concept Wrapped in Its Decision

### 4.1 The Elements of Cost — the raw material of every classification

Before we can slice cost cleverly, we need the three natural building blocks. Every rupee a factory spends is one of three **elements**:

1. **Material** — physical inputs (steel tubes, tyres, paint).
2. **Labour** — human effort (welders, painters, supervisors).
3. **Expenses** — everything else (power, rent, depreciation, royalty).

Each element then splits by *traceability* into **Direct** and **Indirect** (we justify this split in 4.2). Stacking the elements gives the famous cost build-up:

| Build-up stage | Formula | What it captures |
|---|---|---|
| **Prime Cost** | Direct Material + Direct Labour + Direct Expenses | The cost that *belongs* to the product directly |
| **Works / Factory Cost** | Prime Cost + Factory (Works) Overhead | Everything spent *inside* the factory |
| **Cost of Production** | Works Cost + Administration Overhead (production-related) | Cost of a finished, ready-to-sell unit |
| **Cost of Goods Sold** | Cost of Production ± Opening/Closing finished-goods stock | Cost of what actually *left* the door |
| **Cost of Sales / Total Cost** | COGS + Selling & Distribution Overhead | Full cost to get the product into a customer's hands |
| **Sales** | Total Cost + Profit (or − Loss) | The top line |

**Overhead** is simply the sum of all *indirect* costs (indirect material + indirect labour + indirect expenses). It is grouped by function into **Factory/Works**, **Administration**, and **Selling & Distribution** overhead — because a manager controlling the shop floor should not be judged on the sales team's advertising spend. *Function-wise grouping serves responsibility.*

### 4.2 Classification by Traceability — Direct vs. Indirect

> **Decision served:** "What did *this product / job* actually cost?" and "Which costs can I honestly *trace* versus which must I *spread*?"

- **Direct cost** — can be *conveniently and economically traced* to a specific cost object (a product, job, or process). Steel tubes going into a City cycle are direct material; the welder's wages on that line are direct labour; a design royalty paid per cycle is a direct expense.
- **Indirect cost (overhead)** — *cannot* be economically traced to one unit, so it must be *apportioned/absorbed* using some basis. The factory manager's salary, factory rent, and lubricating oil serve *many* products at once.

The dividing line is **convenience/economy of tracing, not physical importance.** Nails in furniture are physically part of the product but so cheap to track individually that we treat them as *indirect* material. The whole point is that direct costs give a *reliable* product cost, while indirect costs need a defensible *sharing rule* (covered in the Overheads chapter). Get the split wrong and every product-cost, price and mix decision downstream is polluted.

### 4.3 Classification by Behaviour — Fixed, Variable, Semi-Variable

> **Decision served:** "If I make 10% more (or fewer) units, what happens to cost — and therefore to profit?" This lens powers pricing, extra-order acceptance, break-even, and shutdown decisions. It is arguably the single most powerful lens in the subject.

Behaviour = how *total* cost reacts to changes in *activity level* (units, machine-hours) **within the relevant range**.

- **Variable cost** — total rises/falls *in proportion* to activity; *per-unit* stays constant. Direct material, direct wages (piece-rate), power for machines. Make zero cycles → zero material cost.
- **Fixed cost** — total stays *constant* regardless of activity (within the relevant range); *per-unit* falls as volume rises. Factory rent, manager's salary, straight-line depreciation. Whether you make 1 cycle or 1,000, the rent is ₹2,00,000.
- **Semi-variable (mixed) cost** — has both a fixed base and a variable slope. Electricity bill (fixed meter charge + per-unit usage), telephone, repairs. Must be *split* into its fixed and variable parts before use (via the **high-low method** or regression — detailed in the Marginal Costing chapter).

The counter-intuitive trap that behaviour explains: **fixed cost *per unit* is variable, and variable cost *per unit* is fixed.** Managers who reason on "cost per unit" without knowing behaviour make catastrophic pricing errors. That is *why* this lens exists — to stop you treating a fixed cost as if it changes with volume.

*Figure 4.1 — Total-cost behaviour against activity. Fixed cost is a flat line; variable cost is a ray from the origin; semi-variable starts at the fixed intercept and slopes up.*

```mermaid
graph LR
    subgraph Behaviour_of_total_cost_as_output_rises
    F["Fixed - flat line stays at same total"]
    V["Variable - straight line rising from zero"]
    S["Semi variable - starts above zero then rises"]
    end
```

### 4.4 Classification by Function / Attributability to the Period — Product vs. Period

> **Decision served:** "Which costs cling to the *unit* and sit in inventory until it is sold, and which costs expire with *time* and hit this period's profit regardless of sales?" This governs inventory valuation and the *timing* of profit.

- **Product cost (inventoriable)** — attaches to the product and is carried in inventory as an asset until the unit is sold. Under absorption costing this is *cost of production* (direct materials, direct labour, factory overhead). Unsold → sits on the balance sheet, not yet an expense.
- **Period cost** — relates to a *period*, not a *unit*; expensed in full when incurred. Selling, distribution and general administration costs (and, under *marginal* costing, *all* fixed overhead).

Why split them? Because *when* a cost becomes an expense changes reported profit. Load a cost into "product" and it can be parked in closing stock, deferring the hit; treat it as "period" and it bites now. This is the exact fault-line between **Absorption Costing and Marginal Costing** (a later chapter), and examiners love the profit *difference* it creates when stock levels change.

### 4.5 Classification by Controllability — Controllable vs. Uncontrollable

> **Decision served:** "Whom do I hold *responsible* for this variance?" This is the foundation of **responsibility accounting** and performance appraisal — answering our foreman question from Section 1.

- **Controllable cost** — can be *influenced* by the action of a *specified* manager within a *given* time span. A shop supervisor controls material wastage and idle time on his line.
- **Uncontrollable cost** — cannot be influenced by that manager at that level. The supervisor cannot control the *apportioned* head-office rent or a government tariff hike.

Two subtleties that make this an *exam favourite*:
1. **Controllability is relative to a level and a time horizon.** Factory rent is uncontrollable for the foreman but *controllable* for the CEO negotiating the lease. Almost everything is controllable by *someone* over a *long enough* horizon.
2. You judge a manager *only* on what he controls — otherwise you punish people for tariff hikes and monsoons, and the whole incentive system collapses.

### 4.6 Classification by Relevance to a Decision — Relevant, Sunk, Opportunity, Differential

> **Decision served:** *any specific one-off choice* — accept/reject an order, make-or-buy, keep/replace a machine, shut down a line. This is the "decision-making" cluster and the intellectual peak of the chapter.

The single test for **relevance**: *a cost is relevant only if it is a **future** cost that **differs between the alternatives**.* Anything else is irrelevant noise, however large.

- **Sunk cost** — cost *already incurred*, unrecoverable, *unaffected* by any future decision. The ₹8,00,000 you already spent on a machine is sunk; it must be **ignored** when deciding whether to replace it. The most common managerial fallacy ("we've invested too much to quit now") is exactly the failure to ignore sunk cost.
- **Opportunity cost** — the value of the *next-best alternative forgone*. If using a spare machine for Order A means you cannot rent it out for ₹15,000, that ₹15,000 is a real cost of Order A — even though *no cheque is written and FA never records it.* This is precisely the kind of "notional" cost only cost accounting captures.
- **Differential (incremental) cost** — the *difference in total cost* between two alternatives. If Plan X costs ₹5,00,000 and Plan Y ₹5,60,000, the differential cost of Y is ₹60,000. When it's a *rise* it's *incremental*; a *fall* is *decremental*.
- **Marginal cost** — the *additional* cost of producing *one more* unit; in practice equals *variable cost per unit* within the relevant range. Drives the "accept the ₹4,200 order?" decision.
- **Avoidable vs. unavoidable cost** — costs that *disappear* if an activity is dropped (avoidable → relevant to a shutdown) versus those that *continue* regardless (unavoidable → irrelevant to that decision).
- **Imputed / notional cost** — a hypothetical cost not involving cash outflow, inserted for better decisions or comparability (e.g., notional interest on owner's capital, notional rent on own building). It makes a debt-free unit comparable to a financed one.
- **Replacement cost** — cost to *replace* an asset/material at *current* market prices, versus original historical cost — relevant when deciding on reorder or valuation in inflationary times.
- **Out-of-pocket cost** — the portion involving *actual cash* outflow (excludes non-cash items like depreciation) — relevant to short-run cash-constrained decisions.

*Figure 4.2 — The relevance filter: a cost enters a specific decision only if it clears both gates.*

```mermaid
flowchart TD
    A["A cost item under consideration"] --> B{"Is it a future cost - not yet incurred"}
    B -->|"No - already spent"| S["SUNK - ignore it"]
    B -->|"Yes"| C{"Does the amount differ between the alternatives"}
    C -->|"No - same either way"| I["IRRELEVANT - ignore it"]
    C -->|"Yes"| R["RELEVANT - include it in the decision"]
    R --> O["Remember to add opportunity cost of resources used"]
```

### 4.7 Cost Centres and Cost Units — *where* and *per what* we collect cost

You cannot classify cost until you decide *where* to pool it and *per what* to express it. Two structural concepts:

**Cost Centre** — a *location, person, item of equipment, or group thereof* for which costs are *ascertained and controlled*. It is the *smallest segment of activity* for which costs are accumulated. It answers "*where* was the cost incurred / who is answerable?" Types:

- **Personal cost centre** — a *person* or group of persons (a works manager, a sales team).
- **Impersonal cost centre** — a *location or equipment* (a machine, a department, a delivery van).
- **Production cost centre** — where actual production/conversion happens (machining, assembly, welding shop).
- **Service cost centre** — supports production but does no conversion itself (stores, maintenance, canteen, boiler house). Its cost is *re-apportioned* to production centres.

A related, wider idea is the **Responsibility Centre**, where a manager is accountable for defined items:
- **Cost centre** — responsible for *costs* only.
- **Profit centre** — responsible for *costs and revenues* (hence profit).
- **Investment centre** — responsible for costs, revenues *and* the *capital invested* (judged on ROI).

*Why the hierarchy exists:* you localize cost to the smallest sensible unit so that control and responsibility can be pinned precisely (ties straight back to 4.5 controllability).

**Cost Unit** — the *unit of product or service* to which costs are ascertained, i.e., the *unit of measurement* of cost. It answers "*per what* do we express cost?" It must be the natural unit customers and managers think in:

| Industry | Typical cost unit |
|---|---|
| Cement / Steel / Sugar | per tonne |
| Automobile / Cycle | per vehicle / per cycle |
| Electricity | per kilowatt-hour (kWh) |
| Transport (goods) | per tonne-kilometre |
| Passenger transport | per passenger-kilometre |
| Hospital | per patient-day / per bed-day |
| Hotel | per room-day |
| Gas | per cubic metre |
| Brick-making | per 1,000 bricks |
| Professional services | per chargeable hour |

Notice several are **composite units** (tonne-km, passenger-km, patient-day): they combine *two* dimensions because a single dimension would mislead — moving 1 tonne 100 km is not the same effort as moving 100 tonnes 1 km, yet both are "100 tonne-km." *The unit is chosen to make cost comparisons fair.*

*Figure 4.3 — Cost flows through centres and is finally expressed per cost unit.*

```mermaid
flowchart LR
    M["Cost incurred as Material Labour Expenses"] --> SC["Service cost centres - stores maintenance"]
    M --> PC["Production cost centres - machining assembly"]
    SC -->|"re-apportioned"| PC
    PC --> CU["Absorbed into the Cost Unit - one bicycle"]
```

### 4.8 Methods vs. Techniques of Costing — a two-axis map

Students constantly confuse these. They are *orthogonal* — you pick one **method** *and* one-or-more **techniques** simultaneously.

**Methods** answer *"how is production organized, so how do we collect cost?"* The method is dictated by the **nature of the product/industry**, and you do not get to choose it freely.

| Method | When used | Cost object |
|---|---|---|
| **Job costing** | Distinct, custom jobs to order | Each job |
| **Batch costing** | Identical items made in batches (pharma tablets, cycles in lots) | Each batch (then ÷ units) |
| **Contract costing** | Large, long-duration, site-based jobs (construction) | Each contract |
| **Process costing** | Continuous mass production, output homogeneous (chemicals, sugar, paint) | Each process; cost averaged over output |
| **Operating (Service) costing** | Services, not products (transport, hospital, power) | The service cost unit (per km, per bed-day) |
| **Single/Output costing** | One product, continuous (mining, cement) | Per tonne / unit |
| **Multiple/Composite costing** | Product assembled from many components (car, cycle, TV) | Blend of the above |

*Job/Batch/Contract are all "specific order" costing; Process/Operating are "continuous operation" costing.* The dividing question is: **is output made to a specific customer order (→ specific-order methods) or produced continuously in a stream (→ process/operating)?**

**Techniques** answer *"what principle do we apply to the collected cost, for control or decision-making?"* You *choose* the technique to suit the *managerial purpose*, and you can overlay it on *any* method.

| Technique | Purpose it serves |
|---|---|
| **Absorption (Total/Full) costing** | Charge *all* costs (fixed + variable) to units — needed for inventory valuation & external reporting |
| **Marginal (Variable) costing** | Charge only *variable* cost to units, treat fixed as period cost — for decisions (pricing, mix, make-or-buy) |
| **Standard costing** | Set predetermined costs and analyse *variances* — for control |
| **Budgetary control** | Plan via budgets and compare actuals — for planning & control |
| **Uniform costing** | Common costing principles across firms — for inter-firm comparison |
| **Historical costing** | Ascertain cost *after* it is incurred |

**The mental model:** *Method* is chosen by the **product** (given to you); *Technique* is chosen by the **decision** (chosen by you). A cycle-maker uses **batch costing (method)** and may apply **standard + marginal costing (techniques)** on top. A hospital uses **operating costing (method)** with **budgetary control (technique)**.

*Figure 4.4 — Costing splits into methods driven by product nature and techniques driven by managerial purpose.*

```mermaid
flowchart TD
    Root["Costing Systems"] --> Met["METHODS - fixed by product nature"]
    Root --> Tec["TECHNIQUES - chosen by managerial purpose"]
    Met --> SO["Specific order - Job Batch Contract"]
    Met --> CO["Continuous - Process Operating Output"]
    Tec --> Val["For valuation - Absorption costing"]
    Tec --> Dec["For decisions - Marginal costing"]
    Tec --> Ctrl["For control - Standard costing and Budgetary control"]
```

---

## 5. Worked Examples — From Warm-Up to Exam-Hard

### Worked Example 1 (Easy) — Building a Cost Sheet from Elements

**Data (Deccan Cycles, City model, for the month):** Direct material consumed ₹6,00,000; Direct wages ₹2,40,000; Direct expenses (design royalty) ₹60,000; Factory overhead ₹1,80,000; Administration overhead (production-related) ₹90,000; Selling & distribution overhead ₹1,10,000; Profit margin: 20% on sales. Units produced and sold: 400 cycles. **Prepare the cost sheet and find the selling price per cycle.**

**Step 1 — Prime Cost:** Direct Material + Direct Labour + Direct Expenses = 6,00,000 + 2,40,000 + 60,000 = **₹9,00,000**.

**Step 2 — Works (Factory) Cost:** Prime Cost + Factory OH = 9,00,000 + 1,80,000 = **₹10,80,000**.

**Step 3 — Cost of Production:** Works Cost + Admin OH = 10,80,000 + 90,000 = **₹11,70,000**. (No opening/closing WIP or finished stock given, so Cost of Production = COGS.)

**Step 4 — Cost of Sales (Total Cost):** COGS + S&D OH = 11,70,000 + 1,10,000 = **₹12,80,000**.

**Step 5 — Profit and Sales.** Profit is 20% *on sales*, so cost is 80% of sales. Sales = Total Cost ÷ 0.80 = 12,80,000 ÷ 0.80 = **₹16,00,000**. Profit = 16,00,000 − 12,80,000 = ₹3,20,000 (check: 20% × 16,00,000 = 3,20,000 ✓).

| Cost Sheet — City model (400 cycles) | Total (₹) | Per cycle (₹) |
|---|---:|---:|
| Direct Material | 6,00,000 | 1,500 |
| Direct Wages | 2,40,000 | 600 |
| Direct Expenses | 60,000 | 150 |
| **Prime Cost** | **9,00,000** | **2,250** |
| Factory Overhead | 1,80,000 | 450 |
| **Works Cost** | **10,80,000** | **2,700** |
| Administration Overhead | 90,000 | 225 |
| **Cost of Production / COGS** | **11,70,000** | **2,925** |
| Selling & Distribution OH | 1,10,000 | 275 |
| **Cost of Sales** | **12,80,000** | **3,200** |
| Profit (20% on sales) | 3,20,000 | 800 |
| **Sales** | **16,00,000** | **4,000** |

**Selling price = ₹4,000 per cycle.** Every subtotal reconciles top-to-bottom.

---

### Worked Example 2 (Medium) — The Special-Order Decision (Relevant Cost in Action)

Recall Section 1's dilemma. The *accounts* say each City cycle "costs" ₹3,200 (cost of sales) or ₹2,925 (cost of production). A dealer offers **₹4,200 each for 500 extra cycles**, a one-off export order that needs **no selling & distribution effort** (dealer collects at the gate). Current output is *within* capacity, so no new fixed costs arise. **Should you accept?**

**The wrong answer** (the trap): "Cost is ₹3,200, price is ₹4,200 — but wait, are all costs covered? The order price ₹4,200 > full cost ₹3,200, accept." Right conclusion here, but often the price offered is *below* full cost and the naïve manager wrongly *rejects*. The discipline is to use **relevant cost only.**

**Step 1 — Identify cost behaviour** from Example 1's per-cycle figures. Classify each as variable (changes with the extra 500 units) or fixed (won't change within capacity):

| Element | Per cycle (₹) | Behaviour | Relevant to extra order? |
|---|---:|---|---|
| Direct Material | 1,500 | Variable | Yes |
| Direct Wages | 600 | Variable | Yes |
| Direct Expenses (royalty per cycle) | 150 | Variable | Yes |
| Factory Overhead (assume fixed) | 450 | Fixed | **No** — capacity already paid for |
| Administration OH | 225 | Fixed | **No** |
| Selling & Distribution OH | 275 | Fixed/avoided here | **No** — dealer collects |

**Step 2 — Relevant (marginal) cost per cycle** = 1,500 + 600 + 150 = **₹2,250** (this equals Prime Cost because only the direct/variable elements are relevant).

**Step 3 — Incremental analysis for 500 cycles:**

| | Per cycle (₹) | 500 cycles (₹) |
|---|---:|---:|
| Incremental revenue | 4,200 | 21,00,000 |
| Less: Relevant (marginal) cost | 2,250 | 11,25,000 |
| **Incremental contribution / profit** | **1,950** | **9,75,000** |

**Decision: ACCEPT.** The order adds **₹9,75,000** to profit. The ₹450 factory OH, ₹225 admin OH and ₹275 S&D per cycle are **irrelevant** (fixed/sunk within capacity). Had you judged against full cost ₹3,200 you'd still accept here — but the *method* is what matters: if the offer had been ₹2,800 (below ₹3,200 full cost but above ₹2,250 marginal cost) the naïve manager rejects and *loses* ₹550 × 500 = ₹2,75,000 of contribution. *This is exactly the decision FA cannot make and cost classification exists to enable.*

**Caveat to state in an exam:** valid only if (a) spare capacity exists, (b) the export price won't leak into the domestic market and spoil the ₹4,000 price, and (c) no better alternative use of capacity exists (else add its **opportunity cost**).

---

### Worked Example 3 (Exam-Hard) — Shutdown, Sunk Cost & Opportunity Cost Combined; plus a Composite Cost Unit

**Part A — Product-line shutdown.** Deccan's *Racer* line shows this annual statement, and the board wants to *drop* it because it "loses ₹1,20,000":

| Racer line (per annum) | ₹ |
|---|---:|
| Sales (2,000 cycles @ ₹5,000) | 1,00,00,000 |
| Less: Variable costs (@ ₹3,400/cycle) | 68,00,000 |
| **Contribution** | **32,00,000** |
| Less: Fixed costs charged to line | 33,20,000 |
| **Reported "loss"** | **(1,20,000)** |

Of the ₹33,20,000 fixed costs, **₹21,00,000 is apportioned head-office/common cost** that will *continue* even if the Racer line closes (unavoidable), and only **₹12,20,000 is specific to the Racer line** and would be *saved* on closure (avoidable). A machine currently used by the Racer line could, if the line closes, be **rented out for ₹2,50,000 p.a.** (opportunity cost of keeping the line running). Two years ago the company spent **₹40,00,000** developing the Racer design. **Should the line be shut down?**

**Step 1 — Discard the sunk cost.** The ₹40,00,000 design spend is *sunk* — already incurred, unrecoverable, identical under "keep" or "close." **Ignore it entirely.** (The classic "we spent 40 lakh, we can't quit" fallacy is precisely what we must resist.)

**Step 2 — Identify what actually changes on closure (relevant items only):**

| On shutting the Racer line | ₹ |
|---|---:|
| Contribution *lost* (foregone) | (32,00,000) |
| Specific/avoidable fixed cost *saved* | 12,20,000 |
| Rental income *gained* (opportunity now realised) | 2,50,000 |
| **Net change in profit if shut down** | **(17,30,000)** |

**Step 3 — Decision.** Shutting down makes the company **₹17,30,000 *worse* off** per year. The apportioned ₹21,00,000 common cost continues either way, so the "₹1,20,000 loss" is an *accounting artefact* of arbitrary apportionment. **Keep the Racer line running.** Proof by rebuilding total profit both ways:

| Company profit impact of the Racer line | Keep (₹) | Close (₹) |
|---|---:|---:|
| Contribution from Racer | 32,00,000 | 0 |
| Rent income (machine) | 0 | 2,50,000 |
| Specific fixed cost | (12,20,000) | 0 |
| Common fixed cost (continues regardless) | (21,00,000) | (21,00,000) |
| **Net effect** | **(1,20,000)** | **(18,50,000)** |

Keeping the line leaves the firm ₹17,30,000 better off (−1,20,000 vs −18,50,000). Reconciles with Step 2. **The line stays.** *Notice how four classifications — variable/fixed, avoidable/unavoidable, sunk, and opportunity — had to work together for one decision.*

**Part B — Choosing and computing a composite cost unit (Operating costing).** Deccan runs a delivery lorry to ship cycles to dealers. In a month it makes the trips below; running cost for the month is **₹96,000**. Management wants the **cost per tonne-kilometre** (the fair unit, because it captures *both* load and distance).

| Trip | Distance one way (km) | Load carried outward (tonnes) | Return load (tonnes) |
|---|---:|---:|---:|
| A | 40 | 6 | 0 (empty) |
| B | 60 | 5 | 2 |
| C | 30 | 8 | 4 |

**Step 1 — Decide the unit.** A plain "per km" would reward driving far with a light load; "per tonne" ignores distance. The **tonne-km** (tonnes × km) fairly measures haulage effort — *that is why operating costing uses composite units.*

**Step 2 — Compute effective tonne-km** (each leg = load on that leg × its distance; the return distance equals the outward distance):

| Trip | Outward tonne-km | Return tonne-km | Total |
|---|---:|---:|---:|
| A | 6 × 40 = 240 | 0 × 40 = 0 | 240 |
| B | 5 × 60 = 300 | 2 × 60 = 120 | 420 |
| C | 8 × 30 = 240 | 4 × 30 = 120 | 360 |
| **Total** | | | **1,020** |

**Step 3 — Cost per tonne-km** = Total running cost ÷ Total tonne-km = 96,000 ÷ 1,020 = **₹94.12 per tonne-km** (to 2 dp).

This single figure lets management benchmark the lorry month-on-month, decide freight quotes, and compare against a third-party transporter — *decisions the financial P&L's lump "transport expense ₹96,000" could never support.*

---

## 6. Presentation & Format — How to Lay It Out in the Exam

**Cost-sheet discipline (memorise the skeleton, understand each subtotal):**

- Always run *elements → prime → works → production → COGS → cost of sales → sales*, showing **bold subtotals** at Prime, Works, Production and Cost of Sales.
- Show a **Total (₹)** column and, when units are given, a **Per-unit (₹)** column. Per-unit fixed costs will differ across volumes — flag that.
- **Adjust stocks at the right level:** raw-material stock adjusts *before* prime cost (opening + purchases − closing = consumed); **WIP** adjusts at *works cost*; **finished-goods** stock adjusts *after* cost of production to reach COGS.
- **Direction of stock adjustment:** *add opening, subtract closing.*
- Keep a "*Less:*" / "*Add:*" prefix on every adjusting line so the marker can follow the arithmetic.

**Decision-statement discipline (for relevant-cost problems):**

- Head the statement *"Statement showing Relevant/Incremental Cost"* — never mix in sunk or apportioned-fixed lines except to explicitly *exclude* them with a note.
- Work in **contribution** (Sales − Variable cost) for mix/shutdown/extra-order questions, then handle fixed cost separately as avoidable vs. unavoidable.
- Always **state your assumptions** (spare capacity, no market spoilage, opportunity cost included) — examiners award marks for the caveats.

**Operating-costing discipline:** define the cost unit first, build the *composite* quantity in a table, then divide total cost by total units. Show the tonne-km / passenger-km build-up explicitly.

---

## 7. Connections — Where This Chapter Feeds the Rest of the Syllabus

- **Elements → Material, Labour, Overheads chapters.** The direct/indirect split opened here becomes the machinery of stock valuation (FIFO/weighted average), labour incentive schemes, and overhead absorption rates.
- **Fixed/Variable → Marginal Costing & CVP.** Behaviour analysis is the entire foundation of contribution, break-even, margin of safety, and the make-or-buy and mix decisions.
- **Product/Period + Absorption → Marginal vs. Absorption reconciliation.** The period-cost cut you learned here *is* the reason the two systems report different profits when stock changes.
- **Controllable/Uncontrollable → Standard Costing & Budgetary Control.** Variance analysis only makes sense once you can say *who could have controlled it.*
- **Relevant/Sunk/Opportunity → Decision-Making chapter.** Examples 2 and 3 are miniatures of the full special-order, make-or-buy, and shutdown problem sets.
- **Cost centres → Overheads & Reconciliation.** Service-centre re-apportionment (repeated distribution, simultaneous equations) rests on the centre taxonomy defined here.
- **Methods → Job/Batch/Process/Contract/Operating chapters**, each of which is a *deep dive* into one row of the methods table in 4.8.

Cost accounting also **reconciles** with financial accounting (a dedicated chapter): the two profits differ because of items FA records but cost accounting excludes (pure financial income/expense like dividends, interest on investments) and notional items cost accounting includes (notional rent/interest). This chapter's *"why they're separate"* is the conceptual root of that reconciliation.

---

## 8. Traps & Examiner Tricks

1. **"Cost per unit" without behaviour.** If a question gives a per-unit cost at one volume and asks for total cost at another volume, you must *strip out* the fixed portion — fixed cost per unit is *not* constant. This is the number-one silent trap.
2. **Treating apportioned (common) fixed cost as avoidable in shutdown problems.** Only *specific/avoidable* fixed cost is relevant to closure. Common cost that continues is irrelevant — see Example 3.
3. **Including sunk cost.** Past R&D, historical machine cost, already-paid deposits — all sunk. Any solution that lets them influence a *future* decision is wrong.
4. **Forgetting opportunity cost.** If a scarce resource used by an option could earn elsewhere, that foregone earning is a *real* relevant cost even though no cash moves. Examiners plant a "could be rented / could make another product" clue precisely to test this.
5. **Direct vs. indirect by importance, not traceability.** Glue and thread are physically essential yet *indirect* because tracing them per unit is uneconomic. Don't be fooled by physical prominence.
6. **Confusing method with technique.** "Deccan should use marginal costing" — marginal is a *technique*, not a method. The *method* (batch) is fixed by the product. State both correctly.
7. **Composite-unit arithmetic.** In tonne-km / passenger-km, remember the *return leg* and any *empty running* — a lorry going back empty earns *zero* tonne-km for that leg but still costs money; that's what pushes up cost per effective tonne-km.
8. **Stock adjustment at the wrong level.** WIP adjusts at *works* cost, finished goods at *production* cost. Swapping them corrupts COGS.
9. **Profit "on cost" vs. "on sales."** 20% *on sales* ≠ 20% *on cost*. On sales: Sales = Cost ÷ 0.80. On cost: Sales = Cost × 1.20. Read the wording.
10. **Controllability without a level/time frame.** Never label a cost "uncontrollable" absolutely — always relative to *this manager* over *this period*.

---

## 9. First-Principles Recap

Strip everything away and rebuild from one seed: **managers make forward decisions about parts of a business, and financial accounting only reports backward totals for the whole.** From that single gap, everything in this chapter follows by necessity:

- Because decisions concern *parts*, we localize cost to **cost centres** and express it **per cost unit**.
- Because different decisions need different cuts of the same rupee, cost is not one number but a **number-for-a-purpose**, sliced by **classifications** — and *each classification exists to serve a specific decision*:
  - trace product cost → **direct/indirect**;
  - predict cost as volume moves → **fixed/variable/semi-variable**;
  - value inventory and time profit → **product/period**;
  - fix responsibility → **controllable/uncontrollable**;
  - choose between alternatives → **relevant vs. sunk, opportunity, differential, marginal**.
- Because industries organize production differently, the *collection framework* is a **method** (job, batch, process, operating…), fixed by the product.
- Because managers pursue different purposes, the *analytical principle* laid over any method is a **technique** (absorption, marginal, standard, budgetary), chosen by the decision.

If you can, for any cost item, answer *"which lens, and for which decision?"* — you have understood this chapter. The formulas are just the bookkeeping of that understanding.

---

## 10. Quick-Revision Sheet

**Cost build-up (learn cold):**

| Stage | Formula |
|---|---|
| Prime Cost | Direct Material + Direct Labour + Direct Expenses |
| Works (Factory) Cost | Prime Cost + Factory Overhead (± opening/closing WIP) |
| Cost of Production | Works Cost + Admin Overhead |
| Cost of Goods Sold | Cost of Production + Opening FG − Closing FG |
| Cost of Sales | COGS + Selling & Distribution Overhead |
| Sales | Cost of Sales + Profit |
| Overhead | Indirect Material + Indirect Labour + Indirect Expenses |
| Contribution | Sales − Variable Cost |

**Profit-margin conversions:** Profit 20% *on sales* → Sales = Cost ÷ 0.80. Profit 20% *on cost* → Sales = Cost × 1.20.

**Classifications and the decision each serves:**

| Classification | Split | Decision it enables |
|---|---|---|
| Traceability | Direct / Indirect | Product costing; overhead absorption |
| Behaviour | Fixed / Variable / Semi-variable | Pricing, break-even, extra-order, shutdown |
| Period-attach | Product / Period | Inventory valuation; timing of profit |
| Controllability | Controllable / Uncontrollable | Responsibility accounting; appraisal |
| Relevance | Relevant / Sunk / Opportunity / Differential / Marginal | Make-or-buy, accept order, replace, shutdown |

**Decision rules:**
- Relevant cost = *future* cost that *differs* between alternatives. Ignore sunk. Add opportunity cost.
- Accept special order if **price > marginal cost** *and* spare capacity exists (and no market spoilage).
- Shutdown: compare **contribution lost** vs **avoidable fixed cost saved + opportunity gains**. Ignore apportioned common cost.

**Cost centre types:** Personal / Impersonal; Production / Service. **Responsibility centres:** Cost, Profit, Investment.

**Composite cost units:** tonne-km (transport-goods), passenger-km (transport-passenger), patient-day (hospital), room-day (hotel), kWh (electricity).

**Methods (product-driven):** Job · Batch · Contract · Process · Operating/Service · Single/Output · Multiple/Composite.
**Techniques (purpose-driven):** Absorption · Marginal · Standard · Budgetary Control · Uniform · Historical.

**One-line memory hook:** *Method is chosen by the product; Technique is chosen by the decision; Classification is chosen by the question.*
