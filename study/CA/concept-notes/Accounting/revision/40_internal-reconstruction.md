# Internal Reconstruction

## Snapshot
Fix a broken balance sheet **inside the same company** — wipe accumulated losses, write assets to fair value, shrink capital — **without a new company and without liquidation**. Every sacrifice pours INTO one pot (**Capital Reduction / Reconstruction A/c**); every loss is spent OUT of it. Contrast: external reconstruction = new company + PC + Realisation A/c.

## Core concepts
The **Capital Reduction Account** is a clearing pot: sacrifices **credited** in, write-offs/write-downs **debited** out. Must close to **nil or a credit (→ Capital Reserve)**. A **debit balance is impossible/error** (scheme under-funded).
**Order of sacrifice:** equity first, then preference, then lenders/creditors — mirrors winding-up priority.

## Key provisions / rules — formulas, treatment; tables

**Two legal routes:**
| | Section 61 — Alteration | Section 66 — Reduction |
|---|---|---|
| Acts | Increase / consolidate / sub-divide / convert / cancel **unissued** shares | Extinguish uncalled liability; cancel **lost paid-up** capital; return surplus capital |
| Resolution | Ordinary (+ Articles) | **Special (75%)** |
| Tribunal (NCLT) | **No** | **Yes** (creditors protected) |
Trap: cancelling **unissued** shares = Sec 61 (no Tribunal); cancelling **paid-up** capital = Sec 66. Sub-division/consolidation change number & face value but **NOT total capital** — no pot effect. Sec 66 clause: cancel capital "lost or unrepresented by available assets".

**Credits to the pot (sacrifices):**
- Equity capital reduced (₹ per share released × shares).
- Preference capital reduced.
- Debenture principal reduced.
- Creditors' haircut (forgiven portion).
- Directors' loan waived.
- Securities Premium / Capital Reserve / General Reserve applied.
- **Revaluation GAIN** (asset written up — only to figure stated in scheme).
- **Accrued debenture interest forgone** (it IS a booked liability → entry).

**Debits to the pot (uses):**
- P&L Dr balance (accumulated losses).
- Fictitious assets (preliminary exp, discount on issue, underwriting commission).
- Goodwill.
- Over-valued assets written down; provision for doubtful debts.
- Contingent liability that crystallises; reconstruction expenses (cash out = pot Dr).
- Loss on asset handed to a claimholder (book − agreed value).

**No entry / not a sacrifice:**
- **Arrears of preference dividend** cancelled → contingent, **disclosure only, NO entry** (unless satisfied by issue of shares → entry).
- **Fresh cash** brought in → Bank Dr / Share Capital Cr — NOT a pot credit.
- **Cash paid to settle a real liability** (e.g. creditor part-settlement) → touches Bank, only the *forgiven* portion is the sacrifice.

**Reverse-engineering ("reduce so pot closes to nil"):**
```
Required equity sacrifice = Total debits − All non-equity credits
Reduction per share = Required equity sacrifice ÷ number of equity shares
New face value = Old face − reduction per share
```
(Fixed reduction → expect a Capital Reserve; solving for it → nil close.)

**Asset handed to a claimholder (touches pot twice):** (i) book value − agreed value = loss/gain → pot; (ii) agreed value + new paper vs old claim: shortfall forgone → claimholder sacrifice (pot credit).

**Golden checks:** pot closes to nil or Capital Reserve (never Dr balance); revised Balance Sheet must balance; Bank must not go negative (bring fresh cash in first). New shares issued in settlement credited at **reduced** face value. Capital Reserve from scheme → bonus shares / absorb capital losses, **never cash dividend**. Company may append **"And Reduced"** to name.

## Journal entries
```
Sacrifice (equity):   Equity Share Capital A/c Dr / To Capital Reduction A/c
Preference reduced:   Pref. Share Capital A/c Dr / To Capital Reduction A/c
Debenture reduced:    Debentures A/c Dr / To Capital Reduction A/c
Accrued deb interest: Interest Accrued A/c Dr / To Capital Reduction A/c
Creditors forgo:      Sundry Creditors A/c Dr / To Capital Reduction A/c
Revaluation up:       Asset A/c Dr / To Capital Reduction A/c
Fresh cash:           Bank A/c Dr / To Share Capital A/c
Write-offs:           Capital Reduction A/c Dr / To P&L, Goodwill, Assets, Provision
Expenses/damages:     Capital Reduction A/c Dr / To Bank
Surplus:              Capital Reduction A/c Dr / To Capital Reserve
```
Asset to debenture-holder in settlement:
```
Debentures A/c Dr; Interest Accrued A/c Dr
   To Investments/Asset A/c (book value); To new Debentures A/c; To Capital Reduction A/c (forgone)
```

## Worked mini-example
Delta Ltd: pot must close to nil. Debits — Goodwill 60,000 + Plant down 50,000 + Stock down 20,000 + Provision 4,000 + P&L 2,20,000 = **₹3,54,000**. Non-equity credits — Debentures 25%×2,00,000 = 50,000 + Creditors 10%×1,40,000 = 14,000 + Freehold revaluation gain 50,000 = **₹1,14,000**.
Required equity sacrifice = 3,54,000 − 1,14,000 = **₹2,40,000** ÷ 60,000 shares = **₹4/share**. So ₹10 share → **₹6**.

## Exam traps & must-remember
- Arrears of preference dividend → NO entry (disclosure).
- Fresh cash is NOT a sacrifice.
- Cash to a creditor: only the forgiven part is a sacrifice; the paid part touches Bank.
- Debit balance in Capital Reduction A/c = error/under-funded (never invent a credit).
- Cancelling unissued shares = Sec 61; cancelling paid-up = Sec 66.
- Revaluation GAINS route through the pot (credit) too.
- **Accrued debenture interest IS a booked debt** — forgoing it IS an entry (vs pref-dividend arrears which are not).
- Asset handed to claimholder touches pot twice.
- New shares issued in settlement at **reduced** face value.
- Bank must not go negative; tally sacrifices vs losses before drafting B/S.
- Capital Reserve from scheme cannot pay dividend.

## One-line recall
- Same company survives; no PC, no Realisation A/c, no new company.
- Sec 61 alteration = light (ordinary resolution, no Tribunal); Sec 66 reduction = heavy (special resolution + Tribunal).
- Capital Reduction A/c: sacrifices Cr in, write-offs Dr out; closes to nil or Capital Reserve.
- Order of sacrifice: equity → preference → lenders/creditors.
- Pref-dividend arrears = no entry; accrued debenture interest forgone = entry.
- Revised Balance Sheet must balance; Bank must not go negative.
