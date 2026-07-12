# Chapter 32 — Buyback of Securities

## Snapshot

Buyback = a company purchasing its **own shares/specified securities** and **cancelling** them (no treasury stock in India), thereby returning surplus capital and shrinking equity. Governed by **Companies Act 2013 — Sec. 68 (power & conditions), Sec. 69 (CRR), Sec. 70 (prohibitions)** + **Companies (Share Capital & Debentures) Rules, 2014**; listed companies additionally under **SEBI (Buy-Back) Regulations**. It matters because it drains the creditors' permanent-capital cushion — so the law fences it with CRR, quantum ceilings and a gearing test.

## Core concepts

- **Dividend vs Buyback:** Dividend is paid out of distributable profit only, leaves share capital & share count untouched, no CRR. Buyback **cancels shares, reduces paid-up capital, triggers CRR**.
- **CRR (Capital Redemption Reserve) = capital's ghost.** When capital is extinguished out of profits, an equal sum of free reserves is frozen into CRR (treated as capital; usable only for bonus). Cushion preserved brick-for-brick.
- **Three limit tests — buyback must satisfy the LOWEST:**
  - (A) 25% of (paid-up capital + free reserves) — ₹ value ceiling
  - (B) 25% of paid-up **equity** capital — equity share count/face ceiling
  - (C) Debt ≤ 2 × owned funds **after** buyback (2:1 gearing)
- **Master CRR formula:** `CRR = Nominal value bought back − Nominal value of fresh issue made for the buyback`.
- **What may be bought:** own equity or other specified securities (ESOPs/sweat equity etc.). **Routes of acquisition:** (1) proportionate from existing holders (tender), (2) open market, (3) from ESOP/sweat-equity holders. Route affects price/fairness only — entries are identical.

## Key provisions / conditions & limits

### Permitted SOURCES (Sec. 68(1))

| Source | Note |
|---|---|
| (a) Free reserves | General Reserve, P&L surplus, any reserve free for dividend |
| (b) Securities Premium | May pay the **premium on buyback** only (not CRR) |
| (c) Proceeds of a FRESH ISSUE | **Cannot** buy back one kind of security out of a fresh issue of the **same kind** |

**Never out of borrowed funds.**

### Free-reserve eligibility

| Reserve | Free? | Fund buyback/premium? | Fund CRR? |
|---|---|---|---|
| General Reserve | Yes | Yes | Yes |
| P&L surplus (credit) | Yes | Yes | Yes |
| Dividend Equalisation Reserve | Yes | Yes | Yes |
| Securities Premium | Free for 25% test (statutory) | Premium on buyback ONLY | **No** |
| Existing CRR | No | No (bonus only) | No |
| Revaluation Reserve | No | No | No |
| Capital Reserve | No | No | No |
| Debenture Redemption Reserve (earmarked) | No | No | No |

### CRR requirement (Sec. 69)

- CRR created **only to the extent buyback is out of free reserves / securities premium**.
- To the extent financed **out of fresh-issue proceeds → NO CRR** (new capital already rebuilt the wall; else double-counting).
- `CRR = Face value bought back − Face value of fresh issue (for the buyback)`.
- **CRR source = free reserves ONLY** (Gen. Reserve / P&L). **Never** Securities Premium or Capital Reserve.
- **CRR use = fully-paid bonus shares only.**
- Fresh issue may be any securities **other than same kind**; even a preference/other-security fresh issue offsets CRR.

### Quantum limits (Sec. 68(2))

| Test | Formula | Measures |
|---|---|---|
| (A) 25% capital+reserves | 25% × (paid-up equity + preference capital + free reserves, incl. Sec. Premium per ICAI) | ₹ value of buyback |
| (B) 25% of equity | 25% × paid-up **equity** capital alone | face value / count of equity shares |
| (C) Debt-equity 2:1 | Debt (secured + unsecured) ≤ 2 × owned funds AFTER buyback → **Max payout = owned funds − Debt/2** | ₹ value — subtract **full price**, not just face |

