<!-- v2-deep -->

# Chapter 06 — Cost Sheet

## 1. The Problem — the manager's question that financial accounts cannot answer

Imagine you run *Sunrise Cycles*, a factory making bicycles. At the year-end your financial accountant hands you a Profit & Loss Account. It says: *Sales ₹80,00,000, all expenses ₹68,00,000, Profit ₹12,00,000.* You nod. But then a dealer walks in and asks a question that makes the P&L useless:

> "I want to place an order for 500 special-frame cycles. What price will you quote me?"

Turn to the P&L for the answer and you are stranded. The P&L tells you the **result of the past** — one lump profit for everything sold. It cannot tell you:

- What did **one** cycle cost to make?
- Of that cost, how much was **material**, how much **labour**, how much **factory overhead**, how much **office and selling** expense?
- If I make 500 more, which costs will **rise** and which stay flat?
- At what price do I stop *losing* money and start *making* it?

The financial P&L is organised by **nature** (salaries, rent, depreciation, purchases) and lumps the whole business together. A manager needs cost organised by **function and by unit** — material vs labour vs overhead, factory vs office vs selling, and ultimately *per cycle*. That reorganisation, laid out as a vertical statement that builds cost stage by stage up to profit, is the **Cost Sheet**.

**The decision the Cost Sheet enables:** pricing a quotation, judging whether a product is profitable, controlling each element of cost by watching it separately, valuing closing stock for the balance sheet, and comparing this period against the last. Every line of the format below exists because some manager needed one of those answers.

**Three definitions worth fixing at the outset** (the examiner tests the distinction):

- A **Cost Sheet** is a statement showing the *build-up of cost of a product/service* for a period, element by element and stage by stage. It is a **memorandum statement** — it is *not* part of the double-entry ledger, so it has no debit/credit sides.
- A **Cost Statement** is the same thing under a slightly broader name (ICAI uses the two interchangeably; some texts call the columnar output with per-unit figures a "Statement of Cost").
- A **Production Account / Cost of Production Statement** *is* a ledger account (double-entry) that also arrives at cost of production but is presented in account form. The Cost Sheet is its readable, columnar cousin. If a question says "prepare a Cost Sheet," never present a T-account.

**Why the Cost Sheet is historical *and* prospective.** A *historical* cost sheet records what a period actually cost (used for control and stock valuation). An *estimated* cost sheet projects what a future job will cost (used for quotations and tenders — see Example 3 and Example 5). Same skeleton, different data source. The examiner loves to hand you a historical sheet and then ask you to build an estimated one from it — that single pivot is the most valuable skill in the chapter.

---

## 2. The Core Idea — building a wall, brick by brick

Think of total cost not as one number but as a **wall built in courses (layers)**. You cannot lay the roof before the walls, and you cannot lay the walls before the foundation. Cost accumulates in exactly that disciplined order:

- **Foundation** = the direct, traceable costs of *making the thing* — the raw material you can point to, the wages of the person who touched it, any expense incurred specifically for that job. Together they are the **Prime Cost**.
- **Ground floor** = add the *factory's* indirect costs (the supervisor, factory rent, machine power). Now you have **Works / Factory Cost**.
- **First floor** = add the *office's* cost of administering production. Now you have **Cost of Production**.
- **Roof** = add *selling and distribution* cost. Now you have **Cost of Sales**.
- **The sky above the roof** = whatever the customer pays *over* Cost of Sales is **Profit**; Cost of Sales + Profit = **Sales**.

Each course rests on the one below because each answers a *different manager's question*. The factory manager is judged on Works Cost. The sales manager is judged on selling cost. The MD is judged on the final profit. By stacking the wall in named layers, the Cost Sheet lets each manager see *his own brick* — and lets you quote a price that covers *every* brick.

**The four "cost" milestones you must be able to name on sight** (examiners test the vocabulary directly):

| Milestone | What it is | Alternative name |
|---|---|---|
| **Prime Cost** | All direct costs (DM + DL + DE) | Basic / First / Flat Cost |
| **Works Cost** | Prime + factory OH ± WIP | Factory / Manufacturing Cost |
| **Cost of Production** | Works Cost + admin OH | Office Cost / Gross Cost of Production |
| **Cost of Sales** | Cost of goods sold + S&D OH | Total Cost |

*Figure 1 — the cost wall: each layer adds one function's cost until the customer's price sits on top.*

```mermaid
flowchart TD
    A["Direct Material + Direct Labour + Direct Expenses"] --> B["PRIME COST"]
    B --> C["Add Factory Overheads"]
    C --> D["WORKS or FACTORY COST"]
    D --> E["Add Administration Overheads"]
    E --> F["COST OF PRODUCTION"]
    F --> G["Adjust Finished Goods Stock"]
    G --> H["COST OF GOODS SOLD"]
    H --> I["Add Selling and Distribution Overheads"]
    I --> J["COST OF SALES"]
    J --> K["Add Profit"]
    K --> L["SALES"]
```

---

## 3. Why it is built this way — the logic behind the staircase

Three design principles explain every feature of the Cost Sheet. Understand these and you never memorise the format again — you *reconstruct* it.

