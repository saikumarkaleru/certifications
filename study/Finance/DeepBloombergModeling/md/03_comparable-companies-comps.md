# Building a Comparable Companies (Comps) Analysis

## What you'll be able to do

Build a trading-comps table from scratch: choose a defensible peer set, pull the raw inputs (market cap, net debt → enterprise value, revenue, EBITDA, EBIT, net income, shares, EPS), compute the multiples (EV/EBITDA, EV/Sales, EV/EBIT, P/E, PEG), calendarise so mismatched fiscal years are comparable, strip one-offs so the numbers are clean, take the median, and apply it to your target to imply a value and a football-field range. Worked end-to-end on Indian IT services with Infosys as the target.

## The drill — step by step

**1. Pick the peer set — this is 50% of the work.** Comparable means *comparable*: same industry, similar business model, similar size, geography and margin profile. Use `EQS`/BICS on Bloomberg or CapIQ Screening: BICS "IT Consulting & Services", country India, market cap band. For Infosys the honest peer set is TCS, Wipro, HCLTech, Tech Mahindra, LTIMindtree. You could add Accenture/Cognizant as global reference points, but flag them — different scale and currency. **Write down your inclusion rule**; you will be asked to defend every name.

**2. Pull the raw inputs into a clean grid** (from your `Data_Raw` tab, Chapter 2). Per company you need:

- Share price and diluted shares → **Equity value (market cap)**
- Total debt + preferred + minority interest − cash & equivalents → **Net debt**
- **Enterprise Value (EV) = Equity value + Net debt** (+ minorities + preferred)
- Revenue, EBITDA, EBIT, Net income, EPS — both **LTM** (last twelve months) and **forward** (NTM / FY+1 consensus, `BEST_`/`IQ_NTM`)

**3. Compute the multiples.** The iron rule: **numerator and denominator must belong to the same claimants.**

| Multiple | Formula | Whose metric |
|---|---|---|
| EV/EBITDA | EV ÷ EBITDA | capital-structure-neutral, pre-D&A |
| EV/EBIT | EV ÷ EBIT | after D&A, still pre-financing |
| EV/Sales | EV ÷ Revenue | for low/negative-margin names |
| P/E | Price ÷ EPS (or Equity ÷ Net income) | equity holders only |
| PEG | P/E ÷ EPS growth % | P/E normalised for growth |

**EV** pairs with pre-interest metrics (EBITDA, EBIT, Sales) because EV represents *all* capital providers. **P/E** pairs with net income/EPS because both are *after* interest — equity-only. Never put EV over net income, or price over EBITDA.

**4. Calendarise.** Infosys, TCS, Wipro run **March year-ends**; Accenture runs **August**, Cognizant **December**. Comparing raw FY figures mixes periods. Fix by converting everyone to LTM, or calendarising to a common calendar year: e.g. CY = (months of FYn in the calendar year × FYn) + (remaining months × FYn+1), weighted. For a purely Indian peer set with aligned March ends this is mostly moot — which is itself a reason to keep the set domestic.

**5. Adjust for one-offs (clean the metric).** Strip non-recurring items so multiples reflect underlying earnings: remove litigation settlements, restructuring, one-time visa/impairment charges, gains on asset sales; normalise a tax rate if a period had a one-off tax credit. Document each adjustment in a footnote row. A peer that took a big restructuring charge will show a distorted EBIT — un-distort it or its multiple lies.

**6. Summarise — median, not just mean.** Compute **min, 25th percentile, median, mean, 75th, max** for each multiple down the peer column. **Lead with the median** — it's robust to one outlier; the mean gets dragged by a single 40x name.

**7. Imply the target's value.** Apply the peer median multiple to the target's own metric:

- Implied EV = peer median EV/EBITDA × target EBITDA
- Implied Equity = Implied EV − target net debt
- Implied price = Implied equity ÷ target diluted shares
- Cross-check with P/E: Implied price = peer median P/E × target EPS

**8. Football field.** Plot each methodology's implied per-share range (25th–75th percentile of each multiple) as a horizontal bar; the overlap is your defensible value range, next to the current price.

**Worked example — Infosys target, illustrative LTM figures:**

