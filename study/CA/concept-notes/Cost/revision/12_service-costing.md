# Chapter 12 — Service Costing

## Snapshot
Service (operating) costing measures the cost of an **intangible, non-storable, instantly-consumed** output. No product → no stock valuation, no WIP. The whole skill is **choosing the right denominator** — usually a **composite cost unit** fusing a quantity dimension × a service dimension (tonne-km, passenger-km, patient-day, kWh, room-day). Cost is **capacity/standing-charge dominated**, so occupancy/utilisation drives cost per unit.

## Core concepts
- **Composite (compound) cost unit** = quantity dimension × service dimension. Use when both dimensions vary and matter; else a **simple unit** (per meal, per ticket, per kilolitre) suffices.
- **Internal (captive) service** (boiler, captive power, transport pool, canteen): recover **cost, not price** — deliverable is a **transfer/recovery rate**; usually **no profit margin**. **External** service: cost feeds a fare/tariff with margin.
- Behaviour identity: Cost per unit = (F + vN) ÷ N = F/N + v. Fixed term collapses as N (utilisation) rises → "occupancy is destiny".

## Key provisions / rules

**Core formula**: Cost per composite unit = Total operating cost ÷ Total composite units.

**Cost classification (transport template)**
- **Standing (fixed)**: time-based depreciation, insurance, road tax, permit, garage/depot rent, monthly salaries, admin/supervision, licence fees, interest on capital.
- **Running (variable)**: fuel, lubricating oil, tyres/tubes, mileage-based depreciation, per-trip/per-km/commission wages.
- **Maintenance (semi-variable)**: repairs, spares, servicing, painting, overhauls.

**Tonne-km / passenger-km — two builds**
- **Absolute (weighted)** = Σ(load on each leg × distance of that leg). **Default for cost.**
- **Commercial (average)** = Average load × Total distance. Use only if stated.
- Heavy loads on long legs ⇒ absolute > commercial; on short legs ⇒ absolute < commercial; equal when load same each leg.

**Denominator recipe (transport)**
1. Effective days = total days − idle/maintenance days.
2. Distance = days × trips × km per trip (×2 for return legs of a round trip).
3. Capacity used = seats × load factor (or tonnes × utilisation).
4. Composite units = Σ(load × distance) per leg (absolute).

**Offered vs sold**: Cost per km/seat-km (offered) = efficiency; Cost per passenger-km (sold) = pricing = cost per seat-km ÷ load factor.

**Pricing (watch the base)**
- Profit on **cost**: Fare = Cost × (1 + m).
- Profit on **takings/sales**: Fare = Cost ÷ (1 − m).

**Other sectors**
- Hospital: patient-days = beds × days × occupancy% (+ hired beds × days occupied); include hire charge in cost.
- Hotel: occupied room-days = rooms × days × occupancy% (per season); divide by **occupied**, not available.
- Power/steam/water: divide cost by units **delivered/consumed** (net of transmission/evaporation loss), not units generated.

**Depreciation flag**: per-annum/straight-line ⇒ **standing**; per-km/mileage ⇒ **running**.

## Worked mini-example
Bus: 50 km one-way, 40 seats, 2 round trips/day, 25 days, 80% load factor.
Distance = 50×2×2×25 = 5,000 km. Passengers = 40×80% = 32. Passenger-km = 5,000×32 = 1,60,000.
Total operating cost = ₹1,18,000. Cost/passenger-km = 1,18,000 ÷ 1,60,000 = ₹0.7375.
Fare at 20% on takings = 0.7375 ÷ 0.80 = ₹0.9219/passenger-km.
Check: takings 0.9219×1,60,000 = ₹1,47,500; profit 29,500 = 20% of takings ✓.
(If "20% on cost": fare = 0.7375×1.20 = ₹0.885 — different answer.)

## Exam traps & must-remember
1. **Depreciation basis** — time ⇒ standing; km ⇒ running. #1 trap.
2. **Profit on cost vs on takings**: ÷(1−m) for takings, ×(1+m) for cost.
3. Count **both legs** for distance/fuel, but tonne-km only for **loaded** leg (+ back-load).
4. **Absolute vs commercial** — default absolute unless "commercial" stated.
5. Use **occupied** capacity, not available, when occupancy given.
6. Subtract **idle/maintenance days** to get effective running days.
7. "2 round trips" = 4 one-way legs.
8. Hired beds/rooms add to **both** cost and denominator.
9. Wage basis decides bucket: monthly salary = standing; per-trip/km = running.
10. Convert fuel: ₹90/L at 4 km/L = ₹22.50/km (two-step).
11. Simple vs composite: don't cost "per patient" or "per tonne" when a dimension varies.
12. Power/water/steam: divide by units **delivered**, not generated (loss recovered from what arrives).
13. **Include interest on capital** if given (standing charge); don't drop as "financial".
14. **No margin** on internal/captive service unless output sold externally.
15. Never average per-unit rates across mixed fleet/bed-class/season — build total cost & total units, divide once (or weight by volumes).

## One-line recall
- Cost per composite unit = Total operating cost ÷ Total composite units.
- Composite unit = quantity dimension × service dimension.
- Absolute tonne-km = Σ(load × distance per leg); default over commercial.
- Fare = Cost ÷ (1 − m) on takings; = Cost × (1 + m) on cost.
- Divide by units delivered/occupied, not generated/available.
- Depreciation: per-annum = standing, per-km = running.
