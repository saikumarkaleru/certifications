# DCF Valuation — Interview Study Guide

A cheat sheet for defending every line of this project in an equity-research
interview. The model pulls a **real** company from yfinance (default: Apple),
derives its cash flows, and values it from first principles.

---

## 1. 30-Second Pitch
"I built a live discounted-cash-flow model. It pulls a real company's three
financial statements from yfinance, derives its unlevered free cash flow
(FCFF), and estimates a WACC using CAPM with a live 10-year Treasury yield as
the risk-free rate and the company's real beta. It projects FCFF five years
with a fading growth rate, builds two terminal values — a Gordon perpetuity and
an exit EV/EBITDA multiple — discounts everything to an enterprise value, and
bridges to an intrinsic value per share. Then it stress-tests that with
bull/base/bear scenarios, a WACC-by-terminal-growth sensitivity table, and a
reverse DCF that backs out the growth the current price is implying. For Apple
today the plain FCFF model screens the stock as expensive, and the reverse DCF
says the market is pricing in ~50%+ near-term FCFF growth — which is the real
debate."

---

## 2. What a DCF Is and Why Equity Research Uses It
A DCF values a business as the **present value of the cash it will generate for
its capital providers over its life**. It is *intrinsic* valuation — the value
comes from the company's own cash flows and risk, not from what peers trade for.

Equity research uses it because it forces every assumption to be explicit
(growth, margins, risk), it is independent of market sentiment so it can flag
mispricing, and it ties directly to cash — what owners actually receive. It is
run **alongside** comparable-company analysis (see project 2) for a market view.

---

## 3. THE Key Answers (memorize these)
**Why discount?** A dollar in the future is worth less than a dollar today —
today's dollar can be invested to earn a return, and future money carries risk
and inflation. Discounting converts every future dollar into "today's dollars".

**What is FCFF and why use it (not net income or FCFE)?** Free Cash Flow to the
Firm is the cash the operating business generates *before financing* — after
tax but before interest. It belongs to **all** capital providers (debt +
equity), so it must be discounted at the **WACC** (the blended cost of all
capital). We build it up as:
`FCFF = EBIT × (1 − tax) + D&A − Capex − increase in net working capital`.

**What is WACC?** The Weighted Average Cost of Capital — the blended annual
return debt and equity holders require, weighted by how much of each the firm
uses. `WACC = E/V·Ke + D/V·Kd·(1−tax)`. Cost of equity `Ke` comes from CAPM:
`Ke = risk-free + beta × equity risk premium`. It's the discount rate because
it reflects the risk/opportunity cost of the cash flows.

**What is Terminal Value?** A business doesn't stop after five years, but we
can't forecast forever, so we capture all cash flows after year five in one
number. Gordon: `TV = FCFF₅ × (1+g) / (WACC − g)`. We also compute an exit
EV/EBITDA multiple as a cross-check and blend the two.

---

## 4. Walkthrough (the build, module by module)
1. **`src/dcf/data.py`** — pulls income statement, balance sheet, cash-flow
   statement and market data (price, shares, beta) via yfinance, plus the 10Y
   Treasury yield from `^TNX`. Caches the extracted inputs to `input/` and falls
   back to that cache (then a bundled snapshot) if offline — so it always runs.
2. **`src/dcf/fcff.py`** — derives FCFF for each historical year from the
   statements and cross-checks it against `CFO + after-tax interest − capex`.
   The base FCFF is the multi-year **average** to normalise one-off
   working-capital swings.
3. **`src/dcf/wacc.py`** — CAPM cost of equity, cost of debt (interest/total
   debt, or risk-free + spread if not disclosed), market-value weights, WACC.
4. **`src/dcf/model.py`** — the engine: fading-growth projection, two terminal
   values, discounting, EV→equity bridge, scenarios, the 2-way sensitivity
   grid, and the reverse-DCF bisection solver.
5. **`src/dcf/report.py`** — writes the Excel workbook (Assumptions, DCF,
   Scenarios, Sensitivity, ReverseDCF) and the two charts.
6. **`main.py`** — orchestrates the above and prints the console summary.

---

