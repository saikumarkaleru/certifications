# AS 28: Impairment of Assets

## Snapshot
Depreciation (AS 10) is cost allocation fixed at acquisition — blind to sudden value falls. AS 28 is point-in-time value verification: no asset may be carried above the cash it can recover. **Impaired when Carrying Amount > Recoverable Amount**; excess = impairment loss, recognised immediately. Age is irrelevant — a brand-new asset can be impaired.

## Core concepts
- **Recoverable Amount = HIGHER of Net Selling Price (NSP) and Value in Use (VIU)** — because a fixed asset is *used*, selling is a fallback; the owner takes the better route. (Contrast AS 2 inventory = *lower* of cost and NRV.) Bounded below at **zero** (asset can be abandoned; never negative).
- Shortcut: if **either** NSP or VIU already exceeds carrying amount → not impaired; no need to compute the other.
- Testing is **indicator-driven** (cheap annual scan triggers the expensive test). ICAI AS 28: **no** mandatory annual test for goodwill/intangibles (that is Ind AS 36).

## Key provisions / rules
**Master rule:** Impairment Loss = Carrying Amount − Recoverable Amount (only if positive). "Immediately" (not spread), "exceeds" (strictly greater than). Carrying amount = cost/revalued amount − accumulated depreciation − accumulated impairment.

**NSP** = fair value from arm's-length sale − direct disposal costs (legal, stamp duty, removal). **Exclude** finance costs, income tax, costs already recognised as liabilities, and termination/reorganisation costs. Evidence order: (1) binding sale agreement → (2) active-market price → (3) best estimate from recent deals.

**VIU** = PV of future cash flows from continuing use + residual/disposal value, at a **pre-tax** rate.
- Base on reasonable assumptions, most recent budgets; projections generally ≤ **5 years**, then extrapolate at **steady or declining** growth (never rising).
- **Exclude:** cash flows from uncommitted future **restructuring**; **enhancements/improvements** (test asset in current condition); **financing** flows; **income tax**.
- **Consistency:** pre-tax flows ↔ pre-tax rate; nominal ↔ nominal; real ↔ real.
- Residual/terminal value uses prices at valuation date for similar end-of-life assets.

**Indicators (illustrative minimum, not exhaustive):**
- *External:* market value fell significantly more than expected; adverse tech/market/economic/legal change; market interest rates rose (raises discount rate — but soft trigger, escape valve if insensitive); carrying amount of net assets > market capitalisation.
- *Internal:* physical damage/obsolescence; asset idle / part of discontinuing operation / plan to dispose early; internal reports show worse-than-expected performance.
- **Reversal indicators** mirror these in the opposite direction.

**Post-impairment:** depreciation resets on new carrying amount − residual over **remaining useful life**.

**CGU** = smallest identifiable group of assets generating cash inflows **largely independent** of other assets. Boundary drawn by independent **inflows**, not cost/department structure. If an active market exists for the output, it is a CGU even if output used internally. Carrying amount measured consistently with recoverable amount (include allocated goodwill/corporate assets; usually exclude liabilities).
- **CGU allocation order:** (1) reduce **goodwill** fully first (no independent recoverable value); (2) then other assets **pro rata** by carrying amount.
- **Floor:** no asset written below the highest of its own NSP, its own VIU, and **zero**; un-absorbed amount reallocated pro rata to other assets.

**Reversal:** re-estimate if indicator that prior loss decreased/gone.
- **Ceiling:** increased carrying amount must not exceed the carrying amount (net of depreciation) that would have existed had **no impairment** ever been recognised.
- Reverse up to the **LOWER of** re-estimated recoverable amount and the ceiling.
- Asset at cost → reversal credited to P&L (income). Revalued asset → treated as revaluation increase (to Revaluation Reserve), except to extent it reverses a prior decrease charged to P&L (that part to P&L).
- **Goodwill impairment is NOT reversed** (any later increase = internally generated goodwill, barred by AS 26). CGU reversal allocated pro rata, **never to goodwill**; per-asset ceiling applies.