**(a) Direct before indirect — because traceability drives control.**
A cost is *direct* if you can economically trace it to one unit (the steel in a frame). It is *indirect* (an overhead) if it is shared and must be *apportioned* (the factory's electricity bill). Direct costs move automatically with volume and are controlled at the shop floor; overheads are controlled by budgets and absorption rates. Separating them at the very first stage (Prime Cost = all directs) is what makes cost *controllable*.

*A deeper cut on "direct":* directness is a matter of **economic traceability, not physical presence**. The glue in a chair is physically in the product yet is treated as indirect material because tracing it per chair costs more than it is worth. Conversely, a hired mould used on one job is physically *outside* the product yet is a direct expense because it is wholly traceable to that job. The test is always "can I trace this to one cost unit without disproportionate effort?" — never "is it inside the product?"

**(b) Function follows the physical journey of the product — because responsibility follows function.**
A product is born in the **factory**, is administered by the **office**, and is pushed to the customer by **selling & distribution**. The Cost Sheet adds overheads in that same sequence — factory → admin → selling — so that each functional manager owns exactly the layer he can influence. This is why Works Cost is struck *before* admin cost: the works manager should not be blamed for the MD's office rent.

**(c) Stock is the timing bridge — because *produced* is not the same as *sold*.**
Here is the subtle heart of the chapter. The factory *produces* a quantity in a period; the sales team *sells* a possibly different quantity. Cost must be matched to the **stage at which the goods physically are**:

- **Raw material stock** sits *before* production, so it is adjusted inside the material line, *before* Prime Cost.
- **Work-in-progress (WIP)** sits *inside* production, so it is adjusted at the *factory* stage — after factory overheads, as we compute Works Cost.
- **Finished goods stock** sits *after* production, so it is adjusted *after* Cost of Production, to convert "cost of goods **produced**" into "cost of goods **sold**".

Each stock is inserted at the exact rung where the goods physically rest. Get the *rung* right and the whole sheet reconciles. Get it wrong and every number below is contaminated. This single rule — **match each stock to its stage** — is the most-tested idea in the chapter.

**The valuation principle behind each stock** (the deeper "why"): a stock is *always* valued at the cost of the stage it has *reached*, never a stage it has not.

- Raw material stock is valued at **purchase cost** (it has been bought but not processed).
- WIP is valued at **works-stage cost** — material + labour + factory overhead absorbed so far (it is inside the factory). This is why WIP enters *after* factory overheads: it already carries a share of them.
- Finished goods are valued at **cost of production per unit** (they have exited the factory and been administered but not yet sold — no selling cost is loaded onto stock, because selling cost is *not incurred until sale*).

That last point is a favourite trap: **selling & distribution overhead is never carried in closing finished-goods stock.** A unit sitting in the warehouse has cost you to *make and administer*, but you have not yet *sold* it, so no selling cost attaches. Load selling cost only onto the units actually sold.

*Figure 2 — where each stock adjustment enters the staircase.*

```mermaid
flowchart LR
    RM["Opening plus Purchases minus Closing RAW MATERIAL"] --> P["Material Consumed"]
    P --> PC["Prime Cost"]
    PC --> WIP["Opening plus current minus Closing WIP"]
    WIP --> WC["Works Cost"]
    WC --> COP["Cost of Production"]
    COP --> FG["Opening plus produced minus Closing FINISHED GOODS"]
    FG --> CGS["Cost of Goods Sold"]
```

---

## 4. Full Technical Content — the formulas, each with its "why"

### 4.1 The elements of cost (the vocabulary)

| Element | Direct (traceable) | Indirect / Overhead (shared) |
|---|---|---|
| **Material** | Direct Material — steel, tyres, forms part of the product | Indirect Material — lubricants, cotton waste, small tools |
| **Labour** | Direct Labour — wages of machine operator, welder | Indirect Labour — supervisor, storekeeper, sweeper |
| **Expenses** | Direct (Chargeable) Expenses — hire of a special mould for one job, royalty per unit, design cost for a specific order | Indirect Expenses — factory rent, power, office salaries, advertising |

> **Direct Material + Direct Labour + Direct Expenses = PRIME COST.**
> **All indirects = OVERHEADS**, later split by function into Factory, Administration, and Selling & Distribution.

**The two classifications the exam layers on top of this.** The same rupee of cost can be cut two ways at once, and the Cost Sheet uses *both*:

- **By element** — material / labour / expense (the columns of the table above).
- **By function** — production / administration / selling & distribution (the *stages* of the staircase).
- **By behaviour** — fixed / variable / semi-variable (this cut does *not* appear on a traditional cost sheet; it belongs to Marginal Costing, §7. But examiners test whether you know that a *classified* or *behavioural* cost sheet re-sorts the same totals into fixed and variable columns.)
- **By controllability** — controllable / uncontrollable (used for responsibility reporting, not the sheet itself).

Keeping "element" and "function" separate in your head is what lets you place a mystery item: *indirect wages of a factory supervisor* is **labour** by element but sits in the **factory overhead** stage by function.

### 4.2 Stage 1 — Direct Material Consumed (why the RM stock lives here)

You bought material during the year, but you did not necessarily *use* all of it, and some was left over from last year. The cost sheet needs what was **consumed**, not what was purchased:

```
Raw Material Consumed
  = Opening Stock of Raw Material
  + Purchases of Raw Material
  + Carriage/Freight Inward on material
  + Import duty, octroi, insurance on incoming material
  − Purchase returns / trade discount
  − Closing Stock of Raw Material
```

*Why here?* Material is consumed at the very start of the process, so its stock adjustment belongs *before* Prime Cost. Carriage **inward** is added because it is a cost of *bringing material in* — part of its acquisition cost. (Carriage *outward* is a selling cost and appears far below.)

**What counts as part of material cost (and what does not) — the CAS-6 view.** The *cost of material* is its purchase price *net of trade discount, rebate, duty drawback and refundable taxes* (like GST input credit), *plus* all costs of bringing it to the factory door — freight inward, insurance in transit, loading/unloading, octroi/entry tax, and normal transit loss. **Exclude** from material cost: cash discount (financial), demurrage/detention/penalties (abnormal), and any refundable tax you will reclaim. This "net purchase price + bringing-in cost" rule is exactly why import duty and carriage inward are *added* while GST credit and trade discount are *deducted*.

**Two material subtleties the examiner plants:**

1. **Normal vs abnormal loss of material.** Normal (unavoidable) process loss is absorbed by the *good* units — it silently raises the per-unit cost and needs no separate line. Abnormal loss (fire, theft, careless spillage) is stripped out of the cost sheet and charged to Costing P&L, so it does not inflate product cost.
2. **Materials Consumed vs Materials Purchased vs Materials Issued.** "Consumed" = opening + purchases − closing (the cost-sheet figure). If a question gives "materials issued to production" it may already be the consumed figure — read carefully before re-adjusting stock.

### 4.3 Stage 2 — Prime Cost

```
Prime Cost = Direct Material Consumed + Direct Labour (Wages) + Direct Expenses
```

*Why struck separately?* Prime Cost is the "hard core" of traceable cost — the part a foreman can control unit-by-unit. It is also the base on which some factories absorb overheads (percentage-of-prime-cost method).

**Direct labour — the pieces that belong here.** Direct wages include basic wages of production workers *plus* the production-worker share of dearness allowance, production bonus, and overtime *at normal rate*. Two classic tweaks:

- **Overtime premium** (the *extra* over the normal rate). If overtime is worked at the customer's request for a specific job → the premium is a **direct expense** of that job. If it is due to general factory pressure → the premium is **factory overhead**. If it is due to abnormal causes (making up for a flood shutdown) → **Costing P&L**. Only the *premium* is reclassified; the normal-rate element of overtime stays in direct wages.
- **Idle-time wages.** Normal idle time (unavoidable — tea breaks, machine set-up) is treated as factory overhead (or loaded into the direct-labour rate). Abnormal idle time (strike, power failure) → Costing P&L, never the cost sheet.

### 4.4 Stage 3 — Works / Factory Cost (why WIP stock lives here)

```
Gross Works Cost   = Prime Cost + Factory (Works) Overheads
Factory Cost       = Gross Works Cost + Opening WIP − Closing WIP
```

**Factory overheads** = indirect material + indirect wages + factory rent, power, fuel, depreciation of plant, factory insurance, works manager's salary, etc.

*Why is WIP adjusted here and nowhere else?* WIP means goods **partly through the factory** — material and labour and some overhead have been incurred but the unit is not finished. That is precisely the *works stage*. So opening WIP (last period's half-done units, now being finished) is added and closing WIP (this period's half-done units) is removed **after** factory overheads have gone in, because WIP already carries a share of factory overhead.

**The one genuine ambiguity — WIP valued at prime cost vs works cost.** ICAI's standard position (and the safe default) is that WIP already carries factory overhead, so it is adjusted **after** factory overheads (as above). But *some* problems explicitly value WIP at **prime cost only**. If so, the WIP adjustment must be made **before** adding factory overheads, i.e. between Prime Cost and factory OH. *Rule to state in your answer:* "WIP has been adjusted after factory overheads on the assumption it is valued at works cost; if it were valued at prime cost the adjustment would precede factory overheads." Naming the assumption earns the mark even if the examiner intended the other treatment.

> **Common adjustment — sale of scrap:** scrap arising in the factory is a *recovery* of factory cost. Its sale value is **deducted** from factory overheads (or from Works Cost) before striking Factory Cost.

**Defectives, spoilage and by-products at the works stage** (finer distinctions):

- **Normal spoilage** cost is borne by good units (no separate line). **Abnormal spoilage** → Costing P&L.
- **Rectification cost of normal defectives** is added to factory overhead; abnormal-defective rectification → Costing P&L.
- **By-product** net realisable value is *deducted* from factory/works cost (like scrap but usually larger) unless the question asks for a separate by-product costing.

### 4.5 Stage 4 — Cost of Production

```
Cost of Production = Factory Cost + Administration Overheads (relating to production)
```

**Administration overheads** = office rent, office salaries, office lighting, printing & stationery, directors' remuneration, audit fees, legal charges — the cost of *running the office that administers production*.

*Why after Works Cost?* Administration is a level *above* the shop floor; conceptually you cannot administer production until production exists. (ICAI convention charges general administration here; some purist syllabi treat admin as a period cost — for CA Inter, include production-related admin at this stage unless told otherwise.)

**Gross vs net cost of production — the R&D and quality-cost refinement.** ICAI (per CAS-4/CAS-6 thinking) sometimes distinguishes:

```
Gross Cost of Production      = Factory Cost + Administration OH (production)
Add: Opening stock of finished goods
Less: Closing stock of finished goods
= Cost of Goods Sold
```

Where a question separates **research & development cost** attributable to production, or **quality-control cost**, add it here at the production stage (it is a cost of *making the product to standard*), not at selling. General/head-office administration unrelated to production is, strictly, a period cost — but for CA Inter default, keep all administration at this stage unless the question explicitly splits it.

### 4.6 Stage 5 — Cost of Goods Sold (why finished-goods stock lives here)

```
Cost of Goods Sold (COGS)
  = Cost of Production
  + Opening Stock of Finished Goods
  − Closing Stock of Finished Goods
```

*Why here — the crux?* Cost of Production is the cost of everything **produced** this period. But we only match cost against **sales**. Some produced units remain unsold (closing FG stock) and must be carried out; some units sold this period were produced *last* period (opening FG stock) and must be brought in. Adjusting FG stock *after* Cost of Production converts "cost of goods **produced**" into "cost of goods **sold**." This is the timing bridge between production and sales.

> **Valuing the FG stock:** unless told otherwise, closing finished goods are valued at the **current period's Cost of Production per unit** = Cost of Production ÷ units produced. Opening FG is valued at *last* period's rate (given in the problem).

**The units-produced vs units-sold reconciliation (do this whenever FG stock exists).** When a problem gives you units, always run the physical identity first:

```
Units sold = Opening FG units + Units produced − Closing FG units
```

This tells you *how many* units the sales figure covers, and lets you value closing FG at the *right* per-unit rate. If the question also gives closing-FG *value* directly, use it; if it gives only *quantity*, value it at current cost of production per unit. Mixing the two — valuing closing FG at cost of *sales* per unit, for instance — is a guaranteed error, because a unit in stock has not been sold and so carries no selling cost.

**FIFO assumption on finished goods.** Cost sheets assume **FIFO** on finished goods unless told otherwise: the opening stock is sold first (at last period's rate), and closing stock consists of the *most recently produced* units (at this period's rate). This is why opening FG carries last year's rate and closing FG carries this year's.

### 4.7 Stage 6 — Cost of Sales, and Profit

```
Cost of Sales = COGS + Selling & Distribution Overheads
Profit        = Sales − Cost of Sales
Sales         = Cost of Sales + Profit
```

**Selling & distribution overheads** = salesmen's salaries and commission, advertising, carriage **outward**, warehouse of finished goods, showroom rent, bad debts, packing for delivery.

*Why last?* Selling cost is incurred only when you *push the finished good to the customer* — the final leg of the product's journey.

**Selling vs distribution — the sub-split some questions demand.** *Selling* overheads create/stimulate demand: advertising, salesmen's salary and commission, showroom rent, catalogues, samples, bad debts. *Distribution* overheads move the finished good to the buyer *after* the sale: carriage outward, warehouse of finished goods, packing for delivery, running the delivery van, secondary transport. When a question asks for a functional break-up, keep the two sub-heads distinct; otherwise merge them into "Selling & Distribution."

**Packing — the trap.** *Primary packing* essential to the product's saleability (e.g. the tube of toothpaste's carton) is a **production/works** cost; *secondary/transport packing* to move goods to the customer is a **distribution** cost. Same word "packing," two different stages depending on purpose.

