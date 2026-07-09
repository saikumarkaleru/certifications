# Q&A — Production and Costs

> Scope: Economics for Finance — Chapter 05 (Production and Costs). Every question is followed by a full model answer. All amounts in Rupees (₹). Work every numerical problem yourself before checking the solution. Sections: **A** concept-check · **B** applied/numerical · **C** interview-style · **D** MCQs with reasoning.

---

## The chapter in one picture

```mermaid
flowchart LR
    A["Technology + inputs"] --> B["Production function Q=f(L,K)"]
    B --> C["Marginal & average product"]
    C --> D["Cost curves: MC, AVC, ATC (MC = w/MPL)"]
    D --> E["Operating leverage"]
    E --> F["Risk, beta, valuation"]
```

**One-line statement:** Costs are the production function priced out; diminishing marginal returns make short-run cost curves U-shaped, and the fixed/variable split drives operating leverage and firm value.

---

## Section A — Concept Check

**A1. Distinguish the short run from the long run. Is the distinction about calendar time?**
No — it is about which inputs can vary. In the **short run** at least one input (typically capital/plant) is **fixed**; the firm changes output by varying the variable input (labour). In the **long run** *all* inputs are variable. The calendar length of the "short run" differs by industry — weeks for a food truck, a decade for a nuclear utility. The short run is the world of diminishing marginal returns; the long run is the world of returns to scale.

**A2. Define total product, marginal product, and average product of labour.**
Holding capital fixed and adding labour: **Total Product (TP)** is total output; **Marginal Product of Labour (MPL)** = ΔTP/ΔL, the extra output from one more worker; **Average Product (AP)** = TP/L, output per worker.

**A3. State the law of diminishing marginal returns and why it holds.**
As successive units of a variable input are added to a fixed input, the marginal product **eventually declines**. It holds because the fixed factor (say one oven, or fixed floor space) becomes a bottleneck: the first workers specialise and use idle capacity, but additional workers increasingly crowd the same fixed capital, so each adds less. MPL can even turn negative if workers get in each other's way.

**A4. Why does MPL cut the AP curve at AP's maximum?**
Pure marginal-versus-average arithmetic. When the marginal worker is *more* productive than the current average, they pull the average up; when *less* productive, they drag it down. So AP is rising while MPL > AP, falling while MPL < AP, and at its peak exactly where MPL = AP. (Same logic as a batting average: a below-average innings lowers your average.)

**A5. Why are short-run cost curves U-shaped? Give the one-equation reason.**
Because **MC = w / MPL**. When MPL is rising (early workers), MC falls; once diminishing marginal returns set in and MPL falls, MC rises. The U-shape of cost is therefore not an assumption — it is the mirror image of the productivity curve.

**A6. Distinguish TFC, TVC, and TC, and give an example of each.**
**Total Fixed Cost (TFC)** does not vary with output — rent, insurance, plant depreciation, salaried management. **Total Variable Cost (TVC)** varies with output — raw materials, hourly wages, energy, shipping. **Total Cost (TC)** = TFC + TVC.

**A7. Why does marginal cost depend only on variable cost?**
Producing one more unit does not change fixed cost, so MC = ΔTC/ΔQ = ΔTVC/ΔQ. Fixed cost never enters the marginal decision — the foundation of "fixed costs are sunk; ignore them at the margin."

**A8. Why does AFC always fall, and what does the gap between ATC and AVC represent?**
AFC = TFC/Q, and since TFC is constant, dividing it by an ever-larger Q makes AFC fall continuously toward zero ("spreading the overhead"). The vertical gap between ATC and AVC **is** AFC, so that gap narrows as output grows.

**A9. Why does ATC reach its minimum at a higher output than AVC?**
Because AFC keeps falling even after AVC has started rising. Near AVC's minimum, the continued fall in AFC still pulls ATC down, so ATC keeps declining a bit longer; its trough sits to the right of AVC's.

**A10. State the relationship between MC and the average cost curves.**
MC passes through the **minimum** of both AVC and ATC. When MC is below an average curve it pulls the average down; when above, it pushes the average up. So MC must intersect each average curve exactly at its lowest point. Efficient scale is where MC = ATC (minimum).

