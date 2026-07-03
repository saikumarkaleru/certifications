<!-- v2-deep -->

# Chapter 02 — Material Cost

## 1. The Problem — Why a Whole Chapter on "Stuff You Buy"?

Walk into any manufacturing business and ask the accountant: "Where does your money go?" In the overwhelming majority of Indian manufacturing firms the answer is the same — **material is the single largest cost element**, routinely 40% to 70% of total cost. A steel fabricator, a textile mill, a pharmaceutical plant, an FMCG unit — for all of them, rupees spent on raw material dwarf rupees spent on wages or overhead.

Now here is the uncomfortable part. Material is also the cost element that is **easiest to lose control of**, for three brutal reasons:

1. **It is physical and portable.** Cash sits in a bank with layers of controls. Material sits in a godown where it can be pilfered, substituted, over-issued, or simply walk out the gate. Theft of material is a real, quantifiable loss in Indian factories.
2. **It deteriorates, evaporates, spills, and breaks.** Chemicals evaporate, grain is eaten by rats, liquids spill, glass breaks, food rots. Some of this is unavoidable (normal); some signals a broken process (abnormal). Telling the two apart is a costing decision.
3. **It ties up working capital.** Every rupee sitting as stock in the godown is a rupee borrowed from the bank at 10–12% interest, or a rupee not earning returns elsewhere. Buy too much and you bleed carrying cost; buy too little and the production line stops and you lose customers.

Financial accounting is *useless* for managing any of this in real time. The financial P&L tells you, once a year, that you consumed ₹8 crore of material. It cannot tell you: *how much* should we order at a time? *When* should we reorder? At *what price* should we value the units we just issued to the shop floor when prices have been rising all year? Was that 500 kg "loss" acceptable or did someone steal it?

These are **managerial decisions**, and each one has a purpose-built technique in cost accounting:

| The decision a manager faces | The technique this chapter builds |
|---|---|
| How much to order in one go? | **Economic Order Quantity (EOQ)** |
| When to place the order? | **Re-order Level** |
| How low can stock safely fall? | **Minimum Level** |
| How high should stock ever go? | **Maximum Level** |
| At what point do we panic-buy? | **Danger Level** |
| What price do we put on units issued to production? | **FIFO / LIFO / Weighted Average** |
| Was a loss acceptable or does it need investigation? | **Normal vs Abnormal loss treatment** |
| Which items deserve tight control and which don't? | **ABC Analysis** |
| Is my stock moving or rotting on the shelf? | **Inventory Turnover Ratio** |
| Who is allowed to buy, receive, store, and issue? | **Procurement cycle & documentation** |

Every formula below exists to answer one of these questions. We never state a formula before you feel the pain it removes.

A last framing point before we build. Material control is not one technique but a **chain of custody** — a rupee of material passes through *purchasing → receiving → storage → issue → consumption → loss/scrap*, and cost accounting installs a control (and a document) at every link. If you can see the chain, the chapter stops being a pile of disconnected formulae and becomes one story: **keep the right quantity, priced honestly, with every movement recorded and every loss classified.**

---

## 2. The Core Idea — The Godown as a Bathtub

Picture your material stock as **water in a bathtub**.

- The **tap** pouring water in = purchases (deliveries from suppliers).
- The **drain** letting water out = issues to production (consumption).
- The **water level** at any moment = stock on hand.

The whole art of material control is keeping the water level in a **safe band** — never so low the drain sucks air (a **stock-out**, production stops), never so high it overflows and floods the bathroom (**over-stocking**, capital locked and material spoiling).

The catch is that the tap has a **delay**: when you open it (place an order), water doesn't arrive instantly — it takes the supplier's **lead time** to deliver. So you must open the tap *before* the level gets dangerous, judging how fast the drain is running (consumption rate) and how long the tap takes to respond (lead time).

Every "level" in this chapter is just a **marked line on the side of the bathtub**:
- **Re-order level** = the line at which you shout "open the tap!"
- **Minimum level** = the lowest the water should ever get in normal life.
- **Maximum level** = the highest it should ever get.
- **Danger level** = an emergency red line below minimum — if you hit it, something went wrong, halt normal issues and rush an emergency order.

And **EOQ** answers a different, quieter question: each time you open the tap, *how much* water should you let in? Too little and you're forever running to the tap (high ordering cost); too much and you're storing stale water (high carrying cost). EOQ is the sweet spot between those two nagging costs.

**Extend the picture once more.** The saw-tooth shape of the water level over time is the single most useful mental image in the chapter. Draw stock on the vertical axis and time on the horizontal: the level slides *down* a slope (the drain / consumption), hits the re-order line, keeps sliding for the length of the lead time, and then jumps *vertically up* by one order quantity when the lot lands. Repeat. That jagged saw-tooth is where **every** number comes from:
- the **average height** of the teeth is your average stock (→ carrying cost),
- the **number of teeth per year** is your number of orders (→ ordering cost),
- the **depth of the valley** at the bottom of each tooth is your minimum level,
- and the **height at which you start each downslope's order** is the re-order level.

Once you can see the saw-tooth, you are not memorising six level formulae — you are *reading them off a picture*.

Hold this bathtub picture. Everything technical below hangs on it.

---

## 3. Why It's Built This Way — The Logic Before the Formulae

### 3.1 The two-cost tug-of-war behind EOQ

Why can't we just "order what we need when we need it"? Because **ordering itself costs money**, and **holding stock costs money**, and these two costs pull in *opposite directions*.

- **Ordering cost** (cost per order): raising a purchase requisition, inviting quotations, placing the order, following up, receiving, inspecting, and processing the invoice. This is largely *fixed per order* — it costs roughly the same to order 100 units or 10,000 units. So: **more orders → more total ordering cost.** To cut ordering cost, order in *big lots, rarely*.

- **Carrying cost** (holding cost): interest on capital locked in stock, godown rent, insurance, handling, obsolescence, deterioration, pilferage. This grows with *how much you hold*. So: **bigger lots → higher average stock → more carrying cost.** To cut carrying cost, order in *small lots, often*.

You cannot minimise both. Big rare orders kill carrying cost but inflate ordering cost. Small frequent orders do the reverse. **Total cost is minimised where the two curves cross** — where annual ordering cost exactly equals annual carrying cost. That crossing point is the EOQ. That single insight is the *whole* derivation; the algebra just formalises it.

**A deeper "why" — why the minimum sits exactly at the crossing.** Total cost is a U-shaped curve: falling ordering cost (a hyperbola, A·O/Q) added to rising carrying cost (a straight line, C·Q/2). A useful mathematical fact: the sum of a term that falls as 1/Q and a term that rises linearly in Q is minimised precisely where the two terms are equal in magnitude. That is *why* "ordering cost = carrying cost" is not a coincidence but the defining property of EOQ — and why it doubles as a self-check in every problem. Notice also that the total-cost curve is **flat near the bottom**: order 20–30% away from EOQ and total cost barely rises (see Example 2). This "robustness" is a genuine exam-and-real-life insight — EOQ need not be hit to the last unit.

### 3.2 Why we need levels at all

Even with the right order *size*, you still need to know *when* to order and how to bound the stock. Levels exist because **lead time is uncertain and consumption is uncertain**. If both were perfectly predictable you'd need no buffer — you'd place an order timed so the last unit is issued exactly as the new lot arrives. But suppliers are late and the shop floor sometimes consumes faster than expected. Levels are essentially a **safety-buffer system**: a set of pre-computed lines so that a storekeeper — not a manager — can run day-to-day stock control mechanically and only escalate at the danger line.

There is an organisational "why" hiding here too. Levels **push control down to the least-skilled reliable person**. A storekeeper needs no judgement: watch the bin, when it drops to the re-order line raise a requisition, when it drops to the danger line escalate. Judgement (setting the levels, revising them when usage or lead time shifts) stays with management, and is exercised *once*, not every day. This separation — policy set high, executed low — is the design principle behind the whole levels system.

### 3.3 Why issue valuation is even a question