- Owned funds = paid-up capital + free reserves (incl. securities premium per ICAI).
- Buyback reduces owned funds by the **full cash outflow (price)**: capital ↓ face, reserves ↓ premium, CRR transfer nets to zero internally → total fall = P.
- **Board-route sub-limit:** buyback by board resolution alone → ceiling in (A) drops to **10% of (paid-up equity + free reserves)**, only **one** per year. 2:1 & CRR/destruction rules unchanged.

### Procedural conditions & post-buyback restrictions (Sec. 68(2)-(8), 69, 70)

- **Authorised by Articles**; **special resolution** required (exception: board route ≤10%, once/year).
- **≥1-year gap** between two buybacks (from closure of preceding).
- Complete within **1 year** of the resolution.
- File Form SH-9 (declaration of solvency) before; Form SH-11 (return) after.
- **No buyback while a default subsists** — repayment of deposits, interest, redemption of debentures/preference shares, dividend to any shareholder, or repayment of term loan. Bar lifts once default is remedied.
- **Extinguish & physically destroy** bought-back shares within **7 days** of completion (no treasury stock).
- **No fresh issue of same kind** for **6 months** (except bonus, or discharge of existing obligations — warrants/ESOP/sweat equity/conversion).
- CRR shown in Balance Sheet under Reserves & Surplus; usable only for bonus.

**Forms:** SH-8 (letter of offer, before), SH-9 (solvency, before), SH-11 (return, after), SH-15 (compliance cert by 2 directors incl. MD, after).

## Journal entries

**Step 1 — Fresh issue (only if made to finance buyback):**

| Particulars | Dr | Cr |
|---|---|---|
| Bank A/c | XXX | |
|   To Share Capital A/c (nominal) | | XXX |
|   To Securities Premium A/c (if at premium) | | XXX |

**Step 2 — Create buyback liability:**

| Particulars | Dr | Cr |
|---|---|---|
| Equity Share Capital A/c (face value) | XXX | |
| Premium on Buyback A/c (if price > face) | XXX | |
|   To Equity Shareholders A/c (total buyback amount) | | XXX |

**Step 3 — Absorb premium on buyback (Securities Premium FIRST, then free reserves):**

| Particulars | Dr | Cr |
|---|---|---|
| Securities Premium A/c (to extent available) | XXX | |
| General Reserve / P&L A/c (balance) | XXX | |
|   To Premium on Buyback A/c | | XXX |

**Step 4 — Create CRR (= face bought − fresh-issue face), from free reserves only:**

| Particulars | Dr | Cr |
|---|---|---|
| General Reserve / P&L A/c | XXX | |
|   To Capital Redemption Reserve A/c | | XXX |

**Step 5 — Pay shareholders:**

| Particulars | Dr | Cr |
|---|---|---|
| Equity Shareholders A/c | XXX | |
|   To Bank A/c | | XXX |

**Reserve-debit priority ladder:** Premium → Securities Premium first, then Gen. Reserve, then P&L. CRR → Gen. Reserve / P&L (never Sec. Premium/Capital Reserve). If free reserves are insufficient for premium balance + full CRR, buyback is **scaled down or disallowed** — never plug the CRR gap from securities/capital reserve.

## Worked mini-example

**Orbit Ltd:** Equity capital (₹10) ₹20,00,000; Securities Premium ₹3,00,000; General Reserve ₹8,00,000; P&L ₹4,00,000. Proposes buyback of 40,000 shares @ ₹25 (face ₹10), no fresh issue.

**Test (A):** capital + free reserves = 20 + 3 + 8 + 4 = ₹35,00,000. 25% = **₹8,75,000** max value. Proposed outflow = 40,000 × 25 = ₹10,00,000 → **fails (A)** (premium buyback silently breaches the value ceiling).

**Test (B):** 25% × 20,00,000 = ₹5,00,000 face = 50,000 shares max. Proposed 40,000 ✓.

