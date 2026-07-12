# Chapter 36 — Underwriting of Shares & Debentures

## Snapshot
Underwriting = a contract where an underwriter guarantees, for a **commission**, to take up shares/debentures **not subscribed by the public** (insurance on the issue). **Devolvement** = shortfall falling on the underwriter. Commission is payable **whether or not** the guarantee is called. Governed by **Sec 40(6), Companies Act 2013 + Rule 13** (Prospectus & Allotment Rules 2014). Two exam skills: the **liability table** (arithmetic) and the **journal entries**.

## Core concepts
- **Marked applications** — bear an underwriter's stamp/code → credited to **that** underwriter (measures selling performance).
- **Unmarked applications** — no stamp → shared among all in **gross-liability ratio**.
- **Firm underwriting** — underwriter definitely buys a fixed lot (like an ordinary applicant), over and above the guarantee; taken up regardless of public response.
- **Complete** underwriting (whole issue; company takes any un-underwritten balance) vs **Partial** (company is underwriter for the un-underwritten slice).

## Key provisions / conditions & limits

### Commission caps (Sec 40(6) + Rule 13)
| Security | Max rate | Base |
|---|---|---|
| Shares | **5%** (or Articles' rate, whichever **less**) | Issue price (incl. premium) of shares **underwritten** |
| Debentures | **2.5%** (or Articles' rate, whichever **less**) | Issue price of debentures underwritten |

- **Commission = shares underwritten × issue price × min(statutory cap, Articles' rate).**
- On shares **UNDERWRITTEN**, not taken up. On **issue price**, not face value.
- **No commission** on company's own portion (partial) or shares **not offered to public** (firm/reserved to underwriter per SEBI).
- Payable in cash, or fully-paid shares/debentures, or combination.
- **Conditions to pay:** authorised by Articles; within cap; disclosed in prospectus; underwriting contract filed with ROC; number underwritten disclosed.
- **Brokerage ≠ commission** — brokerage is for *procuring* subscriptions (paid only on shares actually placed); can be paid to same party additionally; no 5%/2.5% cap applies to it.

### Gross Liability Method (work in NUMBER of shares)
1. **Gross liability** — split in agreed ratio (add **company** as underwriter if partial).
2. **Less: Marked applications** (each their own).
3. **Less: Unmarked applications** (distribute in gross-liability ratio).
4. = **Balance**. Negative → **surplus** (over-delivered).
5. **Surplus** of over-performer → **SUBTRACT** from others in ratio of **their** gross liabilities (exclude surplus party; surplus party → 0). Repeat if a second turns negative.
6. **Less: Firm underwriting** (per convention).
7. = **Net liability**. Then **+ own firm shares = total taken up**.

**Order matters:** marked → unmarked → surplus → firm.
**Golden reconciliation:** **Marked + Unmarked + Firm + Net liability = Shares issued.**

### Firm-underwriting conventions
- **Convention A** (ICAI default) — firm treated like the underwriter's **own marked** apps (deduct from own account).
- **Convention B** — firm **pooled with unmarked**, shared in gross ratio. If silent, assume A and state it. Convention materially changes net liabilities.

### Fully subscribed in aggregate
If total subscription (marked + unmarked + firm) ≥ shares issued → **no liability on anyone**, even an underwriter whose own marking fell short. Commission still fully payable. **Exception:** agreement says "liable on marked applications only" → individual shortfall owed regardless of aggregate.

### Context
- **Minimum subscription** (Sec 39): no allotment unless min. subscription received; else refund. **SEBI ICDR 90% rule** — refund if <90% of offer subscribed. Underwriting guarantees this floor via devolvement.
- Underwriter must be **SEBI-registered**; directors state in prospectus underwriters have sufficient resources; agreement filed with ROC.

## Journal entries (N shares, face ₹10, issue ₹12, premium ₹2)
```
Underwriters A/c              Dr   (N × issue price)
    To Share Capital A/c              (N × face value)
    To Securities Premium A/c         (N × premium)

Underwriting Commission A/c   Dr   (commission)
    To Underwriters A/c

Bank A/c                      Dr   (net)    [or Underwriters Dr, To Bank if commission > shares value]
    To Underwriters A/c

Securities Premium A/c        Dr   (write-off, to extent available)
    To Underwriting Commission A/c
```
- Debentures → credit **Debentures A/c** instead of Share Capital; cap 2.5%.
- Commission in fully-paid shares: Underwriters A/c Dr → Share Capital + Securities Premium.
- Write-off: against **Securities Premium (Sec 52(2)(c))** to the extent available; **excess / par issue → Statement of P&L**.

## Worked mini-example
Ganga Ltd: 2,00,000 shares @ ₹10 par, underwritten **A:B:C = 5:3:2**. Marked: A 40,000, B 20,000, C 60,000; Unmarked 30,000.

| | A | B | C | Total |
|---|---|---|---|---|
| Gross liability | 1,00,000 | 60,000 | 40,000 | 2,00,000 |
| Less marked | 40,000 | 20,000 | 60,000 | 1,20,000 |
| Less unmarked (5:3:2) | 15,000 | 9,000 | 6,000 | 30,000 |
| Balance | 45,000 | 31,000 | (26,000) | 50,000 |
| C surplus (5:3) | (16,250) | (9,750) | 26,000 | 0 |
| **Net liability** | **28,750** | **21,250** | **0** | **50,000** |

Reconcile: Marked 1,20,000 + Unmarked 30,000 + Net 50,000 = 2,00,000 ✓. C over-delivered → **subtracts** from A, B (total stays = shortfall 50,000).

## Exam traps & must-remember
1. Commission on shares **UNDERWRITTEN, not taken up** (₹50,000 on 1,00,000, not on 28,000).
2. Commission on **issue price incl. premium**, not face value.
3. Company earns **no commission** on own / not-offered-to-public portion.
4. Surplus **REDUCES** (subtract from) others — sign discipline. Total after redistribution must still = original shortfall.
5. Marked vs unmarked: often **unmarked = total apps − marked** (don't double count).
6. Firm convention A vs B changes numbers — identify which.
7. Firm shares **always** taken up by underwriter, added to net liability for "total subscribed".
8. Surplus redistributed in **remaining** underwriters' gross ratio (exclude surplus party); repeat if second goes negative.
9. Partial → insert **company** as underwriter for balance.
10. Reconcile at the end (free marks + error detection).
11. Work in **number of shares**, not rupees, in the table.
12. Rate = **min(statutory cap, Articles' rate)** — Articles below cap bind down (2% not 2.5%); above cap don't lift (5% not 6%).
13. Fully subscribed in aggregate ⇒ **nil liability** (unless "marked applications only").
14. Settlement cash can **reverse**: if commission > shares value, company **pays** underwriter.
15. Write-off **capped by premium available**; excess → P&L.
16. Brokerage ≠ commission; don't merge or apply cap.

## One-line recall
- Purpose: transfer demand-risk company → underwriter for a commission (insurance).
- Caps: 5% shares / 2.5% debentures, or Articles' rate if lower; base = issue price of shares underwritten.
- Table: Gross → −Marked → −Unmarked(gross ratio) → surplus subtract → −Firm → Net liability (+own firm = total taken up).
- Reconciliation: Marked + Unmarked + Firm + Net liability = Shares issued.
- Commission written off vs Securities Premium (Sec 52); excess → P&L. Debentures → credit Debentures A/c.
