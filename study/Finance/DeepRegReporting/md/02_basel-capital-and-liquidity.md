# Basel III/IV: Capital & Liquidity (RWA, CAR, CET1, LCR, NSFR)

## What you'll be able to do

You will be able to take a simple bank balance sheet and compute, by hand, the four ratios every prudential regulator cares about: the Capital Adequacy Ratio (CAR), the Common Equity Tier 1 (CET1) ratio, the Liquidity Coverage Ratio (LCR), and the Net Stable Funding Ratio (NSFR). You'll know what goes in each capital tier, how risk-weighted assets (RWA) are built, which run-off and haircut factors to apply, and — crucially — what the analyst actually hands over: a capital return and a liquidity return that reconcile to the GL and clear the regulatory minimums.

## The essentials

**Basel III/IV** is the global bank-capital rulebook from the Basel Committee (BIS). India implements it through RBI's Master Circular on Basel III Capital Regulations. "Basel IV" (the 2017 finalisation — output floor, revised standardised approaches for credit/operational risk) is phasing in globally through 2025–2028; RBI is adopting elements progressively.

**Capital tiers** — capital is ranked by loss-absorbing quality:

| Tier | What it is | Loss absorption |
|---|---|---|
| CET1 (Common Equity Tier 1) | Paid-up equity + retained earnings + disclosed reserves − regulatory deductions (goodwill, DTA, intangibles) | Highest — first to absorb losses, going concern |
| AT1 (Additional Tier 1) | Perpetual non-cumulative instruments (e.g. AT1 bonds) with loss-absorption triggers | Going concern |
| Tier 2 | Subordinated debt (min 5-yr), general provisions (capped) | Gone concern — absorbs on liquidation |

Total Capital = CET1 + AT1 + Tier 2.

**The regulatory minimums (RBI, 2026):**

| Ratio | Basel min | RBI min (incl. CCB) |
|---|---|---|
| CET1 | 4.5% | 5.5% + 2.5% CCB = 8.0% |
| Tier 1 | 6.0% | 7.0% |
| Total CAR | 8.0% | 9.0% + 2.5% CCB = 11.5% |
| Leverage ratio | 3.0% | 3.5% (4% for D-SIBs) |
| LCR | 100% | 100% |
| NSFR | 100% | 100% |

CCB = Capital Conservation Buffer. D-SIBs (SBI, HDFC Bank, ICICI) carry an additional surcharge.

**RWA** — assets weighted by riskiness. Cash and sovereign (G-sec) = 0%; home loans ~35–50%; corporate loans 20–150% by rating; unrated corporate 100%. RWA = Σ(exposure × risk weight). Total RWA = credit RWA + market RWA + operational RWA.

**CAR = Total Capital / Total RWA. CET1 ratio = CET1 / Total RWA.**

**LCR = Stock of HQLA / Total net cash outflows over 30 days ≥ 100%.** HQLA: Level 1 (cash, G-secs, at 100% value) and Level 2 (high-grade corporate/covered bonds, haircut, capped). Net outflows = stressed outflows − min(inflows, 75% of outflows).

**NSFR = Available Stable Funding / Required Stable Funding ≥ 100%.** ASF weights funding by stability (capital 100%, stable retail deposits 95%, wholesale <1yr lower). RSF weights assets by how much stable funding they need to hold (cash 0%, loans >1yr 85–100%).

## Hands-on — step by step

Take **Meridian Bank**. Simplified balance sheet (₹ crore):

Assets: Cash 50 · G-secs 200 · Home loans 300 · Corporate loans (unrated) 400 · Fixed assets 50 = **1,000**.
Liabilities: Equity (paid-up + reserves) 80 · AT1 bonds 10 · Tier-2 sub-debt 20 · Retail deposits 700 · Wholesale deposits (financial cpty) 190 = **1,000**.

**Step 1 — Capital.** CET1 = 80 (assume no deductions). AT1 = 10 → Tier 1 = 90. Tier 2 = 20. Total Capital = 110.

**Step 2 — Credit RWA.**
- Cash: 50 × 0% = 0
- G-secs: 200 × 0% = 0
- Home loans: 300 × 35% = 105
- Corporate (unrated): 400 × 100% = 400
- Fixed assets: 50 × 100% = 50
- Credit RWA = **555**. Add market + operational RWA, say 45 → **Total RWA = 600**.

**Step 3 — Ratios.**
- CAR = 110 / 600 = **18.33%** (≥ 11.5% ✓)
- CET1 ratio = 80 / 600 = **13.33%** (≥ 8.0% ✓)
- Tier 1 = 90 / 600 = 15.0% (✓)

