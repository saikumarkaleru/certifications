# Chapter 33 — Bonus Issue

## Snapshot
Bonus issue = **capitalisation of reserves** into **fully-paid** bonus shares; reserve ↓, capital ↑, **net worth unchanged**, no cash moves. Governed by **Sec 63, Companies Act 2013 + Rule 14** (Share Capital & Debentures Rules 2014); listed cos. also **SEBI ICDR 2018, Ch. XI (Reg 293–295)**. It hardens distributable reserve into permanent capital (creditor buffer ↑), so the law is relatively permissive.

## Core concepts
- Capitalisation is a **one-way ratchet** — reversible only via Sec 66 (NCLT capital reduction) or Sec 68 (buy-back), never a reversing entry.
- **Realisation test** for any reserve: did real value (cash / realised gain) flow in, AND is it freely distributable/unencumbered? Both limbs must pass.
- Bonus ≠ dividend: dividend is a distribution (value out); bonus locks value in — hence **not in lieu of dividend** (but bonus *alongside* a separate cash dividend is legal).

## Key provisions / conditions & limits

### Sec 63(1) — Permitted sources
| Source | Note |
|---|---|
| (a) Free reserves | Gen. Reserve, credit balance of P&L — distributable |
| (b) Securities Premium (Sec 52) | Statutory reserve, permitted use |
| (c) Capital Redemption Reserve | Only for fully-paid bonus |

**Free reserves — Sec 2(43):** distributable per latest audited BS, **excluding** unrealised/notional gains & revaluation of assets — **even if credited to P&L**. (So strip a fair-value gain sitting inside P&L surplus.)

### Prohibited sources
Revaluation Reserve; unrealised/notional/fair-value gains; Capital Reserve **not realised in cash** (ICAI default: treat as unavailable unless realised — state assumption); earmarked statutory reserves (Investment Allowance etc.); **DRR while debentures outstanding**; **profit prior to incorporation**; **Shares Forfeited A/c**.

### GOLDEN restriction
Securities Premium & CRR → **fully-paid bonus ONLY**. They **cannot** convert existing partly-paid shares to fully paid. **Free reserves can do BOTH.**

### Sec 63(2) — Six conditions (ALL must hold)
1. Authorised by **Articles** (else alter first).
2. Recommended by **Board** + authorised in **general meeting**.
3. No default on interest/principal of **fixed deposits or debt securities** (NOT "any loan").
4. No default on **statutory dues of employees** (PF, gratuity, bonus).
5. Partly-paid shares **made fully paid** on/before allotment.
6. Other prescribed conditions (Rule 14).

**Sec 63(3):** not in lieu of dividend; must be fully paid.
**No withdrawal** once board decision announced (Rule 14; SEBI for listed).

### SEBI ICDR (listed only)
- Only free reserves / **securities premium collected in cash** / CRR. Premium collected **in kind** (non-cash amalgamation) barred.
- No bonus out of revaluation reserve.
- Complete within **15 days** (if no shareholder approval needed) or **2 months** (if approval needed).
- Protect outstanding convertible-holders (reserve simultaneous bonus).

### Formulas
- Bonus shares = Existing shares × (bonus ratio num ÷ denom)
- Bonus amount = Bonus shares × face value
- If post-bonus capital > **authorised capital** → increase authorised first (Sec 61 ordinary resolution, file **Form SH-7** under Sec 64, pay fee). **NOT a journal entry.**

## Journal entries

**Step 1 — Capitalise reserves:**
```
General Reserve A/c            Dr
Securities Premium A/c         Dr
Capital Redemption Reserve A/c Dr
Profit & Loss A/c              Dr
    To Bonus to Shareholders A/c
```
**Step 2A — Issue fully-paid bonus shares:**
```
Bonus to Shareholders A/c   Dr
    To Equity Share Capital A/c
```
**Step 2B — Making partly-paid fully paid (FREE RESERVES ONLY):**
```
Equity Share Final Call A/c  Dr
    To Equity Share Capital A/c        (call due)
Bonus to Shareholders A/c    Dr
    To Equity Share Final Call A/c     (free reserve applied; no cash)
```
("Bonus to Shareholders A/c" = temporary bridge, never on BS. If asked "through Bonus A/c," show both steps.)

## Worked mini-example
Vayu Ltd: Equity capital ₹20,00,000 (2,00,000 × ₹10); Sec. Premium ₹3,00,000; CRR ₹2,00,000; Gen. Reserve ₹6,00,000; P&L ₹4,00,000; Revaluation Reserve ₹5,00,000. Bonus **2:5** at par; policy statutory reserves first; authorised ₹30,00,000.

- Bonus shares = 2,00,000 × 2/5 = **80,000** → ₹8,00,000. New capital 28,00,000 < 30,00,000 ✓.
- Revaluation Reserve ₹5,00,000 **excluded**. Usable pool = 3+2+6+4 = ₹15,00,000 ≥ 8 ✓.
- Apply: Sec. Premium 3,00,000 + CRR 2,00,000 + Gen. Reserve 3,00,000 = 8,00,000.

Entry: Sec Premium Dr 3,00,000; CRR Dr 2,00,000; Gen Res Dr 3,00,000 → Bonus A/c 8,00,000; then Bonus A/c Dr 8,00,000 → Equity Share Capital 8,00,000.
Net worth ₹40,00,000 before = after ✓. Revaluation Reserve untouched.

## Exam traps & must-remember
1. **Revaluation Reserve** — never usable (unrealised). Cross out on sight.
2. **Capital Reserve** usable only if realised in cash; if silent/on revaluation → not available (state assumption).
3. Sec Premium / CRR **cannot** make partly-paid shares fully paid — free reserves only.
4. Check **authorised capital** breach → increase first (Sec 61/SH-7). Never journal-entry the increase.
5. Bonus ratio applies to **updated** share count after any prior tranche/call.
6. "Bonus in lieu of dividend" prohibited (Sec 63(3)); bonus + separate dividend OK.
7. Bonus shares must be **fully paid**.
8. Default bar = **FDs & debt securities** + employee statutory dues — not general bank loans.
9. **Net worth UNCHANGED** — only internal split shifts.
10. Strip **impure fair-value gain** out of P&L surplus (Sec 2(43)) even if credited to P&L.
11. Silent order → prudent: exhaust restricted reserves (Sec Premium, CRR) first; state assumption.
12. Listed: SEBI windows 15 days / 2 months; only **cash** securities premium.
13. DRR / profit-prior-to-incorporation / forfeited shares → not free reserves.
14. Bonus vs **stock split**: split sub-divides face value, no reserve/capital change; bonus capitalises reserves (capital ↑, reserves ↓).
15. **EPS (AS 20):** bonus deemed to exist from **earliest period presented** → restate prior EPS retrospectively; **no time-apportionment**.
16. Hidden cost: larger capital → larger future dividend outflow if rate on face value maintained.

## One-line recall
- Sec 63 + Rule 14; SEBI ICDR Ch. XI (listed).
- Sources: free reserves / securities premium / CRR. Never revaluation/notional.
- Sec Premium & CRR = fully-paid bonus ONLY; free reserves do both.
- Net worth NIL change; capital ↑ = reserves ↓.
- Authorised-capital increase = procedure (Sec 61/SH-7), not an entry.
- EPS restated retrospectively; disclose 5-yr aggregate bonus issued without cash.
- Golden check: total reserves + capital before = after.