### 4.8 The two-sided margin relationships (the pricing engine)

For tenders and quotations you must convert between cost, profit, and sales. Master these:

| If profit is a % **on cost** | If profit is a % **on sales** |
|---|---|
| Profit = Cost × rate | Profit = Sales × rate |
| Sales = Cost × (1 + rate) | Cost = Sales × (1 − rate) |
| e.g. 25% on cost → Sales = 1.25 × Cost | e.g. 20% on sales → Cost = 0.80 × Sales |

**Interconversion trick:** profit that is *x%* on cost equals *x / (100 + x) %* on sales; profit that is *y%* on sales equals *y / (100 − y) %* on cost. (Example: 25% on cost = 25/125 = 20% on sales.)

**A ready reckoner you can rebuild instantly** (verify each by the trick above):

| Stated margin | Equivalent margin |
|---|---|
| 10% on cost | 9.09% on sales (10/110) |
| 20% on cost | 16.67% on sales (20/120) |
| 25% on cost | 20% on sales (25/125) |
| 33⅓% on cost | 25% on sales (33.33/133.33) |
| 50% on cost | 33⅓% on sales (50/150) |
| 100% on cost | 50% on sales |

**"On which base?" — read the exact words.** "Profit is 25% *of* cost" and "profit is 25% *on* cost" both mean cost-based. "Profit is 25% *of* selling price / *on* sales / *of* turnover" is sales-based. "Margin of 25%" with no base named is ambiguous — state your assumption ("taken as % on sales, being the trade convention for 'margin'") and proceed. Also watch **"mark-up"** (always on cost) vs **"margin"** (usually on selling price).

