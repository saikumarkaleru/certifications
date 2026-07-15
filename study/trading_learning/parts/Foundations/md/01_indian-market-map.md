# The Indian Market Map: NSE, BSE, SEBI, Segments & Indices

## Why this matters

Retail traders often "know" Nifty and Bank Nifty but have never mentally drawn the *map* — who runs the exchange, who regulates it, where their money actually settles, and which segment their trade lives in. That gap shows up in real losses: placing an equity intraday order thinking it's F&O, holding a stock future into expiry not knowing it's cash-settled or physically delivered, or being surprised that a "market" is shut when MCX is still open at 9 PM. A professional treats the market as a single connected machine — order routing, clearing, depository, regulator — and knows exactly which gear turns when. This chapter draws that machine so every later chapter (instruments, orders, costs, tax) snaps into place.

## The essentials

**The two big exchanges.** India has two national stock exchanges:

- **NSE (National Stock Exchange)** — dominant in derivatives; Nifty 50 is its flagship. The vast majority of F&O volume is NSE.
- **BSE (Bombay Stock Exchange)** — Asia's oldest (1875); Sensex is its flagship. BSE has clawed back real derivatives volume since ~2023 via Sensex and Bankex weekly options.

Both are electronic, order-driven (no floor). You can buy a stock on NSE and sell the same ISIN on BSE — shares are fungible because they sit in the same demat account.

**The regulator: SEBI.** The Securities and Exchange Board of India is the statutory regulator (SEBI Act, 1992). It licenses brokers, sets margin and disclosure rules, runs investor protection, and enforces the algo framework. When this book says "rules change — verify on SEBI," this is who changes them.

**Clearing & depositories.** Your trade doesn't end at the match:

- **Clearing corporations** (NSE Clearing / NSCCL, and Indian Clearing Corp for BSE) become the central counterparty and guarantee settlement.
- **Depositories NSDL and CDSL** hold your shares electronically. Your broker opens a **demat** account mapped to one of them. Delivery shares move here on settlement.

**Settlement cycle (as of 2026 — verify on NSE, rules change).** Equity cash is **T+1 rolling** — buy today, shares/cash settle next working day. A **T+0** (same-day) optional settlement is in beta rollout for a select list of stocks; it runs alongside, not instead of, T+1.

**Segments.** One trading account, several segments you must be enabled for:

| Segment | What trades | Where | Typical hours (IST) |
|---|---|---|---|
| Equity cash | Shares (delivery/intraday) | NSE/BSE | 9:15–15:30 |
| Equity F&O | Index & stock futures/options | NSE/BSE | 9:15–15:30 |
| Currency derivatives | USDINR, EURINR etc. futures/options | NSE/BSE | 9:00–17:00 |
| Commodity | Gold, silver, crude, natgas etc. | MCX (NCDEX agri) | 9:00–23:30 (approx) |

**Trading day structure (equity, IST):**

- **Pre-open 9:00–9:15** — 9:00–9:08 order entry, 9:08–9:12 call-auction price discovery, then a buffer to 9:15. This sets the opening price (important on gap days).
- **Continuous 9:15–15:30** — normal price-time matching.
- **Post-close 15:40–16:00** — orders at the closing price (thin, mostly ignored by traders).

**Key indices you'll actually trade or watch:**

| Index | What it is | Note |
|---|---|---|
| **Nifty 50** | 50 large NSE stocks, free-float weighted | The India benchmark |
| **Bank Nifty** | 12 major banks | Most-traded, high-beta, volatile |
| **Fin Nifty** (Nifty Financial Services) | Banks + NBFCs + insurance | Broader financials |
| **Nifty Midcap Select** | Midcap basket | F&O available |
| **Sensex** | 30 BSE blue-chips | BSE benchmark, weekly options |
| **Bankex** | BSE banking index | BSE derivative |
| **Sectorals** | Nifty IT, Auto, Pharma, FMCG, Metal, Energy | Rotation & relative strength |

(Verify current weekly-expiry structure on NSE/BSE — SEBI trimmed the number of weekly expiries per exchange, so which index expires which weekday changes; check the exchange calendar.)

## Worked example

You want to trade a Bank Nifty view on a Tuesday. Mentally trace the machine:

1. **Segment:** Equity F&O on NSE. Your account must be F&O-enabled (income proof was required at activation).
2. **Instrument:** Say Bank Nifty weekly option (verify current lot size on NSE — index lot sizes were revised upward in 2024–25; do not assume 15 or 25). Suppose the lot is 35 and you buy 1 lot of the 52,000 CE at ₹300. Contract premium value = 300 × 35 = **₹10,500** plus charges.
3. **Match:** Your limit order hits NSE's order book; NSE Clearing becomes counterparty — you never face the seller directly.
4. **Money:** Upfront SPAN+Exposure margin was blocked when you *sold* options; as a buyer you pay full premium upfront. Funds move via your broker to the clearing corp.
5. **Settlement:** Index options are **cash-settled** — no shares, no demat delivery. On expiry you get intrinsic value in cash; NSDL/CDSL never touch it.

Contrast: buy 10 shares of a stock for delivery — now CDSL/NSDL *do* get involved, shares land in demat on **T+1**, and you can pledge or sell them thereafter.

## How pros do it / common mistakes

- **Pros know the segment before the trade.** They never confuse "I'm long the index" (F&O, cash-settled) with "I own bank shares" (cash, demat, T+1).
- **They respect the pre-open.** On event/gap mornings the 9:00–9:08 window sets the open; retail traders who fire a market order at 9:15:00 often get a terrible fill into the opening imbalance.
- **They check the expiry calendar weekly.** Weekly-expiry weekdays shifted after SEBI's 2024–25 rationalisation; trading "Thursday expiry" out of habit is now a real error.
- **Classic mistakes:** assuming all commodities close at 3:30 (MCX runs into the night); thinking NSE and BSE prices must be identical (small arbitrage gaps exist); forgetting stock futures can go to **physical delivery** at expiry if held.
- **Red flag:** any "exchange" or app not routing through NSE/BSE/MCX with SEBI-registered brokers — that's a dabba/illegal operator.

## Checklist / drill

Before any trade, answer these in five seconds:

- [ ] Which **exchange** — NSE / BSE / MCX?
- [ ] Which **segment** — cash / F&O / currency / commodity?
- [ ] **Cash-settled or delivery?** If delivery, is my demat ready and do I want T+1?
- [ ] Is the market **open** for this segment right now (equity 9:15–15:30; MCX late)?
- [ ] For F&O: correct **lot size** and **expiry weekday** verified on the exchange today?

**Drill:** open Kite (or your terminal), and for Nifty 50, Bank Nifty, one stock future, USDINR, and MCX Gold, write down the exchange, segment, settlement type, and current lot size. Verify every number on the NSE/BSE/MCX site — do not trust memory. Rules and lot sizes change; date-stamp your notes (today: 2026).
