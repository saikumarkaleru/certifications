# Amalgamation, Absorption & External Reconstruction

## Snapshot
One company's entire assets, liabilities and shareholders folded into another (or a new) company; transferor is wound up. Governed by **AS 14**. Substance (a five-condition test), not legal form, decides the method: **Pooling (merger)** vs **Purchase**.

## Core concepts
Three legally-distinct but AS-14-identical forms:
| Term | What happens | Survivor |
|---|---|---|
| Amalgamation | 2+ companies wind up; **new company** formed | New co. (A + B → AB) |
| Absorption | **existing** co. takes over another (wound up) | Existing co. |
| External Reconstruction | battered co. wound up; **new co.** (same shareholders) takes over | New co. |

**Terminology:** Transferor Company (vendor, wound up) → Transferee Company (purchasing, survives).
"New company formed" and "merger accounting" are **independent** — decide method only by the five-condition test.

## Key provisions / rules — formulas, treatment; tables

**AS 14 five merger conditions (ALL must hold → Pooling; any one fails → Purchase):**
1. All assets and liabilities of transferor become transferee's.
2. Shareholders holding **≥90%** of face value of equity (excluding shares transferee already holds) become equity shareholders of transferee.
3. Consideration to equity shareholders discharged **wholly by equity shares** (cash only for fractional shares).
4. Business of transferor **intended to be carried on**.
5. **No adjustment to book values** except for uniformity of accounting policies.
(90% measured on outsider block; condition 3 polices only the equity leg — preference holders may get cash/pref.)

| | Merger (Pooling) | Purchase |
|---|---|---|
| Trigger | ALL 5 met | ANY fails |
| Asset/liab values | **Book value** | **Agreed/fair value** |
| Transferor reserves | **Carried over** | **NOT carried over** |
| Goodwill/Cap. Reserve | None (adjust in reserves) | Goodwill if PC>NA; Cap. Res. if PC<NA |

**Purchase Consideration = payment to SHAREHOLDERS only** (NOT total assets). Payments to debenture-holders, creditors, liquidation expenses are **excluded**.
- **Net Assets Method:** Agreed value of assets taken over − Agreed value of liabilities taken over. (Do NOT deduct reserves/share capital — they are owners' claims.)
- **Net Payments Method:** Cash + Equity shares (at **issue value = par + premium**) + Pref. shares + other securities/assets given to shareholders.
- **Intrinsic value / exchange ratio:** Shares to issue = transferor's shares × exchange ratio; PC = shares × issue value. Exchange ratio = transferor's intrinsic value/share ÷ transferee's.
- **Lump-sum:** PC stated directly.

**Goodwill / Capital Reserve (Purchase only):**
```
Goodwill/Cap. Reserve = PC − Net assets (agreed values)
PC > NA → Goodwill (Dr, asset)      "paid more, got goodwill"
PC < NA → Capital Reserve (Cr)      "paid less, got a reserve"
```
Two transferors → show Goodwill for one and Capital Reserve for the other; **no netting**.

**Pooling difference rule:** difference between share capital issued and transferor's share capital adjusted **in reserves** (reduce revenue/free reserves first, then capital reserve). No goodwill.

**Discharge of PC:** shares above par → excess to **Securities Premium**. PC = capital portion + premium portion (do NOT add premium a second time). Total discharged = PC exactly.

**Specific items:** Statutory reserves under Purchase preserved via **Amalgamation Adjustment Reserve** (negative/contra line under Reserves & Surplus). Goodwill on amalgamation amortised (presumed ≤5 years). Inter-company owings & unrealised profit eliminated. Cross-holding: pay only outside shareholders + add transferee's existing investment (carrying value) to cost side; cancel investment on discharge. Debentures taken over → issue own debentures, **not** part of PC.

## Journal entries
**Transferee (Purchase):**
```
Business Purchase A/c  Dr (PC) / To Liquidator of Transferor A/c
[Incorporate:] Assets Dr (agreed); Goodwill Dr (if any)
   To Liabilities (agreed); To Business Purchase; To Capital Reserve (if any)
[Discharge:] Liquidator A/c Dr / To Equity Share Capital; To Securities Premium; To Cash
```
**Transferee (Pooling):** bring in assets, liabilities **and reserves** at book value; difference adjusted in reserves.

**Transferor (Realisation Account):**
```
Realisation A/c Dr / To individual Assets (book value)
Liabilities A/c Dr / To Realisation (taken over, book value)
Transferee Co. A/c Dr / To Realisation (PC due)
Bank/Shares Dr / To Transferee Co. (PC received)
Reserves & P&L(Cr) → Equity Shareholders A/c
Share Capital → Equity Shareholders A/c
Realisation profit/loss → Equity Shareholders A/c
```
**Fictitious assets** (preliminary exp, discount on issue, debit P&L) go **straight to Equity Shareholders A/c**, never through Realisation. All transferor accounts close to zero.

## Worked mini-example
Beta absorbed by Alpha; net assets (agreed) ₹6,60,000; Alpha issues 60,000 equity shares of ₹10 @ ₹12.
PC (Net Payments) = 60,000 × 12 = ₹7,20,000. Values adjusted → condition 5 fails → **Purchase**.
Goodwill = 7,20,000 − 6,60,000 = **₹60,000**. Discharge: Equity Capital ₹6,00,000 + Securities Premium ₹1,20,000.
(If shares issued at par → PC ₹6,00,000 < NA ₹6,60,000 → **Capital Reserve ₹60,000** — flips on issue price.)

## Exam traps & must-remember
- PC ≠ total net assets; excludes payments to debenture-holders/creditors/expenses.
- Reserves carry over under Pooling only, NOT Purchase.
- Any cash beyond fractions / any revaluation / <90% → Purchase.
- Goodwill vs Capital Reserve direction reversed = instant zero.
- Value shares at issue price (par + premium); don't double-count premium.
- Fictitious assets and excluded liabilities left out of net assets.
- Old goodwill: treat per terms (often nil); don't double-count.
- Liquidation expenses borne by transferee — not part of PC (charge per policy; P&L is safer default).
- Cross-holding: pay only outsiders + net the existing investment.
- Absorption ≠ purchase automatically; new company ≠ merger automatically.
- Realisation profit (transferor, vs book values) can differ in sign from transferee's goodwill (vs agreed values).

## One-line recall
- Substance test (5 conditions) picks method: all met → Pooling; any fails → Purchase.
- PC = payment to shareholders only; Net Assets or Net Payments method.
- Goodwill = PC − Net assets (agreed); positive → Goodwill, negative → Capital Reserve (Purchase only).
- Pooling carries reserves + book values, no goodwill; Purchase fair-values, drops reserves.
- Transferor closes via Realisation A/c (fictitious assets bypass it); transferee opens via Business Purchase A/c.
- Balance sheet must tie: Assets = Equity + Liabilities.