### 4.9 What is EXCLUDED from a Cost Sheet (pure-cost principle)

The Cost Sheet records only costs of the *product/operation*. It **excludes** all *financial* and *appropriation* items:

- Financial items: interest on loans/debentures, dividends paid, income-tax, loss/profit on sale of assets, transfer to reserves.
- Purely notional gains and non-operating income (interest received, rent received, dividend received).
- Abnormal losses (abnormal wastage, cost of idle time due to strike) — charged to Costing P&L, not the Cost Sheet.
- Cash discount (a financial item). *Trade discount*, however, is netted off purchases/sales.

*Why?* Cost Accounting isolates the *cost of making and selling*, so that decisions are not distorted by how the business is *financed* or *taxed*.

**A fuller exclusion checklist** (the examiner scatters these among genuine costs to see if you spot them):

| Excluded item | Reason | Where it really goes |
|---|---|---|
| Interest on capital / loan / debentures | Financial | Costing P&L (some texts include notional interest — only if asked) |
| Income-tax, advance tax | Appropriation of profit | P&L appropriation |
| Dividends paid, transfer to reserve | Appropriation | Below the line |
| Loss / profit on sale of fixed asset or investment | Non-operating capital item | Costing P&L |
| Goodwill / preliminary expenses / discount on shares written off | Financial write-off | Costing P&L |
| Donation, charity | Non-operating appropriation | Costing P&L |
| Cash discount received / allowed | Financial | Costing P&L |
| Interest / dividend / rent *received* | Non-operating income | Costing P&L (income side) — **not** deducted from cost |
| Abnormal loss (fire, theft, strike idle time, abnormal wastage) | Not a cost of normal production | Costing P&L |
| Fines and penalties | Abnormal / statutory | Costing P&L |

*A subtle one:* **notional costs** (notional rent of own premises, notional interest on own capital, salary of a proprietor who draws none) are *included* in a cost sheet only when the question tells you to, because cost accounting sometimes imputes them to make comparison fair. Default: exclude unless instructed.

---

## 5. Worked Examples

### Example 1 — The foundation (simple, no stocks)

*Meridian Tools furnishes the following for the year. Prepare a Cost Sheet showing each stage and profit.*

| Item | ₹ |
|---|---|
| Direct materials purchased & consumed | 4,00,000 |
| Direct wages | 2,00,000 |
| Direct expenses (special mould hire) | 40,000 |
| Factory overheads | 1,20,000 |
| Administration overheads | 60,000 |
| Selling & distribution overheads | 80,000 |
| Sales | 10,00,000 |

**Solution — Cost Sheet of Meridian Tools**

| Particulars | ₹ | ₹ |
|---|---:|---:|
| Direct Materials consumed | | 4,00,000 |
| Direct Wages | | 2,00,000 |
| Direct Expenses | | 40,000 |
| **Prime Cost** | | **6,40,000** |
| Add: Factory Overheads | | 1,20,000 |
| **Works / Factory Cost** | | **7,60,000** |
| Add: Administration Overheads | | 60,000 |
| **Cost of Production** | | **8,20,000** |
| Add: Selling & Distribution Overheads | | 80,000 |
| **Cost of Sales** | | **9,00,000** |
| **Profit (balancing figure)** | | **1,00,000** |
| **Sales** | | **10,00,000** |

*Check:* Sales 10,00,000 − Cost of Sales 9,00,000 = Profit 1,00,000. ✓ Reconciles. Note profit is 1,00,000/9,00,000 = **11.11% on cost** = 1,00,000/10,00,000 = **10% on sales** — the interconversion of §4.8 in action.

---

### Example 2 — Introducing all three stocks (the timing bridge)

*Nova Appliances, for the year ended 31 March 2026. Prepare a Cost Sheet.*

| Item | ₹ |
|---|---|
| Raw material — opening stock | 50,000 |
| Raw material — purchases | 6,00,000 |
| Carriage inward | 20,000 |
| Raw material — closing stock | 70,000 |
| Direct wages | 3,00,000 |
| Direct expenses | 30,000 |
| Factory overheads | 1,80,000 |
| Opening Work-in-Progress | 40,000 |
| Closing Work-in-Progress | 60,000 |
| Sale of factory scrap | 10,000 |
| Administration overheads | 90,000 |
| Opening finished goods | 80,000 |
| Closing finished goods | 1,20,000 |
| Selling & distribution overheads | 1,10,000 |
| Profit margin | 20% on sales |

**Step 1 — Material consumed** (RM stock adjusted *before* Prime Cost):
50,000 + 6,00,000 + 20,000 − 70,000 = **6,00,000**.

