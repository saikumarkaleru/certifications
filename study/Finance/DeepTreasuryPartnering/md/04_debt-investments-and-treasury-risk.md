# Debt, Investments & Treasury Risk Policy

## What you'll be able to do
Structure and track a company's borrowings and short-term investments, measure and hedge interest-rate risk, set and monitor counterparty limits, and write the treasury policy and control framework that keeps all of it inside the board's risk appetite. You'll compute an interest-rate exposure and the cost/benefit of a payer swap, build a counterparty-limit table, list the KPIs a treasurer reports, and know exactly what the CTP (Certified Treasury Professional) credential covers. This is the "run the balance sheet's financing side, safely" skill set.

## The essentials

**Borrowings & facilities.**

| Instrument | Tenor | Notes |
|---|---|---|
| **Overdraft / cash credit** | On demand | Working-capital float; costly, flexible |
| **Working-capital demand loan / WCDL** | Short | Cheaper than OD for a known need |
| **Commercial paper (CP)** | 7 days–1 yr | Unsecured, for strong credits; discount instrument |
| **Term loan** | 1–10+ yr | Project/capex; fixed or floating |
| **NCD / bond** | Medium–long | Capital-market debt, rated |
| **Committed line (RCF)** | Multi-year | Undrawn backstop; pay a commitment fee for headroom |

**Committed vs uncommitted:** a committed facility (RCF) the bank *must* lend under, for a fee — that's your liquidity insurance. Uncommitted is available "subject to bank discretion" and can vanish when you most need it.

**Short-term investments** (surplus cash) — ranked by the policy priority **security → liquidity → yield** (in that order):
- Liquid/overnight mutual funds, TREPS, T-bills, bank FDs, high-grade CP/CD. Never chase yield with credit or duration you can't justify.

**Interest-rate risk.** Floating-rate debt (linked to MIBOR/MCLR/repo/SOFR) means rising rates raise your interest cost. Measured by **repricing gap** (fixed vs floating mix) and sensitivity to a rate move (e.g. +100 bps). Hedge by:
- **Interest-rate swap (IRS):** pay fixed / receive floating to convert floating debt to fixed.
- **Cap:** buy protection above a strike (option; premium; keeps downside).
- **FRA:** lock a forward rate for one period.

**Counterparty (credit) risk.** The risk a bank/issuer you deposit with or trade with defaults. Controlled by **limits**: a maximum exposure per counterparty, set by their credit rating, and monitored daily. Spread cash across names; don't put all surplus in one bank.

**Treasury policy** — the board-approved rulebook. Core contents:
1. Objectives & risk appetite. 2. Governance & delegated authorities (dealing mandates, limits). 3. Approved instruments & prohibited activities. 4. Counterparty limits & rating floors. 5. Hedging policy (what, how much, horizon). 6. Liquidity & minimum-buffer rules. 7. Segregation of duties & controls. 8. Reporting & KPIs.

**KPIs a treasurer reports:** liquidity headroom (cash + undrawn committed lines), net debt & gearing, weighted-average cost of debt, fixed/floating ratio, debt maturity profile (no cliff), hedge ratio / hedged %, forecast accuracy, counterparty concentration, days cash on hand, bank fees.

**The CTP.** *Certified Treasury Professional*, issued by the **AFP (Association for Financial Professionals, US)** — the global benchmark treasury credential. Covers cash & liquidity management, capital markets & funding, FX and interest-rate risk, working capital, treasury tech and controls. Eligibility is work-experience based; it's the credential treasury job ads name most. (UK equivalent: the ACT's AMCT/CertICM.)

## Hands-on — step by step
**Scenario.** A company has **₹100 cr term debt**: ₹60 cr floating at **MIBOR + 200 bps**, ₹40 cr fixed at 8.0%. Current 3-month MIBOR = 6.5%. Board policy: keep at least **60% of debt fixed**. Also, ₹30 cr surplus cash to place under a counterparty-limit policy.

**Step 1 — Current fixed/floating mix.** Fixed = 40/100 = **40%**. Policy floor 60%. **Breach** — too much floating; must fix at least another ₹20 cr.

**Step 2 — Current interest cost (annual).**
- Floating ₹60 cr at 6.5% + 2.0% = 8.5% → ₹5.10 cr
- Fixed ₹40 cr at 8.0% → ₹3.20 cr
- **Total = ₹8.30 cr; WACD = 8.30%.**

**Step 3 — Rate-shock sensitivity (+100 bps).** Only floating reprices: ₹60 cr × 1% = **+₹0.60 cr** extra interest per year per 100 bps. That's the exposure the board cares about.

**Step 4 — Hedge to policy: pay-fixed IRS on ₹20 cr.** Enter a 3-year IRS: **pay fixed 7.2%, receive 3M MIBOR** on ₹20 cr notional. This converts ₹20 cr of floating to fixed → new mix fixed 60% / floating 40% — **back in policy**.

