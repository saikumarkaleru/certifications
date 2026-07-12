# Chapter 08 — Unit & Batch Costing

## Snapshot
Two methods on the homogeneity spectrum. **Unit/Output/Single costing** — one homogeneous product, mass/continuous production (bricks, cement, steel, sugar, paper, power): divide period cost by period output via a Cost Sheet. **Batch costing** — identical articles in distinct lots (pharma, bakery, garments, printing, components): unit costing inside the batch, job costing between batches; the batch is the cost unit. **EBQ** decides optimum batch size. Decision test: "did these units consume resources identically?" All period → unit; per lot → batch; each order bespoke → job.

## Core concepts
- Division is honest only between identical things; grades/by-products need weighting, not blind division.
- "Cost per unit" is a family: prime/works/production/sales per unit — always ask "at which stage?"
- Setup cost is **fixed per batch/event** (same rupees whether 100 or 100,000 pieces) → makes batch size matter → drives EBQ. Remove setup or holding cost and EBQ collapses.
- EBQ = EOQ wearing a factory uniform (setup replaces ordering cost).

## Key provisions / rules

**Cost Sheet ladder:** Prime → (+Factory OH ±WIP −Normal scrap) Works Cost → (+Admin OH) Cost of Production → (±FG stock) COGS → (+S&D OH) Cost of Sales → (+Profit) Sales.

Key formulas:
- Direct Material Consumed = Op. RM + Purchases + Carriage In − Returns − Cl. RM
- Prime Cost = Direct Material + Direct Labour + Direct (Chargeable) Expenses
- Works Cost = Gross Works Cost + Op. WIP − Cl. WIP
- COGS = Cost of Production + Op. FG − Cl. FG
- Units sold = Op. FG + Produced − Cl. FG
- Profit p% on sales: Sales = Cost of Sales ÷ (1 − p); p% on cost: Sales = Cost × (1 + p)

**Stock stages:** RM before Prime; WIP at Works (valued at factory cost); FG at Cost of Production → COGS (valued at COP/unit). Closing FG at current year's COP/unit; opening FG at last year's rate (unless FIFO/WA specified).

**Scrap:** normal scrap sale deducted from works/factory cost; abnormal loss → Costing P&L.

**Carriage:** inward = material cost (before prime); outward = S&D (after COGS).

**Batch costing:**
- Total Batch Cost = Direct Materials + Direct Labour + Setup cost + Overheads absorbed.
- **Cost per unit = Total Batch Cost ÷ number of GOOD units** (normal rejects: divide by good units; abnormal spoilage stripped out to Costing P&L at cost less scrap).
- OH absorbed by labour/machine-hour rate OR % of direct cost — apply each block to its own base.
- Batch may span several orders: compute cost per good unit, then × order units.

**EBQ:**
- **EBQ = √(2 D S ÷ C)**  (D = annual demand, S = setup cost/batch, C = holding cost/unit/annum; if C = i% of price p, use C = i·p)
- **EBQ (gradual replenishment) = √(2DS ÷ [C(1 − d/p)])** — only when both production rate p and usage rate d given; gives a larger batch.
- Number of batches/year = D ÷ EBQ; Cycle = (EBQ ÷ D) × 360 days (or ×12 months, ×365).
- At EBQ: annual setup cost = annual holding cost (self-check).
- **Minimum total relevant cost = √(2 D S C)** = twice the setup (= twice the holding) at optimum.
- Curve is flat-bottomed → near-optimum round sizes cost almost nothing extra.
- Halving setup cost shrinks EBQ and total relevant cost by factor √2 (lean/SMED lever).

**Excluded (financial) items:** interest on loan/debentures, income tax, dividends, donations, transfer to reserves, loss/profit on sale of assets/investments, goodwill written off, fines, cash discount.

## Worked mini-example
Annual demand 24,000 strips; setup ₹1,200/batch; holding ₹4/strip p.a.
- EBQ = √(2×24,000×1,200 ÷ 4) = √1,44,00,000 = **3,795 strips**.
- Batches/year = 24,000 ÷ 3,795 = 6.3; Cycle = (3,795 ÷ 24,000) × 360 = 57 days.
- Check: setup (24,000/3,795)×1,200 = ₹7,589 ≈ holding (3,795/2)×4 = ₹7,590 ✓; total = √(2×24,000×1,200×4) = ₹15,179.
- Q=4,000 → total ₹15,200 (worse); Q=3,000 → ₹15,600 (worse).

## Exam traps & must-remember
- Purchases ≠ Material Consumed (adjust RM stock + carriage inward).
- WIP adjusted at Works, FG at COGS — never swapped.
- Closing FG at current year's COP/unit, not selling price/last year's rate.
- Cost of production ÷ units produced; cost of sales/profit relate to units sold.
- 20% on sales ⇒ cost = 80% of sales; 20% on cost ⇒ Sales = Cost × 1.20 (note: 20% on sales = 25% on cost).
- Divide batch by GOOD units (not units started) for normal rejects; abnormal loss to P&L (value at total-input rate less scrap).
- EBQ: convert holding % to ₹ (C = i·p); the Q/2 halving is already in the formula — don't halve again.
- Don't eyeball square roots — square the answer back (√1,44,00,000 = 3,795, not 4,000).
- Gradual-replenishment (1 − d/p) form ONLY when both production and usage rates given.
- "Cost of one batch" includes that batch's setup; annual trade-off uses (D/Q)·S — same S, two roles.
- Read the base of a % overhead (of wages vs prime cost vs works cost).
- Opening FG at last year's rate; only closing FG at current rate.

## One-line recall
- Unit costing = period cost ÷ period output (homogeneous mass output).
- Batch cost/unit = total batch cost ÷ good units; batch = the "job".
- EBQ = √(2DS/C); at optimum setup cost = holding cost; min total = √(2DSC).
- EBQ is EOQ with setup replacing ordering cost; flat-bottomed curve.
- Stock stages: RM before Prime, WIP at Works, FG at COP→COGS.
- Halving setup ⇒ EBQ and total cost fall by √2.