**Step 2 — Prime Cost:** 6,00,000 + 3,00,000 + 30,000 = **9,30,000**.

**Step 3 — Works Cost** (factory overheads *less* scrap recovery, then WIP adjusted at the factory stage):
Factory OH net of scrap = 1,80,000 − 10,000 = 1,70,000.
Gross works = 9,30,000 + 1,70,000 = 11,00,000; + opening WIP 40,000 − closing WIP 60,000 = **10,80,000**.

**Step 4 — Cost of Production:** 10,80,000 + 90,000 = **11,70,000**.

**Step 5 — Cost of Goods Sold** (finished-goods stock adjusted *after* Cost of Production):
11,70,000 + 80,000 − 1,20,000 = **11,30,000**.

**Step 6 — Cost of Sales:** 11,30,000 + 1,10,000 = **12,40,000**.

**Step 7 — Profit & Sales** (profit is 20% *on sales* → Cost of Sales is 80% of Sales):
Sales = 12,40,000 ÷ 0.80 = **15,50,000**; Profit = 15,50,000 − 12,40,000 = **3,10,000**.

**Cost Sheet of Nova Appliances (year ended 31.03.2026)**

| Particulars | ₹ | ₹ |
|---|---:|---:|
| Opening stock of Raw Material | 50,000 | |
| Add: Purchases | 6,00,000 | |
| Add: Carriage inward | 20,000 | |
| Less: Closing stock of Raw Material | (70,000) | |
| **Raw Material Consumed** | | 6,00,000 |
| Direct Wages | | 3,00,000 |
| Direct Expenses | | 30,000 |
| **Prime Cost** | | **9,30,000** |
| Add: Factory Overheads 1,80,000 less Scrap 10,000 | | 1,70,000 |
| Add: Opening WIP | | 40,000 |
| Less: Closing WIP | | (60,000) |
| **Works / Factory Cost** | | **10,80,000** |
| Add: Administration Overheads | | 90,000 |
| **Cost of Production** | | **11,70,000** |
| Add: Opening Finished Goods | | 80,000 |
| Less: Closing Finished Goods | | (1,20,000) |
| **Cost of Goods Sold** | | **11,30,000** |
| Add: Selling & Distribution Overheads | | 1,10,000 |
| **Cost of Sales** | | **12,40,000** |
| **Profit (20% on sales)** | | **3,10,000** |
| **Sales** | | **15,50,000** |

*Check:* Profit 3,10,000 ÷ Sales 15,50,000 = 20.0% on sales. ✓ Every stock entered at its correct rung; the sheet reconciles.

---

### Example 3 — The exam-hard tender/quotation (per-unit costing + estimate)

This is the archetypal ICAI question: use *last period's* actuals to derive *per-unit* rates, then *project* them onto a future order with cost changes — and quote a price.

*Precision Castings produced and sold **10,000 units** last year. Actuals:*

| Item | ₹ |
|---|---|
| Raw materials consumed | 8,00,000 |
| Direct wages | 5,00,000 |
| Direct expenses | 1,00,000 |
| Factory overheads | 3,00,000 |
| Administration overheads | 2,40,000 |
| Selling & distribution overheads | 2,00,000 |
| Sales | 25,00,000 |

*For the coming year the company has received a tender enquiry for **12,000 units** and expects:*
1. **Raw material price** will rise by **10%**.
2. **Wage rates** will rise by **20%**.
3. **Factory overhead** is recovered as a **percentage of direct wages** (same % as last year).
4. **Administration overhead** is recovered as a **percentage of works cost** (same % as last year).
5. **Selling & distribution overhead** is recovered **per unit** at last year's rate.
6. Direct expenses are **variable** — same rate per unit.
7. The company wants a **profit of 20% on the selling price**.

*Prepare (a) last year's Cost Sheet with per-unit columns, and (b) the estimated Cost Sheet / quotation for the 12,000-unit tender, and state the price per unit to quote.*

---

**Part (a) — Last year's Cost Sheet (10,000 units) to extract the rates**

| Particulars | Total ₹ | Per unit ₹ |
|---|---:|---:|
| Raw Materials consumed | 8,00,000 | 80.00 |
| Direct Wages | 5,00,000 | 50.00 |
| Direct Expenses | 1,00,000 | 10.00 |
| **Prime Cost** | **14,00,000** | **140.00** |
| Factory Overheads | 3,00,000 | 30.00 |
| **Works Cost** | **17,00,000** | **170.00** |
| Administration Overheads | 2,40,000 | 24.00 |
| **Cost of Production** | **19,40,000** | **194.00** |
| Selling & Distribution OH | 2,00,000 | 20.00 |
| **Cost of Sales** | **21,40,000** | **214.00** |
| Profit | 3,60,000 | 36.00 |
| **Sales** | **25,00,000** | **250.00** |

**Extract the recovery bases (this is the "why" of the tender):**
- Factory OH as % of Direct Wages = 3,00,000 ÷ 5,00,000 = **60% of wages**.
- Administration OH as % of Works Cost = 2,40,000 ÷ 17,00,000 = **14.1176% of works cost**.
- Selling & distribution = **₹20 per unit** (flat rate).

*Why use rates, not totals? Because the totals belong to 10,000 units at old prices. A rate is a portable law — apply it to any volume at any price level. That is exactly what a manager needs to price a future order.*

**Part (b) — Estimated per-unit costs for the 12,000-unit tender**

Build the *new* per-unit figures using the given changes, then multiply by 12,000.

- Raw material per unit: 80.00 × 1.10 = **₹88.00**
- Direct wages per unit: 50.00 × 1.20 = **₹60.00**
- Direct expenses per unit: **₹10.00** (variable, unchanged rate)
- **Prime Cost per unit** = 88 + 60 + 10 = **₹158.00**
- Factory OH = 60% of new wages = 60% × 60 = **₹36.00**
- **Works Cost per unit** = 158 + 36 = **₹194.00**
- Administration OH = 14.1176% of works cost = 0.141176 × 194 = **₹27.39**
- **Cost of Production per unit** = 194 + 27.39 = **₹221.39**
- Selling & distribution = **₹20.00** per unit (flat)
- **Cost of Sales per unit** = 221.39 + 20 = **₹241.39**
- Profit = 20% *on selling price* → Cost of Sales is 80% of price → Profit per unit = 241.39 × (20/80) = **₹60.35**
- **Selling price to quote per unit** = 241.39 + 60.35 = **₹301.74** (i.e., 241.39 ÷ 0.80)

