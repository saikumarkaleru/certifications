# Cost & Management Accounting — HARD Reasoning-First Q&A (Q1–Q100)

*100 of the toughest CA-Intermediate questions — multi-step problems with twists, integrated cross-concept problems, and "analyse / advise / examine validity" case-style questions. Every answer carries a **"Why this way (the reasoning)"** block that explains the principle behind each step (and why the tempting wrong approach fails), so you learn to think, not memorise. Full chapter coverage, ICAI-depth working notes and statements.*

---

## Part C — HARD Reasoning-First Bank (Q1–Q100)

### Q1. Ch: Material Cost — EOQ with Quantity Discounts (Marks: 8) [Problem]
**Question:** A manufacturer uses 24,000 units of a raw material per year. The supplier offers the following price schedule. Ordering cost is ₹360 per order and carrying cost is 20% of the average inventory value per annum. Advise the economic order size.

| Order size (units) | Price per unit (₹) |
|---|---|
| Less than 3,000 | 20.00 |
| 3,000 to 5,999 | 19.60 |
| 6,000 and above | 19.20 |

**Solution:**

**WN-1 — Basic EOQ (ignoring discount):**
EOQ = √(2 × A × O ÷ C), where A = 24,000, O = ₹360, C = 20% × price.
At the lowest price the carrying cost is smallest, so test the EOQ at each price band and check feasibility.

At price ₹20: C = 20% × 20 = ₹4 → EOQ = √(2 × 24,000 × 360 ÷ 4) = √(17,280,000 ÷ 4)... 
= √(2 × 24,000 × 360 / 4) = √(4,320,000) ≈ **1,470 units** (feasible, this band is <3,000). 

**WN-2 — Total cost at each candidate order size.** Total Annual Cost = Purchase + Ordering + Carrying.
Ordering = (24,000 ÷ Q) × 360. Carrying = (Q ÷ 2) × (20% × price).

| Candidate Q | Price (₹) | Purchase (₹) | Ordering (₹) | Carrying (₹) | Total (₹) |
|---|---|---|---|---|---|
| 1,470 (EOQ @₹20) | 20.00 | 4,80,000 | 5,878 | 5,880 | 4,91,758 |
| 3,000 (min for ₹19.60) | 19.60 | 4,70,400 | 2,880 | 5,880 | 4,79,160 |
| 6,000 (min for ₹19.20) | 19.20 | 4,60,800 | 1,440 | 11,520 | 4,73,760 |

Carrying at Q=3,000, price 19.60: (3,000÷2)×(0.20×19.60)=1,500×3.92=₹5,880.
Carrying at Q=6,000, price 19.20: 3,000×3.84=₹11,520. Ordering at 6,000: 4×360=₹1,440.

**Answer:** The lowest total annual cost, **₹4,73,760, occurs at an order size of 6,000 units** (price ₹19.20). The firm should order **6,000 units per order**, not the textbook EOQ of 1,470.

**Why this way (the reasoning):** The plain EOQ formula minimises only *ordering + carrying* cost and silently assumes the purchase price is constant. When the supplier offers price breaks, the purchase cost itself becomes a variable that dwarfs the ordering/carrying trade-off — 24,000 units × even ₹0.40 saving = ₹9,600, far more than the few thousand rupees of inventory-cost movement. So the correct method is: compute the unconstrained EOQ, and then, for every price break *above* that EOQ, evaluate the *total* cost (purchase + ordering + carrying) at the minimum quantity that just qualifies for the discount. You buy the larger lot only if the price saving beats the extra carrying cost — which it does here. Testing only the EOQ, or comparing only ordering-plus-carrying, is the classic trap that loses the discount.

*(Full-marks tip: examiners award marks for computing purchase cost inside total cost — omit it and you cannot detect the discount. State clearly that the plain EOQ is rejected and why.)*

---

### Q2. Ch: Material Cost — EOQ with Stock-out / Shortage Cost (Marks: 8) [Problem]
**Question:** Annual demand is 12,000 units, evenly spread. Ordering cost ₹150 per order, carrying cost ₹6 per unit per annum. The firm is willing to permit planned shortages; back-orders cost ₹24 per unit per annum. Determine (i) the optimum order quantity, (ii) the maximum planned shortage, and (iii) the maximum inventory level. Compare with the no-shortage EOQ.

**Solution:**

**WN-1 — No-shortage EOQ (benchmark):** EOQ = √(2 × 12,000 × 150 ÷ 6) = √(6,00,000) ≈ **775 units**.

**WN-2 — EOQ permitting shortages:**
Q* = √(2AO/C) × √((C+S)/S), where S = shortage cost = ₹24.
√((C+S)/S) = √((6+24)/24) = √(30/24) = √1.25 = 1.1180.
Q* = 775 × 1.1180 ≈ **866 units**.

**WN-3 — Maximum shortage (B):** B = Q* × C/(C+S) = 866 × 6/30 = 866 × 0.20 = **173 units**.

**WN-4 — Maximum inventory (I):** I = Q* − B = 866 − 173 = **693 units**.

**Answer:** Optimum order quantity ≈ **866 units**; maximum planned shortage ≈ **173 units**; maximum inventory ≈ **693 units**. Permitting shortages *raises* the order size (775 → 866) but *lowers* the peak stock held (775 → 693).

**Why this way (the reasoning):** The shortage model recognises that carrying cost (₹6) is far cheaper than the back-order penalty (₹24), so the firm gladly holds more per order but deliberately runs the tail of each cycle "dry", meeting late demand from the next delivery. The factor √((C+S)/S) is always ≥ 1, so Q always increases relative to the classic EOQ — this makes intuitive sense: if being short is only mildly worse than holding stock, you order big and let a little shortage build up. Conversely the fraction C/(C+S) that governs the shortage is small because S ≫ C here (24 ≫ 6), so you permit only a modest shortage. The trap is to use the plain EOQ and ignore that a *cheap* carrying cost relative to a *dear* stock-out cost changes the optimum — the two costs must be balanced, not one ignored.

*(Full-marks tip: state that maximum inventory = Q − B, not Q; many candidates report Q as peak stock and lose the last mark.)*

---

### Q3. Ch: Material Cost — Stock Levels (Re-order, Max, Min, Average, Danger) (Marks: 8) [Problem]
**Question:** From the following, compute Re-order Level, Minimum Level, Maximum Level, Average Stock Level and Danger Level.

| Particulars | Data |
|---|---|
| Normal usage | 300 units/day |
| Minimum usage | 200 units/day |
| Maximum usage | 400 units/day |
| Re-order quantity | 3,600 units |
| Re-order period (lead time) | 10 to 15 days |
| Emergency purchase lead time | 4 days |

**Solution:**

**WN-1 — Re-order Level (ROL):** = Max usage × Max re-order period = 400 × 15 = **6,000 units**.

**WN-2 — Minimum Level:** = ROL − (Normal usage × Average re-order period) = 6,000 − (300 × 12.5) = 6,000 − 3,750 = **2,250 units**. (Average lead = (10+15)/2 = 12.5 days.)

**WN-3 — Maximum Level:** = ROL + ROQ − (Min usage × Min re-order period) = 6,000 + 3,600 − (200 × 10) = 9,600 − 2,000 = **7,600 units**.

**WN-4 — Average Stock Level:** = ½ (Min Level + Max Level) = ½ (2,250 + 7,600) = **4,925 units**. (Alternatively Min Level + ½ ROQ = 2,250 + 1,800 = 4,050 units — state assumption.)

**WN-5 — Danger Level:** = Normal usage × Emergency lead time = 300 × 4 = **1,200 units**.

**Answer:** ROL = 6,000; Minimum = 2,250; Maximum = 7,600; Average ≈ 4,925 (or 4,050 on the alternative basis); Danger = 1,200 units.

**Why this way (the reasoning):** Each level answers a different "worst-case vs normal" question, and the trick is matching the *right extreme* of usage and lead time to the purpose. ROL must protect against the *worst* case during lead time — the most you could consume (max usage) over the longest wait (max period) — so both maxima are used; anything less risks a stock-out. Minimum Level is the buffer expected to remain *if things go normally* after reordering, hence normal usage over the average lead time. Maximum Level guards against over-stocking: it assumes the *slowest* possible depletion (min usage over min lead time) so that a fresh ROQ arrives on top of an almost-full bin — the largest stock that can accumulate. Danger Level uses *normal* usage over the *emergency* lead time because it marks the point at which routine replenishment has failed and you must invoke emergency buying. Mixing up which extreme goes where is the single most common error.

*(Full-marks tip: for Average Stock the examiner accepts either formula — but you must state which one and be consistent; unstated assumptions cost marks.)*

---

### Q4. Ch: Material Cost — Inventory Turnover & Slow-Moving Stock (Marks: 6) [Problem]
**Question:** From the data below, compute the inventory turnover ratio and average holding period for each material, and comment on which material needs management attention.

| Material | Opening stock (₹) | Closing stock (₹) | Purchases (₹) |
|---|---|---|---|
| A | 20,000 | 30,000 | 1,80,000 |
| B | 25,000 | 15,000 | 55,000 |
| C | 40,000 | 60,000 | 30,000 |

**Solution:**

**WN-1 — Materials consumed = Opening + Purchases − Closing:**
A: 20,000 + 1,80,000 − 30,000 = ₹1,70,000. B: 25,000 + 55,000 − 15,000 = ₹65,000. C: 40,000 + 30,000 − 60,000 = ₹10,000.

**WN-2 — Average stock = ½(Opening + Closing):** A = 25,000; B = 20,000; C = 50,000.

**Statement Showing Inventory Turnover:**

| Material | Consumption (₹) | Avg stock (₹) | Turnover (times) | Holding period (days = 365÷turnover) |
|---|---|---|---|---|
| A | 1,70,000 | 25,000 | 6.80 | 54 |
| B | 65,000 | 20,000 | 3.25 | 112 |
| C | 10,000 | 50,000 | 0.20 | 1,825 |

**Answer:** Material **C** turns over only **0.20 times a year (≈ 5 years of holding)** — a slow-moving/near-dormant item tying up ₹50,000. It needs immediate attention: investigate obsolescence, stop further purchase, and dispose of surplus. A is the healthiest (6.8 times).

**Why this way (the reasoning):** Turnover ratio = consumption ÷ average stock measures how many times capital locked in an item is "recycled" through production in a year; a low ratio means money is sleeping in the stores. The reasoning trap is to look at closing stock value alone — C's ₹60,000 looks like just another balance — but relating it to how little is actually *consumed* (₹10,000) exposes that the firm holds five years' worth. High turnover frees working capital and reduces obsolescence/carrying risk; that is precisely why ABC-style attention is directed at the *slowest* movers, not the biggest balances. Consumption must be derived (Opening + Purchases − Closing), not read off directly — using purchases instead of consumption is the usual error.

*(Full-marks tip: show the consumption derivation explicitly and convert turnover to a holding period — the comment carries the marks, not the ratio alone.)*

---

### Q5. Ch: Material Cost — Pricing of Issues & Effect on Profit (Marks: 6) [Problem/Theory]
**Question:** In a period of steadily *rising* prices, a company is choosing between FIFO and Weighted Average for pricing material issues. Using the transactions below, compute the value of closing stock and cost of materials issued under both methods, and explain the effect on reported profit and on the balance-sheet stock value.

| Date | Receipts | Rate (₹) | Issues |
|---|---|---|---|
| 1st | 100 units | 10 | — |
| 10th | 100 units | 12 | — |
| 20th | — | — | 150 units |

**Solution:**

**WN-1 — FIFO issue (150 units):** first 100 @ ₹10 = ₹1,000, next 50 @ ₹12 = ₹600 → issue = **₹1,600**. Closing 50 units @ ₹12 = **₹600**.

**WN-2 — Weighted Average:** total cost = 1,000 + 1,200 = ₹2,200 for 200 units → rate ₹11. Issue 150 × 11 = **₹1,650**. Closing 50 × 11 = **₹550**.

**Statement:**

| Method | Cost of issue (₹) | Closing stock (₹) |
|---|---|---|
| FIFO | 1,600 | 600 |
| Weighted Average | 1,650 | 550 |

**Answer:** Under rising prices FIFO gives a *lower* issue cost (₹1,600 vs ₹1,650) → **higher reported profit** and a **higher, more current closing-stock value** (₹600 vs ₹550). Weighted Average smooths the price, charging a higher cost to production and reporting lower profit and lower stock.

**Why this way (the reasoning):** FIFO assumes the *oldest* (cheapest, in a rising market) units leave first, so production is charged historic low prices while the newest, dearest units stay in stock — hence lower cost of issue, higher profit, and a closing stock that reflects near-current replacement cost. Weighted Average blends old and new prices into one rate, so it charges production more than FIFO and leaves stock valued below current cost. The key conceptual point examiners test is *directionality*: in rising prices FIFO → higher profit & higher stock; the reverse holds when prices fall. Neither is "wrong" — but you must be able to explain that FIFO's higher profit is partly a holding gain, which is why in inflationary conditions it can overstate distributable profit.

*(Full-marks tip: link the numeric result to BOTH profit and balance-sheet stock, and note the rising-price condition explicitly — a generic "FIFO is higher" without the price-trend qualifier is marked down.)*

---

### Q6. Ch: Material Cost — Treatment of Losses (Waste/Scrap/Spoilage/Defectives) (Marks: 6) [Theory/Application]
**Question:** A production manager argues: "All material losses are the same — just reduce the good output and the per-unit cost sorts itself out." Examine the validity of this statement by distinguishing normal from abnormal loss, and state the correct costing treatment of waste, scrap, spoilage and defectives.

**Answer:**

**Governing principle.** Cost accounting distinguishes losses by (a) *controllability* — normal (inherent, unavoidable) vs abnormal (avoidable, arising from inefficiency), and (b) *nature* of the residue. The rule: the cost of **normal loss is absorbed by good units**; the cost of **abnormal loss is charged to the Costing P&L** (not to production), so that product cost is not distorted by inefficiency.

**Application to each:**
- **Waste** — residue with little/no measurable value (evaporation, smoke). Normal waste: its cost is spread over good output (raising their unit cost). Abnormal waste: costed like good units and written off to Costing P&L.
- **Scrap** — measurable residue with a *recoverable* sale value (metal turnings). Normal scrap realisation is credited to the job/overhead; abnormal scrap loss goes to P&L. Net cost, not gross, is absorbed.
- **Spoilage** — units so damaged they cannot be rectified. Normal spoilage cost (net of any disposal value) is borne by good output; abnormal spoilage is charged to Costing P&L.
- **Defectives** — units that *can be rectified* by extra work. Normal rectification cost is charged to the job/overhead; abnormal rectification cost goes to P&L.

**Conclusion.** The manager is **wrong**. Treating all losses identically would (i) hide inefficiency inside product cost, distorting pricing and control, and (ii) ignore recoverable scrap value. Only *normal* loss loads onto good units; *abnormal* loss must be isolated and written off so that management sees, and can act on, avoidable waste.

**Why this way (the reasoning):** The whole point of the normal/abnormal split is *managerial visibility and fair product cost*. If abnormal loss were buried in good-unit cost, every unit would look more expensive and no one could tell whether the extra cost was inherent or the result of a careless operator — control is lost and pricing is misled. Normal loss, by contrast, is a genuine, unavoidable cost of running that process, so it legitimately belongs to the units that survived. Distinguishing scrap (has value) from waste (has none) and spoilage (unrectifiable) from defectives (rectifiable) matters because each has a different *offsetting recovery* and a different *cost to fix* — lumping them together destroys both the value recovery and the accountability the system is designed to give.

*(Full-marks tip: examiners want the treatment stated separately for each of the four terms AND the normal/abnormal axis — a generic "charge to P&L" answer without the four-way distinction caps you at half marks.)*

---

### Q7. Ch: Material Cost — ABC Analysis + EOQ Integration (Marks: 8) [Problem/Application]
**Question:** A store holds 5 items. (i) Classify them under ABC analysis by annual consumption value. (ii) For the single 'A' item, given ordering cost ₹200/order and carrying cost 25% p.a. of unit cost, compute the EOQ and the number of orders. Advise the control policy per class.

| Item | Annual usage (units) | Unit cost (₹) |
|---|---|---|
| P | 1,000 | 500 |
| Q | 20,000 | 20 |
| R | 2,000 | 25 |
| S | 15,000 | 2 |
| T | 8,000 | 1.25 |

**Solution:**

**WN-1 — Annual consumption value & ranking:**

| Item | Usage | Unit cost | Annual value (₹) | % of total | Rank |
|---|---|---|---|---|---|
| P | 1,000 | 500 | 5,00,000 | 52.6% | 1 |
| Q | 20,000 | 20 | 4,00,000 | 42.1% | 2 |
| R | 2,000 | 25 | 50,000 | 5.3% | 3 |
| S | 15,000 | 2 | 30,000 | ... | 4 |
| T | 8,000 | 1.25 | 10,000 | ... | 5 |

Recompute totals: 5,00,000 + 4,00,000 + 50,000 + 30,000 + 10,000 = ₹9,90,000.
P = 50.5%, Q = 40.4%, R = 5.05%, S = 3.03%, T = 1.01%.

**WN-2 — ABC classification:** **A = P (≈50.5%)**; **B = Q (≈40.4%)** (or P+Q as A on ~91% cut); **C = R, S, T (≈9%)**. (State the cut-off used: A ≈ item(s) up to ~50–70% value, C = the low-value bulk.)

**WN-3 — EOQ for 'A' item P:** C = 25% × 500 = ₹125/unit p.a.
EOQ = √(2 × 1,000 × 200 ÷ 125) = √(4,00,000 ÷ 125) = √3,200 ≈ **57 units**.
Number of orders = 1,000 ÷ 57 ≈ **18 orders/year**.

**Answer:** P is the 'A' item; EOQ ≈ 57 units, ≈18 orders p.a. **Policy: A-items — tight control, frequent small orders, low safety stock, regular review; C-items — loose control, bulk orders, higher safety stock, infrequent review.**

**Why this way (the reasoning):** ABC applies the "vital few vs trivial many" principle: a small fraction of items usually accounts for the bulk of inventory value, so scarce management attention should be concentrated there. Note the deliberate trap — item Q has the *highest usage in units* (20,000) but is a 'B', while P with only 1,000 units is the top 'A', because classification is by *value* (usage × cost), not quantity. Ordering 'A' items in small, frequent EOQ lots minimises the large capital locked up and its 25% carrying cost, even at the price of more orders; for 'C' items the carrying cost is trivial, so you deliberately order big and rarely to save clerical/ordering effort. Applying the same tight control to a ₹1.25 item as to a ₹500 item would waste effort where it cannot pay — that is the insight ABC exists to deliver.

*(Full-marks tip: state your % cut-offs and justify why the high-quantity item Q is not automatically 'A' — that reasoning line is where marks are won.)*

---

### Q8. Ch: Employee (Labour) Cost — Halsey vs Rowan with Efficiency Twist (Marks: 8) [Problem]
**Question:** Standard time for a job is 40 hours; the wage rate is ₹50 per hour. A worker completes the job in 30 hours. Compute the total earnings, effective hourly rate, and labour cost per job under (i) Halsey (50% bonus), (ii) Rowan. Then show for what percentage of time saved the two schemes give equal earnings, and explain the significance.

**Solution:**

**WN-1 — Time saved:** 40 − 30 = 10 hours. Basic wages = 30 × ₹50 = ₹1,500.

**WN-2 — Halsey earnings:** Bonus = 50% × time saved × rate = 0.5 × 10 × 50 = ₹250.
Total = 1,500 + 250 = **₹1,750**. Effective rate = 1,750 ÷ 30 = **₹58.33/hr**.

**WN-3 — Rowan earnings:** Bonus = (Time saved ÷ Std time) × time taken × rate = (10÷40) × 30 × 50 = 0.25 × 1,500 = ₹375.
Total = 1,500 + 375 = **₹1,875**. Effective rate = 1,875 ÷ 30 = **₹62.50/hr**.

**WN-4 — When are the two equal?** Setting Halsey bonus = Rowan bonus:
0.5 × S × R = (S/Std) × (Std−S) × R ⇒ 0.5 = (Std−S)/Std ⇒ (Std−S)/Std = 0.5 ⇒ **time saved = 50% of standard time.**

**Statement Showing Earnings:**

| Scheme | Basic (₹) | Bonus (₹) | Total (₹) | Effective rate (₹/hr) |
|---|---|---|---|---|
| Halsey | 1,500 | 250 | 1,750 | 58.33 |
| Rowan | 1,500 | 375 | 1,875 | 62.50 |

**Answer:** Halsey ₹1,750; Rowan ₹1,875. The two schemes pay **equal earnings when time saved = 50% of standard time** (i.e., job done in 20 hrs here). Below 50% saving Rowan pays more; beyond 50% Halsey pays more.

**Why this way (the reasoning):** Both schemes share the time-saving gain between worker and employer, but they share it *differently*, and the crossover at 50% is the concept examiners probe. Halsey gives a *fixed fraction* (here 50%) of every hour saved, so its bonus rises linearly and without limit as the worker speeds up. Rowan's bonus, (saved/standard) × wages, is a *parabola* that peaks when exactly half the standard time is saved and then *falls* — a built-in brake that protects the employer against a loose standard: even if a worker finishes absurdly fast, Rowan can never pay more than double the basic rate, whereas Halsey can. That is why, at low savings (<50%), Rowan is more generous (rewarding modest gains), but for large savings (>50%), Halsey overtakes. The practical significance: Rowan is "safer" when time standards are unreliable; Halsey incentivises hard sprinting more strongly.

*(Full-marks tip: derive the 50% equality algebraically, not by trial — and state the direction of the inequality on each side of 50%. Effective-rate figures should reconcile with total ÷ hours worked.)*

---

### Q9. Ch: Employee (Labour) Cost — Rowan "Cannot Exceed Double" Property (Marks: 6) [Problem/Theory]
**Question:** A worker under the Rowan scheme claims that by working extremely fast he can earn far more than twice his time-rate for the hours he works. Standard time 20 hours, rate ₹40/hour. Test his claim at time taken of 10 hours and 4 hours, and prove the general property. Comment.

**Solution:**

**WN-1 — At 10 hours taken (saved 10):** Basic = 10×40 = ₹400. Bonus = (10/20)×400 = ₹200. Total = ₹600. Effective rate = 600/10 = **₹60/hr = 1.5× rate.**

**WN-2 — At 4 hours taken (saved 16):** Basic = 4×40 = ₹160. Bonus = (16/20)×160 = ₹128. Total = ₹288. Effective rate = 288/4 = **₹72/hr = 1.8× rate.**

**WN-3 — General proof.** Effective rate = Earnings ÷ Time taken = [Rate × T + (S/Std)(T×Rate)] ÷ T, where T = time taken, S = Std − T.
= Rate × [1 + S/Std] = Rate × [1 + (Std−T)/Std] = Rate × [ (2Std − T)/Std ].
As T → 0, effective rate → Rate × (2Std/Std) = **2 × Rate**, but never reaches it for T > 0.

**Answer:** The claim is **false**. The effective hourly rate under Rowan approaches but can **never exceed twice the time-rate** (₹80 here). At 10 hrs it is 1.5×, at 4 hrs 1.8× — rising towards, but always below, 2×.

**Why this way (the reasoning):** The algebra shows the effective rate equals Rate × (2Std − T)/Std, which is a decreasing function of T bounded above by 2×Rate. This is the built-in safeguard of the Rowan plan: the fraction of the wage paid as bonus, (Std−T)/Std, is capped at 1 (you cannot save more than the whole standard time), so the bonus can at most double the basic hourly earning. This is deliberate — it protects the employer from paying runaway bonuses if the time standard is set too loose, unlike Halsey where a fast worker's effective rate is unbounded. Understanding this ceiling explains *why* firms with shaky time standards prefer Rowan: the plan self-limits the damage from a bad standard.

*(Full-marks tip: the marks are in the algebraic proof of the 2× ceiling — a numerical demonstration alone is incomplete without showing effective rate = Rate(2Std−T)/Std.)*

---

### Q10. Ch: Employee (Labour) Cost — Labour Turnover: Replacement vs Separation vs Flux (Marks: 6) [Problem]
**Question:** During a year, a factory's records show: workers at start 4,800; at end 5,200; separations 120; workers discharged and replaced 40; new workers engaged 400 (of which some were to fill vacancies and some for expansion). Compute the labour turnover rate under (i) Separation method, (ii) Replacement method, (iii) Flux method. Reconcile the accessions.

**Solution:**

**WN-1 — Average number of workers:** (4,800 + 5,200) ÷ 2 = **5,000**.

**WN-2 — Accession split.** Total joined = 400. Net increase = 5,200 − 4,800 = 400 due to expansion... but separations were 120, so accessions must cover replacements + expansion. Replacements (to fill vacancies caused by separation) = 40 (given as replaced). New for expansion = 400 − 40 = 360.
Check: Opening 4,800 − separations 120 + accessions 400 = 5,080? That gives 5,080, not 5,200 — so reconcile: closing must equal opening − separations + accessions. To reach 5,200: accessions = 5,200 − 4,800 + 120 = **520**. Of these, replacements = separations replaced = 40, expansion = 520 − 40 = 480. (We take separations = 120, replacements = 40, expansion accessions = 480, total accessions = 520.)

**WN-3 — Rates:**
- Separation method = Separations ÷ Avg × 100 = 120 ÷ 5,000 × 100 = **2.40%**.
- Replacement method = Replacements ÷ Avg × 100 = 40 ÷ 5,000 × 100 = **0.80%**.
- Flux method = (Separations + Accessions) ÷ Avg × 100 = (120 + 520) ÷ 5,000 × 100 = 640 ÷ 5,000 × 100 = **12.80%**.

**Answer:** Separation 2.40%; Replacement 0.80%; Flux 12.80%. The gap between flux and replacement shows most accessions were for **expansion (480 workers)**, not to replace leavers.

**Why this way (the reasoning):** The three methods answer different questions and must not be confused. The *separation* rate measures how many workers left — the pure "loss" of trained hands. The *replacement* rate counts only those hired *to fill vacancies of leavers*, deliberately excluding workers taken on to *grow* the workforce, because expansion recruitment is not "turnover" — it is not churn, it is growth. That is exactly why replacement (0.80%) is far below flux (12.80%) here: the firm is expanding, adding 480 new posts, and lumping those into turnover would wildly overstate instability. The *flux* rate captures total workforce movement (in + out) and is the broadest. Reading a high flux rate as "high attrition" is the trap — you must decompose it, and the replacement rate is what isolates genuine, avoidable churn.

*(Full-marks tip: the examiner rewards separating expansion accessions from replacement accessions; using total accessions in the replacement formula is the standard error.)*

---

### Q11. Ch: Employee (Labour) Cost — Cost of Labour Turnover: Preventive vs Replacement (Marks: 8) [Problem/Application]
**Question:** A company is deciding how much to spend preventing labour turnover. Data for the year: preventive costs (personnel admin, welfare, medical, pension) totalled ₹2,70,000; replacement costs (recruitment, training, loss of output, defectives, extra scrap) totalled ₹1,80,000. Average number of workers 3,000. In the *previous* year, with preventive spend of only ₹1,50,000, replacement costs were ₹3,60,000. Compute the cost of labour turnover per worker for each year and advise whether the increased preventive spending was justified.

**Solution:**

**WN-1 — Total labour-turnover cost each year:**

| | Previous year (₹) | Current year (₹) |
|---|---|---|
| Preventive cost | 1,50,000 | 2,70,000 |
| Replacement cost | 3,60,000 | 1,80,000 |
| **Total** | **5,10,000** | **4,50,000** |

**WN-2 — Cost per worker (÷ 3,000):** Previous = 5,10,000 ÷ 3,000 = **₹170**; Current = 4,50,000 ÷ 3,000 = **₹150**.

**WN-3 — Incremental analysis:** Extra preventive spend = 2,70,000 − 1,50,000 = ₹1,20,000. Replacement cost fell = 3,60,000 − 1,80,000 = ₹1,80,000. **Net saving = 1,80,000 − 1,20,000 = ₹60,000.**

**Answer:** Total turnover cost fell from **₹5,10,000 (₹170/worker) to ₹4,50,000 (₹150/worker)**. Spending an extra ₹1,20,000 on prevention saved ₹1,80,000 in replacement costs — a **net gain of ₹60,000**. The increased preventive spending was **justified**; further increases are worthwhile only up to the point where marginal replacement savings still exceed marginal preventive cost.

**Why this way (the reasoning):** Labour turnover cost has two opposing components: *preventive* cost (spent to keep workers from leaving — welfare, pensions, good supervision) and *replacement* cost (incurred *because* they left — recruiting, training, lost output, extra scrap from raw recruits). They trade off: spend more on prevention and replacement cost tends to fall. The correct decision rule is not "minimise preventive spend" nor "minimise turnover at any cost", but *minimise the total*, and at the margin keep spending on prevention only while each extra rupee of prevention saves more than a rupee of replacement. Here the incremental logic proves it: ₹1.20 lakh bought ₹1.80 lakh of savings, so the move was value-adding. The trap is to look at the *rise* in preventive cost in isolation and conclude the company overspent — you must net it against the larger fall in replacement cost.

*(Full-marks tip: show the incremental (marginal) comparison, not just the two totals — the "advise" mark is earned by the ₹60,000 net-saving argument and the marginal-spending caveat.)*

---

### Q12. Ch: Employee (Labour) Cost — Idle Time: Normal vs Abnormal Treatment (Marks: 6) [Problem/Theory]
**Question:** A worker's weekly attendance is 48 hours at ₹60/hour. During the week, idle time comprised: tea/lunch and personal needs 3 hours; machine set-up and waiting for the next job 2 hours; a power failure 4 hours; time lost due to a strike 5 hours. Compute the productive hours, the amount of normal and abnormal idle-time wages, and state the correct accounting treatment of each.

**Solution:**

**WN-1 — Classify idle time.**
- Normal, unavoidable (inherent in the job): tea/lunch/personal 3 hrs + set-up/waiting 2 hrs = **5 hrs normal**.
- Abnormal (avoidable/exceptional): power failure 4 hrs + strike 5 hrs = **9 hrs abnormal**.

**WN-2 — Productive (effective) hours:** 48 − 5 − 9 = **34 hours**.

**WN-3 — Idle-time cost:** Normal idle = 5 × 60 = ₹300; Abnormal idle = 9 × 60 = ₹540. Total wages = 48 × 60 = ₹2,880.

**Statement of Treatment:**

| Component | Hours | Amount (₹) | Treatment |
|---|---|---|---|
| Productive wages | 34 | 2,040 | Direct to job/production |
| Normal idle time | 5 | 300 | Absorbed as production overhead (inflates effective hourly rate) |
| Abnormal idle time | 9 | 540 | Charged to Costing Profit & Loss A/c |
| **Total** | **48** | **2,880** | — |

**Answer:** Productive hours = 34; normal idle wages ₹300 (loaded onto production overhead); abnormal idle wages ₹540 (written off to Costing P&L). Effective wage rate on productive hours if normal idle is loaded on direct labour = (2,040 + 300) ÷ 34 = ₹68.82/hr.

**Why this way (the reasoning):** Idle time is paid-for-but-unproductive time, and its treatment turns on whether it is *inherent and unavoidable* or *abnormal and avoidable* — the same normal/abnormal logic that governs material losses, for the same reason. Normal idle time (lunch, unavoidable set-up/waiting) is a genuine, expected cost of employing labour; it is spread over good output as overhead (or by inflating the direct labour rate), so product cost bears its fair share. Abnormal idle time (power failure, strike) is *not* a cost of making the product — it is a cost of something going wrong — so charging it to jobs would overstate product cost and hide the loss; instead it is isolated in the Costing P&L where management can see and act on it. Treating power-failure and strike hours as if they were normal production cost is the classic error and defeats the whole purpose of cost control.

*(Full-marks tip: the marks hinge on the *classification*, then the treatment. Show productive hours reconciling to 48, and never charge abnormal idle time to the job.)*

---

### Q13. Ch: Employee (Labour) Cost — Overtime Premium: Cause-Based Treatment (Marks: 6) [Theory/Application]
**Question:** "Overtime always increases the cost of the job on which it is worked, so the whole overtime payment should be charged to that job." Examine the validity of this statement and state the correct treatment of the overtime premium in four different situations.

**Answer:**

**Governing principle.** Overtime pay = normal rate + *overtime premium* (the excess over normal rate). The *normal-rate portion* is always a direct labour cost of whatever job is worked. The treatment of the **premium** depends on *why* the overtime was necessary — cost is charged to the party/cause responsible.