Here's a subtlety that trips up newcomers from a financial background. You bought the same bolt in January at ₹10, in March at ₹12, in May at ₹15. Today you issue 1,000 bolts to production. **What is their cost — ₹10, ₹12, ₹15, or a blend?** Physically the bolts are identical and mixed in a bin; you genuinely cannot say *which* rupee-batch left. So costing must adopt an **assumption** — FIFO, LIFO, or weighted average. This is not accounting pedantry: the assumption you pick changes the cost charged to the job, the value of closing stock, and therefore **reported profit**. In a period of rising prices, the choice can swing profit by lakhs. That is why it is a managerial decision, not a clerical one.

The deeper principle: material issue valuation is a **cost-flow assumption, not a physical-flow claim.** FIFO does not require you to physically issue the oldest bolt; it only assumes you *cost* the issue as if you did. This decoupling of the accounting flow from the physical flow is what makes several methods possible for the *same* physical process. The examiner rewards candidates who state this explicitly ("under FIFO we *assume* the earliest receipts are issued first").

### 3.4 Why "cost of material" is not just the invoice price

A quieter first-principles point that the exam loves. The cost at which material enters the stores ledger is **not** the sticker price on the invoice. Costing builds up a *landed cost*:

> **Material cost = Purchase price − trade discount − duty/GST credit available + carriage inward + insurance in transit + other purchase-related charges (commission, taxes not creditable) − subsidies.**

The *why* behind each adjustment is a control principle:
- **Trade discount is deducted** because it is a genuine reduction in price — the firm never owes the gross amount.
- **Cash discount is NOT deducted** from material cost. Cash discount is a *reward for paying early* — a financial matter, credited to a financial income account — not a reduction in the material's economic cost. Treating it as a material-cost reduction would let a *financing* decision distort *product* cost.
- **GST/duty that is creditable (input tax credit available) is EXCLUDED** from cost — you will recover it, so it is never a cost to you. GST that is *not* creditable (e.g. on items where credit is blocked) *is* added to cost.
- **Carriage inward, insurance in transit, and loading/unloading are ADDED** — they are unavoidable to get the material to your godown, so they are part of what the material genuinely costs you.

Get this build-up right and the very first line of the cost sheet is right; get it wrong and every downstream number inherits the error.

---

## 4. Full Technical Content — Every Formula With Its "Why"

### 4.0 The Procurement Cycle and Its Documents (the control backbone)

Before quantities and prices, the exam expects you to know *who does what, and which document proves it.* Material control is a **segregation-of-duties** system: the person who *requests* material is not the person who *buys* it, who is not the person who *receives* it, who is not the person who *stores* it, who is not the person who *authorises payment*. This separation is deliberate — it makes fraud require collusion rather than a single dishonest hand.

| Stage | Document | Raised by → sent to | Its control purpose |
|---|---|---|---|
| Need identified | **Purchase Requisition** | Storekeeper / Dept → Purchasing | Proves the buy was *requested* by an authorised person, not invented by the buyer |
| Buying | **Purchase Order (PO)** | Purchasing → Supplier | The binding commitment; fixes quantity, price, delivery terms |
| Goods arrive | **Goods Received Note (GRN)** / Material Received Note | Receiving/Inspection → Stores, Purchasing, Accounts | Proves goods actually arrived, in what quantity and condition, after inspection |
| Storage record | **Bin Card** (kept in the godown, quantity only) | Storekeeper | Real-time physical quantity record at the bin |
| Value record | **Stores Ledger** (kept in costing office, quantity *and* value) | Cost accounting | Priced perpetual record; the basis for issue valuation |
| Issue to floor | **Material Requisition Note (MRN)** | Production → Stores | Authorises and records an issue; the source document for charging jobs |
| Return unused | **Material Returned Note** | Production → Stores | Records material sent back to stores (credited to the job) |
| Move between jobs | **Material Transfer Note** | Job → Job | Records inter-job transfer *without* physically returning to stores |

**Bin Card vs Stores Ledger — a classic 4-mark distinction.**

| Feature | Bin Card | Stores Ledger |
|---|---|---|
| Kept by | Storekeeper, in the stores | Cost accounting office |
| Records | **Quantity only** | Quantity **and value** |
| When posted | At the moment of each movement | Periodically, from documents |
| Purpose | Physical control at the bin | Costing and valuation |

They should reconcile in quantity; a mismatch signals unrecorded movement, error, or pilferage.

**Perpetual vs Periodic (physical) inventory.** *Perpetual inventory* is a system of records (bin card + stores ledger) that shows the balance **continuously** after every movement. *Continuous stocktaking* is the physical counting of a few items every day so that all items are counted several times a year — it is the *verification* that keeps the perpetual records honest. Do not confuse the record system (perpetual inventory) with the counting programme (continuous stocktaking); the exam deliberately blurs them.

```mermaid
flowchart LR
  REQ["Purchase Requisition<br/>need is authorised"] --> PO["Purchase Order<br/>commitment to supplier"]
  PO --> GRN["Goods Received Note<br/>arrival and inspection"]
  GRN --> BIN["Bin Card<br/>quantity in stores"]
  GRN --> LEDG["Stores Ledger<br/>quantity and value"]
  MRN["Material Requisition Note<br/>issue authorised"] --> LEDG
  LEDG --> PROD["Charged to job or process"]
  RET["Material Returned Note"] --> LEDG
```
*Figure 1 — The procurement chain of custody: every link has its own document so responsibility is always traceable.*

### 4.1 Inventory Control Levels

Let us build each level from the bathtub logic. First, the raw ingredients (the "primitives") every level is made of:

- **Lead time** = time between placing an order and receiving it (also called delivery/procurement time).
- **Consumption (usage) rate** = units used per unit of time (per day/week).

Because both wobble, we speak of **maximum, minimum and normal (average)** values of each.

**(a) Re-order Level (ROL)** — the "open the tap now" line.

> **Re-order Level = Maximum Usage × Maximum Lead Time**

*Why maximum × maximum?* The reorder level must protect you in the **worst realistic case** — the fastest the shop floor might consume during the longest the supplier might take. Set it here and even a bad month won't cause a stock-out before the new lot lands. This is the primary line; several other levels are derived *from* it.

An equivalent, often-quoted form when safety stock is stated separately:

> **Re-order Level = Safety Stock + (Average Usage × Average Lead Time)**

Both express the same idea; ICAI problems usually give max/min usage and lead time, so the first form is the workhorse. *(Reconciling the two: Maximum usage × Maximum lead time = (Average usage × Average lead time) + safety stock — so the safety stock implied by the first form equals Max·Max − Avg·Avg. Examiners sometimes ask you to derive safety stock this way.)*

**(b) Minimum Level** — the floor of normal operation (the safety stock).

> **Minimum Level = Re-order Level − (Average Usage × Average Lead Time)**

*Why subtract the average, not the maximum?* Once you've re-ordered at ROL, on a *normal* day you'll consume at the *average* rate over the *average* lead time before the lot arrives. Whatever is left when it arrives is your cushion against things going wrong — that cushion *is* the minimum level. If actual usage and lead time turn out average, stock touches exactly this floor as the new lot lands. Anything below signals abnormality.

**(c) Maximum Level** — the ceiling; don't let capital drown here.

> **Maximum Level = Re-order Level + Re-order Quantity − (Minimum Usage × Minimum Lead Time)**

*Why this shape?* The highest stock can ever get is: you were sitting at ROL, you placed an order of size ROQ, and then — best case for stock build-up — the **least** was consumed (minimum usage) over the **shortest** wait (minimum lead time) before the full lot piled in on top. Add the incoming lot to reorder level, subtract the little that was drawn down in the meantime. That's the physical peak.

**(d) Danger Level** — the red emergency line, below minimum.

> **Danger Level = Average Usage × Lead Time for Emergency Purchases**

*Why a separate emergency lead time?* If you've dropped *below* the minimum, normal replenishment has failed. You must now buy through an **emergency channel** (spot purchase, faster/costlier supplier) which has its *own*, shorter lead time. The danger level is the stock that will just barely cover average consumption during that emergency procurement. Hit it and you stop issuing for non-critical use and rush an emergency buy. (Some texts use *maximum* usage here for extra conservatism; ICAI's standard formula uses average usage × emergency lead time — use that unless the question says otherwise.)