| Company | EV (₹ cr) | EBITDA (₹ cr) | EV/EBITDA | Net income (₹ cr) | P/E |
|---|---|---|---|---|---|
| TCS | 14,20,000 | 62,000 | 22.9x | 46,000 | 30.9x |
| Wipro | 2,60,000 | 22,000 | 11.8x | 13,100 | 19.8x |
| HCLTech | 3,90,000 | 34,000 | 11.5x | 15,700 | 24.8x |
| Tech Mahindra | 1,30,000 | 9,500 | 13.7x | 4,300 | 30.2x |
| LTIMindtree | 1,60,000 | 8,200 | 19.5x | 4,600 | 34.8x |
| **Median** | | | **13.7x** | | **30.2x** |

Apply to Infosys (EBITDA ≈ ₹38,900 cr, net debt ≈ −₹30,000 cr net cash, ~415 cr shares, EPS ≈ ₹66):
- Implied EV = 13.7 × 38,900 ≈ **₹5,32,930 cr**
- Implied equity = 5,32,930 + 30,000 (net cash adds back) ≈ **₹5,62,930 cr**
- Implied price = 5,62,930 cr ÷ 415 cr ≈ **₹1,357/sh**
- P/E cross-check: 30.2 × 66 ≈ **₹1,993/sh** → the spread tells you which multiple the market is really paying and that Infosys screens richer on P/E than EV/EBITDA vs. this set.

## The output

A one-page comps sheet: peer rows with EV build-up and each multiple; a stats block (min/25th/median/mean/75th/max) per multiple; a target-implied-value block showing EV → equity → per-share for EV/EBITDA and P/E; and a football-field chart with the implied ranges against the live price. Footnotes list peer-selection rationale and every one-off adjustment.

## Checks & gotchas

- **EV must be consistent** — always subtract cash and add debt, minorities and preferred the same way for every peer, or the ranking is noise.
- **Net cash companies** (most Indian IT) have EV < market cap; adding back net cash *raises* implied equity. Get the sign right.
- **LTM vs. forward mismatch** — never compare one peer's forward multiple to another's trailing. Pick one basis for the whole table.
- **Diluted, not basic shares** — include options/RSUs; treasury-stock method.
- **Outliers** — a high-growth or newly-listed peer can carry a 40x multiple; that's why you lead with the median and eyeball the range.
- **Currency** — don't mix an Accenture USD EV/EBITDA into an INR table without noting the multiple is currency-neutral but the size context isn't.
- **Garbage peers = garbage output.** The most common mistake is a lazy peer set. Comps are only as good as comparability.

## Interview drill

**Q: "Why EV/EBITDA over P/E?"**
A: "EV/EBITDA is capital-structure-neutral and pre-D&A, so it compares operating value across companies with different debt loads and depreciation policies — cleaner for cross-company comparison and for buyers who'll refinance the target. P/E is distorted by leverage and tax. I'd use both and explain divergences."

**Q: "Your target trades at a discount to the peer median EV/EBITDA — buy signal?"**
A: "Not automatically. A discount can be justified — slower growth, lower margins, weaker returns on capital, governance or client-concentration risk. I'd check whether the discount is explained by fundamentals before calling it cheap. Comps tell you *where* it trades, not *why*."

**Q: "How do you handle mismatched fiscal year-ends in a comps set?"**
A: "Calendarise — convert everyone to LTM or to a common calendar year by weighting the overlapping fiscal periods — so I'm comparing the same window. For an all-Indian March-end set it's usually moot, which is one reason I prefer a domestic peer group."

## Practise free

- **Screener.in / TIKR / stockanalysis.com** — pull EV, EBITDA, net income, P/E for TCS, Wipro, HCLTech, Tech Mahindra, LTIMindtree and Infosys and build the exact grid above by hand.
- **Tijori Finance** — free peer-comparison views that mirror an RV screen.
- **Python** — `yfinance` `.info` gives `enterpriseValue`, `enterpriseToEbitda`, `trailingPE`; loop over the peer tickers, `pd.DataFrame`, compute median, imply Infosys value. This is the single best rep: it forces you to build EV yourself and see where net cash flips the sign.
Drill target: reproduce the median EV/EBITDA and the implied Infosys price, then write the two-line rationale for why Infosys deserves a premium or discount to it.