Effect on that ₹20 cr:
- Was paying MIBOR+200 = 8.5% (at today's MIBOR).
- Now pays: swap fixed 7.2% + the 200 bps loan margin − receive-leg offsets the MIBOR in the loan → effective ≈ **7.2% + 2.0% = 9.2%** locked, *regardless of where MIBOR goes*.
- You pay ~0.7% more than today's floating cost to remove the risk of rates rising. If MIBOR rises above ~7.0%, the swap pays off.

**Step 5 — Sensitivity after hedge.** Floating now ₹40 cr → +100 bps = **+₹0.40 cr** (down from ₹0.60 cr). Exposure cut by a third, mix compliant.

**Step 6 — Place the ₹30 cr surplus under counterparty limits.** Policy: max exposure per bank by rating.

| Counterparty | Rating | Limit | Placed | Instrument |
|---|---|---|---|---|
| Bank A (AAA) | AAA | ₹15 cr | ₹12 cr | Liquid fund / FD |
| Bank B (AAA) | AAA | ₹15 cr | ₹10 cr | TREPS |
| Bank C (AA+) | AA+ | ₹8 cr | ₹8 cr | 91-day T-bill via C |
| **Total** | | | **₹30 cr** | within all limits |

No single name over its limit; no sub-AA credit used. Security and liquidity satisfied before yield.

## The output
**Treasury debt & risk dashboard — Jul-2026**

```
DEBT PROFILE
  Total debt                     ₹100.0 cr
  Fixed / Floating (pre-hedge)   40% / 60%   -> POLICY BREACH (min 60% fixed)
  Action: pay-fixed IRS ₹20 cr @ 7.2% (3y)
  Fixed / Floating (post-hedge)  60% / 40%   -> COMPLIANT
  WACD                           8.30% (pre) -> ~8.44% (post, locked)

INTEREST-RATE SENSITIVITY (+100 bps, annual)
  Pre-hedge   +₹0.60 cr
  Post-hedge  +₹0.40 cr        (exposure cut 33%)

INVESTMENTS (₹30 cr surplus)
  All placements within counterparty limits; min rating AA+; 
  priority security > liquidity > yield satisfied.

KPIs
  Liquidity headroom  ₹18 cr cash + ₹25 cr undrawn RCF = ₹43 cr
  Net debt / EBITDA   1.8x     Hedge ratio  60% fixed
  Debt maturities     no single year > 30% of total (no cliff)
  Counterparty conc.  max 12/30 = 40% (within 50% cap)
```

## Checks, gotchas & red flags
- **Security and liquidity beat yield — always.** An investment policy that reaches for return on surplus operating cash is the classic blow-up (think of firms caught in a bank failure with over-limit deposits).
- **Committed ≠ uncommitted headroom.** Only *committed* undrawn lines count as real liquidity insurance; uncommitted can be pulled.
- **A swap hedges rate risk but adds counterparty & MTM risk.** The swap has its own credit exposure and mark-to-market volatility; hedge accounting (cash-flow hedge on floating debt) keeps the MTM out of P&L.
- **Policy floors are hard limits, not targets** — a 40% fixed ratio against a 60% floor is a breach to report and fix, not to average away.
- **Maturity cliffs kill companies.** Watch the refinancing profile — never let a large slug of debt mature in one window.
- **Limit monitoring must be daily and independent** (middle office), on current exposure including accrued interest, not month-end snapshots.
- **CP/short debt rolls over** — funding liquidity risk: if the market shuts, can you refinance? Keep committed backstop lines behind CP programmes.

## Interview drill
**Q: How do you measure and hedge interest-rate risk on a debt portfolio?** A: Measure the fixed/floating mix and the repricing gap, then shock the floating portion — e.g. +100 bps on ₹60 cr floating is ₹0.60 cr extra annual interest. If that exposure or the floating share breaches policy, I'd hedge with a pay-fixed / receive-floating interest-rate swap to convert floating debt to fixed, or buy a cap if I want to keep the downside. Post-hedge I re-run the mix and the rate shock to confirm I'm inside the board's limit, and I'd apply cash-flow hedge accounting so the swap's MTM sits in OCI, not P&L.

**Q: What's the priority order for investing surplus cash, and why?** A: Security, then liquidity, then yield. Surplus operating cash exists to be available and safe — a small extra return never justifies principal risk or being locked up when you need it. So I'd use high-grade, short, liquid instruments (liquid funds, TREPS, T-bills, top-rated FDs) spread across counterparties within per-name limits, and only optimise yield within those constraints.

**Q: What goes in a treasury policy and what's the CTP?** A: A treasury policy sets objectives and risk appetite, governance and delegated dealing authorities, approved and prohibited instruments, counterparty limits and rating floors, the hedging and liquidity rules, segregation of duties, and reporting/KPIs — the board's rulebook that keeps treasury inside its mandate. The CTP is the AFP's Certified Treasury Professional, the leading global treasury credential, covering cash and liquidity, funding and capital markets, FX and rate risk, and treasury controls.

## Learn/practise (free)
- **AFP (afponline.org)** — free CTP exam outline and sample questions; read the body-of-knowledge domains.
- **ACT Treasurer's Wiki** — free, high-quality entries on facilities, swaps, investment policy, and counterparty limits.
- **RBI & FIMMDA** — free reference for MIBOR/MIFOR, T-bill auctions, TREPS, and CP guidelines in India.
- **Build the dashboard** above in Excel from a mock debt schedule: compute fixed/floating %, WACD, the +100 bps sensitivity, and a swap that restores policy — then write the one-page action note.
- **Draft a two-page treasury policy** for a fictional mid-cap: appetite, limits, approved instruments, KPIs. Recruiters love seeing you can write one.
- **CFA / FRM interest-rate risk readings** and **Corporate Finance Institute** free articles cover swaps, gap analysis, and investment policy statements.