**(e) Average Stock Level** — for working-capital and carrying-cost estimates.

> **Average Stock = Minimum Level + ½ × Re-order Quantity**
>
> or, equivalently, **Average Stock = ½ × (Minimum Level + Maximum Level)**

*Why?* Between deliveries, stock saw-tooths from a peak down to the minimum, then jumps back up. Its time-average is the floor plus half a saw-tooth (half a re-order quantity).

**(f) Two related buffer ideas the exam may name.**
- **Safety (buffer) stock** = the minimum level itself in most ICAI problems — the cushion held for uncertainty. Formally, Safety Stock = (Maximum usage − Average usage) × lead time, or Max·Max − Avg·Avg depending on how the data is framed. Always define which you used.
- **Buffer for lead-time variability alone** = Average usage × (Maximum lead time − Average lead time). If the question isolates lead-time risk from usage risk, decompose accordingly.

### 4.2 Economic Order Quantity (EOQ)

Now the star formula. Define:

- **A** = Annual demand / consumption (units per year)
- **O** = Ordering cost **per order** (₹)
- **C** = Carrying cost **per unit per year** (₹). If given as a % of unit price, then C = (carrying % ) × (price per unit).

**Derivation from the two-cost tug-of-war** (Section 3.1). Let **Q** be the order quantity we're solving for.

- Number of orders per year = A / Q. So **Annual Ordering Cost = (A / Q) × O**.
- Average stock held = Q / 2 (saw-tooth). So **Annual Carrying Cost = (Q / 2) × C**.
- **Total relevant cost** T = (A/Q)·O + (Q/2)·C.

As Q rises, the first term falls and the second rises. Minimum is where they are equal (or by calculus, dT/dQ = 0):

−(A·O)/Q² + C/2 = 0  ⟹  Q² = 2·A·O / C. Hence:

> **EOQ = √( 2 × A × O / C )**

*The formula is literally the point where "ordering cost = carrying cost".* You never have to memorise it as a magic string — you can rebuild it any time from "set the two costs equal".

**Companion figures at EOQ:**

- Number of orders per year = A / EOQ
- Time between orders = 365 / (number of orders) days
- Total ordering cost = (A/EOQ)·O ; Total carrying cost = (EOQ/2)·C — **and at EOQ these two are equal** (a superb self-check!).
- Total inventory cost (excluding purchase price) = ordering + carrying = both added.
- **Total cost including purchase** = (A × price) + ordering + carrying — needed the moment quantity discounts appear (Section 4.2a).

**Assumptions of EOQ (know these — examiners test them):** (i) demand is known and constant; (ii) ordering cost per order and carrying cost per unit are constant; (iii) price per unit is constant — *no quantity discounts* (if discounts exist, EOQ must be tested against discount break-points separately); (iv) the entire order is delivered at once; (v) lead time is known; (vi) no stock-outs are permitted. Reality violates all of these, which is exactly why we bolt on the *levels* of 4.1 as shock absorbers.

**Unit-consistency warning (a silent killer).** A and C must be on the *same time basis*. If A is annual, C must be per unit **per year**. If a problem gives monthly demand, either annualise it or keep everything monthly — but never mix. The √ hides the error, so a mixed-basis EOQ still "looks" plausible; discipline on units is your only defence.

**Effect of parameter changes (a favourite theory-cum-numerical twist).** Because EOQ ∝ √(A·O / C):
- If **demand quadruples**, EOQ only **doubles** (√4 = 2) — ordering does not scale linearly with volume.
- If **ordering cost doubles**, EOQ rises by √2 ≈ 41%, not 100%.
- If **carrying cost doubles**, EOQ *falls* by a factor of √2. Examiners test whether you know the square-root damping, not just the formula.

#### 4.2a EOQ with Quantity Discounts (the most common EOQ trap)

When a supplier offers a lower **price per unit** for larger lots, the plain EOQ can be wrong, because a bigger order — though it raises carrying cost — may slash the **purchase price** of the entire annual quantity. Now the relevant total cost must include purchase price:

> **Total Annual Cost = (A × Price) + (A/Q × O) + (Q/2 × C)**

The decision procedure:
1. Compute the plain EOQ at the base price.
2. For **each** discount slab, evaluate total annual cost at the *smallest quantity that earns that slab's price* (because within a slab, cost rises with Q, so the slab's lowest qualifying quantity is its best point) — unless the EOQ itself falls inside the slab, in which case use the EOQ.
3. Pick the quantity with the **lowest total annual cost**, comparing purchase + ordering + carrying together.

Note carrying cost C often itself depends on price (if C = % × price), so **recompute C at each slab's price.** Fully worked in Example 6.

### 4.3 Valuation of Material Issues

When identical units bought at different prices are issued, we assume a cost-flow order. ICAI recognises several methods; the big three below plus a family of "average / notional price" methods you should be able to name and apply.

**FIFO (First-In-First-Out).** Assume the **oldest** stock is issued first. Closing stock is valued at the **most recent** prices.
- *Logic & effect:* physically sensible (you use up old stock first to avoid spoilage). In **rising prices**, issues are charged at old (low) prices → **lower cost → higher profit**; closing stock at new (high) prices → **higher balance-sheet stock value**.

**LIFO (Last-In-First-Out).** Assume the **newest** stock is issued first. Closing stock sits at **old** prices.
- *Logic & effect:* charges production at prices closest to current replacement cost. In **rising prices**, issues at new (high) prices → **higher cost → lower profit** (and lower reported tax, historically its attraction); closing stock understated at old prices. *Note: LIFO is not permitted under Ind AS-2 / AS-2 for financial reporting, but remains examinable in cost accounting.*

**Weighted Average.** After each receipt, recompute one blended rate:

> **Weighted Average Rate = Total value of stock on hand ÷ Total units on hand**

All issues until the next receipt go out at this rate.
- *Logic & effect:* smooths price fluctuations; issue price lies between FIFO and LIFO; profit and stock values sit in the middle. Preferred when prices swing and you want a stable, un-manipulable cost.

**The other named methods (know the definition and the one-line "when used"):**

| Method | Issue priced at | Notable feature / when used |
|---|---|---|
| **Simple Average** | Average of the *rates* of lots in stock (ignores quantities) | Crude; can violate the reconciliation check because it ignores quantity weighting — flagged by examiners as theoretically unsound |
| **Periodic Weighted Average** | One rate for the whole period = total value ÷ total units for the period | Computed at period-end, not after each receipt; simpler but not real-time |
| **HIFO (Highest-In-First-Out)** | Highest-priced lot issued first | Conservative; keeps stock at lowest values; rare, used to suppress reported stock value |
| **Replacement / Market Price** | Current market price on the date of issue | Charges production at what it would cost to replace *today*; used in volatile markets; a *notional* price |
| **Standard Price** | A pre-set standard rate | Any difference vs actual is a **price variance**; links to standard costing; simplifies clerical work |
| **Base Stock** | A minimum "base" quantity is always carried at its original old price; issues above base priced by FIFO/LIFO | Not a standalone method — a layer on top of FIFO/LIFO |

*Distinction the exam probes:* **actual-price methods** (FIFO, LIFO, HIFO, averages) recover *exactly* the money spent — the reconciliation Opening + Purchases = Issues + Closing holds to the rupee. **Notional-price methods** (replacement, standard) deliberately do *not* — they price issues at a price the firm may never have paid, throwing up a variance that must be written to Costing P&L. Simple average is an actual-price method in intent but, because it ignores quantities, it can *fail* the reconciliation — that failure is itself an examinable criticism.

**Master rule of thumb (rising prices):**

| | Issue cost | Profit | Closing stock value |
|---|---|---|---|
| **FIFO** | Lowest | Highest | Highest |
| **LIFO** | Highest | Lowest | Lowest |
| **Wtd Avg** | Middle | Middle | Middle |

