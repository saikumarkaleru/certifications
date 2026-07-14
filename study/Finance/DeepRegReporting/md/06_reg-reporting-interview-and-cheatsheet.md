# Reg-Reporting Interview Drills + Calendar & Cheat-Sheet

## What you'll be able to do

This chapter turns everything from the reg-reporting module into **exam-ready
recall**. After it you'll be able to: compute CAR/CRAR, LCR and NSFR live on a
whiteboard with the numbers tying out; explain any major return (COREP, FINREP,
LCR, RBI Form A, DSB III) in two clean sentences; describe **data lineage** and
why it matters; and rattle off the key ratios, thresholds, return names, filing
frequencies and platform vendors without notes. It doubles as a one-page
cheat-sheet you can revise the morning of the interview.

## The essentials

Interviewers for GCC / Luxoft-type reg-reporting seats test three things:
**(1) do the arithmetic** — can you actually compute the ratios; **(2) do you
understand the return** — what it captures and why; **(3) do you get the
control** — lineage, reconciliation, four-eyes, taxonomy. Below are the drills
with model answers, then the cheat-sheet.

## Hands-on — step by step (the drills)

### Drill 1 — Compute CAR / CRAR

*Given:* CET1 = ₹1,150 cr, AT1 = ₹150 cr, Tier 2 = ₹200 cr; Credit RWA = 7,500,
Market RWA = 900, Operational RWA = 1,600.

**Work it:**
- Tier 1 = CET1 + AT1 = 1,150 + 150 = **1,300**
- Total capital = Tier 1 + Tier 2 = 1,300 + 200 = **1,500**
- Total RWA = 7,500 + 900 + 1,600 = **10,000**
- **CET1 ratio** = 1,150 / 10,000 = **11.50%**
- **Tier 1 ratio** = 1,300 / 10,000 = **13.00%**
- **CRAR (Total)** = 1,500 / 10,000 = **15.00%**

*Say this:* "CRAR is total regulatory capital over risk-weighted assets. RBI's
minimum is 9%, plus a 2.5% capital-conservation buffer, so effectively **11.5%**;
CET1 min is 5.5% + CCB. At 15% CRAR and 11.5% CET1 this bank is comfortably above
requirement, with ~3.5% headroom on total capital."

### Drill 2 — Compute LCR

*Given:* HQLA = ₹4,000 cr (all Level 1). Stressed outflows over 30 days:
retail deposits 20,000 × 5% = 1,000; operational wholesale 8,000 × 25% = 2,000;
non-operational wholesale 5,000 × 40% = 2,000. Stressed inflows: contractual
loan inflows 3,000 × 50% = 1,500.

**Work it:**
- Total outflows = 1,000 + 2,000 + 2,000 = **5,000**
- Total inflows = **1,500**, capped at 75% of outflows = 3,750 → 1,500 stands
- **Net cash outflows** = 5,000 − 1,500 = **3,500**
- **LCR** = HQLA / net outflows = 4,000 / 3,500 = **114.3%**

*Say this:* "LCR ensures 30 days of survival in stress. Minimum is **100%**. At
114% we hold enough HQLA to cover a month of net stressed outflows. Note the
**inflow cap at 75% of outflows** — a bank can't rely on more than 75% of
outflows being met by inflows, so it must always hold some buffer."

### Drill 3 — NSFR (quick)

*Given:* Available Stable Funding (ASF) = ₹9,000 cr, Required Stable Funding
(RSF) = ₹8,200 cr. **NSFR** = ASF/RSF = 9,000/8,200 = **109.8%**, min 100%.
Structural, one-year horizon vs LCR's 30-day. Both must be ≥100%.

### Drill 4 — Explain a return

*Prompt: "What is COREP?"* — "COREP (Common Reporting) is the EBA's harmonised
prudential return: own funds, capital ratios, credit/market/operational RWA,
large exposures, leverage ratio and the LCR/NSFR liquidity templates. Its sister
is **FINREP** (Financial Reporting) — IFRS balance-sheet, P&L and asset-quality
data. COREP = capital & risk; FINREP = financial statements. Both filed as XBRL
against the EBA taxonomy, usually quarterly."

*Prompt: "RBI Form A?"* — "Form A is the fortnightly return of a bank's
liabilities and assets in India used to compute **CRR and SLR** compliance —
demand and time liabilities (NDTL) against cash and SLR securities held."

### Drill 5 — Explain data lineage

*Say this:* "Data lineage is the documented path from a reported cell back to the
source transaction and system. If a regulator questions 'other assets = 340 cr',
lineage lets me drill: reported cell → reg line-item mapping → GL account 1950 →
sub-ledger entry → originating trade. It's essential for **reconciliation**
(prove the return ties to the GL), **audit** (evidence every number), and **error
resolution** (find where a break enters). No lineage = you can't defend a number."

## The output

The finished artefact is the cheat-sheet — memorise it:

### Key ratios & thresholds (Basel III / RBI 2026)

