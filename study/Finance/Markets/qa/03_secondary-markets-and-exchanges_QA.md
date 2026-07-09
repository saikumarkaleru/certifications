# Q&A — Secondary Markets and Stock Exchanges

A companion practice bank for Chapter 03. Every question is followed by a full answer. Attempt your own answer first, then compare.

---

## Section A — Concept Check (test your understanding)

**A1. In one sentence, what does the secondary market do that the primary market does not?**

It lets already-issued securities change hands between investors again and again for the life of the security, whereas the primary market sells newly issued securities from the company to raise fresh capital. No new money reaches the issuer in a secondary trade.

**A2. Why does the primary market depend on the secondary market even though the latter raises no capital for companies?**

Investors fund an IPO only if confident they can exit later at a fair price, and that confidence comes entirely from a liquid secondary market. Downstream liquidity is the precondition for upstream fundraising — remove it and IPO demand collapses because every investment becomes a permanent trap.

**A3. Name the two great public goods an exchange produces.**

Liquidity — converting a security to cash quickly, in size, without moving the price much. Price discovery — continuous aggregation of all participants' information into a single, transparent last-traded price.

**A4. Distinguish an order-driven market from a quote-driven market.**

Order-driven (NSE, BSE cash): prices emerge from all participants' buy and sell orders in a central book, matched directly; anyone can supply liquidity. Quote-driven (dealer): market makers post two-way bid/ask quotes and you trade against the dealer, who earns the spread and guarantees a counterparty. Corporate bonds and the old Nasdaq were quote-driven.

**A5. State the price-time priority rule and why it is fair.**

Better-priced orders execute first; among orders at the same price, the earliest-entered executes first. It is fair because the only way to jump the queue is to offer a genuinely better price — you cannot cut in line through privilege.

**A6. As a trader, which price do you buy at — the bid or the ask?**

You buy at the ask and sell at the bid. The bid is where someone is willing to buy from you; the ask is the lowest price at which someone will sell to you. Crossing the spread — hitting the ask — is what a buy market order does.

**A7. What is novation, and which institution performs it?**

Novation is the legal splitting of a single matched trade between two strangers into two trades, each facing the clearing corporation (the CCP). After it, you no longer bear the risk that the stranger defaults — the CCP guarantees your side. In India, NSE Clearing (NCL) and ICCL do this.

**A8. Clearing and settlement are two different steps — define each.**

Clearing computes who owes what — netting each member's obligations, novation, and margin collection. Settlement is the actual exchange of shares and cash on settlement day (pay-in, pay-out). Clearing figures out obligations; settlement discharges them.

**A9. What does "T+1" mean, and what has India done recently on settlement speed?**

T+1 means settlement completes one business day after the trade date (T). India completed the move from T+2 to T+1 by January 2023 and began rolling out an optional same-day T+0 cycle from 2024, making it among the fastest-settling major markets. The US moved to T+1 in May 2024.

**A10. Name the four market-infrastructure layers a retail order passes through, in order, with one job of each.**

Broker/trading member (validates and routes the order, since only members access the exchange); stock exchange (matching engine pairs best buy with best sell); clearing corporation (novation, netting, margining, settlement guarantee); depository — NSDL/CDSL (moves shares between demat accounts). A clearing bank handles the cash leg.

**A11. Differentiate a market order from a limit order, with the trade-off of each.**

A market order executes immediately at the best available price — guaranteed fill, uncertain price (slippage). A limit order executes only at a specified price or better — price certainty, no guaranteed fill. Market orders take liquidity; limit orders provide it.

**A12. Difference between the cash segment and the derivatives (F&O) segment?**

Cash: you buy the actual share, becoming a part-owner with dividends and votes, settled on delivery at T+1. Derivatives: you trade a contract whose value is derived from an underlying — no ownership, no dividends/votes, fixed expiry, and you post only margin (leverage). Derivatives exist for hedging, speculation, and arbitrage.

**A13. Why is liquidity said to be "priced" into every asset?**

