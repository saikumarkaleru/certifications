# Building an LBO Model (Sources/Uses, Debt Schedule, Returns)

## What you'll be able to do

Take a target, set an entry enterprise value off an EBITDA multiple, build a Sources & Uses table that funds the deal, layer a realistic debt stack (Term Loan A/B + a revolver + optionally mezzanine), forecast EBITDA and free cash flow, run a cash sweep that pays debt down year by year, exit at a multiple, and compute the two numbers a PE interviewer actually cares about — **IRR** and **MOIC** — then stress them on leverage and exit. You'll carry one target, **Deccan Components Ltd (DCL)**, from a ₹1,000 cr entry to a five-year return, to the rupee.

## The drill — step by step

**Step 1 — Set the entry.** DCL LTM EBITDA = ₹150 cr. Entry multiple = 8.0× → **Entry EV = ₹1,200 cr**. Assume no existing debt acquired (cash-free, debt-free deal), so equity purchase price = EV = 1,200. This is the "purchase enterprise value" line.

**Step 2 — Decide leverage.** Sponsors lever to what cash flow can service. Total debt = 4.5× EBITDA = ₹675 cr, split:

| Tranche | × EBITDA | ₹ cr | Rate | Amort |
|---|---|---|---|---|
| Term Loan A | 2.0× | 300 | 9.5% | 10%/yr mandatory |
| Term Loan B | 2.0× | 300 | 10.5% | 1%/yr, bullet |
| Revolver | — | 0 drawn | 9.0% | as needed |
| **Total debt** | **4.5×** | **675** | | |

**Step 3 — Sources & Uses.** Uses = what you must pay for. Sources = how you fund it. They must balance; the sponsor equity is the plug.

```
USES                          SOURCES
Purchase EV        1,200      Term Loan A          300
Transaction fees      30      Term Loan B          300
Financing fees        15      Revolver               0
                             Sponsor equity (plug) 645
TOTAL USES         1,245      TOTAL SOURCES       1,245
```

