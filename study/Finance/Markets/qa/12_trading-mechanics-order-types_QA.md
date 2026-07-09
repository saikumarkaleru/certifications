# Q&A — Trading Mechanics and Order Types

Companion practice bank for Chapter 12. Every question is followed by a full answer. Section A checks concepts, B applies them to numbers and situations, C rehearses interview questions with model answers, and D sharpens judgement through MCQs with reasoning.

---

## Section A — Concept Check

**A1. What is the single core idea that modern trading mechanics implements, and why is it needed?**

The core idea is to **replace bilateral trust with a central, anonymous, rule-based intermediary**. Millions of strangers who never meet and cannot verify each other must nevertheless swap securities for cash without either side cheating. So instead of negotiating with a named counterparty, you submit an order to an exchange that matches it anonymously by public rules, and a clearing corporation then guarantees the swap. Everything else — order types, spreads, margin, halts — is machinery that makes this idea work smoothly, fairly, and safely at scale.

**A2. Describe the order book and the two-part rule that governs matching.**

The order book is two sorted lists: the **bid** side (all outstanding buy orders, highest price first) and the **ask/offer** side (all outstanding sell orders, lowest price first). Matching follows **price-time priority**: (1) price priority — the best-priced order executes first (highest bid, lowest ask); (2) time priority — among orders at the same price, the earliest-entered executes first (first-in, first-out). This is what makes anonymous markets fair: you jump the queue only by offering a better price or arriving earlier, never by who you know.

**A3. What is the bid-ask spread and why does it exist?**

The spread is the gap between the best bid and best ask. It exists as the **compensation to whoever provides immediacy** — the market maker or liquidity provider who stands ready to trade the other side of your order. They bear **inventory risk** (the price moving against stock they hold) and **adverse selection** (trading against someone better informed). The spread is their fee and, for you, a real round-trip transaction cost. Its width is a direct gauge of liquidity: thin for Reliance, wide for illiquid small-caps.

**A4. Contrast a market order and a limit order along the fundamental trade-off.**

The trade-off is **execution certainty versus price control** — you cannot maximise both. A **market order** says "fill me now at the best available price," prioritising certainty; it almost always executes instantly but exposes you to slippage and market impact. A **limit order** says "fill me only at price X or better," prioritising price; it may never execute if the market moves away, but if unfilled it rests in the book and provides liquidity.

**A5. Distinguish a stop-loss order from a stop-limit order.**

Both are conditional orders dormant until a **trigger price** is hit. A **stop-loss** then becomes a **market order** — guaranteed to fill but at an uncertain, possibly terrible, price in a gap or crash. A **stop-limit** becomes a **limit order** with a second price you set — it protects you from a bad fill but risks **not executing at all** if the price crashes straight through your limit. Stop-loss trades price for certainty; stop-limit trades certainty for price. Neither is "better"; they encode different fears (bad fill vs no fill).

**A6. What does novation mean, and how does netting reduce settlement flows?**

**Novation** is the legal substitution by which the clearing corporation (CCP) interposes itself, becoming the buyer to every seller and the seller to every buyer, so each side faces only the well-capitalised CCP rather than an unknown counterparty. **Netting** (multilateral) offsets a member's buys and sells in a security so only the net obligation settles — if a broker bought 10,000 and sold 8,000 shares, only 2,000 net move, drastically cutting the money and securities that must change hands.

**A7. What is India's current settlement cycle, and why is a shorter cycle desirable?**

India settles equities on **T+1** (completed across all stocks on 27 January 2023) and launched an optional **T+0** same-day beta from 28 March 2024. Shorter cycles are desirable because the gap between trade and settlement is exactly the window in which **counterparty and market risk** linger and capital sits locked as margin. Faster settlement frees capital and cuts systemic risk — but demands flawless operational plumbing.

**A8. Why is short selling more tightly regulated in India than intraday trading, and what is SLB?**

Because delivery-based (overnight) short selling means you must **deliver shares at T+1 that you do not own**; failure triggers an exchange auction and penalty. So retail delivery shorts are essentially barred unless you borrow shares through **SLB (Securities Lending and Borrowing)** — the mechanism that supplies shares to deliver. **Intraday** short selling is freely allowed because you buy back the same day and never reach settlement. **Naked** shorting (with no ability to deliver) is banned outright.

---

## Section B — Applied / Scenario Questions

**B1. Given the order book below, where does a market buy of 700 shares fill, and what is the average price and total slippage versus the best ask?**