Because investors know an illiquid security is costly to exit (large market impact), they demand a lower price / higher expected return to hold it — the illiquidity premium. A blue chip with tight spreads trades richer than an otherwise identical thinly traded SME stock precisely because you can get out cheaply.

---

## Section B — Applied / Scenario Questions

**B1. Infosys order book — bids: 300 @ ₹1,499.50, 500 @ ₹1,499.00; asks: 200 @ ₹1,500.00, 400 @ ₹1,500.50. (a) Spread and signal? (b) A market buy for 500 shares fills how? (c) Where does a limit buy at ₹1,499.00 go?**

(a) Spread = ₹0.50, about 0.03% of price — very tight, signalling a highly liquid stock. (b) It takes all 200 at ₹1,500.00, then 300 at ₹1,500.50, averaging ~₹1,500.30; the order "walked up the book," and the extra cost versus the touch price is slippage. (c) A limit buy at ₹1,499.00 does not execute (below the best ask); it joins the bid queue behind the ₹1,499.50 order and waits, since ₹1,499.50 has price priority.

**B2. An investor holds ₹50 lakh in a NIFTY-tracking portfolio, fears a pre-Budget dip, but won't sell. What can she do, how much capital, and who takes the other side?**

She shorts NIFTY futures worth ~₹50 lakh. If NIFTY falls 5%, her cash portfolio loses ~₹2.5 lakh but the short future gains ~₹2.5 lakh — roughly flat, i.e. hedged. Being margin-based, it ties up only ~₹6 lakh, and avoids the tax and re-entry cost of selling. The counterparty may be a speculator betting NIFTY rises; the market transfers her downside risk to someone willing to bear it — the economic purpose of derivatives.

**B3. For a moment Apple prints $190.00 on one venue while its futures-implied fair value is $190.10. What happens, who does it, and what principle is at work?**

Arbitrageurs (usually HFT algos) instantly buy at $190.00 and sell the equivalent at $190.10, capturing the gap. Their buying lifts the low price and selling depresses the high price until the gap closes, usually within milliseconds. No one coordinates it — the profit motive alone enforces consistency (the law of one price), which is why co-location and ultra-low latency matter.

**B4. You want to buy ₹10 lakh of a thinly traded SME stock (spread several percent, a few thousand shares a day). What execution problem do you face versus ₹10 lakh of Reliance?**

In Reliance, ₹10 lakh is trivial — deep book, ₹0.05 spread, near-zero impact. In the SME stock the thin book means your order walks far up the offers and could move price 5–10%; exiting is equally punishing. You face large slippage because depth is missing — which is why the SME stock must offer a higher expected return (illiquidity premium).

**B5. A seller fails to deliver shares on settlement day. What protects the buyer and what happens to the defaulter?**

Because of novation the buyer's counterparty is the clearing corporation, not the failed seller, so the buyer is insulated. The clearing corp triggers an auction (close-out): it buys the missing shares to deliver to the buyer, making him whole, and charges the auction cost plus penalties to the defaulter. Margins collected between trade and settlement (VaR, ELM, mark-to-market) exist precisely to cover such shortfalls.

**B6. A founder says, "Every time our stock trades, our company gets cash." Correct her and name the situation where the company does receive cash.**

Wrong for ordinary secondary trading: cash flows from the buying investor to the selling investor — the company is not a party and receives nothing. It receives cash only in the primary market: IPO, FPO, rights issue, QIP, or preferential allotment, where new shares are sold by the company. Price moves affect its market value and future fundraising ability, but no cash reaches the firm.

**B7. Two companies both "went public." One says it "did an IPO," the other "got listed." Same event?**

Related but distinct. The IPO is the sale of shares to raise capital (primary market). Listing is admission of the securities to trading on an exchange (enabling secondary trading). They usually coincide, but a company can list without a fresh issue (a direct listing) or be listed on more than one exchange. Confusing the two is a classic trap.

**B8. A trader placed a stop-loss and was "stopped out" during a momentary spike, then price recovered. Explain the mechanism and the trade-off.**

