# Instruments & How They Trade

## Why this matters

The single fastest way to blow up as an Indian retail trader is to pick the wrong *instrument* for your edge. A swing trader who has a genuine three-week view but expresses it in weekly options watches theta eat him alive. A scalper who wants tight spreads trades an illiquid midcap future and pays the spread every round trip. A "conservative" investor buys a stock future for leverage and gets a physical-delivery obligation at expiry he can't fund. Your options book taught you *how options are priced*; your TA guide taught you *when* to trade. Neither told you which vehicle — cash, future, option, ETF, currency, commodity — actually matches your holding period, capital, and risk. This chapter is the vehicle selection guide, India-specific, with the mechanics that trip people up: lot sizes, ticks, expiry cycles, and settlement.

## The essentials

**Equity (cash segment).** Buying the share itself.

- **Delivery:** shares hit your demat on **T+1** (2026); you own them, can hold forever, pledge, or collect dividends. STT from 01-Apr-2026 (Budget 2026): **0.1% on buy and sell** (verify on NSE/broker — rules change).
- **Intraday (MIS):** buy and sell same day; broker gives limited leverage per SEBI (no unlimited intraday leverage since 2021). STT **0.025% on the sell side** only. Nothing enters demat.
- Tick size typically ₹0.05; no lot — trade 1 share up.

**Index futures.** One contract = index level × lot size. Cash-settled at expiry, no delivery.

- Monthly expiry (last Thursday-type schedule — **verify current expiry weekday on NSE**, it changed in 2024–25); three serial months live.
- Leverage via SPAN+Exposure margin (upfront, peak-margin enforced).

**Stock futures.** Same idea on single stocks — **but physically settled** at expiry if held: long means you must take delivery and pay full value; short means you must deliver shares. Most traders square off before expiry to avoid this.

**Options (index & stock).** Covered deeply in your options book — here only the *plumbing*: index options cash-settled; STT ~**0.15% on premium (sell side)** and on exercise (2026, verify); weekly and monthly expiries on index, monthly on most stocks. SEBI trimmed weekly expiries to essentially one per exchange in 2024–25 — check the calendar.

**ETFs.** Exchange-traded funds (Niftybees, Bankbees, Goldbees, Liquidbees) trade like shares in the cash segment, settle **T+1** to demat, taxed like equity/other depending on type. Great for delivery exposure without picking single stocks; watch for tracking error and thin spreads on smaller ETFs.

**Currency derivatives.** USDINR, EURINR, GBPINR, JPYINR futures & options on NSE/BSE, 9:00–17:00. Small contract sizes (USDINR future = $1,000). Cash-settled in rupees. CTT does not apply; STT structure differs — verify.

**MCX commodities.** Gold, Silver, Crude Oil, Natural Gas, base metals; trades ~9:00 to ~23:30 tracking global markets. Futures and options. **CTT ~0.01% on sell side** (non-agri futures, 2026, verify). Contracts can be large (a full Gold lot is 1 kg — huge notional); use mini/micro variants.

### Comparison table

| Instrument | Segment | Lot/min size | Settlement | Leverage | Best for |
|---|---|---|---|---|---|
| Equity delivery | Cash | 1 share | T+1 demat | MTF only | Investors, positional |
| Equity intraday (MIS) | Cash | 1 share | Same day, no demat | Broker intraday limit | Day traders |
| Index future | F&O | index × lot | Cash, monthly | SPAN margin | Directional swing/positional |
| Stock future | F&O | stock × lot | **Physical** if held | SPAN margin | Directional; square off pre-expiry |
| Options | F&O | index/stock × lot | Cash (index) | Premium/margin | See options book |
| ETF | Cash | 1 unit | T+1 demat | MTF only | Passive/basket exposure |
| Currency future | Currency | $1,000 (USDINR) | Cash ₹ | High | FX view, hedging |
| MCX commodity | Commodity | varies (Gold 1kg) | Cash/delivery | High | Commodity view |

(All numbers 2026 — verify lot sizes on NSE/BSE/MCX; index lot sizes were revised upward and change periodically.)

## Worked example

You have a bullish 3-week view on a large private bank, ₹1,00,000 capital, willing to risk ₹8,000.

- **Cash delivery:** at ₹1,600/share you buy ~62 shares (₹99,200). No expiry, no theta, you can hold 3 weeks or 3 years. STT 0.1% each side ≈ ₹99 buy + ₹99 sell, plus other charges. Downside: no leverage; a 5% move = ₹5,000.
- **Stock future:** say lot 500 (verify), notional = 500 × 1,600 = **₹8,00,000**; margin maybe ~₹1,20,000 — *more than your capital*. Too big; and if you forget to exit, you face **physical delivery** of ₹8 lakh of shares. Wrong vehicle here.
- **Weekly option:** a 3-week view across a weekly expiry means you cross an expiry and re-enter, paying spread and theta twice; a monthly option is cleaner but that's your options book's domain.

**Verdict:** for this holding period and capital, **cash delivery** (or a monthly call from the options book) fits; the stock future's lot size makes it unsuitable. Matching instrument to view and capital *is* the trade.

## How pros do it / common mistakes

- **Pros size to the lot, not the other way round.** Before falling in love with a stock future, they compute notional = price × lot and margin; if it dwarfs their capital, they drop to cash or options.
- **They never hold stock futures into expiry casually** — physical delivery has burned many retail accounts (forced to fund lakhs, or auction penalties on short delivery).
- **They match holding period to decay:** multi-week view → cash/futures/monthly options, not weeklies.
- **Classic mistakes:** trading illiquid stock F&O with wide spreads; buying tiny ETFs with 1–2% bid-ask; treating MCX Gold's 1 kg lot as "just gold" and taking on ₹70+ lakh notional; ignoring that currency and commodity have their own timings and margins.
- **Red flag:** picking an instrument because "leverage is high" rather than because it fits the view.

## Checklist / drill

- [ ] What's my **holding period** — minutes, days, weeks?
- [ ] **Notional = price × lot** — can my capital carry it?
- [ ] **Settlement:** cash or physical/demat? Any delivery risk at expiry?
- [ ] **Liquidity:** tight spread and real depth in *this* contract?
- [ ] **Costs & tax** for this instrument (STT/CTT differ) — verified for 2026?

**Drill:** take one trade idea and price it three ways — cash, future, option — writing lot size, notional, margin, per-side STT, and expiry for each (verify all on NSE/MCX). Then justify in one sentence why one vehicle wins for your period and capital.