| Bid Qty | Bid ₹ | Ask ₹ | Ask Qty |
|---|---|---|---|
| 500 | 1,250.40 | 1,250.55 | 300 |
| 800 | 1,250.35 | 1,250.60 | 400 |
| 1,500 | 1,250.30 | 1,250.75 | 900 |

A market buy lifts the offers from the top down: **300 at ₹1,250.55**, **400 at ₹1,250.60**, totalling 700 shares. Cost = (300 × 1,250.55) + (400 × 1,250.60) = 3,75,165 + 5,00,240 = ₹8,75,405. Average = ₹1,250.578. Against the best ask of ₹1,250.55, slippage ≈ ₹0.028 per share × 700 ≈ **₹19.60**. Your order "walked up the book," consuming depth beyond the top level — this is market impact in hard numbers.

**B2. Same book. You place a limit buy for 700 shares at ₹1,250.55. What happens?**

Only the resting quantity at ₹1,250.55 or better trades. There are just **300 shares** at ₹1,250.55 and nothing cheaper on offer, so you fill 300 at ₹1,250.55; the remaining **400 shares rest in the book** as the new best bid at ₹1,250.55 (above the old best bid of ₹1,250.40). You protected your price — no share cost more than ₹1,250.55 — but sacrificed certainty: 400 shares are unfilled and may stay that way if the market rises away from you.

**B3. You buy Adani Ports at ₹1,400 and set a stop-loss trigger at ₹1,350. Overnight bad news gaps the stock to open at ₹1,300. What fills, and how would a stop-limit at trigger ₹1,350 / limit ₹1,345 have behaved differently?**

The plain stop-loss becomes a **market order** once ₹1,350 is touched (or gapped through) and fills near **₹1,300**, well below your trigger, because there were no buyers at ₹1,350 — you lose ₹100/share, not the ₹50 you imagined. The **stop-limit** would trigger but place a limit at ₹1,345; with the stock already at ₹1,300 and no buyers at ₹1,345, it **would not execute at all**, leaving you still holding a falling stock. The gap exposes the true nature of each: stop-loss guarantees exit but not price; stop-limit guarantees price but not exit.

**B4. You post ₹1,20,000 margin for one Nifty futures lot worth ₹18,00,000. Nifty falls 2%. What is your loss in rupees and as a percentage of margin, and what may the broker do?**

Contract loss = 2% × ₹18,00,000 = **₹36,000**. As a fraction of your ₹1,20,000 margin that is **−30%** — the 15× leverage (18,00,000 ÷ 1,20,000) multiplied the market's 2% move into a 30% hit on your capital. As margin erodes you receive a **margin call** to top up; if you fail, the broker **squares off** (force-closes) the position and you remain liable for any shortfall. Leverage did not change the market's 2% move; it changed your exposure to it by 15×, symmetrically for gains and losses.

**B5. A stock's spread is ₹0.10 on a ₹1,250 price; a small-cap's spread is ₹3.00 on a ₹200 price. Compare the round-trip cost of immediacy as a percentage.**

Crossing the spread costs roughly the full spread per round trip. Large-cap: ₹0.10 ÷ ₹1,250 = **0.008%** (0.8 bps). Small-cap: ₹3.00 ÷ ₹200 = **1.5%** (150 bps) — nearly **190× more**, before any brokerage or taxes. This is why liquidity is a feature you pay for, and why illiquid names quietly erode active-trading returns.

**B6. On the pre-open session, orders collect from 09:00 to 09:15 but are not continuously matched. What is discovered, how, and why is this better than a continuous open?**

A single **equilibrium (opening) price** is discovered via a **call auction** that selects the price maximising executable volume across all collected orders. It beats a continuous open because it aggregates overnight information into one fair clearing price instead of letting the first fast orders whipsaw the market — **dampening opening volatility** and reducing the advantage of pure speed at the bell.

**B7. A broker's client bought 10,000 and sold 8,000 shares of the same stock during the day. How much settles, and what two CCP functions made that possible?**

