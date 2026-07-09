# Study Guide — Credit Risk Scoring (Altman Z-Score + Merton)

## 30-second pitch
"I built a credit-risk tool that scores ~10 real large-cap companies for default
risk two independent ways. First, the **Altman Z-score** — an accounting model
that blends five balance-sheet ratios into one bankruptcy score. Second, the
**Merton structural model** — a market model that treats a company's equity as a
call option on its assets and backs out a probability of default. I then combine
them into a loan-book **expected loss** = PD × LGD × EAD. Data comes live from
Yahoo Finance with an offline fallback, and it's all packaged as a small Python
module with unit tests, an Excel report and charts."

## What it is
Two classic textbook credit models applied to a real universe (AAPL, MSFT, JPM,
XOM, JNJ, PG, WMT, KO, CAT, F):
- **Altman** looks *backwards* at the accounts (accounting / book values).
- **Merton** looks *forwards* using the *market's* view (equity price and its
  volatility). Comparing them is the whole point: where do the book and the
  market disagree about who's risky?

## The key interview answer
> "Why two models?"

Because they use different information and fail differently. Altman is cheap,
transparent and works off filings, but it's static and was calibrated on 1960s
manufacturers. Merton is forward-looking and reacts to the market in real time,
but it's only as good as its inputs (equity vol, the debt barrier) and assumes a
lognormal asset process. Using both gives a **triangulated** view: if the
accounts *and* the market both flag a name, that's a strong signal; when they
disagree, that's exactly where an analyst should dig.

## Code walkthrough
- **`src/credit/data.py`** — pulls balance sheet, income statement, market cap
  and 2yr price history per ticker via yfinance. yfinance row labels vary, so a
  robust helper (`_first_match`) scans candidate row names (exact then
  substring) and returns NaN if nothing matches. Equity volatility = std of
  daily log returns × √252. Everything is cached to `input/credit_inputs.csv`;
  on failure it loads the cache, and if there's no cache it uses a realistic
  hard-coded fallback. Reports LIVE / CACHED / FALLBACK.
- **`src/credit/altman.py`** — computes the five ratios, the weighted Z, and the
  Safe/Grey/Distress zone.
- **`src/credit/merton.py`** — solves the two-equation Merton system by
  fixed-point iteration for asset value V and asset vol σ_V, then DD = d2 and
  PD = N(−d2). Standard normal CDF from `math.erf` (no scipy). Guards against
  bad inputs (returns NaN + `converged=False` instead of crashing).
- **`src/credit/portfolio.py`** — merges both models, ranks issuers (by Z and by
  PD), flags agreement, and computes per-issuer and portfolio expected loss.
- **`src/credit/reporting.py`** — formatted 4-sheet Excel workbook plus two
  charts (Z bar chart by zone; PD-vs-Z scatter).
- **`main.py`** — orchestrates the pipeline and prints the console summary.
- **`tests/test_credit.py`** — Altman math against a hand-computed value, Merton
  sanity (PD∈[0,1], finite DD, convergence), leverage monotonicity (more debt →
  higher PD), and the EL identity.

## Interview Q&A
1. **What are the five Altman ratios and what do they measure?**
   X1 Working Capital/Total Assets (liquidity); X2 Retained Earnings/Total
   Assets (cumulative profitability / firm age); X3 EBIT/Total Assets (operating
   profitability — the highest-weighted, at 3.3); X4 Market Value of
   Equity/Total Liabilities (market leverage cushion); X5 Sales/Total Assets
   (asset turnover / activity).

2. **What do the Z zones mean?**
   Z > 2.99 = Safe (low bankruptcy risk); 1.81–2.99 = Grey (caution); < 1.81 =
   Distress (high risk). The weights and cutoffs came from Altman's 1968
   discriminant analysis on bankrupt vs healthy manufacturers.

3. **Explain the Merton model in one sentence.**
   Equity holders own a call option on the firm's assets struck at the face
   value of debt — if assets fall below debt at maturity they default, so the
   option-pricing math gives a probability of default.

4. **What is distance-to-default (DD) and how does it relate to PD?**
   DD = d2 = the number of standard deviations the firm's asset value sits above
   its default point at the horizon. PD = N(−DD): a DD of 2 implies ≈2.3% PD.
   Bigger DD ⇒ smaller PD.

5. **Why do these mega-caps show PD ≈ 0?**
   Over a *one-year* horizon, huge low-leverage firms are 8–14 standard
   deviations from default, and the normal tail past that is astronomically
   small. That's honest Merton behaviour, not a bug — Ford, the most levered
   name, is the one with a visible PD. Longer horizons or a stressed asset vol
   would raise the numbers.

6. **What is expected loss and what are LGD and EAD?**
   EL = PD × LGD × EAD. PD is the default probability (from Merton). LGD (loss
   given default) is the fraction *not* recovered — I use 0.45 for senior
   unsecured (≈55% recovery). EAD (exposure at default) is the dollars at risk —
   here an equal $10M line to each issuer. Sum the pieces for portfolio EL.

7. **Why did a bank (JPM) come out N/A on Altman?**
   The original Z-score was built for manufacturers; "working capital" and asset
   turnover aren't comparable for a bank, so some ratios are undefined. That's a
   real limitation of applying Altman across sectors — the honest answer is to
   use it only where it's calibrated, or switch to the market-based Merton view.

## Vocabulary
- **Altman Z-score** — accounting model that combines 5 ratios into one
  bankruptcy-risk score.
- **The 5 ratios** — X1 liquidity, X2 cumulative profitability, X3 operating
  profitability, X4 market leverage cushion, X5 asset turnover.
- **Distress / Grey / Safe zones** — Z < 1.81 / 1.81–2.99 / > 2.99.
- **Merton model** — structural credit model; equity as a call option on assets.
- **Distance-to-default (DD)** — std devs between asset value and the default
  point (= d2).
- **PD (probability of default)** — N(−DD); chance the firm defaults by the
  horizon.
- **LGD (loss given default)** — fraction of exposure lost in default (1 −
  recovery rate).
- **EAD (exposure at default)** — dollar amount at risk when default happens.
- **Expected loss (EL)** — PD × LGD × EAD.
- **Structural vs reduced-form vs accounting models** — structural (Merton) uses
  the firm's asset dynamics; reduced-form models default as an exogenous jump
  calibrated to credit spreads; accounting models (Altman) use book ratios.
- **Equity-as-a-call-option** — the core Merton insight: shareholders' limited
  liability makes equity a call on firm assets struck at the debt level.