**Binding = (A).** Buy max = 8,75,000 ÷ 25 = **35,000 shares.** Face = ₹3,50,000; premium = 35,000 × 15 = ₹5,25,000.

**CRR = face bought = ₹3,50,000** (no fresh issue).

Premium absorbed: Sec. Premium ₹3,00,000 + Gen. Reserve ₹2,25,000.

| Reserve | Opening | Premium | CRR | Closing |
|---|---|---|---|---|
| Securities Premium | 3,00,000 | (3,00,000) | — | 0 |
| General Reserve | 8,00,000 | (2,25,000) | (3,50,000) | 2,25,000 |
| P&L | 4,00,000 | — | — | 4,00,000 |
| CRR | 0 | — | +3,50,000 | 3,50,000 |

Cushion check: capital ↓ ₹3,50,000, CRR ↑ ₹3,50,000 → permanent layer preserved. Cash out ₹8,75,000; every figure ties.

*(2:1 illustration — Anchor Ltd: owned funds ₹64,00,000, debt ₹1,10,00,000. Min owned funds after = Debt/2 = ₹55,00,000 → max outflow = 64 − 55 = ₹9,00,000 → at ₹20/sh = 45,000 shares. Here (C) binds below (A) ₹16,00,000.)*

## Exam traps & must-remember

1. **Two 25% tests confused:** (A) = capital + free reserves, in ₹ value; (B) = paid-up **equity only**, in face/count. Run both.
2. **Premium buyback breaches (A):** compute ₹ value of outflow, not just count.
3. **CRR on wrong amount:** CRR = **face/nominal value**, NOT price, NOT premium. Then subtract fresh-issue face.
4. **CRR out of Securities Premium — NEVER.** Sec. Premium pays premium only; CRR from free reserves.
5. **2:1 tested AFTER buyback;** max payout = owned funds − Debt/2. Don't test before or invert.
6. **Forgetting fresh-issue offset** on CRR → over-provides, won't reconcile.
7. **Buyback out of borrowed funds — prohibited.** Loan + no reserves = "cannot buy back."
8. **No treasury stock** — destroy within 7 days; never credit "Treasury Shares."
9. **Premium write-off order:** Securities Premium first, then free reserves.
10. **Capital/Revaluation Reserve** are not free reserves — can't fund buyback, premium or CRR.
11. **Round shares DOWN** after dividing ₹ ceiling by price.
12. **2:1: subtract full price** (face + premium), not just face.
13. **Use updated figures** after any prior action (fresh issue/bonus/pref redemption) for the tests.
14. **CRR is capital-like** — not a free reserve for the next dividend/buyback/premium.
15. **25%/2:1 tests are buyback-only** — a Sec. 55 preference redemption has no quantum or gearing ceiling.
16. **Board route = 10% ceiling** (not 25%), once/year — watch "the Board resolved."
17. **Default gate:** if default subsists, buyback barred regardless of reserves.

**vs Preference Redemption (Sec. 55):** same CRR engine (Capital → CRR, less fresh issue), CRR from free reserves only; but pref redemption has **NO 25% and NO 2:1 test**, and premium goes off Securities Premium/P&L. Combined problems: CRR is **cumulative** (one account), free reserves are a **shared pool** (run one running balance), and buyback tests use **post-redemption** figures.

## One-line recall

- **Law:** Sec. 68 (conditions), 69 (CRR), 70 (prohibitions) + SCD Rules 2014.
- **Buyback ≤ lowest of** 25% cap+reserves (value), 25% equity (count), Debt ≤ 2× owned funds after.
- **CRR = face bought − fresh-issue face**, from free reserves only, usable for bonus only.
- **Premium on buyback:** Securities Premium first, then free reserves.
- **Sources:** free reserves / securities premium / fresh-issue proceeds — never borrowed, never same-kind fresh issue.
- **Fences:** AoA + special resolution (or board ≤10%), 1-yr gap, complete in 1 yr, destroy in 7 days, no same-kind issue for 6 months, no buyback in default.
