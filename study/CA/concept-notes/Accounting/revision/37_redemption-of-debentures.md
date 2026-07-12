# Chapter 37 — Redemption of Debentures

## Snapshot
Redemption = discharging (repaying + cancelling) the debenture liability per the trust deed (par or premium). Creditor protection via two locks: **DRR** (fence profit from dividend — Sec 71(4)) and **DRI** (stockpile liquid cash — Rule 18(7)). Plus splitting **cum-/ex-interest** on open-market purchases. Redemption is a **timeline** — right entry on the right date.

## Core concepts
- **DRR** = appropriation of **profit** (equity; no cash), sized on **outstanding** debentures, built **before** redemption, released to General Reserve **after**.
- **DRI** = **cash** invested in liquid securities, sized on debentures **maturing next year**, in place by **30 April**.
- **Four methods:** Lump sum (bullet) · Instalments (drawing lots) · Open-market purchase · Conversion. (Conversion = no cash → DRR/DRI not needed.)
- **Three sources:** Out of profits (DRR = redemption amount, conservative) · Out of capital (only statutory minimum DRR) · Partly both (10% DRR = the middle path).

## Key provisions / conditions & limits

### DRR — Sec 71(4) + Rule 18(7)(b) (post 16 Aug 2019 amendment)
| Company | DRR |
|---|---|
| Banks; AIFIs regulated by RBI | **No DRR** |
| Listed NBFCs / listed HFCs | **No DRR** |
| Other **listed** companies | **No DRR** |
| Unlisted NBFCs / HFCs — privately placed | **No DRR** |
| **Other unlisted companies** | **DRR = 10% of outstanding value of debentures** |

- Created out of **profits available for dividend**; before redemption; released to **General Reserve** after (never back to P&L / dividend).
- Base = **outstanding face value** (converted/redeemed portions drop out); **NOT** premium-inclusive amount.
- **Pre-2019 rate = 25%** (of debentures to be redeemed) — use if problem is dated pre-2019 or says 25%. State regime applied.
- One-time adequacy test — build to level, hold; in instalment problems create full DRR before first instalment, release after last.

### DRI — Rule 18(7)(c)
- Only if **DRR is required** (no DRR → no DRI).
- **≥15%** of debentures **maturing during the FY ending next 31 March**, invested/deposited **on or before 30 April**, kept ≥15% until redemption complete.
- Base = debentures **maturing in coming FY**, not total outstanding, not 15% of DRR.
- Permitted (**unencumbered**): scheduled-bank deposit; Central/State Govt securities; securities per Sec 20(a)–(d) Indian Trusts Act 1882; bonds of another listed company. (Banking cos.: deposit route only.)
- DRI **interest = company's income** (to P&L); enlarges cash pool but does **not** reduce holders' dues.

### Open-market purchase — cum vs ex-interest
Accrued interest = **Face × coupon rate × (months since last coupon ÷ 12)**.

| Quotation | Includes interest? | Cost of debenture | Total cash paid |
|---|---|---|---|
| **Cum-interest** | Yes | Quoted price − accrued | Quoted price |
| **Ex-interest** | No | Quoted price | Quoted price + accrued |

- Interest slice → **Interest on Debentures A/c** (finance cost).
- **Cancellation profit** (Face − Cost, if Cost < Face) → **Capital Reserve**. **Loss** (Cost > Face, e.g. bought above par) → **Statement of P&L**.
- **For immediate cancellation** → debit 12% Debentures directly. **Held as investment** → route via **Investment in Own Debentures A/c**; interest on own debentures neutralised while held; cancel later, difference to Capital Reserve/P&L.

### Sinking Fund (Debenture Redemption Fund) method
- Annual set-aside = **Redemption amount × SF factor**, factor = **r ÷ [(1+r)ⁿ − 1]**.
- Interest earned on **opening** investment balance, reinvested (Year-1 interest = 0).
- **No fresh investment in final year** (sold to redeem).
- Sale profit/loss routed through Fund A/c; on maturity transfer Fund → **General Reserve**.

