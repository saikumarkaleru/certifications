# ESOPs, Dilution and Share-Count Analysis

## The Problem / Why this matters
Per-share value is enterprise value less net debt divided by share count, and analysts spend almost all their effort on the numerator. The denominator is treated as a given, pulled from a data screen, and rarely forecast. For companies that pay a meaningful part of compensation in equity — technology, platforms, financial services, and increasingly others — the share count grows every year, and a five-year forecast that holds it constant systematically overstates value per share.

## Core Idea
Share count is a **forecast variable, not a constant**. Model it forward the same way revenue is modelled, with an explicit assumption for grants, exercises, buybacks and any planned issuance.

## Why it works this way
Share-based compensation is a real transfer of value from existing shareholders to employees. It does not appear as a cash outflow, which is exactly why it is easy to overlook — but the shareholder's claim on future cash flows is smaller afterwards, and that is economically identical to having paid cash.

```mermaid
graph LR
  A[Opening share count] --> B[+ Options/RSUs vesting and exercised]
  B --> C[+ New grants entering the pool]
  C --> D[+ Any equity issuance: QIP, warrants, conversions]
  D --> E[- Buybacks]
  E --> F[Closing share count for the forecast year]
```

## Full technical content

### Why share-based compensation is a real cost

The argument for excluding it — "it's non-cash" — fails on inspection:

- If the company paid the same employees in cash and simultaneously issued shares to raise that cash, nobody would call the compensation non-cash. The economics are identical; only the sequence differs.
- The cost is borne by shareholders through dilution rather than by the company through cash, which makes it invisible in cash-flow measures but no less real.
- **Excluding it from "adjusted EBITDA" while including the resulting shares in a diluted count double-benefits the presented figures**, and this presentation is common enough to warrant checking on every company that grants equity.

**The correct treatments, either of which is defensible:**
1. Treat share-based compensation as an **expense** and use the current share count; or
2. Exclude the expense but **forecast the growing share count** so the dilution appears in the denominator.

**What is not defensible is doing neither** — excluding the expense and holding the share count constant, which is the default in a surprising number of models.

### Building a share-count forecast

| Component | Source | Treatment |
|---|---|---|
| **Outstanding options/RSUs** | ESOP note: granted, vested, exercised, lapsed, outstanding | Apply the treasury method for in-the-money instruments |
| **Grant run-rate** | Historical grants as a percentage of equity | Project forward; check the remaining pool |
| **Pool exhaustion and top-ups** | Shareholder resolutions authorising new pools | A pool top-up resolution signals continued dilution |
| **Lapse rate** | Historical lapses in the ESOP note | Reduces gross dilution meaningfully in high-attrition businesses |
| **Buybacks** | Stated policy and history | Offsets dilution; check whether buybacks merely neutralise grants |
| **Planned issuance** | Board/shareholder approvals for QIP, preferential issue | Include with a stated price assumption |

**The buyback interaction is worth stating explicitly.** A company that buys back 1.5% of equity annually while granting 1.6% is not returning capital to shareholders — it is funding employee compensation with shareholder cash and reporting it as a return of capital. **Compare buyback volume to grant volume** before crediting a company with capital return. This single comparison changes the interpretation of many capital-allocation stories.

### The ESOP note — what to read

Indian companies disclose ESOP details in the annual report and in a separate statutory disclosure. The items worth extracting:

- **Options outstanding and exercise prices**, by tranche, which determines how many are in the money at any given price.
- **Vesting schedule**, which tells you the timing of dilution.
- **Grants during the year** as a percentage of equity — the run-rate.
- **Exercise price relative to market price at grant** — deep-discount grants transfer more value.
- **Any repricing** of existing options, which is a governance signal: it transfers value to employees after a share-price decline that shareholders absorb without adjustment.
- **Performance conditions**, if any. Options that vest on time alone reward tenure; options that vest on performance conditions align incentives, and which conditions were chosen tells you what the board wants management to optimise.

That last point connects to the management-quality analysis: **the vesting conditions are the clearest available statement of what management is actually incentivised to do**, and they are frequently more informative than anything said on an earnings call.

### The full-dilution checklist

Every instrument that can become a share:
1. Employee options and RSUs — treasury method, at the target price.
2. Convertible bonds and debentures — if-converted method.
3. Warrants — treasury method; check the exercise window.
4. Compulsorily convertible instruments — convert now; they are equity in substance.
5. Contingent consideration shares from acquisitions — include if the conditions are likely to be met.
6. Any board-approved but unissued equity.

### The per-share discipline in valuation

- **Use the diluted count consistent with the price.** Dilution computed at spot understates dilution at a higher target price, since exercise proceeds repurchase fewer shares as the price rises.
- **Add exercise proceeds** to equity value — the cash comes into the company.
- **Forecast the count for the valuation year.** If the target is based on FY29 earnings, use the FY29 share count, not today's.
- **Check the historical growth in share count.** A company whose share count has compounded at 3% annually for five years will likely continue, and a model holding it flat is inconsistent with the company's own record.

**Illustration of why this matters.** A company with 100mn shares grants 2% of equity annually. Over a five-year forecast, the share count reaches roughly 110mn, before considering any other issuance. A valuation producing ₹55,000mn of equity value in year five gives ₹550 per share on the current count and ₹500 on the forecast count — **a 9% difference produced entirely by the denominator**, and one that no amount of care in the operating forecast will surface.

### Anti-dilution and structural share-count issues

- **Rights issues** dilute only those who do not participate; the theoretical ex-rights price adjustment handles the arithmetic, and historical per-share data must be restated for the bonus element.
- **Bonus issues and splits** change the count without changing value, but every historical per-share series must be adjusted, and failing to do so produces nonsensical growth rates.
- **Preferential allotments** to promoters or investors at a discount transfer value to the allottee; check the pricing against the regulatory floor and the prevailing market price.
- **Differential voting rights shares**, where present, mean voting power and economic ownership diverge, which matters for control analysis.

## Common mistakes
- Holding the share count **constant** across a multi-year forecast.
- Excluding share-based compensation from earnings **and** ignoring the resulting dilution.
- Computing dilution at **spot** rather than at the target price.
- Adding dilutive shares while **omitting exercise proceeds**.
- Crediting a buyback as capital return without comparing it to **grant volume**.
- Ignoring **option repricing** as a governance signal.
- Not reading **vesting conditions** as evidence of what management is incentivised to do.
- Failing to restate historical per-share data for bonuses and splits.
- Treating compulsorily convertible instruments as debt.

## Interview angle
"How do you handle stock-based compensation in a valuation?" State the principle first: it is a genuine transfer of value from shareholders to employees, and the fact that it is non-cash is a matter of form, since paying in cash and issuing shares to fund it is economically identical. So either expense it and use the current share count, or exclude the expense and forecast the share count growing at the company's grant run-rate — but never do neither, which is the common default and flatters the per-share number twice. Then add the practical points: compute option dilution at the target price rather than at spot, because higher prices mean the exercise proceeds retire fewer shares; add those proceeds to equity value; and compare buyback volume against grant volume before crediting the company with returning capital, since many buybacks only neutralise dilution. Finish with the qualitative read — the vesting conditions in the ESOP note are the clearest public statement of what management is actually paid to achieve.