**A11. Distinguish diminishing marginal returns from decreasing returns to scale.**
**Diminishing marginal returns** is short-run: add *one* variable input to *fixed* others and marginal product falls. **Decreasing returns to scale** is long-run: scale *all* inputs together and output rises less than proportionately. A firm can have diminishing marginal returns to labour while still enjoying increasing returns to scale.

**A12. Define increasing, constant, and decreasing returns to scale.**
Scale every input by the same factor: if output *more* than doubles when inputs double → **increasing** returns to scale; exactly doubles → **constant**; *less* than doubles → **decreasing**.

**A13. List three sources of economies of scale and three of diseconomies.**
**Economies:** spreading fixed costs over more units (technical), specialisation/division of labour, bulk purchasing, cheaper finance, marketing/network effects. **Diseconomies:** managerial/coordination failures and bureaucracy, motivational/principal-agent problems, and bidding up the price of scarce inputs (talent, prime real estate).

**A14. Why is the LRAC curve called an "envelope"?**
Each plant size has its own short-run ATC curve. In the long run the firm picks the plant that is cheapest for the output it wants, so LRAC is the **lower boundary** hugging the bottom of all the short-run ATC curves. It is typically flatter than any single short-run curve, often "L-shaped" in modern industries.

**A15. State the cost-minimisation (isoquant–isocost) condition and interpret it.**
Least-cost input mix occurs where **MPL/MPK = w/r**, equivalently **MPL/w = MPK/r** — the extra output per rupee spent is equal across all inputs. If wages rise, the isocost line tilts and the optimum shifts toward more capital: the economic logic behind automation and offshoring.

**A16. Define minimum efficient scale (MES).**
The smallest output at which LRAC reaches its minimum — the lowest scale at which a firm captures all available economies of scale and can compete on cost.

---

## Section B — Applied / Numerical Problems

**B1. Marginal product and marginal cost.**
A factory with fixed capital hires workers at ₹800/day. Total product is: 1 worker → 15 units, 2 → 35, 3 → 60, 4 → 78, 5 → 90. Compute MPL and MC per unit at each step, and identify where diminishing returns begin.

*Solution.* MPL = ΔTP; MC = w/MPL = 800/MPL.

| Workers | TP | MPL | MC = 800/MPL |
|---|---|---|---|
| 1 | 15 | 15 | ₹53.3 |
| 2 | 35 | 20 | ₹40.0 |
| 3 | 60 | 25 | ₹32.0 |
| 4 | 78 | 18 | ₹44.4 |
| 5 | 90 | 12 | ₹66.7 |

MPL rises through the 3rd worker (specialisation) then falls — **diminishing marginal returns begin with the 4th worker**. MC is the mirror image: it falls to ₹32 then climbs to ₹66.7. This is MC = w/MPL in action.

**B2. Build the full short-run cost table.**
TFC = ₹600. TVC at outputs Q = 10, 20, 30, 40, 50 is ₹300, ₹500, ₹660, ₹900, ₹1,300. Compute TC, AFC, AVC, ATC, and MC (per unit over each 10-unit step). Where is efficient scale?

*Solution.*

| Q | TVC | TC | AFC | AVC | ATC | MC (per unit) |
|---|---|---|---|---|---|---|
| 10 | 300 | 900 | 60.0 | 30.0 | 90.0 | — |
| 20 | 500 | 1,100 | 30.0 | 25.0 | 55.0 | 20.0 |
| 30 | 660 | 1,260 | 20.0 | 22.0 | 42.0 | 16.0 |
| 40 | 900 | 1,500 | 15.0 | 22.5 | 37.5 | 24.0 |
| 50 | 1,300 | 1,900 | 12.0 | 26.0 | 38.0 | 40.0 |

AVC bottoms at Q = 30 (₹22.0); **ATC bottoms at Q = 40 (₹37.5)** — note ATC's minimum lies to the right of AVC's because AFC keeps falling. Efficient scale ≈ 40 units. Between Q = 30 and 40, MC (₹24) exceeds AVC but ATC still falls — exactly the region the theory predicts.

