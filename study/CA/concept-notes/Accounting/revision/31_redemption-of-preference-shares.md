# Redemption of Preference Shares

## Snapshot
Preference shares behave like debt but legally sit in **share capital** — the creditors' cushion. Section 55 lets them be redeemed **without a Tribunal** provided the capital cushion stays intact: replace redeemed face value rupee-for-rupee either with **fresh share capital** or with a **Capital Redemption Reserve (CRR)** carved from distributable profit. Capital is substituted, never net-reduced.

## Core concepts
- **Capital maintenance:** members' capital must be kept intact for creditors; returning it needs Section 66 (Tribunal reduction) or Section 68 (buy-back) — Section 55 is a standing, self-policing exception because shares were *born* redeemable.
- **CRR = the part of face value NOT refilled by a fresh issue.** All fresh issue → CRR nil; no fresh issue → CRR = full face value.
- **Premium on redemption travels on a separate track** — it is an extra reward (like a dividend), funded from Securities Premium / free reserves, and **never** enters the CRR identity.

## Key provisions / rules
**Section 55(1)/(2):** No irredeemable preference shares. Redeemable within **20 years** (infrastructure companies: up to **30 years**, min 10% redeemed per year from year 21). Must be **authorised by Articles**. Redeem at par or premium — **never at a discount**.

**Three conditions (Sec 55(2)):**
1. Only **fully paid-up** shares may be redeemed (call up & collect balance first if partly paid).
2. Redeem out of **profits available for dividend** OR **proceeds of a fresh issue made for redemption**.
3. Redeemed out of profits → transfer a sum equal to **nominal (face) value** redeemed to **CRR**.

**Profits available for CRR** (could have been paid as dividend): General Reserve, Surplus in P&L, Dividend Equalisation Reserve, Workmen Compensation Reserve (free excess), voluntary reserves out of profits. **NOT available:** Securities Premium, Capital Reserve, Revaluation Reserve, existing CRR, profit prior to incorporation / capital profits. Acid test: *"Could this have been distributed as dividend?"*

**Master identity:**
- Nominal value redeemed = Fresh issue (nominal) + CRR
- **CRR = Nominal redeemed − Fresh issue nominal**
- **Minimum fresh issue = Nominal redeemed − Profits available for CRR**

**CRR facts:**
- Fresh issue of **shares** (equity OR preference) reduces CRR by its nominal value. **Debentures/loans do NOT** reduce CRR (they add creditors, not capital — full face value still to CRR).
- CRR uses **nominal value only**; premium excluded.
- **Use of CRR = only fully paid bonus shares** (proviso to Sec 55(2) + Sec 63(1); treated as paid-up capital). Cannot pay dividend, write off losses, or write off expenses. (No "Section 55(4)" exists.)

**Premium on redemption:** provided **before** redemption; funded from **Securities Premium first, then free reserves / P&L**. Not part of CRR (only face value is substituted; creditors relied only on face value).

**Fresh issue at a premium:** the **nominal** value drives the CRR/redemption identity (premium on new issue → Securities Premium, cannot create CRR). Issuing at a premium never lets you issue *fewer* shares for the CRR rule; it only changes the cash raised.

**Minimum fresh issue** = last resort (fresh issue dilutes/costs; burn free reserves first). A retention constraint ("keep ₹X reserve") walls off ₹X from the pool, raising the minimum fresh issue by ₹X.

**Cash cross-check** (may bind instead of the CRR rule): Cash after = Cash before + issue proceeds − (face + premium) ≥ any required minimum. Actual fresh issue = **larger of** CRR-minimum and cash-constraint minimum. Issuing more than the CRR-minimum **reduces** CRR (more face value refilled directly).