(In **falling** prices, reverse FIFO and LIFO.) A guaranteed reconciliation check across any actual-price method: **Opening stock + Purchases = Issues (charged to production) + Closing stock**, in *both* value and quantity.

```mermaid
flowchart TD
  ROOT["Pricing material issues"] --> ACT["Actual price methods<br/>recover exactly what was paid"]
  ROOT --> NOT["Notional price methods<br/>price at a chosen rate<br/>throw up a variance"]
  ACT --> COST["Cost based<br/>FIFO LIFO HIFO base stock"]
  ACT --> AVG["Average based<br/>simple and weighted average"]
  NOT --> STD["Standard price"]
  NOT --> REP["Replacement or market price"]
```
*Figure 2 — Family tree of issue-pricing methods; the actual-versus-notional split decides whether a price variance appears.*

### 4.4 Stock Losses — Wastage, Scrap, Spoilage, Defectives

Loss of material is inevitable; the costing question is always the same: **was it normal (inherent, unavoidable, expected) or abnormal (avoidable, exceptional, a signal something broke)?** The *treatment* depends entirely on that classification.

The **golden principle:**

> **Normal loss** is expected, so its cost is **absorbed by the good output** — the cost of the good units is inflated to carry the normal loss. **Abnormal loss** is not expected, so it is **charged to the Costing Profit & Loss Account** and kept *out* of product cost — otherwise a controllable failure would be hidden inside product cost and never investigated.

The four forms of loss:

| Term | What it is | Realisable value? | Treatment |
|---|---|---|---|
| **Waste** | Portion with **no measurable recovery** — evaporation, smoke, shrinkage, dust; may even cost money to dispose. | Usually nil (may be negative disposal cost). | Normal waste: absorbed by good output (raises unit cost). Abnormal waste: cost to Costing P&L. |
| **Scrap** | Residue with a **small but definite sale value** — metal turnings, off-cuts, trimmings. | Yes, small. | Normal scrap sale value credited to overhead / job / material cost (reduces cost). Abnormal scrap sale credited to Costing P&L. |
| **Spoilage** | Units so damaged they **cannot be rectified** and are sold as seconds/junk. | Sold at low value. | Normal spoilage cost (net of recovery) borne by good output. Abnormal spoilage net cost to Costing P&L. |
| **Defectives** | Units that **can be rectified** by extra work and then sold as good. | Rectifiable. | Normal: rectification cost charged to good output/overhead. Abnormal: rectification cost to Costing P&L. |

**Computing the cost of an abnormal loss** (the exam-favourite manoeuvre): first spread the *total* cost over *expected good output* (i.e. after removing normal loss) to get a **cost per good unit**, then value the abnormal-loss units at that rate, net of any scrap recovered. Fully worked in Example 5 below.

*Why value abnormal loss at the "good unit" cost?* Because the normal loss was always going to happen — it is a legitimate cost of producing good units. The abnormal loss is *extra* units lost that *should* have been good; they must be valued at what a good unit costs and written off, so management sees the true rupee bleed.

**Abnormal GAIN — the mirror image (frequently paired with abnormal loss).** Sometimes actual output *exceeds* expected good output — the process lost *less* than the normal allowance. That surplus is **abnormal gain**. Its treatment is the exact reverse of abnormal loss:
- Value abnormal-gain units at the **same cost-per-good-unit** rate.
- **Debit** the process/good output and **credit** the Costing P&L (abnormal gain is a *credit*, an income, in Costing P&L).
- But there is a subtlety on scrap: because you produced *fewer* scrap/normal-loss units than expected, the scrap revenue you assumed for normal loss is *overstated*. So the abnormal gain credited to Costing P&L is reduced by the scrap value of the normal-loss units that did **not** actually arise. Worked in Example 7.

*Why abnormal gain is a credit, not just "negative loss":* the good output was valued at a rate that already loaded the *full* normal loss. When less loss actually occurred, good output has been slightly over-costed; the abnormal gain account corrects this by returning the excess to profit — while still keeping product cost at the honest "normal" rate.

### 4.5 ABC Analysis — Selective Control

You cannot lavish equal attention on every one of 10,000 stock items — controlling a ₹5 washer as tightly as a ₹5-lakh engine is a waste of managerial time. **ABC analysis** ("Always Better Control") applies the Pareto principle to inventory: a *small fraction of items accounts for a large fraction of value.*

| Class | Typical share of items | Typical share of value | Control policy |
|---|---|---|---|
| **A** | ~10% | ~70% | Tight: low safety stock, frequent review, EOQ enforced, senior sign-off, perpetual records. |
| **B** | ~20% | ~20% | Moderate control, periodic review. |
| **C** | ~70% | ~10% | Loose: bulk orders, large safety stock, simple two-bin system, minimal paperwork. |

*Why bother?* Managerial attention is itself a scarce, costly resource. ABC channels it where rupees are at stake. Note it classifies by **annual consumption value (quantity × unit price)**, *not* by unit price alone — a cheap item consumed in huge volumes can be a Class-A item.

**How to actually *build* an ABC classification (an examinable procedure, not just a table):**
1. For each item compute **annual consumption value = annual quantity × unit price**.
2. **Rank** items descending by that value.
3. Compute the **cumulative % of value** and **cumulative % of items**.
4. Draw the cut-offs: the top items contributing ~70% of value = A, the next ~20% = B, the rest = C. (Percentages are indicative, not rigid — the *shape* of the cumulative curve decides the cuts.)

**Cousin techniques — name, basis, and the *situation* each fits:**

| Technique | Classifies by | Best when |
|---|---|---|
| **VED** | Criticality: Vital / Essential / Desirable | Spare parts — a cheap vital gasket can halt a plant, so criticality beats value |
| **FSN** | Movement: Fast / Slow / Non-moving | Detecting dead/obsolete stock; drives write-off and disposal decisions |
| **HML** | Unit price: High / Medium / Low | Deciding authorisation levels for purchase, regardless of consumption |
| **SDE** | Availability: Scarce / Difficult / Easy to obtain | Setting safety stock for hard-to-source imports |
| **FNSD / GOLF / SOS** | Various (movement, source, seasonality) | Situational; know that they exist |

The examiner's favourite contrast: **ABC ignores criticality; VED captures it.** A Class-C (low value) item may be VED-Vital — so a *combined* ABC-VED matrix is used in practice for spares.

---

## 5. Worked Examples — Full Step-by-Step

### Example 1 — EOQ, order frequency, and total cost (foundation)

**Data.** A factory consumes **12,000 units** of a raw material per year. Ordering cost is **₹150 per order**. The material costs **₹20 per unit**, and carrying cost is **20% of unit value per year**.

**Required.** (a) EOQ, (b) number of orders per year, (c) time between orders, (d) total ordering, carrying and inventory cost at EOQ.

**Solution.**

*Step 1 — identify the primitives.*
- A = 12,000 units/yr ; O = ₹150/order.
- C = 20% × ₹20 = **₹4 per unit per year.**

*Step 2 — EOQ (set ordering = carrying, i.e. the formula).*

EOQ = √(2 × A × O / C) = √(2 × 12,000 × 150 / 4) = √(3,600,000 / 4) = √900,000 = **√900000 = 948.68 ≈ 949 units.**

Let me keep it exact: 2 × 12,000 × 150 = 36,00,000; ÷ 4 = 9,00,000; √9,00,000 = **948.68 units** (≈ 949).

*Step 3 — number of orders per year* = A / EOQ = 12,000 / 948.68 = **12.65 orders** (≈ 13 orders).

*Step 4 — time between orders* = 365 / 12.65 = **28.9 days** (≈ every 29 days).

*Step 5 — costs at EOQ.*
- Ordering cost = (A/EOQ) × O = 12.65 × 150 = **₹1,897.4**
- Carrying cost = (EOQ/2) × C = (948.68/2) × 4 = 474.34 × 4 = **₹1,897.4**
- **Self-check: the two are equal — the hallmark of a correct EOQ.** ✓
- Total inventory cost (excl. purchase price) = 1,897.4 + 1,897.4 = **₹3,794.8**