**Estimated Cost Sheet / Quotation — 12,000 units**

| Particulars | Per unit ₹ | Total ₹ (×12,000) |
|---|---:|---:|
| Raw Materials (80 × 1.10) | 88.00 | 10,56,000 |
| Direct Wages (50 × 1.20) | 60.00 | 7,20,000 |
| Direct Expenses | 10.00 | 1,20,000 |
| **Prime Cost** | **158.00** | **18,96,000** |
| Factory OH (60% of wages) | 36.00 | 4,32,000 |
| **Works Cost** | **194.00** | **23,28,000** |
| Administration OH (14.1176% of works) | 27.39 | 3,28,695 |
| **Cost of Production** | **221.39** | **26,56,695** |
| Selling & Distribution (₹20/unit) | 20.00 | 2,40,000 |
| **Cost of Sales** | **241.39** | **28,96,695** |
| Profit (20% on selling price) | 60.35 | 7,24,174 |
| **Sales / Tender Price** | **301.74** | **36,20,869** |

*Check:* Profit 7,24,174 ÷ Sales 36,20,869 = 20.0% on sales. ✓ Works cost per unit 194 × 12,000 = 23,28,000. ✓ Admin 3,28,695 ÷ 23,28,000 = 14.12%. ✓ Rounding to two decimals leaves totals within a rupee; ICAI accepts either the per-unit-rounded or the exact-fraction answer as long as it reconciles.

**Managerial punchline:** the quote is **₹301.74 per unit** (₹36,20,869 for the order). Notice how *every* input change flowed through cleanly *because* we costed by rate and by stage. That is the entire payoff of the Cost Sheet — a defensible, transparent price built brick by brick.

---

### Example 4 — The units-differ case (produced ≠ sold, with per-unit stock valuation)

*This is the trap Example 2 hides: there, all stocks were given in value. Here you are given **quantities**, and must value closing finished goods yourself. It tests whether you truly understand the "produced vs sold" bridge.*

*Apex Pumps for the year ended 31 March 2026. There was **no** opening finished stock and **no** WIP. The company **produced 20,000 units** and **sold 18,000 units** at ₹300 each.*

| Item | ₹ |
|---|---|
| Raw materials consumed | 24,00,000 |
| Direct wages | 12,00,000 |
| Direct expenses | 2,00,000 |
| Factory overheads | 9,00,000 |
| Administration overheads (production) | 5,00,000 |
| Selling & distribution overheads | 3,60,000 |

*Prepare the Cost Sheet, value the closing finished goods, and find profit.*

**Step 1 — Cost of Production of 20,000 units produced:**
Prime Cost = 24,00,000 + 12,00,000 + 2,00,000 = **38,00,000**.
Works Cost = 38,00,000 + 9,00,000 = **47,00,000** (no WIP).
Cost of Production = 47,00,000 + 5,00,000 = **52,00,000**.

**Step 2 — Cost of Production per unit** = 52,00,000 ÷ 20,000 = **₹260**.

**Step 3 — Closing finished goods** = units unsold × cost of production per unit.
Units unsold = 20,000 produced − 18,000 sold − 0 opening = **2,000 units**.
Value = 2,000 × ₹260 = **₹5,20,000**. *(Valued at cost of production, NOT cost of sales — no selling cost on unsold stock.)*

**Step 4 — Cost of Goods Sold** = 52,00,000 + 0 opening − 5,20,000 closing = **46,80,000** (= 18,000 × ₹260 ✓).

**Step 5 — Cost of Sales** = 46,80,000 + 3,60,000 S&D = **50,40,000**.

**Step 6 — Sales & Profit:** Sales = 18,000 × ₹300 = **54,00,000**. Profit = 54,00,000 − 50,40,000 = **₹3,60,000**.

**Cost Sheet of Apex Pumps (year ended 31.03.2026)**

| Particulars | Units | Total ₹ |
|---|---:|---:|
| Raw Materials consumed | | 24,00,000 |
| Direct Wages | | 12,00,000 |
| Direct Expenses | | 2,00,000 |
| **Prime Cost** | | **38,00,000** |
| Add: Factory Overheads | | 9,00,000 |
| **Works Cost** | 20,000 produced | **47,00,000** |
| Add: Administration Overheads | | 5,00,000 |
| **Cost of Production** | 20,000 | **52,00,000** |
| Less: Closing Finished Goods (2,000 × 260) | (2,000) | (5,20,000) |
| **Cost of Goods Sold** | 18,000 sold | **46,80,000** |
| Add: Selling & Distribution Overheads | | 3,60,000 |
| **Cost of Sales** | 18,000 | **50,40,000** |
| **Profit** | | **3,60,000** |
| **Sales (18,000 × 300)** | 18,000 | **54,00,000** |

*Check:* COGS 46,80,000 ÷ 18,000 = ₹260 per unit = cost of production per unit. ✓ Closing stock 2,000 × 260 = 5,20,000, and 5,20,000 + 46,80,000 = 52,00,000 = full cost of production. ✓ Every produced unit's cost is accounted for — 18,000 flowed to COGS, 2,000 sit in closing stock. Nothing leaked. **The whole lesson:** production cost splits between what was sold (COGS) and what remains (closing FG), and both use the *same* ₹260 production rate.

---

### Example 5 — Examiner tweak: material at prime cost WIP + notional item planted

*A short "what if the examiner tweaks it" drill. Zenith Forgings gives:* Materials consumed ₹10,00,000; Direct wages ₹6,00,000; Direct expenses ₹50,000; Factory overhead ₹4,00,000; **Opening WIP ₹1,20,000 and Closing WIP ₹1,00,000, both valued at prime cost**; Administration OH ₹2,00,000; **Interest on bank loan ₹80,000**; **Profit on sale of old machine ₹30,000**; Selling OH ₹1,50,000; Profit 25% on cost.

*Two tweaks are planted:* (i) WIP is valued at **prime cost**, so it must be adjusted **before** factory overheads, not after; (ii) interest and profit-on-sale are **financial/non-operating** and must be **excluded** entirely.

**Solution**

