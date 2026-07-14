# Building a Full DCF from Terminal Data

## What you'll be able to do

Pull a company's historicals off a terminal (Bloomberg/CapIQ or a free proxy), forecast unlevered free cash flow (FCFF) for five years, build a WACC bottom-up using CAPM, layer in a terminal value two ways (Gordon growth and exit multiple), discount everything, walk enterprise value down to a per-share equity value, and pressure-test it with a 2-way sensitivity grid and a football-field chart. You will carry one real-ish company — call it **Bharat Consumer Ltd (BCL)** — all the way to a rupee-precise fair value, and you'll know how to spot when your own model is quietly cheating.

## The drill — step by step

**Step 1 — Pull the raw financials.** On Bloomberg, `BCL IN Equity <GO>`, then `FA <GO>` (Financial Analysis). Tab to Income Statement and Cash Flow, set periodicity Annual, and export to Excel with the red `Export` button (or `=BDH("BCL IN Equity","SALES_REV_TURN","2021","2025")` in the Excel add-in). On CapIQ it's the "Financials" template. Free proxy: Screener.in export, or Tijori/annual report PDFs. Grab five years so you have growth rates and margins to anchor forecasts.

BCL FY25 actuals (₹ cr): Revenue 12,000, EBITDA 2,160 (18.0%), D&A 360, EBIT 1,800, tax rate 25.17% (India new regime + surcharge/cess), Capex 420, and change in working capital that consumed ₹150 cr as sales grew.

**Step 2 — Forecast the revenue driver.** Don't forecast 15 lines; forecast the driver and let margins do the rest. BCL grew revenue ~11% historically; I taper it: 11% → 10% → 9% → 8% → 7%. Hold EBITDA margin flat at 18% (state this assumption explicitly — margin expansion is where models lie). D&A ≈ 3% of sales, capex ≈ 3.5% of sales, working capital drag ≈ 1.25% of incremental sales.

**Step 3 — Build FCFF, year by year.** The formula, memorise it:

```
FCFF = EBIT × (1 − tax) + D&A − Capex − ΔNWC
```

Year 1 (FY26): Revenue = 12,000 × 1.11 = 13,320. EBITDA = 2,397.6. D&A = 399.6. EBIT = 1,998. NOPAT = 1,998 × (1−0.2517) = 1,495.1. + D&A 399.6 − Capex (3.5%×13,320 = 466.2) − ΔNWC (1.25% × 1,320 = 16.5) = **FCFF ₹1,412.0 cr**.

Roll the same engine forward:

| ₹ cr | FY26 | FY27 | FY28 | FY29 | FY30 |
|---|---|---|---|---|---|
| Revenue | 13,320 | 14,652 | 15,971 | 17,249 | 18,456 |
| EBIT | 1,998.0 | 2,197.8 | 2,395.7 | 2,587.3 | 2,768.4 |
| NOPAT | 1,495.1 | 1,644.6 | 1,792.7 | 1,936.1 | 2,071.6 |
| + D&A | 399.6 | 439.6 | 479.1 | 517.5 | 553.7 |
| − Capex | 466.2 | 512.8 | 559.0 | 603.7 | 646.0 |
| − ΔNWC | 16.5 | 16.7 | 16.5 | 16.0 | 15.1 |
| **FCFF** | **1,412.0** | **1,554.7** | **1,696.3** | **1,833.9** | **1,964.2** |

**Step 4 — Build WACC from CAPM.** Risk-free: `GIND10YR Index <GO>` → 10-yr G-sec ≈ **6.9%**. Beta: on Bloomberg `BCL IN Equity BETA <GO>` gives raw and adjusted beta; use adjusted (Blume) ≈ **0.85** (or lever an industry beta). Equity risk premium for India: Damodaran's mature-market + country risk ≈ **7.5–8.0%**; use 7.5%.

```
Cost of equity = Rf + β × ERP = 6.9% + 0.85 × 7.5% = 13.28%
```

Cost of debt: BCL's coupon / rating spread ≈ 8.5% pre-tax, after-tax = 8.5% × (1−0.2517) = 6.36%. Capital weights at market: equity ₹28,000 cr, debt ₹4,000 cr → E/V = 87.5%, D/V = 12.5%.

```
WACC = 0.875 × 13.28% + 0.125 × 6.36% = 11.62% + 0.795% = 12.42%
```

Round to **12.4%**.

**Step 5 — Terminal value, two ways.** Gordon: pick g = 5.0% (below nominal GDP ~10.5%, sanity intact).

```
TV = FCFF_FY30 × (1+g) / (WACC − g) = 1,964.2 × 1.05 / (0.124 − 0.05)
   = 2,062.4 / 0.074 = ₹27,870 cr
```

Exit multiple cross-check: apply 12× EV/EBITDA to FY30 EBITDA (18% × 18,456 = 3,322): TV = ₹39,864 cr. The two disagree — that's the point; the Gordon TV implies a cheaper business. I'll run the DCF on Gordon and show exit as a bound.