*Interpretation.* Ordering ~949 units about 13 times a year minimises the combined ordering-plus-carrying cost at roughly ₹3,795. Order much bigger and carrying cost balloons; much smaller and ordering cost balloons.

---

### Example 2 — Proving EOQ is genuinely the minimum (a cost table)

**Data.** Same as Example 1 (A = 12,000, O = ₹150, C = ₹4). Let's tabulate total cost at several order sizes to *see* the U-shaped curve bottom out near EOQ.

| Order Qty (Q) | No. of orders (A/Q) | Ordering cost = orders × 150 (₹) | Avg stock (Q/2) | Carrying cost = (Q/2)×4 (₹) | **Total (₹)** |
|---|---|---|---|---|---|
| 400 | 30.0 | 4,500 | 200 | 800 | **5,300** |
| 600 | 20.0 | 3,000 | 300 | 1,200 | **4,200** |
| 800 | 15.0 | 2,250 | 400 | 1,600 | **3,850** |
| **949 (EOQ)** | 12.6 | 1,897 | 474 | 1,897 | **3,794** |
| 1,200 | 10.0 | 1,500 | 600 | 2,400 | **3,900** |
| 1,600 | 7.5 | 1,125 | 800 | 3,200 | **4,325** |

The total-cost column dips to its **minimum right at EOQ (~₹3,794)** and rises on either side — a live demonstration that EOQ is the trough of the U, not an arbitrary formula. Also note that only at Q = 949 do ordering and carrying costs coincide (₹1,897 each).

**Read the flatness.** Move from Q = 949 to Q = 1,200 (a 26% larger order) and total cost rises only from ₹3,794 to ₹3,900 — about **2.8%**. This is the *robustness* of EOQ mentioned in Section 3.1: being modestly off EOQ costs almost nothing, which is why real firms happily round EOQ to a convenient pack/truck size. The penalty for error is small *near* the trough and grows only as you move far away (Q = 400 costs 40% more).

```mermaid
graph LR
  A["Small orders<br/>Q low"] -->|"many orders"| B["High ordering cost"]
  A -->|"low avg stock"| C["Low carrying cost"]
  D["Large orders<br/>Q high"] -->|"few orders"| E["Low ordering cost"]
  D -->|"high avg stock"| F["High carrying cost"]
  B --> G["EOQ = balance point<br/>ordering cost = carrying cost<br/>Total cost minimised"]
  C --> G
  E --> G
  F --> G
```
*Figure 3 — The two-cost tug-of-war: EOQ sits exactly where the opposing pressures balance.*

---

### Example 3 — Full stock-level computation (exam-standard)

**Data.** For component "X":
- Normal usage: **300 units/week**; Minimum usage: **200 units/week**; Maximum usage: **400 units/week**.
- Re-order (delivery) period (lead time): **4 to 6 weeks**.
- Re-order Quantity (EOQ): **2,400 units**.
- Emergency delivery time: **1 week**.

**Required.** Re-order level, Minimum level, Maximum level, Danger level, Average stock level.

**Solution.** Work strictly from the formulae in 4.1, plugging max/min correctly.

*Step 1 — Re-order Level = Maximum usage × Maximum lead time*
= 400 × 6 = **2,400 units.**

*Step 2 — Minimum Level = ROL − (Average usage × Average lead time)*
Average usage = 300 (given as "normal"); Average lead time = (4 + 6)/2 = 5 weeks.
= 2,400 − (300 × 5) = 2,400 − 1,500 = **900 units.**

*Step 3 — Maximum Level = ROL + ROQ − (Minimum usage × Minimum lead time)*
= 2,400 + 2,400 − (200 × 4) = 4,800 − 800 = **4,000 units.**

*Step 4 — Danger Level = Average usage × Emergency lead time*
= 300 × 1 = **300 units.**

*Step 5 — Average Stock = Minimum level + ½ ROQ*
= 900 + ½ × 2,400 = 900 + 1,200 = **2,100 units.**
(Cross-check via ½(min + max) = ½(900 + 4,000) = 2,450 — the two formulas differ slightly because the "½ ROQ" version assumes stock swings between minimum and minimum+ROQ, while the max/min version uses the extreme peak; ICAI accepts the **Minimum + ½ ROQ = 2,100** form as the standard answer. State the formula you used.)

*Interpretation & ordering of the lines (sanity check):* Danger (300) < Minimum (900) < Re-order (2,400) < Maximum (4,000). This ordering must always hold — if your danger level exceeds your minimum, or reorder exceeds maximum, you've mis-plugged a max/min somewhere.

**What if the examiner tweaks it?** Two common twists:
1. *"Usage given per day, lead time in weeks."* Convert to a common unit first (e.g. multiply daily usage by 7, or express lead time in days). Mixing days and weeks is the No. 1 levels error after the max/min mix-up.
2. *"Compute safety stock separately."* Safety stock = Minimum level here = 900 (the buffer left when the lot lands on an average day). Equivalently Max·Max − Avg·Avg = 2,400 − 1,500 = 900. Both routes agree — a built-in check.

```mermaid
flowchart TD
  MAX["Maximum Level<br/>4000 units<br/>ceiling: capital locked above here"]
  ROL["Re-order Level<br/>2400 units<br/>place a fresh order now"]
  MIN["Minimum Level<br/>900 units<br/>safety stock floor"]
  DAN["Danger Level<br/>300 units<br/>emergency purchase now"]
  MAX --> ROL
  ROL --> MIN
  MIN --> DAN
```
*Figure 4 — Stock levels as marked lines on the bathtub, from ceiling down to the emergency red line.*

---

### Example 4 — Material issue valuation under FIFO, LIFO and Weighted Average (with profit effect)

**Data.** Transactions for material "M" during March:

| Date | Transaction | Units | Rate ₹/unit |
|---|---|---|---|
| Mar 1 | Opening balance | 200 | 10 |
| Mar 5 | Purchase | 300 | 12 |
| Mar 10 | Issue | 400 | — |
| Mar 18 | Purchase | 400 | 15 |
| Mar 25 | Issue | 300 | — |

**Required.** Value the two issues and the closing stock under (a) FIFO, (b) LIFO, (c) Weighted Average, and comment on profit impact.

First, the physical reconciliation (identical across all methods):
Opening 200 + Purchases (300 + 400) = 900 units in. Issues 400 + 300 = 700 out. **Closing = 900 − 700 = 200 units.** ✓ Total value in = 200×10 + 300×12 + 400×15 = 2,000 + 3,600 + 6,000 = **₹11,600.**

---

**(a) FIFO — oldest issued first.**

| Date | Receipts | Issues | Balance |
|---|---|---|---|
| Mar 1 | — | — | 200 @ ₹10 = ₹2,000 |
| Mar 5 | 300 @ ₹12 = ₹3,600 | — | 200 @ ₹10 ; 300 @ ₹12 (₹5,600) |
| Mar 10 | — | **200 @ ₹10 + 200 @ ₹12 = 2,000 + 2,400 = ₹4,400** | 100 @ ₹12 = ₹1,200 |
| Mar 18 | 400 @ ₹15 = ₹6,000 | — | 100 @ ₹12 ; 400 @ ₹15 (₹7,200) |
| Mar 25 | — | **100 @ ₹12 + 200 @ ₹15 = 1,200 + 3,000 = ₹4,200** | 200 @ ₹15 = ₹3,000 |

- Total issues (to production) = 4,400 + 4,200 = **₹8,600.**
- **Closing stock = 200 @ ₹15 = ₹3,000** (newest prices).
- Check: 8,600 + 3,000 = 11,600 ✓

**(b) LIFO — newest issued first.**

