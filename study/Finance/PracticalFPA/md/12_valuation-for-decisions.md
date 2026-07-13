# Valuation in practice (for decisions)

## What it is & where it's used

Valuation "for decisions" is deliberately *not* the 200-tab IPO model. It is the fast, defensible number you build to answer a business question: *Should we buy this competitor? Is this vendor overpriced? What's our own company roughly worth for ESOP pricing or a funding round? Is Segment B destroying value?* The output is a **range plus a recommendation**, delivered in hours or a day, not weeks.

Two workhorses do 90% of the job:

- **DCF (Discounted Cash Flow)** — intrinsic value from projected free cash flows discounted at WACC. Used when you have a view on future cash flows and want to test whether the market/asking price is sane.
- **Comps (Comparable company / transaction multiples)** — value by analogy: apply peer EV/EBITDA, EV/Revenue, or P/E to the target. Faster, market-anchored, needs a peer set.

Roles that pay for this: **Corporate Development / M&A**, **FP&A** (business-case and buy-vs-build decisions), **investment banking / equity research**, **PE/VC associates**, **strategy/consulting**, and increasingly **finance business partners** who must sanity-check a capex or acquisition proposal in a meeting.

## The gap: why companies want this (and college didn't teach it)

College teaches you the *Gordon Growth formula* and makes you discount a clean cash-flow stream to a single "correct" answer. Industry never has a clean stream. The gap is threefold:

1. **Speed and judgment over precision.** Employers want someone who, given a messy P&L, can produce a value range by end of day and *say which assumptions matter*. Textbooks reward exactness on made-up numbers.
2. **The plumbing MBA skips.** Converting equity value ↔ enterprise value (add net debt, minorities, subtract cash), mid-year convention, terminal value as 70–80% of value, calendarising to India's Apr–Mar FY, treating leases and ESOPs — none of this is in the lecture.
3. **Framing a decision, not a number.** A valuation that ends in "it's worth ₹142.7 cr" is useless. "It's worth ₹120–160 cr; below ₹135 cr it's accretive to our EPS, above ₹150 cr we're paying for synergies we haven't underwritten" — that gets you hired.

## What "proficient" looks like

A job-ready person can, **unaided and under time pressure**:

- Build a 5-year DCF from a P&L in under 45 minutes, with a clean **FCFF → Enterprise Value → Equity Value → per-share** bridge.
- Compute **WACC** from a cap structure and defend every input (risk-free = 10-yr G-Sec, ERP, beta, cost of debt post-tax).
- Pull a **comps table**, pick the right multiple for the sector (EV/EBITDA for manufacturing, EV/Revenue or EV/GMV for early SaaS, P/B for banks), and reconcile it against the DCF.
- Run a **sensitivity table** (value vs WACC and terminal growth) and state the swing factors.
- Say **"precision doesn't matter here"** when it doesn't — e.g. a ₹5 cr build-vs-buy where the answer is obvious at any reasonable discount rate.

## Hands-on: how to actually do it

### 1. The FCFF build (Excel)

Free Cash Flow to Firm each year:

```
FCFF = EBIT × (1 − tax) + D&A − Capex − ΔNet Working Capital
```

Layout with years across columns (B:F = FY26–FY30). Assume EBIT in row 10, D&A row 11, Capex row 12, ΔNWC row 13, tax rate in `$B$3`:

```excel
=B10*(1-$B$3) + B11 - B12 - B13        # FCFF for FY26, copy right
```

### 2. Discount factors and PV

Put WACC in `$B$2`. Use **mid-year convention** (cash arrives mid-period) for a tighter number:

```excel
# Period number in row 20: 1,2,3,4,5
# Mid-year discount factor:
=1/(1+$B$2)^(B20-0.5)
# PV of each year's FCFF:
=B14*B21          # FCFF row 14 × discount factor row 21
```

### 3. Terminal value (Gordon growth), then discount it

```excel
# Terminal value at end of year 5, g in $B$4:
=F14*(1+$B$4)/($B$2-$B$4)
# PV of TV (discount 5 full years, or 4.5 with mid-year):
=TV/(1+$B$2)^(F20-0.5)
```

Sanity check: **TV should be 60–80% of total EV**. Above 85% means your explicit forecast is doing no work — extend it.

### 4. EV → Equity → per share bridge