Only the **net 2,000 shares** settle (a net buy). This is enabled by **novation** (the CCP becomes counterparty to both the buys and the sells, so they can be legally offset against one entity) and **multilateral netting** (aggregating the member's opposing positions into a single net obligation). Depositories NSDL/CDSL then effect the demat debit/credit for the net amount. Netting slashes the volume of cash and securities that must physically move, cutting operational and settlement risk.

**B8. At 11:00 am the Nifty falls 15% from the previous close. Using India's market-wide circuit breaker matrix, what happens?**

A 15% move before 1:00 pm triggers a **1-hour-45-minute halt** across NSE and BSE. Trading then resumes with a **15-minute pre-open call auction** to re-establish a fair price. (Had the same 15% occurred after 2:30 pm, the market would halt for the **rest of the day**; a 20% move at any time halts the whole remaining day.) The halt trades a small loss of continuous trading for a large gain in stability, breaking the panic feedback loop.

---

## Section C — Interview-Style Questions (with model answers)

**C1. "Walk me through what actually happens between clicking 'buy' and the shares appearing in your account."**

*Model answer:* Seven steps. (1) **Origination** — I place a buy order in the broker app, choosing an order type and, for intraday/derivatives, meeting the margin requirement. (2) **Risk check and routing** — the broker's RMS verifies funds and position limits, then routes to NSE/BSE over a low-latency link. (3) **Order book** — the exchange's matching engine places my order in the limit order book. (4) **Matching** — using price-time priority it pairs my buy with the best resting sells; a trade executes in milliseconds and price discovery has happened. (5) **Clearing** — details flow to the clearing corporation, which novates (becomes counterparty to both sides) and nets obligations. (6) **Settlement** — on T+1, pay-in and pay-out run: my cash is debited to the seller, the seller's shares move from their demat to mine at NSDL/CDSL. (7) **Post-settlement** — shares sit in my demat and the contract note, STT, stamp duty and GST on brokerage are generated. The whole design exists to let anonymous strangers trade without trusting each other.

**C2. "When would you use a market order over a limit order, and what are the hidden costs of each?"**

*Model answer:* I use a **market order** when certainty of execution dominates — a liquid stock where I need to be in or out immediately, or when closing a position in a fast market. Its hidden costs are **slippage** (the fill is worse than the price I saw) and **market impact** (a large order walks up the book and moves the price against me). I use a **limit order** when price control matters more than speed, or when I want to provide liquidity and rest in the book. Its hidden cost is **opportunity cost / non-execution** — in a market moving away from me I may never get filled and miss the trade entirely. The one-line framing: market orders pay in price uncertainty, limit orders pay in fill uncertainty.

**C3. "Why did India move to T+1, and is faster settlement strictly better?"**

*Model answer:* India moved from T+2 to **T+1** (fully by 27 January 2023) and even piloted **T+0** from March 2024, ahead of the US which reached T+1 only in May 2024. The rationale: the settlement gap is the window in which counterparty and market risk persist and capital sits idle as margin — shortening it frees capital and cuts systemic risk. But it is not *costlessly* better: it demands near-instant fund transfers, pre-funded accounts and flawless operational plumbing, which raises the bar for brokers and can strain participants who relied on the float. So the direction is clearly right, but the constraint is operational readiness, which is why T+0 is being rolled out gradually rather than mandated overnight.

**C4. "Explain how leverage and short selling import risk, and how regulators cage it."**

*Model answer:* **Leverage** lets me control a position far larger than my capital by posting only a fraction as margin — magnifying both gains and losses and adding margin-call and forced-liquidation risk a cash position never faces. **Short selling** — selling borrowed shares to profit from a fall — carries **theoretically unlimited loss** (a price can rise without bound) plus the duty to deliver shares I do not own. Regulators cage these: SEBI's **peak/upfront margin** rules (phased 2020–21) ended extreme intraday leverage by forcing pre-collection of VaR+ELM margin; **SLB** channels delivery shorts through proper borrowing; **naked shorting is banned**; institutions must declare shorts upfront. The US analogue is Regulation SHO ("locate" requirement plus the Rule 201 uptick rule). The common thread: every rule defends against a specific default or blow-up.

**C5. "What are circuit breakers, and do they actually help?"**

*Model answer:* Circuit breakers are **automatic trading halts** triggered by extreme price moves — in India on the Nifty/Sensex at 10%, 15% and 20%, with duration depending on level and time of day, the 20% level halting the whole day; individual stocks have price bands. The philosophy is to trade a small loss of continuous trading for a large gain in stability: a halt interrupts self-reinforcing panic, lets information disseminate, and catches fat-finger or algorithmic cascades — as on 13 March 2020 when a 10% Nifty crash triggered a 45-minute halt and the market stabilised. Critics note a possible "magnet effect" (traders rushing to exit before a breaker), but for genuine disorderly panics the cooling-off benefit outweighs the interruption. Crucially, breakers protect market *integrity*, not any individual's position.

---

## Section D — Multiple-Choice Questions (with reasoning)

**D1. Under price-time priority, which order executes first?**
(a) The largest-quantity order
(b) The order from the most senior member
(c) The best-priced order, then the earliest among equal prices
(d) The most recently entered order

**Answer: (c).** Price priority comes first (highest bid / lowest ask), then time priority (first-in, first-out) among orders at the same price. Quantity and member identity are irrelevant — that irrelevance is precisely what makes anonymous matching fair.

**D2. A market buy order executes against which side of the book, and at what price?**
(a) The bid, at the best bid price
(b) The ask, at the best ask price
(c) The bid, at the last traded price
(d) The ask, at the previous close

**Answer: (b).** A market buy "lifts the offer," executing against resting sell orders starting at the best ask. (A market *sell* hits the bid.) The last traded price and previous close do not determine the fill — you transact against live resting liquidity.

**D3. Which statement about a plain stop-loss order is correct?**
(a) It guarantees your fill will be at or better than the trigger price
(b) On trigger it becomes a limit order
(c) On trigger it becomes a market order and can fill well below the trigger in a gap
(d) It executes continuously as the price falls

**Answer: (c).** A stop-loss converts to a *market* order once triggered, so the fill price is uncertain — in a gap or crash it can be far below the trigger. Only a stop-*limit* caps the fill price (option a/b describe that instead), and even then at the risk of no execution.

**D4. The bid-ask spread is best described as:**
(a) A tax collected by the exchange
(b) Compensation to liquidity providers for immediacy, inventory and adverse-selection risk
(c) The difference between par value and market value
(d) A regulatory fee under SEBI rules

**Answer: (b).** The spread is the market maker's earnings for standing ready to trade and bearing inventory and adverse-selection risk. It is a market-determined transaction cost, not a tax or regulatory levy, and has nothing to do with par value.

**D5. India completed its move to T+1 equity settlement in:**
(a) January 2023
(b) May 2024
(c) March 2020
(d) January 2021

**Answer: (a).** The phased T+1 rollout finished on 27 January 2023. May 2024 is when the *US* reached T+1; March 2020 is the COVID circuit-breaker date; T+2 was the norm until 2021. India then launched optional T+0 from 28 March 2024.

**D6. Novation by the clearing corporation primarily achieves:**
(a) Faster order matching
(b) Elimination of the bid-ask spread
(c) Removal of counterparty default risk by interposing the CCP as counterparty to both sides
(d) Tax efficiency for investors

**Answer: (c).** Novation legally substitutes the CCP as buyer to every seller and seller to every buyer, so each participant faces only the well-capitalised clearing corporation. It does not affect matching speed, the spread, or taxes.

**D7. In India, which form of short selling is freely permitted for retail traders?**
(a) Naked short selling
(b) Delivery-based overnight short selling without borrowing
(c) Intraday short selling squared off the same day
(d) None; short selling is banned

**Answer: (c).** Intraday shorting is fully allowed because you buy back before settlement and never fail to deliver. Naked shorting is banned; retail delivery shorts require SLB borrowing; the blanket "banned" claim is a common misconception.

**D8. India's market-wide circuit breakers are triggered at index moves of:**
(a) 7%, 13%, 20%
(b) 10%, 15%, 20%
(c) 5%, 10%, 15%
(d) 2%, 5%, 10%

**Answer: (b).** India uses 10/15/20% on the Nifty 50 or Sensex, with halt duration depending on level and time of day. Option (a) is the *US* S&P 500 thresholds; the smaller percentages are individual-stock price bands, not market-wide breakers.

**D9. A market buy of 1,000 shares fills 500 at ₹975.20 and 500 at ₹975.40, when the best ask was ₹975.20. The ₹0.10 average shortfall is called:**
(a) Brokerage
(b) Slippage / market impact
(c) The bid-ask spread
(d) Stamp duty

**Answer: (b).** The order walked up the book, consuming depth beyond the top level; the gap between the expected best-ask fill and the actual volume-weighted average is slippage plus market impact — a cost your own order size created, distinct from brokerage, the spread, or statutory levies.

**D10. SEBI's peak/upfront margin rules (phased 2020–21) primarily aimed to:**
(a) Increase intraday leverage available to retail traders
(b) Curb reckless intraday leverage by mandating upfront margin collection
(c) Abolish the T+1 settlement cycle
(d) Ban derivatives trading

**Answer: (b).** The rules ended the era of 20–40× advertised intraday exposure by requiring brokers to pre-collect at least VaR+ELM (peak) margin, reducing systemic and client blow-up risk. They increased, not decreased, the margin required — the opposite of (a) — and had nothing to do with settlement cycles or banning derivatives.

---

*End of practice bank. Re-attempt Section D from memory after a day; if you can also reproduce the seven-step trade lifecycle (C1) and the execution-versus-price trade-off (A4, C2) unprompted, the chapter is secure.*