**Application — four situations:**
1. **Overtime at the customer's specific request** (to meet an urgent delivery): the premium is charged **directly to that job**, because the customer caused it and should bear it.
2. **Overtime due to general pressure of work / to raise overall output**: the premium is treated as **production (factory) overhead**, spread over all jobs of the period, since no single job caused it.
3. **Overtime caused by abnormal conditions** (e.g., making good the effect of a fire, flood, or management's failure to plan): the premium is charged to the **Costing Profit & Loss A/c**, as it is an abnormal loss not attributable to production.
4. **Overtime caused by a particular department's fault/delay**: the premium is charged to **that department**, so responsibility is fixed.

**Conclusion.** The statement is **only partly valid**. The *normal wages* for overtime hours do attach to the job, and where the customer specifically demands the rush, even the premium is charged to the job. But it is **wrong** to charge the premium to the job in all cases — if the overtime arose from general workload it becomes overhead, and if it arose from abnormal causes it is written off to P&L. Blanket job-charging would distort inter-job cost comparisons.

**Why this way (the reasoning):** The premium is charged according to *cause and controllability* so that each job carries only the cost it genuinely triggered, and abnormal/general costs do not masquerade as product cost. If a job that happened to be running when the factory decided to work extra hours for *general* output were burdened with the full premium, it would look artificially expensive and mislead pricing and profitability comparisons — even though other jobs equally benefited from the extra capacity. Isolating abnormal-cause overtime in the P&L, meanwhile, preserves the visibility of avoidable loss for management action. The unifying idea across idle time, overtime and losses is identical: costs follow the cause, and abnormal costs are quarantined from product cost.

*(Full-marks tip: give all four situations with the *reason* each treatment follows; a two-line "sometimes job, sometimes overhead" answer is capped. Distinguish the normal-rate portion from the premium explicitly.)*

---

### Q14. Ch: Employee (Labour) Cost — Overtime + Idle Time Integrated Cost per Piece (Marks: 8) [Problem]
**Question:** A worker is guaranteed 45 hours a week at ₹80/hour. Overtime (hours beyond 40) is paid at 1.5× the normal rate. In a week he attended 45 hours, of which 3 hours were normal idle time and 2 hours abnormal idle (a power cut). He produced 400 acceptable pieces. Compute (i) gross wages, (ii) the effective direct-labour cost per acceptable piece charged to production, and (iii) the amount written off to Costing P&L. Overtime here was worked to meet general production targets.

**Solution:**

**WN-1 — Split of hours & gross wages.** Normal hours = 40 @ ₹80 = ₹3,200. Overtime = 5 hrs @ (80 × 1.5 = ₹120) = ₹600. Gross wages = **₹3,800**. Of the ₹600 OT pay: normal-rate portion 5 × 80 = ₹400; overtime premium 5 × 40 = ₹200.

**WN-2 — Treatment of each element (OT worked for general targets → premium to overhead; abnormal idle → P&L).**

| Element | Amount (₹) | Treatment |
|---|---|---|
| Normal-rate wages 45 hrs (40×80 + 5×80) | 3,600 | Labour cost pool |
| Overtime premium (general work) | 200 | Production overhead |
| Abnormal idle wages (2 × 80) | 160 | Costing P&L |

**WN-3 — Direct labour charged to production.** Effective/productive hours = 45 − 3 (normal idle) − 2 (abnormal idle) = 40 hrs. Wages attaching to production = normal-rate wages 3,600 − abnormal idle 160 = ₹3,440 (this includes normal idle ₹240, which stays with production). Overtime premium ₹200 goes to overhead (not to this job's direct cost).

Direct labour cost to product = ₹3,440. Cost per acceptable piece (direct labour) = 3,440 ÷ 400 = **₹8.60/piece**. If OT premium (₹200) is recovered as overhead on this output, add 200 ÷ 400 = ₹0.50 → fully-absorbed labour+OT = **₹9.10/piece**.

**Answer:** Gross wages **₹3,800**; direct-labour cost per acceptable piece **₹8.60** (₹9.10 including the OT premium recovered as overhead); amount written off to Costing P&L (abnormal idle) = **₹160**.

**Why this way (the reasoning):** This problem forces three separate principles to work together. First, overtime pay splits into a normal-rate part (always a labour cost) and a premium; because the overtime here served *general* production, its premium is overhead, not a charge on this specific job — charging it to the job would overstate this batch's cost versus others that shared the extra capacity. Second, normal idle time (3 hrs) stays within production cost because it is inherent, so it correctly inflates the per-piece rate; abnormal idle (the power cut) is quarantined to Costing P&L so that the loss is visible and does not make the product look dearer. Third, "acceptable pieces" is the right denominator so that the productive cost is spread only over sound output. Getting any one of these classifications wrong throws off the per-piece figure — the discipline is to route every rupee to its correct destination *before* dividing.

*(Full-marks tip: show the OT pay split into normal-rate + premium, and keep abnormal idle out of the per-piece cost. Marks are lost when candidates charge the whole ₹600 OT to the job or divide by hours instead of acceptable pieces.)*

---

### Q15. Ch: Employee (Labour) Cost — Taylor Differential Piece Rate + Comparison (Marks: 8) [Problem]
**Question:** Standard output is 10 units per hour. Normal piece rate is ₹6 per unit. Under Taylor's differential piece-rate system, 80% of the piece rate is paid below standard and 120% at or above standard. In an 8-hour day, Worker A produced 70 units and Worker B produced 90 units. Compute each worker's daily earnings under (i) Taylor's system and (ii) a straight piece rate, and comment on the incentive effect.

**Solution:**

**WN-1 — Standard output for the day:** 10 units/hr × 8 hrs = **80 units**. So the "efficient" threshold is 80 units/day.
Worker A: 70 units → **below** standard → low rate 80% × 6 = ₹4.80/unit.
Worker B: 90 units → **at/above** standard → high rate 120% × 6 = ₹7.20/unit.

**WN-2 — Taylor earnings:**
A = 70 × 4.80 = **₹336**. B = 90 × 7.20 = **₹648**.

**WN-3 — Straight piece rate (₹6):** A = 70 × 6 = ₹420; B = 90 × 6 = ₹540.

**Statement Showing Earnings:**

| Worker | Output | Taylor rate (₹) | Taylor earnings (₹) | Straight earnings (₹) | Difference (₹) |
|---|---|---|---|---|---|
| A (70) | below std | 4.80 | 336 | 420 | −84 |
| B (90) | above std | 7.20 | 648 | 540 | +108 |

**Answer:** Under Taylor, A earns **₹336** and B earns **₹648**; under straight piece rate A gets ₹420 and B ₹540. Taylor *penalises* the inefficient worker A (−₹84) and *sharply rewards* the efficient worker B (+₹108).

**Why this way (the reasoning):** Taylor's system is deliberately harsh: it has *no* guaranteed time wage and applies the *whole* output at either the low or the high rate depending on which side of standard the worker falls — there is no blending. The design intent is maximum pressure to reach standard: a worker just below the line (A) is punished across *all* his units, not just the shortfall, while a worker who clears it (B) is rewarded on *all* units. This creates a large, discontinuous jump in pay right at the standard, which is exactly what drives sub-standard workers to push over the line. Compared with a straight piece rate, Taylor widens the earnings gap between efficient and inefficient workers. The concept to grasp is that the *entire* output is repriced (not a marginal bonus on excess units) — treating only the excess above standard at the higher rate is the classic misapplication.

*(Full-marks tip: apply the single applicable rate to ALL units of each worker; the examiner deducts marks if you pay part at 80% and part at 120% for the same worker.)*

---

### Q16. Ch: Employee (Labour) Cost — Labour Cost Reconciliation: Payroll to Job Cost (Marks: 6) [Problem/Application]
**Question:** A department's payroll for a month shows gross wages ₹6,00,000 for 10 workers. Analysis reveals: productive time 82%, normal idle time 8%, abnormal idle time (breakdown) 6%, and time on a rectification of defectives (normal) 4%. Show how the ₹6,00,000 is distributed across cost destinations, and compute the direct wages rate per productive hour if total attended hours were 1,600.

**Solution:**

**WN-1 — Rupee split of ₹6,00,000 by activity:**

| Activity | % | Amount (₹) | Cost destination |
|---|---|---|---|
| Productive time | 82% | 4,92,000 | Direct wages → jobs |
| Normal idle time | 8% | 48,000 | Production overhead |
| Abnormal idle (breakdown) | 6% | 36,000 | Costing P&L A/c |
| Normal rectification of defectives | 4% | 24,000 | Production overhead (or job) |
| **Total** | 100% | **6,00,000** | — |

**WN-2 — Productive hours:** 82% × 1,600 = 1,312 hours.

**WN-3 — Direct wages rate per productive hour:** ₹4,92,000 ÷ 1,312 = **₹375/hr**.
If normal idle (₹48,000) is loaded onto direct labour, effective rate = (4,92,000 + 48,000) ÷ 1,312 = 5,40,000 ÷ 1,312 = **₹411.59/hr**.

**Answer:** Direct wages to jobs ₹4,92,000; production overhead ₹72,000 (normal idle 48,000 + rectification 24,000); Costing P&L ₹36,000 (abnormal idle). Direct wages rate ≈ **₹375 per productive hour** (₹411.59 if normal idle absorbed into the labour rate).

**Why this way (the reasoning):** Payroll is a single lump, but sound costing insists every rupee reach the destination that reflects *why* it was incurred, so that product cost is neither inflated by abnormal events nor understated by ignoring inherent idle time. Productive wages attach straight to jobs. Normal idle time and normal rectification are *expected* costs of running the department, so they are recovered as overhead (or on the job) and thus still borne by output. Abnormal idle from a breakdown is an avoidable loss with no product-value, so it is stripped out to the Costing P&L for management scrutiny. The reconciliation discipline — the four pieces summing back to ₹6,00,000 — is what proves nothing has been mis-routed. The common error is to divide gross wages by attended hours to get the labour rate; the correct rate uses *productive* hours (and, if chosen, loads only the normal idle onto that rate), never the abnormal element.

*(Full-marks tip: the reconciliation must total exactly to gross wages, and the rate must use productive hours. State clearly whether normal idle is absorbed into the rate or shown as overhead — either is acceptable if stated.)*

---

### Q17. Ch: Material Cost + Employee Cost — Integrated: Effective Material Cost & Labour Efficiency (Marks: 10) [Problem/Case]
**Question:** A firm buys a component and processes it. For a batch it received the following invoice and incurred the labour below. GST is fully creditable (input tax credit available). A cash discount of 2% is offered for payment within 10 days, which the firm avails. Normal process loss is 5% of input. Two workers on the Rowan scheme were engaged. Compute (i) the effective material cost per good unit, and (ii) the labour cost of the batch, then the total conversion + material cost per good unit.

| Material particulars | Amount |
|---|---|
| List price of 1,000 units | ₹4,00,000 |
| Trade discount | 10% |
| GST @ 18% (creditable) | on net price |
| Freight inward | ₹9,000 |
| Insurance in transit | ₹3,000 |
| Cash discount availed | 2% (financial) |

| Labour particulars | Worker X | Worker Y |
|---|---|---|
| Standard time for batch | 60 hrs | 60 hrs |
| Actual time taken | 45 hrs | 50 hrs |
| Rate per hour | ₹100 | ₹80 |

**Solution:**

**WN-1 — Net purchase price of material.** List 4,00,000 − 10% trade discount 40,000 = ₹3,60,000. GST ₹64,800 is *creditable* → excluded from cost. Cash discount 2% is a *financial* item → excluded from cost (not deducted from material cost).
Add freight ₹9,000 + insurance ₹3,000 = ₹12,000.
Total material cost = 3,60,000 + 12,000 = **₹3,72,000** for 1,000 units.

**WN-2 — Good units after normal loss.** Normal loss = 5% × 1,000 = 50 units → good output = **950 units**. Normal loss cost is absorbed by good units.
Effective material cost per good unit = 3,72,000 ÷ 950 = **₹391.58**.

**WN-3 — Labour under Rowan.**
Worker X: basic 45 × 100 = ₹4,500; time saved 15 hrs; bonus = (15/60) × 4,500 = ₹1,125 → total ₹5,625.
Worker Y: basic 50 × 80 = ₹4,000; time saved 10 hrs; bonus = (10/60) × 4,000 = ₹666.67 → total ₹4,666.67.
Batch labour = 5,625 + 4,666.67 = **₹10,291.67**.
Labour per good unit = 10,291.67 ÷ 950 = **₹10.83**.

**WN-4 — Total cost per good unit:** 391.58 + 10.83 = **₹402.41**.

**Statement Showing Cost per Good Unit:**

| Element | Batch (₹) | Per good unit (₹) |
|---|---|---|
| Material (net of GST & cash discount, incl. freight/insurance) | 3,72,000 | 391.58 |
| Labour (Rowan, X + Y) | 10,291.67 | 10.83 |
| **Total** | **3,82,291.67** | **402.41** |

**Answer:** Effective material cost ≈ **₹391.58/good unit**; batch labour ≈ **₹10,291.67**; total material + labour cost ≈ **₹402.41 per good unit**.

**Why this way (the reasoning):** This case tests three principles at once. (1) *What belongs in material cost*: only costs of *bringing the material to a usable state* — net-of-trade-discount price plus freight and insurance. GST is excluded because it is recoverable as input tax credit (it never becomes a real cost to the firm), and **cash (financial) discount is excluded** because it is a reward for prompt *payment*, a financing decision, not a reduction in the material's cost — deducting it would understate material cost and mix financing with product cost. This is the standard trap: trade discount reduces cost, cash discount does not. (2) *Normal loss* is spread over good units, so the denominator is 950, not 1,000 — the good units must absorb the cost of the units inevitably lost, raising the true per-good-unit cost. (3) *Rowan bonus* rewards each worker in proportion to time saved over standard, computed separately per worker at his own rate. Blending any of these — crediting GST/cash discount into cost, dividing by input units, or mis-computing Rowan — corrupts the final figure.

*(Full-marks tip: the two make-or-break decisions are (a) excluding creditable GST AND cash discount from material cost while keeping freight/insurance in, and (b) dividing by 950 good units, not 1,000. State the ITC and financial-discount reasoning explicitly — examiners award a specific mark for each.)*

### Q18. Ch: Overheads – Absorption Costing — Reciprocal Service Distribution (Simultaneous Equations) (Marks: 10) [Problem]
**Question:** A factory has two production departments (P1, P2) and two service departments — Stores (S1) and Maintenance (S2) — that serve each other. After primary distribution the overheads and the pattern of service consumption are:

| Particulars | P1 | P2 | S1 (Stores) | S2 (Maint.) |
|---|---|---|---|---|
| Overhead after primary distribution (₹) | 80,000 | 60,000 | 30,000 | 20,000 |
| Service of S1 (Stores) given to | 40% | 40% | — | 20% |
| Service of S2 (Maint.) given to | 30% | 50% | 20% | — |

Reapportion the service department costs to P1 and P2 using the **simultaneous equation (algebraic) method**.

**Solution:**

**WN-1 — Frame the equations.** Let the *total* cost of each service department (own cost + cost received from the other) be S1 and S2.
- S1 = 30,000 + 0.20 S2
- S2 = 20,000 + 0.20 S1

**WN-2 — Solve simultaneously.** Substitute S2 into S1:
S1 = 30,000 + 0.20 (20,000 + 0.20 S1) = 30,000 + 4,000 + 0.04 S1
0.96 S1 = 34,000 → **S1 = ₹35,416.67**
S2 = 20,000 + 0.20 × 35,416.67 = **₹27,083.33**

**WN-3 — Distribute total service cost to production departments.**
- To P1: 0.40 × 35,416.67 + 0.30 × 27,083.33 = 14,166.67 + 8,125.00 = ₹22,291.67
- To P2: 0.40 × 35,416.67 + 0.50 × 27,083.33 = 14,166.67 + 13,541.67 = ₹27,708.34

**Statement Showing Secondary Distribution of Overheads**

| Particulars | P1 (₹) | P2 (₹) | S1 (₹) | S2 (₹) |
|---|---|---|---|---|
| Overhead (primary) | 80,000.00 | 60,000.00 | 30,000.00 | 20,000.00 |
| Add: Stores (S1) apportioned | 14,166.67 | 14,166.67 | (35,416.67) | 7,083.33 |
| Add: Maintenance (S2) apportioned | 8,125.00 | 13,541.67 | 5,416.67 | (27,083.33) |
| **Total overhead** | **1,02,291.67** | **87,708.33** | Nil | Nil |

**Answer:** Overhead absorbed — **P1 = ₹1,02,291.67 and P2 = ₹87,708.33** (total ₹1,90,000, exactly equal to the ₹1,90,000 primary total, confirming no cost is lost).

**Why this way (the reasoning):** The two service departments feed each other, so their *final* cost cannot be known until each is known — a chicken-and-egg loop. The algebraic method breaks the loop by treating each department's total as an unknown and writing one equation per department that captures every rupee flowing in. Solving them together apportions the reciprocal service **exactly in one pass**, whereas the tempting "step-down / repeated distribution" method only approximates it by ignoring the return service after a few rounds (it closes one service department first and never sends cost back). The check that both service columns net to *nil* and the grand total is unchanged proves the entire ₹1,90,000 has been fully absorbed into P1 and P2 — the whole purpose of secondary distribution.

*(Full-marks tip: examiners reward writing the equations on **total** cost — not own cost — and showing the S1↔S2 cross-charge. Common deduction: forgetting the 20% each department gives back to the other, or a total that no longer equals ₹1,90,000.)*

---

### Q19. Ch: Overheads – Absorption Costing — Comprehensive Machine Hour Rate with Effective Capacity (Marks: 10) [Problem]
**Question:** Compute the machine hour rate for a machine from the following annual data. State clearly how you treat the setting-up (idle) time.

| Particulars | Amount |
|---|---|
| Cost of machine (including installation) | ₹11,00,000 |
| Estimated scrap value at end of life | ₹1,00,000 |
| Working life | 10 years |
| Department rent p.a. (machine occupies 1/4 of floor area) | ₹96,000 |
| Supervisor's salary p.a. (supervises 3 identical machines equally) | ₹1,08,000 |
| Insurance specific to the machine p.a. | ₹6,000 |
| Repairs & maintenance p.a. | ₹40,000 |
| Consumable stores p.a. | ₹20,000 |
| Power: 10 units per running hour @ ₹6 per unit | — |
| Total machine hours available | 2,200 hrs |
| Of which setting-up time (unproductive) | 200 hrs |

**Solution:**

**WN-1 — Effective (productive) machine hours.** 2,200 − 200 (setting-up) = **2,000 productive hours**. All standing charges are recovered over these 2,000 hours, and power is consumed only while the machine actually runs (2,000 hrs).

**WN-2 — Annual standing & machine charges (fixed, spread over 2,000 hrs).**

| Item | Basis | Amount (₹) |
|---|---|---|
| Depreciation | (11,00,000 − 1,00,000) ÷ 10 | 1,00,000 |
| Rent | 96,000 × 1/4 | 24,000 |
| Supervision | 1,08,000 ÷ 3 | 36,000 |
| Insurance | given | 6,000 |
| Repairs & maintenance | given | 40,000 |
| Consumable stores | given | 20,000 |
| **Total fixed** | | **2,26,000** |

Fixed cost per productive hour = 2,26,000 ÷ 2,000 = **₹113.00**

**WN-3 — Power (variable, running hours only).** 10 units × ₹6 = ₹60 per running hour.

**Statement of Machine Hour Rate**

| Element | ₹ per machine hour |
|---|---|
| Fixed standing & machine charges (WN-2) | 113.00 |
| Power (WN-3) | 60.00 |
| **Machine Hour Rate** | **173.00** |

**Answer:** **Machine hour rate = ₹173 per productive machine hour.**

**Why this way (the reasoning):** A machine hour rate must recover the machine's whole annual cost through only the hours it produces value. Setting-up time creates no output, so if the fixed ₹2,26,000 were spread over 2,200 hours the rate would be too low and the 200 idle hours would leave cost **under-recovered** — the department would silently lose ₹113 × 200 = ₹22,600. Spreading over the 2,000 *effective* hours forces every productive hour to carry its fair share, achieving full recovery. Power is handled separately because it is a *variable* cost that flows only when the motor runs; loading it on idle hours would overstate the setting-up cost. Depreciation here is on a **time (straight-line) basis** because the life is stated in years and obsolescence runs with time, not usage — so it stays fixed regardless of hours worked.

*(Full-marks tip: state your capacity assumption in one line. Examiners split fixed vs. running charges; the classic deduction is dividing power by 2,000 as if fixed, or dividing standing charges by 2,200 and thereby under-recovering.)*

---

### Q20. Ch: Overheads – Absorption Costing — Disposal of Under-Absorption by Supplementary Rate (Marks: 8) [Problem]
**Question:** A company recovered factory overheads on a predetermined basis. Actual overheads for the year were ₹4,50,000 and overheads absorbed were ₹3,90,000. Investigation showed that ₹20,000 of the shortfall arose from an abnormal machinery breakdown and a labour strike; the balance was due to a general rise in input prices. At year-end the relevant output was: units sold 32,000; finished goods in stock 5,000 units; work-in-progress 3,000 equivalent units. Show how the under-absorption should be disposed of, with journal logic.

**Solution:**

**WN-1 — Total under-absorption and its split.**
Under-absorption = 4,50,000 − 3,90,000 = **₹60,000.**
- Abnormal portion (breakdown + strike) = ₹20,000 → written off to Costing P&L (not a product cost).
- Normal portion (price rise) = ₹40,000 → apportioned over production by a **supplementary rate**.

**WN-2 — Supplementary rate.**
Units to absorb the normal shortfall = 32,000 + 5,000 + 3,000 = 40,000 units.
Supplementary rate = 40,000 ÷ 40,000 = **₹1.00 per unit.**

**Statement Showing Disposal of Under-Absorbed Overhead**

| Destination | Units | Rate (₹) | Amount (₹) |
|---|---|---|---|
| Cost of Sales (units sold) | 32,000 | 1.00 | 32,000 |
| Finished Goods stock | 5,000 | 1.00 | 5,000 |
| Work-in-Progress | 3,000 | 1.00 | 3,000 |
| **Normal shortfall recovered** | 40,000 | | **40,000** |
| Abnormal shortfall → Costing P&L | — | — | 20,000 |
| **Total under-absorption** | | | **60,000** |

**Answer:** Charge **₹32,000 to Cost of Sales, ₹5,000 to Finished Goods, ₹3,000 to WIP** (via a ₹1/unit supplementary rate) and **write ₹20,000 off to the Costing Profit & Loss Account.** Total ₹60,000 fully disposed.

**Why this way (the reasoning):** Absorption costing aims to charge each unit its *true* share of factory cost. When under-absorption is caused by a **normal, controllable** factor like a price rise, the extra cost genuinely belongs to the goods produced — but those goods are now in three places (sold, in finished stock, in WIP), so a supplementary rate re-spreads the shortfall across all of them, restoring inventory to actual cost as AS-2 requires. The tempting shortcut of dumping the whole ₹60,000 into the P&L is wrong because it would understate closing inventory and shift genuine product cost into the current period's loss. Conversely, the ₹20,000 from a strike and breakdown is **abnormal** — it reflects lost capacity, not value added to product — so it must hit the P&L immediately and never inflate stock, otherwise unsold units would carry the cost of idleness.

*(Full-marks tip: separate abnormal from normal first, then base the supplementary rate on *all* production benefited, including WIP. Deduction: applying the rate only to units sold, or capitalising the abnormal ₹20,000 into stock.)*

---

### Q21. Ch: Overheads – Absorption Costing — Blanket vs. Departmental Rate (Marks: 6) [Case/Application]
**Question:** A firm has two departments — **Machining** (highly mechanised) and **Assembly** (labour-intensive). It absorbs *all* factory overhead using a single plant-wide (blanket) rate on direct labour hours. Total overhead ₹6,00,000; total direct labour hours 60,000 (Machining 10,000; Assembly 50,000). Of the overhead, ₹4,50,000 relates to Machining and ₹1,50,000 to Assembly. A cost clerk argues the blanket rate is fine because "the total recovered is the same." A quotation for Job Z, which needs 400 machine-related hours in Machining but only 20 labour hours in Assembly, is under review. **Examine the validity of using a blanket rate.**

**Answer:**

**Governing principle.** A blanket (single) overhead rate is acceptable only when all products pass through all departments in roughly the same proportion, or when one department dominates. Where departments differ sharply in overhead intensity, a **departmental rate** must be used so that each job bears the overhead of the departments it actually consumes.

**Application to the facts.**
- Blanket rate = 6,00,000 ÷ 60,000 = **₹10 per labour hour.** A job is charged on the labour hours it clocks, *irrespective of where the cost is caused*.
- Correct **departmental rates**: Machining = 4,50,000 ÷ 10,000 = **₹45 per hour**; Assembly = 1,50,000 ÷ 50,000 = **₹3 per hour**.
- Job Z is machining-heavy. Under the blanket rate it is charged on (say) its ~20 Assembly labour hours → overhead ≈ 20 × ₹10 = **₹200**. But it genuinely draws on the ₹45-per-hour Machining pool. The blanket rate systematically **under-costs** machining-intensive jobs and **over-costs** assembly-intensive jobs.

**Conclusion/Advice.** The clerk is right that the *total* recovered is unchanged — but averaging is precisely the flaw. A correct total hides serious per-job distortion: Job Z would be quoted too cheaply and could be won at a loss, while labour-heavy jobs are over-quoted and lost to competitors. The firm should adopt **departmental overhead rates** (or an activity-based approach), pricing Job Z on the ₹45 Machining rate for its machine work.

**Why this way (the reasoning):** Overhead absorption is about *cause and effect* — a job should carry the cost of the resources it consumes. A blanket rate assumes overhead is caused uniformly by labour hours everywhere, which collapses two very different cost structures (a ₹45 department and a ₹3 department) into one misleading ₹10 average. The total always reconciles because averaging conserves the sum; it just misallocates it. Departmental rates restore the causal link, which is why they are essential wherever overhead intensity varies across departments.

*(Full-marks tip: show both rates numerically and name a specific job that is mis-costed. Deduction: merely defining blanket vs departmental without demonstrating the ₹45-vs-₹10 distortion.)*

---

### Q22. Ch: Overheads – Absorption Costing — Choice of Capacity & Cost of Idle Capacity (Marks: 5) [Case/Application]
**Question:** During a recession a company operated at **60% of its normal capacity**. The accountant proposes to absorb the *entire* annual fixed factory overhead over the reduced actual output, so that the fixed overhead per unit rises steeply and each unit "carries its full share." The marketing head objects that this inflates product cost and cripples pricing. **Comment on the validity of the accountant's approach and advise the correct treatment.**

**Answer:**

**Governing principle.** For product costing, fixed overhead should be absorbed using a **normal (or budgeted) capacity** denominator, not the depressed actual activity. The cost of *unused normal capacity* is an **abnormal idle-capacity cost** to be written off to the Costing P&L, not loaded onto the units produced.

**Application.** If fixed overhead is spread over 60% output, the fixed cost per unit is inflated by 1/0.60 ≈ 1.67 times. Every unit then absorbs not only its own share but also the cost of the 40% capacity that stood idle. This over-values inventory (contrary to AS-2, which requires allocation on normal capacity) and produces an artificially high cost that, if used for pricing, would push prices up in a downturn — exactly when demand is weakest — worsening the spiral.

**Conclusion/Advice.** The accountant's approach is **invalid**. Absorb fixed overhead on normal capacity so that units produced carry only their legitimate share, and transfer the under-absorbed overhead attributable to the idle 40% directly to the Costing P&L as a period cost. This keeps product cost and inventory realistic and lets management price on genuine cost while separately spotlighting the ₹ cost of idleness for corrective action.

**Why this way (the reasoning):** Fixed overhead exists to provide *capacity*; a unit should pay only for the capacity it needed, not for capacity the business chose (or was forced) to leave idle. Charging idleness to the product disguises a management/economic problem as a product-cost problem, distorts inventory valuation, and can trigger a "death spiral" of ever-higher costs and prices as volumes fall. Isolating the idle-capacity cost as an abnormal loss keeps decision-relevant unit cost stable and makes the true cost of under-utilisation visible to those who can act on it.

*(Full-marks tip: name AS-2's "normal capacity" rule and the term *abnormal idle-capacity cost*, and link it to the pricing danger. Deduction: agreeing that all fixed cost must be recovered from actual output.)*

---

### Q23. Ch: Activity-Based Costing — ABC vs. Traditional Volume-Based Distortion (Marks: 10) [Problem]
**Question:** A company makes two products. Product A is a high-volume, simple product; Product B is a low-volume, complex product. Total factory overhead is ₹14,00,000. Compute the overhead cost per unit under (i) traditional absorption on direct labour hours and (ii) activity-based costing, and comment on the distortion.

| Data | Product A | Product B | Total |
|---|---|---|---|
| Units produced | 30,000 | 5,000 | — |
| Direct labour hours per unit | 2 | 2 | 70,000 hrs |
| Machine hours per unit | 1 | 2 | 40,000 hrs |
| No. of machine set-ups | 20 | 30 | 50 |
| No. of material movements | 100 | 150 | 250 |
| No. of inspections | 40 | 60 | 100 |

**Overhead cost pools:** Machine operation ₹5,00,000 (driver: machine hrs); Set-ups ₹4,00,000 (driver: set-ups); Material handling ₹3,00,000 (driver: movements); Inspection ₹2,00,000 (driver: inspections).

**Solution:**

**WN-1 — Traditional rate (direct labour hours).**
Rate = 14,00,000 ÷ 70,000 = **₹20 per DLH.**
Overhead/unit: A = 2 × 20 = **₹40**; B = 2 × 20 = **₹40.**

**WN-2 — Activity cost-driver rates.**

| Activity | Cost (₹) | Driver total | Rate |
|---|---|---|---|
| Machine operation | 5,00,000 | 40,000 mh | ₹12.50/mh |
| Set-ups | 4,00,000 | 50 | ₹8,000/set-up |
| Material handling | 3,00,000 | 250 | ₹1,200/move |
| Inspection | 2,00,000 | 100 | ₹2,000/insp. |

**WN-3 — Overhead assigned under ABC.**

| Activity | Product A (₹) | Product B (₹) |
|---|---|---|
| Machine operation | 30,000×12.50 = 3,75,000 | 10,000×12.50 = 1,25,000 |
| Set-ups | 20×8,000 = 1,60,000 | 30×8,000 = 2,40,000 |
| Material handling | 100×1,200 = 1,20,000 | 150×1,200 = 1,80,000 |
| Inspection | 40×2,000 = 80,000 | 60×2,000 = 1,20,000 |
| **Total overhead** | **7,35,000** | **6,65,000** |
| ÷ Units | 30,000 | 5,000 |
| **Overhead per unit (ABC)** | **₹24.50** | **₹133.00** |

**Statement Comparing Overhead per Unit**

| Method | Product A | Product B |
|---|---|---|
| Traditional (DLH) | 40.00 | 40.00 |
| Activity-Based Costing | 24.50 | 133.00 |
| Distortion | Over-costed by 15.50 | Under-costed by 93.00 |

**Answer:** Traditional costing charges both products ₹40/unit; ABC reveals the true burden is **₹24.50 for A and ₹133 for B.** High-volume A was **over-costed** and low-volume B massively **under-costed** (total ABC overhead ₹7,35,000 + ₹6,65,000 = ₹14,00,000, reconciling exactly).

**Why this way (the reasoning):** Traditional costing assumes overhead is driven by a single volume measure (labour hours), so a product that uses twice the units automatically absorbs twice the overhead. But most modern overhead — set-ups, material handling, inspections — is driven by **transactions and complexity, not volume.** Product B, though small in volume, triggers *more* set-ups, movements and inspections; those batch- and product-level activities are consumed almost regardless of how many units are made, so they land brutally on B's small unit base (hence ₹133). The volume-based rate quietly shifts B's transaction costs onto high-volume A. ABC restores accuracy by tracing each pool through its own **cost driver** — the activity that actually causes the cost — which is why the two methods diverge so sharply for a low-volume/high-complexity product. The reconciliation to ₹14,00,000 proves ABC only *re-slices* the same total, more truthfully.

*(Full-marks tip: compute all four driver rates and show the reconciliation to ₹14,00,000. Deduction: leaving machine-operation overhead on labour hours, or a per-unit total that doesn't tie back.)*

---

### Q24. Ch: Activity-Based Costing — Cost Hierarchy & Batch-Size Effect (Marks: 8) [Problem]
**Question:** Two products have the **same annual volume of 20,000 units** but different batch sizes. Using the data below, compute overhead per unit under traditional (unit-based) absorption and under ABC, and explain the hierarchy level of each activity.

| Data | Product H | Product L | Total |
|---|---|---|---|
| Units p.a. | 20,000 | 20,000 | 40,000 |
| Batch size | 1,000 | 250 | — |
| No. of batches | 20 | 80 | 100 |
| Machine hrs per unit | 1.5 | 1.5 | 60,000 |

**Overhead pools:** Machining ₹8,00,000 (unit-level, driver: machine hrs); Set-ups ₹6,00,000 (batch-level, ₹6,000/batch × 100); Inspection ₹2,00,000 (batch-level, one inspection per batch).

**Solution:**

**WN-1 — Traditional rate (per unit / on total overhead).**
Total overhead = 8,00,000 + 6,00,000 + 2,00,000 = ₹16,00,000; total units 40,000.
Rate = **₹40 per unit** → H = ₹40, L = ₹40.

**WN-2 — ABC driver rates.**
Machining = 8,00,000 ÷ 60,000 mh = ₹13.333/mh → per unit = 1.5 × 13.333 = **₹20** (both).
Set-ups = 6,00,000 ÷ 100 = ₹6,000/batch.
Inspection = 2,00,000 ÷ 100 = ₹2,000/batch.

**WN-3 — Batch-level cost per unit.**

| Activity | Product H | Product L |
|---|---|---|
| Set-ups | 20×6,000 = 1,20,000 → /20,000 = ₹6.00 | 80×6,000 = 4,80,000 → /20,000 = ₹24.00 |
| Inspection | 20×2,000 = 40,000 → /20,000 = ₹2.00 | 80×2,000 = 1,60,000 → /20,000 = ₹8.00 |

**Statement of Overhead per Unit (ABC)**

| Element (hierarchy) | Product H | Product L |
|---|---|---|
| Machining (unit-level) | 20.00 | 20.00 |
| Set-ups (batch-level) | 6.00 | 24.00 |
| Inspection (batch-level) | 2.00 | 8.00 |
| **Total (ABC)** | **28.00** | **52.00** |
| Traditional | 40.00 | 40.00 |

**Answer:** Despite **identical volumes**, ABC shows **H = ₹28 and L = ₹52 per unit**, versus a flat ₹40 under traditional costing. L is under-costed by traditional methods purely because it is made in small batches. (Check: H 28×20,000 + L 52×20,000 = 5,60,000 + 10,40,000 = ₹16,00,000.)

**Why this way (the reasoning):** ABC classifies costs by a **hierarchy** — unit-level costs (machining) vary with each unit, so they are correctly ₹20 for both; but **batch-level** costs (set-ups, inspection) are incurred *once per batch* regardless of how many units the batch contains. L uses batches of only 250, so it needs 80 batches to make the same 20,000 units that H makes in 20 batches — four times the set-ups and inspections. Spreading those batch costs over the same unit volume gives L four times the batch-cost-per-unit. A traditional unit-based rate is blind to this because it assumes cost rises only with units, so it averages the batch costs equally and hides that small-batch production is genuinely more expensive. Recognising the *level* at which a cost is caused is the core insight of ABC — and here it flips a "same cost" conclusion into a 28-vs-52 reality.

*(Full-marks tip: label each activity's hierarchy level and show that equal volume does NOT mean equal cost. Deduction: absorbing set-ups on units/machine hours, which erases the whole point.)*

---

### Q25. Ch: Activity-Based Costing — Examine Validity of "ABC Should Replace Traditional Everywhere" (Marks: 5) [Case/Application]
**Question:** A consultant advises a small firm that "ABC always gives more accurate costs and should replace traditional absorption costing in *every* business." The firm makes a single product on one simple production line with overhead that is over 90% direct-labour-driven. **Examine the validity of this advice.**

**Answer:**

**Governing principle.** ABC improves accuracy by tracing overhead through multiple cost drivers, but it is beneficial only where **(i)** overheads are large relative to direct cost, **(ii)** products are **diverse** in volume and complexity, and **(iii)** overhead is driven by varied non-volume activities. Its benefit must exceed its **implementation and maintenance cost.**

**Application.** In this firm — one product, one simple line, overhead overwhelmingly labour-driven — there is no product-mix diversity for ABC to untangle and no batch/product-level complexity to reveal. A single labour-based rate already reflects the true cause of overhead. Installing multiple cost pools, drivers and data-capture systems would add cost and effort while changing the product cost hardly at all.

**Conclusion/Advice.** The advice is **not universally valid.** ABC is a decision-support tool, not a mandatory replacement. For this firm, traditional absorption on labour hours is appropriate and cost-effective; ABC would fail a cost-benefit test. ABC should be adopted only where product diversity and heavy transaction-driven overhead make the extra accuracy worth the extra cost.

**Why this way (the reasoning):** Accuracy is not free. ABC's power comes from distinguishing many activities and drivers — valuable only when products consume those activities in *different* proportions. With one homogeneous product and volume-driven overhead, every allocation method returns essentially the same answer, so the sophistication is wasted. The governing idea is **relevance and cost-benefit**: a costing system should be as accurate as decisions require and no more elaborate than the information is worth. Blanket statements like "always more accurate, always adopt" ignore that ABC's own upkeep is an overhead.

*(Full-marks tip: weigh benefit against cost and tie the recommendation to the specific facts (single product, labour-driven). Deduction: reciting ABC advantages without applying the cost-benefit test to this firm.)*

---

### Q26. Ch: Activity-Based Costing — Customer Profitability Analysis (Marks: 6) [Problem]
**Question:** Two customers each buy ₹10,00,000 of goods a year at a uniform gross margin of 20% on sales, but behave very differently. Using activity-based customer-service costs, determine which customer is more profitable and advise.

| Activity | Cost per event | Customer M | Customer N |
|---|---|---|---|
| Order processing | ₹500/order | 10 orders | 100 orders |
| Deliveries | ₹800/delivery | 10 | 100 |
| Sales visits | ₹3,000/visit | 2 | 20 |

**Solution:**

**WN-1 — Gross margin.** 20% × 10,00,000 = **₹2,00,000 each.**

**WN-2 — Cost-to-serve.**
- Customer M = 10×500 + 10×800 + 2×3,000 = 5,000 + 8,000 + 6,000 = **₹19,000.**
- Customer N = 100×500 + 100×800 + 20×3,000 = 50,000 + 80,000 + 60,000 = **₹1,90,000.**

**Statement of Customer Profitability**

| Particulars | Customer M (₹) | Customer N (₹) |
|---|---|---|
| Gross margin | 2,00,000 | 2,00,000 |
| Less: Cost-to-serve | 19,000 | 1,90,000 |
| **Net customer profit** | **1,81,000** | **10,000** |

**Answer:** Though both generate the same sales and gross margin, **M yields ₹1,81,000 net while N yields only ₹10,000.** M is dramatically more profitable.

**Why this way (the reasoning):** Sales revenue and gross margin measure only the product side; the *cost of serving* a customer depends on their ordering behaviour — small frequent orders, many deliveries and constant sales visits each trigger activities that cost real money. ABC traces those service activities to the customer who causes them, exposing that N's "high-maintenance" pattern all but eats its margin. A traditional average (say, spreading total service cost across sales value) would show both customers as equally profitable, hiding N's true drain. The advice that follows: renegotiate N's terms — larger minimum order sizes, fewer deliveries, self-service ordering — or introduce order/delivery charges, converting behaviour that destroys margin into behaviour that preserves it.

*(Full-marks tip: compute cost-to-serve per driver and state a concrete action for N. Deduction: stopping at gross margin and concluding the customers are equally good.)*

---

### Q27. Ch: Cost Accounting Systems — Non-Integrated Control Accounts (Full Set) (Marks: 10) [Problem]
**Question:** A company maintains a **non-integrated (cost ledger) accounting system.** From the following, write up the Stores Ledger Control, Wages Control, Factory Overhead Control, Work-in-Progress Control, Finished Goods Control, Costing P&L and Cost Ledger (General Ledger Adjustment) Accounts.

| Opening balances (₹) | | Transactions during the year (₹) | |
|---|---|---|---|
| Stores Ledger Control | 50,000 | Materials purchased | 2,00,000 |
| WIP Control | 30,000 | Direct materials issued to WIP | 1,80,000 |
| Finished Goods Control | 40,000 | Indirect materials issued | 20,000 |
| | | Wages incurred (direct 1,20,000; indirect 30,000) | 1,50,000 |
| | | Other factory overhead incurred | 90,000 |
| | | Factory overhead absorbed by WIP | 1,25,000 |
| | | Cost of finished goods produced | 3,60,000 |
| | | Cost of goods sold | 3,50,000 |
| | | Sales | 4,50,000 |

**Solution:**

**WN-1 — Opening Cost Ledger Control (General Ledger Adjustment) balance** = sum of asset balances = 50,000 + 30,000 + 40,000 = **₹1,20,000 (Cr).**

**WN-2 — Factory Overhead Control.** Debits: indirect materials 20,000 + indirect wages 30,000 + other 90,000 = 1,40,000. Absorbed 1,25,000 → **under-absorbed ₹15,000** to Costing P&L.

**Stores Ledger Control A/c**

| Dr | ₹ | Cr | ₹ |
|---|---|---|---|
| To Balance b/d | 50,000 | By WIP Control (direct) | 1,80,000 |
| To GLA (purchases) | 2,00,000 | By Factory OH (indirect) | 20,000 |
| | | By Balance c/d | 50,000 |
| | **2,50,000** | | **2,50,000** |

**Wages Control A/c**

| Dr | ₹ | Cr | ₹ |
|---|---|---|---|
| To GLA (wages paid) | 1,50,000 | By WIP (direct) | 1,20,000 |
| | | By Factory OH (indirect) | 30,000 |
| | **1,50,000** | | **1,50,000** |

**Factory Overhead Control A/c**

| Dr | ₹ | Cr | ₹ |
|---|---|---|---|
| To Stores (indirect matl) | 20,000 | By WIP (absorbed) | 1,25,000 |
| To Wages (indirect) | 30,000 | By Costing P&L (under-abs.) | 15,000 |
| To GLA (other OH) | 90,000 | | |
| | **1,40,000** | | **1,40,000** |

**Work-in-Progress Control A/c**

| Dr | ₹ | Cr | ₹ |
|---|---|---|---|
| To Balance b/d | 30,000 | By Finished Goods | 3,60,000 |
| To Stores (direct matl) | 1,80,000 | By Balance c/d | 95,000 |
| To Wages (direct) | 1,20,000 | | |
| To Factory OH (absorbed) | 1,25,000 | | |
| | **4,55,000** | | **4,55,000** |

**Finished Goods Control A/c**

| Dr | ₹ | Cr | ₹ |
|---|---|---|---|
| To Balance b/d | 40,000 | By Cost of Sales | 3,50,000 |
| To WIP | 3,60,000 | By Balance c/d | 50,000 |
| | **4,00,000** | | **4,00,000** |

**Costing Profit & Loss A/c**

| Dr | ₹ | Cr | ₹ |
|---|---|---|---|
| To Cost of Sales | 3,50,000 | By GLA (Sales) | 4,50,000 |
| To Factory OH (under-abs.) | 15,000 | | |
| To GLA (Net profit) | 85,000 | | |
| | **4,50,000** | | **4,50,000** |

**Cost Ledger (General Ledger Adjustment) A/c**

| Dr | ₹ | Cr | ₹ |
|---|---|---|---|
| To Costing P&L (Sales) | 4,50,000 | By Balance b/d | 1,20,000 |
| To Balance c/d | 1,95,000 | By Stores (purchases) | 2,00,000 |
| | | By Wages | 1,50,000 |
| | | By Factory OH (other) | 90,000 |
| | | By Costing P&L (profit) | 85,000 |
| | **6,45,000** | | **6,45,000** |

**Answer:** Closing balances — Stores ₹50,000, WIP ₹95,000, Finished Goods ₹50,000 (total ₹1,95,000) = closing GLA ₹1,95,000; **Costing net profit ₹85,000.**

**Why this way (the reasoning):** In a non-integrated system the cost books are self-balancing but **separate** from the financial ledger, so there is no real cash/creditor/asset account inside them. The **General Ledger Adjustment (Cost Ledger Control) Account** stands in for the entire financial ledger: every item that in reality touches cash, creditors or the outside world is completed by a contra to GLA. That is why purchases, wages, other overhead and the sale value all pass through GLA, and why the closing GLA balance must equal the sum of the real asset balances (Stores + WIP + FG). This double-entry discipline is what makes the cost ledger *self-balancing* and lets us prove nothing is lost — the ₹1,95,000 tie-out is the proof. Under-absorbed overhead is routed to the Costing P&L (not buried in WIP) so that inventory carries only absorbed cost and the recovery shortfall is transparent.

*(Full-marks tip: the GLA closing balance must equal Stores+WIP+FG — always cross-check. Deduction: omitting the GLA contra for purchases/wages/sales, or leaving the under-absorption inside WIP.)*

---

### Q28. Ch: Cost Accounting Systems — Memorandum Reconciliation Statement (Marks: 8) [Problem]
**Question:** The profit as per **cost accounts** is ₹1,00,000. From the following, prepare a **memorandum reconciliation statement** and ascertain the profit as per financial accounts.

| Item | ₹ |
|---|---|
| Interest received (financial only) | 12,000 |
| Dividend received (financial only) | 7,000 |
| Notional rent of own building charged in cost | 10,000 |
| Notional interest on capital charged in cost | 5,000 |
| Office overhead over-recovered in cost | 5,000 |
| Preliminary expenses written off (financial only) | 6,000 |
| Loss on sale of asset (financial only) | 4,000 |
| Donation paid (financial only) | 3,000 |
| Factory overhead under-recovered in cost | 8,000 |
| Opening stock valued higher in financial by | 3,000 |
| Closing stock valued higher in financial by | 4,000 |
| Depreciation excess charged in financial | 5,000 |

**Solution:**

**Memorandum Reconciliation Statement (Cost → Financial)**

| Particulars | Add (₹) | Less (₹) |
|---|---|---|
| Profit as per Cost Accounts | 1,00,000 | |
| Interest received (financial income) | 12,000 | |
| Dividend received (financial income) | 7,000 | |
| Notional rent (cost-only charge, add back) | 10,000 | |
| Notional interest on capital (cost-only charge) | 5,000 | |
| Office overhead over-recovered in cost | 5,000 | |
| Closing stock higher in financial | 4,000 | |
| Preliminary expenses written off | | 6,000 |
| Loss on sale of asset | | 4,000 |
| Donation paid | | 3,000 |
| Factory overhead under-recovered in cost | | 8,000 |
| Opening stock higher in financial | | 3,000 |
| Depreciation excess in financial | | 5,000 |
| **Totals** | **1,43,000** | **29,000** |

Profit as per Financial Accounts = 1,43,000 − 29,000 = **₹1,14,000.**

**Answer:** **Profit as per financial accounts = ₹1,14,000.**

**Why this way (the reasoning):** Two ledgers differ because each records some items the other ignores or values differently, so reconciliation walks item-by-item asking *"does this make the financial figure higher or lower than the cost figure?"* **Purely financial incomes** (interest, dividend) never entered the cost profit, so they raise financial profit → add. **Purely financial expenses/losses** (preliminary expenses, loss on sale, donation) reduce financial profit → deduct. **Notional charges** (rent on own building, interest on capital) are cost-book fictions with no real outflow; the cost profit was reduced by them, so add them back. For **over/under recovery**: over-recovery means cost accounts charged *more* overhead than actual, so cost profit was understated → add; under-recovery means cost charged *less* → cost profit overstated → deduct. **Stock**: a higher closing stock in financial books means less went to cost of sales there → higher financial profit → add; a higher opening stock means the reverse → deduct. Getting the *direction* right for each cause is the whole skill — the amounts are easy, the signs are where marks are won or lost.

*(Full-marks tip: state clearly you are moving cost→financial and justify each sign. Deduction: reversing over/under-recovery, or mishandling the opening vs closing stock direction.)*

---

### Q29. Ch: Cost Accounting Systems — Reconciliation Worked Backwards (Financial → Cost) (Marks: 6) [Problem]
**Question:** The profit as per **financial accounts** is ₹1,50,000. Using the items below, ascertain the profit as per **cost accounts**, explaining the direction of each adjustment.

| Item | ₹ |
|---|---|
| Interest on investments (financial income) | 20,000 |
| Rent received (financial income) | 8,000 |
| Goodwill written off (financial only) | 15,000 |
| Fines paid (financial only) | 5,000 |
| Notional salary of proprietor charged in cost | 24,000 |
| Overheads over-absorbed in cost | 6,000 |
| Closing stock valued higher in cost by | 4,000 |

**Solution:**

**Reconciliation Statement (Financial → Cost)**

| Particulars | Add (₹) | Less (₹) |
|---|---|---|
| Profit as per Financial Accounts | 1,50,000 | |
| Interest on investments (financial income, not in cost) | | 20,000 |
| Rent received (financial income, not in cost) | | 8,000 |
| Goodwill written off (financial expense, not in cost) | 15,000 | |
| Fines paid (financial expense, not in cost) | 5,000 | |
| Notional salary of proprietor (cost-only charge) | 24,000 | |
| Overheads over-absorbed in cost | 6,000 | |
| Closing stock higher in cost | 4,000 | |
| **Totals** | **2,04,000** | **28,000** |

Profit as per Cost Accounts = 2,04,000 − 28,000 = **₹1,76,000.**

**Answer:** **Profit as per cost accounts = ₹1,76,000.**

**Why this way (the reasoning):** Reconciliation is symmetric — every rule of the cost→financial walk simply **reverses** when you travel financial→cost. Incomes that appear only in financial books (interest, rent) inflated the financial profit but never touched cost profit, so to recover the cost figure we **deduct** them. Expenses that hit only financial books (goodwill, fines) depressed financial profit, so we **add** them back to reach the higher cost profit. The proprietor's notional salary was charged only in cost, pulling cost profit *down*, so it is added when moving toward cost. Over-absorption made the cost profit *higher* than financial (extra overhead credited back), so it is added; and a higher closing stock in the cost books means cost profit is higher, so again add. Mastering reconciliation in *both* directions proves you understand the underlying cause of each difference rather than memorising a one-way table.

*(Full-marks tip: label the direction and mirror each sign correctly; a quick check is that reversing every sign should return the financial figure. Deduction: applying the cost→financial signs unchanged.)*

---

### Q30. Ch: Cost Accounting Systems — Integrated Accounting: Advise on Adoption (Marks: 5) [Case/Application]
**Question:** A company currently keeps **separate cost and financial ledgers** and spends significant effort each period reconciling the two profits. Management is considering an **integrated accounting system.** Explain what it is, why it removes the need for reconciliation, and advise, noting one limitation.

**Answer:**

**Governing principle.** An **integrated (integral) accounting system** maintains **one set of books** that serves both cost and financial accounting, recording all transactions in a single ledger so that cost and financial data flow from common accounts.

**Why reconciliation disappears.** Reconciliation is needed only because two *separate* sets of books value or include items differently. In an integrated system there is a **single profit figure** drawn from one ledger — there are no two profits to differ, so a reconciliation statement is unnecessary by construction. Notional charges (notional rent, interest on capital) are not booked, and there is no under/over-recovery gap between two ledgers because actual and recovered figures meet in the same accounts (any absorption difference is disclosed within that one set).

**Advantages / Advice.** Integration gives a **single, coherent set of accounts**, avoids duplication of effort and records, eliminates reconciliation work, provides quicker information, and reduces clerical cost and the risk of the two ledgers drifting apart. Given that this company is expending real effort on periodic reconciliation, **adoption is advisable**, provided its accounting staff and software can support the required coding of transactions.

**Limitation.** Integration demands a well-designed coding structure and trained staff; a small firm with simple needs may find the transition cost and system complexity outweigh the benefit, and some managers value the independent cross-check that two separate ledgers provide.

**Why this way (the reasoning):** The root cause of profit differences is *duplication* — the same events recorded twice under different conventions. Integration attacks the cause rather than the symptom: with one ledger there is nothing to reconcile because there is only one truth. The trade-off is that a unified system needs disciplined design and capable staff; the advice therefore turns on whether the recurring reconciliation effort the firm already bears exceeds the one-time cost of integrating — which, given its stated pain, it does.

*(Full-marks tip: explicitly link "one set of books → one profit → no reconciliation," and give a balanced limitation. Deduction: listing advantages without explaining *why* reconciliation becomes unnecessary.)*

---

### Q31. Ch: Cost Accounting Systems — Missing-Figure Reconstruction of Control Accounts (Marks: 8) [Problem]
**Question:** From the incomplete records of a cost ledger, determine (a) the cost of finished goods produced, (b) the under/over-absorbed overhead, and (c) the costing profit. Present the relevant control accounts.

| Data (₹) | |
|---|---|
| Opening WIP | 45,000 |
| Direct materials issued to WIP | 2,10,000 |
| Direct wages | 1,50,000 |
| Overhead absorbed by WIP (at 80% of direct wages) | ? |
| Closing WIP | 55,000 |
| Actual factory overhead incurred | 1,32,000 |
| Opening Finished Goods | 60,000 |
| Closing Finished Goods | 70,000 |
| Sales | 6,00,000 |

**Solution:**

**WN-1 — Overhead absorbed** = 80% × 1,50,000 = **₹1,20,000.**

**WN-2 — Under-absorption** = actual 1,32,000 − absorbed 1,20,000 = **₹12,000 under-absorbed** → Costing P&L.

**Work-in-Progress Control A/c**

| Dr | ₹ | Cr | ₹ |
|---|---|---|---|
| To Balance b/d | 45,000 | By Finished Goods (bal. fig.) | 4,70,000 |
| To Direct materials | 2,10,000 | By Balance c/d | 55,000 |
| To Direct wages | 1,50,000 | | |
| To Overhead absorbed | 1,20,000 | | |
| | **5,25,000** | | **5,25,000** |

**(a) Cost of finished goods produced = ₹4,70,000** (balancing figure).

**Finished Goods Control A/c**

| Dr | ₹ | Cr | ₹ |
|---|---|---|---|
| To Balance b/d | 60,000 | By Cost of Sales (bal. fig.) | 4,60,000 |
| To WIP | 4,70,000 | By Balance c/d | 70,000 |
| | **5,30,000** | | **5,30,000** |

Cost of Sales = **₹4,60,000.**

**Costing Profit & Loss A/c**

| Dr | ₹ | Cr | ₹ |
|---|---|---|---|
| To Cost of Sales | 4,60,000 | By Sales | 6,00,000 |
| To Factory OH (under-abs.) | 12,000 | | |
| To Net Profit | 1,28,000 | | |
| | **6,00,000** | | **6,00,000** |

**Answer:** (a) Finished goods produced **₹4,70,000**; (b) **under-absorbed overhead ₹12,000**; (c) **costing net profit ₹1,28,000.**

**Why this way (the reasoning):** Control accounts are self-balancing, so a single unknown becomes a **balancing figure** — the cost of finished goods produced is simply everything that entered WIP minus what remains as closing WIP, because production is the only other outlet. The same logic on the Finished Goods account yields cost of sales. Overhead is *absorbed* on a predetermined rate (80% of wages) but *incurred* at actual; the ₹12,000 gap is a recovery shortfall that must be charged to the Costing P&L rather than left in WIP, otherwise unsold inventory would carry more than the absorbed cost the rate intended. This "reconstruct the missing figure" technique tests whether you truly understand the *flow* of cost through the system — materials and conversion in, finished goods out, sold goods against revenue — rather than mechanically copying a given number.

*(Full-marks tip: show each balancing figure explicitly and route the ₹12,000 under-absorption to the P&L, not to stock. Deduction: absorbing overhead at actual, or netting under-absorption inside WIP so the profit is wrong.)*

---

### Q32. Ch: Overheads – Absorption Costing — Choosing a Method to Dispose of Under/Over-Absorption (Marks: 5) [Case/Application]
**Question:** At year-end a company finds material **under-absorption of factory overhead.** The accountant proposes to write the *entire* amount off to the Costing P&L. On analysis, part of the under-absorption is due to an **abnormal plant breakdown** and part to a **general rise in material and power prices** affecting all output. **Comment on the validity of a single write-off and advise the correct treatment.**

**Answer:**

**Governing principle.** Under/over-absorbed overhead may be disposed of by **(i)** transfer to the Costing P&L (write-off), **(ii)** use of a **supplementary rate** to spread it over cost of sales, finished goods and WIP, or **(iii)** carrying forward to the next period. The choice depends on the **cause and magnitude** of the variance.

**Application.** The abnormal-breakdown portion reflects *lost capacity*, not value added to product; charging it to units would inflate inventory with the cost of idleness, so it must be **written off to the Costing P&L**. The price-rise portion is a **normal** cost that genuinely belongs to the goods produced this year; since those goods are spread across cost of sales, finished stock and WIP, it should be recovered through a **supplementary rate** so that inventory is stated at true cost (AS-2). Carrying forward is inappropriate here because the causes are current-year and not merely seasonal.

**Conclusion/Advice.** A blanket write-off is **only partly correct.** Split the under-absorption: write the abnormal-breakdown share off to the Costing P&L, and apportion the normal price-rise share by a supplementary rate over cost of sales, finished goods and WIP.

**Why this way (the reasoning):** The disposal method must respect *why* the variance arose. Abnormal costs are period losses — capitalising them would let unsold units carry the cost of a breakdown, distorting inventory and future results. Normal cost increases, by contrast, are legitimate product costs that happen to have been under-recovered; a supplementary rate restores each pool (sold, finished, in-process) to the cost it should have borne. Writing everything off is quick but violates the matching and inventory-valuation principles for the normal portion; a supplementary rate for everything wrongly capitalises abnormal losses. Correct practice separates the two.

*(Full-marks tip: name all three disposal methods, then justify the split by cause. Deduction: recommending one method for the whole amount without distinguishing abnormal from normal.)*

---

### Q33. Ch: Activity-Based Costing — The Cost "Death Spiral" and Pricing (Marks: 6) [Case/Application]
**Question:** A firm using **traditional labour-hour absorption** notices it consistently **wins bids for simple, high-volume jobs** (often at a loss) but **loses bids for complex, low-volume jobs** to competitors. Overhead is large and dominated by set-ups, scheduling and inspection. **Explain, using ABC reasoning, why this pattern arises and advise.**

**Answer:**

**Governing principle.** Under volume-based absorption, overhead is charged in proportion to a single volume measure (labour hours). When overhead is actually driven by **transactions/complexity** (set-ups, scheduling, inspection), simple high-volume jobs are **over-costed** and complex low-volume jobs are **under-costed** — the classic ABC distortion.

**Application (illustrative).** Suppose a simple job needs many labour hours but few set-ups, while a complex job needs few labour hours but many set-ups. The labour-hour rate loads most overhead on the simple job's high hours and almost none on the complex job's transaction-heavy profile. So:
- The **complex job is quoted too cheaply by the firm's competitors** (who cost accurately) and **too dearly by this firm** → the firm loses it.
- The **simple job is quoted too dearly elsewhere and too cheaply here** → the firm wins it, but its price fails to cover the transaction overhead it truly triggers → a loss.

As the firm chases more high-volume work, its overhead per remaining unit rises, prices climb, more accurate rivals undercut it, and it spirals into ever-worse mix — the **"death spiral."**

**Conclusion/Advice.** Adopt **activity-based costing** to trace set-up, scheduling and inspection costs to the jobs that cause them. Re-price on ABC cost: complex jobs will show higher, defensible prices (still competitive), and simple jobs will reveal their true cost, ending loss-making wins. This corrects the mix and halts the spiral.

**Why this way (the reasoning):** The pattern is a signature symptom of a volume-based system misapplied to transaction-driven overhead. Because averaging *conserves the total*, whatever the firm under-charges complex jobs it must over-charge simple ones — so its winning bids and losing bids are two sides of the same distortion. Rivals who cost by activity see the real numbers and pick off exactly the jobs this firm mis-prices. ABC breaks the spiral by charging each job for the activities it consumes, so prices track cost and the firm competes on the work it is genuinely efficient at.

*(Full-marks tip: connect over-/under-costing to *which bids are won and lost* and name the death spiral. Deduction: describing ABC generically without explaining the bidding pattern.)*

---

### Q34. Ch: Cost Accounting Systems — Prepare Cost & Financial P&L and Reconcile (Marks: 10) [Problem]
**Question:** From the following, prepare the **Costing Profit & Loss Account** and the **Financial Profit & Loss Account** for the year, and reconcile the two profits. Output = sales = 10,000 units.

| Particulars | ₹ |
|---|---|
| Sales (10,000 units @ ₹100) | 10,00,000 |
| Direct materials | 3,00,000 |
| Direct wages | 2,00,000 |
| Works overhead — actual | 1,50,000 |
| Works overhead — absorbed in cost @ 60% of wages | 1,20,000 |
| Administration overhead — actual | 80,000 |
| Administration overhead — absorbed in cost @ ₹9/unit | 90,000 |
| Selling overhead — actual | 70,000 |
| Selling overhead — absorbed in cost @ 5% of sales | 50,000 |
| Interest received (financial only) | 10,000 |
| Dividend received (financial only) | 4,000 |
| Loss on sale of furniture (financial only) | 6,000 |

**Solution:**

**Costing Profit & Loss A/c**

| Particulars | ₹ |
|---|---|
| Sales | 10,00,000 |
| Less: Direct materials | 3,00,000 |
| Less: Direct wages | 2,00,000 |
| **Prime cost** | **5,00,000** |
| Add: Works OH absorbed (60% × 2,00,000) | 1,20,000 |
| **Works cost** | **6,20,000** |
| Add: Administration OH absorbed (₹9 × 10,000) | 90,000 |
| **Cost of production** | **7,10,000** |
| Add: Selling OH absorbed (5% × 10,00,000) | 50,000 |
| **Cost of sales** | **7,60,000** |
| **Costing Profit** | **2,40,000** |

**Financial Profit & Loss A/c**

| Dr | ₹ | Cr | ₹ |
|---|---|---|---|
| To Direct materials | 3,00,000 | By Sales | 10,00,000 |
| To Direct wages | 2,00,000 | By Interest received | 10,000 |
| To Works OH (actual) | 1,50,000 | By Dividend received | 4,000 |
| To Administration OH (actual) | 80,000 | | |
| To Selling OH (actual) | 70,000 | | |
| To Loss on sale of furniture | 6,000 | | |
| To Net Profit | 2,08,000 | | |
| | **10,14,000** | | **10,14,000** |

**Reconciliation Statement (Cost → Financial)**

| Particulars | Add (₹) | Less (₹) |
|---|---|---|
| Profit as per Cost Accounts | 2,40,000 | |
| Works OH under-absorbed (1,20,000 vs 1,50,000) | | 30,000 |
| Administration OH over-absorbed (90,000 vs 80,000) | 10,000 | |
| Selling OH under-absorbed (50,000 vs 70,000) | | 20,000 |
| Interest received (financial income) | 10,000 | |
| Dividend received (financial income) | 4,000 | |
| Loss on sale of furniture (financial expense) | | 6,000 |
| **Totals** | **2,64,000** | **56,000** |

Profit as per Financial Accounts = 2,64,000 − 56,000 = **₹2,08,000** ✓ (agrees with the Financial P&L).

**Answer:** **Costing profit ₹2,40,000; financial profit ₹2,08,000**, reconciled through overhead absorption differences and purely financial items.

**Why this way (the reasoning):** The cost account uses **absorbed (predetermined)** overheads to build product cost, while the financial account records **actual** overheads and includes items outside the costing scope. Each overhead therefore creates a reconciling item equal to the absorbed-vs-actual gap: works and selling overhead were *under-absorbed* (cost charged less than actual), so cost profit was overstated → deduct; administration was *over-absorbed* → add. Interest and dividend are incomes the cost account never saw, and the furniture loss is a capital loss excluded from cost — all pure-financial items adjusting to the financial figure. Preparing both statements side-by-side and then reconciling proves the ₹32,000 gap is fully explained by *known causes*, not error — which is exactly what a reconciliation is meant to demonstrate. The tie-out to ₹2,08,000 confirms every difference has been accounted for.

*(Full-marks tip: build the cost sheet in proper stages (prime → works → production → sales), then reconcile each overhead's absorbed-vs-actual direction and add the pure-financial items. Deduction: mixing actual overheads into the Costing P&L, or a reconciliation that fails to land on the financial profit.)*

### Q35. Ch: Cost Sheet — Cost sheet with stock/scrap adjustments and tender pricing (Marks: 10) [Problem]
**Question:** From the records of Vega Manufacturing Ltd for the year ended 31-03-2026, prepare a Cost Sheet, and using the overhead-recovery rates so derived, quote a tender price for a special order that must yield a profit of **20% on the tender price**.

| Particulars | ₹ |
|---|---:|
| Raw materials — opening stock | 1,50,000 |
| Raw materials — purchases | 11,00,000 |
| Carriage inward on materials | 30,000 |
| Raw materials — closing stock | 1,80,000 |
| Direct wages | 5,00,000 |
| Direct (chargeable) expenses | 40,000 |
| Works / factory overheads | 3,50,000 |
| Work-in-progress — opening | 60,000 |
| Work-in-progress — closing | 80,000 |
| Sale of factory scrap (arising in production) | 20,000 |
| Administration overheads (production-related) | (10% of works cost) |
| Finished goods — opening | 1,05,000 |
| Finished goods — closing (at current cost) | 1,50,000 |
| Selling & distribution overheads | (6% of works cost) |

Special order data: materials ₹2,20,000; direct wages ₹1,00,000; direct expenses ₹8,000. Recover works OH, admin OH and S&D OH at the same rates as in the cost sheet.

**Solution:**

**WN-1 — Raw materials consumed:** Opening 1,50,000 + Purchases 11,00,000 + Carriage inward 30,000 − Closing 1,80,000 = **₹11,00,000**. (Carriage inward is a cost of *getting material in*, so it is part of material cost, not an expense charged later.)

**WN-2 — Overhead recovery rates (from the sheet):** Works OH = 3,50,000 / 5,00,000 wages = **70% of direct wages**; Admin OH = **10% of works cost**; S&D OH = **6% of works cost** (as given).

**Cost Sheet for the year ended 31-03-2026**

| Particulars | ₹ |
|---|---:|
| Raw materials consumed (WN-1) | 11,00,000 |
| Direct wages | 5,00,000 |
| Direct expenses | 40,000 |
| **Prime Cost** | **16,40,000** |
| Add: Works overheads (70% of wages) | 3,50,000 |
| Add: Opening WIP | 60,000 |
| Less: Closing WIP | (80,000) |
| Less: Sale of factory scrap | (20,000) |
| **Works / Factory Cost** | **19,50,000** |
| Add: Administration OH (10% of works cost) | 1,95,000 |
| **Cost of Production** | **21,45,000** |
| Add: Opening finished goods | 1,05,000 |
| Less: Closing finished goods | (1,50,000) |
| **Cost of Goods Sold** | **21,00,000** |
| Add: Selling & distribution OH (6% of works cost) | 1,17,000 |
| **Cost of Sales** | **22,17,000** |
| Add: Profit (20% on cost) | 4,43,400 |
| **Sales** | **26,60,400** |

**Statement of Tender Price (Special Order)**

| Particulars | ₹ |
|---|---:|
| Direct materials | 2,20,000 |
| Direct wages | 1,00,000 |
| Direct expenses | 8,000 |
| **Prime Cost** | **3,28,000** |
| Works OH (70% of wages) | 70,000 |
| **Works Cost** | **3,98,000** |
| Admin OH (10% of works cost) | 39,800 |
| **Cost of Production** | **4,37,800** |
| S&D OH (6% of works cost) | 23,880 |
| **Total Cost** | **4,61,680** |
| Profit (20% on tender price = 1/4 of cost) | 1,15,420 |
| **Tender Price** | **5,77,100** |

Profit is 20% *of price*, so cost = 80% of price → Tender price = 4,61,680 ÷ 0.80 = **₹5,77,100**.

**Answer:** Cost of sales ₹22,17,000; profit ₹4,43,400; sales ₹26,60,400. Tender price for the special order = **₹5,77,100**.

**Why this way (the reasoning):** Every stock and scrap line sits at the stage where the value is *actually consumed or recovered*. Carriage inward and the two raw-material stocks belong to material cost because they change what was physically put into production. WIP is adjusted *inside* works cost — not before prime cost — because a job half-finished has already absorbed materials, labour AND factory overhead, so it can only be netted after works overhead is added. Factory scrap is credited to *works cost* (not sales) because scrap is a recovery that reduces the net cost of running the factory; treating its sale as ordinary revenue would overstate both cost and profit. Finished-goods stock is adjusted only *after* cost of production, because a unit is not "finished" until it has borne production admin OH. The classic trap is deducting scrap from prime cost or adjusting FG before admin OH — both misstate the per-stage cost. For the tender we drop the one-off items (WIP, scrap, opening/closing stocks relate to a *period*, not a *fresh order*) and rebuild cost from the recovery rates, because a quotation estimates the resources the new job will itself consume.

*(Full-marks tip: examiners award the marks for placing scrap and WIP at the correct stage and for solving profit as a fraction of *price* — writing 20% × cost instead of cost ÷ 0.80 is the single most common deduction on the tender.)*

---

### Q36. Ch: Cost Sheet — Reverse working: finding missing figures from ratios (Marks: 8) [Problem]
**Question:** The cost records of Orion Ltd are incomplete. From the data below, work **backwards** to prepare the cost sheet and ascertain the missing figures — materials consumed, prime cost, works cost, cost of production, cost of sales and profit.

| Particulars | Data |
|---|---|
| Direct wages | ₹4,00,000 |
| Direct expenses | ₹50,000 |
| Works overheads | 125% of direct wages |
| Administration overheads | 20% of works cost |
| Selling & distribution overheads | 10% of works cost |
| Profit | 20% on sales |
| Sales | ₹24,37,500 |

**Solution:**

**WN-1 — Fix the total cost from the top:** Profit is 20% *on sales*, so cost of sales = 80% × 24,37,500 = **₹19,50,000**.

**WN-2 — Express cost of sales in terms of works cost (W):**
- Cost of production = W + Admin OH = W + 0.20W = 1.20W
- Cost of sales = Cost of production + S&D = 1.20W + 0.10W = **1.30W**
- 1.30W = 19,50,000 → **W (Works cost) = ₹15,00,000**.

**WN-3 — Works overheads and prime cost:** Works OH = 125% × 4,00,000 = **₹5,00,000**. Prime cost = Works cost − Works OH = 15,00,000 − 5,00,000 = **₹10,00,000**.

**WN-4 — Materials consumed:** Prime cost − Wages − Direct expenses = 10,00,000 − 4,00,000 − 50,000 = **₹5,50,000**.

**Cost Sheet (reconstructed)**

| Particulars | ₹ |
|---|---:|
| Materials consumed (WN-4) | 5,50,000 |
| Direct wages | 4,00,000 |
| Direct expenses | 50,000 |
| **Prime Cost** | **10,00,000** |
| Works overheads (125% of wages) | 5,00,000 |
| **Works Cost** | **15,00,000** |
| Administration OH (20% of works cost) | 3,00,000 |
| **Cost of Production** | **18,00,000** |
| Selling & distribution OH (10% of works cost) | 1,50,000 |
| **Cost of Sales** | **19,50,000** |
| Profit (20% on sales) | 4,87,500 |
| **Sales** | **24,37,500** |

**Answer:** Materials consumed ₹5,50,000; prime cost ₹10,00,000; works cost ₹15,00,000; cost of production ₹18,00,000; cost of sales ₹19,50,000; profit ₹4,87,500.

**Why this way (the reasoning):** When intermediate figures are missing you cannot build the sheet upward from materials — you do not yet know materials. The trick is that admin and S&D are both anchored to *works cost*, so the whole structure below prime cost can be written as a single multiple of W (1.30W). Once you convert the one figure you *do* know from the bottom (sales → cost of sales via the profit relation), you get W in one step, then unwind upward. Students lose marks by treating "20% on sales" as if it were 20% on cost — sales and cost are different bases, and here profit ÷ sales = 20% means cost is 80% of sales, not 100%/120%. Recognising which base each percentage sits on (wages, works cost, or sales) is the entire skill this variant tests.

*(Full-marks tip: state the base of every ratio before substituting; the examiner specifically checks that you did not mix "on sales" with "on cost", and awards method marks even if a later arithmetic slip occurs.)*

---

### Q37. Ch: Cost Sheet — Treatment of items in cost accounts (Marks: 5) [Theory]
**Question:** State, with reasons, whether and how each of the following is dealt with in a Cost Sheet: (i) interest on capital / loans; (ii) cash discount received; (iii) donations to a political party; (iv) income tax paid; (v) notional rent of the firm's own factory building; (vi) cost of abnormal idle time; (vii) carriage outward; (viii) research cost for a specific customer order.

**Answer:** The governing principle is that only costs that are **normal and incurred in the process of production or sale of the product** enter the cost sheet; items of **financial nature, appropriations of profit, and abnormal losses** are excluded and taken to the financial (Costing P&L) statement.

| Item | Treatment in Cost Sheet | Reason |
|---|---|---|
| (i) Interest on capital / loans | **Excluded** | Financial charge on the way the business is *funded*, not a cost of *making* the product (a pure-cost view; some managerial decisions add notional interest separately). |
| (ii) Cash discount received | **Excluded** | A financial benefit for prompt payment, unrelated to production cost. |
| (iii) Donation to political party | **Excluded** | Appropriation of profit / non-cost item. |
| (iv) Income tax | **Excluded** | A charge on profit, not an element of cost. |
| (v) Notional rent of own building | **Included** (as a notional cost) | For true cost comparison, the building has an opportunity cost; ignoring it understates cost of an owned vs rented facility. |
| (vi) Abnormal idle-time cost | **Excluded** from cost; charged to Costing P&L | Abnormal losses must not distort product cost; only *normal* idle time is absorbed. |
| (vii) Carriage outward | **Included** in Selling & Distribution OH | It is a cost of *delivering* the product to the customer. |
| (viii) Research for a specific order | **Included** — charged to that job/order | It is directly caused by, and traceable to, that customer's work. |

**Conclusion:** The recurring test is *cause and normality*: is the item caused by making/selling the product, and is it normal? If yes, it is a cost; if it is financial, an appropriation, or abnormal, it is excluded.

**Why this way (the reasoning):** Cost accounting exists to give a *decision-useful* product cost, so it deliberately filters out anything that reflects how the firm is financed or how its profit is distributed — those vary with capital structure and tax law, not with the product. Notional rent is the subtle one: it is *added* even though no cash moves, because leaving it out would make an owned factory look artificially cheaper than a rented one and mislead a make-or-buy or pricing decision. Abnormal idle time is the other trap: it is a real cash cost but is *excluded from product cost* because loading a one-off breakdown onto units would make good production look expensive and destroy period-to-period comparability.

*(Full-marks tip: give a *reason* per item, not just "excluded"; and never confuse carriage inward (material cost) with carriage outward (S&D) — that swap is a guaranteed mark loss.)*

---

### Q38. Ch: Cost Sheet — Per-unit cost sheet with scrap and tender under cost escalation (Marks: 8) [Problem]
**Question:** Solaris Ltd produced and sold 10,000 units during the quarter. Prepare a cost sheet showing total and per-unit cost, then quote a price for a fresh order of **3,000 units** for next quarter, given that material prices will rise **10%** and wage rates **5%**, other rates unchanged. Profit is **20% on cost**.

| Particulars | ₹ |
|---|---:|
| Materials consumed | 6,00,000 |
| Direct wages | 3,00,000 |
| Direct expenses | 50,000 |
| Factory overheads | (50% of direct wages) |
| Sale of factory scrap | 15,000 |
| Administration overheads | (10% of works cost) |
| Selling & distribution overheads | (5% of works cost) |

**Solution:**

**WN-1 — Factory OH:** 50% × 3,00,000 = ₹1,50,000. Scrap sale ₹15,000 is credited to works cost.

**Cost Sheet for the quarter (10,000 units)**

| Particulars | Total ₹ | Per unit ₹ |
|---|---:|---:|
| Materials consumed | 6,00,000 | 60.00 |
| Direct wages | 3,00,000 | 30.00 |
| Direct expenses | 50,000 | 5.00 |
| **Prime Cost** | **9,50,000** | **95.00** |
| Factory OH (50% of wages) | 1,50,000 | 15.00 |
| Less: Sale of factory scrap | (15,000) | (1.50) |
| **Works Cost** | **10,85,000** | **108.50** |
| Admin OH (10% of works cost) | 1,08,500 | 10.85 |
| **Cost of Production** | **11,93,500** | **119.35** |
| S&D OH (5% of works cost) | 54,250 | 5.425 |
| **Cost of Sales** | **12,47,750** | **124.775** |
| Profit (20% on cost) | 2,49,550 | 24.955 |
| **Sales** | **14,97,300** | **149.73** |

**WN-2 — Escalated per-unit direct costs for the new order:** Materials 60 × 1.10 = ₹66; Wages 30 × 1.05 = ₹31.50; Direct expenses unchanged ₹5.

**Statement of Tender Price — order of 3,000 units**

| Particulars | Per unit ₹ | 3,000 units ₹ |
|---|---:|---:|
| Materials (escalated) | 66.00 | 1,98,000 |
| Direct wages (escalated) | 31.50 | 94,500 |
| Direct expenses | 5.00 | 15,000 |
| **Prime Cost** | 102.50 | 3,07,500 |
| Factory OH (50% of new wages) | 15.75 | 47,250 |
| **Works Cost** | 118.25 | 3,54,750 |
| Admin OH (10% of works cost) | 11.825 | 35,475 |
| **Cost of Production** | 130.075 | 3,90,225 |
| S&D OH (5% of works cost) | 5.9125 | 17,737.50 |
| **Total Cost** | 135.9875 | 4,07,962.50 |
| Profit (20% on cost) | 27.1975 | 81,592.50 |
| **Tender Price** | **163.185** | **4,89,558** |

**Answer:** Quarter cost of sales ₹12,47,750; sales ₹14,97,300. Tender price for 3,000 units ≈ **₹4,89,558 (₹163.19 per unit)**.

**Why this way (the reasoning):** Notice that the ₹15,000 scrap credit appears in the *actual* cost sheet but **not** in the tender. Scrap is a recovery from goods *already produced*; a fresh estimate has generated no scrap yet, so crediting a notional scrap figure would understate the quotation and erode the margin. Overhead recovery *rates* (50% of wages, 10% and 5% of works cost) are carried forward because they express a stable relationship between overhead and activity — but they are applied to the *escalated* wage and works-cost bases, so factory OH automatically rises with wages (15.00 → 15.75) without any separate adjustment. The common error is escalating materials and wages but forgetting that percentage-based overheads move with them, leaving overheads at old-quarter rupee values.

*(Full-marks tip: apply the % overheads to the *new* bases and omit the scrap credit from the tender — carrying scrap into a fresh quotation, or freezing overhead at old rupee amounts, are the two errors examiners hunt for here.)*

---

### Q39. Ch: Unit & Batch Costing — Economic Batch Quantity with setup and carrying cost (Marks: 10) [Problem]
**Question:** Nimbus Components makes a part for its own assembly line. Annual demand is **48,000 units**, set-up cost per production run is **₹500**, manufacturing cost is **₹20 per unit**, and carrying cost (including interest on capital blocked) is **15% of unit cost per annum**. (a) Compute the Economic Batch Quantity (EBQ) and the associated annual cost. (b) The production manager proposes making the part in **6 runs of 8,000 units** to "save on set-ups" — evaluate. (c) A new quick-changeover method would cut set-up cost to **₹125**; find the revised EBQ and comment on the lesson.

**Solution:**

**WN-1 — Carrying cost per unit p.a. (C):** 15% × ₹20 = **₹3 per unit p.a.**

**WN-2 — EBQ:**
$$EBQ=\sqrt{\frac{2DS}{C}}=\sqrt{\frac{2\times48,000\times500}{3}}=\sqrt{1,60,00,000}= \mathbf{4,000\ units}$$

**(a) Annual cost at EBQ = 4,000 units**

| Particulars | Working | ₹ |
|---|---|---:|
| No. of set-ups | 48,000 ÷ 4,000 = 12 | — |
| Set-up cost | 12 × 500 | 6,000 |
| Carrying cost | (4,000 ÷ 2) × 3 | 6,000 |
| **Total relevant cost** | | **12,000** |

At the EBQ the two costs are equal (₹6,000 each) — the hallmark of the optimum.

**(b) Manager's proposal — 6 runs of 8,000 units**

| Particulars | Working | ₹ |
|---|---|---:|
| Set-up cost | 6 × 500 | 3,000 |
| Carrying cost | (8,000 ÷ 2) × 3 | 12,000 |
| **Total** | | **15,000** |

Extra cost vs EBQ = 15,000 − 12,000 = **₹3,000 higher**. The set-up saving of ₹3,000 is *more than wiped out* by ₹6,000 of extra carrying cost. **Reject the proposal.**

**(c) Revised EBQ after set-up cost falls to ₹125:**
$$EBQ=\sqrt{\frac{2\times48,000\times125}{3}}=\sqrt{40,00,000}= \mathbf{2,000\ units}$$ (12 → 24 runs).

**Answer:** EBQ = 4,000 units (total cost ₹12,000). The 8,000-unit proposal costs ₹15,000 (₹3,000 worse) and should be rejected. Cutting set-up cost to ₹125 halves the EBQ to 2,000 units.

**Why this way (the reasoning):** EBQ balances two opposing forces: bigger batches cut *set-up* cost (fewer runs) but raise *carrying* cost (more average stock tying up capital). The square-root formula finds the batch where a further unit of size adds exactly as much carrying cost as it saves in set-up cost — which is why at the optimum the two totals are equal, a fast self-check. The manager's "save on set-ups" instinct is the classic trap: it looks only at one side of the trade-off. Part (c) delivers the deeper insight behind lean/JIT: because EBQ varies with the *square root* of set-up cost, slashing set-up time is exactly what lets a plant run economically in *smaller* batches — the reason world-class manufacturers invest in quick changeovers rather than in bigger runs.

*(Full-marks tip: show that set-up cost = carrying cost at the EBQ as proof of optimality, and quantify the manager's proposal in rupees rather than asserting it is "wrong" — the reasoning in (c) about set-up reduction driving smaller batches is what separates a rank answer.)*

---

### Q40. Ch: Unit & Batch Costing — Batch cost sheet with rejections (Marks: 8) [Problem]
**Question:** Zenith Pharma manufactures in batches. For **Batch No. 45**, 2,400 units were put into process; 100 were rejected on inspection as *normal* spoilage with no realisable value; 2,300 good units were transferred. Prepare the batch cost statement, the cost per good unit, and the selling price if the firm marks up to earn **20% on selling price** after adding S&D cost of ₹5 per good unit.

| Particulars | ₹ |
|---|---:|
| Direct materials | 34,500 |
| Direct wages — Machining: 120 hrs @ ₹75 | 9,000 |
| Direct wages — Finishing: 80 hrs @ ₹60 | 4,800 |
| Production overheads | (150% of direct wages) |

**Solution:**

**WN-1 — Direct wages:** Machining 9,000 + Finishing 4,800 = **₹13,800**.
**WN-2 — Production OH:** 150% × 13,800 = **₹20,700**.
**WN-3 — Good units:** 2,400 − 100 normal rejects (nil value) = **2,300 units**.

**Batch Cost Statement — Batch No. 45**

| Particulars | ₹ |
|---|---:|
| Direct materials | 34,500 |
| Direct wages (WN-1) | 13,800 |
| **Prime Cost** | **48,300** |
| Production overheads (WN-2) | 20,700 |
| **Total Production Cost of batch** | **69,000** |
| Good units | 2,300 |
| **Production cost per good unit** (69,000 ÷ 2,300) | **30.00** |
| Add: S&D cost per good unit | 5.00 |
| **Total cost per good unit** | **35.00** |
| Add: Profit (20% on selling price = 1/4 of cost) | 8.75 |
| **Selling price per unit** | **43.75** |

Selling price = 35.00 ÷ 0.80 = **₹43.75**.

**Answer:** Total batch production cost ₹69,000; cost per good unit ₹30 (₹35 including S&D); selling price **₹43.75 per unit**.

**Why this way (the reasoning):** The whole batch's cost (₹69,000) is spread only over the **2,300 good units**, not the 2,400 started, because the 100 normally-rejected units are an unavoidable feature of the process — their cost is legitimately borne by the survivors. Dividing by 2,400 would understate unit cost and lead to under-pricing. Rejects with *no* realisable value simply drop out; had they fetched scrap value, that recovery would first be deducted from batch cost before dividing. The profit step repeats the "on selling price" logic: 20% of price means cost is 80% of price, so divide by 0.80 rather than multiply by 1.20.

*(Full-marks tip: divide by good units (2,300), not units introduced (2,400); absorbing normal spoilage into good output and pricing off selling-price (÷0.80) are the two judgement points that carry the marks.)*

---

### Q41. Ch: Unit & Batch Costing — EBQ sensitivity (Marks: 6) [Case/Application]
**Question:** The works manager of a company argues: *"Set-ups are expensive, so we should always produce in the largest possible batches — ideally one giant run per year."* Examine the validity of this view using the EBQ concept, and explain the effect on EBQ of (i) a rise in annual demand, (ii) a fall in set-up cost per run, and (iii) an increase in the interest rate used in carrying cost.

**Answer:** **Governing principle — EBQ.** The economic batch quantity is $EBQ=\sqrt{2DS/C}$, the batch size that *minimises the sum* of annual set-up cost and annual carrying cost. Both costs matter; the manager looks at only one.

**Applying it to the manager's claim.** A single giant run each year does minimise set-up cost, but average inventory then equals half of a year's demand, so *carrying cost* (warehousing, obsolescence, insurance and interest on the capital locked in stock) becomes enormous. The total cost curve is U-shaped: below EBQ, set-up cost dominates; above EBQ, carrying cost dominates. The manager's "biggest possible batch" sits far to the right of the minimum and is therefore **more** expensive, not less. The view is **invalid** — the objective is not to minimise set-ups but to minimise *total* cost.

**Sensitivity of EBQ:**
- **(i) Demand (D) rises →** EBQ rises, but only with $\sqrt{D}$: quadrupling demand only doubles the batch. Runs still increase.
- **(ii) Set-up cost (S) falls →** EBQ falls with $\sqrt{S}$: cheaper set-ups justify *smaller, more frequent* batches (the lean/JIT rationale).
- **(iii) Interest rate rises →** carrying cost C rises, so EBQ falls (EBQ varies with $1/\sqrt{C}$): dearer capital makes holding stock costlier, pushing toward smaller batches.

**Conclusion:** Batch size is a balancing act, not a maximisation. The manager should target the EBQ, and should note that the real route to fewer, cheaper set-ups *without* bloating inventory is to reduce set-up **cost/time**, which itself lowers the EBQ.

**Why this way (the reasoning):** The square-root structure is the key to genuine understanding: because every driver enters under a root, EBQ responds in a damped way and — crucially — moves in *opposite* directions for set-up cost (numerator) and carrying cost (denominator). Grasping that "make it bigger" only ever addresses the set-up half of a two-sided trade-off is what exposes the manager's error, and seeing that reducing set-up cost *shrinks* the optimal batch is the counter-intuitive result the examiner is probing.

*(Full-marks tip: explicitly state the U-shaped total-cost trade-off and give the direction of each sensitivity with its √ relationship; a purely verbal answer with no reference to the formula's structure caps at half marks.)*

---

### Q42. Ch: Unit & Batch Costing — Unit vs batch costing: choosing the method (Marks: 5) [Case/Application]
**Question:** A company runs two activities in the same plant: (A) it continuously produces a **single standard grade of packaged salt** in bulk, and (B) it makes **pharmaceutical tablets in identifiable lots of 50,000 strips**, each lot to a specific formulation and expiry batch number. The cost clerk records both under one "unit costing" system. Advise which costing method suits each activity and why, and identify the risk of using unit costing for activity (B).

**Answer:** **Principle.** The costing method must match the *cost object and the way output is produced*. **Unit (output/single) costing** suits a *continuous, homogeneous* output where cost per unit = total cost ÷ total units. **Batch costing** — a variant of job costing — suits production in *distinct, identifiable lots* where each batch is a cost unit, and cost per article = total batch cost ÷ good units in the batch.

**Application:**
- **Activity (A) — packaged salt:** output is continuous and identical, with no need to distinguish lots. **Unit costing is appropriate**: a simple cost sheet dividing period cost by units produced gives a reliable per-unit cost.
- **Activity (B) — tablet lots:** each lot has its own formulation, materials, set-up and — importantly — its own **batch/expiry number** for traceability and quality control. Costs must be *accumulated per lot*. This is textbook **batch costing**, and the EBQ question (optimal lot size balancing set-up vs carrying cost) also arises.

**Risk of forcing unit costing on (B):** Averaging all lots together hides the cost differences between formulations, prevents per-lot profitability and pricing, breaks the audit trail needed for regulatory recall/traceability, and ignores set-up cost — so lot sizes will not be optimised. **Advice:** keep unit costing for salt; adopt **batch costing** (with EBQ analysis) for the tablet lots.

**Why this way (the reasoning):** The deciding test is whether the units are *distinguishable and separately costed*. Salt units are interchangeable, so averaging is not just acceptable but efficient. Tablet lots are *not* interchangeable — each is a controlled batch — so collapsing them into one average destroys exactly the per-lot information the business (and the drug regulator) needs. The same physical plant can therefore legitimately host two different costing methods; matching method to cost object, not to the factory, is the principle being tested.

*(Full-marks tip: name both methods, tie batch costing to the *identifiable-lot* feature and the traceability need, and mention the set-up/EBQ dimension — a generic "batch costing is for batches" without the traceability and averaging-risk reasoning loses the application marks.)*

---

### Q43. Ch: Job & Contract Costing — Contract account with notional profit, WIP and profit to transfer (Marks: 10) [Problem]
**Question:** Meridian Constructions began Contract No. 7 (price **₹60,00,000**) during the year. Prepare the Contract Account, compute the notional profit, decide the profit to be credited to the Profit & Loss Account, and show how the work-in-progress will appear in the Balance Sheet. Work certified is **₹36,00,000** and cash received is **80% of work certified**.

| Particulars | ₹ |
|---|---:|
| Materials issued to site | 14,00,000 |
| Materials returned to stores | 40,000 |
| Materials at site (closing) | 1,20,000 |
| Direct wages paid | 10,00,000 |
| Outstanding wages | 60,000 |
| Direct expenses paid | 1,50,000 |
| Outstanding direct expenses | 20,000 |
| Plant issued to site (cost) | 5,00,000 |
| Plant at site (revalued, closing) | 4,00,000 |
| Site establishment overheads | 2,00,000 |
| Work uncertified (cost) | 1,80,000 |

**Solution:**

**WN-1 — Charges to the account:** wages 10,00,000 + outstanding 60,000 = 10,60,000; direct expenses 1,50,000 + outstanding 20,000 = 1,70,000. Plant depreciation is captured automatically by carrying the plant down at its revalued ₹4,00,000 (i.e. ₹1,00,000 consumed).

**Contract No. 7 Account**

| Dr — Particulars | ₹ | Cr — Particulars | ₹ |
|---|---:|---|---:|
| To Materials issued | 14,00,000 | By Materials returned to stores | 40,000 |
| To Wages (10,00,000 + 60,000 o/s) | 10,60,000 | By Materials at site c/d | 1,20,000 |
| To Direct expenses (1,50,000 + 20,000 o/s) | 1,70,000 | By Plant at site c/d (revalued) | 4,00,000 |
| To Plant issued to site | 5,00,000 | By Work-in-progress c/d: | |
| To Site establishment overheads | 2,00,000 |   Work certified 36,00,000 | |
| To Notional profit c/d (bal. fig.) | 10,10,000 |   Work uncertified 1,80,000 = | 37,80,000 |
| **Total** | **43,40,000** | **Total** | **43,40,000** |

**WN-2 — Degree of completion:** Work certified ÷ Contract price = 36,00,000 ÷ 60,00,000 = **60%** (falls in the 50%–90% band).

**WN-3 — Cash received & ratio:** Cash = 80% × 36,00,000 = ₹28,80,000; cash/certified ratio = **0.80**.

**WN-4 — Profit to transfer to P&L:**
$$\text{Profit}= \tfrac{2}{3}\times \text{Notional profit}\times \frac{\text{Cash received}}{\text{Work certified}}=\tfrac{2}{3}\times 10,10,000\times 0.80 = \mathbf{₹5,38,667}$$
Reserve (profit held back) = 10,10,000 − 5,38,667 = **₹4,71,333**.

**WN-5 — Balance Sheet presentation of WIP:**

| Particulars | ₹ |
|---|---:|
| Work certified + Work uncertified | 37,80,000 |
| Less: Reserve (profit not transferred) | (4,71,333) |
| Less: Cash received from contractee | (28,80,000) |
| **Net WIP shown under current assets** | **4,28,667** |

**Answer:** Notional profit ₹10,10,000; profit credited to P&L ₹5,38,667; reserve ₹4,71,333; net WIP in Balance Sheet ₹4,28,667.

**Why this way (the reasoning):** A contract spans years, so recognising the *whole* notional profit now would breach prudence — the unbilled and unfinished work could still go wrong. Hence only a fraction is taken. The **2/3 factor** applies because completion is in the 50%–90% band (well advanced but not near finished); the **cash-received ratio** further scales the profit down to reflect that money not yet collected (the 20% retention) is not yet certain. Multiplying the two builds in a double margin of safety. Outstanding wages and expenses are added because cost must be on an *accrual* basis — the work consumed those resources even if unpaid. Plant is not charged at full cost; only the depreciation (cost ₹5,00,000 less revalued ₹4,00,000) is a cost of the contract, so the plant is carried down at ₹4,00,000. The trap is deducting cash received *and* the reserve *and* forgetting one of them in the WIP figure, or applying 1/3 instead of 2/3 for the completion band.

*(Full-marks tip: pick the correct completion band multiplier (2/3 for 50–90%), always multiply by the cash ratio, and present the WIP net of *both* reserve and cash — dropping either is the standard 2-mark deduction.)*

---

### Q44. Ch: Job & Contract Costing — Escalation clause claim (Marks: 8) [Problem]
**Question:** Apex Infra secured a contract of **₹1,50,00,000** containing an escalation clause: *if the price of any material or the wage rate rises by more than 5% over the rates on which the tender was based, the contractee will reimburse the contractor for the increase over and above that 5%*. Compute the amount of the escalation claim from the data below, and state the treatment of the extra material actually consumed.

| Item | Standard qty (per tender) | Standard rate | Actual rate | Actual qty used |
|---|---:|---:|---:|---:|
| Material X | 20,000 units | ₹200 | ₹240 | 21,000 units |
| Material Y | 15,000 kg | ₹100 | ₹106 | 15,000 kg |
| Labour | 30,000 hrs | ₹150 | ₹172.50 | 30,000 hrs |

**Solution:**

**WN-1 — Rate allowed before reimbursement (standard + 5%):** X: 200 × 1.05 = ₹210; Y: 100 × 1.05 = ₹105; Labour: 150 × 1.05 = ₹157.50.

**WN-2 — Reimbursable excess per unit (actual rate − 5%-allowed rate):** X: 240 − 210 = ₹30; Y: 106 − 105 = ₹1; Labour: 172.50 − 157.50 = ₹15.

**Statement of Escalation Claim**

| Item | Standard qty | Reimbursable excess rate ₹ | Claim ₹ |
|---|---:|---:|---:|
| Material X | 20,000 | 30 | 6,00,000 |
| Material Y | 15,000 | 1 | 15,000 |
| Labour | 30,000 | 15 | 4,50,000 |
| **Total escalation claim** | | | **10,65,000** |

**Treatment of extra material X:** The claim uses the **standard/agreed quantity (20,000)**, not the 21,000 actually used. The extra **1,000 units of X** consumed is due to the contractor's own usage/inefficiency; its cost (1,000 × ₹240 = ₹2,40,000) is **borne by the contractor** and is *not* claimable.

**Answer:** Escalation claim recoverable from the contractee = **₹10,65,000**. The cost of the extra 1,000 units of Material X is the contractor's own loss.

**Why this way (the reasoning):** An escalation clause protects the contractor against **price movements outside his control**, not against his own inefficiency in *using* more input. So reimbursement is computed as *agreed quantity × price increase*, deliberately quarantining the quantity variance. Two twists carry the marks: (1) reimbursement is only the increase **above the 5% cushion** — you first lift the standard rate by 5% and claim only the excess over that, otherwise you over-claim; and (2) applying the price rise to the *actual* 21,000 units of X would wrongly pass the contractor's excess-usage cost to the client. Material Y shows why the 5% test matters — its 6% rise yields only a token ₹1 claimable, because 5% is absorbed by the contractor.

*(Full-marks tip: lift the base rate by 5% *before* taking the excess, and use standard quantity — claiming on actual quantity or on the full price rise (ignoring the 5% cushion) are the two errors that cost the most marks.)*

---

### Q45. Ch: Job & Contract Costing — Profit to transfer across completion stages (Marks: 6) [Problem]
**Question:** For a contract in progress, the notional profit to date is **₹6,00,000** and cash received is **75% of work certified**. Compute the profit to be transferred to the Profit & Loss Account if the work certified represents **45%** of the contract price, and separately if it represents **70%**. Explain the difference.

**Solution:**

**WN-1 — Cash/certified ratio:** 0.75 in both cases.

**WN-2 — Applicable rule by degree of completion:**

| Stage of completion | Rule for profit to P&L |
|---|---|
| Below 25% | Nil (too early — no reliable profit) |
| 25% to below 50% | 1/3 × Notional profit × (Cash ÷ Certified) |
| 50% to below 90% | 2/3 × Notional profit × (Cash ÷ Certified) |
| 90% and above | Estimated-total-profit method |

**Case (a) — 45% complete (25%–50% band):**
$$\tfrac{1}{3}\times 6,00,000\times 0.75 = \mathbf{₹1,50,000}\quad(\text{Reserve }₹4,50,000)$$

**Case (b) — 70% complete (50%–90% band):**
$$\tfrac{2}{3}\times 6,00,000\times 0.75 = \mathbf{₹3,00,000}\quad(\text{Reserve }₹3,00,000)$$

**Answer:** Profit to P&L = **₹1,50,000** at 45% completion and **₹3,00,000** at 70% completion, on the *same* notional profit.

**Why this way (the reasoning):** The recognisable fraction of notional profit **rises with completion** (1/3 → 2/3) because the further a contract has progressed, the more reliable its profit estimate and the smaller the chance of a late reversal — so prudence relaxes. In *both* stages the profit is additionally scaled by the cash-received ratio, because profit tied up in uncollected retention money is not yet secure. The reserve is simply the un-recognised balance, held back as a cushion against future losses on the remaining work. The message: identical notional profit produces very different recognised profit depending purely on how far the job has advanced — recognition is governed by *certainty*, not by cash earned.

*(Full-marks tip: state the band *and* the multiplier before computing; a candidate who applies 2/3 to a sub-50% contract, or omits the cash ratio, forfeits the concept marks even with correct arithmetic.)*

---

### Q46. Ch: Job & Contract Costing — Notional profit, WIP and retention (Marks: 5) [Case/Application]
**Question:** A contractor whose contract is 60% complete argues: *"I have earned a notional profit of ₹20 lakh this year, so I will credit the whole ₹20 lakh to my Profit & Loss Account."* Examine the validity of this treatment. In doing so, explain the concepts of **notional profit**, **work-in-progress**, and **retention money**, and why the profit actually taken is deliberately restricted.

**Answer:** **Principle — prudence in long-term contracts.** For contracts spanning more than one period, profit is recognised progressively, but conservatively, so that no profit is taken that a future loss might reverse.

- **Notional profit** = value of work certified + work uncertified − cost of work done to date. It is *notional* precisely because the contract is unfinished: it is an *estimate* of profit earned so far, not a realised result.
- **Work-in-progress (WIP)** = the cost of work certified plus work uncertified, carried forward as an asset (shown net of the reserve and of cash received). It represents effort that has been performed but not yet fully billed/settled.
- **Retention money** = the portion of certified value (here typically 10%–20%) the contractee withholds until the defect-liability period expires, as security for quality. It is *earned but not yet collectible*.

**Examining the contractor's claim:** Crediting the **entire** ₹20 lakh is **invalid**. Two safeguards are ignored: (1) at 60% completion the contract is well advanced but not near-complete, so only **2/3** of the notional profit is eligible; and (2) the eligible figure is further reduced by the **cash-received ratio**, because retention money is uncollected and at risk. The balance is kept as a **reserve** against possible cost over-runs or penalties on the remaining 40%.

**Conclusion:** He may credit only $\tfrac{2}{3}\times 20{,}00{,}000\times\frac{\text{cash}}{\text{certified}}$, transferring the rest to reserve. Recognising all ₹20 lakh overstates current profit and breaches prudence.

**Why this way (the reasoning):** The entire architecture exists because a contract's outcome is uncertain until it ends — early over-optimism would let a contractor distribute profit that a later loss then claws back. The 2/3 factor and the cash ratio together translate two distinct uncertainties (work not yet finished; money not yet received) into a single conservative figure. Retention money is the sharpest illustration: it is genuinely *earned* revenue, yet withholding it in the profit calculation reflects that it is not *secure* until quality is proven. Prudence, not cash, drives recognition.

*(Full-marks tip: define all three terms *and* tie the restriction to prudence plus the two uncertainties; simply saying "take 2/3" without explaining retention money and the reserve rationale caps the answer.)*

---

### Q47. Ch: Job & Contract Costing — Estimated total profit method (near completion) (Marks: 10) [Problem]
**Question:** Contract No. 12 (price **₹80,00,000**) is nearly complete. Cost incurred to date is **₹58,00,000**; estimated further cost to complete is **₹6,00,000**. Work certified is **₹74,00,000** and cash received is **90% of work certified**. Because the contract is more than 90% complete, compute the profit to be credited to the Profit & Loss Account under the **estimated-total-profit** method using **all four** recognised formulae, and advise which is most prudent.

**Solution:**

**WN-1 — Degree of completion:** 74,00,000 ÷ 80,00,000 = **92.5%** (≥90% → estimated-profit method applies).
**WN-2 — Estimated total cost:** 58,00,000 + 6,00,000 = **₹64,00,000**.
**WN-3 — Estimated total profit (ETP):** 80,00,000 − 64,00,000 = **₹16,00,000**.
**WN-4 — Ratios:** Cost to date ÷ estimated total cost = 58 ÷ 64 = 0.90625; Work certified ÷ contract price = 74 ÷ 80 = 0.925; Cash ÷ certified = 0.90.

**Statement of Profit to be credited — four formulae**

| # | Formula | Computation | Profit to P&L ₹ |
|---|---|---|---:|
| (i) | ETP × (Cost to date ÷ Est. total cost) | 16,00,000 × 58/64 | 14,50,000 |
| (ii) | ETP × (Cost to date ÷ Est. total cost) × (Cash ÷ Certified) | 14,50,000 × 0.90 | 13,05,000 |
| (iii) | ETP × (Work certified ÷ Contract price) | 16,00,000 × 74/80 | 14,80,000 |
| (iv) | ETP × (Work certified ÷ Contract price) × (Cash ÷ Certified) | 14,80,000 × 0.90 | 13,32,000 |

**Advice:** The most prudent figure is **formula (ii) — ₹13,05,000**, because it scales the estimated profit by *both* the proportion of total cost incurred **and** the cash actually collected, giving the lowest, most conservative recognition. Formula (iv) (₹13,32,000) is the common alternative when certified value is preferred as the completion measure.

**Answer:** Estimated total profit ₹16,00,000; profit credited to P&L on the most prudent basis (formula ii) = **₹13,05,000**.

**Why this way (the reasoning):** Once a contract passes ~90% completion, the *whole* outcome can be estimated reliably, so the 1/3–2/3 "band" method is abandoned in favour of recognising a share of the **estimated total profit**. The four formulae differ only in *which completion measure* they trust (cost-based vs certified-value based) and *whether* they further discount for uncollected cash. The cost-based ratio (i)/(ii) is usually preferred over the certified-value ratio because certified value can be inflated by front-loaded billing, whereas cost incurred is harder to distort. Adding the cash ratio then quarantines the retention still outstanding. The examiner wants to see that you (a) recognised the ≥90% trigger to switch methods and (b) understand that the "most prudent" choice is the one embedding the *most* safety factors — hence formula (ii).

*(Full-marks tip: identify the ≥90% trigger explicitly, show all four formulae, and justify the recommended one on *prudence* grounds; jumping straight to one formula without recognising why the band method no longer applies loses method marks.)*

---

### Q48. Ch: Job & Contract Costing — Job cost sheet, departmental absorption and pricing (Marks: 8) [Problem]
**Question:** Prepare the cost sheet for **Job No. 202**, quote a price to earn **20% on selling price**, and then advise on the customer's counter-offer of a fixed **₹50,000**.

| Element | Data |
|---|---|
| Direct materials | ₹18,000 |
| Direct labour — Dept X | 40 hrs @ ₹120 |
| Direct labour — Dept Y | 25 hrs @ ₹100 |
| Overheads — Dept X | Machine-hour rate ₹200; 30 machine hrs |
| Overheads — Dept Y | Labour-hour rate ₹160; 25 labour hrs |
| Admin & S&D overheads | 20% of works cost |

**Solution:**

**WN-1 — Direct labour:** Dept X 40 × 120 = 4,800; Dept Y 25 × 100 = 2,500 → **₹7,300**.
**WN-2 — Overheads absorbed:** Dept X 30 × 200 = 6,000 (machine-hour basis); Dept Y 25 × 160 = 4,000 (labour-hour basis) → **₹10,000**.

**Cost Sheet — Job No. 202**

| Particulars | ₹ |
|---|---:|
| Direct materials | 18,000 |
| Direct labour (WN-1) | 7,300 |
| **Prime Cost** | **25,300** |
| Overheads absorbed (WN-2) | 10,000 |
| **Works Cost** | **35,300** |
| Admin & S&D OH (20% of works cost) | 7,060 |
| **Total Cost** | **42,360** |
| Profit (20% on selling price = 1/4 of cost) | 10,590 |
| **Quoted Selling Price** | **52,950** |

Quoted price = 42,360 ÷ 0.80 = **₹52,950**.

**WN-3 — Evaluation of ₹50,000 counter-offer:** Profit = 50,000 − 42,360 = **₹7,640**; margin = 7,640 ÷ 50,000 = **15.28% on price** (still above cost).

**Advice:** ₹50,000 still yields a positive profit of ₹7,640 (15.28% on price), though below the 20% target. If the plant has spare capacity and no better order is available, **accept** — it covers full cost and contributes ₹7,640; hold firm nearer ₹52,950 only if capacity is scarce or other work is queued.

**Answer:** Total job cost ₹42,360; quoted price ₹52,950; at ₹50,000 the job still earns ₹7,640 (15.28%).

**Why this way (the reasoning):** Job costing accumulates cost against a *specific order*, and each department's overhead is absorbed on the base that best reflects how *it* incurs cost — Dept X is machine-intensive (machine-hour rate), Dept Y is labour-intensive (labour-hour rate). Using one blanket rate for both would misprice the job. The counter-offer question tests decision-making: because ₹50,000 exceeds full cost, it is not a loss — the "reject anything below the quoted price" reflex is wrong. The right lens is opportunity cost of capacity: accept marginal-but-profitable work when capacity is idle, defend the target margin when it is not.

*(Full-marks tip: use the *departmentally correct* absorption base for each department and evaluate the counter-offer against *full cost* — dismissing ₹50,000 merely because it is below the quote, without noting it still profits, loses the application marks.)*

---

### Q49. Ch: Job & Contract Costing — Retention money and Balance-Sheet WIP (Marks: 6) [Problem]
**Question:** On Contract No. 9, the value of **work certified is ₹45,00,000** and the contractee retains **15% as retention money**, paying the rest. Work uncertified (at cost) is ₹90,000 and the reserve for unrecognised profit is ₹3,60,000. Compute the cash received and the retention money, and show the work-in-progress figure that will appear under current assets in the Balance Sheet.

**Solution:**

**WN-1 — Retention money:** 15% × 45,00,000 = **₹6,75,000**.
**WN-2 — Cash received:** 85% × 45,00,000 = **₹38,25,000**.

**Balance-Sheet extract — Work-in-progress (current assets)**

| Particulars | ₹ |
|---|---:|
| Work certified | 45,00,000 |
| Add: Work uncertified (at cost) | 90,000 |
| Gross work-in-progress | 45,90,000 |
| Less: Reserve (unrecognised profit) | (3,60,000) |
| Less: Cash received from contractee | (38,25,000) |
| **Net WIP shown under current assets** | **4,05,000** |

**Check:** Net WIP ₹4,05,000 = retention money ₹6,75,000 + work uncertified ₹90,000 − reserve ₹3,60,000 = ₹4,05,000. ✔

**Answer:** Retention money ₹6,75,000; cash received ₹38,25,000; net WIP under current assets = **₹4,05,000**.

**Why this way (the reasoning):** The Balance Sheet must show only the *net* amount still tied up in the contract, so from gross WIP you subtract two things: the **cash already received** (that value is no longer an asset in WIP — it is in the bank) and the **reserve** (profit not yet recognised must not inflate the asset). What remains — economically the *retention money still due* plus the *uncertified work* less the *profit reserve* — is exactly the residual the contractor is owed but has not collected, confirmed by the reconciliation check. The classic error is subtracting cash but forgetting the reserve, which overstates the asset by the very profit prudence told us not to recognise.

*(Full-marks tip: deduct *both* cash received and the reserve, and show the retention/uncertified reconciliation as a self-check — that check is often worth an easy mark and catches the "forgot-the-reserve" error.)*

---

### Q50. Ch: Job & Contract Costing — Job costing with under-absorbed overhead (Marks: 8) [Problem]
**Question:** Halcyon Engineering absorbs factory overhead on a pre-determined **machine-hour rate**. Budgeted overhead was **₹8,00,000** for **40,000 machine hours**. Actual overhead for the year was **₹9,00,000** for **42,000 machine hours**. **Job No. 88** used direct materials ₹15,000, direct wages ₹8,000 and **500 machine hours**. Compute (a) the pre-determined rate, (b) the under/over-absorption, (c) the factory cost of Job 88 as originally charged, and (d) the revised factory cost if the under-absorption (assumed to arise from a general rise in overhead prices) is recovered by a supplementary rate.

**Solution:**

**WN-1 — Pre-determined rate:** 8,00,000 ÷ 40,000 = **₹20 per machine hour**.
**WN-2 — Overhead absorbed (year):** 42,000 × 20 = ₹8,40,000. Actual = ₹9,00,000.
**Under-absorption** = 9,00,000 − 8,40,000 = **₹60,000** (absorbed < actual).
**WN-3 — Supplementary rate:** 60,000 ÷ 42,000 machine hours = **₹1.4286 per machine hour**.

**(c) Factory cost of Job 88 as originally charged**

| Particulars | ₹ |
|---|---:|
| Direct materials | 15,000 |
| Direct wages | 8,000 |
| Overhead absorbed (500 × ₹20) | 10,000 |
| **Factory cost (as charged)** | **33,000** |

**(d) Revised factory cost using supplementary rate:** Additional overhead on Job 88 = 500 × 1.4286 = **₹714**. Revised factory cost = 33,000 + 714 = **₹33,714**.

**Answer:** Pre-determined rate ₹20/hr; under-absorbed overhead ₹60,000; Job 88 factory cost ₹33,000, revised to **₹33,714** after the supplementary rate.

**Why this way (the reasoning):** A pre-determined rate is struck *before* the year so jobs can be costed and priced as they arise, without waiting for actual overheads. At year-end actual and absorbed almost always differ. The *cause* of the difference dictates its treatment: because here the under-absorption stems from a **general price rise (a normal cause) and is material**, it is fair to spread it back onto the jobs via a **supplementary rate**, restoring each job to something close to actual cost. Had the ₹60,000 arisen from **abnormal** reasons — idle time, a strike, gross inefficiency — it would instead be **written off to the Costing P&L**, because distorting product cost with abnormal events destroys comparability. Job 88 therefore carries only its ₹714 share, not the whole ₹60,000.

*(Full-marks tip: link the *treatment* to the *cause* — supplementary rate for normal/material amounts, write-off to Costing P&L for abnormal — and apply the supplementary rate to the job's own hours, not the whole under-absorption.)*

---

### Q51. Ch: Job & Contract Costing — Contract account with escalation and profit transfer (integrated) (Marks: 8) [Problem]
**Question:** Contract No. 15 (price **₹50,00,000**) contains an escalation clause, and a claim of **₹1,20,000** has been admitted by the contractee but not yet received. From the data below, compute the notional profit (treating the admitted escalation claim as additional recoverable value) and the profit to be transferred to the Profit & Loss Account. Work certified is **55%** of the contract price and cash received is **80% of work certified**.

| Particulars | ₹ |
|---|---:|
| Materials consumed | 12,00,000 |
| Direct wages | 8,00,000 |
| Direct expenses | 2,00,000 |
| Plant depreciation charged | 1,00,000 |
| Site overheads | 1,50,000 |
| Work uncertified (at cost) | 1,00,000 |

**Solution:**

**WN-1 — Cost of work to date (Dr side):** 12,00,000 + 8,00,000 + 2,00,000 + 1,00,000 + 1,50,000 = **₹24,50,000**.
**WN-2 — Value recoverable (Cr side):** Work certified = 55% × 50,00,000 = 27,50,000; + work uncertified 1,00,000; + escalation claim admitted 1,20,000 = **₹29,70,000**.
**WN-3 — Notional profit:** 29,70,000 − 24,50,000 = **₹5,20,000**.
**WN-4 — Degree of completion:** 55% → **50%–90% band → 2/3 rule.**
**WN-5 — Cash & ratio:** Cash = 80% × 27,50,000 = ₹22,00,000; cash/certified = **0.80** (escalation claim not yet received, so excluded from cash).

**Profit to transfer to P&L:**
$$\tfrac{2}{3}\times 5,20,000\times 0.80 = \mathbf{₹2,77,333}\quad(\text{Reserve }5,20,000-2,77,333=₹2,42,667)$$

**Contract No. 15 — summary**

| Particulars | ₹ |
|---|---:|
| Total cost to date | 24,50,000 |
| Work certified + uncertified + escalation claim | 29,70,000 |
| **Notional profit** | **5,20,000** |
| Profit transferred to P&L (2/3 × NP × cash ratio) | 2,77,333 |
| Reserve carried forward | 2,42,667 |

**Answer:** Notional profit ₹5,20,000; profit credited to P&L ₹2,77,333; reserve ₹2,42,667.

**Why this way (the reasoning):** The admitted escalation claim is *earned additional contract revenue* — the contractee has accepted liability — so it legitimately increases the value side and hence the notional profit; ignoring it would understate the profit the contractor has genuinely earned. But because that ₹1,20,000 has **not been collected**, it is kept **out of the cash figure**, so the cash-to-certified ratio stays at 0.80 and the prudence discount still bites on the uncollected amount. The completion band (55%) fixes the 2/3 multiplier. The elegance here is seeing that escalation and profit-recognition interact: the claim lifts profit *earned*, while the cash ratio simultaneously restrains how much of that profit is *recognised* until the money arrives.

*(Full-marks tip: add the admitted escalation claim to the value side (it raises notional profit) but keep it out of cash received (it is uncollected) — students who either omit the claim entirely or wrongly add it to cash both misstate the transfer.)*

### Q52. Ch: Process & Operation Costing — Equivalent Units (FIFO) with Normal & Abnormal Loss (Marks: 10) [Problem]
**Question:** In Process-A the following data relates to a month. Inspection is carried out at the END of the process, so all loss units are 100% complete for every cost element. Normal loss is 10% of units introduced during the month and scrap realises ₹10 per unit. Prepare, under the **FIFO method**, (i) the Statement of Equivalent Production, (ii) cost per equivalent unit, (iii) the Statement of Evaluation, and (iv) the Process-A Account.

| Particulars | Units | Materials | Labour | Overhead |
|---|---|---|---|---|
| Opening WIP | 2,000 | 100% | 60% | 60% |
| Units introduced | 18,000 | — | — | — |
| Completed & transferred | 15,000 | — | — | — |
| Closing WIP | 3,000 | 100% | 40% | 40% |
| Opening WIP value (₹) | — | 43,000 | 10,000 | 8,000 |
| Current cost (₹) | — | 3,42,000 | 1,52,000 | 1,21,600 |

**Solution:**

**WN-1 — Physical reconciliation.** Input = 2,000 + 18,000 = 20,000. Output = 15,000 + closing 3,000 = 18,000. Total loss = 20,000 − 18,000 = **2,000 units**. Normal loss = 10% × 18,000 introduced = **1,800**; Abnormal loss = 2,000 − 1,800 = **200 units**.

**WN-2 — Statement of Equivalent Production (FIFO).** FIFO first *completes* opening WIP, then starts-and-completes fresh units. Normal loss gets NIL equivalent units (its cost is absorbed by good units); abnormal loss is a real cost carrier and gets full equivalent units.

| Particulars | Units | Materials EU | Labour EU | Overhead EU |
|---|---|---|---|---|
| Opening WIP completed | 2,000 | 0 (0%) | 800 (40%) | 800 (40%) |
| Introduced & completed (15,000−2,000) | 13,000 | 13,000 | 13,000 | 13,000 |
| Normal loss | 1,800 | — | — | — |
| Abnormal loss | 200 | 200 | 200 | 200 |
| Closing WIP | 3,000 | 3,000 (100%) | 1,200 (40%) | 1,200 (40%) |
| **Equivalent units** | | **16,200** | **15,200** | **15,200** |

**WN-3 — Cost per equivalent unit (current cost only; normal-loss scrap deducted from material).** Scrap of normal loss = 1,800 × ₹10 = ₹18,000.

- Materials = (3,42,000 − 18,000) ÷ 16,200 = 3,24,000 ÷ 16,200 = **₹20**
- Labour = 1,52,000 ÷ 15,200 = **₹10**
- Overhead = 1,21,600 ÷ 15,200 = **₹8**
- **Cost per completed unit (current) = ₹38**

**WN-4 — Statement of Evaluation.**

| Item | Computation | ₹ |
|---|---|---|
| Opening WIP: cost b/f | 43,000+10,000+8,000 | 61,000 |
| Opening WIP: to complete | (800×10)+(800×8) | 14,400 |
| Started & completed | 13,000 × 38 | 4,94,000 |
| **Transferred (15,000 u)** | 61,000+14,400+4,94,000 | **5,69,400** |
| Closing WIP | (3,000×20)+(1,200×10)+(1,200×8) | 81,600 |
| Abnormal loss | 200 × 38 | 7,600 |

**Process-A Account**

| Dr | Units | ₹ | Cr | Units | ₹ |
|---|---|---|---|---|---|
| Opening WIP | 2,000 | 61,000 | Normal loss (scrap) | 1,800 | 18,000 |
| Materials | 18,000 | 3,42,000 | Abnormal loss | 200 | 7,600 |
| Labour | — | 1,52,000 | Transfer to Process-B | 15,000 | 5,69,400 |
| Overhead | — | 1,21,600 | Closing WIP | 3,000 | 81,600 |
| **Total** | **20,000** | **6,76,600** | **Total** | **20,000** | **6,76,600** |

**Answer:** Transfer to next process **15,000 units @ ₹5,69,400**; Closing WIP **₹81,600**; Abnormal loss **200 units @ ₹7,600**; Normal-loss scrap **₹18,000**.

**Why this way (the reasoning):** FIFO keeps the *old* work (opening WIP) and the *new* work separate, so the cost/EU is built **only from the current month's cost** — the fairest measure of *this period's* efficiency and price. That is why opening WIP contributes only its *unfinished* fraction (40% of labour/overhead) to equivalent units, and its brought-forward value is simply added back at the end rather than blended in. Normal loss earns **no equivalent units** because it is an expected, unavoidable shrinkage: charging it cost would then re-allocate that cost to the survivors anyway, so we short-circuit the arithmetic by dividing the (net-of-scrap) cost only among good/abnormal units — this automatically loads the normal-loss cost onto the good output. Its scrap value is netted off *material* cost because that is the recoverable element. Abnormal loss, by contrast, is a controllable failure, so it must **carry full cost** (200 × ₹38) and be written to Costing P&L — hiding it inside product cost would conceal inefficiency. The tempting error of giving normal loss equivalent units *and* then apportioning double-counts it.

*(Full-marks tip: examiners reward (a) deducting normal-loss scrap from the material cost pool before computing the rate, (b) showing opening-WIP only for the balance % under FIFO, and (c) a Process A/c that reconciles to the paise. Common deductions: blending opening value into the rate (that is weighted-average, not FIFO), and giving normal loss equivalent units.)*

---

### Q53. Ch: Process & Operation Costing — Equivalent Units (Weighted Average) with Loss (Marks: 8) [Problem]
**Question:** Process-P uses the **weighted-average method**. Normal loss is 5% of units introduced, scrap ₹10/unit; inspection is at the end (loss 100% complete). Prepare the Statement of Equivalent Production, cost per EU and evaluation of transfer, closing WIP and abnormal loss.

| Particulars | Units | Materials | Lab & OH |
|---|---|---|---|
| Opening WIP | 1,000 | 100% | — |
| Introduced | 9,000 | — | — |
| Completed & transferred | 8,000 | — | — |
| Closing WIP | 1,500 | 100% | 60% |
| Opening WIP value (₹) | — | Mat 8,450; Lab 4,750; OH 3,800 | |
| Current cost (₹) | — | Mat 82,000; Lab 40,000; OH 32,000 | |

**Solution:**

**WN-1 — Physical flow.** Input = 10,000. Output 8,000 + closing 1,500 = 9,500. Total loss = 500. Normal loss = 5% × 9,000 = **450**; Abnormal loss = **50**.

**WN-2 — Equivalent Production (weighted average).** WA makes **no** distinction between opening and current work, so completed units are always 100% and the opening degree of completion is irrelevant.

| Particulars | Units | Materials EU | Labour EU | Overhead EU |
|---|---|---|---|---|
| Completed | 8,000 | 8,000 | 8,000 | 8,000 |
| Normal loss | 450 | — | — | — |
| Abnormal loss | 50 | 50 | 50 | 50 |
| Closing WIP | 1,500 | 1,500 | 900 (60%) | 900 (60%) |
| **Equivalent units** | | **9,550** | **8,950** | **8,950** |

**WN-3 — Cost per EU (opening + current, less normal-loss scrap on material).** Scrap = 450 × ₹10 = ₹4,500.

- Materials = (8,450 + 82,000 − 4,500) ÷ 9,550 = 85,950 ÷ 9,550 = **₹9**
- Labour = (4,750 + 40,000) ÷ 8,950 = 44,750 ÷ 8,950 = **₹5**
- Overhead = (3,800 + 32,000) ÷ 8,950 = 35,800 ÷ 8,950 = **₹4**
- **Cost per completed unit = ₹18**

**WN-4 — Evaluation.**

| Item | Computation | ₹ |
|---|---|---|
| Transferred (8,000) | 8,000 × 18 | 1,44,000 |
| Closing WIP | (1,500×9)+(900×5)+(900×4) | 21,600 |
| Abnormal loss | 50 × 18 | 900 |
| Normal-loss scrap | 450 × 10 | 4,500 |

**Reconciliation:** Inputs = opening 17,000 + current 1,54,000 = ₹1,71,000 = 1,44,000 + 21,600 + 900 + 4,500. ✓

**Answer:** Transfer **8,000 u @ ₹1,44,000**; Closing WIP **₹21,600**; Abnormal loss **50 u @ ₹900**.

**Why this way (the reasoning):** Weighted average pools *all* cost (brought-forward + current) and *all* work (opening + fresh) into one average, so opening WIP's stage of completion never appears in the EU statement — that is the single biggest conceptual difference from FIFO. The method is appropriate when input prices are stable or when the firm does not need to isolate current-period performance; it is simpler because there is no "opening WIP to complete" line. Normal-loss scrap is again netted from the material cost pool and the loss carries no EU, so its cost self-loads onto good units. If you had used FIFO here you would get a *different* material rate, because FIFO excludes the ₹8,450 cheap opening material from the numerator — the choice of method is therefore an accounting-policy decision that directly changes reported stock values.

*(Full-marks tip: state clearly "opening WIP % ignored under WA" and net scrap before dividing. Deductions arise from carrying opening-WIP completion % into the WA statement, or forgetting that abnormal loss (50) is 100% complete.)*

---

### Q54. Ch: Process & Operation Costing — Abnormal Gain with Scrap Adjustment (Marks: 8) [Problem]
**Question:** Process-2 introduced 10,000 units at a total cost (material ₹1,50,000 + labour ₹90,000 + overhead ₹45,000). Normal loss is 10% of input and scrap realises ₹15 per unit. Actual output was **9,300 units**. Prepare the Process-2 Account, the Normal Loss Account and the Abnormal Gain Account, and state the amount finally transferred to Costing P&L.

**Solution:**

**WN-1 — Normal vs actual.** Normal loss = 10% × 10,000 = 1,000 → expected output 9,000. Actual output 9,300 > 9,000, so **Abnormal GAIN = 300 units**.

**WN-2 — Cost per (good) unit.** Loss/gain are valued at the normal cost per good unit:
Cost/unit = (Total cost − scrap value of *normal* loss) ÷ (Input − normal loss units)
= (2,85,000 − 1,000×15) ÷ (10,000 − 1,000) = 2,70,000 ÷ 9,000 = **₹30**.

**WN-3 — Abnormal gain valuation.** Abnormal gain = 300 × ₹30 = **₹9,000** (debited to Process, credited to Abnormal Gain A/c).

**Process-2 Account**

| Dr | Units | ₹ | Cr | Units | ₹ |
|---|---|---|---|---|---|
| Materials | 10,000 | 1,50,000 | Normal loss (scrap) | 1,000 | 15,000 |
| Labour | — | 90,000 | Transfer out (output) | 9,300 | 2,79,000 |
| Overhead | — | 45,000 | | | |
| Abnormal gain | 300 | 9,000 | | | |
| **Total** | **10,300** | **2,94,000** | **Total** | **10,300** | **2,94,000** |

**Normal Loss Account**

| Dr | Units | ₹ | Cr | Units | ₹ |
|---|---|---|---|---|---|
| Process-2 | 1,000 | 15,000 | Cash (700 × 15) | 700 | 10,500 |
| | | | Abnormal Gain A/c | 300 | 4,500 |
| **Total** | **1,000** | **15,000** | **Total** | **1,000** | **15,000** |

**Abnormal Gain Account**

| Dr | ₹ | Cr | ₹ |
|---|---|---|---|
| Normal Loss A/c (300×15) | 4,500 | Process-2 A/c | 9,000 |
| Costing P&L (bal.) | 4,500 | | |
| **Total** | **9,000** | **Total** | **9,000** |

**Answer:** Net credit to Costing P&L from abnormal gain = **₹4,500**.

**Why this way (the reasoning):** Abnormal gain arises because *actual* loss (700) fell short of the *expected* normal loss (1,000) — the process performed better than the standard allows. It is the mirror image of abnormal loss and must be valued at the **same normal cost per good unit (₹30)** so that the Process A/c is not distorted by the firm's good luck/efficiency. The subtle trap is scrap: because only 700 units were actually lost, only 700 units' worth of scrap (₹10,500) is realised in cash. The normal-loss account was *credited* with 1,000 units of expected scrap when we computed the ₹30 rate, so the **300 units of scrap that were never generated must be charged back** to the Abnormal Gain A/c (300 × ₹15 = ₹4,500). Hence the net benefit to P&L is not the full ₹9,000 but ₹9,000 − ₹4,500 = ₹4,500. Forgetting this scrap clawback overstates the gain — the single most common error on this variant.

*(Full-marks tip: examiners specifically check the ₹4,500 scrap debit in the Abnormal Gain A/c and that the cash column of Normal Loss A/c uses 700, not 1,000, units. Miss the clawback and you lose 2–3 marks.)*

---

### Q55. Ch: Process & Operation Costing — Inter-Process Profit & Stock Reserve (Marks: 10) [Problem]
**Question:** A product passes through Process-I and Process-II and then to Finished Stock. Each transfer is made at cost **plus a profit margin computed on transfer price** — Process-I loads 20%, Process-II loads 25%. There is no opening stock anywhere. Closing stock in Process-II is ₹27,000 (at transfer value) and closing Finished Stock is ₹36,000 (at transfer value). Sales for the period were ₹1,50,000.

| Element | Process-I (₹) | Process-II (₹) |
|---|---|---|
| Direct materials | 30,000 | 30,000 |
| Direct wages | 20,000 | 20,000 |
| Overheads | 10,000 | 10,000 |

Compute (a) the transfer prices, (b) the provision for unrealised profit in each closing stock, and (c) the **actual (realised) profit** for the period. Verify your answer independently.

**Solution:**

**WN-1 — Process-I transfer price.** Cost = 30,000+20,000+10,000 = ₹60,000. Profit is 20% of transfer price ⇒ cost is 80% ⇒ Transfer = 60,000 ÷ 0.80 = **₹75,000** (Cost 60,000, Profit **15,000**).

**WN-2 — Process-II three-column build-up (before its own profit).**

| Particulars | Cost ₹ | Profit ₹ | Total ₹ |
|---|---|---|---|
| Transfer from I | 60,000 | 15,000 | 75,000 |
| Materials/Wages/OH added | 60,000 | — | 60,000 |
| **Sub-total (before closing stock)** | **1,20,000** | **15,000** | **1,35,000** |

**WN-3 — Unrealised profit in Process-II closing stock.** The stock carries the *same proportion of profit* as the goods it came from:
Reserve = Closing stock × (Profit ÷ Total) = 27,000 × (15,000 ÷ 1,35,000) = 27,000 × 1/9 = **₹3,000**.
So closing stock = Cost 24,000 + Profit 3,000. Cost of goods leaving Process-II = 1,20,000 − 24,000 = 96,000; profit carried = 15,000 − 3,000 = 12,000; Total = ₹1,08,000.

**WN-4 — Process-II adds 25% on transfer price.** Transfer to Finished = 1,08,000 ÷ 0.75 = ₹1,44,000; Process-II's own profit = **₹36,000**. Goods to Finished: Cost 96,000, Profit 48,000 (=12,000+36,000), Total 1,44,000.

**WN-5 — Unrealised profit in Finished closing stock.** Reserve = 36,000 × (48,000 ÷ 1,44,000) = 36,000 × 1/3 = **₹12,000**.

**WN-6 — Apparent profit by account.**

| Account | Apparent profit (₹) |
|---|---|
| Process-I | 15,000 |
| Process-II | 36,000 |
| Finished Stock: Sales 1,50,000 − (0 + 1,44,000 − 36,000) | 42,000 |
| **Total apparent profit** | **93,000** |

**Statement of Actual Profit**

| Particulars | ₹ |
|---|---|
| Total apparent profit | 93,000 |
| Less: Provision — Process-II closing stock | (3,000) |
| Less: Provision — Finished closing stock | (12,000) |
| **Actual (realised) profit** | **78,000** |

**WN-7 — Independent verification.** Actual profit = Sales − actual cost incurred + closing stock **at cost** − opening stock at cost = 1,50,000 − 1,20,000 + (24,000 + 24,000) − 0 = **₹78,000**. ✓ (Finished stock at cost = 36,000 − 12,000 = 24,000.)

**Answer:** Actual realised profit = **₹78,000**; unrealised-profit provisions = ₹3,000 (Process-II) + ₹12,000 (Finished) = **₹15,000**.

**Why this way (the reasoning):** Loading profit at each transfer lets management see whether each process *would* be profitable if it "sold" its output — useful for make-or-buy and inter-departmental performance. But that inter-process profit is **book profit, not cash**: as long as the goods sit unsold in the next process's stock, the margin is imaginary and must be *provided against*, otherwise closing stock (an asset) would be inflated above true cost, violating the prudence concept and the cost principle for inventory. The reserve is computed by the profit-to-total ratio of *that stock's source* because the stock is a homogeneous slice of those goods — it carries profit in the same proportion. When the goods are finally sold the provision is released, so realised profit only crystallises on sale. The verification (Sales − cost + closing-stock-at-cost) proves the whole apparatus merely restates inventory at true cost — which is exactly why it must equal the simple cost-based profit.

*(Full-marks tip: award-winning answers use the three-column (Cost/Profit/Total) format and apply the ratio on the *sub-total before deducting closing stock*. The classic error is computing the reserve on cost rather than on the total, or forgetting that Process-II's 25% is on transfer price, not cost.)*

---

### Q56. Ch: Process & Operation Costing — Valuation of Normal vs Abnormal Loss (Marks: 5) [Theory]
**Question:** "Normal loss is valued only at its scrap (realisable) value, whereas abnormal loss is valued at the full cost per good unit." Explain the principle that justifies this asymmetric treatment, and analyse the consequence for the good output and for the Costing P&L Account. Would your reasoning change if there were **no** scrap value?

**Answer:**

**Governing principle.** Cost accounting distinguishes **expected (normal)** shrinkage from **unexpected (abnormal)** shrinkage, and treats them oppositely because they mean different things about the process.

1. **Normal loss** is an unavoidable, inherent feature of the process (evaporation, chippings, rejects within tolerance). It is *anticipated*, so its cost is treated as a **legitimate cost of producing good output**. Accordingly it is given **no share of process cost** and is carried only at whatever the scrap fetches. The mechanism: cost per good unit = (total cost − scrap value of normal loss) ÷ (input − normal-loss units). Reducing the denominator automatically spreads the normal-loss cost over the survivors — good output *absorbs* it. This is correct because a buyer of the good units is, in reality, paying for the material that was always destined to be lost.

2. **Abnormal loss** is loss *beyond* the normal tolerance — caused by breakdown, negligence, sub-standard material, i.e. controllable failure. It is **not** a cost of good production; it is a loss of resources that should not have happened. Hence it is valued at the **full normal cost per good unit** and written off to **Costing P&L**, so that (a) the good units are *not* burdened with the cost of avoidable inefficiency, and (b) management sees the rupee cost of the failure as a separate, visible figure to be investigated and controlled.

**Consequence.** If abnormal loss were valued at scrap (like normal loss), the entire avoidable cost would silently reload onto good units, inflating product cost, concealing the inefficiency and defeating cost control. Conversely, if normal loss were valued at full cost, good output would appear artificially cheap while an "expected" loss is paraded through P&L — misleading, since it was never controllable.

**Effect of no scrap value.** The *reasoning is unchanged*. With no scrap: normal loss is valued at **nil** (its cost still self-loads onto good units via the denominator), and abnormal loss is still valued at **full cost** and written to P&L. Scrap value only reduces the amounts, not the principle: the deciding factor is *controllability and expectedness*, not the existence of a resale value.

**Why this way (the reasoning):** The heart of the matter is the accountant's job of **separating the controllable from the uncontrollable**. Product cost should reflect what it *unavoidably* takes to make a good unit; anything avoidable belongs to the manager's performance report (P&L), not the product. Valuing normal loss at scrap and abnormal loss at full cost is simply this philosophy expressed in numbers — it makes the "cost of inefficiency" a bright line item instead of a hidden loading. Students who memorise "normal at scrap, abnormal at cost" without this logic cannot handle the no-scrap or abnormal-gain variants; those who understand controllability answer every variant correctly.

*(Full-marks tip: examiners look for the words "controllable/avoidable vs unavoidable", the denominator-reduction mechanism, and the P&L write-off rationale. A pure definition without the "why good units absorb normal loss" mechanism caps you at ~2 marks.)*

---

### Q57. Ch: Process & Operation Costing — FIFO vs Weighted Average Cost per Unit (Marks: 8) [Problem]
**Question:** Process-Z had no losses this month. From the data below, compute the cost per equivalent unit **under both FIFO and weighted-average methods** and reconcile *why* they differ. Comment on which method better reflects current-period cost, using the figures.

| Particulars | Units | Materials | Conversion |
|---|---|---|---|
| Opening WIP | 4,000 | 100% | 75% |
| Introduced | 16,000 | — | — |
| Completed & transferred | 18,000 | — | — |
| Closing WIP | 2,000 | 100% | 50% |
| Opening WIP value (₹) | — | 40,000 | 30,000 |
| Current cost (₹) | — | 1,60,000 | 3,12,000 |

**Solution:**

**WN-1 — Weighted-average EU & rate.**

| | Materials | Conversion |
|---|---|---|
| Completed 18,000 | 18,000 | 18,000 |
| Closing WIP 2,000 | 2,000 (100%) | 1,000 (50%) |
| **EU** | **20,000** | **19,000** |
| Cost (opening + current) | 40,000+1,60,000 = 2,00,000 | 30,000+3,12,000 = 3,42,000 |
| **Rate/EU** | **₹10** | **₹18** |

WA cost per completed unit = 10 + 18 = **₹28**.

**WN-2 — FIFO EU & rate (current cost only).**

| | Materials | Conversion |
|---|---|---|
| Opening WIP to complete (4,000) | 0 (0%) | 1,000 (25%) |
| Started & completed (18,000−4,000) | 14,000 | 14,000 |
| Closing WIP 2,000 | 2,000 (100%) | 1,000 (50%) |
| **EU** | **16,000** | **16,000** |
| Current cost | 1,60,000 | 3,12,000 |
| **Rate/EU** | **₹10** | **₹19.50** |

FIFO cost per (current) equivalent unit = 10 + 19.50 = **₹29.50**.

**WN-3 — Why the difference.** Materials rate is identical (₹10) because the opening material rate happened to equal the current rate. The **conversion** rate differs: WA ₹18 vs FIFO ₹19.50. The implied *opening* conversion rate = 30,000 ÷ (4,000 × 75% = 3,000 EU) = **₹10** — far below the current ₹19.50. WA averages the cheap ₹10 opening conversion with the dearer current cost, dragging the rate down to ₹18; FIFO refuses to mix them and reports the pure current ₹19.50.

**Answer:** FIFO cost/EU = **₹29.50**; WA cost/EU = **₹28.00**; the ₹1.50 gap is entirely conversion cost, caused by WA blending the cheaper ₹10 opening-period conversion cost into the current average.

**Why this way (the reasoning):** The two methods answer different questions. FIFO asks "what did it cost to do *this month's* work?" — so it excludes the entire brought-forward value and counts only the work physically done this period (including finishing the opening WIP's leftover 25% conversion). Weighted average asks "what is the *average* cost of a unit in this pool?" — so it fuses old and new cost and old and new work. When input prices are *rising* (here conversion jumped from ₹10 to ₹19.50), WA **understates** current cost and drags closing-stock value below replacement cost, whereas FIFO's rate mirrors current conditions and is the better guide for pricing and cost control. The lesson for students: the numerical gap is never arbitrary — it is exactly the profit/stock effect of averaging a cheaper opening layer, and you can always trace it to the difference between the opening-layer rate and the current rate.

*(Full-marks tip: the reconciliation paragraph (isolating the ₹10 vs ₹19.50 conversion rates) is where the marks sit. Merely producing two numbers without explaining the driver forfeits the "comment/analyse" marks.)*

---

### Q58. Ch: Process & Operation Costing — Validity of Loss Treatment (Marks: 6) [Case/Application]
**Question:** The cost accountant of Vega Ltd prepared Process-3 as follows: he **charged the entire cost of the normal loss to the Costing P&L Account** ("since it is a loss"), and he **valued the abnormal loss at scrap value only** ("since damaged units are only worth scrap"). He also credited the *whole* of the scrap sale proceeds — from both normal and abnormal loss — to the Costing P&L. Examine the validity of each of these three treatments and state the correct approach.

**Answer:**

**Treatment 1 — charging the whole normal-loss cost to P&L.** *Invalid.* Normal loss is an **unavoidable, expected** cost of obtaining good output; it must be **absorbed by the good units**, not written off. The correct method gives normal loss **no** cost of its own and divides (total cost − normal-loss scrap) by (input − normal-loss units), so its cost automatically self-loads onto good output. Routing it through P&L understates product cost, overstates period loss, and would let a manager under-price the goods because they look artificially cheap. The only amount that touches an account outside the process is the *scrap realisation*, not the cost.

**Treatment 2 — valuing abnormal loss at scrap only.** *Invalid.* Abnormal loss is an **avoidable** failure and must be valued at the **full normal cost per good unit** and then written to Costing P&L (net of its own scrap). Valuing it at mere scrap hides the true rupee cost of the inefficiency: the difference between full cost and scrap would silently reload onto the good units, inflating their cost and defeating cost control — the exact opposite of what the accountant intended.

**Treatment 3 — crediting all scrap to P&L.** *Partly invalid.* The scrap of **normal loss** must be credited to the **Process Account / Normal Loss Account** (it reduces the process cost that good units bear), not to P&L. Only the scrap of **abnormal loss** is netted within the Abnormal Loss Account before the balance goes to P&L. Dumping all scrap into P&L again distorts product cost.

**Correct picture.** Normal loss → nil cost, scrap credited to process; good units absorb the cost. Abnormal loss → full cost per good unit, its scrap netted in the Abnormal Loss A/c, balance to P&L. In short, the accountant has **exactly reversed** the correct treatment.

**Conclusion.** All three treatments are wrong; each has the effect of misstating both product cost and period profit and destroying the control information that the normal/abnormal split exists to provide.

**Why this way (the reasoning):** The scenario is a deliberate inversion designed to test whether the student understands *why* the rules exist rather than the rules themselves. The governing idea is that product cost must capture only *unavoidable* cost, while *avoidable* loss must be spotlighted in P&L. The accountant's "commonsense" logic ("a loss is a loss", "damaged goods are worth scrap") sounds plausible but breaks both principles at once — it buries the controllable loss inside the product and parades the uncontrollable loss through P&L. Recognising that his treatment is the mirror-image of the correct one is the mark of genuine understanding.

*(Full-marks tip: address each of the three treatments separately with a verdict + reason + correction. A generic "he is wrong" without correcting the scrap-crediting point loses the third mark. Examiners reward the phrase "he has reversed the correct treatment".)*

---

### Q59. Ch: Process & Operation Costing — Inter-Process Profit: Opening-Stock Reversal (Marks: 8) [Problem]
**Question:** The Finished Stock Account of Nimbus Ltd (goods received from processes at cost-plus) shows, for the year: opening stock ₹60,000, goods received during the year ₹4,00,000 (of which the profit element loaded by prior processes is ₹1,00,000), closing stock ₹80,000 (at transfer value), and sales ₹4,20,000. The provision for unrealised profit **brought forward** on the opening stock was ₹15,000. Compute (a) the provision required on closing stock, (b) the change in provision, and (c) the actual realised profit, clearly showing the treatment of the opening-stock provision.

**Solution:**

**WN-1 — Profit ratio in goods received.** Profit ÷ Total received = 1,00,000 ÷ 4,00,000 = **25%**.

**WN-2 — Provision on closing stock.** Closing stock carries the same 25% profit proportion:
Reserve (closing) = 80,000 × 25% = **₹20,000**.

**WN-3 — Apparent profit in Finished Stock A/c.**
Apparent profit = Sales − (Opening + Received − Closing) = 4,20,000 − (60,000 + 4,00,000 − 80,000) = 4,20,000 − 3,80,000 = **₹40,000**.

**Statement of Actual Realised Profit**

| Particulars | ₹ |
|---|---|
| Apparent profit (Finished Stock A/c) | 40,000 |
| Add: Provision on opening stock now RELEASED (b/f) | 15,000 |
| Less: Provision on closing stock CREATED (c/f) | (20,000) |
| **Actual realised profit** | **35,000** |

**WN-4 — Net change in provision.** Provision rose from 15,000 to 20,000 → **increase of ₹5,000** charged to P&L (equivalently: 40,000 − 5,000 = 35,000). ✓

**Answer:** Closing-stock provision **₹20,000**; net increase in provision **₹5,000**; actual realised profit **₹35,000**.

**Why this way (the reasoning):** The presence of *opening* stock is the twist that separates a good answer from a poor one. Last year's closing provision of ₹15,000 was created because those goods were then unsold — their loaded profit was still unreal. This year those very goods have been sold, so that profit has **crystallised into cash** and the old provision must be **released (added back)** to profit. Simultaneously, a *new* batch of goods remains unsold at year-end, carrying fresh unreal profit of ₹20,000, which must now be **provided (deducted)**. Hence the P&L is charged only with the **net movement** in the provision (₹5,000), not the whole closing figure. Failing to reverse the opening provision double-counts the earlier profit deferral and understates realised profit by ₹15,000. The principle is the matching/prudence pairing: recognise profit only when goods leave the building, defer it while they sit in stock, and reverse the deferral when they finally sell.

*(Full-marks tip: the two-line "add opening provision, deduct closing provision" is the examiner's checklist. The frequent error is deducting only the ₹20,000 closing provision and forgetting to release the ₹15,000 opening provision — costing 2–3 marks and giving the wrong ₹20,000 profit.)*

---

### Q60. Ch: Joint Products & By-Products — NRV / Reverse-Cost Apportionment (Marks: 10) [Problem]
**Question:** In a common process costing ₹3,00,000, three joint products emerge. Product-A and Product-B require further processing before sale; Product-C is sold at split-off. Selling & distribution costs are incurred on all three. Apportion the joint cost by the **Net Realisable Value (reverse-cost) method** and prepare a Statement of Profitability.

| Product | Units | Final selling price/unit (₹) | Further processing cost (₹ total) | Selling exp/unit (₹) |
|---|---|---|---|---|
| A | 5,000 | 40 | 30,000 | 2 |
| B | 4,000 | 55 | 40,000 | 5 |
| C | 8,000 | 12 | Nil | 2 |

**Solution:**

**WN-1 — Net Realisable Value at split-off** = Sales value − further processing cost − selling expenses.

| Product | Sales (₹) | Less: Further (₹) | Less: Selling (₹) | NRV (₹) |
|---|---|---|---|---|
| A | 5,000×40 = 2,00,000 | 30,000 | 5,000×2 = 10,000 | 1,60,000 |
| B | 4,000×55 = 2,20,000 | 40,000 | 4,000×5 = 20,000 | 1,60,000 |
| C | 8,000×12 = 96,000 | Nil | 8,000×2 = 16,000 | 80,000 |
| **Total** | **5,16,000** | **70,000** | **46,000** | **4,00,000** |

**WN-2 — Apportion joint cost ₹3,00,000 in NRV ratio 160:160:80** (i.e. 2:2:1; factor = 3,00,000 ÷ 4,00,000 = 0.75).

| Product | NRV (₹) | Joint cost share (₹) |
|---|---|---|
| A | 1,60,000 | 1,20,000 |
| B | 1,60,000 | 1,20,000 |
| C | 80,000 | 60,000 |
| **Total** | **4,00,000** | **3,00,000** |

**Statement of Profitability**

| Particulars | A (₹) | B (₹) | C (₹) | Total (₹) |
|---|---|---|---|---|
| Sales | 2,00,000 | 2,20,000 | 96,000 | 5,16,000 |
| Less: Joint cost | 1,20,000 | 1,20,000 | 60,000 | 3,00,000 |
| Less: Further processing | 30,000 | 40,000 | — | 70,000 |
| Less: Selling expenses | 10,000 | 20,000 | 16,000 | 46,000 |
| **Profit** | **40,000** | **40,000** | **20,000** | **1,00,000** |

**Answer:** Joint cost apportioned A ₹1,20,000, B ₹1,20,000, C ₹60,000; total profit **₹1,00,000**.

**Why this way (the reasoning):** When products are **not saleable at the split-off point** (A and B must be processed further), there is no market value at split-off to apportion on — so we *work backwards* ("reverse cost"): take the final sales value and strip out every cost incurred **after** split-off (further processing + selling), leaving a **notional value at split-off** = NRV. Apportioning joint cost on NRV is fair because it charges each product with joint cost in proportion to the wealth it can *ultimately* realise net of its own downstream costs. Note the trap: A and B have *equal* final sales value only after you deduct their *different* further and selling costs — a naïve "final sales value" apportionment (₹2,00,000 : ₹2,20,000 : ₹96,000) would over-burden B, which incurs the heaviest post-split costs, and distort every product's profit. Deducting the post-split costs first is precisely what stops that distortion.

*(Full-marks tip: show the NRV working as a separate statement and label it "value at split-off". Deductions come from apportioning on *gross* final sales value instead of NRV, or forgetting selling expenses in the NRV computation.)*

---

### Q61. Ch: Joint Products & By-Products — Further-Processing (Sell-or-Process) Decision (Marks: 8) [Problem]
**Question:** Product-X emerges from a joint process. At split-off, 10,000 units of X can be sold at ₹20 each. Alternatively X can be processed further at an additional cost of ₹80,000; processing causes a 5% loss of units, and the finished output sells at ₹30 each but incurs additional selling & distribution cost of ₹1 per unit sold. The joint cost apportioned to X is ₹1,50,000. **Advise, with an incremental analysis, whether X should be processed further.**

**Solution:**

**WN-1 — Units after further processing.** 10,000 − 5% loss = **9,500 units**.

**WN-2 — Incremental (differential) analysis.** The apportioned joint cost of ₹1,50,000 is **irrelevant** — it is incurred whether or not X is processed further (a sunk/common cost at the decision point).

| Particulars | ₹ |
|---|---|
| Revenue if processed further (9,500 × 30) | 2,85,000 |
| Revenue if sold at split-off (10,000 × 20) | 2,00,000 |
| **Incremental revenue** | **85,000** |
| Incremental costs — further processing | 80,000 |
| Incremental costs — extra selling (9,500 × 1) | 9,500 |
| **Total incremental cost** | **89,500** |
| **Incremental result (85,000 − 89,500)** | **(4,500)** |

**Answer:** Processing further yields ₹4,500 **less** than selling at split-off. **Advise: sell Product-X at split-off; do NOT process further.**

**Why this way (the reasoning):** A sell-or-process-further decision is a classic **incremental (differential) cost** problem, and the golden rule is that **only costs and revenues that change** with the decision are relevant. The joint cost of ₹1,50,000 has already been incurred to reach split-off and cannot be un-spent — it is common to both alternatives, so including it in the comparison (e.g., computing a "profit" for each route) is a beginner's error that can flip the answer. The correct comparison is *incremental revenue* (the ₹85,000 uplift from the higher price on fewer units) against *incremental cost* (further processing ₹80,000 **plus** the extra ₹1/unit selling cost that only arises on the processed route). Two traps make this "hard": (1) the 5% processing loss means you sell 9,500 not 10,000 units, so the revenue uplift is smaller than the naïve 10,000 × (30−20) = ₹1,00,000; and (2) the extra selling cost tips a marginally positive decision into negative. Miss either and you wrongly recommend further processing.

*(Full-marks tip: explicitly state "joint cost of ₹1,50,000 is irrelevant/sunk" — examiners award a mark just for that. The other marks hinge on using 9,500 units for revenue *and* the extra selling cost. Presenting full-cost profit statements instead of incrementals is heavily penalised.)*

---

### Q62. Ch: Joint Products & By-Products — By-Product Credit Methods & Stock Effect (Marks: 8) [Problem]
**Question:** A process costing ₹1,00,000 yields 10,000 units of main product-M and 1,000 units of by-product-N. By-product-N is sold for ₹8/unit after incurring ₹2/unit further processing and ₹1/unit selling cost. During the period 9,000 units of M were sold at ₹15 each and 1,000 units remained in closing stock. Show the cost per unit of M and the profit under (i) the **"Other Income" method** (by-product net income credited to P&L) and (ii) the **"Net Realisable Value credited to process" method**, and explain why the two profits differ.

**Solution:**

**WN-1 — By-product net realisable value.** NRV of N = 1,000 × (8 − 2 − 1) = 1,000 × 5 = **₹5,000**.

**Method (i) — Other Income (by-product income to P&L).**
- Cost of M = full joint cost ₹1,00,000 ⇒ cost/unit = 1,00,000 ÷ 10,000 = **₹10**.
- COGS (9,000 × 10) = 90,000; Sales = 9,000 × 15 = 1,35,000.
- Profit = 1,35,000 − 90,000 + by-product income 5,000 = **₹50,000**.

**Method (ii) — NRV credited to joint cost.**
- Cost of M = (1,00,000 − 5,000) = 95,000 ⇒ cost/unit = 95,000 ÷ 10,000 = **₹9.50**.
- COGS (9,000 × 9.50) = 85,500; Sales = 1,35,000.
- Profit = 1,35,000 − 85,500 = **₹49,500**.

**WN-2 — Reconciliation of the ₹500 difference.**

| | Method (i) | Method (ii) |
|---|---|---|
| Profit | 50,000 | 49,500 |

The ₹500 gap = by-product credit retained in **closing stock** under Method (ii): 1,000 unsold units × (₹0.50 credit per unit) = ₹500. Method (i) recognises the *entire* ₹5,000 by-product income immediately; Method (ii) spreads it over all 10,000 units, so 1,000/10,000 (= ₹500) stays locked in unsold stock and is not yet in profit.

**Answer:** Cost/unit of M = ₹10 (Method i) vs ₹9.50 (Method ii); Profit = ₹50,000 vs ₹49,500; the ₹500 difference is the by-product credit deferred inside closing stock under Method (ii).

**Why this way (the reasoning):** By-products have minor value, so the question is *where* to put their small realisation. The **Other Income** method treats the by-product as incidental and credits its net proceeds straight to P&L in the period of sale — simple, and it recognises the whole benefit at once. The **NRV-credited-to-cost** method treats the by-product recovery as a *reduction of the main product's cost of production*, so the benefit is embedded in the main product's unit cost and is released to profit only as the main product sells. When there is **no closing stock the two methods give identical profit**; the difference appears *only because* unsold main-product stock defers part of the by-product credit under Method (ii). This teaches the deeper point: the choice of by-product method is essentially an **inventory-valuation policy** — it shifts profit between periods via stock, it does not create or destroy total profit over the product's life.

*(Full-marks tip: the marks are in the reconciliation — proving the ₹500 is 1,000 unsold units × ₹0.50. Stating "profits differ because of method" without quantifying via closing stock earns little. Note NRV (not gross ₹8) is the correct credit.)*

---

### Q63. Ch: Joint Products & By-Products — NRV Apportionment with a By-Product (Marks: 10) [Problem]
**Question:** A joint process costing ₹5,00,000 produces two joint products P and Q (neither saleable at split-off) and one by-product Z. By-product Z (2,000 units) has a net realisable value of ₹5 per unit. P and Q are then processed further. Apportion the joint cost by the **Net Realisable Value method** (after adjusting for the by-product) and prepare a profitability statement.

| Product | Units | Final SP/unit (₹) | Further processing cost (₹) |
|---|---|---|---|
| P | 10,000 | 40 | 60,000 |
| Q | 8,000 | 50 | 40,000 |

**Solution:**

**WN-1 — Adjust joint cost for by-product.** By-product NRV credited to the joint process = 2,000 × ₹5 = ₹10,000.
**Net joint cost to be apportioned** = 5,00,000 − 10,000 = **₹4,90,000**.

**WN-2 — NRV at split-off for P and Q.**

| Product | Final sales (₹) | Less: Further (₹) | NRV (₹) |
|---|---|---|---|
| P | 10,000×40 = 4,00,000 | 60,000 | 3,40,000 |
| Q | 8,000×50 = 4,00,000 | 40,000 | 3,60,000 |
| **Total** | **8,00,000** | **1,00,000** | **7,00,000** |

**WN-3 — Apportion ₹4,90,000 in NRV ratio 340:360** (factor = 4,90,000 ÷ 7,00,000 = 0.70).

| Product | NRV (₹) | Joint cost share (₹) |
|---|---|---|
| P | 3,40,000 | 2,38,000 |
| Q | 3,60,000 | 2,52,000 |
| **Total** | **7,00,000** | **4,90,000** |

**Statement of Profitability**

| Particulars | P (₹) | Q (₹) | Total (₹) |
|---|---|---|---|
| Final sales | 4,00,000 | 4,00,000 | 8,00,000 |
| Less: Joint cost share | 2,38,000 | 2,52,000 | 4,90,000 |
| Less: Further processing | 60,000 | 40,000 | 1,00,000 |
| **Profit** | **1,02,000** | **1,08,000** | **2,10,000** |

**Answer:** Net joint cost ₹4,90,000 apportioned P ₹2,38,000, Q ₹2,52,000; total profit **₹2,10,000** (by-product Z's ₹10,000 already absorbed as a cost reduction).

**Why this way (the reasoning):** Two principles combine here. First, a **by-product is not a joint product** — its value is too small to justify apportioning joint cost *to* it; instead its net realisable value is **deducted from the total joint cost before apportionment**, so the *main* products effectively enjoy the by-product recovery as a cost saving. That is why we apportion ₹4,90,000, not ₹5,00,000. Second, because P and Q cannot be sold at split-off, we again use the **reverse-cost/NRV** logic: strip each product's own further-processing cost from its final sales value to get a notional split-off value, and apportion on that. Doing the by-product adjustment *first* and the NRV apportionment *second* is the correct sequence — reversing them (apportioning ₹5,00,000 and then trying to credit Z) would over-charge the joint products. The neat 0.70 factor confirms the arithmetic: each product bears joint cost equal to 70% of the wealth it can net realise.

*(Full-marks tip: examiners specifically check that the by-product NRV is netted *before* apportionment and that NRV (not gross sales) drives the ratio. Apportioning the full ₹5,00,000, or crediting Z to P&L instead of to the joint cost, are the common 2–3 mark errors.)*

---

### Q64. Ch: Joint Products & By-Products — Physical Units vs Sales Value Method (Marks: 6) [Problem]
**Question:** Joint cost ₹2,40,000 is shared by two joint products. Apportion it under (i) the **physical units** method and (ii) the **sales value at split-off** method, prepare profit statements under each, and comment on which gives a more meaningful result.

| Product | Units | Selling price/unit (₹) |
|---|---|---|
| A | 12,000 | 30 |
| B | 8,000 | 5 |

**Solution:**

**WN-1 — Sales values.** A = 12,000 × 30 = ₹3,60,000; B = 8,000 × 5 = ₹40,000; Total = ₹4,00,000.

**Method (i) — Physical units (ratio 12,000 : 8,000 = 3 : 2).**

| Product | Joint cost (₹) | Sales (₹) | Profit / (Loss) (₹) |
|---|---|---|---|
| A | 2,40,000 × 3/5 = 1,44,000 | 3,60,000 | 2,16,000 |
| B | 2,40,000 × 2/5 = 96,000 | 40,000 | **(56,000)** |
| **Total** | **2,40,000** | **4,00,000** | **1,60,000** |

**Method (ii) — Sales value at split-off (ratio 360 : 40 = 9 : 1).**

| Product | Joint cost (₹) | Sales (₹) | Profit (₹) | GP % |
|---|---|---|---|---|
| A | 2,40,000 × 360/400 = 2,16,000 | 3,60,000 | 1,44,000 | 40% |
| B | 2,40,000 × 40/400 = 24,000 | 40,000 | 16,000 | 40% |
| **Total** | **2,40,000** | **4,00,000** | **1,60,000** | **40%** |

**Answer:** Total profit is ₹1,60,000 under both, but the physical-units method shows Product-B making a **loss of ₹56,000** while the sales-value method shows both products earning a uniform **40% gross margin**. The **sales value method is more meaningful.**

**Why this way (the reasoning):** The physical-units method charges cost purely in proportion to *quantity*, ignoring that a unit of A is worth ₹30 while a unit of B is worth only ₹5. It therefore dumps a large slice of joint cost (₹96,000) onto the low-value product B, which cannot possibly recover it from ₹40,000 of sales — manufacturing a phantom loss and making A look spectacularly profitable. This is misleading because **at the split-off point the products are inseparable**; no product is "really" losing money — the split is an accounting convention. The **sales value method** apportions cost on each product's *ability to bear cost* (its revenue-earning power), which produces a **uniform gross-margin %** and prevents the distortion. That uniform margin is exactly why it is preferred: it reflects the reality that all joint products share one indivisible production effort. Physical-units apportionment is defensible only when products' unit values are similar or when a common physical unit (tonne, litre) genuinely drives cost.

*(Full-marks tip: the comment is worth ~2 marks — highlight the phantom loss on B and the uniform 40% margin. Simply producing both tables without the critique caps you well below full marks.)*

---

### Q65. Ch: Joint Products & By-Products — Reverse-Cost / NRV Method Rationale (Marks: 5) [Theory]
**Question:** Explain the **reverse-cost (Net Realisable Value) method** of apportioning joint cost. Why is it considered superior when joint products require further processing before sale, and why would apportioning on *final* sales value (without deducting post-split-off costs) be incorrect?

**Answer:**

**The method.** Under the reverse-cost / NRV method, joint cost is apportioned in the ratio of each product's **Net Realisable Value at the split-off point**, computed by *working backwards* from the final sale:
> NRV at split-off = Final sales value − Further processing cost after split-off − Selling & distribution cost.
The joint cost pool (net of any by-product credit) is then divided in that NRV ratio.

**Why it is used when products need further processing.** The ideal apportionment base is the **market value at split-off**. But when a product is **not saleable at split-off** — it must first be refined, blended or packed — no such market value exists. The reverse-cost method *manufactures* a surrogate split-off value by removing all costs incurred *after* split-off from the final price. What remains is the wealth the product carries *as it leaves the joint process* — a logically sound proxy for the missing split-off market value.

**Why final sales value (gross) would be wrong.** Apportioning on **final** sales value ignores that different products incur **different post-split-off costs**. A product that needs heavy further processing has a high final price *not* because it was more valuable at split-off, but because a lot of *separate, identifiable* cost was added later. Charging joint cost in proportion to final price would over-burden that product with joint cost for value it did **not** possess at split-off, distorting every product's profitability. Deducting the post-split-off costs corrects this: it isolates the value attributable to the *joint* effort from the value created by *subsequent, separable* effort.

**Conclusion.** The reverse-cost method is superior precisely because it apportions joint cost on the value that existed **at the point of separation**, which is the only value the joint cost actually produced. It gives fairer product costs and avoids the systematic bias of the gross-sales-value approach.

**Why this way (the reasoning):** Joint cost is, by definition, the cost of everything *up to* split-off. It must therefore be shared on a base that measures value *at* split-off — not value created afterwards by separable processing that is already directly charged to each product. The reverse-cost method's whole purpose is to "undo" the later value additions so that only the split-off value drives the apportionment. Students who grasp this see immediately why gross final sales value double-counts: it lets a product's *own* later processing pull *joint* cost towards it, which is economically meaningless.

*(Full-marks tip: give the NRV formula, the phrase "value at the point of separation", and a concrete reason why gross-value apportionment is biased. A definition without the "why gross value is wrong" analysis will not reach full marks on this "explain why" variant.)*

---

### Q66. Ch: Joint Products & By-Products — Validity of a Further-Processing Rejection (Marks: 8) [Case/Application]
**Question:** Product-R emerges from a joint process; 2,000 units can be sold at split-off for ₹100 each. Marketing proposes processing R further at a cost of ₹1,20,000, after which it would sell at ₹180 per unit (no unit loss, no extra selling cost). The plant manager rejects the proposal, arguing: *"Each unit of R already absorbs ₹45 of joint cost (₹90,000 ÷ 2,000). After further processing, the total cost per unit is ₹45 + ₹60 further cost = ₹105, but the price rises by only ₹80. So we lose ₹25 a unit — reject it."* **Examine the validity of the manager's reasoning and advise the correct decision.**

**Answer:**

**Governing principle.** A sell-or-process-further decision is governed by **incremental (differential) analysis**: compare only the revenues and costs that *change*. Costs already incurred to reach split-off (the joint cost) are **sunk and common** to both alternatives and must be **excluded**.

**Where the manager errs.** The manager has committed the **sunk-cost fallacy**. The ₹45/unit joint cost (₹90,000) is incurred *whether R is sold at split-off or processed further* — it is identical under both options and therefore **irrelevant** to the choice. By loading it into the "further-processing cost" he has manufactured a fictitious ₹25 loss. His ₹105 "total cost" mixes a relevant cost (₹60 further processing) with an irrelevant one (₹45 joint), which is analytically invalid.

**Correct incremental analysis.**

| Particulars | ₹ |
|---|---|
| Incremental revenue (2,000 × (180 − 100)) | 1,60,000 |
| Less: Incremental cost (further processing) | 1,20,000 |
| **Incremental benefit of processing further** | **40,000** |

Per unit: incremental revenue ₹80 vs incremental cost ₹60 → **net gain ₹20/unit** (×2,000 = ₹40,000).

**Conclusion / Advice.** The manager's reasoning is **invalid**. Correctly analysed, processing R further yields an **additional ₹40,000** profit, so R **should be processed further** (assuming spare capacity and no better use of it). Qualitative checks: confirm the ₹180 market can absorb the volume, the further processing does not strain capacity needed by more profitable products, and the price is sustainable.

**Why this way (the reasoning):** The case is engineered around the single most common decision-making error in joint-product costing — dragging **apportioned joint cost** into a decision it cannot influence. Apportioned joint cost is an *accounting allocation*, not a *decision-relevant cash flow*: no future action can change the ₹90,000 already spent to reach split-off, so it is the same under both options and cancels out. Once removed, the choice is transparent — spend ₹60 more per unit to earn ₹80 more per unit, a clear ₹20 gain. Teaching students to *first ask "does this cost change with the decision?"* immunises them against exactly this trap, which examiners plant repeatedly.

*(Full-marks tip: you must (1) name the sunk-cost fallacy, (2) state that apportioned joint cost is irrelevant, (3) produce the incremental statement, and (4) add a qualitative caveat (capacity/market). Merely computing ₹40,000 without diagnosing the manager's specific error loses the "examine validity" marks.)*

---

### Q67. Ch: Joint Products & By-Products — By-Product Credit: Gross vs Net (Marks: 6) [Problem]
**Question:** A process costing ₹3,60,000 yields 20,000 units of main product-A and 5,000 units of by-product-B. By-product-B sells at ₹12/unit but requires ₹2/unit further processing and ₹1/unit selling cost. Compute the cost per unit of main product-A when the by-product is credited to the joint cost under (i) the **gross sales value** basis and (ii) the **net realisable value** basis, and state which is the sounder treatment.

**Solution:**

**WN-1 — By-product credits.**
- Gross sales value = 5,000 × 12 = **₹60,000**.
- Net realisable value = 5,000 × (12 − 2 − 1) = 5,000 × 9 = **₹45,000**.

**WN-2 — Cost per unit of main product-A.**

| Basis | Joint cost less by-product credit (₹) | Cost/unit of A (÷20,000) |
|---|---|---|
| (i) Gross sales value | 3,60,000 − 60,000 = 3,00,000 | **₹15.00** |
| (ii) Net realisable value | 3,60,000 − 45,000 = 3,15,000 | **₹15.75** |

**Answer:** Cost/unit of A = ₹15.00 (gross basis) vs **₹15.75 (NRV basis)**. The **NRV basis is sounder**.

**Why this way (the reasoning):** Both methods reduce the main product's cost by the by-product's value, but they differ on *how much* value to credit. The **gross sales value** basis credits the full ₹60,000 selling price — yet ₹15,000 of that (further ₹2 + selling ₹1 per unit) is cost the firm must still *spend* to turn the raw by-product into saleable form. Crediting the gross figure therefore **over-states** the by-product's true benefit and **under-states** the main product's cost (₹15 instead of ₹15.75), understating inventory value and overstating early profit. The **net realisable value** basis credits only ₹45,000 — the genuine *net* recovery after its own downstream costs — which correctly measures the saving the by-product delivers to the main product. The principle mirrors the joint-product NRV logic: never let a product (or by-product) claim credit for value that only exists *because* of separately identifiable costs incurred after split-off. Hence NRV gives the truer main-product cost.

*(Full-marks tip: show both credits explicitly and justify NRV as "net of the by-product's own further and selling costs". The error that costs marks is crediting gross ₹60,000 without recognising the ₹15,000 of post-split-off cost.)*

---

### Q68. Ch: Joint Products & By-Products — Integrated: Apportionment + Further Processing + By-Product (Marks: 10) [Problem]
**Question:** A joint process costs ₹6,00,000 and yields three joint products A, B, C and one by-product Z (2,000 units, NRV ₹10/unit). Split-off (market) values are: A ₹30/unit, B ₹25/unit, C ₹45/unit; output is A 10,000 units, B 8,000 units, C 5,000 units. Product-C may instead be processed further into C+ at a cost of ₹1,00,000 and then sold at ₹70/unit (no unit loss). (a) Apportion the net joint cost by the **sales value at split-off** method; (b) decide whether C should be processed further; (c) prepare a profitability statement assuming your decision on C is adopted and A, B are sold at split-off. Verify total profit independently.

**Solution:**

**WN-1 — Net joint cost after by-product credit.** Z credit = 2,000 × ₹10 = ₹20,000 → **Net joint cost = 6,00,000 − 20,000 = ₹5,80,000**.

**WN-2 — Split-off sales values.**

| Product | Units | SP/unit (₹) | Split-off value (₹) |
|---|---|---|---|
| A | 10,000 | 30 | 3,00,000 |
| B | 8,000 | 25 | 2,00,000 |
| C | 5,000 | 45 | 2,25,000 |
| **Total** | | | **7,25,000** |

**WN-3 — Apportion ₹5,80,000 in ratio 300:200:225** (factor = 5,80,000 ÷ 7,25,000 = 0.80).

| Product | Split-off value (₹) | Joint cost share (₹) |
|---|---|---|
| A | 3,00,000 | 2,40,000 |
| B | 2,00,000 | 1,60,000 |
| C | 2,25,000 | 1,80,000 |
| **Total** | **7,25,000** | **5,80,000** |

**WN-4 — Sell-or-process-further decision for C** (joint cost share ₹1,80,000 is irrelevant/sunk).

| Particulars | ₹ |
|---|---|
| Revenue if processed further (5,000 × 70) | 3,50,000 |
| Revenue at split-off (5,000 × 45) | 2,25,000 |
| Incremental revenue | 1,25,000 |
| Less: Further processing cost | 1,00,000 |
| **Incremental benefit** | **25,000** |

⇒ **Process C further** (gain ₹25,000).

**Statement of Profitability** (A, B at split-off; C processed further)

| Particulars | A (₹) | B (₹) | C+ (₹) | Total (₹) |
|---|---|---|---|---|
| Sales | 3,00,000 | 2,00,000 | 3,50,000 | 8,50,000 |
| Less: Joint cost share | 2,40,000 | 1,60,000 | 1,80,000 | 5,80,000 |
| Less: Further processing | — | — | 1,00,000 | 1,00,000 |
| **Profit** | **60,000** | **40,000** | **70,000** | **1,70,000** |

**WN-5 — Independent verification.** Total revenue = product sales 8,50,000 + by-product Z (2,000×10) 20,000 = ₹8,70,000. Total cost = joint 6,00,000 + further 1,00,000 = ₹7,00,000. Profit = 8,70,000 − 7,00,000 = **₹1,70,000**. ✓

**Answer:** Net joint cost ₹5,80,000 apportioned A ₹2,40,000, B ₹1,60,000, C ₹1,80,000; **C should be processed further** (adds ₹25,000); total profit **₹1,70,000**.

**Why this way (the reasoning):** This capstone stitches together three separate principles that examiners love to test in one problem, and the order matters. **First**, the by-product Z is *not* apportioned joint cost — its NRV is netted off the joint cost pool, so only ₹5,80,000 is shared among the true joint products. **Second**, because all three joint products *have* a market value at split-off, the fairer **sales-value-at-split-off** basis is used (not physical units, which would distort). **Third — and this is the trap** — the apportioned joint cost of C (₹1,80,000) is a **sunk, common cost** and must be *excluded* from the process-further decision; the choice depends only on the ₹1,25,000 incremental revenue versus the ₹1,00,000 incremental cost. A student who wrongly includes C's ₹1,80,000 joint share would compute a "loss" on C+ and reject a profitable option. The independent check (total revenue including Z, less total cost) proves the whole schedule reconciles — a discipline that catches arithmetic slips and demonstrates that apportionment merely *redistributes* a fixed total profit, it never changes it.

*(Full-marks tip: sequence the answer — by-product credit → apportion net cost → incremental decision → profit statement → reconciliation. Examiners award marks at each stage; the two classic errors are (1) apportioning the gross ₹6,00,000 and (2) letting C's ₹1,80,000 joint share contaminate the further-processing decision. The reconciliation line is worth a mark on its own.)*

### Q69. Ch: Standard Costing — Material Cost, Price, Usage, Mix & Yield Variances (Marks: 10) [Problem]
**Question:** A firm produces a chemical "ZX" by processing two raw materials A and B. The standard cost card is set for a batch of **90 kg of finished ZX**:

| Material | Std input (kg) | Std price (₹/kg) | Std cost (₹) |
|---|---|---|---|
| A | 50 | 40 | 2,000 |
| B | 50 | 30 | 1,500 |
| **Input** | **100** | | **3,500** |
| Less: normal loss | 10 | | — |
| **Output** | **90** | | **3,500** |

During the month the actual output was **5,400 kg of ZX** and the actual materials consumed were:

| Material | Actual qty (kg) | Actual price (₹/kg) |
|---|---|---|
| A | 3,200 | 38 |
| B | 3,000 | 33 |

Compute the total material cost variance and analyse it fully into **price, usage, mix and yield** variances, marking each (F)/(A). Show that the sub-variances reconcile.

**Solution:**

**WN-1 — Standard quantity & standard cost for actual output.**
5,400 kg output = 5,400 ÷ 90 = **60 standard batches.**
- Std qty A = 50 × 60 = **3,000 kg** @ ₹40 → 1,20,000
- Std qty B = 50 × 60 = **3,000 kg** @ ₹30 → 90,000
- **Standard cost of actual output = ₹2,10,000** (std input 6,000 kg)

**WN-2 — Actual cost.**
- A: 3,200 × 38 = 1,21,600
- B: 3,000 × 33 = 99,000
- **Total actual cost = ₹2,20,600** (actual input 6,200 kg)

**WN-3 — Revised standard quantity (RSQ) = total actual input in standard mix (50:50).**
Total actual input = 6,200 kg → RSQ A = 3,100 kg, RSQ B = 3,100 kg.

**Statement Showing Material Variances**

| Variance | Formula | A | B | Total |
|---|---|---|---|---|
| Price = (SP−AP)×AQ | | (40−38)×3,200 = 6,400 (F) | (30−33)×3,000 = 9,000 (A) | **2,600 (A)** |
| Usage = (SQ−AQ)×SP | | (3,000−3,200)×40 = 8,000 (A) | (3,000−3,000)×30 = 0 | **8,000 (A)** |
| Mix = (RSQ−AQ)×SP | | (3,100−3,200)×40 = 4,000 (A) | (3,100−3,000)×30 = 3,000 (F) | **1,000 (A)** |
| Yield = (SQ−RSQ)×SP | | (3,000−3,100)×40 = 4,000 (A) | (3,000−3,100)×30 = 3,000 (A) | **7,000 (A)** |

**Reconciliation:** Price 2,600 (A) + Usage 8,000 (A) = **Cost Variance 10,600 (A)** = ₹2,10,000 − ₹2,20,600. ✓
Mix 1,000 (A) + Yield 7,000 (A) = Usage 8,000 (A). ✓

**Answer:** Material Cost Variance **₹10,600 (A)**; Price ₹2,600 (A); Usage ₹8,000 (A) [Mix ₹1,000 (A) + Yield ₹7,000 (A)].

**Why this way (the reasoning):** Usage variance measures whether we physically consumed more input than the standard *allows for the output actually achieved* — that is why the benchmark is SQ for actual output (3,000 kg each), never the original budgeted batch. Usage then splits into two independent causes. **Mix** isolates the effect of departing from the 50:50 recipe: we compare the actual quantities against what those *same total kilograms* (6,200) would have been if blended in standard proportion (RSQ). **Yield** isolates the effect of the total input differing from what the standard permits: comparing SQ (6,000, the input a good process should have needed) against RSQ (6,200, the input we actually put in, correctly mixed). Here yield is heavily adverse (7,000 A) because we fed 6,200 kg to make output that should have needed only 6,000 — a process loss. The tempting error is to compute mix using RSQ based on *output* rather than *actual total input*; that double-counts the yield loss inside the mix figure. Keeping RSQ tied to actual total input is what makes Mix + Yield collapse exactly back to Usage.

*(Full-marks tip: the examiner rewards (i) SQ built on actual output not budget, (ii) RSQ on actual total input, and (iii) an explicit reconciliation line. Common deduction: mixing up (SP−AP) sign or writing yield as a per-unit-of-output figure without proving Mix+Yield = Usage.)*

---

### Q70. Ch: Standard Costing — Labour Rate, Idle-Time, Efficiency, Mix & Yield Variances (Marks: 10) [Problem]
**Question:** For the output actually achieved in a period, the standard labour allowance and the actual data of a two-grade gang were:

| Grade | Std hours | Std rate (₹/hr) | Hours **paid** | Idle hours | Actual rate (₹/hr) |
|---|---|---|---|---|---|
| Skilled | 4,000 | 50 | 4,200 | 80 | 52 |
| Unskilled | 2,000 | 20 | 2,050 | 50 | 18 |

Compute the labour cost variance and analyse it into **rate, idle-time, efficiency, mix and yield** variances. Reconcile.

**Solution:**

**WN-1 — Hours actually worked = hours paid − idle.**
Skilled worked = 4,200 − 80 = **4,120 hrs**; Unskilled worked = 2,050 − 50 = **2,000 hrs**; total worked = **6,120 hrs.**

**WN-2 — Standard & actual cost.**
- Std cost = 4,000×50 + 2,000×20 = **₹2,40,000**
- Actual cost (on hours paid) = 4,200×52 + 2,050×18 = 2,18,400 + 36,900 = **₹2,55,300**
- **Labour Cost Variance = 2,40,000 − 2,55,300 = ₹15,300 (A)**

**WN-3 — RSH = total hours worked in standard mix (4,000:2,000 = 2:1).**
RSH Skilled = 6,120 × 2/3 = 4,080; RSH Unskilled = 6,120 × 1/3 = 2,040.

**Statement Showing Labour Variances**

| Variance | Formula | Skilled | Unskilled | Total |
|---|---|---|---|---|
| Rate = (SR−AR)×Hrs paid | | (50−52)×4,200 = 8,400 (A) | (20−18)×2,050 = 4,100 (F) | **4,300 (A)** |
| Idle Time = Idle hrs×SR | | 80×50 = 4,000 (A) | 50×20 = 1,000 (A) | **5,000 (A)** |
| Efficiency = (SH−Hrs worked)×SR | | (4,000−4,120)×50 = 6,000 (A) | (2,000−2,000)×20 = 0 | **6,000 (A)** |
| Mix = (RSH−Hrs worked)×SR | | (4,080−4,120)×50 = 2,000 (A) | (2,040−2,000)×20 = 800 (F) | **1,200 (A)** |
| Yield = (SH−RSH)×SR | | (4,000−4,080)×50 = 4,000 (A) | (2,000−2,040)×20 = 800 (A) | **4,800 (A)** |

**Reconciliation:** Rate 4,300 (A) + Idle 5,000 (A) + Efficiency 6,000 (A) = **15,300 (A)** = Cost Variance. ✓
Mix 1,200 (A) + Yield 4,800 (A) = Efficiency 6,000 (A). ✓

**Answer:** LCV **₹15,300 (A)**; Rate 4,300 (A); Idle-Time 5,000 (A); Efficiency 6,000 (A) [Mix 1,200 (A) + Yield 4,800 (A)].

**Why this way (the reasoning):** The single most-penalised trap here is the treatment of idle time. Rate variance is calculated on **hours paid** (we pay the higher/lower rate on every hour we pay for, worked or idle), but efficiency is measured on **hours actually worked** — because you cannot blame a worker's productivity for hours during which the machine stood idle. If you carelessly used "hours paid" in the efficiency formula, the idle-time loss would be buried inside efficiency and double-relieved. Idle-time variance is therefore carved out separately and is **always adverse** (idle hours can never be favourable). Splitting worked-hours-efficiency further: Mix asks "did we deploy skilled vs unskilled in the wrong proportion?" (benchmark RSH = total worked in 2:1), and Yield asks "given a correct blend, did the gang as a whole take more hours than standard?" (benchmark SH vs RSH). The adverse yield reflects that the gang worked 6,120 hrs against a 6,000-hr standard.

*(Full-marks tip: examiners look for rate-on-paid-hours, idle carved out and flagged always-adverse, and efficiency-on-worked-hours. Common deduction: computing rate variance on worked hours, or forgetting Mix+Yield must equal Efficiency.)*

---

### Q71. Ch: Standard Costing — Variable Overhead Variances (Marks: 5) [Problem]
**Question:** A firm absorbs variable overhead on labour hours. Budgeted VOH ₹3,00,000 for 20,000 standard hours (budgeted output 10,000 units at 2 std hrs/unit). Actual output 9,000 units; actual hours worked 18,500; actual VOH incurred ₹2,85,000. Compute the VOH cost variance and split it into **expenditure and efficiency** variances.

**Solution:**

**WN-1 — Standard VOH rate = 3,00,000 ÷ 20,000 = ₹15/hr.**
**WN-2 — Standard hours for actual output = 9,000 × 2 = 18,000 hrs.**
Absorbed VOH = 18,000 × 15 = ₹2,70,000.

| Variance | Formula | ₹ |
|---|---|---|
| VOH Cost | Absorbed − Actual = 2,70,000 − 2,85,000 | **15,000 (A)** |
| VOH Expenditure | (AH×Rate) − Actual = (18,500×15) − 2,85,000 = 2,77,500 − 2,85,000 | **7,500 (A)** |
| VOH Efficiency | (SH−AH)×Rate = (18,000−18,500)×15 | **7,500 (A)** |

Reconciliation: 7,500 (A) + 7,500 (A) = 15,000 (A). ✓

**Answer:** VOH Cost Variance **₹15,000 (A)** = Expenditure ₹7,500 (A) + Efficiency ₹7,500 (A).

**Why this way (the reasoning):** Variable overhead is assumed to vary with activity measured in *hours*. So the expenditure (spending) variance holds hours constant at the actual level (18,500) and asks only "for the hours we actually ran, did we spend more per hour than the ₹15 standard?" — pure rate/price effect. The efficiency variance then asks "did we take more hours than the 18,000 standard allowed for 9,000 units?", valued at the standard rate, because every excess hour drags an extra ₹15 of variable overhead with it. Unlike fixed overhead, VOH has **no volume/capacity/calendar variance** — because variable cost, by definition, flexes with activity, there is no "under-absorption of a fixed pool" to recover. Confusing VOH with FOH and computing a volume variance is the classic error.

*(Full-marks tip: state the two-way split only, and note explicitly "no volume variance for VOH". Deduction for using budgeted hours instead of actual hours in the expenditure line.)*

---

### Q72. Ch: Standard Costing — Fixed Overhead Variances incl. Capacity, Efficiency & Calendar (Marks: 10) [Problem]
**Question:** The following relate to fixed factory overhead:

| Particulars | Budget | Actual |
|---|---|---|
| Output (units) | 10,000 | 9,500 |
| Fixed overhead (₹) | 5,00,000 | 5,20,000 |
| Working days | 25 | 26 |
| Labour hours | 25,000 | 24,000 |

Standard time is 2.5 hrs/unit. Compute the FOH total variance and analyse it fully into **expenditure and volume**, and volume further into **efficiency, capacity and calendar** variances.

**Solution:**

**WN-1 — Standard rates.** Std FOH rate/hour = 5,00,000 ÷ 25,000 = **₹20/hr**; per unit = ₹50. Budgeted hrs/day = 25,000 ÷ 25 = **1,000 hrs/day**; std FOH/day = 5,00,000 ÷ 25 = ₹20,000/day.
**WN-2 — Standard hours for actual output = 9,500 × 2.5 = 23,750 hrs.** Absorbed FOH = 23,750 × 20 = **₹4,75,000.**
**WN-3 — Revised budgeted hours for actual days = 26 × 1,000 = 26,000 hrs.**

| Variance | Formula | ₹ |
|---|---|---|
| FOH Cost | Absorbed − Actual = 4,75,000 − 5,20,000 | **45,000 (A)** |
| Expenditure | Budget − Actual = 5,00,000 − 5,20,000 | **20,000 (A)** |
| Volume | Absorbed − Budget = 4,75,000 − 5,00,000 | **25,000 (A)** |
| — Efficiency | (SH−AH)×Rate = (23,750−24,000)×20 | **5,000 (A)** |
| — Capacity | (AH−Rev. Bud. hrs)×Rate = (24,000−26,000)×20 | **40,000 (A)** |
| — Calendar | (Actual−Budget days)×std FOH/day = (26−25)×20,000 | **20,000 (F)** |

**Reconciliation:** Expenditure 20,000 (A) + Volume 25,000 (A) = **45,000 (A)** ✓. Efficiency 5,000 (A) + Capacity 40,000 (A) + Calendar 20,000 (F) = Volume 25,000 (A) ✓.

**Answer:** FOH Total Variance **₹45,000 (A)** = Expenditure ₹20,000 (A) + Volume ₹25,000 (A); the Volume = Efficiency ₹5,000 (A) + Capacity ₹40,000 (A) + Calendar ₹20,000 (F).

**Why this way (the reasoning):** Fixed overhead is a *fixed pool* that standard costing recovers by pretending it is a rate per hour. Everything flows from one idea: **under-absorption arises whenever we run fewer standard hours than budgeted.** The expenditure variance captures spending more/less than the ₹5,00,000 pool — nothing to do with volume. The volume variance captures the recovery gap, and it has three distinct physical causes: **Calendar** — the factory was *open more days than budgeted* (26 vs 25), so it had extra "budgeted capacity", shown favourable; **Capacity** — despite having 26,000 hrs of available capacity for those 26 days, we actually clocked only 24,000 hrs (idle/under-utilised plant), a large 40,000 adverse; **Efficiency** — of the 24,000 hrs worked, output needed only 23,750 std hours, a small inefficiency. The subtle point is the capacity benchmark: it must be *revised* budgeted hours (26,000) that already give credit for the extra day, otherwise the calendar effect gets double-counted. Miss the calendar variance and your three sub-variances will not reconcile to the volume variance.

*(Full-marks tip: the calendar variance and the *revised* budgeted hours in the capacity line are the discriminators between a rank-holder answer and an average one. Deduction: using 25,000 (original budget) hours in the capacity formula, which swallows the calendar effect.)*

---

### Q73. Ch: Standard Costing — Sales Variances: Price, Volume, Mix & Quantity (Marks: 8) [Problem]
**Question:** A company sells two products. Budget and actual data:

| Product | Budget qty | Std price (₹) | Std cost (₹) | Actual qty | Actual price (₹) |
|---|---|---|---|---|---|
| X | 6,000 | 50 | 40 | 6,500 | 48 |
| Y | 4,000 | 80 | 65 | 4,000 | 85 |

Compute the sales variances under the **turnover (value) method** — total, price and volume, and analyse volume into **mix and quantity**. Reconcile.

**Solution:**

**WN-1 — Budgeted vs actual turnover.**
Budgeted sales = 6,000×50 + 4,000×80 = 3,00,000 + 3,20,000 = ₹6,20,000.
Actual sales = 6,500×48 + 4,000×85 = 3,12,000 + 3,40,000 = ₹6,52,000.
**Total Sales Value Variance = 6,52,000 − 6,20,000 = ₹32,000 (F).**

**WN-2 — RBQ = total actual qty (10,500) in budget mix (6,000:4,000 = 3:2).**
RBQ X = 6,300; RBQ Y = 4,200.

| Variance | Formula | X | Y | Total |
|---|---|---|---|---|
| Price = (AP−SP)×AQ | | (48−50)×6,500 = 13,000 (A) | (85−80)×4,000 = 20,000 (F) | **7,000 (F)** |
| Volume = (AQ−BQ)×SP | | (6,500−6,000)×50 = 25,000 (F) | 0 | **25,000 (F)** |
| Mix = (AQ−RBQ)×SP | | (6,500−6,300)×50 = 10,000 (F) | (4,000−4,200)×80 = 16,000 (A) | **6,000 (A)** |
| Quantity = (RBQ−BQ)×SP | | (6,300−6,000)×50 = 15,000 (F) | (4,200−4,000)×80 = 16,000 (F) | **31,000 (F)** |

**Reconciliation:** Price 7,000 (F) + Volume 25,000 (F) = **32,000 (F)** ✓. Mix 6,000 (A) + Quantity 31,000 (F) = Volume 25,000 (F) ✓.

**Answer (turnover method):** Total Sales Value Variance **₹32,000 (F)**; Price ₹7,000 (F); Volume ₹25,000 (F) [Mix ₹6,000 (A) + Quantity ₹31,000 (F)].

**Why this way (the reasoning):** Sales variances mirror cost variances but reversed in sign logic: for sales a *higher* actual price is **favourable**, so the price formula is (AP − SP), not (SP − AP). The volume variance is valued at **standard selling price** (not std profit) under the turnover method, because we are explaining the change in *revenue*, holding price at standard. The mix/quantity split answers two commercially different questions: **Mix** — did we sell a richer or poorer basket than the planned 3:2? Here we over-sold cheaper X and under-sold dearer Y, so mix is adverse even though total units rose. **Quantity** — did the *total* number of units (correctly weighted) beat budget? Strongly favourable because 10,500 > 10,000 units. A common trap is to value volume at selling price when the question actually wants the **profit/margin method** for profit reconciliation — there volume is valued at *standard profit per unit*. Read which method is asked; the two give different volume figures.

*(Full-marks tip: state clearly "turnover method → volume at std price". Note that for reconciling to budgeted profit you would instead use the margin method: Sales Margin Volume Variance = (AQ−BQ)×std profit = 5,000 (F). Deduction: sign reversal on price, or valuing volume at margin when turnover method is asked.)*

---

### Q74. Ch: Standard Costing — Reconciliation of Budgeted Profit to Actual Profit (Marks: 10) [Problem]
**Question:** A single-product firm has this standard card and budget:

| Element | Std per unit (₹) |
|---|---|
| Direct material (3 kg @ ₹20) | 60 |
| Direct labour (2 hr @ ₹30) | 60 |
| Variable OH (2 hr @ ₹10) | 20 |
| Fixed OH (2 hr @ ₹15) | 30 |
| **Total cost** | **170** |
| Profit | 30 |
| **Selling price** | **200** |

Budgeted output & sales = 10,000 units (budgeted FOH ₹3,00,000). **Actual:** produced & sold 9,000 units for ₹18,45,000; materials 28,000 kg costing ₹5,88,000; labour 17,500 hrs (no idle) costing ₹5,42,500; VOH ₹1,80,000; FOH ₹3,20,000. Prepare a **statement reconciling budgeted profit with actual profit** through all variances.

**Solution:**

**WN-1 — Budgeted profit = 10,000 × 30 = ₹3,00,000.** Actual profit = 18,45,000 − (5,88,000+5,42,500+1,80,000+3,20,000) = 18,45,000 − 16,30,500 = **₹2,14,500.**
**WN-2 — Standards for 9,000 units:** material SQ 27,000 kg; labour/VOH SH 18,000 hrs; FOH absorbed 9,000×30 = 2,70,000.

**WN-3 — Variances.**
- **Material:** Price (20−21)×28,000 = 28,000 (A); Usage (27,000−28,000)×20 = 20,000 (A).
- **Labour:** Rate (30−31)×17,500 = 17,500 (A); Efficiency (18,000−17,500)×30 = 15,000 (F).
- **VOH:** Expenditure (17,500×10−1,80,000) = 5,000 (A); Efficiency (18,000−17,500)×10 = 5,000 (F).
- **FOH:** Expenditure (3,00,000−3,20,000) = 20,000 (A); Volume (2,70,000−3,00,000) = 30,000 (A).
- **Sales:** Price (205−200)×9,000 = 45,000 (F); Sales Margin Volume (9,000−10,000)×30 = 30,000 (A).

**Statement Reconciling Budgeted Profit to Actual Profit**

| Particulars | (F) ₹ | (A) ₹ | ₹ |
|---|---|---|---|
| **Budgeted profit** | | | **3,00,000** |
| Sales margin volume variance | | 30,000 | |
| Sales price variance | 45,000 | | |
| Material price | | 28,000 | |
| Material usage | | 20,000 | |
| Labour rate | | 17,500 | |
| Labour efficiency | 15,000 | | |
| VOH expenditure | | 5,000 | |
| VOH efficiency | 5,000 | | |
| FOH expenditure | | 20,000 | |
| FOH volume | | 30,000 | |
| **Sub-totals** | **65,000** | **1,50,500** | (85,500) |
| **Actual profit** | | | **2,14,500** |

**Answer:** Budgeted profit ₹3,00,000 − net adverse variances ₹85,500 = **Actual profit ₹2,14,500.** ✓

**Why this way (the reasoning):** A profit reconciliation must use the **sales margin volume variance (valued at standard profit ₹30), never the turnover volume variance (valued at ₹200)** — this is the single biggest trap. Reason: we start from *budgeted profit*, so every bridging item must be expressed in *profit* terms. If you selling below budget by 1,000 units, you lose only the *profit* of ₹30 on each (₹30,000), not the whole ₹200 of revenue — the variable costs on those unmade units were never incurred, so they cannot be a loss. Similarly the FOH volume variance already captures the under-recovery of fixed cost from making fewer units, so bringing in a revenue-based volume figure would double-count. The reconciliation is a proof of arithmetic honesty: if it does not tie to the independently computed actual profit (₹2,14,500 from the P&L), a variance has the wrong sign or the wrong valuation base.

*(Full-marks tip: examiners award the marks for (i) using sales *margin* volume, (ii) tying to an independently computed actual profit, and (iii) a two-column F/A layout. Deduction: using turnover volume (₹2,00,000) which blows the reconciliation apart.)*

---

### Q75. Ch: Standard Costing — Reverse Working from Given Variances (Idle Time) (Marks: 8) [Problem]
**Question:** For the output actually achieved, a firm's **standard labour** allowance was **8,000 hours at ₹40/hour**. Only the following labour variances are known:

| Variance | Amount |
|---|---|
| Labour Rate Variance | ₹23,100 (A) |
| Idle Time Variance | ₹8,000 (A) |
| Labour Efficiency Variance | ₹20,000 (F) |

Working backwards, determine: (i) idle hours, (ii) actual hours worked, (iii) actual hours paid, (iv) actual wage rate, and (v) total actual wages. Verify with the labour cost variance.

**Solution:**

**WN-1 — Idle hours** (Idle Time Variance = Idle hrs × SR):
8,000 = Idle × 40 → **Idle hours = 200.**

**WN-2 — Actual hours worked** (Efficiency = (SH − Hrs worked) × SR):
+20,000 = (8,000 − Worked) × 40 → 8,000 − Worked = 500 → **Hrs worked = 7,500.**

**WN-3 — Actual hours paid** = worked + idle = 7,500 + 200 = **7,700 hrs.**

**WN-4 — Actual wage rate** (Rate = (SR − AR) × Hrs paid):
−23,100 = (40 − AR) × 7,700 → (40 − AR) = −3 → **AR = ₹43/hr.**

**WN-5 — Total actual wages** = 7,700 × 43 = **₹3,31,100.**

**Verification:** Std cost = 8,000 × 40 = ₹3,20,000. LCV = 3,20,000 − 3,31,100 = **₹11,100 (A).** Cross-check: Rate 23,100 (A) + Idle 8,000 (A) + Efficiency 20,000 (F) = ₹11,100 (A). ✓

**Answer:** Idle 200 hrs; worked 7,500 hrs; paid 7,700 hrs; actual rate ₹43/hr; actual wages ₹3,31,100; LCV ₹11,100 (A).

**Why this way (the reasoning):** Reverse variance problems test whether you truly understand which *base quantity* each formula sits on, because you must invert the exact relationship. The order is forced by dependency: idle-time variance depends only on idle hours and SR, so it is solved first and in isolation. Efficiency depends on **hours worked** (not paid), giving the worked figure. Only then can you reconstruct hours *paid* (worked + idle) — and this matters because the **rate variance is computed on hours paid**. Feeding "hours worked" into the rate inversion would give the wrong actual rate. The favourable efficiency but adverse everything-else tells a story: the gang was fast when working (took 7,500 hrs for an 8,000-hr job) but expensive (₹43 vs ₹40) and lost 200 idle hours — a realistic pattern where a high-skill, high-wage crew is efficient yet suffers downtime.

*(Full-marks tip: state the base of each formula explicitly and solve in dependency order. Deduction: using hours worked in the rate inversion, or forgetting idle-time is always adverse so its sign is fixed.)*

---

### Q76. Ch: Standard Costing — Interdependence of Variances (Marks: 5) [Case/Application]
**Question:** A purchase manager proudly reports a large **favourable material price variance** for the quarter and claims a bonus. In the same quarter the production manager's report shows a large **adverse material usage variance** and an adverse **labour efficiency variance**, and the quality department reports higher rejections. Examine the validity of the purchase manager's claim and explain, with the governing principle, how these variances may be interrelated. What control action do you advise?

**Answer:**

**Governing principle — interdependence of variances.** Standard-costing variances are *not* independent silos; a decision taken in one responsibility centre routinely spills into another. Responsibility for a favourable variance can therefore be illusory if it *caused* adverse variances elsewhere that outweigh it.

**Application to the facts.** The most probable explanation is that the purchase manager bought **cheaper, sub-standard material** to earn the favourable price variance. Inferior material:
- Requires **more quantity** to produce the same good output (breakages, scrap) → adverse **material usage/yield** variance in production;
- Is **harder to work with**, so operatives take longer per unit → adverse **labour efficiency** variance; and
- Produces more **rejections** → the quality report corroborates the linkage.

Thus the favourable price variance and the adverse usage/efficiency/quality outcomes share a **single root cause** located in the purchase function, not the production function.

**Weighing the two views.** *View favouring the claim:* if the price fall were due to genuine market softening or bulk-discount negotiation with no quality drop, the favourable variance is a real gain and controllable by purchasing. *View against:* the simultaneous, correlated adverse usage/labour/quality signals point to quality compromise. The decisive test is the **net effect** — compare the favourable price variance against the sum of the adverse usage, labour and rejection costs it triggered. Only if the price saving exceeds the induced adverse costs is the firm better off.

**Conclusion/Advice.** The claim cannot be accepted at face value. Management should (i) investigate whether the price gain came from a quality reduction, (ii) net the price variance against the induced adverse variances before crediting the purchase manager, and (iii) revise the material specification/vendor rating so cost control does not degrade quality. Bonus should rest on **net favourable impact**, not an isolated price variance.

**Why this way (the reasoning):** The whole point of variance analysis is *control through responsibility accounting*, and control fails if a manager can be rewarded for a locally favourable number that destroys value globally. Recognising that price ↔ usage ↔ efficiency ↔ quality are causally linked prevents "gaming" of the system. The examiner wants you to reject the mechanical, single-variance view and reason about root cause and net effect — the same principle underlies why a favourable variance is not automatically "good" and an adverse one not automatically "bad".

*(Full-marks tip: name the principle "interdependence/interrelationship of variances", give the concrete cheaper-material mechanism, and insist on netting before assigning responsibility. Deduction: merely defining price and usage variance without linking them causally.)*

---

### Q77. Ch: Marginal Costing — Multi-Product Break-Even & Effect of Sales Mix (Marks: 10) [Problem]
**Question:** A company sells three products in a fixed sales mix of **4 : 3 : 3 (by units)**:

| Product | Selling price (₹) | Variable cost (₹) | Contribution (₹) |
|---|---|---|---|
| A | 100 | 60 | 40 |
| B | 80 | 50 | 30 |
| C | 50 | 30 | 20 |

Total fixed cost is **₹6,20,000**. Required: (i) composite break-even point in units and in value; (ii) sales (units & value) to earn a target profit of ₹3,10,000; and (iii) recompute the break-even units **if the mix shifted to 1 : 1 : 1** — and explain the movement.

**Solution:**

**WN-1 — Build a "standard batch" of 10 units in ratio 4:3:3.**
- Contribution/batch = 4×40 + 3×30 + 3×20 = 160 + 90 + 60 = **₹310**
- Revenue/batch = 4×100 + 3×80 + 3×50 = 400 + 240 + 150 = **₹790**
- Composite P/V ratio = 310 ÷ 790 = **39.24%**

**(i) Break-even.**
BEP (batches) = Fixed ÷ contribution per batch = 6,20,000 ÷ 310 = **2,000 batches.**

| Product | BEP units | BEP value (₹) |
|---|---|---|
| A (4×2,000) | 8,000 | 8,00,000 |
| B (3×2,000) | 6,000 | 4,80,000 |
| C (3×2,000) | 6,000 | 3,00,000 |
| **Total** | **20,000** | **15,80,000** |

Check: Fixed ÷ P/V = 6,20,000 ÷ 0.3924 = ₹15,80,000. ✓

**(ii) Target profit ₹3,10,000.**
Batches = (6,20,000 + 3,10,000) ÷ 310 = 9,30,000 ÷ 310 = **3,000 batches** → A 12,000, B 9,000, C 9,000 units (**30,000 units**); sales value = 3,000 × 790 = **₹23,70,000.**

**(iii) Mix changes to 1:1:1 (batch of 3 units).**
Contribution/batch = 40 + 30 + 20 = ₹90. BEP batches = 6,20,000 ÷ 90 = **6,888.9 batches → 6,889 units each of A, B, C ≈ 20,667 units** (vs 20,000 before).

**Answer:** BEP = 20,000 units / ₹15,80,000; for ₹3,10,000 profit sell 30,000 units / ₹23,70,000; on a 1:1:1 mix BEP rises to ≈20,667 units.

**Why this way (the reasoning):** There is no single break-even for a multi-product firm — break-even is **defined only for a given sales mix**. The "batch" (or weighted-average contribution) technique works because holding the mix constant lets us treat the whole basket as one composite product with a blended contribution and a blended P/V ratio. The BEP-in-value check via composite P/V ratio must agree with the units route; if it doesn't, the mix weighting is wrong. Part (iii) delivers the conceptual punch: shifting from 4:3:3 toward 1:1:1 *raises* the break-even because the mix now carries proportionately more of the low-contribution product C and less of high-contribution A, dragging the average contribution per batch down (₹31/unit → ₹30/unit). This is why a firm can "hit its unit target yet miss break-even" if the mix deteriorates — volume alone never guarantees profit; **contribution mix does.**

*(Full-marks tip: show both the batch method and the composite P/V cross-check, and explicitly attribute the BEP shift to the change in weighted contribution. Deduction: giving a single BEP without stating "for the given mix", or averaging P/V ratios of products directly instead of weighting by the sales basket.)*

---

### Q78. Ch: Marginal Costing — Shut-Down Point with Capacity Analysis (Marks: 8) [Problem]
**Question:** A seasonal manufacturer is deciding whether to **shut down** during the lean quarter. Data (annualised): selling price ₹50/unit, variable cost ₹30/unit; total fixed cost ₹8,00,000 p.a., of which **₹3,00,000 is unavoidable** (continues even if shut). Shutting down triggers additional one-off costs (retrenchment + reopening + maintenance) of **₹50,000**. Full capacity is **60,000 units p.a.** Expected lean-season demand is **18,000 units**. Compute the **shut-down point (units, value and as % of capacity)** and advise, supporting the advice with a comparative statement.

**Solution:**

**WN-1 — Contribution & avoidable fixed cost.**
Contribution/unit = 50 − 30 = ₹20; P/V ratio = 40%.
Avoidable fixed cost (saved by shutting) = 8,00,000 − 3,00,000 = ₹5,00,000.
**Net saving from shutting** = 5,00,000 − 50,000 additional shut-down cost = **₹4,50,000.**

**WN-2 — Shut-down point.**
= Net avoidable fixed cost ÷ contribution per unit = 4,50,000 ÷ 20 = **22,500 units.**
In value = 4,50,000 ÷ 0.40 = **₹11,25,000.**
As % of capacity = 22,500 ÷ 60,000 = **37.5%.**

**Interpretation:** if expected volume **exceeds 22,500 units → continue**; if **below → shut down.** Expected demand 18,000 units (30% capacity) < 22,500 → **shut down.**

**Comparative Statement (lean quarter)**

| Particulars | Continue (18,000 u) | Shut down |
|---|---|---|
| Contribution (18,000 × 20) | 3,60,000 | — |
| Less: Fixed cost | 8,00,000 | 3,00,000 |
| Less: Additional shut-down cost | — | 50,000 |
| **Loss** | **(4,40,000)** | **(3,50,000)** |

Shutting reduces the loss by **₹90,000.**

**Answer:** Shut-down point = **22,500 units / ₹11,25,000 / 37.5% of capacity.** As expected demand (18,000 units) is below this, **shut down** — it saves ₹90,000.

**Why this way (the reasoning):** A shut-down decision is *not* the same as a break-even decision. At break-even you cover *all* fixed costs; a firm operating below break-even is still often better off staying open, because staying open contributes toward the fixed costs that will be incurred *anyway*. The right comparison is only the **avoidable** fixed cost — the ₹3,00,000 unavoidable cost is irrelevant to the choice because it is incurred under both options and cancels out. Crucially, we must *net off* the extra ₹50,000 that shutting itself costs; ignoring it overstates the benefit of shutting. The shut-down point (22,500 units) is the volume at which the contribution earned by continuing exactly equals the net fixed cost saved by closing. Above it, contribution more than covers avoidable cost → keep running to absorb overheads; below it, the contribution is too thin to justify the avoidable costs of staying open → shut. Beginners wrongly use total fixed cost (₹8,00,000) in the numerator, giving a false shut-down point of 40,000 units and the wrong advice.

*(Full-marks tip: use *net avoidable* fixed cost in the numerator, express the point as a capacity %, and prove the recommendation with a two-column loss comparison. Deduction: using total fixed cost, or ignoring the additional shut-down cost.)*

---

### Q79. Ch: Marginal Costing — Make-or-Buy with Avoidable Fixed Cost & Opportunity Cost (Marks: 10) [Problem]
**Question:** A firm makes 10,000 units p.a. of component "K" in-house. The unit cost sheet is:

| Element | ₹/unit |
|---|---|
| Direct material | 30 |
| Direct labour | 20 |
| Variable overhead | 10 |
| Fixed overhead (absorbed) | 15 |
| **Total** | **75** |

A supplier offers component K at **₹62/unit**. Of the fixed overhead, only **₹10,000 p.a. is specific to K (avoidable if outsourced)**; the rest is general plant overhead that will continue. (a) On cost grounds, should the firm make or buy? (b) If outsourcing frees capacity that can be used to earn a **contribution of ₹25,000 p.a.** from another product, does the decision change?

**Solution:**

**WN-1 — Relevant cost to MAKE (per annum).**
Variable cost = (30+20+10) × 10,000 = 60 × 10,000 = ₹6,00,000
Add: avoidable (specific) fixed cost = ₹10,000
**Relevant make cost = ₹6,10,000 → ₹61/unit.**
(General fixed overhead ₹1,40,000 is ignored — it continues whether we make or buy.)

**WN-2 — Cost to BUY = 10,000 × ₹62 = ₹6,20,000.**

**(a) Statement of Relevant Costs — Make vs Buy**

| Particulars | Make (₹) | Buy (₹) |
|---|---|---|
| Variable manufacturing cost | 6,00,000 | — |
| Avoidable specific fixed cost | 10,000 | — |
| Purchase price | — | 6,20,000 |
| **Relevant cost** | **6,10,000** | **6,20,000** |

Making is cheaper by **₹10,000 → MAKE.**

**(b) Add opportunity cost of the released capacity.**
If bought, the freed facilities earn ₹25,000. So the true cost of *making* = 6,10,000 + 25,000 opportunity cost forgone = **₹6,35,000**, versus buy ₹6,20,000. **Now BUY** — buying is better by ₹15,000.

**Answer:** (a) **Make** — saves ₹10,000. (b) With an alternative contribution of ₹25,000 from freed capacity, **buy** — better by ₹15,000.

**Why this way (the reasoning):** The whole cost sheet is a trap. The naïve comparison — buy ₹62 vs make ₹75 — screams "buy, save ₹13/unit". But ₹75 includes ₹15 of absorbed fixed overhead, ₹14 of which is **general overhead that does not disappear if we stop making K**. Only *relevant* (differential) costs belong in a decision: the variable cost that vanishes if we outsource, plus the ₹1/unit of fixed cost that is genuinely specific/avoidable. On that basis making costs only ₹61 — *below* the ₹62 buy price — so the correct answer reverses the naïve one: **make.** Part (b) introduces the second layer: capacity is a scarce resource. If outsourcing releases capacity that can earn ₹25,000 elsewhere, then continuing to make *sacrifices* that ₹25,000 — an **opportunity cost** that must be added to the make option. Once it exceeds the ₹10,000 make-saving, the decision flips again to buy. This staged reasoning — relevant cost first, opportunity cost second — is the hallmark of a correct make-or-buy analysis.

*(Full-marks tip: explicitly exclude general fixed overhead, include only avoidable fixed, and treat freed-capacity contribution as an opportunity cost on the *make* side. Deduction: comparing full cost ₹75 to ₹62, or adding the ₹25,000 to the buy column instead of the make column.)*

---

### Q80. Ch: Marginal Costing — Key-Factor (Limiting-Factor) Decision with Constraints (Marks: 8) [Problem]
**Question:** A firm makes three products, all requiring the same scarce machine. Only **20,000 machine hours** are available next period.

| Product | Contribution/unit (₹) | Machine hrs/unit | Max market demand (units) |
|---|---|---|---|
| P | 40 | 2 | 4,000 |
| Q | 60 | 4 | 3,000 |
| R | 30 | 1 | 5,000 |

There is a **contractual obligation to supply at least 1,000 units of Q**. Fixed cost is ₹2,00,000. Determine the profit-maximising production plan and the resulting profit.

**Solution:**

**WN-1 — Contribution per machine hour (the key factor) and ranking.**

| Product | Contribution/hr | Rank |
|---|---|---|
| P | 40 ÷ 2 = ₹20 | II |
| Q | 60 ÷ 4 = ₹15 | III |
| R | 30 ÷ 1 = ₹30 | I |

**WN-2 — Allocate 20,000 hours by rank, honouring the contractual minimum first.**
- Contractual Q: 1,000 units × 4 = 4,000 hrs (reserved) → left 16,000
- Rank I — R: 5,000 units × 1 = 5,000 hrs → left 11,000
- Rank II — P: 4,000 units × 2 = 8,000 hrs → left 3,000
- Rank III — Q (balance): 3,000 hrs ÷ 4 = 750 more units → total Q = 1,750 units

**Statement of Optimum Product Mix**

| Product | Units | Machine hrs | Contribution (₹) |
|---|---|---|---|
| R | 5,000 | 5,000 | 1,50,000 |
| P | 4,000 | 8,000 | 1,60,000 |
| Q | 1,750 | 7,000 | 1,05,000 |
| **Total** | | **20,000** | **4,15,000** |
| Less: Fixed cost | | | 2,00,000 |
| **Profit** | | | **2,15,000** |

**Answer:** Produce **R 5,000, P 4,000, Q 1,750 units**; total contribution ₹4,15,000; **profit ₹2,15,000.**

**Why this way (the reasoning):** When a resource is scarce, ranking by **contribution per unit** is wrong — it maximises contribution per *product* but not per *scarce hour*. Q has the highest contribution per unit (₹60) yet the **lowest per machine hour (₹15)** because it devours 4 hours each; R, the "smallest" product per unit, earns the most per hour (₹30). The scarce resource is what we are really economising, so we rank by **contribution per unit of the limiting factor** and load the machine with the highest-yielding products first. The contractual minimum overrides pure ranking: we must ring-fence 1,000 units of Q (4,000 hrs) *before* free allocation, even though Q ranks last, because breaching a contract carries penalties/loss of goodwill outside this contribution calculus. Only the residual capacity is then optimised. Ignoring the contractual floor and simply filling by rank would leave Q at 750 units and breach the obligation.

*(Full-marks tip: rank on contribution-per-key-factor, satisfy the contractual minimum first, and stop each product at its market-demand ceiling. Deduction: ranking by contribution per unit, or exceeding a product's max demand.)*

---

### Q81. Ch: Marginal Costing — Accept/Reject Special Order with Capacity Constraint (Marks: 10) [Problem]
**Question:** A firm has a capacity of **1,00,000 units** and currently produces & sells **70,000 units** at ₹200 each. Costs: variable ₹120/unit; fixed ₹40,00,000 p.a. A foreign buyer offers a one-time export order at **₹150/unit**, and the order needs a special modification costing **₹5/unit** plus one-off tooling of **₹1,00,000**. Evaluate acceptance if the order is for (a) **20,000 units**, and (b) **40,000 units** (the domestic price/market is protected from the export price). Advise.

**Solution:**

**WN-1 — Spare capacity = 1,00,000 − 70,000 = 30,000 units.**
Incremental contribution/unit on the order = 150 − 120 − 5 = **₹25.**

**(a) Order of 20,000 units (within 30,000 spare — no displacement).**

| Particulars | ₹ |
|---|---|
| Incremental contribution (20,000 × 25) | 5,00,000 |
| Less: One-off tooling | 1,00,000 |
| **Net incremental gain** | **4,00,000** |

Fixed cost unchanged (90,000 ≤ capacity). **Accept** → profit rises ₹4,00,000.

**(b) Order of 40,000 units (exceeds spare by 10,000 → displaces regular sales).**

| Particulars | ₹ |
|---|---|
| Incremental contribution (40,000 × 25) | 10,00,000 |
| Less: Contribution lost on 10,000 displaced regular units (200−120)×10,000 | 8,00,000 |
| Less: One-off tooling | 1,00,000 |
| **Net incremental gain** | **1,00,000** |

**Accept** — but the margin is thin (₹1,00,000).

**Answer:** (a) Accept — gain ₹4,00,000. (b) Accept — gain only ₹1,00,000, because 10,000 units of profitable domestic sales are sacrificed.

**Why this way (the reasoning):** A special order is a classic *relevant-cost* decision, and the two traps are opposite in direction. **Trap 1 (reject wrongly):** the export price ₹150 is below the full cost of ₹120 + ₹40 fixed = ₹160, tempting rejection. But existing fixed costs are already committed and are covered by the regular business, so they are *irrelevant* to spare-capacity output — the order only needs to beat its *incremental* cost (₹125), and ₹150 does, adding ₹25 each. **Trap 2 (accept blindly):** once the order exceeds spare capacity, the extra units can only be made by **giving up regular sales**, so the lost contribution of ₹80/unit on those displaced units becomes an **opportunity cost** of the order. In (b) this opportunity cost (₹8,00,000) almost wipes out the gain. So capacity is the hinge: within spare capacity, judge against incremental cost; beyond it, add the opportunity cost of displaced business. Qualitatively one should also flag risks — dumping/anti-dumping exposure and the danger of the export price leaking into the domestic market — before final acceptance.

*(Full-marks tip: separate the within-capacity and displacement portions, cost the displaced units at *lost contribution* (₹80) not at full price, and mention the qualitative price-erosion/dumping risk. Deduction: rejecting because ₹150 < full cost ₹160, or ignoring displacement in part (b).)*

---

### Q82. Ch: Marginal Costing — CVP: Price-Cut Proposal, P/V Ratio & Margin of Safety (Marks: 8) [Problem]
**Question:** A company's current position: selling price ₹100/unit, variable cost ₹60/unit, sales 40,000 units, fixed cost ₹12,00,000. Marketing proposes **cutting the selling price by 10%**, expecting unit volume to rise **25%**. (i) Compute present profit, P/V ratio, BEP, margin of safety and degree of operating leverage; (ii) evaluate the proposal; (iii) find the volume increase actually required to *maintain* present profit at the reduced price, and advise.

**Solution:**

**WN-1 — Present position.**
Contribution/unit = 100 − 60 = ₹40; P/V ratio = 40%.
Contribution = 40,000 × 40 = ₹16,00,000; **Profit = 16,00,000 − 12,00,000 = ₹4,00,000.**
BEP = 12,00,000 ÷ 40 = **30,000 units (₹30,00,000).**
Margin of safety = 40,000 − 30,000 = 10,000 units = **25% of sales.**
Degree of operating leverage = Contribution ÷ Profit = 16,00,000 ÷ 4,00,000 = **4.0.**

**WN-2 — Under the proposal.**
New SP = ₹90; VC unchanged ₹60 → new contribution/unit = ₹30 (new P/V = 33.33%).
New volume = 40,000 × 1.25 = 50,000 units.
New contribution = 50,000 × 30 = ₹15,00,000 → **Profit = 15,00,000 − 12,00,000 = ₹3,00,000.**
Profit *falls* by ₹1,00,000. **Reject.**

**WN-3 — Volume needed to hold ₹4,00,000 profit at ₹90 price.**
Required units = (12,00,000 + 4,00,000) ÷ 30 = **53,333 units** — an increase of 33.3%, well above the 25% expected.

**Answer:** Present profit ₹4,00,000, P/V 40%, BEP 30,000 units, MoS 25%, DOL 4.0. The proposal *lowers* profit to ₹3,00,000 → **reject**; holding profit would need +33.3% volume, not the +25% expected.

**Why this way (the reasoning):** The seductive error is to assume "more units = more profit". A price cut attacks profit through the **contribution per unit and hence the P/V ratio** — cutting price ₹10 while variable cost stays at ₹60 slashes contribution from ₹40 to ₹30 (a 25% fall in unit contribution) and the P/V ratio from 40% to 33.3%. For total contribution to merely stand still, the *percentage rise in volume must exceed the percentage fall in contribution per unit* — here volume must grow ~33% just to offset a 25% margin cut, so a 25% volume rise leaves the firm worse off. The degree of operating leverage (4.0) reinforces the danger: with high leverage, profit is highly sensitive to contribution, so eroding contribution is especially costly. The disciplined method is to rebuild contribution per unit *after* the price change and re-solve, never to reason from revenue or units alone.

*(Full-marks tip: recompute the P/V ratio after the price cut and compare the required vs expected volume growth explicitly. Deduction: applying the old ₹40 contribution to the new volume, or judging the proposal on turnover rather than profit.)*

---

### Q83. Ch: Marginal Costing — Drop-a-Product (Segment) Decision (Marks: 8) [Problem]
**Question:** Under absorption costing, Product C shows a loss and management wants to drop it:

| Particulars (₹) | A | B | C | Total |
|---|---|---|---|---|
| Sales | 5,00,000 | 3,00,000 | 2,00,000 | 10,00,000 |
| Variable cost | 3,00,000 | 2,00,000 | 1,50,000 | 6,50,000 |
| **Contribution** | **2,00,000** | **1,00,000** | **50,000** | **3,50,000** |
| Fixed cost (apportioned) | 1,20,000 | 90,000 | 90,000 | 3,00,000 |
| **Profit/(Loss)** | 80,000 | 10,000 | **(40,000)** | 50,000 |

Of C's ₹90,000 apportioned fixed cost, only **₹30,000 is specific to C (avoidable on dropping it)**; the balance is common overhead reapportioned to A and B. Advise whether to drop Product C, with supporting statements.

**Solution:**

**WN-1 — Relevant effect of dropping C.**
- Contribution lost = ₹50,000
- Fixed cost saved (avoidable only) = ₹30,000
- **Net loss on dropping C = 50,000 − 30,000 = ₹20,000.**

**Statement of Total Profit — Keep vs Drop C**

| Particulars (₹) | Keep C | Drop C |
|---|---|---|
| Contribution: A + B | 3,00,000 | 3,00,000 |
| Contribution: C | 50,000 | — |
| **Total contribution** | **3,50,000** | **3,00,000** |
| Less: Fixed cost | 3,00,000 | 2,70,000 |
| **Profit** | **50,000** | **30,000** |

Dropping C reduces total profit by **₹20,000.**

**Answer:** **Do not drop Product C.** It earns ₹50,000 contribution but only ₹30,000 of its overhead is avoidable, so it still contributes ₹20,000 toward common fixed costs; dropping it would cut total profit from ₹50,000 to ₹30,000.

**Why this way (the reasoning):** The reported ₹40,000 "loss" on C is a bookkeeping artefact of **apportioning common fixed cost**, not an economic loss. The correct test for keeping a segment is whether its **contribution exceeds its avoidable (segment-specific) fixed cost** — not whether it shows a net profit after arbitrary overhead allocation. Here C's ₹50,000 contribution comfortably exceeds its ₹30,000 avoidable fixed cost, so it makes a positive ₹20,000 contribution toward the ₹60,000 of *common* overhead that will *not* disappear if C goes. If C is dropped, that ₹60,000 does not vanish — it simply gets reapportioned onto A and B, worsening *their* apparent performance while total profit falls. The disciplined marginal-costing view strips away apportioned common cost and looks only at differential contribution and avoidable cost. Only if C's specific avoidable fixed cost had exceeded its contribution (or the freed capacity had a more profitable use) would dropping it be justified.

*(Full-marks tip: separate avoidable from common fixed cost, compute the net effect, and show a whole-company keep-vs-drop profit statement proving the ₹20,000 fall. Deduction: dropping C on the strength of the ₹40,000 allocated "loss".)*

---

### Q84. Ch: Marginal Costing — Marginal vs Absorption Costing Profit Reconciliation (Marks: 6) [Problem]
**Question:** In its first period a firm **produced 12,000 units and sold 10,000 units** (no opening stock). Selling price ₹100; variable manufacturing cost ₹50/unit; variable selling cost ₹5/unit; fixed manufacturing overhead ₹2,40,000 (absorbed on normal capacity of 12,000 units); fixed selling overhead ₹60,000. Compute profit under (i) **marginal costing** and (ii) **absorption costing**, and **reconcile** the difference, explaining its cause.

**Solution:**

**WN-1 — Fixed manufacturing OH absorption rate = 2,40,000 ÷ 12,000 = ₹20/unit.** Closing stock = 12,000 − 10,000 = 2,000 units.

**(i) Marginal Costing — Statement of Profit**

| Particulars | ₹ |
|---|---|
| Sales (10,000 × 100) | 10,00,000 |
| Less: Variable mfg cost (10,000 × 50) | 5,00,000 |
| Less: Variable selling (10,000 × 5) | 50,000 |
| **Contribution** | **4,50,000** |
| Less: Fixed mfg OH | 2,40,000 |
| Less: Fixed selling OH | 60,000 |
| **Profit** | **1,50,000** |

*(Closing stock valued at variable cost only: 2,000 × 50 = ₹1,00,000.)*

**(ii) Absorption Costing — Statement of Profit**

| Particulars | ₹ |
|---|---|
| Sales | 10,00,000 |
| Cost of production (12,000 × 70) | 8,40,000 |
| Less: Closing stock (2,000 × 70) | (1,40,000) |
| Cost of goods sold | 7,00,000 |
| **Gross profit** | **3,00,000** |
| Less: Variable selling (10,000 × 5) | 50,000 |
| Less: Fixed selling OH | 60,000 |
| **Profit** | **1,90,000** |

*(No under/over absorption: production 12,000 = normal capacity, so absorbed FOH = actual ₹2,40,000.)*

**WN-2 — Reconciliation.**
Difference = 1,90,000 − 1,50,000 = **₹40,000** = fixed manufacturing OH carried in closing stock = 2,000 units × ₹20 = ₹40,000.

| Reconciliation | ₹ |
|---|---|
| Profit (marginal costing) | 1,50,000 |
| Add: Fixed mfg OH in closing stock (2,000 × 20) | 40,000 |
| **Profit (absorption costing)** | **1,90,000** |

**Answer:** Marginal profit ₹1,50,000; absorption profit ₹1,90,000; difference ₹40,000 = fixed manufacturing overhead deferred in closing inventory.

**Why this way (the reasoning):** The two systems differ in exactly one respect — the treatment of **fixed manufacturing overhead**. Marginal costing treats it as a **period cost**, expensing the full ₹2,40,000 in the period it arises. Absorption costing treats it as a **product cost**, attaching ₹20 to every unit; so when 2,000 units remain unsold, ₹40,000 of fixed overhead is *carried forward* inside closing stock (the ₹70 stock value vs ₹50 under marginal) rather than expensed now. That is why, **when production exceeds sales (stock rises), absorption profit is higher** by the fixed overhead lodged in the inventory increase — and the reverse when stocks fall. The reconciliation is simply the change in stock units × the fixed-overhead-per-unit. Note also that fixed *selling* overhead is a period cost under *both* methods, so only fixed *manufacturing* overhead drives the difference — a point students routinely get wrong by trying to defer selling overhead into stock too.

*(Full-marks tip: value closing stock at ₹50 (marginal) vs ₹70 (absorption), reconcile via stock-change × fixed-mfg-OH-rate, and note that fixed selling overhead never enters stock. Deduction: including variable/fixed selling cost in inventory valuation, or misstating which method gives the higher profit when stocks rise.)*

### Q85. Ch: Budgets & Budgetary Control — Flexible Budget at Multiple Activity Levels (Marks: 10) [Problem]
**Question:** A manufacturing company's 100% capacity is 10,000 units per month. Prepare a flexible budget showing total cost, cost per unit and profit at **60%, 80% and 100%** capacity, given the data below and a uniform selling price of ₹280 per unit.

| Element | Behaviour / Amount |
|---|---|
| Direct materials | ₹100 per unit (variable) |
| Direct labour | ₹40 per unit (variable) |
| Variable overheads | ₹30 per unit (variable) |
| Fixed overheads | ₹3,00,000 per month (constant) |
| Semi-variable overheads | ₹2,00,000 at 60% capacity; rise by 10% between 60% and 80%; rise by a further 20% between 80% and 100% |
| Selling price | ₹280 per unit |

**Solution:**

**WN-1 — Output at each level:** 60% = 6,000 u; 80% = 8,000 u; 100% = 10,000 u.

**WN-2 — Semi-variable overhead at each level (this is the trap — it is neither pure fixed nor pure variable):**
- 60%: ₹2,00,000
- 80%: ₹2,00,000 × 1.10 = ₹2,20,000
- 100%: ₹2,20,000 × 1.20 = ₹2,64,000

**WN-3 — Variable cost per unit** = 100 + 40 + 30 = **₹170**.

**Flexible Budget (Statement Showing Cost and Profit at Different Capacities):**

| Particulars | 60% (6,000 u) | 80% (8,000 u) | 100% (10,000 u) |
|---|---|---|---|
| Sales @ ₹280 | 16,80,000 | 22,40,000 | 28,00,000 |
| Variable cost @ ₹170 | 10,20,000 | 13,60,000 | 17,00,000 |
| Semi-variable OH (WN-2) | 2,00,000 | 2,20,000 | 2,64,000 |
| Fixed overheads | 3,00,000 | 3,00,000 | 3,00,000 |
| **Total cost** | **15,20,000** | **18,80,000** | **22,64,000** |
| **Profit (Sales − Cost)** | **1,60,000** | **3,60,000** | **5,36,000** |
| **Cost per unit (₹)** | **253.33** | **235.00** | **226.40** |

**Answer:** Total cost ₹15,20,000 / ₹18,80,000 / ₹22,64,000; profit ₹1,60,000 / ₹3,60,000 / ₹5,36,000; cost per unit ₹253.33 / ₹235.00 / ₹226.40 at 60% / 80% / 100%.

**Why this way (the reasoning):** A flexible budget exists precisely because costs behave differently. Variable costs are re-computed by multiplying the *per-unit* rate by the new volume (they change in total but not per unit); fixed costs are kept *constant in total* (so per-unit fixed cost falls as volume rises — this is why cost per unit drops from ₹253.33 to ₹226.40, the whole point of the exercise). The semi-variable element is the examiner's trap: you must NOT scale it in proportion to units, nor freeze it — you apply the stated step-up percentages, because a semi-variable cost has a fixed core plus a portion that jumps with activity bands. Flexing fixed cost per unit or scaling the semi-variable line linearly are the two classic errors. The falling unit cost also explains *operating leverage* — why profit grows faster than sales.

*(Full-marks tip: the examiner rewards correct treatment of the semi-variable line and a per-unit cost row that visibly falls; the common deduction is treating semi-variable OH as fully variable or applying the 20% on the base ₹2,00,000 instead of on the ₹2,20,000 figure.)*

---

### Q86. Ch: Budgets & Budgetary Control — Cash Budget (Marks: 10) [Problem]
**Question:** From the data below prepare a **month-wise cash budget for January, February and March**. Opening cash on 1 January is ₹50,000.

| Month | Sales (₹) | Purchases (₹) | Wages (₹) |
|---|---|---|---|
| November (actual) | 1,80,000 | 1,00,000 | — |
| December (actual) | 1,90,000 | 1,10,000 | — |
| January | 2,00,000 | 1,20,000 | 40,000 |
| February | 2,20,000 | 1,30,000 | 44,000 |
| March | 2,40,000 | 1,40,000 | 48,000 |

Additional information: (i) Sales are collected 20% in the month of sale, 50% in the next month, 30% in the second following month. (ii) Purchases are paid in full in the month following purchase. (iii) Wages are paid in the same month. (iv) Overheads are ₹30,000 per month (including ₹5,000 depreciation) paid in the month incurred. (v) A dividend of ₹20,000 is paid in January. (vi) Machinery bought in February for ₹1,00,000 is paid in March. (vii) Advance tax ₹30,000 is paid in March.

**Solution:**

**WN-1 — Collections from debtors (20% / 50% / 30%):**

| Received in | 20% of month | 50% of prior month | 30% of 2nd-prior | Total |
|---|---|---|---|---|
| Jan | 40,000 (Jan) | 95,000 (Dec) | 54,000 (Nov) | **1,89,000** |
| Feb | 44,000 (Feb) | 1,00,000 (Jan) | 57,000 (Dec) | **2,01,000** |
| Mar | 48,000 (Mar) | 1,10,000 (Feb) | 60,000 (Jan) | **2,18,000** |

**WN-2 — Payment to creditors (one month lag):** Jan pays Dec purchases ₹1,10,000; Feb pays Jan ₹1,20,000; Mar pays Feb ₹1,30,000.

**WN-3 — Cash overheads** = ₹30,000 − ₹5,000 depreciation = **₹25,000** per month (depreciation is a non-cash charge — excluded).

**Cash Budget for January–March:**

| Particulars | January | February | March |
|---|---|---|---|
| Opening balance | 50,000 | 44,000 | 56,000 |
| **Add: Receipts** — collections | 1,89,000 | 2,01,000 | 2,18,000 |
| **Total available (A)** | 2,39,000 | 2,45,000 | 2,74,000 |
| **Payments:** | | | |
| Creditors (WN-2) | 1,10,000 | 1,20,000 | 1,30,000 |
| Wages | 40,000 | 44,000 | 48,000 |
| Cash overheads (WN-3) | 25,000 | 25,000 | 25,000 |
| Dividend | 20,000 | — | — |
| Machinery | — | — | 1,00,000 |
| Advance tax | — | — | 30,000 |
| **Total payments (B)** | **1,95,000** | **1,89,000** | **3,33,000** |
| **Closing balance (A − B)** | **44,000** | **56,000** | **(59,000)** |

**Answer:** Closing cash — Jan ₹44,000; Feb ₹56,000; Mar **deficit ₹59,000**. The firm must arrange an overdraft/short-term finance of at least ₹59,000 for March.

**Why this way (the reasoning):** A cash budget records money actually moving, on the *date it moves* — not when the transaction is booked. That is why sales are spread over three months per the collection pattern (a ₹2,00,000 January sale is not ₹2,00,000 of January cash) and purchases hit cash a month late. The single most-tested trap is **depreciation**: it is an accounting allocation of past capital spending, never a cash outflow, so it is stripped out of the ₹30,000 overhead — students who leave it in overstate payments by ₹5,000 a month. Non-operating items (dividend, capital purchase, tax) must be slotted into their exact payment month, not the month of the decision. The negative March balance is the *reason* a treasurer prepares a cash budget: it flags a financing gap early so an overdraft can be pre-arranged rather than a payment being dishonoured.

*(Full-marks tip: examiners reward (a) removing depreciation, (b) correct month-lags, and (c) explicitly naming the overdraft need. Deductions come from netting purchases against sales, or paying capital items in the wrong month.)*

---

### Q87. Ch: Budgets & Budgetary Control — Functional Budgets: Production & Materials Purchase (Marks: 8) [Problem]
**Question:** Prepare the **production budget** and the **materials purchase budget (quantity and value)** for products A and B from the following.

| Particulars | Product A | Product B |
|---|---|---|
| Budgeted sales (units) | 12,000 | 8,000 |
| Opening finished stock (units) | 1,500 | 1,000 |
| Desired closing finished stock (units) | 2,000 | 1,500 |
| Material X per unit (kg) | 3 | 2 |
| Material Y per unit (kg) | 1 | 4 |

Material stocks: X — opening 5,000 kg, closing 6,000 kg; Y — opening 4,000 kg, closing 3,000 kg. Prices: X ₹20/kg, Y ₹15/kg.

**Solution:**

**WN-1 — Production budget (units)** = Sales + Closing FG − Opening FG:
- A = 12,000 + 2,000 − 1,500 = **12,500 units**
- B = 8,000 + 1,500 − 1,000 = **8,500 units**

**WN-2 — Material consumption for production:**

| Material | For A | For B | Total (kg) |
|---|---|---|---|
| X | 12,500 × 3 = 37,500 | 8,500 × 2 = 17,000 | 54,500 |
| Y | 12,500 × 1 = 12,500 | 8,500 × 4 = 34,000 | 46,500 |

**Materials Purchase Budget** = Consumption + Closing stock − Opening stock:

| Particulars | Material X | Material Y |
|---|---|---|
| Consumption (WN-2) | 54,500 | 46,500 |
| Add: Closing stock | 6,000 | 3,000 |
| Less: Opening stock | (5,000) | (4,000) |
| **Purchase quantity (kg)** | **55,500** | **45,500** |
| Rate (₹/kg) | 20 | 15 |
| **Purchase value (₹)** | **11,10,000** | **6,82,500** |

**Answer:** Production — A 12,500 units, B 8,500 units. Purchases — X 55,500 kg (₹11,10,000), Y 45,500 kg (₹6,82,500); total purchase value **₹17,92,500**.

**Why this way (the reasoning):** Functional budgets are built in a strict cause-and-effect chain: sales drive production, production drives material consumption, and consumption plus the inventory policy drives purchases. The two formulae look alike but do different jobs. For production you add the *finished-goods* stock change because you must make enough both to sell AND to end the period with the desired closing stock. For purchases you add the *raw-material* stock change because you buy enough both to consume in production AND to hold the desired closing raw stock — and consumption itself is a function of the *production* figure, never the *sales* figure. The frequent error is computing material on sales units (12,000) instead of production units (12,500), which silently understates purchases. Note also that opening stock is subtracted (it reduces what you must buy/make) and closing stock is added.

*(Full-marks tip: show the two-stage flow explicitly — sales→production→consumption→purchases; deductions arise from using sales instead of production units for material, and from mixing up the sign of opening/closing stock.)*

---

### Q88. Ch: Budgets & Budgetary Control — Principal Budget Factor (Marks: 5) [Case/Application]
**Question:** The budget officer of a company asserts: *"The sales budget must always be prepared first because sales is the principal budget factor for every business."* The company is currently unable to meet demand because a specialised grade of skilled labour is in acute short supply, while its order book is full and material is freely available. **Examine the validity of the officer's statement** and advise which budget should be prepared first.

**Answer:**

**Governing principle.** The *principal (key) budget factor* is the factor which, at a given time, limits the activities of the undertaking. Because it constrains everything else, it must be identified *first*, and the budget for that factor must be prepared *first*; all other functional budgets are then built around it so that the plan is achievable and internally consistent.

**Application to the facts.** The officer is only *partly* correct. Sales is *often* the principal budget factor — for most firms demand is the binding constraint. But the key factor is not fixed by rule; it is whatever is scarce at the moment, and it can be sales, materials, labour, plant capacity, cash, or even management. Here the facts show demand is *not* the constraint (order book full, material freely available); the binding constraint is the **shortage of specialised skilled labour**. Therefore labour, not sales, is the principal budget factor for this company right now.

**Conclusion / Advice.** The statement is invalid as a universal rule. The company should first prepare the **labour budget** (quantifying available skilled labour hours), then flex the production budget to fit that ceiling, and only then finalise the sales budget to the volume that the constrained production can actually deliver. Preparing an unconstrained sales budget first would produce a plan the factory cannot execute.

**Why this way (the reasoning):** The whole logic of budgeting is that budgets must be *feasible and coordinated*, not aspirational. If you build every budget off a sales figure that the scarce resource cannot support, each subordinate budget inherits an impossible target and the master budget collapses. Identifying the key factor first forces the plan through the eye of the needle — the scarce resource — so that production, purchases and cash all reconcile to what is genuinely achievable. The tempting "sales-first" reflex fails whenever the market wants more than the firm's scarcest input can supply; recognising *which* resource is scarce is precisely the judgement the topic tests.

*(Full-marks tip: the examiner wants the definition, the explicit statement that the key factor is situation-specific (with examples), and a clear identification of labour as the constraint here; a bare "sales budget first" answer scores near zero.)*

---

### Q89. Ch: Budgets & Budgetary Control — Master Budget with Break-even Analysis (Marks: 8) [Problem]
**Question:** From the functional-budget data below, prepare the **budgeted income statement (master budget summary)** for the year, and compute the **P/V ratio, break-even point (units and ₹) and margin of safety**. Budgeted output = budgeted sales = 20,000 units; there is no opening or closing stock.

| Particulars | ₹ per unit |
|---|---|
| Selling price | 150 |
| Direct materials | 40 |
| Direct labour | 30 |
| Variable production overhead | 20 |
| Variable selling overhead | 10 |

Fixed factory overhead ₹5,00,000; fixed selling & administration overhead ₹3,00,000.

**Solution:**

**WN-1 — Contribution per unit** = 150 − (40 + 30 + 20 + 10) = 150 − 100 = **₹50**.

**WN-2 — Total fixed cost** = 5,00,000 + 3,00,000 = **₹8,00,000**.

**Budgeted Income Statement (Master Budget Summary):**

| Particulars | Amount (₹) |
|---|---|
| Sales (20,000 × 150) | 30,00,000 |
| Less: Variable production cost (20,000 × 90) | 18,00,000 |
| Less: Variable selling cost (20,000 × 10) | 2,00,000 |
| **Contribution (20,000 × 50)** | **10,00,000** |
| Less: Fixed factory overhead | 5,00,000 |
| Less: Fixed selling & admin overhead | 3,00,000 |
| **Budgeted profit** | **2,00,000** |

**WN-3 — Ratios:**
- P/V ratio = Contribution ÷ Sales = 50 ÷ 150 = **33.33%**
- BEP (units) = Fixed cost ÷ Contribution/unit = 8,00,000 ÷ 50 = **16,000 units**
- BEP (₹) = 8,00,000 ÷ 0.3333 = **₹24,00,000**
- Margin of safety = 20,000 − 16,000 = **4,000 units** (₹6,00,000), i.e. 20% of sales.

**Answer:** Budgeted profit ₹2,00,000; P/V ratio 33.33%; BEP 16,000 units / ₹24,00,000; margin of safety 4,000 units (₹6,00,000).

**Why this way (the reasoning):** The master budget is the consolidation of all functional budgets into one financial picture, and presenting it in *marginal (contribution) format* — rather than a plain cost stack — is deliberate: it separates cost by behaviour so the plan can be stress-tested. Once contribution is isolated, the P/V ratio, break-even and margin of safety fall out immediately, telling management *how much cushion* the budget carries before losses begin. The margin of safety of only 20% is the analytical payoff: it warns that a 20% sales shortfall wipes out all profit. Building the statement in absorption format would give the same profit but would hide these risk metrics, which is why the marginal layout is preferred for planning.

*(Full-marks tip: present the statement in contribution format and label each ratio; deductions come from mixing fixed cost into the per-unit contribution or forgetting variable *selling* overhead when computing contribution.)*

---

### Q90. Ch: Budgets & Budgetary Control — Cost Segregation (High–Low) & Flexible Budget with Step Cost (Marks: 8) [Problem]
**Question:** A department's total semi-variable overhead was ₹70,000 at 5,000 machine hours and ₹1,00,000 at 8,000 machine hours. The fixed portion is a *step cost*: it increases by ₹15,000 as soon as activity exceeds 9,000 machine hours. **Segregate** the cost into fixed and variable elements, and prepare a **flexible overhead budget at 6,000, 8,000 and 10,000 machine hours.**

**Solution:**

**WN-1 — High–low method:**
Variable rate = (1,00,000 − 70,000) ÷ (8,000 − 5,000) = 30,000 ÷ 3,000 = **₹10 per machine hour**.
Fixed cost = 70,000 − (5,000 × 10) = **₹20,000** (valid up to 9,000 hours).

**WN-2 — Step in fixed cost:** above 9,000 hours the fixed cost = 20,000 + 15,000 = **₹35,000**. So at 10,000 hours the higher fixed block applies; at 6,000 and 8,000 hours the ₹20,000 block applies.

**Flexible Overhead Budget:**

| Particulars | 6,000 hrs | 8,000 hrs | 10,000 hrs |
|---|---|---|---|
| Variable OH @ ₹10/hr | 60,000 | 80,000 | 1,00,000 |
| Fixed OH (step, WN-2) | 20,000 | 20,000 | 35,000 |
| **Total overhead** | **80,000** | **1,00,000** | **1,35,000** |

*(Check: the 8,000-hour column reproduces the given ₹1,00,000, confirming the segregation.)*

**Answer:** Variable ₹10/hr; fixed ₹20,000 (up to 9,000 hrs), ₹35,000 above. Budgeted overhead: ₹80,000 (6,000 hrs), ₹1,00,000 (8,000 hrs), ₹1,35,000 (10,000 hrs).

**Why this way (the reasoning):** You cannot flex a mixed cost until you know its two components, and with only two data points the high–low method is the tool: the *difference* in cost over the *difference* in activity isolates the variable rate (because the fixed part cancels out in the subtraction), after which fixed cost is the plug at either level. The deliberate twist is the *step-fixed* cost — fixed only within a *relevant range*. Beyond 9,000 hours a new resource block (e.g., a second supervisor or shift) is committed, so the fixed line jumps to ₹35,000. Treating fixed cost as flat all the way to 10,000 hours would understate the budget by ₹15,000; that is the very trap the question sets, and it teaches that "fixed" means fixed *only within a range*.

*(Full-marks tip: the self-check that the derived formula reproduces the ₹1,00,000 given point earns credit and catches arithmetic slips; the classic deduction is ignoring the step and reporting ₹1,20,000 at 10,000 hours.)*

---

### Q91. Ch: Budgets & Budgetary Control — Zero-Based Budgeting (Marks: 6) [Theory]
**Question:** A newly-appointed CFO finds that every department's budget is set each year by simply adding 8% to last year's figures, and that several long-obsolete activities continue to be funded. She proposes replacing this with **Zero-Based Budgeting (ZBB)**. **Explain ZBB, its process and advantages over incremental budgeting, and advise where it is most suitable.**

**Answer:**

**Concept.** Zero-Based Budgeting is a method in which every budget is built *from a "zero base"* — no activity or amount is carried forward as automatically justified. Each period, every function must justify its *entire* proposed expenditure afresh, as if the activity were being undertaken for the first time.

**Process.** (i) Identify **decision packages** — each activity described with its objective, the resources it needs, and the consequences of *not* funding it; (ii) evaluate and **rank** these packages in order of importance/benefit to the organisation; (iii) **allocate resources** to packages in rank order until the available funds are exhausted, cutting off the low-ranked packages.

**Advantages over incremental ("last year plus X%") budgeting.**
- It questions *every* rupee, so obsolete or low-value activities (like those the CFO found) are exposed and dropped instead of being perpetuated.
- It links spending to *objectives and outputs*, improving the cost–benefit discipline and value for money.
- It prevents the "budget padding" and creeping inefficiency that incremental budgeting quietly compounds year after year.

**Suitability / Advice.** ZBB is most valuable for **discretionary and support/service costs** — R&D, marketing, training, administration, government and non-profit spending — where there is no direct output-volume driver to justify cost. It is less suited to routine, volume-driven manufacturing costs (which flexible budgets handle better) and is time- and effort-intensive. Advice: adopt ZBB selectively for the discretionary areas where obsolete activities were found, rather than universally.

**Why this way (the reasoning):** The defect ZBB attacks is the hidden assumption inside incremental budgeting — that last year's base was *right* and only the increment needs scrutiny. That assumption lets waste become permanent, because inefficiency embedded once is funded forever. Forcing a zero base every period removes that shelter and re-tests each activity's justification against current objectives. The reason it is targeted at *discretionary* costs is that these lack a natural output measure, so without a fresh justification there is nothing to discipline them; engineered/volume costs already have that discipline through standards and flexible budgets, so applying costly ZBB there adds effort for little gain.

*(Full-marks tip: name the three-step process — decision packages → ranking → allocation — and give the discretionary-cost suitability; a generic "start from zero" answer without the process and suitability caps the marks.)*

---

### Q92. Ch: Budgets & Budgetary Control — Labour (Man-power) Budget with Idle Time (Marks: 6) [Problem]
**Question:** Prepare the **direct labour cost budget** for the period. Idle time (allowed) is 5% of hours *paid*, and the wage rate is ₹50 per hour paid.

| Product | Budgeted production (units) | Standard time (hours/unit) |
|---|---|---|
| A | 10,000 | 2 |
| B | 6,000 | 3 |

**Solution:**

**WN-1 — Standard (productive) hours required:**
- A: 10,000 × 2 = 20,000 hrs
- B: 6,000 × 3 = 18,000 hrs
- Total productive hours = **38,000 hrs**

**WN-2 — Gross hours to be paid (grossing up for idle time):**
Idle time is 5% of hours *paid*, so productive hours = 95% of hours paid.
Hours to be paid = 38,000 ÷ 0.95 = **40,000 hrs**.
(Idle hours = 40,000 − 38,000 = 2,000 hrs = 5% of 40,000 ✓.)

**Direct Labour Cost Budget:**

| Particulars | Hours | ₹ |
|---|---|---|
| Productive hours (A + B) | 38,000 | — |
| Add: Idle time (5% of paid) | 2,000 | — |
| **Hours to be paid** | **40,000** | — |
| Wage rate per paid hour | — | 50 |
| **Direct labour cost** | — | **20,00,000** |

**Answer:** Budgeted direct labour cost = 40,000 paid hours × ₹50 = **₹20,00,000** (of which idle-time cost = 2,000 × ₹50 = ₹1,00,000).

**Why this way (the reasoning):** The labour budget must plan for hours the firm will *pay for*, not merely the hours of useful output. Since some paid time is unavoidably idle (setup waits, tea breaks, machine down-time), the productive hours are always *less* than paid hours. The subtlety is the direction of the grossing-up: because idle time is expressed as a percentage of hours *paid*, productive hours equal 95% of paid hours, so you **divide** the 38,000 by 0.95 (≈ 40,000) — you do **not** add 5% of 38,000 (which would wrongly give 39,900). Multiplying by the rate on the *paid* hours ensures the idle-time cost is captured in the budget, which is exactly what management needs to fund and control.

*(Full-marks tip: grossing up by dividing by 0.95 — not adding 5% — is the marked point; showing the idle-time cost separately (₹1,00,000) demonstrates command of the concept.)*

---

### Q93. Ch: Service Costing — Passenger Transport (Passenger-km) (Marks: 10) [Problem]
**Question:** A bus operator runs one 40-seat bus on a 30-km route, making **2 round trips per day for 25 days a month**, at an average occupancy of **80%**. From the data below, compute (a) total monthly operating cost, (b) cost per passenger-km, and (c) the fare per passenger for the full 30-km journey to earn a profit of **25% on takings (fare)**.

| Standing (monthly) | ₹ | Running / maintenance | ₹ |
|---|---|---|---|
| Driver salary | 18,000 | Diesel: mileage 5 km/litre, ₹90/litre | as computed |
| Conductor salary | 12,000 | Oil & lubricants | ₹2 per km |
| Insurance (₹24,000 p.a.) | 2,000 | Tyres & spares | ₹3 per km |
| Road tax (₹12,000 p.a.) | 1,000 | Repairs (fixed) | 8,000 |
| Garage rent | 3,000 | | |
| Depreciation: bus ₹20,00,000, scrap ₹2,00,000, life 5 yrs | 30,000 | | |

**Solution:**

**WN-1 — Kilometres run per month:** one round trip = 30 km × 2 (up & down) = 60 km; 2 round trips/day = 120 km; × 25 days = **3,000 km/month**.

**WN-2 — Passenger-km:** effective passengers = 40 × 80% = 32; passenger-km = 32 × 3,000 = **96,000 passenger-km**.

**WN-3 — Diesel cost:** cost/km = ₹90 ÷ 5 = ₹18; monthly = 3,000 × 18 = **₹54,000**.

**WN-4 — Depreciation** = (20,00,000 − 2,00,000) ÷ 5 = ₹3,60,000 p.a. = **₹30,000/month** (given).

**Operating Cost Statement (per month):**

| Particulars | ₹ |
|---|---|
| **A. Standing charges** | |
| Driver + Conductor | 30,000 |
| Insurance + Road tax | 3,000 |
| Garage rent | 3,000 |
| Depreciation | 30,000 |
| **Sub-total (A)** | **66,000** |
| **B. Running charges** | |
| Diesel (WN-3) | 54,000 |
| Oil & lubricants (₹2 × 3,000) | 6,000 |
| Tyres & spares (₹3 × 3,000) | 9,000 |
| **Sub-total (B)** | **69,000** |
| **C. Maintenance — repairs** | 8,000 |
| **Total operating cost (A+B+C)** | **1,43,000** |

**WN-5 — Cost per passenger-km** = 1,43,000 ÷ 96,000 = **₹1.4896**.

**WN-6 — Fare (25% profit on *takings*):** cost = 75% of fare, so fare/passenger-km = 1.4896 ÷ 0.75 = ₹1.9861. Fare for the 30-km journey = 1.9861 × 30 = **₹59.58**.

**Answer:** Total monthly cost ₹1,43,000; cost per passenger-km ₹1.49; fare per passenger for 30 km ≈ **₹59.58** (to earn 25% on takings).

**Why this way (the reasoning):** In transport the *composite unit* — passenger-km — is used because neither "passengers" nor "kilometres" alone captures the service: carrying 32 people 3,000 km is 96,000 passenger-km of output, and cost must be spread over that combined measure so a short crowded route and a long empty one are comparable. Two traps are built in. First, kilometres must count *both* directions of every round trip (60 km, not 30), or km and hence variable cost halve. Second, "25% profit on **takings**" means profit is a slice of the *fare*, so cost is 75% of fare and you **divide by 0.75** — students who add 25% to cost (treating it as profit on cost) understate the fare, because ₹X + 25%X gives a smaller figure than ₹X ÷ 0.75. Separating standing (time-based) from running (distance-based) costs also mirrors how the fleet actually incurs cost.

*(Full-marks tip: correct passenger-km, both-way km, and the "on takings → ÷0.75" logic are the three scoring points; the standard deduction is profit-on-cost instead of profit-on-takings.)*

---

### Q94. Ch: Service Costing — Goods Transport: Absolute vs Commercial Tonne-km (Marks: 10) [Problem]
**Question:** A 10-tonne truck makes the following daily round trip for **25 days a month**: A→B, 100 km carrying 10 tonnes; B→C, 120 km carrying 8 tonnes; C→A, 160 km **empty (return)**. Compute (a) monthly **absolute tonne-km** and **commercial tonne-km**, and (b) the operating cost per tonne-km on **both** bases, from the data below.

| Fixed (monthly) | ₹ | Running (per km) | ₹ |
|---|---|---|---|
| Driver salary | 15,000 | Diesel: 4 km/litre, ₹90/litre | as computed |
| Cleaner salary | 8,000 | Oil & lubricants | 1.50 |
| Insurance | 2,500 | Tyres & maintenance | 4.00 |
| Road tax | 1,500 | | |
| Garage rent | 4,000 | | |
| Depreciation: truck ₹12,00,000, life 8 yrs, no scrap | 12,500 | | |

**Solution:**

**WN-1 — Distance per day** = 100 + 120 + 160 = 380 km; per month = 380 × 25 = **9,500 km**.

**WN-2 — Absolute tonne-km per day** = Σ(load × distance) = (10 × 100) + (8 × 120) + (0 × 160) = 1,000 + 960 = 1,960; per month = 1,960 × 25 = **49,000 tonne-km**.

**WN-3 — Commercial tonne-km per day** = average load × total distance. Average load = total load ÷ number of legs = (10 + 8 + 0) ÷ 3 = 6 tonnes; commercial tkm = 6 × 380 = 2,280; per month = 2,280 × 25 = **57,000 tonne-km**.

**WN-4 — Diesel cost/km** = 90 ÷ 4 = ₹22.50.

**Operating Cost Statement (per month):**

| Particulars | ₹ |
|---|---|
| **A. Fixed charges** (15,000+8,000+2,500+1,500+4,000+12,500) | 43,500 |
| **B. Running charges (on 9,500 km):** | |
| Diesel (₹22.50) | 2,13,750 |
| Oil & lubricants (₹1.50) | 14,250 |
| Tyres & maintenance (₹4.00) | 38,000 |
| **Sub-total (B)** | **2,66,000** |
| **Total operating cost (A + B)** | **3,09,500** |

**WN-5 — Cost per tonne-km:**
- Absolute basis = 3,09,500 ÷ 49,000 = **₹6.316**
- Commercial basis = 3,09,500 ÷ 57,000 = **₹5.430**

**Answer:** Absolute tonne-km 49,000; commercial tonne-km 57,000; cost per absolute tonne-km **₹6.32** and per commercial tonne-km **₹5.43** per month.

**Why this way (the reasoning):** The two measures answer different questions and that is exactly why the syllabus contrasts them. **Absolute (weighted-average) tonne-km** multiplies *each* leg's actual load by *its own* distance and sums them — it is the true productive work done, so cost per absolute tonne-km is the honest efficiency measure and the right basis for pricing a specific consignment. **Commercial tonne-km** takes one *average* load across the *whole* distance (including the empty return leg here, load 0), which flatters the figure because the empty leg drags the average load down but keeps the full distance, inflating the tonne-km and so *lowering* the apparent cost per unit. The empty return (dead mileage) is the crux: it costs real fuel and time but earns zero revenue, so absolute tonne-km — which gives it zero credit — is the more conservative, decision-relevant number. Presenting both, and explaining the gap, is what the question rewards.

*(Full-marks tip: state both definitions, include the empty leg (0 tonnes) in the average-load count for commercial tkm, and comment on why absolute < commercial gives a higher unit cost; the usual deduction is computing only one basis or omitting the empty leg from the average.)*

---

### Q95. Ch: Service Costing — Hospital Costing (Patient-day) (Marks: 8) [Problem]
**Question:** A 40-bed hospital operated at **100% occupancy for 300 days** and **60% occupancy for the remaining 65 days** in a 365-day year. From the annual costs below, compute (a) the number of patient-days, (b) the cost per patient-day, and (c) the charge per patient-day if the hospital wants a **profit of 20% on the charge (takings)**.

| Annual cost | ₹ |
|---|---|
| Staff salaries | 15,00,000 |
| Medicines & consumables (₹50 per patient-day) | as computed |
| Food (₹40 per patient-day) | as computed |
| Depreciation — building & equipment | 8,00,000 |
| Utilities | 4,00,000 |
| Administration | 3,00,000 |

**Solution:**

**WN-1 — Patient-days** = (40 × 300) + (40 × 60% × 65) = 12,000 + 1,560 = **13,560 patient-days**.

**WN-2 — Variable costs:** Medicines = 13,560 × 50 = ₹6,78,000; Food = 13,560 × 40 = ₹5,42,400.

**Statement of Total Cost (per year):**

| Particulars | ₹ |
|---|---|
| Staff salaries | 15,00,000 |
| Medicines & consumables (WN-2) | 6,78,000 |
| Food (WN-2) | 5,42,400 |
| Depreciation | 8,00,000 |
| Utilities | 4,00,000 |
| Administration | 3,00,000 |
| **Total cost** | **42,20,400** |

**WN-3 — Cost per patient-day** = 42,20,400 ÷ 13,560 = **₹311.24**.

**WN-4 — Charge (20% profit on takings):** cost = 80% of charge, so charge = 311.24 ÷ 0.80 = **₹389.05 per patient-day**.

**Answer:** 13,560 patient-days; cost per patient-day **₹311.24**; charge per patient-day **₹389.05** (for 20% profit on takings).

**Why this way (the reasoning):** A hospital's cost unit is the **patient-day** because the service consumed is a *bed occupied for a day* — both the number of patients and the length of stay matter, so a composite unit is essential (a single "patient" ignores stay length). Occupancy must be computed band-by-band, because the two periods have different fill rates; blindly using 40 beds × 365 would overstate capacity used, while using only the 300 full days would ignore the partly-filled period. The variable items (medicines, food) are correctly driven by patient-days, while salaries, depreciation and admin are period fixed costs — the classic service-costing split. Finally, "20% on takings" again forces the **÷ 0.80** logic: profit is a fraction of the charge, not an add-on to cost, so adding 20% to cost would under-recover.

*(Full-marks tip: band-wise patient-day computation and the takings-based charge are the scoring points; deductions come from using bed-days at full capacity regardless of occupancy, or profit-on-cost instead of profit-on-takings.)*

---

### Q96. Ch: Service Costing — Hotel Costing (Room-day) with Two-Tier Tariff (Marks: 8) [Problem]
**Question:** A hotel of **50 rooms** runs at **80% occupancy for 200 season-days** and **40% occupancy for 165 off-season days**. Annual costs are given below. Season rooms are charged at **1.5 times** the off-season tariff. Determine the **off-season and season room tariffs per room-day** that will yield a **profit of 25% on cost**.

| Annual cost | ₹ |
|---|---|
| Staff salaries | 12,00,000 |
| Depreciation — building & furnishings | 12,00,000 |
| Room attendant & linen (₹30 per room-day) | as computed |
| Utilities & maintenance | 5,00,000 |
| Administration | 3,61,000 |

**Solution:**

**WN-1 — Occupied room-days:** Season = 50 × 80% × 200 = 8,000; Off-season = 50 × 40% × 165 = 3,300; **Total = 11,300 room-days**.

**WN-2 — Variable attendant/linen cost** = 11,300 × 30 = ₹3,39,000.

**Statement of Total Cost (per year):**

| Particulars | ₹ |
|---|---|
| Staff salaries | 12,00,000 |
| Depreciation | 12,00,000 |
| Room attendant & linen (WN-2) | 3,39,000 |
| Utilities & maintenance | 5,00,000 |
| Administration | 3,61,000 |
| **Total cost** | **36,00,000** |

**WN-3 — Required revenue** (25% profit on cost) = 36,00,000 × 1.25 = **₹45,00,000**.

**WN-4 — Tariff computation.** Let off-season tariff = ₹x, season tariff = ₹1.5x.
Revenue = (season room-days × 1.5x) + (off-season room-days × x)
= (8,000 × 1.5x) + (3,300 × x) = 12,000x + 3,300x = **15,300x**.
Set 15,300x = 45,00,000 → x = **₹294.12**.
Season tariff = 1.5 × 294.12 = **₹441.18**.

**Room-day Tariff Statement:**

| Season | Room-days | Tariff (₹) | Revenue (₹) |
|---|---|---|---|
| Season | 8,000 | 441.18 | 35,29,440 |
| Off-season | 3,300 | 294.12 | 9,70,596 |
| **Total** | **11,300** | | **≈ 45,00,000** |

**Answer:** Off-season tariff **₹294.12** and season tariff **₹441.18** per room-day (25% profit on cost).

**Why this way (the reasoning):** The cost unit is the **room-day** — a room let for one night — because a hotel sells *time-blocks of a room*, and occupancy differs across seasons, so capacity used must be built band-by-band (8,000 + 3,300), not from 50 × 365. The genuinely hard step is the *differential tariff*: because season rooms cost the guest 1.5×, you cannot just divide total revenue by total room-days (that would give a single average rate). Instead you express both tariffs in terms of one unknown x, weight each season's room-days by its price factor to get **equivalent room-days** (15,300x), and solve — mirroring the "equivalent units" idea. Anchoring on the required *revenue* (cost + 25% of cost) rather than on cost per room-day is what lets the two prices reconcile back to ₹45,00,000.

*(Full-marks tip: the equivalent-room-day weighting (12,000x + 3,300x) and solving for one variable is the examiner's target; a single flat tariff, or forgetting to gross cost up for the 25% profit, are the usual deductions.)*

---

### Q97. Ch: Service Costing — Selection of Composite Cost Units (Marks: 5) [Theory]
**Question:** A trainee argues that service organisations should use a *single* cost unit such as "one passenger" or "one tonne" because it is simpler. **Comment on the validity of this view**, explain the concept of a **composite cost unit**, and illustrate with suitable examples across service industries.

**Answer:**

**Governing principle.** In service (operating) costing the cost unit must reflect the *service actually rendered*. Many services combine *two* dimensions — a quantity dimension and a distance/time dimension — and no single-factor unit can capture both. A **composite (or equivalent) cost unit** is one that fuses two such factors into a single measure, so that cost per unit becomes meaningful and comparable.

**Application / examples.**

| Service industry | Simple unit (inadequate) | Composite unit (appropriate) |
|---|---|---|
| Passenger transport | Passenger | Passenger-kilometre |
| Goods transport | Tonne | Tonne-kilometre |
| Hospital | Patient | Patient-day |
| Hotel | Room | Room-day |
| Power generation | — | Kilowatt-hour (kWh) |
| Steam supply | — | Kg / cubic-metre of steam |

**Commenting on the trainee's view — why it is invalid.** Take goods transport: "one tonne" ignores *how far* the tonne moved, so carrying 10 tonnes 5 km would look identical to carrying 10 tonnes 500 km, though the second consumes a hundred times the fuel and time. Only the composite **tonne-km** captures both weight and distance, giving a cost that fairly reflects the resource used. The same logic applies to passenger-km (people × distance) and patient-day (patients × length of stay).

**Conclusion.** The trainee is wrong: simplicity that hides a genuine cost driver produces misleading unit costs and bad pricing. Composite units are chosen precisely because the service's cost is driven jointly by two factors. (Within transport, one further refines into *absolute* tonne-km — Σ load × distance — versus *commercial* tonne-km — average load × total distance — for different decision purposes.)

**Why this way (the reasoning):** A cost unit is only useful if it moves in step with the cost it summarises. Where cost is driven by two independent factors, a one-dimensional unit necessarily suppresses one of them and so breaks the link between unit and cost — the very failure operating costing exists to avoid. The composite unit restores that link by multiplying the two drivers, which is also why it is called an *equivalent* unit: it converts heterogeneous services (short heavy trips, long light trips) onto one comparable scale.

*(Full-marks tip: give the two-factor rationale plus a table of at least four industry-specific composite units; a definition without examples, or examples without the "why two factors" reasoning, loses marks.)*

---

### Q98. Ch: Service Costing — Transport with Dead Mileage: Cost per Effective km & Tonne-km (Marks: 8) [Problem]
**Question:** A delivery van of 5-tonne capacity runs **4,000 km a month**, of which **25% is empty (dead) running** on return journeys. When loaded, it carries an average of **4 tonnes**. From the costs below, compute (a) cost per total km, (b) cost per **loaded (effective)** km, and (c) cost per loaded tonne-km — and advise the minimum freight rate per tonne-km if the operator wants a **20% margin on the rate**.

| Fixed (monthly) | ₹ | Running (per total km) | ₹ |
|---|---|---|---|
| Driver salary | 14,000 | Fuel | 15.00 |
| Insurance | 1,500 | Maintenance | 5.00 |
| Road tax | 1,000 | | |
| Depreciation | 10,000 | | |

**Solution:**

**WN-1 — Loaded vs total km:** empty = 25% × 4,000 = 1,000 km; **loaded (effective) km = 3,000 km**; total km = 4,000.

**WN-2 — Loaded tonne-km** = 4 tonnes × 3,000 km = **12,000 tonne-km**.

**Operating Cost Statement (per month):**

| Particulars | ₹ |
|---|---|
| **A. Fixed charges** (14,000+1,500+1,000+10,000) | 26,500 |
| **B. Running charges (on 4,000 total km):** | |
| Fuel (₹15 × 4,000) | 60,000 |
| Maintenance (₹5 × 4,000) | 20,000 |
| **Total operating cost** | **1,06,500** |

**WN-3 — Unit costs:**
- Cost per **total** km = 1,06,500 ÷ 4,000 = **₹26.625**
- Cost per **loaded** km = 1,06,500 ÷ 3,000 = **₹35.50**
- Cost per loaded **tonne-km** = 1,06,500 ÷ 12,000 = **₹8.875**

**WN-4 — Minimum freight (20% margin on rate):** cost = 80% of rate, so rate = 8.875 ÷ 0.80 = **₹11.094 per tonne-km**.

**Answer:** Cost per total km ₹26.63; per loaded km ₹35.50; per loaded tonne-km ₹8.875; minimum freight ≈ **₹11.09 per tonne-km** for a 20% margin on the rate.

**Why this way (the reasoning):** The key insight is that cost is incurred on *all* km run (fuel and maintenance burn on the empty return too), but revenue can only be earned on the *loaded* km. Therefore the *total* cost must be recovered over the *loaded* distance, which is why cost per loaded km (₹35.50) is higher than cost per total km (₹26.63) — the empty 25% has to be subsidised by the paying 75%. Pricing off the "total km" rate would systematically under-recover and the operator would lose money on every dead-mileage trip. Reducing to tonne-km further recognises that partial loads (4 of 5 tonnes) dilute recovery per tonne. The "20% margin on rate" again means the rate is the base (÷ 0.80), not a mark-up on cost. This is the practical lesson: freight must be quoted to recover the cost of the *whole* journey, empty leg included.

*(Full-marks tip: recovering cost over loaded — not total — km, and the ÷0.80 on the rate, are the scored ideas; the classic error is dividing total cost by 4,000 km (understating the recovery rate) or spreading fuel only over loaded km.)*

---

### Q99. Ch: Service Costing — Staff Canteen (Internal Service) Costing (Marks: 6) [Problem]
**Question:** A company runs a staff canteen serving **500 meals a day for 25 days a month**. From the costs below, compute the **cost per meal**, and the **price charged to employees** if the company subsidises **50% of the cost**.

| Cost | ₹ |
|---|---|
| Provisions (₹18 per meal) | as computed |
| Cook & serving staff salaries | 40,000 |
| Fuel / gas | 15,000 |
| Consumables (₹2 per meal) | as computed |
| Depreciation of kitchen equipment | 5,000 |

*(Canteen premises are provided free by the company.)*

**Solution:**

**WN-1 — Meals per month** = 500 × 25 = **12,500 meals**.

**WN-2 — Variable costs:** Provisions = 12,500 × 18 = ₹2,25,000; Consumables = 12,500 × 2 = ₹25,000.

**Statement of Cost per Meal (per month):**

| Particulars | ₹ |
|---|---|
| Provisions (WN-2) | 2,25,000 |
| Cook & serving staff salaries | 40,000 |
| Fuel / gas | 15,000 |
| Consumables (WN-2) | 25,000 |
| Depreciation of equipment | 5,000 |
| **Total cost** | **3,10,000** |
| ÷ Meals served | 12,500 |
| **Cost per meal** | **₹24.80** |

**WN-3 — Price to employees** (50% subsidy) = 24.80 × 50% = **₹12.40 per meal**.

**Answer:** Cost per meal **₹24.80**; price charged to employees after 50% subsidy **₹12.40**.

**Why this way (the reasoning):** A canteen is an *internal service department*, so service costing applies even though nothing is sold externally — the "output" is the meal, and cost per meal is found by pooling all costs and dividing by meals served. The subtlety students miss is *what to include and exclude*: provisions and consumables are correctly driven by meals (variable), while cook's salary, fuel and depreciation are period fixed costs that must still be absorbed into the meal cost. Free premises are given deliberately as a distractor — since the company incurs no rent charge to the canteen, no rent enters the cost (you do not impute a notional rent unless the question asks). The 50% subsidy is a *sharing* of the derived cost, so the employee price is simply half the full cost — the subsidy is the company's welfare cost, not a reduction in the true cost of producing the meal.

*(Full-marks tip: absorbing fixed items (salary, fuel, depreciation) into the per-meal cost and correctly excluding the free rent are the scoring points; deductions come from costing only the variable provisions or imputing a rent that was not charged.)*

---

### Q100. Ch: Service Costing — BOT Toll Road: Toll Rate per Vehicle (Marks: 10) [Problem]
**Question:** A company has built a highway under a **20-year BOT (Build-Operate-Transfer)** concession at a project cost of **₹100 crore**, with no residual value at transfer. Annual operation & maintenance cost is **₹5 crore**. Estimated daily traffic is **8,000 cars** (1 PCU each) and **2,000 buses/trucks** (3 PCU each), for **365 days a year**. The company requires a **15% return on the average capital employed**. Determine the annual toll revenue required and the **toll rate per car and per heavy vehicle**, charging in proportion to Passenger Car Units (PCU).

**Solution:**

**WN-1 — Annual capital recovery (depreciation of the asset over the concession)** = ₹100 crore ÷ 20 years = **₹5 crore per year**.

**WN-2 — Return on capital employed:** average capital employed = ₹100 crore ÷ 2 = ₹50 crore; return = 15% × 50 = **₹7.5 crore per year**.

**WN-3 — Annual revenue required:**

| Particulars | ₹ crore |
|---|---|
| Capital recovery (WN-1) | 5.0 |
| Operation & maintenance | 5.0 |
| Return on average capital (WN-2) | 7.5 |
| **Total annual toll revenue required** | **17.5** |

**WN-4 — Annual PCU (the composite output):**
Daily PCU = (8,000 × 1) + (2,000 × 3) = 8,000 + 6,000 = 14,000 PCU.
Annual PCU = 14,000 × 365 = **51,10,000 PCU**.

**WN-5 — Toll rate per PCU** = ₹17,50,00,000 ÷ 51,10,000 = **₹34.25 per PCU**.

**Toll Rate Statement:**

| Vehicle | PCU factor | Toll (₹) |
|---|---|---|
| Car | 1 | 34.25 |
| Bus / truck | 3 | 102.75 |

*(Check: 34.25 × 51,10,000 PCU ≈ ₹17.5 crore — reconciles with required revenue.)*

**Answer:** Required annual toll revenue **₹17.5 crore**; toll ≈ **₹34.25 per car** and **₹102.75 per heavy vehicle**.

**Why this way (the reasoning):** A toll road is priced by service costing because the "output" is *road usage*, and different vehicles impose very different loads on the road — so a single "per vehicle" rate would be unfair. The **PCU (Passenger Car Unit)** is the composite/equivalent unit that converts a heavy vehicle into "3 cars' worth" of road use, letting all traffic be measured on one scale; the toll is then a flat rate per PCU, which automatically charges a truck 3× a car. On the cost side, the concessionaire must recover three distinct things: the *capital* sunk in the road (spread over the 20-year life since it reverts to the government with nil value — hence straight-line recovery), the recurring *O&M*, and a *return* on the money tied up. The return is taken on **average** capital employed (₹50 crore, not ₹100 crore) because, as the asset is recovered/depreciated over the concession, the capital locked up declines from ₹100 crore to nil, averaging ₹50 crore — charging 15% on the full ₹100 crore throughout would over-recover and over-price the toll.

*(Full-marks tip: the PCU-weighting of traffic and the use of *average* (not full) capital employed for the 15% return are the two examiner targets; deductions arise from charging all vehicles the same toll, or applying the return on ₹100 crore instead of the ₹50 crore average.)*