| Ratio | Formula | Minimum |
|---|---|---|
| CET1 | CET1 capital / RWA | 4.5% (RBI 5.5%) + 2.5% CCB |
| Tier 1 | Tier 1 / RWA | 6% (RBI 7%) |
| CRAR / CAR | Total capital / RWA | 8% (RBI 9%) + 2.5% CCB → 11.5% |
| Leverage ratio | Tier 1 / total exposure | 3% (RBI 3.5–4%) |
| LCR | HQLA / 30-day net stressed outflows | ≥100% |
| NSFR | Available SF / Required SF | ≥100% |
| Large exposure | to single counterparty | ≤25% of Tier 1 |

### Key returns & who files what

| Return | Regulator | Covers | Frequency |
|---|---|---|---|
| COREP | EBA / PRA | Own funds, RWA, LR, LCR, NSFR, large exposures | Quarterly |
| FINREP | EBA / PRA | IFRS B/S, P&L, asset quality | Quarterly |
| AnaCredit | ECB | Loan-level credit data | Monthly |
| FR Y-9C / FFIEC 031 | US Fed / FFIEC | Bank holding co. financials / Call Report | Quarterly |
| Form A | RBI | NDTL for CRR/SLR | Fortnightly |
| RLC / LCR return | RBI | Liquidity coverage | Monthly |
| DSB III / RBS | RBI | Risk-based supervision data | Quarterly/Annual |
| CIMS returns | RBI | Centralised Information Mgmt System filings | Various |

### Filing calendar (typical)

| Frequency | Examples | Timing after period-end |
|---|---|---|
| Fortnightly | RBI Form A | ~7 days |
| Monthly | LCR, AnaCredit | ~15–30 days |
| Quarterly | COREP, FINREP, Call Report | ~30–45 days |
| Annual | Pillar 3, RBS | 3–6 months |

### Platforms & vendors

| Platform | Vendor (2026) | Note |
|---|---|---|
| ControllerView | AxiomSL → Adenza → **Nasdaq** | Deep data integration, configurable logic |
| OneSumX | **Wolters Kluwer** | Managed Regulatory Update Service |
| Rcloud / ABACUS | **Regnology** | EBA granular, AnaCredit, cloud/SaaS |
| Vermeg / AGILE | Vermeg | Also used in EU |

### The five-stage workflow (one line)

**Source → Map → Validate → Reconcile to GL → Sign-off & submit (XBRL).**

## Checks, gotchas & red flags

- **LCR inflow cap** — always cap inflows at 75% of outflows before dividing.
- **Buffers on top of minimums** — quote 11.5% CRAR (9% + 2.5% CCB) for RBI, not
  the bare 9%; interviewers listen for the buffer.
- **CET1 ≤ Tier 1 ≤ Total capital** — if your numbers break this ordering you've
  made an error.
- **Return ties to GL** — if asked about a break, never "plug" it; drill lineage.
- **XBRL taxonomy version** — filing against the wrong DPM/taxonomy = rejection.
- **Don't confuse LCR (30-day, liquidity stress) with NSFR (1-year, structural)**
  or FINREP (financials) with COREP (capital).

## Interview drill

**Q1. "A bank's CRAR is 15% but CET1 is only 6%. Is that a problem?"** *Answer:*
"CET1 at 6% is above the 4.5% Basel minimum but, after the 2.5% CCB, the
effective CET1 requirement is ~7% (RBI 8%). So despite a healthy 15% total CRAR,
the bank may be **breaching its CET1 buffer** and could face distributable-profit
restrictions. Total capital adequacy can mask weak core capital — always look at
CET1 separately."

**Q2. "Why do regulators want granular / loan-level data like AnaCredit instead
of just totals?"** *Answer:* "Granular data lets the regulator run its own
analytics — concentration, sector risk, IFRS-9 staging — rather than trusting
bank-computed aggregates, and it enables consistency checks across banks. It
shifts the calculation burden and reduces the room for classification games. The
trade-off is far heavier data-quality and lineage demands on the bank."

**Q3. "How do you know a return is correct before you submit?"** *Answer:*
"Three gates: the engine runs the regulator's validation rules with zero blocking
failures; the return reconciles exactly to the trial balance/audited financials
with any timing differences documented; and four-eyes maker-checker sign-off with
variance commentary explaining material QoQ movements. Only then is the XBRL
instance generated and filed."

## Learn/practise (free)

- **Drill the ratios cold** with random inputs until CAR, LCR and NSFR are
  reflexive — 10 minutes a day with flashcards.
- **BIS Basel III framework** (bis.org) — the definitive free source for capital
  and liquidity rules; read the LCR and NSFR standards.
- **EBA reporting frameworks** — download real COREP/FINREP templates and
  validation-rule lists; reproduce them in Excel.
- **RBI Master Directions** on capital adequacy, LCR and returns — the primary
  source for the India-specific numbers and forms.
- **Arelle (free XBRL tool)** — validate a sample EBA instance to feel
  taxonomy-based validation.
- **Mock the interview**: record yourself computing a ratio out loud in under
  90 seconds — fluency under time pressure is what actually gets tested.
