# Carbon Accounting & ESG Data/Ratings

## What you'll be able to do

Build a company's **greenhouse-gas footprint from scratch** under the GHG Protocol: classify activities into **Scopes 1, 2 and 3**, apply **emission factors**, compute **location-based vs market-based** Scope 2, and total the inventory in **tCO₂e**. You'll also read the **ESG ratings landscape** (MSCI, Sustainalytics, CDP, S&P) — how each scores, why they disagree — and spot **greenwashing** and where **assurance** fits.

## The essentials

**GHG Protocol** is the global carbon-accounting standard. Emissions are grouped into three scopes:

| Scope | Definition | Examples |
|---|---|---|
| **Scope 1** | Direct emissions from owned/controlled sources | Company boilers, furnaces, owned vehicles, process CO₂ (e.g., cement calcination), refrigerant leaks |
| **Scope 2** | Indirect from **purchased energy** | Purchased electricity, steam, heating/cooling |
| **Scope 3** | All other **value-chain** indirect (15 categories) | Purchased goods, business travel, commuting, use of sold products, logistics, waste, investments (financed emissions) |

**Seven greenhouse gases**, each converted to **CO₂-equivalent (CO₂e)** via its **Global Warming Potential (GWP)**: CO₂ (GWP 1), CH₄ (~28), N₂O (~265), plus HFCs/PFCs/SF₆/NF₃ (hundreds to tens of thousands). *tCO₂e = activity × emission factor × GWP.*

**Emission factor (EF)** = emissions per unit of activity. Sources: **IPCC**, **DEFRA/UK Gov** (widely used, free), **India's CEA** grid emission factor (for Scope 2 electricity — India ~0.7-0.8 tCO₂/MWh depending on year; always cite the CEA version used).

**Scope 2 — two methods (report both):**
- **Location-based:** use the *grid average* EF (e.g., CEA national/regional factor).
- **Market-based:** use EF of the *contracted* electricity (e.g., 0 for renewable PPAs backed by instruments/RECs). This is where renewable purchases show up.

**ESG ratings landscape:**

| Provider | What it rates | Scale | Angle |
|---|---|---|---|
| **MSCI ESG** | Financially material ESG risk mgmt vs peers | **AAA-CCC** | Risk/opportunity, industry-relative |
| **Sustainalytics** (Morningstar) | **ESG Risk** = unmanaged risk to enterprise value | **0-40+**, *lower = better* | Absolute risk exposure |
| **CDP** | Disclosure on climate/water/forests | **A to D-** | Disclosure quality, not risk |
| **S&P Global CSA** | Corporate Sustainability Assessment (DJSI) | **0-100** | Questionnaire-driven |

*Key trap:* **MSCI high letter = good; Sustainalytics high number = bad.** They also weight materiality differently, so the *same firm* can look strong on one and weak on the other — always ask *which methodology* and *what's material to that industry*.

**Greenwashing** — overstating green credentials: vague "eco-friendly" claims, cherry-picked metrics, Scope 3 omission, net-zero targets with no interim milestones, buying cheap offsets instead of cutting. **Assurance** (limited/reasonable, per ISAE 3000 / SEBI BRSR Core) is the antidote — an independent check that the numbers are fairly stated.

## Hands-on — step by step

**Worked example: "Deccan Cements Ltd" FY26 carbon footprint.** Activity data:
- Coal burnt in kiln: 4,000 tonnes; EF (coal) ≈ 2.42 tCO₂e per tonne.
- Diesel in owned trucks: 120,000 litres; EF ≈ 0.00268 tCO₂e/litre.
- Process CO₂ from limestone calcination: 3,100 tCO₂e (given, from clinker chemistry).
- Purchased electricity: 3,500 MWh; CEA grid EF = 0.71 tCO₂/MWh; but 900 MWh sourced via a solar PPA (EF 0).
- Business air travel: 250,000 passenger-km; EF ≈ 0.00015 tCO₂e/pkm.
- Purchased clinker/goods (Scope 3 cat 1): 5,000 tCO₂e (from supplier data).

**Step 1 — Scope 1 (direct).**
- Coal: 4,000 × 2.42 = **9,680 tCO₂e**
- Diesel: 120,000 × 0.00268 = **321.6 tCO₂e**
- Process CO₂: **3,100 tCO₂e**
- **Scope 1 total = 9,680 + 321.6 + 3,100 = 13,101.6 tCO₂e**

**Step 2 — Scope 2 (purchased electricity), both methods.**
- **Location-based:** 3,500 MWh × 0.71 = **2,485 tCO₂e** (grid average applied to all consumption).
- **Market-based:** only non-renewable 2,600 MWh × 0.71 = **1,846 tCO₂e**; the 900 MWh solar PPA = 0. The 639 tCO₂e gap is the credit for renewable procurement.

**Step 3 — Scope 3 (value chain).**
- Air travel (cat 6): 250,000 × 0.00015 = **37.5 tCO₂e**
- Purchased goods (cat 1): **5,000 tCO₂e**
- **Scope 3 (partial) = 5,037.5 tCO₂e** (full inventory would screen all 15 categories).