Sponsor equity = 1,245 − 675 = **₹570… wait, plug to balance: 1,245 − 600 (TLA+TLB) = ₹645 cr.** (Note the ₹45 cr of fees are funded by equity — that's why equity is 645, not 570.) Equity as % of total capitalisation = 645/1,245 = 51.8%.

**Step 4 — Project EBITDA and FCF.** DCL grows revenue 8% with 25% EBITDA margin holding. Build the cash available for debt paydown:

```
Cash for sweep = EBITDA − cash interest − cash taxes − capex − ΔNWC − mandatory amort
```

Year 1: EBITDA 150 × 1.08 = 162. Interest: TLA 9.5%×300 = 28.5, TLB 10.5%×300 = 31.5 → 60.0. D&A 30, EBIT 132, less interest 60 = PBT 72, tax @25% = 18, so cash taxes 18. Capex = 6% of sales (sales ≈ 648) = 38.9. ΔNWC = 8. Mandatory amort TLA 10%×300 = 30, TLB 1%×300 = 3. 

FCF before sweep = 162 − 60 − 18 − 38.9 − 8 = 37.1. Less mandatory amort 33 = **₹4.1 cr free for the cash sweep** in Year 1 (early years are tight — that's realistic).

**Step 5 — Debt schedule with cash sweep.** Each year: opening balance − mandatory amort − optional sweep = closing balance. Sweep hits the most expensive prepayable tranche first (usually TLB after TLA mandatory). Interest is computed on the average or opening balance (be consistent). Roll five years:

| ₹ cr | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| EBITDA | 162.0 | 175.0 | 189.0 | 204.1 | 220.5 |
| Cash interest | 60.0 | 56.5 | 52.2 | 47.0 | 40.8 |
| Cash taxes | 18.0 | 21.4 | 25.1 | 29.2 | 33.7 |
| Capex | 38.9 | 42.0 | 45.4 | 49.0 | 52.9 |
| ΔNWC | 8.0 | 8.6 | 9.3 | 10.0 | 10.8 |
| FCF pre-amort | 37.1 | 46.5 | 57.0 | 68.9 | 82.3 |
| Total debt paid | 37.1 | 46.5 | 57.0 | 68.9 | 82.3 |
| **Debt closing** | **637.9** | **591.4** | **534.4** | **465.5** | **383.2** |

By Year 5, ₹675 cr of debt is down to **₹383.2 cr** — the deleveraging engine that drives PE returns.

**Step 6 — Exit and returns.** Exit at Year 5, EBITDA = ₹220.5 cr. Exit multiple — conservatively assume *multiple contraction* to 7.5× (you never underwrite to expansion):

```
Exit EV = 7.5 × 220.5 = 1,653.8
− Net debt at exit      (383.2)  [assume minimal cash]
= Exit equity value    1,270.6
```

MOIC = exit equity / entry equity = 1,270.6 / 645 = **1.97×**. IRR = MOIC^(1/5) − 1 = 1.97^0.2 − 1 = **14.5%**. Below the ~20% PE hurdle — so at 8.0× entry / 4.5× leverage / 7.5× exit, this deal is marginal. That's a *finding*, and knowing it beats a model that always says "great deal."

## The output

The finished LBO is four linked blocks on one screen: Sources & Uses (balances at 1,245), the debt schedule (above), the FCF build, and a returns box:

```
Entry equity            645.0
Exit EV (7.5×)        1,653.8
Exit net debt          (383.2)
Exit equity          1,270.6
MOIC                    1.97×
IRR (5-yr)              14.5%
```

Return attribution (the "bridge" PE loves): of the ₹625.6 cr equity gain, **deleveraging** contributed 675 − 383 = ₹291.8 cr, **EBITDA growth** at constant multiple contributed (220.5−150)×7.5 = ₹528.8 cr, and **multiple change** contributed (7.5−8.0)×150 = −₹75 cr. That decomposition is the answer to "where do your returns come from?"

## Checks & gotchas

- **Sources must equal Uses** to the rupee, every time, including fees. Fees are a Use funded by equity — forgetting them overstates returns.
- **The revolver is the backstop**: if FCF goes negative, you *draw* the revolver, you don't create negative debt paydown. Model a minimum cash balance.
- **Interest is circular** (interest depends on debt, debt depends on sweep, sweep depends on interest). Enable iterative calc or use a beginning-balance interest convention to break it cleanly.
- **Never underwrite multiple expansion.** Assume flat or contracting exit; if the deal only works on expansion, it doesn't work.
- **Cash taxes ≠ book taxes** once you have amortising fees and interest shields — keep a separate tax build.
- **MOIC and IRR must be consistent**: IRR ≈ MOIC^(1/years) − 1 only with a single entry and single exit and no interim dividends; a dividend recap changes both.
- **Sanity**: entry leverage 4.5× with EBITDA margin 25% and rising rates — check the interest coverage (EBITDA/interest) stays above ~2.5× or the deal is un-financeable.

## Interview drill

**Q: What are the three drivers of LBO returns?** Deleveraging (FCF pays down debt, so equity grows even at a flat multiple), EBITDA growth (revenue growth plus margin expansion), and multiple arbitrage (buy low, sell high — but you never *underwrite* to this; you assume flat or lower exit). In my DCL model, deleveraging added ₹292 cr and EBITDA growth ₹529 cr, while the multiple contraction *cost* ₹75 cr — showing returns can survive a worse exit multiple if the operating story delivers.

**Q: Why does more leverage boost IRR but raise risk?** Higher debt shrinks the equity cheque, so the same absolute equity gain is a larger percentage return — that's the IRR lift. But it also raises fixed cash interest, thinning the FCF cushion; a small EBITDA miss can breach covenants or force a revolver draw, and equity is first-loss. Leverage amplifies both the upside and the probability of a zero.

**Q: Walk me from entry EV to sponsor equity.** Entry EV = entry multiple × LTM EBITDA. Add transaction and financing fees to get total uses. Fund it with the debt tranches you can raise given leverage capacity; sponsor equity is the plug that makes sources equal uses. So equity = total uses − total debt drawn, and it explicitly absorbs the fees.

## Practise free

No LBO software needed — it's all Excel. Pull a mid-cap's EBITDA from **Screener.in**, pick an entry multiple from **comparable transactions** (news of recent PE deals, or trading comps as a floor). Build Sources & Uses, then a five-row debt schedule with a `=MIN(cash_available, debt_outstanding)` sweep and iterative calculation turned on (File ▸ Options ▸ Formulas ▸ Enable iterative). Compute IRR with `=RATE` or `=(exit/entry)^(1/n)-1`, and MOIC as a simple ratio. Add a `Data Table` sensitising IRR against entry leverage (rows) and exit multiple (columns) to reproduce the classic PE sensitivity grid. Rehearse the return-attribution bridge by hand — that verbal decomposition is what actually gets tested in PE interviews.