## Journal entries
```
Create DRR:  Surplus in Statement of P&L A/c  Dr   → Debenture Redemption Reserve A/c
Make DRI:    Debenture Redemption Investment A/c Dr → Bank A/c            (15%, by 30 Apr)
Realise DRI: Bank A/c Dr → DRI A/c (+ interest received, if any)
Amount due:  12% Debentures A/c Dr (face) + Premium on Redemption A/c Dr (premium)
                 → Debenture-holders A/c
Final coupon: Interest on Debentures A/c Dr → Debenture-holders / Bank
Payment:     Debenture-holders A/c Dr → Bank A/c
Release DRR (after redemption): DRR A/c Dr → General Reserve A/c
Cancel own (bargain): 12% Debentures A/c Dr (face) → Own Debentures A/c (cost)
                 + Profit on Cancellation A/c; then Profit on Cancellation A/c Dr → Capital Reserve
```
Premium on Redemption is a **liability created at issue** (against Loss on Issue of Debentures) — at redemption merely paid off, not a fresh expense.

## Worked mini-example
Meridian Ltd (unlisted): ₹20,00,000 of 12% Debentures @ ₹100, redeem **at par 31 Mar 2027**. Current rules.
- DRR = 10% × 20,00,000 = **₹2,00,000** (created FY2025-26): Surplus in P&L Dr → DRR.
- DRI = 15% × 20,00,000 = **₹3,00,000** by **30 Apr 2026**: DRI Dr → Bank.
- On maturity: Bank Dr 3,00,000 → DRI (realise); 12% Debentures Dr 20,00,000 → Holders → Bank 20,00,000.
- Release DRR: DRR Dr 2,00,000 → General Reserve.
- **If listed:** no DRR, no DRI — only the due + pay ₹20,00,000 survives.

Open-market: 1,000 own debentures @ ₹98, 4 months accrued (last coupon 31 Mar), 12% → accrued = 1,00,000 × 12% × 4/12 = ₹4,000. **Cum:** cost = 98,000 − 4,000 = ₹94,000, profit ₹6,000 → Capital Reserve. **Ex:** cost = ₹98,000, cash 1,02,000, profit ₹2,000 → Capital Reserve.

## Exam traps & must-remember
1. **DRR %**: 10% (unlisted non-exempt) post-2019; 25% pre-2019; nil for banks/AIFIs/NBFCs-HFCs/listed. Read status + date.
2. **DRI base = debentures maturing in coming year**, not total outstanding, not 15% of DRR. DRI = cash; DRR = profit appropriation.
3. DRR needs **actual profits available for dividend**.
4. **Cum: subtract** accrued; **Ex: add** accrued. Most common slip.
5. Count accrued from **last coupon date** to purchase date (half-yearly may be 30 Sep).
6. Cancellation **profit → Capital Reserve**; **loss → P&L** (never Capital Reserve for loss).
7. DRR released to **General Reserve**, never P&L/dividend.
8. Sinking fund: interest on **opening** balance, reinvested — don't omit.
9. Premium on redemption = liability from **issue**, not fresh expense at redemption.
10. Held-as-investment (via Investment in Own Debentures) vs immediate cancellation — read wording.
11. DRR on **face/outstanding value only**, not face + premium.
12. Bought **above par** → loss → P&L.
13. DRI must be funded **on/before 30 April**, not on maturity date.
14. Don't forget **final coupon interest** at redemption (separate from principal).
15. DRI interest income does **not** reduce amount due to holders.

**Presentation (Schedule III):** Debentures → Long-term Borrowings (or **Current maturities** in Other Current Liabilities if within 12 months); DRR / DRF → Reserves & Surplus; DRI → Investments; Premium on Redemption → Other Liabilities; cancellation profit → Capital Reserve. Interest accrued **but not due** distinct from accrued **and due**.

## One-line recall
- DRR (Sec 71(4)): 10% of outstanding, out of profits, before redemption, → General Reserve after; nil for listed/banks/NBFCs.
- DRI (Rule 18(7)): ≥15% of debentures maturing next FY, by 30 April, liquid unencumbered securities; only if DRR required.
- Cum: cost = price − accrued; Ex: cost = price, cash = price + accrued. Accrued = Face × rate × months/12.
- Cancellation gain → Capital Reserve; loss → P&L.
- Sinking fund set-aside = amount × r/[(1+r)ⁿ−1]; interest on opening balance reinvested.