**Step 4 — Total inventory.**

| Scope | tCO₂e (location-based S2) |
|---|---|
| Scope 1 | 13,101.6 |
| Scope 2 (location) | 2,485.0 |
| Scope 3 (partial) | 5,037.5 |
| **Total** | **20,624.1** |

**Step 5 — Intensity metric** (ties to BRSR): if turnover = ₹4,200 cr, Scope 1+2 intensity = (13,101.6 + 2,485)/4,200 = **3.71 tCO₂e per ₹ cr**. Per tonne of cement (say 500,000 t) = (15,586.6)/500,000 = **0.031 tCO₂e/tonne** — the decision-useful figure for a cement peer comparison.

**Step 6 — Document EFs & sources** so it survives assurance: a factor register listing every EF, its source (CEA v2025, DEFRA 2025, IPCC), and the activity-data source (fuel invoices, electricity bills, travel system).

## The output

**GHG inventory statement (assurance-ready):**

> **Deccan Cements Ltd — GHG Inventory FY 2025-26** (GHG Protocol, operational control)
> | Scope | tCO₂e | Basis |
> |---|---|---|
> | Scope 1 — stationary + mobile + process | 13,101.6 | Fuel invoices; DEFRA/IPCC EFs |
> | Scope 2 — location-based | 2,485.0 | 3,500 MWh × CEA 0.71 |
> | Scope 2 — market-based | 1,846.0 | Net of 900 MWh solar PPA |
> | Scope 3 — cat 1 + cat 6 (partial) | 5,037.5 | Supplier + travel data |
> | **Total (location-based)** | **20,624.1** | |
> | Scope 1+2 intensity | 3.71 tCO₂e/₹ cr | vs 4.02 prior year |
>
> *Assurance:* reasonable assurance per SEBI BRSR Core / ISAE 3000. EF register annexed. Base year FY22 restated for the solar PPA.

## Checks, gotchas & red flags

- **Don't double-count.** An emission is Scope 1 for the emitter and Scope 3 for the buyer — never both within one entity's inventory.
- **Report *both* Scope 2 methods.** Reporting only market-based hides grid reality; only location-based hides renewable effort. GHG Protocol wants both.
- **Cite the exact EF vintage** (CEA year, DEFRA year). A stale grid factor is the top assurance finding.
- **Scope 3 is usually the biggest scope** (often 70-90% of a footprint) — omitting it is the classic greenwash. ISSB S2 now requires it (with phasing).
- **Offsets ≠ reductions.** Netting gross emissions with offsets to claim "net zero" without cutting gross is a red flag; disclose gross and offsets separately.
- **Ratings ≠ performance.** A high MSCI rating measures *risk management relative to peers*, not low emissions. Don't equate a good rating with a green company.
- **Unit hygiene:** tonnes vs kg, MWh vs kWh, CO₂ vs CO₂e — one slip moves totals by 1000×.

## Interview drill

**Q1. "Classify: employee flights, the diesel in our delivery trucks, and our purchased electricity."**
*A:* Owned-truck diesel is **Scope 1** (direct, controlled source). Purchased electricity is **Scope 2** (indirect from bought energy). Employee flights are **Scope 3, category 6 (business travel)** — value-chain indirect. If we used a third-party logistics fleet instead of owned trucks, that diesel would shift to Scope 3 category 4.

**Q2. "Compute Scope 2 location vs market-based: 3,500 MWh, grid EF 0.71, of which 900 MWh is a solar PPA."**
*A:* Location-based applies grid average to everything: 3,500 × 0.71 = **2,485 tCO₂e**. Market-based credits the contracted renewable: non-renewable 2,600 × 0.71 = **1,846 tCO₂e**, solar = 0. The 639 tCO₂e difference is the reported benefit of the PPA; GHG Protocol requires disclosing both.

**Q3. "MSCI rates this firm AAA but Sustainalytics gives it a 32 — is that contradictory?"**
*A:* Not necessarily. MSCI is industry-relative letter grades where AAA = best-managed risk versus peers; Sustainalytics is an absolute *ESG Risk* score where **higher is worse**, so 32 (high) signals substantial unmanaged risk. They weight materiality differently and answer different questions — I'd read the methodology and the underlying material issues rather than treat the labels as comparable.

## Learn/practise (free)

- **GHG Protocol** — free Corporate Standard, Scope 2 Guidance, Scope 3 Standard, and Excel calculation tools.
- **DEFRA/UK Government conversion factors** (annual, free) and **IPCC** EFs; **India CEA CO₂ Baseline Database** for the grid factor.
- **CDP guidance** and **MSCI/Sustainalytics public methodology** documents — read one of each to see why scores diverge.
- **Rehearse:** take any company's fuel and electricity data from its BRSR/annual report and rebuild the Scope 1+2 inventory in Excel with an EF register, then compute intensity. Do it for a manufacturer and a services firm to feel how the scope mix flips (Scope 3 dominates services via purchased goods & travel).