**B3. Contribution margin and break-even.**
A product sells at ₹50, variable cost per unit is ₹30, and fixed costs are ₹2,00,000 per month. (a) Contribution margin per unit? (b) Break-even quantity? (c) Profit at 15,000 units? (d) Units for a target profit of ₹1,00,000?

*Solution.*
(a) Contribution margin = 50 − 30 = **₹20/unit**.
(b) Break-even Q = Fixed Cost / Contribution = 2,00,000 / 20 = **10,000 units**.
(c) Profit = (15,000 − 10,000) × 20 = **₹1,00,000**. Every unit above break-even drops its full ₹20 contribution to profit.
(d) Q = (2,00,000 + 1,00,000) / 20 = **15,000 units** (consistent with (c)).

**B4. Operating leverage — two cost structures.**
Two firms each have revenue ₹100 and profit ₹10. Firm A: fixed 70, variable 20. Firm B: fixed 20, variable 70. Revenue rises 10% to ₹110 (variable costs scale with revenue, fixed do not). Compute each firm's new profit and % change. Then repeat for a 10% revenue fall.

*Solution.* Variable costs scale by 1.10; fixed stay put.
- **+10% revenue.** Firm A: 110 − (20×1.1) − 70 = 110 − 22 − 70 = **₹18 (+80%)**. Firm B: 110 − (70×1.1) − 20 = 110 − 77 − 20 = **₹13 (+30%)**.
- **−10% revenue (to 90).** Firm A: 90 − 18 − 70 = **₹2 (−80%)**. Firm B: 90 − 63 − 20 = **₹7 (−30%)**.

The high-fixed-cost firm (A) has far higher **operating leverage**: profits swing ±80% for a ±10% revenue move, versus ±30% for B. Leverage amplifies both the upside and the downside.

**B5. Degree of operating leverage (DOL).**
Using Firm A above at the base point (revenue 100, profit 10), compute DOL = % change in profit / % change in revenue, and interpret.

*Solution.* From B4, a +10% revenue change gave +80% profit, so **DOL = 80/10 = 8**. Interpretation: near this operating point, each 1% change in revenue moves operating profit about 8%. Equivalently, DOL = Contribution / Operating Profit = (100 − 20) / 10 = 80/10 = 8. High DOL = high fixed-cost intensity = high sensitivity of earnings to the business cycle → higher beta.

**B6. Economies of scale from a fixed-cost fab.**
A chip fab has fixed cost ₹40,000 crore and a variable cost of ₹200 per chip. Compute average total cost per chip at outputs of 1 crore, 10 crore, and 100 crore chips.

*Solution.* ATC = (Fixed/Q) + variable per unit.
- 1 crore: 40,000/1 = ₹40,000 fixed per chip + 200 = **₹40,200**.
- 10 crore: 40,000/10 = ₹4,000 + 200 = **₹4,200**.
- 100 crore: 40,000/100 = ₹400 + 200 = **₹600**.

ATC collapses from ₹40,200 to ₹600 purely by spreading the enormous fixed cost — the arithmetic behind why leading-edge fabs must run at massive scale, and why that scale is a cost moat entrants cannot match.

**B7. Least-cost input mix.**
MPL = 40, wage w = ₹200; MPK = 30, rental r = ₹100. Is the firm minimising cost? If not, which input should it use more of?

*Solution.* Compare bang-per-buck: MPL/w = 40/200 = **0.20** units per rupee on labour; MPK/r = 30/100 = **0.30** units per rupee on capital. Since capital delivers more output per rupee, the firm is **not** at least-cost — it should use **more capital and less labour**. As it does, diminishing returns lower MPK and raise MPL until MPL/w = MPK/r.

---

## Section C — Interview-Style Questions (economics in finance interviews)