| Particulars | ₹ |
|---|---:|
| Materials consumed | 10,00,000 |
| Direct Wages | 6,00,000 |
| Direct Expenses | 50,000 |
| **Prime Cost (of work done)** | **16,50,000** |
| Add: Opening WIP (at prime cost) | 1,20,000 |
| Less: Closing WIP (at prime cost) | (1,00,000) |
| **Prime Cost adjusted for WIP** | **16,70,000** |
| Add: Factory Overheads | 4,00,000 |
| **Works Cost** | **20,70,000** |
| Add: Administration Overheads | 2,00,000 |
| **Cost of Production / COGS (no FG stock)** | **22,70,000** |
| Add: Selling & Distribution Overheads | 1,50,000 |
| **Cost of Sales** | **24,20,000** |
| Add: Profit (25% on cost) | 6,05,000 |
| **Sales** | **30,25,000** |

*Excluded:* interest on loan ₹80,000 and profit on sale of machine ₹30,000 — both financial/non-operating, so they never touch the cost sheet.

*Check:* Profit 6,05,000 ÷ Cost of Sales 24,20,000 = 25.0% on cost. ✓ WIP was adjusted **before** factory OH precisely because it was valued at prime cost — had it been valued at works cost, it would have gone in after the ₹4,00,000. Naming that assumption is where the mark is. Had you also wrongly deducted the ₹80,000 interest as a cost or added the ₹30,000 machine profit to sales, every figure below would be corrupted.

---

## 6. Presentation / Format — the standard vertical layout

ICAI expects a **vertical (columnar) statement**, not a debit/credit account. Golden presentation rules:

1. **Title:** "Cost Sheet (or Statement of Cost) of ___ for the period ended ___."
2. **Two amount columns** for build-up (detail column + total column); add a **"Per Unit"** column and a **"Total"** column when quantities are given.
3. Show the **bold sub-totals** in order: Prime Cost → Works/Factory Cost → Cost of Production → Cost of Goods Sold → Cost of Sales → Sales. Never skip a stage even if a layer is nil.
4. Insert each **stock at its correct stage** (RM before Prime; WIP at Works; FG after Cost of Production).
5. Show **scrap sale** as a deduction from factory overhead/works cost; show **defective/rectification** per instructions.
6. Keep **excluded financial items** off the sheet entirely (see §4.9) — mention them only if a reconciliation with financial profit is asked.

**Per-unit column discipline** (where students lose marks): the per-unit figure at each stage must be that stage's *total ÷ the relevant quantity*, and the relevant quantity **changes down the sheet**:

- Material, Prime, Works, Cost of Production → divide by **units produced**.
- Cost of Goods Sold, Cost of Sales, Sales, Profit → divide by **units sold**.

Because produced ≠ sold when stock exists, a single "per unit" column cannot be internally consistent all the way down. State which quantity you used at the stock boundary, or use two per-unit columns (produced-basis above COGS, sold-basis from COGS down). The examiner rewards you for noticing the base switches at the finished-goods line.

*Skeleton to reproduce from memory:*

| Stage | Add | Less | Gives |
|---|---|---|---|
| Materials | Op. RM + Purchases + Carriage in | Cl. RM | Material Consumed |
| + Wages + Direct Exp | | | **Prime Cost** |
| + Factory OH | Op. WIP | Cl. WIP, Scrap | **Works Cost** |
| + Admin OH | | | **Cost of Production** |
| | Op. FG | Cl. FG | **Cost of Goods Sold** |
| + Selling & Distribution OH | | | **Cost of Sales** |
| + Profit | | | **Sales** |

**Reconciliation footnote to keep handy.** If a question also gives financial-account profit and asks *why* it differs, the gap is exactly the §4.9 items (financial expenses, non-operating incomes, abnormal losses, and any over/under-absorbed overhead and stock-valuation differences). That is the entire subject of the *Cost & Financial Accounts Reconciliation* chapter — the Cost Sheet is where the divergence is *created*.

---

## 7. Connections — where this sits in the wider syllabus

*Figure 3 — the Cost Sheet as the confluence of the element chapters.*

```mermaid
graph LR
    M["Material Costing"] --> CS["COST SHEET"]
    L["Labour Costing"] --> CS
    O["Overheads Absorption"] --> CS
    CS --> R["Cost Ledger and Reconciliation"]
    CS --> T["Job Batch and Contract Costing"]
    CS --> MD["Marginal Costing and Pricing decisions"]
```

- **Material, Labour, Overhead chapters** feed the three elements — the Cost Sheet is where they *assemble*.
- **Overhead absorption** supplies the recovery rates (% of wages, % of works cost, per unit) used in tenders — exactly Example 3.
- **Reconciliation of cost and financial accounts** exists because the Cost Sheet *excludes* the financial items of §4.9; the reconciliation statement bridges the gap.
- **Job / Batch / Contract costing** are the Cost Sheet applied to a single job, a batch, or a long project.
- **Marginal costing** re-cuts the same costs into *fixed vs variable* rather than *function-wise*, for short-run decisions.

*Figure 4 — the two independent ways the same total cost is classified.*

```mermaid
flowchart TD
    TC["TOTAL COST"] --> E["By ELEMENT"]
    TC --> F["By FUNCTION"]
    E --> E1["Material"]
    E --> E2["Labour"]
    E --> E3["Expenses"]
    F --> F1["Production"]
    F --> F2["Administration"]
    F --> F3["Selling and Distribution"]
    E1 --> X["Each element splits into direct and indirect"]
    E2 --> X
    E3 --> X
```

*The Cost Sheet uses the element cut to build Prime Cost and the function cut to build the staircase above it.*

---

## 8. Traps & Examiner Tricks

