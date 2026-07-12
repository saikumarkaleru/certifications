# Chapter 34 — Rights Issue

## Snapshot
Rights issue = further shares offered **first to existing equity shareholders, pro-rata**, at a price (usually discounted), before outsiders — the statutory anti-dilution / pre-emptive mechanism. Governed by **Sec 62(1)(a), Companies Act 2013**. Pro-rata + discount makes it **wealth-neutral**: the discount reappears as the **value of the right**.

## Core concepts
- Three dilutions: **ownership/voting**, **wealth/value**, **EPS**. Rights issue cures wealth & voting for a subscriber; EPS dilution is unavoidable (more shares on same profit).
- Right is an **entitlement, not obligation**: subscribe, renounce (sell), or lapse. Only **lapsing** loses money (= VR forgone).
- Bonus and rights are the **same operation** on a spectrum: S = 0 → bonus; S = M → non-event.

## Key provisions / conditions & limits

### Sec 62(1) — three routes for further issue
| Route | Section | To whom | Approval |
|---|---|---|---|
| Rights | 62(1)(a) | Existing equity holders pro-rata | **Board resolution** |
| ESOP | 62(1)(b) | Employees under scheme | Special resolution (ordinary for private co.) |
| Preferential / private placement | 62(1)(c) | Anyone | **Special resolution + registered valuer** |

- Sec 62 bites only on issue of **"further" shares** by a company having share capital (not initial subscribers' shares).
- **Sec 62(3):** loan/debenture conversion pre-approved by special resolution *before* raising the loan → exempt from pro-rata.

### Mandatory features of a 62(1)(a) offer
1. **Pro-rata** to paid-up capital on record date.
2. **Letter of offer** stating shares offered & terms.
3. Offer open **≥15 and ≤30 days**; non-acceptance = **deemed declined**. (Shorten if **≥90% members** consent in writing/electronic.)
4. **Right of renunciation** included unless articles provide otherwise [62(1)(a)(ii)].
5. Unsubscribed shares disposed by Board in a manner **"not disadvantageous to shareholders and the company"** [62(1)(a)(iii)].

**Pricing:** S < M for attractiveness; no registered valuer needed (pro-rata self-protects). **Never below face value** (Sec 53; narrow Sec 54 sweat-equity exception).

### Formulas (ratio = n new for every N old; M = cum-rights price; S = issue price)
- New shares = Existing shares × n ÷ N
- Money raised = New shares × S
- **TERP = (N × M + n × S) ÷ (N + n)** — weighted average; always **strictly between S and M**.
  - Total-value form: TERP = (Market cap before + Cash raised) ÷ Total shares after.
- **Value of right per OLD share = M − TERP**
- **Value of right per NEW share = (N ÷ n) × (M − TERP) = N × (M − S) ÷ (N + n)**
- Link: VR per old = (n ÷ N) × VR per new.
- **Backward solve:** given any four of {M, S, N, n, TERP}, solve the one equation for the fifth.

## Journal entries (face value F, issue price S, premium = S − F)
```
Bank A/c                                  Dr   (Shares × S)
    To Equity Share Application & Allotment A/c
Equity Share Application & Allotment A/c   Dr   (Shares × S)
    To Equity Share Capital A/c                 (Shares × F)
    To Securities Premium A/c                   (Shares × (S − F))
```
- Premium → **Securities Premium A/c (Sec 52)**, restricted use; issue **expenses NOT** chargeable here.
- If instalments/calls-in-arrears → ordinary shares-accounting machinery.
- **No entry for the "value of the right"** — it is a market phenomenon; renunciation cash flows privately between shareholders, off the company's books.

## Worked mini-example
Sunrise Ltd: 4,00,000 shares of ₹10, cum-rights ₹50. Rights **1-for-4** at ₹30.
- New shares = 4,00,000 ÷ 4 = **1,00,000**; money = ₹30,00,000.
- TERP = (4×50 + 1×30) ÷ 5 = 230 ÷ 5 = **₹46**.
- VR per old share = 50 − 46 = **₹4**; per new = 4×(50−30)÷5 = **₹16**.
- Holder of 4 shares: before 4×50 = ₹200. Subscribes 1 @ ₹30 → 5 shares × ₹46 = ₹230, less ₹30 = **₹200** ✓ wealth-neutral.
- Renouncer of 400: keeps 400 × ₹46 = ₹18,400 + sells rights 400 × ₹4 = ₹1,600 = **₹20,000** = before ✓.
- Lapse loses exactly VR forgone.

## Exam traps & must-remember
1. "Discount → loss" is **false**; wealth is neutral (discount recaptured as VR).
2. VR per **old** vs **new** share — differ by n/N. State basis; safe route: TERP → M − TERP → scale.
3. Only **lapsing** loses money (= VR of lapsed slice). Subscribe/renounce both neutral.
4. M must be **cum-rights** price; never feed ex-rights price into TERP.
5. Premium → **Securities Premium (Sec 52)**, not GR/P&L; don't debit it for issue expenses.
6. Rights (62(1)(a)) needs only **Board resolution**; special resolution is for (c) / 62(3).
7. Offer **15–30 days**; deemed declined. "Only 12 days" may be valid if **≥90% consent**.
8. No ledger entry for value of the right.
9. **Fractional entitlements** pooled and disposed under 62(1)(a)(iii); don't round individuals up.
10. **Bonus-then-rights** — apply bonus first (enlarges base) unless told otherwise.
11. S below face value → "not permissible" (Sec 53), not a TERP number.
12. TERP outside [S, M] → arithmetic error (swapped N and n).
13. Be ready to solve the TERP equation **backwards**.
- **Disclosure:** shares-reconciliation note (Schedule III) separates "issued for cash" (rights) from "bonus" — two movement lines in layered problems. Cash flow: rights proceeds = **Financing inflow = Shares × S** (VR is not a company cash flow).

## One-line recall
- Sec 62(1)(a); default route; Board resolution; 15–30 days; renounceable; unsubscribed disposed non-disadvantageously.
- TERP = (N·M + n·S)/(N + n), lies strictly between S and M.
- VR/old = M − TERP; VR/new = (N/n)(M − TERP) = N(M−S)/(N+n).
- Wealth neutral if subscribe or sell; only lapse loses (= VR forgone).
- Entry: Bank Dr → Share Capital + Securities Premium; never below face value (Sec 53).
- 3-sec check: 1-for-4 @ ₹30, M ₹50 → TERP ₹46, VR ₹4/old, ₹16/new.