**C1. "Why are cost curves U-shaped?"**
Answer with productivity, not assumption. In the short run at least one input is fixed, so adding the variable input runs into diminishing marginal returns. Because marginal cost equals the wage divided by marginal product (MC = w/MPL), rising productivity early on makes MC fall, and falling productivity later makes MC rise — producing the U-shape. Average cost is U-shaped for the same reason, reinforced by fixed-cost spreading. The clean takeaway: costs are just the production function priced out.

**C2. "What is operating leverage and why should an equity analyst care?"**
Operating leverage is the degree to which fixed costs amplify revenue changes into profit changes; formally, DOL = Contribution / Operating Profit. A high fixed-cost business (airline, chip fab, hotel, telecom, SaaS) sees profits swing violently with revenue — great in booms, brutal in downturns. That volatility raises beta and the cost of equity, worsens credit quality, and makes the stock cyclical. So before valuing a company I read its fixed/variable split out of the financials: it drives margin volatility, the discount rate, and bankruptcy risk. Low-fixed-cost businesses are safer but never enjoy the explosive upside.

**C3. "A company already spent ₹5 crore developing a product. Should that affect whether it launches?"**
No — that ₹5 crore is a **sunk cost**, unrecoverable and irrelevant to any forward-looking decision. The launch decision should compare only *future* incremental revenues against *future* incremental (variable) costs. If expected future contribution exceeds future incremental cost, launch; otherwise don't — regardless of what was already spent. Spotting a sunk-cost fallacy is a marker of disciplined capital allocation.

**C4. "How do economies of scale create a competitive moat?"**
When long-run average cost keeps falling with volume, a large incumbent produces at a structurally lower unit cost than any smaller entrant can match. A new entrant must either operate sub-scale at high cost or invest enormous capital to reach minimum efficient scale — a barrier to entry. TSMC in chips, Amazon in fulfilment, Vanguard in index funds all show this: the scale economies *are* the moat, protecting margins from competition and justifying a premium valuation multiple. So "does this business have economies of scale?" is really "does it have a durable cost advantage?"

**C5. "What is a natural monopoly, and why does it justify regulation?"**
A natural monopoly exists when economies of scale are so vast — huge fixed cost, low marginal cost — that a single firm supplies the whole market at lower cost than two or more could. Water networks, the electricity grid, and rail are classic cases: duplicating the pipes or tracks would waste capital. Because an unregulated sole supplier could exploit its position, governments regulate price and returns (regulated-asset-base models). This underpins the valuation of regulated utilities, where allowed returns and asset bases are the key drivers.

**C6. "Fixed costs are falling per unit as we grow — is that economies of scale?"**
Not necessarily. In the *short run*, average total cost falls partly because average fixed cost is being spread over more units — that is arithmetic, not scale economies. **True economies of scale are a long-run phenomenon** in which LRAC falls even when *all* inputs (including plant) are variable, driven by specialisation, bulk buying, technical indivisibilities, and so on. Confusing the two overstates a company's structural cost advantage.

**C7. "How do operating and financial leverage interact in an LBO or credit analysis?"**
Operating leverage (fixed operating costs) and financial leverage (fixed interest on debt) are both amplifiers of revenue into equity earnings; combined they give *total* leverage. Stacking high financial leverage on a business that already has high operating leverage multiplies risk — a modest revenue dip can wipe out both operating profit and debt-service coverage. So firms with volatile revenue and high fixed costs (airlines, cyclicals) should carry *less* debt; stable, low-operating-leverage businesses can support more. A good sponsor sets financial leverage inversely to operating leverage and cyclicality.

**C8. "What does a company's margin trajectory as it scales tell you?"**
Rising operating margins as revenue grows usually mean the company is climbing *down* its long-run average cost curve — operating leverage and scale economies playing out. Flat-to-falling margins at large scale can signal **diseconomies of scale**: bureaucracy, coordination failures, or market saturation. Margin trend against revenue growth is a core lens for judging whether a scale story is real.

---

## Section D — MCQs with Reasoning

**D1.** Marginal cost equals:
(a) TC/Q (b) TFC/Q (c) w/MPL (d) TVC/Q