## Journal entries
```
(a) Make partly-paid fully paid:
    Pref Share Final Call A/c   Dr / To Pref Share Capital A/c
    Bank A/c                    Dr / To Pref Share Final Call A/c
(b) Fresh issue (at premium):
    Bank A/c  Dr [nominal+premium] / To Share Capital [nominal], To Securities Premium [premium]
(c) Amount due:
    Redeemable Pref Share Capital A/c   Dr [face]
    Premium on Redemption of Pref Shares A/c  Dr [premium]
       To Preference Shareholders A/c  [face+premium]
(d) Provide premium:
    Securities Premium A/c  Dr [up to available]
    P&L / General Reserve   Dr [balance]
       To Premium on Redemption of Pref Shares A/c
(e) Pay off:
    Preference Shareholders A/c  Dr / To Bank A/c
(f) Create CRR (= face − fresh issue nominal):
    General Reserve / P&L A/c  Dr / To Capital Redemption Reserve A/c
(g) Bonus later:
    CRR A/c  Dr / To Bonus to Shareholders A/c
    Bonus to Shareholders A/c  Dr / To Equity Share Capital A/c
```
**Sequencing:** cash arrives (fresh issue) before it leaves (payment); **CRR created last** (once fresh issue is known).

## Worked mini-example
**Fresh issue at premium + redemption at premium:** 2,00,000 pref shares of ₹10 (₹20,00,000), redeemable at 10% premium. Securities Premium ₹3,00,000, General Reserve ₹8,00,000, P&L ₹5,00,000. Issue minimum equity of ₹10 at 25% premium.
- Premium on redemption = 10% × 20,00,000 = ₹2,00,000 → from Securities Premium (leaves ₹1,00,000).
- Profits for CRR = 8,00,000 + 5,00,000 = ₹13,00,000.
- Minimum fresh issue (nominal) = 20,00,000 − 13,00,000 = **₹7,00,000** = 70,000 shares at ₹12.50 → cash ₹8,75,000 (nominal 7,00,000 + Sec Prem 1,75,000).
- CRR = 20,00,000 − 7,00,000 = **₹13,00,000**.
- **Cushion proof:** before capital = Equity 40L + Pref 20L = 60L; after = Equity 47L + CRR 13L = 60L. Preserved. ✓

**Cash-binds case:** if a minimum bank balance forces fresh issue of ₹32,00,000 (vs CRR-minimum ₹22,00,000) on ₹40,00,000 redemption → CRR = 40,00,000 − 32,00,000 = ₹8,00,000 (more capital refilled directly, less CRR).

## Disclosures (Schedule III Division I)
- CRR shown as a distinct line under **Reserves and Surplus**.
- Outstanding redeemable preference shares under **Share Capital**; terms of redemption incl. **earliest redemption date** disclosed in Share Capital note.
- **Premium on Redemption**, until paid, is a liability (Other Current Liabilities).
- Movement in CRR (opening/additions/utilisation for bonus/closing) in Reserves note; fresh issue in Share Capital reconciliation.
- **Ind AS 32 (awareness):** mandatorily redeemable pref shares = financial **liability**; dividend = finance cost (opposite of AS treatment).

## Exam traps & must-remember
- **CRR on nominal value only — never on premium.**
- Securities Premium / Capital Reserve / Revaluation Reserve **cannot** create CRR (not distributable). Securities Premium *can* fund redemption premium.
- Only shares issued **specifically for the redemption** reduce CRR (not last year's expansion issue).
- Minimum fresh issue (CRR rule) vs cash-sufficiency — run the bank cross-check; issue the larger.
- Identity uses **nominal**, not cash raised, when fresh shares issued at a premium.
- Only fully-paid shares redeemable (call up partly-paid first).
- CRR usable only for fully paid **bonus shares**.
- Provide premium **before** redemption.
- Retention constraint reduces available profits → raises minimum fresh issue.
- CRR capitalised as bonus is gone — cannot re-use in a later sub-part.
- **Debenture/loan issue does NOT reduce CRR** (whole face value still to CRR).
- Fresh issue of **preference** shares also reduces CRR.
- Redemption at a discount is impermissible.
- Fresh issue at premium *adds* to Securities Premium; funding redemption premium *subtracts* — net the movement for the closing balance.
- Distinguish **CRR (substitutes capital, Sec 55)** from **DRR (reserves cash for debt repayment; released to General Reserve after redemption)**.

## One-line recall
- Refill with new share capital or wall-up with CRR — face value for face value; premium is a side payment, not part of the wall.
- CRR = nominal redeemed − fresh issue nominal; minimum fresh issue = nominal redeemed − profits available.
- CRR from free reserves/P&L only; used only for bonus shares.
- Premium on redemption from Securities Premium then profits; never in CRR.
- Debentures don't reduce CRR; fresh preference shares do.
- Prove: Capital + CRR after = Capital before (cushion preserved).
