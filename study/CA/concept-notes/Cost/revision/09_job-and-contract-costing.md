# Chapter 09 — Job & Contract Costing

## Snapshot
When output is heterogeneous, averaging lies — so tag every cost to a unique identifier and never average across identifiers. **Job costing** — custom, one-off orders (printers, garages, fabricators); each order a distinct cost object. **Batch costing** — identical units in lots (batch = the job); cost/unit = batch cost ÷ units; EBQ optimises lot size. **Contract costing** — large, long, site-based jobs crossing accounting years, kept in the contractor's books, dominated by direct cost; needs prudence machinery for interim profit.

## Core concepts
- Job/Batch/Contract = one family, three sizes; decide by "which identifier owns this rupee?"
- Contract needs extra machinery because contracts cross years, are mostly direct cost, and payment is controlled by client certification.
- Prudence: **anticipate no profit, provide for all losses.** Recognise only a fraction of notional profit; the fraction grows with completion and is discounted again for cash received (retention risk).
- Job costing WIP = total of open (unfinished) job cost sheets.

## Key provisions / rules

**Job Cost Sheet:** Prime (DM+DL+Direct Exp) → +Works OH = Works Cost → +Admin OH = Cost of Production → +S&D OH = Total Cost → +Profit = Price.
- Profit on **cost** m%: Price = Cost × (1+m). Profit on **sales** m%: Price = Cost ÷ (1−m).
- Ledger: Dr WIP Control / Cr Stores, Wages, Production OH Control; on completion Dr Finished Goods (or Cost of Sales) / Cr WIP. Job carries absorbed (predetermined) OH.
- Spoilage from general cause → overhead (all jobs); from customer's special specification → charged to that job.

**Batch/EBQ:** EBQ = √(2DS ÷ C); setups/yr = D ÷ EBQ; at optimum total setup cost = total carrying cost; convert C to ₹ if given as % of cost; (1−d/p) factor only if both rates given.

**Contract vocabulary:**
- **Contract Price** = finish line, not revenue-to-date.
- **Work Certified** = value (at contract/selling price, incl. profit) of work approved by architect/surveyor to date; anchor for everything.
- **Work Uncertified** = done but not yet certified; carried at COST (no profit).
- **Retention Money:** Cash Received = Work Certified × (1 − retention%); Retention = Certified − Cash.
- **Notional Profit = Value of Work Done − Cost of Work Done**, where Value = Work Certified + Work Uncertified, and Cost of Work Done = costs incurred to date − closing (materials at site + plant WDV).
- **Estimated Total Profit = Contract Price − (Cost to date + Estimated cost to complete).**
- **% Completion = Work Certified ÷ Contract Price × 100.**

**Contract Account:** Dr = materials, wages (incl. accrued), direct expenses, plant (cost or depreciation), sub-contract, extra work, apportioned HO OH. Cr = materials at site c/d, plant WDV c/d, materials sold, WIP (Work Certified + Work Uncertified). Balancing figure = Notional Profit/Loss.

**Six fates of material:** consumed / at-site c/d / returned to stores / transferred to another contract / sold (profit-loss on sale → P&L) / lost (abnormal → P&L).

**Plant:** Method 1 (short) — debit plant at cost, credit closing WDV (difference = depreciation charged). Method 2 (long) — debit only depreciation, no cost-in/WDV-out. Hired plant — only hire charges debited. Both methods give identical notional profit.

**Prudence ladder (profit to P&L):**

| Completion | Transfer to P&L |
|---|---|
| < 25% | NIL |
| 25% to < 50% | ⅓ × NP × (Cash ÷ Certified) |
| 50% to < 90% | ⅔ × NP × (Cash ÷ Certified) |
| ≥ 90% | Est. Profit × (Cash ÷ Contract Price) [= Est.P × (Certified/Price) × (Cash/Certified)]; or cost-ratio variant Est.P × (Cost to date ÷ Est. total cost) [× Cash/Certified] |
| Any % with **notional loss** | **Full loss immediately** (no fraction, no cash ratio) |
| Any % with **overall estimated loss** (Est. total cost > Contract price) | **Full estimated loss immediately** |

Bands are conventions — if question states a policy, follow it; else state your assumption.

**Balance Sheet WIP** = (Certified + Uncertified) − Reserve − Cash received = Cost of work done + Profit recognised − Cash received. Reserve = Notional Profit − Profit recognised. Also show materials at site, plant WDV as assets; accrued wages as liability.

**Escalation clause** (protects contractor; de-escalation protects client):
- **Claim = Σ [Standard Qty allowed × (Actual Rate − Base Rate)]** — rate rise on STANDARD quantity only, never on wastage; net de-escalation if clause symmetric. Standard qty is for work actually done. Added to contract price.
- **Cost-plus contract:** price = allowable cost + agreed profit (fixed fee or % of cost); shifts inflation risk to client; cost-plus-% rewards overspending so clients cap/prefer fixed-fee; contractor's books open to client audit.

## Worked mini-example
Contract price ₹40,00,000. Cost of work done ₹20,50,000; Value of work done (Certified 24,00,000 + Uncertified 60,000) = 24,60,000 → Notional Profit ₹4,10,000. Cash received 85% = ₹20,40,000.
- % completion = 24,00,000 ÷ 40,00,000 = 60% → ⅔ band.
- Profit to P&L = ⅔ × 4,10,000 × (20,40,000 ÷ 24,00,000) = ⅔ × 4,10,000 × 0.85 = **₹2,32,333**.
- Reserve = 4,10,000 − 2,32,333 = ₹1,77,667.
- BS WIP = 24,60,000 − 1,77,667 − 20,40,000 = ₹2,42,333 (= 20,50,000 + 2,32,333 − 20,40,000 ✓).

## Exam traps & must-remember
- Compute % completion FIRST; don't grab ⅔ reflexively (20%→NIL, 40%→⅓, 92%→estimated basis).
- **Check overall loss BEFORE choosing a band** — if Est. total cost > Contract price, provide full estimated loss now regardless of % (highest-value trap).
- Never drop × (Cash ÷ Certified) in ⅓/⅔ formulas — plant a non-standard retention % to catch this.
- Add accrued/outstanding wages to debit.
- Plant: one method only (cost-in requires WDV-out; depreciation basis needs neither). Mid-year arrival → depreciate for months actually at site.
- Work Uncertified at cost (no profit); only Work Certified carries selling-price value.
- Loss transferred in full immediately — no ⅓/⅔, no cash ratio (asymmetry is the point).
- Escalation on standard qty × rate rise, never actual/wasteful qty; net de-escalation if symmetric.
- "Profit on cost" ≠ "profit on sales."
- Notional Profit (work to date) vs Estimated Profit (whole contract) — label separately.
- BS WIP: deduct BOTH reserve and cash received.
- EBQ: convert carrying-% to ₹.
- Lump-sum advance ≠ cash on certification (treat advance as liability unless equated).

## One-line recall
- Job = wallet per order; never average across identifiers.
- Notional Profit = Value of Work Done − Cost of Work Done; % completion = Certified ÷ Contract Price.
- Prudence ladder: <25% NIL, 25–50% ⅓, 50–90% ⅔, ≥90% estimated basis; all × (Cash/Certified).
- Losses full and immediate; overall estimated loss → provide entire loss now.
- Cash Received = Certified × (1 − retention%); BS WIP = (Certified+Uncertified) − Reserve − Cash.
- Escalation = Σ[Standard Qty × (Actual − Base Rate)]; EBQ = √(2DS/C).