**Step 6 — Discount.** Discount factor = 1/(1.124)^t (mid-year convention optional; here year-end).

| | FY26 | FY27 | FY28 | FY29 | FY30 | TV |
|---|---|---|---|---|---|---|
| CF | 1,412.0 | 1,554.7 | 1,696.3 | 1,833.9 | 1,964.2 | 27,870 |
| DF @12.4% | 0.8897 | 0.7916 | 0.7043 | 0.6266 | 0.5575 | 0.5575 |
| PV | 1,256.3 | 1,230.7 | 1,194.7 | 1,149.1 | 1,095.1 | 15,538.5 |

Sum of PV(explicit FCFF) = ₹5,925.9 cr. PV(TV) = ₹15,538.5 cr. **Enterprise Value = ₹21,464 cr.**

**Step 7 — EV-to-equity bridge.** 

```
Equity value = EV − Net debt − Minority interest − Preferred + Investments/associates
```

BCL: EV 21,464 − Net debt (debt 4,000 − cash 900 = 3,100) − minority 200 + associate investments 300 = **₹18,464 cr**. Shares outstanding = 100 cr. **Fair value = ₹184.6 / share.** Current price ₹280 → the DCF says overvalued ~34%; you'd flag that, not force the assumptions to fit.

## The output

A one-screen model block: the FCFF build (table above), a WACC box (Rf 6.9%, β 0.85, ERP 7.5%, Ke 13.28%, Kd(at) 6.36%, weights 87.5/12.5, WACC 12.4%), the discounting strip, and the bridge:

```
EV                     21,464
 − Net debt            (3,100)
 − Minority              (200)
 + Associates             300
= Equity value         18,464
÷ Shares (cr)             100
= Value / share      ₹ 184.6
```

TV as % of EV = 15,538.5 / 21,464 = **72.4%**. Implied exit EV/EBITDA on the Gordon TV = 27,870 / 3,322 = **8.4×** — internally consistent and *below* the 12× comps multiple, so the DCF is conservative.

## Checks & gotchas

- **TV should be 60–80% of EV.** 72% is normal. Above ~85% means your explicit window is too short or g too high.
- **Implied terminal growth vs implied exit multiple** must both be sane. Back out each from the other and eyeball them.
- **g < WACC always**, and g ≤ long-run nominal GDP. g of 8% in a 12.4% WACC world quietly doubles your TV.
- **Consistency of nominal terms**: nominal cash flows → nominal WACC (India, don't mix a real Rf with nominal growth).
- **Tax rate**: use the marginal/statutory rate for NOPAT, not the accounting effective rate distorted by one-offs.
- **Don't double-count**: FCFF is pre-financing, so discount at WACC and *never* subtract interest in the cash flow. Subtract debt only in the bridge.
- **Mid-year convention** lifts value ~6% (half a period less discounting); pick one and disclose it.
- **Circularity**: market-value weights depend on the equity value you're solving for. Iterate once or fix weights at target capital structure.

## Interview drill

**Q: Why FCFF discounted at WACC and not FCFE at cost of equity?** FCFF is capital-structure-neutral — it's the cash to all providers, so you discount at the blended cost of all capital (WACC) and get enterprise value. FCFE is post-debt cash to equity, discounted at Ke, giving equity value directly. FCFF is preferred when leverage is changing because WACC is more stable than a moving Ke; you avoid re-forecasting the debt schedule inside the cash flow.

**Q: Your terminal value is 72% of EV — is the model useless?** No, that's structurally normal because a going concern's value is dominated by cash flows beyond any five-year window. What matters is that the terminal assumptions are defensible: g of 5% is below nominal GDP, and the implied exit multiple of 8.4× is below trading comps of 12×, so I'm not smuggling in optimism through the terminal — if anything I'm conservative.

**Q: Move ERP from 7.5% to 8.5% — direction and rough magnitude?** Ke rises ~0.85%, WACC rises ~0.74%, so the denominator (WACC − g) widens and value falls sharply because TV is convex in the spread. A move from 12.4% to 13.1% WACC roughly cuts fair value from ₹185 toward ₹160 — a ~13% hit from a 1-point ERP change, which is exactly why the sensitivity table matters.

## Practise free

You don't need a live terminal. Pull five years of financials from **Screener.in** (free export to Excel) or the company's annual report; use **GIND10YR** substitute from RBI/worldgovernmentbonds.com for the risk-free rate; get **beta** by regressing 2 years of weekly stock returns against Nifty in Excel (`=SLOPE(stock_returns, index_returns)`) — that literally *is* what the terminal's BETA function does. Take **ERP** from Damodaran's free country-risk-premium spreadsheet (updated each January). Build the whole FCFF → WACC → TV → bridge in one Excel tab, then add a two-input `Data Table` (Data ▸ What-If ▸ Data Table) with WACC across the top and g down the side to reproduce the sensitivity grid and football field for free.