## 5. Assumptions Defended (one line each)
- **Base FCFF = 4-year average** — normalises a single year's working-capital
  swing so the base case isn't distorted by one odd year.
- **Year-1 growth 8%, fading to terminal** — above GDP early, decaying toward
  the long-run rate; more realistic than a flat number.
- **Terminal growth 2.5%** — roughly long-run nominal GDP; a firm can't outgrow
  the economy forever, and g **must** stay below WACC or Gordon breaks.
- **Equity risk premium 5.0%** — long-run US average; the extra return equities
  demand over the risk-free rate.
- **Exit EV/EBITDA 14×** — a mid-range mature-large-cap multiple, used as a
  market-based cross-check on the Gordon terminal value.
- **Risk-free = live 10Y Treasury (^TNX)** — the standard proxy for a
  long-horizon riskless rate.

---

## 6. Interview Q&A

**Q1. "Walk me through a DCF."**
Derive unlevered free cash flow (FCFF) from the statements, project it ~5 years
with fading growth, discount each year at the WACC, compute a terminal value
(Gordon and/or exit multiple) and discount it back, sum to enterprise value,
subtract net debt for equity value, divide by shares for value per share, and
compare to the current price.

**Q2. "Why FCFF and WACC, not FCFE and cost of equity?"**
FCFF is pre-financing cash available to everyone, so it pairs with WACC (the
cost of all capital). FCFE is post-interest cash for equity only, so it pairs
with the cost of equity. Both should give a similar equity value; I use FCFF/WACC
because it separates operating performance from the capital structure.

**Q3. "Your model says Apple is overvalued — do you believe it?"**
On a strict FCFF basis, yes, it screens expensive — that's a known feature of
mega-caps: the market prices in more growth and durability than a mechanical
5-year fade captures. That's exactly why I built the **reverse DCF**: it says
the price implies ~50%+ near-term FCFF growth. The real question isn't "is the
formula right," it's "is that implied growth achievable" — which is a research
judgment, and where I'd push my forecasts and margins.

**Q4. "What's the most sensitive assumption?"**
WACC and terminal growth, because together they drive the terminal value, which
is ~75% of EV here. Small changes in (WACC − g) move the answer a lot — that's
why I show a sensitivity grid rather than a single false-precise number.

**Q5. "How does the reverse DCF work?"**
I hold everything fixed except the year-1 growth rate and solve for the growth
that makes intrinsic value equal the market price. Value is monotincreasing in
growth, so I use bisection to squeeze the bracket. It reframes the question from
"what's it worth" to "what is the market assuming," which is more useful.

**Q6. "77% of your value is terminal value — is that a problem?"**
It's normal for a stable, cash-generative company. It's only a problem if the
terminal assumptions are unrealistic. I keep g below WACC and near long-run GDP,
and I cross-check the Gordon TV against an exit EV/EBITDA multiple; when the two
disagree a lot, that's a flag to revisit the assumptions.

**Q7. "Where could this model be wrong?"**
Single-point beta and a fixed ERP; a linear growth fade is a simplification;
terminal value dominates; yfinance line items can be noisy or restated. I'd
sanity-check FCFF against the filings, consider a normalised margin, and lean on
the scenario range rather than the point estimate.

---

## 7. Vocabulary
- **FCFF (Free Cash Flow to the Firm)** — unlevered, after-tax operating cash
  available to all capital providers; `EBIT(1−t) + D&A − Capex − ΔNWC`.
- **NOPAT** — Net Operating Profit After Tax = `EBIT × (1 − tax rate)`.
- **WACC** — weighted average cost of capital; the discount rate for FCFF.
- **CAPM** — Capital Asset Pricing Model; `Ke = rf + beta × ERP`.
- **Beta** — sensitivity of a stock's returns to the market; the systematic
  risk measure in CAPM.
- **ERP (Equity Risk Premium)** — extra return equities demand over the
  risk-free rate.
- **Terminal Value** — value of all cash flows after the explicit forecast, via
  Gordon growth or an exit multiple.
- **Enterprise Value (EV)** — value of the whole operating business (debt +
  equity claims).
- **Net Debt** — total debt minus cash; the bridge from EV to equity value.
- **Reverse DCF** — solving for the growth (or other input) the current market
  price implies.