**Scope-out:** AS 2 inventories, AS 7 construction contracts, AS 13 financial assets/investments, AS 22 DTA (each has its own valuation cap). Mainly bites on AS 10 PPE, AS 26 intangibles, goodwill.

## Journal entries
- Loss (asset at cost): **Impairment Loss A/c Dr / To Accumulated Impairment (or Asset)** → transferred to P&L.
- Loss (revalued asset): **Revaluation Reserve A/c Dr** (of that asset, up to available) then **Impairment Loss/P&L Dr** for balance **/ To Asset**.
- Reversal (at cost): **Asset A/c Dr / To Reversal of Impairment (P&L income)**.

## Worked mini-example
Plant carrying ₹20,00,000, 4 yrs left, nil residual, SLM. Flood damage. Inflows ₹6,00,000/yr for 4 yrs; disposal ₹1,00,000 in yr4; pre-tax rate 10%; NSP now ₹15,00,000.
- VIU: 6L×(0.909+0.826+0.751+0.683) + 1L×0.683 = 19,01,400 + 68,300 = **₹19,69,700**.
- Recoverable = higher(15,00,000; 19,69,700) = ₹19,69,700.
- Impairment = 20,00,000 − 19,69,700 = **₹30,300**.
- New depreciation = 19,69,700 ÷ 4 = **₹4,92,425/yr**.

CGU example: Goodwill 2L + Building 6L + Plant 4L + Fittings 2L = 14L; recoverable 9L → loss 5L. Goodwill 2L wiped; remaining 3L pro rata (6:4:2). Building floor (own NSP 5,20,000) blocks it below that → Building down only 80,000; un-absorbed 70,000 reallocated to Plant & Fittings (4:2). Final: Goodwill 0, Building 5,20,000, Plant 2,53,333, Fittings 1,26,667 = ₹9,00,000. ✓

## Disclosures
- Impairment loss appears as **P&L expense** (reversal = income); revalued asset routes through Revaluation Reserve of that asset first, then P&L.
- For each class of asset: impairment losses recognised in P&L (and line items); reversals in P&L; amounts recognised directly in revaluation surplus.
- If **material**: events/circumstances causing it; amount; for an individual asset — nature + segment; for a CGU — description, amount by asset class and segment, composition change; whether recoverable amount is NSP or VIU (basis of NSP; discount rate if VIU).
- Segment disclosure (AS 17) by reportable segment. Key assumptions (growth, discount rates) are **encouraged**, not mandatory.

## Exam traps & must-remember
- "Higher of" (AS 28) vs "lower of" (AS 2 inventory) — the #1 error.
- Don't waste time computing VIU if NSP already clears carrying amount (and vice versa).
- Exclude uncommitted restructuring, enhancement, financing, tax flows from VIU; test in **current condition**.
- **Pre-tax** rate with pre-tax flows.
- Reset depreciation after impairment AND after reversal.
- CGU: goodwill first (fully), then pro rata; respect the floor.
- Reversal capped at never-impaired line; but reverse only up to **lower of** recoverable and ceiling.
- Never reverse goodwill impairment; CGU reversal never to goodwill.
- Indicators are illustrative, not exhaustive.
- No asset below zero. Carrying amount = cost − depreciation − prior impairment.

## One-line recall
- Impaired if Carrying Amount > Recoverable Amount = **higher of NSP and VIU** (min zero).
- VIU: PV of current-condition cash flows, pre-tax rate; exclude restructuring/enhancement/financing/tax.
- CGU loss: goodwill first, then pro rata, floor = max(own NSP, own VIU, 0).
- Reset depreciation on new base; reverse up to never-impaired ceiling only.
- Goodwill impairment never reversed.
- Golden chain: Indicator → Recoverable = Higher(NSP,VIU) → write down → reset depreciation → reverse later only up to never-impaired line → never reverse goodwill.