A stop-loss becomes a live market (or limit) order the instant the trigger is touched. A brief, thin-liquidity spike can touch the trigger, convert the order, and execute at a poor price even though price recovers seconds later. The trade-off: stop-losses cap downside and remove the need to watch the screen, but can trigger on transient noise and, as market orders, fill with slippage in a fast market.

**B9. Why do large institutions slice a big order into iceberg pieces or use algorithms instead of one giant market order?**

A single large market order walks up (or down) the book, revealing size and causing severe slippage; others see the demand and front-run or pull quotes. Slicing — showing only a small disclosed quantity, or spreading execution over time via algos — hides true size, reduces market impact, and achieves a better average price. It is the B1 order-book logic (depth, walking the book) being managed.

**B10. India's regulator tightened F&O rules in 2024 (fewer weekly expiries, larger lot sizes). What problem, and how does the change help?**

Explosive retail participation in index options had produced large aggregate losses, with weekly expiries encouraging lottery-like speculation. By cutting weekly expiries and raising lot sizes, SEBI raised the cost and capital needed to speculate, curbing hyperactive small-ticket punting while keeping derivatives available for genuine hedging — investor protection without killing the risk-transfer function.

---

## Section C — Interview-Style Questions (with model answers)

**C1. "Walk me through what happens from the moment I tap 'Buy' on my phone to when I actually own the share."**

Your order goes to your broker, who validates funds/limits and routes it to the exchange. The matching engine pairs it with the best sell order by price-time priority — that is execution. The clearing corporation then performs novation and nets each member's obligations. On settlement day (T+1) the depository (NSDL/CDSL) moves shares into your demat account while the clearing bank moves cash to the seller. You gain economic exposure at T; legal delivery completes at T+1.

**C2. "Order-driven or quote-driven — which is better?"**

Neither universally; it depends on the instrument. Order-driven markets excel for liquid, high-volume equities: full order-book transparency, tight spreads, liquidity from all participants. Quote-driven markets suit illiquid or complex instruments — corporate bonds, many forex pairs — where a natural counterparty may be absent, so a dealer's obligation to quote both sides guarantees you can trade, at the cost of a wider spread. Most large venues are hybrids: NYSE pairs an electronic book with Designated Market Makers; modern Nasdaq overlays competing market makers on a central book.

**C3. "Why does a clearing corporation exist? Couldn't buyers and sellers just settle directly?"**

Direct bilateral settlement forces every participant to bear the default risk of every anonymous counterparty — unworkable across millions of trades. The clearing corporation inserts itself as central counterparty via novation, so each side faces only the highly capitalised, margin-protected CCP. It also nets multilaterally, so a member settles one net figure per security instead of thousands of gross trades. Margins and a guarantee fund backstop it. In short, it converts a web of counterparty risk into trust in one robust institution.

**C4. "What is the difference between liquidity and volume? Why does the distinction matter?"**

Volume is how many shares traded; liquidity is the ability to trade size quickly without moving the price, depending on depth (orders at nearby prices), tight spreads, and resilience (how fast the book refills). A stock can post high turnover yet be shallow, so a moderate order still moves it sharply. It matters because you cannot judge exit cost from volume alone — you must read the book. And liquidity is fickle: it evaporates in a crisis exactly when you need to sell, which is why circuit breakers exist.

**C5. "Explain the bid-ask spread as if I were a new client. Is a tight spread always good?"**

The bid is the best price someone will pay to buy from you; the ask is the lowest price someone will sell to you; the spread is the gap — effectively the round-trip cost of trading. A tight spread signals a liquid, competitive market and low cost, so it is generally good. But it is not guaranteed tomorrow — in stress it widens sharply, and a tight quote on tiny size still hides poor depth. So tight is good, but check depth too.

**C6. "Cash equity versus futures on the same stock — how would you decide which to use?"**