**Answer: (c).** MC = ΔTC/ΔQ, and since only variable cost changes, MC = ΔTVC/ΔQ = w/MPL. Options (a), (b), (d) are *average* concepts (ATC, AFC, AVC), not marginal.

**D2.** The vertical distance between the ATC and AVC curves at any output equals:
(a) MC (b) AFC (c) TFC (d) contribution margin

**Answer: (b).** ATC = AVC + AFC, so ATC − AVC = AFC. Because AFC falls continuously, this gap narrows as output rises.

**D3.** Marginal cost intersects average total cost:
(a) at ATC's maximum (b) at ATC's minimum (c) where AFC = 0 (d) never

**Answer: (b).** When MC < ATC the average falls; when MC > ATC it rises; so MC cuts ATC exactly at its minimum. Pure marginal-vs-average logic; the same holds for AVC.

**D4.** Doubling all inputs raises output by 150%. This is:
(a) increasing returns to scale (b) constant returns to scale (c) decreasing returns to scale (d) diminishing marginal returns

**Answer: (a).** Output more than doubled (rose 2.5×) when inputs doubled → increasing returns to scale. It is a long-run, all-inputs concept, so (d) — a short-run single-input idea — is wrong.

**D5.** Which is a source of *diseconomies* of scale?
(a) bulk purchasing discounts (b) spreading fixed costs (c) managerial coordination failures (d) division of labour

**Answer: (c).** As hierarchies deepen, bureaucracy and communication breakdowns raise unit costs. The other three lower unit costs and are economies of scale.

**D6.** In the long run:
(a) all costs are variable (b) capital is fixed (c) there are no economies of scale (d) MC = 0

**Answer: (a).** The long run is defined by every input being variable, so no cost is fixed — you can exit the lease, sell the plant. (b) describes the short run.

**D7.** A firm has fixed cost ₹1,20,000, price ₹100, variable cost ₹60. Break-even quantity is:
(a) 1,200 (b) 2,000 (c) 3,000 (d) 12,000

**Answer: (c).** Contribution = 100 − 60 = ₹40. Break-even Q = 1,20,000 / 40 = 3,000 units.

**D8.** Firm X has fixed costs equal to 70% of total costs; Firm Y, 20%. Compared with Y, Firm X most likely has:
(a) lower operating leverage and lower beta (b) higher operating leverage and higher beta (c) identical risk (d) lower break-even output

**Answer: (b).** Higher fixed-cost intensity means profits amplify revenue swings more (higher operating leverage), producing more cyclical earnings, higher beta, and a higher cost of equity. Its break-even output is also *higher*, not lower.

**D9.** The marginal product of labour is falling but still positive. The firm is operating in:
(a) Stage 1 (increasing returns) (b) Stage 2 (diminishing but positive) (c) Stage 3 (negative returns) (d) long-run equilibrium

**Answer: (b).** Falling-but-positive MPL is Stage 2, where rational firms operate. Stage 3 has negative MPL (adding labour cuts output); Stage 1 has rising MPL.

**D10.** Least-cost input combination requires:
(a) MPL = MPK (b) w = r (c) MPL/w = MPK/r (d) MRTS = 0

**Answer: (c).** Cost is minimised where the marginal product per rupee is equal across inputs — equivalently MPL/MPK = w/r (the isoquant is tangent to the isocost line). Equal marginal products (a) or equal prices (b) are neither necessary nor sufficient.

**D11.** The firm's short-run supply curve is:
(a) the whole MC curve (b) the MC curve above minimum AVC (c) the ATC curve (d) the AFC curve

**Answer: (b).** A firm supplies along MC, but only above minimum AVC — below that price it cannot cover variable costs and shuts down in the short run. This is why market supply traces back to marginal cost.

**D12.** Economies of *scope* differ from economies of *scale* in that scope refers to:
(a) producing more of the same good cheaper (b) producing different goods together cheaper (c) falling fixed cost per unit (d) bulk purchasing

**Answer: (b).** Scope = cost savings from producing *different* products jointly over shared infrastructure (a bank cross-selling loans and insurance). Scale = producing *more of the same* good at lower unit cost.

---

*End of Q&A — Production and Costs.*