```excel
Enterprise Value      = SUM(PV of FCFF) + PV of TV
(−) Net Debt          = Total Debt − Cash & equivalents
(−) Minority Interest
(−) Preference capital
(+) Non-operating assets / investments
= Equity Value
÷ Diluted shares (incl. ESOP via treasury method)
= Value per share
```

### 5. WACC

```excel
# E = market cap, D = net debt, Re = cost of equity (CAPM), Rd = pre-tax cost of debt, Tc = tax
WACC = E/(E+D)*Re + D/(E+D)*Rd*(1-Tc)
# CAPM:
Re = Rf + Beta*ERP
# India today (illustrative): Rf ≈ 7.0% (10-yr G-Sec), ERP ≈ 6.5–7%, Beta from peers
=0.07 + 1.1*0.065     # → 14.15%
```

### 6. Comps table with a live multiple

```excel
# Peer EV/EBITDA in D2:D6; apply median to target EBITDA in $B$8:
=MEDIAN(D2:D6)*$B$8              # implied EV
# EV/Revenue quick screen for a target with revenue in $B$9:
=MEDIAN(E2:E6)*$B$9
```

### 7. Sensitivity (Data Table)

Put EV formula in a corner cell. Select the grid, `Data → What-If Analysis → Data Table`. Row input = terminal growth, Column input = WACC. Instant 2-D value matrix.

### 8. Python — same DCF, scriptable for screening many targets

```python
import numpy as np

def dcf_ev(fcff, wacc, g, midyear=True):
    fcff = np.array(fcff, dtype=float)
    n = np.arange(1, len(fcff) + 1)
    adj = 0.5 if midyear else 0.0
    df = 1 / (1 + wacc) ** (n - adj)
    pv_explicit = (fcff * df).sum()
    tv = fcff[-1] * (1 + g) / (wacc - g)
    pv_tv = tv / (1 + wacc) ** (n[-1] - adj)
    return pv_explicit + pv_tv, pv_tv / (pv_explicit + pv_tv)

ev, tv_share = dcf_ev([120, 138, 158, 179, 200], wacc=0.14, g=0.05)
print(f"EV ₹{ev:,.0f} cr | TV is {tv_share:.0%} of value")
```

## Worked example / mini-project

**Decision:** Your company (mid-size auto-components maker) is screening **TargetCo**, a bolt-on supplier. Asking price is **₹150 cr equity**. Should you bid?

**Given (₹ cr):** FY25 Revenue 100, EBIT 15, D&A 6, Capex 8, tax 25%, NWC growing ₹2 cr/yr. Growth 12% → tapering. Net debt ₹20 cr. Peers trade at **8× EV/EBITDA**. WACC 14%, terminal g 5%.

**FCFF forecast:**

| Item (₹ cr) | FY26 | FY27 | FY28 | FY29 | FY30 |
|---|---|---|---|---|---|
| EBIT | 16.8 | 18.8 | 20.7 | 22.4 | 23.9 |
| EBIT×(1−0.25) | 12.6 | 14.1 | 15.5 | 16.8 | 17.9 |
| + D&A | 6.7 | 7.3 | 7.8 | 8.2 | 8.5 |
| − Capex | 9.0 | 9.7 | 10.3 | 10.7 | 11.0 |
| − ΔNWC | 2.0 | 2.0 | 2.0 | 2.0 | 2.0 |
| **FCFF** | **8.3** | **9.7** | **11.0** | **12.3** | **13.4** |

**DCF:** PV of FCFF (mid-year, 14%) ≈ ₹37 cr. Terminal value = 13.4×1.05/(0.14−0.05) = **₹156 cr**; PV ≈ **₹85 cr**. TV is 70% of EV — healthy.

- **Enterprise Value ≈ ₹122 cr** → − net debt ₹20 cr → **Equity ≈ ₹102 cr**.

**Comps cross-check:** FY25 EBITDA = EBIT 15 + D&A 6 = ₹21 cr. 8× = **EV ₹168 cr** → − ₹20 cr = **Equity ₹148 cr**.

**The decision (this is the deliverable):**

> DCF says ₹102 cr equity, comps say ₹148 cr. The gap is the market pricing in growth our cash flows don't fully capture. The ₹150 cr ask sits at the *top* of the comps range and ~45% above intrinsic DCF. **Recommendation: counter at ₹110–125 cr.** Above ₹135 cr, the deal only works if we can underwrite ≥₹4 cr/yr of procurement/logistics synergy — which we have not validated. Precision beyond this range is wasted; the negotiation, not the third decimal, decides the outcome.

