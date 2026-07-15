# Commodity Trading on MCX

## Why this matters

MCX is where Indian traders get access to gold, silver, crude oil, natural gas, and base metals — the assets that actually drive inflation, the rupee, and half the stock market's sector moves. Retail traders wander in chasing crude oil's famous intraday swings, discover the contracts run till **11:30 pm / 11:55 pm**, get caught in an overnight Comex gap or an EIA inventory spike, and blow up. The pro understands three things the newcomer doesn't: MCX prices are **imported** (they track Comex/Brent/LME converted through USDINR, not some independent Indian view), each commodity has its own **seasonality and event calendar**, and the leverage plus long hours make position-sizing and *when you're at the screen* matter more than direction. This chapter is the India-specific commodity mechanics the options and TA books skip.

## The essentials

*(Specs as of Jul 2026 — MCX revises lot sizes and launches "mini" contracts periodically; **verify current specs on mcxindia.com** before trading. Rules change.)*

| Commodity | Contract | Lot / unit | ₹ per ₹1 tick move (approx) | Global linkage |
|---|---|---|---|---|
| **Gold** | Gold (1 kg) | 1 kg → **₹100/point per 10g quote... per ₹1 = ₹100 (per 10g)** | ₹100 per ₹1 (per 10g) | Comex gold, USD, USDINR |
| **Gold Mini** | 100 g | 100 g | ₹10 per ₹1 | Comex gold |
| **Silver** | Silver (30 kg) | 30 kg | ₹30 per ₹1 (per kg) | Comex silver |
| **Silver Mini** | 5 kg | 5 kg | ₹5 per ₹1 | Comex silver |
| **Crude Oil** | 100 barrels | 100 bbl | **₹100 per ₹1** | Nymex WTI / Brent |
| **Crude Mini** | 10 barrels | 10 bbl | ₹10 per ₹1 | WTI |
| **Natural Gas** | 1,250 mmBtu | 1,250 | **₹1,250 per ₹1** | Nymex Henry Hub |
| **Copper** | 2,500 kg | 2,500 | ₹2,500 per ₹1 | LME copper |