| Date | Receipts | Issues | Balance |
|---|---|---|---|
| Mar 1 | — | — | 200 @ ₹10 = ₹2,000 |
| Mar 5 | 300 @ ₹12 | — | 200 @ ₹10 ; 300 @ ₹12 (₹5,600) |
| Mar 10 | — | **300 @ ₹12 + 100 @ ₹10 = 3,600 + 1,000 = ₹4,600** | 100 @ ₹10 = ₹1,000 |
| Mar 18 | 400 @ ₹15 | — | 100 @ ₹10 ; 400 @ ₹15 (₹7,000) |
| Mar 25 | — | **300 @ ₹15 = ₹4,500** | 100 @ ₹10 ; 100 @ ₹15 = 1,000 + 1,500 = ₹2,500 |

- Total issues = 4,600 + 4,500 = **₹9,100.**
- **Closing stock = ₹2,500** (100 @ ₹10 + 100 @ ₹15).
- Check: 9,100 + 2,500 = 11,600 ✓

**(c) Weighted Average — reblend after each receipt.**

| Date | Units | Value ₹ | Balance units | Balance ₹ | Wtd-avg rate ₹ |
|---|---|---|---|---|---|
| Mar 1 | +200 | 2,000 | 200 | 2,000 | 10.00 |
| Mar 5 | +300 | 3,600 | 500 | 5,600 | **11.20** (5,600/500) |
| Mar 10 | −400 | −4,480 | 100 | 1,120 | 11.20 |
| Mar 18 | +400 | 6,000 | 500 | 7,120 | **14.24** (7,120/500) |
| Mar 25 | −300 | −4,272 | 200 | 2,848 | 14.24 |

- Mar 10 issue = 400 × 11.20 = **₹4,480.** Mar 25 issue = 300 × 14.24 = **₹4,272.**
- Total issues = 4,480 + 4,272 = **₹8,752.**
- **Closing stock = 200 × 14.24 = ₹2,848.**
- Check: 8,752 + 2,848 = 11,600 ✓

**Comparison & profit comment (prices are rising: 10 → 12 → 15):**

| Method | Total issue cost (charged to production) | Closing stock value | Relative profit |
|---|---|---|---|
| FIFO | ₹8,600 (lowest) | ₹3,000 (highest) | **Highest** |
| LIFO | ₹9,100 (highest) | ₹2,500 (lowest) | **Lowest** |
| Wtd Avg | ₹8,752 (middle) | ₹2,848 (middle) | **Middle** |

Exactly as the master rule predicts: in rising prices FIFO charges the least to production (old cheap units) so it **shows the highest profit and the highest closing stock**, LIFO the opposite, weighted average in between. Same physical facts, three different profits — which is precisely why the choice is a *decision*, and why financial reporting (AS-2 / Ind AS-2) bans LIFO to prevent profit manipulation.

**Examiner tweak — a return to stores.** Suppose on Mar 27 production returns 50 units (originally issued Mar 25). Under **FIFO** the return is normally taken back into stock at the price of the *most recent issue it came from* (₹15 here) and sits as a fresh layer; under **weighted average** it re-enters at the current average rate (₹14.24), triggering a fresh reblend. Watch for the phrase "returned to stores" — it is a *receipt* for balance purposes but priced by a different rule than a purchase.

---

### Example 5 — Normal vs Abnormal loss valuation (the treatment that separates the two)

**Data.** A process is charged with **1,000 kg** of material at **₹50/kg** (total material ₹50,000). Additional processing cost (labour + overhead) = **₹20,000**. **Normal loss is 10%** of input; such loss (scrap) sells for **₹8/kg**. Actual output was **870 kg**.

**Required.** Value the good output, the normal loss, and the abnormal loss; show the Costing P&L treatment.

**Solution.**

*Step 1 — quantities.*
- Input = 1,000 kg. Normal loss = 10% × 1,000 = **100 kg.**
- Expected (good) output = 1,000 − 100 = **900 kg.**
- Actual output = 870 kg ⇒ **Abnormal loss = 900 − 870 = 30 kg.** (Total loss 130 kg = 100 normal + 30 abnormal.)

*Step 2 — cost per good unit (the crucial step).* Total cost put in = material 50,000 + processing 20,000 = **₹70,000.** From this, recover the scrap value of **normal** loss only: 100 kg × ₹8 = ₹800. Net cost to be spread over expected good output:

Cost per good kg = (Total cost − Normal-loss scrap value) ÷ Expected good output
= (70,000 − 800) ÷ 900 = 69,200 ÷ 900 = **₹76.89 per kg.**

*Why divide by 900, not 1,000?* Because the 100 kg normal loss is expected and its cost is legitimately absorbed by the 900 good units. We deliberately load the normal loss onto good output — that's the golden principle in action.

*Step 3 — value each stream at ₹76.89/kg.*
- **Good output:** 870 × 76.89 = **₹66,894** (this flows to the next process / finished goods).
- **Abnormal loss:** 30 × 76.89 = **₹2,306.67**, gross.

*Step 4 — Costing P&L treatment of abnormal loss.* The 30 abnormal-loss kg can still be sold as scrap at ₹8/kg = ₹240 recovery. So:
- Abnormal loss charged to **Costing Profit & Loss A/c** = 2,306.67 − 240 = **₹2,066.67 (net).**
- Normal loss: **no cost** carried (its cost already absorbed by good output); only its ₹800 scrap sale is realised and credited against process cost as done in Step 2.

*Reconciliation.* Value out = good output 66,894 + abnormal loss (at cost) 2,306.67 + normal-loss scrap credited 800 = 70,000.67 ≈ **₹70,000** (rounding). ✓ The cost input is fully accounted for.

*Interpretation.* By ring-fencing the ₹2,067 abnormal loss into the Costing P&L instead of burying it in product cost, management is *forced* to see and investigate the extra 30 kg that vanished. Had we simply divided ₹70,000 by 870 actual kg, product cost would silently swell and the failure would never surface — the entire reason cost accounting insists on the normal/abnormal split.

```mermaid
flowchart TD
  IN["Input 1000 kg<br/>Total cost Rs 70000"]
  IN --> GOOD["Good output 870 kg<br/>@ Rs 76.89 = Rs 66894<br/>to next process"]
  IN --> NL["Normal loss 100 kg<br/>expected and unavoidable<br/>cost absorbed by good output<br/>scrap Rs 800 credited"]
  IN --> AL["Abnormal loss 30 kg<br/>@ Rs 76.89 = Rs 2307<br/>less scrap Rs 240<br/>Rs 2067 to Costing P and L"]
```
*Figure 5 — Cost flow of a process: normal loss is absorbed by good output while abnormal loss is written off to Costing P&L for visibility.*

---

### Example 6 — EOQ with quantity discounts (the trap made explicit)

**Data.** Annual demand **A = 4,000 units.** Ordering cost **O = ₹100 per order.** Base price **₹50/unit.** Carrying cost is **10% of unit price per year.** The supplier offers:
- 0–999 units per order: ₹50.00/unit
- 1,000–1,999 units per order: ₹49.00/unit (2% off)
- 2,000+ units per order: ₹48.50/unit (3% off)

**Required.** Determine the order size that minimises **total annual cost (purchase + ordering + carrying).**

**Solution.** Because C depends on price, recompute it at each slab.

*Step 1 — plain EOQ at base price.* C = 10% × 50 = ₹5.
EOQ = √(2 × 4,000 × 100 / 5) = √(800,000 / 5) = √160,000 = **400 units.** This falls in the ₹50 slab, so 400 is the best point *within* that slab.