## How it's tested

**Interview questions**
- "Walk me from EBITDA to equity value per share." (The bridge — most common screen.)
- "Terminal value is 90% of your DCF. Comfortable? What do you change?"
- "EV/EBITDA vs P/E — when do you use which, and why is EV/EBITDA capital-structure neutral?"
- "Your WACC drops 1% — roughly what happens to value?" (Should answer *directionally and materially*, ~15–25% for a growth name.)
- "When would you *not* build a DCF?"

**Practical tests**
- **Timed Excel case (45–90 min):** raw P&L + balance sheet handed over; build DCF + comps + a football-field chart and a one-line recommendation. Graded on the *bridge, WACC defensibility, and sensitivity* — not formatting.
- **Take-home M&A screen:** "Here are 5 targets, pick the one to pursue." They test whether you triage with quick comps before over-modelling.
- **LBO / accretion-dilution** for PE/IB: given purchase price and financing, is the deal EPS-accretive?

## Common mistakes & how pros avoid them

| Mistake | Fix |
|---|---|
| Discounting FCFF with cost of equity | FCFF → **WACC**; FCFE → cost of equity. Never mix. |
| Mixing EV and equity items | EV multiples ↔ EV numerator (EBITDA, EBIT, sales); equity multiples ↔ P/E, P/B. Don't apply EV/EBITDA to net income. |
| Terminal g ≥ nominal GDP | Cap g at ~4–5% India nominal-ish; a company can't outgrow the economy forever. |
| Terminal value 90%+ of EV | Extend explicit forecast or use an exit multiple as a check. |
| Forgetting the bridge | Always subtract net debt, minorities, prefs to get to equity. |
| False precision | Report a **range**; run sensitivity; state the 2 assumptions that move it. |
| Cherry-picked peers | Match size, growth, margins, geography; show median *and* range, not one flattering comp. |
| Double-counting synergies into standalone value | Value standalone first, then show synergy as a separate, clearly-flagged layer. |

## Learn-it roadmap & resources

**Time to proficiency: 6–10 weeks** part-time if you already know accounting.

- **Weeks 1–2:** FCFF/FCFE mechanics + the bridge. Build 3 DCFs from scratch, no template.
- **Weeks 3–4:** WACC, CAPM, beta unlevering/relevering; sensitivity tables.
- **Weeks 5–6:** Comps — build a peer set from screeners (Screener.in, Tijori for India), reconcile with DCF.
- **Weeks 7–8:** M&A screening, accretion/dilution, a light LBO.
- **Ongoing:** value 1 real listed company a week; check against the CMP and explain the gap.

**Resources**
- *Damodaran Online* (NYU) — free spreadsheets, India ERP/beta data, the global gold standard.
- Aswath Damodaran's YouTube valuation series (free).
- Macabacus / Breaking Into Wall Street / Wall Street Prep — paid, template-heavy, interview-focused.
- **Screener.in** and **Tijori** for Indian financials; NSE/BSE filings; RBI for the 10-yr G-Sec.
- Your **CA Intermediate FM** already covers cost of capital, leverage, and capital budgeting — leverage it directly.
- Certifications that signal this: **CFA Level II** (equity valuation), or a focused financial-modeling course (FMVA / WSP).

## Quick-reference

| Item | Formula / rule |
|---|---|
| FCFF | EBIT(1−t) + D&A − Capex − ΔNWC |
| FCFE | FCFF − Interest(1−t) + Net borrowing |
| WACC | E/V·Re + D/V·Rd(1−t) |
| CAPM (Re) | Rf + β·ERP |
| Terminal value | FCFF₅(1+g)/(WACC−g) |
| EV → Equity | EV − net debt − minorities − prefs + non-op assets |
| Discount (mid-year) | 1/(1+WACC)^(n−0.5) |
| India Rf | 10-yr G-Sec yield (~7%) |
| India ERP | ~6.5–7% |
| Sector multiple | Mfg → EV/EBITDA; SaaS → EV/Revenue; Bank → P/B; mature → P/E |
| TV as % of EV | Aim 60–80%; >85% = extend forecast |
| Excel sensitivity | Data → What-If → Data Table (WACC × g) |
| Golden rule | Deliver a **range + a decision**, not a single number |