**Step 4 — LCR.** HQLA = Cash 50 (L1, 100%) + G-secs 200 (L1, 100%) = **250**.
Outflows (30-day stress): Retail deposits 700 × 5% = 35; Wholesale 190 × 100% = 190. Total outflows = **225**.
Inflows: assume contractual inflows of 40; capped at 75% of outflows = 168, so use 40.
Net outflows = 225 − 40 = **185**.
LCR = 250 / 185 = **135.1%** (≥ 100% ✓).

**Step 5 — NSFR.** ASF: Equity+AT1+T2 = 110 × 100% = 110; Retail deposits 700 × 95% = 665; Wholesale <1yr 190 × 0% (or low) = 0. ASF = **775**.
RSF: Cash 50 × 0% = 0; G-secs 200 × 5% = 10; Home loans 300 × 65% = 195; Corporate loans 400 × 85% = 340; Fixed assets 50 × 100% = 50. RSF = **595**.
NSFR = 775 / 595 = **130.3%** (≥ 100% ✓).

## The output

The analyst produces a **capital-and-liquidity dashboard** that goes to the CFO and into the RBI return:

```
MERIDIAN BANK — PRUDENTIAL DASHBOARD (₹ cr)   Q1 FY27
CAPITAL
  CET1                     80      CET1 ratio     13.33%   (min 8.00%)  ✓
  Tier 1                   90      Tier 1 ratio   15.00%   (min 7.00%)  ✓
  Total capital           110      Total CAR      18.33%   (min 11.50%) ✓
  Total RWA               600
    of which credit RWA   555
LIQUIDITY
  HQLA                    250      LCR           135.1%    (min 100%)   ✓
  Net 30-day outflows     185
  ASF                     775      NSFR          130.3%    (min 100%)   ✓
  RSF                     595
Leverage: Tier1 90 / exposure 1000 = 9.0%       (min 3.5%)   ✓
```

## Checks, gotchas & red flags

- **CET1 deductions are where errors hide.** Goodwill, intangibles, deferred tax assets that rely on future profitability, and investments in own shares must be deducted from CET1. Forgetting them overstates capital — a serious finding.
- **RWA must reconcile to the balance sheet.** Total exposures feeding credit RWA should tie to gross advances + investments. If they don't, the risk weights are being applied to the wrong base.
- **LCR is a 30-day stress, not a snapshot of today's cash.** Apply run-off factors; don't just count deposits. And remember the inflow cap: inflows can offset at most 75% of outflows, so you always hold some HQLA.
- **HQLA Level 2 caps.** Level 2 assets can't exceed 40% of total HQLA (Level 2B capped at 15%), and carry haircuts (15% for 2A). Loading up on corporate bonds doesn't rescue a weak LCR.
- **NSFR and LCR pull in opposite directions on tenor.** Short wholesale funding is cheap but hurts both ratios. Analysts flag maturity mismatches, not just point ratios.
- **Undrawn commitments create outflows.** Committed credit/liquidity lines generate LCR outflows even though nothing has been drawn — easy to miss.

## Interview drill

**Q: A bank swaps ₹100 cr of unrated corporate loans for ₹100 cr of G-secs. What happens to CAR and LCR?**
A: CAR improves: G-secs carry 0% risk weight vs 100% for unrated corporates, so RWA falls by ₹100 cr, raising the ratio (same capital / smaller denominator). LCR also improves: G-secs are Level 1 HQLA at 100% value, so HQLA rises by ₹100 cr while corporate loans weren't HQLA at all. It's a classic "de-risking" trade — but NII (interest income) drops because G-secs yield less than corporate loans. Capital and liquidity strength bought at the cost of profitability.

**Q: Why is CET1 more important than Total CAR to a regulator?**
A: Because CET1 is going-concern, permanent, fully loss-absorbing equity — it protects the bank while it's still operating. Tier 2 only absorbs losses in liquidation (gone-concern), by which point depositors may already be hurt. A bank can have a healthy Total CAR propped up by sub-debt yet a thin CET1, which is fragile. That's why post-2008 Basel III raised the CET1 minimum specifically and made it the binding constraint.

## Learn/practise (free)

- **BIS Basel Framework** (bis.org, free): the CAP, LCR (LCR30) and NSFR (NSF) chapters give exact factors — the authoritative source.
- **RBI Master Circular — Basel III Capital Regulations** and the LCR/NSFR Master Directions (free PDFs) for the India-specific weights.
- Build the Meridian model in Excel: one tab for RWA (exposure × risk weight), one for LCR (outflow factors), one for NSFR (ASF/RSF weights). Stress-test it — halve retail deposits, watch LCR break. This is exactly what an analyst does.
- Any listed Indian bank's **Basel III Pillar 3 disclosure** (on its investor-relations page, free) shows a real capital and RWA table — reverse-engineer it against your model.