*Step 2 — evaluate total annual cost at the three candidate quantities:* the EOQ (400 @ ₹50), and the lowest qualifying quantity of each discount slab (1,000 @ ₹49; 2,000 @ ₹48.50). (Within a discount slab total cost rises with Q, so the slab's smallest qualifying quantity is its cheapest point.)

| | Q = 400 @ ₹50 | Q = 1,000 @ ₹49 | Q = 2,000 @ ₹48.50 |
|---|---|---|---|
| Purchase = A × price | 4,000×50 = 2,00,000 | 4,000×49 = 1,96,000 | 4,000×48.50 = 1,94,000 |
| Ordering = (A/Q)×100 | (10)×100 = 1,000 | (4)×100 = 400 | (2)×100 = 200 |
| Carrying = (Q/2)×(10%×price) | 200×5 = 1,000 | 500×4.90 = 2,450 | 1,000×4.85 = 4,850 |
| **Total annual cost (₹)** | **2,02,000** | **1,98,850** | **1,99,050** |

*Step 3 — decide.* Lowest total = **₹1,98,850 at Q = 1,000 units @ ₹49.** So the firm should **abandon the plain EOQ (400) and order 1,000 units** to capture the 2% discount — the purchase-price saving (₹4,000) outweighs the extra carrying cost.

*The lesson.* Plain EOQ ignored purchase price because it assumed price was constant. Once price varies with lot size, you *must* fold purchase cost into the comparison. Note also that the deepest discount (2,000 @ ₹48.50) is **not** best — its carrying cost (₹4,850) eats the extra price saving. Never assume "biggest discount wins."

---

### Example 7 — Abnormal gain (the mirror of Example 5)

**Data.** Same process as Example 5: input **1,000 kg** at ₹50, processing **₹20,000**, normal loss **10%** with scrap value **₹8/kg**. But this time actual output was **920 kg** (the process performed *better* than expected).

**Required.** Compute abnormal gain and its Costing P&L treatment.

**Solution.**

*Step 1 — quantities.* Expected good output = 900 kg (as before). Actual = 920 kg ⇒ **Abnormal gain = 920 − 900 = 20 kg.** Actual loss = 1,000 − 920 = 80 kg (less than the 100 kg normal allowance).

*Step 2 — cost per good unit (unchanged rate).* We still spread cost over **expected** good output of 900 kg, exactly as before: (70,000 − 800) ÷ 900 = **₹76.89/kg.** Keeping the rate at the *normal* basis is the whole point — good output stays honestly costed.

*Step 3 — value abnormal gain.* 20 kg × ₹76.89 = **₹1,537.78**, credited to the process (debited to the Abnormal Gain account, then to Costing P&L as income).

*Step 4 — scrap adjustment (the subtlety).* We assumed scrap on 100 kg of normal loss (₹800), but only 80 kg of loss actually occurred, so scrap on 20 kg (the "missing" loss) = 20 × ₹8 = **₹160** was over-credited to the process. This ₹160 must be *debited* to the Abnormal Gain account (it reduces the net gain, because that scrap income never materialised).

*Step 5 — net abnormal gain to Costing P&L.*
= Value of abnormal gain − scrap value forgone = 1,537.78 − 160 = **₹1,377.78 (credit / income) in Costing P&L.**

*Interpretation.* Abnormal gain is genuinely good news (less waste), so it lands as *income* in Costing P&L — but only after clawing back the scrap revenue we had optimistically assumed on loss that never happened. This scrap clawback is the single most-missed step; the examiner plants it deliberately.

---

### Example 8 — Inventory turnover ratio and slow-moving stock

**Data.** For three materials over a year:

| Material | Opening stock ₹ | Closing stock ₹ | Material consumed ₹ |
|---|---|---|---|
| P | 20,000 | 30,000 | 2,00,000 |
| Q | 40,000 | 60,000 | 1,00,000 |
| R | 15,000 | 25,000 | 2,20,000 |

**Required.** Inventory turnover ratio and average holding period for each; identify the slow-moving item.

**Solution.**

> **Inventory Turnover Ratio = Cost of material consumed ÷ Average stock**, where Average stock = ½(Opening + Closing).
> **Average holding period (days) = 365 ÷ Turnover ratio.**

| Material | Avg stock ₹ | Turnover = consumed ÷ avg | Holding period = 365 ÷ turnover |
|---|---|---|---|
| P | 25,000 | 2,00,000 / 25,000 = **8.0×** | 365 / 8 = **45.6 days** |
| Q | 50,000 | 1,00,000 / 50,000 = **2.0×** | 365 / 2 = **182.5 days** |
| R | 20,000 | 2,20,000 / 20,000 = **11.0×** | 365 / 11 = **33.2 days** |

*Interpretation.* A **high** turnover means stock is used up quickly (capital not locked, fresh stock, good). A **low** turnover means stock sits long — capital tied, risk of obsolescence. Here **Material Q turns only twice a year (183 days on the shelf)** — it is the **slow-moving** item that warrants investigation: over-ordering? falling demand? obsolete design? Material R, turning 11 times, is the healthiest.

*Why it matters:* turnover ratio is the diagnostic that feeds **FSN analysis** (Fast/Slow/Non-moving) and flags candidates for write-down. A ratio *trending down* year over year is an early warning of dead stock long before it becomes an outright write-off.

---

## 6. Presentation & Format — How to Lay It Out in the Exam

**Stores Ledger Control (perpetual inventory) format.** Whenever asked to value issues, present a three-block ledger — *Receipts | Issues | Balance* — each block showing Quantity, Rate, Amount. This is the format used in Example 4 and it is what earns method marks even if an arithmetic slip occurs.

| Date | Particulars | Receipts (Qty · Rate · Amt) | Issues (Qty · Rate · Amt) | Balance (Qty · Rate · Amt) |
|---|---|---|---|---|

**Levels answer.** Present each level as *Formula → substitution → answer*, then a one-line sanity ordering (Danger < Min < ROL < Max). Always state which usage/lead-time (max/min/avg) you used and why.

**EOQ answer.** State A, O, C explicitly (converting % carrying to ₹ per unit), give the formula, substitute, then the self-check "ordering cost = carrying cost". For **discount** problems, always present the *total annual cost* comparison table (purchase + ordering + carrying) — the marks are for the comparison, not the EOQ alone.

**Loss problems.** Show the quantity reconciliation first (input = good output + normal loss + abnormal loss), then the cost-per-good-unit computation, then value each stream, then the P&L line. End with the value reconciliation. For **abnormal gain**, remember the scrap clawback line.

**Cost of material purchased.** When asked to compute the rate at which material enters stores, show a build-up: *invoice price − trade discount − creditable GST + carriage inward + insurance + other charges ÷ net quantity received.* State explicitly that cash discount is excluded.

**Rounding convention.** EOQ and level answers are usually rounded up to whole units (you cannot order a fraction). Keep two decimals in rates until the final line to avoid compounding rounding error.

---

## 7. Connections — Where This Plugs Into the Rest of Costing

- **Cost Sheet (Ch. 06):** the *value of materials consumed* you compute here (Opening stock + Purchases + carriage inward − Closing stock − returns) is the very first line of the cost sheet — **Direct Material** feeding into Prime Cost. Material valuation choice therefore ripples into prime cost, works cost and profit.
- **Process Costing:** the normal/abnormal loss machinery of Section 4.4/Examples 5 & 7 is used *identically* in process costing, where abnormal loss and **abnormal gain** get their own ledger accounts. Master it here and process costing's loss accounting is free.
- **Overheads:** carrying cost, ordering cost and stores-department costs are themselves overheads; scrap recoveries are credited to overhead. Material control feeds overhead absorption.
- **Standard Costing:** the *standard price* method of issue valuation (Section 4.3) throws up a **material price variance**; the standard usage links to the **material usage variance**. This chapter's issue-pricing choice is the seedbed of variance analysis.
- **Marginal Costing / Decision-making:** EOQ is a mini optimisation — the same "minimise total of two opposing costs" logic reappears in make-or-buy and other decisions.
- **Working Capital (Financial Management):** average stock level, inventory turnover ratio and stock-holding period directly set the inventory component of the working-capital cycle. The bathtub you controlled here *is* the FM inventory conversion period.

---

## 8. Traps & Examiner Tricks

1. **Carrying cost given as a %.** If told "carrying cost is 10% of *average inventory value*" or "10% p.a.", you must convert to **₹ per unit per year = % × unit price** before using it as C in EOQ. Forgetting this is the No. 1 EOQ error.
2. **Ordering cost per order vs per annum.** O in EOQ is cost *per order*. If a total annual purchasing-department cost is given, do **not** plug it in raw — divide out or use only the per-order component.
3. **Max × Max vs Avg × Avg.** Re-order level uses **maximum** usage × **maximum** lead time; minimum level subtracts **average × average**; maximum level subtracts **minimum × minimum**. Mixing these up is the classic levels blunder. Memorise via logic (worst case for stock-out → maximums; best case for pile-up → minimums), not rote.
4. **Quantity discounts.** If the supplier offers a lower price for larger lots, EOQ is **not** automatically the answer. Compute total cost (purchase + ordering + carrying) at EOQ *and* at each discount break-point and pick the lowest — and remember the deepest discount need not win (Example 6).
5. **Dividing total cost by *actual* output in loss problems.** Cost per good unit must use **expected** good output (input − normal loss), *not* actual output. Using actual output wrongly buries abnormal loss in product cost.
6. **Scrap value of normal vs abnormal loss.** Normal-loss scrap reduces the cost spread over good units (credited in the cost-per-unit step). Abnormal-loss scrap is netted against the abnormal loss taken to Costing P&L. In **abnormal gain**, claw back the scrap on the normal loss that *didn't* occur. Don't double-count or mis-route them.
7. **Weighted average must be *re-computed after every receipt***, not once at the end (that would be "periodic weighted average," a different method). Also, an *issue* does **not** change the rate — only a receipt does.
8. **FIFO vs LIFO profit direction depends on price trend.** The "FIFO = higher profit" rule holds only in **rising** prices; reverse it if the question has falling prices. Read the price sequence before quoting the rule.
9. **ABC by value, not unit price.** A ₹2 item consumed 5,00,000 times a year is Class A. Classify by **annual consumption value**, never by sticker price alone. And ABC ignores criticality — a vital cheap spare needs VED, not ABC.
10. **Danger level formula variants.** Standard ICAI: Average usage × emergency lead time. Some problems specify "reorder period for emergency purchase" — use that as the lead time. If the question hands you a different definition, follow the question.
11. **Cash discount inside material cost.** Cash discount is a *financial* item and is **excluded** from material cost; only trade discount is deducted. Creditable GST is excluded; non-creditable GST is added. Carriage inward is added. Getting this build-up wrong corrupts the very first cost-sheet line.
12. **Units mismatch in EOQ / levels.** Annual demand with per-unit-*per-year* carrying cost; usage and lead time on the same time basis. The √ (EOQ) and the multiplication (levels) both hide a units error, so it survives to the final answer undetected. Check units *before* substituting.
13. **Bin card vs stores ledger.** Bin card = quantity only, kept by storekeeper; stores ledger = quantity and value, kept in costing. A question asking "which record shows value?" wants *stores ledger*. Don't swap them.
14. **Simple average pitfall.** Simple average of *rates* ignores quantities and can break the Opening + Purchases = Issues + Closing reconciliation — if a question quietly uses it, note the theoretical objection for extra marks.

---

## 9. First-Principles Recap

Strip everything back and material costing rests on five irreducible ideas:

1. **Material is the biggest, leakiest cost**, so it earns the most control machinery — a *chain of custody* with a document at every link (requisition → PO → GRN → bin card / stores ledger → requisition note). Control means keeping stock in a safe band (the bathtub) and pricing what leaves the godown honestly.
2. **How much to order** is a tug-of-war between ordering cost (falls with big lots) and carrying cost (rises with big lots). Their balance point is EOQ — rebuildable any time by setting the two costs equal. When price varies with lot size, fold purchase cost in and compare total annual cost.
3. **When to order and how far stock may swing** is a safety-buffer problem driven by uncertain usage and uncertain lead time. Re-order/min/max/danger levels are pre-computed lines: worst case (maximums) protects against stock-out, best case (minimums) bounds the pile-up. The system pushes daily control to the storekeeper and reserves judgement for management.
4. **Pricing issues and treating losses** are about *not lying* to management. Issue-valuation assumptions (FIFO/LIFO/WA and the notional-price methods) change profit, so choose deliberately. Losses are split normal (absorbed by good output — it was always going to happen) vs abnormal (written off to Costing P&L — so failure is visible); abnormal *gain* is the mirror income.
5. **Attention is scarce**, so control is *selective* — ABC by rupee value, VED by criticality, FSN by movement, HML by price. Turnover ratio is the diagnostic that tells you whether stock is working or rotting.

If you can regenerate every formula in this chapter from these five ideas, you never have to memorise a single one.

---

## 10. Quick-Revision Sheet

**Procurement documents**

| Document | Records | Kept by |
|---|---|---|
| Purchase Requisition | Authorised need | Stores/Dept |
| Purchase Order | Commitment to supplier | Purchasing |
| Goods Received Note | Arrival + inspection | Receiving |
| Bin Card | Quantity only | Storekeeper |
| Stores Ledger | Quantity + **value** | Costing office |
| Material Requisition Note | Authorised issue | Production → Stores |

**Cost of material purchased**

> Invoice price − trade discount − creditable GST + carriage inward + insurance in transit + other charges (non-creditable duty, commission). **Cash discount excluded** (financial item).

**Inventory Levels**

| Item | Formula |
|---|---|
| Re-order Level (ROL) | Maximum usage × Maximum lead time |
| ROL (alt) | Safety stock + (Avg usage × Avg lead time) |
| Minimum Level | ROL − (Average usage × Average lead time) |
| Maximum Level | ROL + ROQ − (Minimum usage × Minimum lead time) |
| Danger Level | Average usage × Emergency lead time |
| Average Stock | Minimum level + ½ ROQ = ½ (Min + Max) |
| Safety stock | Max·Max − Avg·Avg (lead-time + usage buffer) |

**EOQ block**

| Item | Formula |
|---|---|
| EOQ | √(2 × A × O / C) |
| A | Annual demand (units) |
| O | Ordering cost per order (₹) |
| C | Carrying cost per unit per year = carrying % × unit price |
| No. of orders/yr | A ÷ EOQ |
| Time between orders | 365 ÷ (A/EOQ) days |
| Ordering cost | (A/EOQ) × O |
| Carrying cost | (EOQ/2) × C |
| **Check at EOQ** | Ordering cost = Carrying cost |
| Total inventory cost | (A/EOQ)×O + (EOQ/2)×C |
| With discounts | Minimise (A×price) + ordering + carrying across slabs |

**Issue valuation (rising prices)**

| Method | Issue cost | Profit | Closing stock |
|---|---|---|---|
| FIFO | Lowest | Highest | Highest |
| LIFO | Highest | Lowest | Lowest |
| Wtd Avg | Middle | Middle | Middle |
| Wtd-avg rate | Value on hand ÷ Units on hand (recompute after each receipt) |
| Notional methods | Standard / replacement price → throw up a variance |
| Universal check | Opening + Purchases = Issues + Closing (qty & value) |

**Losses**

| Type | Recovery | Treatment |
|---|---|---|
| Waste | Nil / negative | Normal → absorbed by good output; Abnormal → Costing P&L |
| Scrap | Small sale value | Normal scrap credited to cost/overhead; Abnormal scrap → Costing P&L |
| Spoilage | Low (sold as seconds) | Normal net cost → good output; Abnormal net → Costing P&L |
| Defectives | Rectifiable | Normal rectification → good output/OH; Abnormal → Costing P&L |
| Abnormal loss value | = (Total cost − normal-loss scrap) ÷ **expected good output** × abnormal units, less its own scrap |
| Abnormal gain value | = same rate × gain units, **less** scrap on normal loss that did not occur → credit Costing P&L |

**ABC & cousins**

| Class | ~% items | ~% value | Control |
|---|---|---|---|
| A | 10% | 70% | Tight, low safety stock, frequent review |
| B | 20% | 20% | Moderate |
| C | 70% | 10% | Loose, bulk buy, high safety stock |

*Classify by annual consumption value (qty × price), not unit price. Cousins: VED (criticality), FSN (movement), HML (unit price), SDE (availability).*

**Inventory turnover**

> Turnover = Cost of material consumed ÷ Average stock ; Holding days = 365 ÷ turnover. Low/falling turnover ⇒ slow-moving/obsolete stock — investigate. High turnover ⇒ capital working hard.