**Key India-specific facts:**
- **Timings:** MCX trades **9:00 am – 11:30 pm** (11:55 pm on US daylight-saving evenings). The big moves come *after* the equity close, on Comex/Nymex cues and US data (EIA crude/gas inventories Wed/Thu night). If you can't watch the evening session, don't hold naked overnight.
- **Settlement:** most are **cash-settled**, but some (like the 1kg gold, base metals) have moved to **physical/compulsory delivery** near expiry — **check whether your contract is deliverable and exit before the delivery/tender period** to avoid delivery obligations and warehouse costs.
- **Margins:** SPAN + Exposure, upfront, peak-margin enforced. Crude and natural gas carry the **highest margins** (they're the most volatile — nat gas can move 5-10% in a session).
- **CTT (Commodities Transaction Tax):** ~**0.01% on the sell side** of non-agri commodity futures (per current schedule; verify — the 2026 Budget schedule applies from 01-Apr-2026). Agri commodities are CTT-exempt.
- **Prices are imported.** MCX gold ≈ Comex gold (USD/oz) × conversion × USDINR + duties. So an MCX gold trade is *implicitly* also a USDINR trade — a falling rupee can lift MCX gold even when Comex is flat.

**Drivers & seasonality:**
- **Gold/Silver:** US real yields, DXY, Fed policy, risk-off/geopolitics, and the rupee. Indian festive/wedding demand (Oct-Dec, Akshaya Tritiya) adds a domestic bid.
- **Crude:** OPEC+ decisions, US inventories (EIA Wednesday night), geopolitics, demand data. Notoriously event-driven and gappy.
- **Natural gas:** *the* seasonal contract — winter heating demand and hurricane-season supply scares make it the most volatile MCX product. Treat with respect.
- **Base metals (copper/zinc/lead):** China demand and LME, global growth cycle.

## Worked example — an MCX crude oil trade

*(Illustrative.)* It's an EIA-inventory Wednesday. Draws (falling stockpiles) plus an OPEC+ supply-cut headline point higher. You go **long 1 lot MCX Crude Oil** (100 barrels).

- Entry **₹6,500** per barrel (MCX quotes in ₹/bbl). Notional = 6,500 × 100 = **₹6,50,000**.
- Margin ~**₹65,000-80,000** (crude carries high margin).
- 9:00 pm: EIA prints a large draw; WTI jumps ~2%. MCX crude → **₹6,630** (+₹130).
- P&L = 130 × 100 = **+₹13,000** on ~₹75,000 margin ≈ **+17%** in one evening.

But the mirror risk: had inventories *built*, a ₹130 fall = **−₹13,000**, and a violent whipsaw around the 8:30 pm release could hit both your stop and its reversal. **This is why crude is a screen-time trade, not a set-and-forget.**

## Worked example — a gold trade (with the hidden FX leg)

You expect a Fed rate cut → gold up. Buy **1 lot Gold Mini (100g) @ ₹72,000** (per 10g quote). Notional ≈ 72,000 × 10 = **₹7,20,000**; ₹1 move (per 10g) = ₹10/lot.

- Comex gold rises 1.5% *and* the rupee weakens 0.4% → MCX gold rises ~1.9% to **₹73,370** (+₹1,370).
- P&L = 1,370 × 10 = **+₹13,700**. Note the extra 0.4% came *purely from USDINR* — proof that MCX gold is a gold-plus-rupee trade. If the rupee had *strengthened*, part of your Comex gain would have vanished.

**Costs:** brokerage + exchange txn + **CTT ~0.01% on sell** + **18% GST** + stamp. On a ₹7L gold lot, CTT on exit ≈ ₹72; all-in round-trip typically **₹100-200** — modest vs notional.

## How pros do it / common mistakes

**Pros:**
- **Trade the global anchor.** They watch Comex/Brent/LME and DXY live — MCX is the *follower*. Trading MCX in isolation is trading yesterday's news.
- **Separate the two legs on gold/silver:** is the move metal (Comex) or rupee (USDINR)? It changes the exit.
- **Respect the evening event calendar:** EIA (Wed night crude, Thu night gas), OPEC+ meetings, Fed decisions, US jobs data. They flatten or size down into these.
- **Size for the highest-vol product's worst day** — nat gas and crude can gap through stops overnight; use smaller lots or the **mini contracts** to control risk.
- **Exit before the delivery/tender window** on deliverable contracts.

**Classic retail errors:**
- Holding crude/nat gas naked overnight and eating a Comex gap they never saw.
- Treating MCX gold as independent of the rupee.
- Over-leveraging the tiny-looking tick value on nat gas (₹1,250 per ₹1!) — a ₹10 move is ₹12,500 per lot.
- Ignoring the **physical-delivery** shift near expiry on gold/metals.
- Trading during the illiquid early-morning session instead of the liquid evening overlap with US markets.

## Checklist / drill

Before an MCX trade:
- [ ] Checked the **global anchor** (Comex/Brent/LME) and **DXY** direction right now.
- [ ] For gold/silver: identified whether the driver is **metal or rupee**.
- [ ] Confirmed **current lot size and ₹-per-tick** (used a **mini** contract if sizing down).
- [ ] Checked the **evening event calendar** (EIA, OPEC+, Fed, jobs) — am I holding into a release?
- [ ] Confirmed I'll be **at the screen for the volatile evening session** if holding.
- [ ] Verified the contract's **cash vs physical settlement** and the delivery/tender date.
- [ ] Sized for the product's **worst realistic day**, not its average.

**Drill:** For two weeks, each evening log MCX crude/gold, its Comex/WTI reference, USDINR, and any scheduled data. Predict the next session's MCX open from the overnight global move and score yourself. You'll internalise that MCX is an *imported* price — the single most important mental model for trading it well.