1. **Wrong rung for a stock.** Putting closing FG at the Works stage, or WIP after Cost of Production, corrupts everything below. *Rule:* RM before Prime, WIP at Works, FG after Cost of Production.
2. **Carriage inward vs outward.** Inward = part of material cost (added before Prime). Outward = selling cost (added at Cost of Sales). Examiners bury both in one list.
3. **Profit on cost vs profit on sales.** "25% on cost" ≠ "25% on sales." Convert deliberately (§4.8). This flips the tender price by several rupees.
4. **Financial items sneaked in.** Interest on capital, income-tax, dividends, loss on sale of machinery, donation, goodwill written off, transfer to reserve — all must be **left out**. Non-operating incomes (interest/dividend received) are **not** deducted from cost either.
5. **Scrap treatment.** Normal scrap sale reduces factory cost. Do *not* add it to sales. Abnormal scrap loss goes to Costing P&L, not the sheet.
6. **Cash discount vs trade discount.** Cash discount (received/allowed) is financial — exclude. Trade discount is netted against purchases/sales.
7. **Per-unit rate from the wrong volume.** In tenders, derive rates from *actual output* (units produced), then apply to the *new* quantity. Mixing "sold" and "produced" units is a classic slip when FG stock exists.
8. **Depreciation split.** Depreciation of *plant* → factory OH; of *office equipment* → admin OH; of *delivery van* → selling OH. Location decides the layer.
9. **Overheads given as "office and administration"** default to the admin stage; "showroom/warehouse of finished goods" is selling, not factory.
10. **Under-/over-absorbed overhead** (if given): adjust only if the question asks; otherwise use actuals. Don't invent adjustments.
11. **Closing FG valued at cost of sales.** Closing finished goods carry **cost of production** per unit, never cost of sales — a warehoused unit has not been sold, so no selling cost attaches (Example 4). Valuing it higher overstates stock and understates COGS.
12. **Overtime premium mis-placed.** Only the *premium* is reclassified (job-specific → direct expense; general → factory OH; abnormal → P&L). The *normal-rate* portion of overtime stays in direct wages. Students often shift the whole overtime figure.
13. **WIP valuation basis ignored.** If WIP is stated "at prime cost," adjust it *before* factory overheads (Example 5); default (works cost) is *after*. Always name the assumption.
14. **Primary vs secondary packing.** Primary packing essential to sale → production cost; transport packing → distribution. Same word, different stage.
15. **Notional items added without instruction.** Notional rent/interest/proprietor's salary enter the sheet only if the question says so; otherwise leave them out.
16. **GST / refundable taxes added to material.** Only *irrecoverable* taxes and duties form part of material cost; GST input credit (recoverable) is excluded, like trade discount.
17. **Idle-time and abnormal-loss wages.** Normal idle time → factory OH; abnormal idle time/strike → Costing P&L. Never load abnormal idle wages onto product cost.
18. **"Sold" units used to value production stages.** Prime/Works/Cost of Production per unit use *units produced*; only COGS and below use *units sold*. The base switches at the FG line (§6).

---

## 9. First-Principles Recap

Strip away the format and the whole chapter is one sentence: **cost accumulates as the product physically travels — foundation of directs (Prime), through the factory (Works), through the office (Cost of Production), out to the customer (Cost of Sales) — and each stock is injected at the exact stage where the goods physically rest.**

- *Why a staircase?* Because different managers own different layers, and each needs to see his own cost.
- *Why directs first?* Because traceable cost is controllable at the shop floor before shared overheads.
- *Why three stocks at three stages?* Because "produced" ≠ "sold," and cost must be matched to *where the goods actually are* — RM before making, WIP during making, FG after making.
- *Why is each stock valued at the stage it reached?* Because a unit can only carry the costs it has actually absorbed — RM at purchase cost, WIP at works cost, FG at cost of production. Selling cost never sits in stock because it is not incurred until sale.
- *Why exclude financial items?* Because cost tells you the price of *making and selling*, not of *financing and taxing*.
- *Why per-unit rates for tenders?* Because a rate is a portable law you can carry to any future volume and price level — that is the manager's whole reason for asking.
- *Why does the per-unit base switch at the finished-goods line?* Because everything above COGS is measured over units *produced*, and everything from COGS down is measured over units *sold* — and those two numbers differ exactly by the change in finished-goods stock.

If you can rebuild the format from these *whys*, you never need to memorise it — and you can adapt it to any twist the examiner invents.

---

## 10. Quick-Revision Sheet

| # | Stage | Formula |
|---|---|---|
| 1 | Material Consumed | Op. RM + Purchases + Carriage inward + duty − Returns − Cl. RM |
| 2 | **Prime Cost** | Material Consumed + Direct Wages + Direct Expenses |
| 3 | Gross Works Cost | Prime Cost + Factory Overheads − Scrap sale |
| 4 | **Works / Factory Cost** | Gross Works Cost + Op. WIP − Cl. WIP |
| 5 | **Cost of Production** | Works Cost + Administration Overheads |
| 6 | **Cost of Goods Sold** | Cost of Production + Op. Finished Goods − Cl. Finished Goods |
| 7 | **Cost of Sales** | COGS + Selling & Distribution Overheads |
| 8 | **Sales** | Cost of Sales + Profit |
| 9 | Profit = x% on cost | Sales = Cost × (1 + x); on-sales rate = x/(100+x) |
| 10 | Profit = y% on sales | Cost = Sales × (1 − y); on-cost rate = y/(100−y) |
| 11 | FG stock valuation | Cl. FG units × (Cost of Production ÷ units produced) |
| 12 | Cost per unit | Total cost at a stage ÷ number of units (produced above COGS, sold below) |
| 13 | Units sold identity | Op. FG units + Units produced − Cl. FG units |
| 14 | WIP valued at prime cost | Adjust *before* factory OH (default: after, at works cost) |

**Stock-at-its-stage map:** Raw Material → *before* Prime · WIP → *at* Works · Finished Goods → *after* Cost of Production.

**Stock-valuation map:** RM → purchase cost · WIP → works cost (or prime cost if stated) · FG → cost of production per unit. Selling cost is *never* in stock.

**Per-unit base map:** Material/Prime/Works/Cost of Production → ÷ units *produced* · COGS/Cost of Sales/Sales/Profit → ÷ units *sold*.

**Excluded from Cost Sheet:** interest, income-tax, dividends, loss/profit on sale of assets, transfers to reserve, cash discount, donations, goodwill/preliminary written off, non-operating incomes, abnormal losses, fines/penalties, recoverable taxes (GST credit).

**Overhead-by-location:** plant depreciation & works manager → Factory · office rent & audit fee & directors' fee → Admin · advertising, carriage outward, salesmen commission, showroom → Selling & Distribution.

**Margin ready-reckoner:** 25% on cost = 20% on sales · 33⅓% on cost = 25% on sales · 50% on cost = 33⅓% on sales · 100% on cost = 50% on sales.