It depends on objective and horizon. Use cash equity for genuine ownership: dividends, votes, no expiry, loss capped at your investment. Use futures for leveraged, time-bound exposure — hedging, a directional view with less capital, or arbitrage — accepting expiry, daily mark-to-market, margin calls, and possible losses beyond initial margin. A hedger protecting a portfolio without triggering tax shorts futures rather than selling stock. The two are linked by cost-of-carry, so their prices track each other.

**C7. "What does it mean for a company to list, and what obligations come with it?"**

Listing admits a company's securities to trading on a recognised exchange, giving it a liquid market, a credible public valuation (useful as acquisition and ESOP currency), visibility, and an exit route for early investors. In return it accepts continuous LODR obligations: quarterly results, prompt disclosure of material events, governance norms (independent directors, audit committee), and 25% minimum public shareholding, plus listing fees and short-term market pressure. The reverse, delisting, buys out public shareholders via reverse book-building.

**C8. "Give me a concrete example of price discovery and why we should trust the price an exchange produces."**

Take Infosys. No committee sets its price; thousands of independent participants — retail, a hedge fund, a mutual fund, an HFT market-maker — submit orders reflecting their own information, and the matching engine aggregates that flow tick by tick into a single last-traded price. We trust it because it is the equilibrium of many competing, self-interested opinions with real money at stake, made consistent across venues by arbitrage (the law of one price), and produced transparently under a regulator. It is an information-processing machine whose output is a public good.

---

## Section D — Multiple-Choice Questions (with reasoning)

**D1. In a secondary-market equity trade, the cash paid by the buyer goes to:**
A) The company that issued the shares
B) The stock exchange
C) The selling investor
D) SEBI

**Answer: C.** Secondary trades transfer securities between investors; the buyer's cash goes to the selling investor. The issuer receives money only in the primary market. The exchange and SEBI charge fees/levies but are not the recipients of the trade consideration.

**D2. Which statement about a quote-driven market is correct?**
A) Liquidity comes only from peer orders in a central book
B) Designated market makers post two-way quotes and guarantee a counterparty
C) It offers greater order-book transparency than an order-driven market
D) It is the standard model for the NSE cash segment

**Answer: B.** In a quote-driven market, market makers continuously quote bid and ask, guaranteeing you can trade against them; their margin is the spread. A describes an order-driven market; transparency is generally lower (not C); the NSE cash segment is order-driven (not D).

**D3. In India, cash-market equity trades currently settle on:**
A) T+3
B) T+2
C) T+1, with optional T+0 being rolled out
D) T+5

**Answer: C.** India completed the shift to T+1 by January 2023 and began rolling out an optional same-day T+0 cycle from 2024. T+2 was the earlier regime.

**D4. Which is NOT a feature of the derivatives (F&O) segment?**
A) Leverage through margin
B) Dividend and voting rights on the underlying
C) Fixed expiry dates
D) Trading in standardised lots

**Answer: B.** Derivatives are contracts on an underlying; holders get no dividends or votes — those belong to actual shareholders. Leverage, expiry, and lot-based trading are all genuine F&O features.

**D5. Which pair correctly matches the institution to its role in the Indian market?**
A) NSDL/CDSL — regulator
B) SEBI — depository
C) NSE Clearing / ICCL — central counterparty (clearing)
D) NIFTY 50 — clearing corporation

**Answer: C.** NSE Clearing (NCL) and ICCL are the clearing corporations acting as central counterparties. NSDL/CDSL are depositories, SEBI is the regulator, and NIFTY 50 is an index — so A, B, and D are mismatched.

**D6. Circuit breakers primarily exist to:**
A) Increase trading volume
B) Pause or slow trading during extreme price moves
C) Guarantee profits to market makers
D) Replace the clearing corporation

**Answer: B.** Circuit breakers (price bands and market-wide halts) pause trading on extreme moves, giving participants time to absorb information and preventing disorderly cascades — important because liquidity can vanish in a crisis. They do not boost volume, guarantee profits, or substitute for clearing.

---

*End of Q&A. Revisit any question you could not answer cleanly, then reread the corresponding section of Chapter 03.*
