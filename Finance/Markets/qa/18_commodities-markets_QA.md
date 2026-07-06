# Q&A — Commodities Markets

Companion practice bank for Chapter 18. Every question is followed by a full answer. Section A checks concepts, B applies them to numbers and situations, C rehearses interview questions with model answers, and D sharpens judgement on the tricky distinctions through MCQs with reasoning.

---

## Section A — Concept Check

**A1. What is the single primal need that brought commodity markets into existence?**

**Price certainty for people exposed to physical goods.** A farmer, a flour mill, an airline and a jeweller all face a price they cannot control but must live with — wheat at harvest, jet fuel every day, gold at restocking. None of them wants to *speculate*; each wants to *lock in* a price so they can plan, invest and sleep at night. Commodity markets exist to let those producers and consumers fix a price today for a transaction that settles later. A second, later need layered on top — investors discovering commodities diversify a portfolio — but the founding purpose was risk transfer for physical actors, not investment.

**A2. Two ideas do almost all the work in a commodity market. Name and explain them.**

**Standardisation** and **time-shifting of price.** Standardisation means the contract specifies exactly one grade, purity, quantity, delivery location and date, so every unit is *fungible* (interchangeable) and thousands of strangers can trade it with confidence — you cannot have a liquid market in "some wheat." Time-shifting means a futures contract separates the *price decision* from the *delivery decision*: the farmer fixes his November selling price for wheat he will not deliver until April, transferring the risk of a price fall to someone willing to bear it. Nobody moves any wheat today; they simply agree on tomorrow's price today.

**A3. Distinguish spot and futures markets on their core dimensions.**

The **spot** (cash) market is for *immediate* delivery (T+0 to T+2) at today's price; the buyer pays full value now, and its users are physical buyers and sellers actually exchanging goods. The **futures** market trades standardised contracts for a *fixed future* delivery date; the buyer posts only margin now, and its users are hedgers, speculators and arbitrageurs whose purpose is price discovery and risk transfer, not logistics. Spot has no leverage; futures are highly leveraged through margin. The two prices are linked but not equal — the gap between them is the seed of contango and backwardation.

**A4. Forwards and futures are economically similar but structurally different. How?**

A **forward** is a *private, customised* contract between two parties (say an exporter and a bank) — flexible on size and date, but carrying counterparty (default) risk, illiquid, and with no daily settlement. A **future** is its *standardised, exchange-traded, cleared* cousin, marked to market daily. Forwards dominate physical commercial hedging where a bespoke amount and date matter; futures dominate liquid, transparent price discovery. The economic bet is the same — fix a future price — but the machinery around it differs entirely.

**A5. Explain the difference between hard and soft commodities, and why it matters.**

**Hard** commodities are mined or extracted — metals and energy. **Soft** commodities are grown — crops and livestock. It matters because their economics differ: hard commodities track the *industrial cycle* (copper and oil rise in booms, fall in recessions), while softs are driven by *weather and biology* (a Brazilian frost, a poor monsoon, a crop disease). This is why copper is nicknamed **"Dr. Copper"** — its sensitivity to global industrial health makes it act like an economist forecasting recessions and booms.

**A6. What is the "cost of carry," and which curve shape does it produce?**

The cost of carry is the total cost of holding a physical commodity over time: **storage, insurance, and the financing cost of the capital tied up.** Because deferred delivery saves the holder these costs, in a calm market the futures price roughly equals spot *plus* cost of carry — which naturally produces **contango**, an upward-sloping curve where futures trade above spot. Crude oil, being expensive to store, is often in contango.

**A7. What is convenience yield, and which curve shape does it drive?**

The convenience yield is the *premium value of having the physical commodity on hand right now* — the benefit of being able to use it immediately rather than waiting. When there is a shortage today, people pay more for immediate delivery than for future delivery, so futures trade *below* spot: this is **backwardation**, a downward-sloping curve. A refiner that will shut down without crude this week values a barrel today far above a barrel in six months. Backwardation therefore signals tight physical supply.

**A8. What is roll yield, and why can it dominate a long-term commodity return?**

A futures contract expires, so an investor wanting continuous exposure must **roll** — sell the expiring contract and buy the next one. In **contango**, the next contract is more expensive, so each roll loses money (**negative roll yield**); in **backwardation**, the next is cheaper, so each roll makes money (**positive roll yield**). Over years this repeated cost or gain can dominate returns — which is why an investor "owning oil" through futures can *lose* money even when spot oil is flat, if the curve is persistently in contango.

**A9. Why is gold treated as "special" among commodities?**

Because gold behaves less like an industrial metal and more like a **currency or fear gauge.** It is barely consumed industrially relative to how much is *held* as a store of value, it produces no cash flow, and it is driven by **real interest rates, the US dollar, and crisis sentiment** rather than by industrial demand. Since gold pays no yield, high real rates raise the opportunity cost of holding it (price falls) while low or negative real rates make it shine. Lumping gold with copper and oil, which are geared to the economic cycle, produces wrong intuitions.

**A10. Who are the four main types of market participant, and why are speculators load-bearing?**

**Hedgers** (producers and consumers offloading price risk) are the market's reason to exist; **speculators** take on the risk hedgers shed, hoping to profit; **arbitrageurs** exploit price gaps and keep prices consistent; and **exchanges/clearing houses** provide the infrastructure. Speculators are load-bearing because they supply the **liquidity** without which a hedger would find no counterparty — a market of only hedgers would be one-sided and illiquid. They are not villains; excessive manipulative speculation is a real problem, which is why position limits and regulators exist, but the category as a whole is essential.

---

## Section B — Applied / Scenario Questions

**B1. Ramesh will harvest 100 quintals of chana in March. In December, March futures trade at ₹5,200/quintal. He sells 100 quintals of futures. Compute his net outcome if March spot is (a) ₹4,700 and (b) ₹5,700.**

(a) Spot ₹4,700: he sells physical chana in his mandi at ₹4,700 — a ₹500/quintal loss versus December — but **buys back** his short futures at ₹4,700, gaining ₹500/quintal. Net realised ≈ **₹5,200**. (b) Spot ₹5,700: he gains ₹500 physically but loses ₹500 on the futures buy-back — again net ≈ **₹5,200**. The hedge did its job: whichever way price moved, he locked ₹5,200. He traded away both the windfall and the disaster for certainty — a **short hedge**.

**B2. An airline budgets on Brent at $80 and buys Brent futures at $80 to hedge. Compute the effect on its effective fuel cost if Brent moves to (a) $110 and (b) $60.**

(a) Brent $110: physical fuel now costs $30/barrel more, but the long futures position gained ~$30/barrel, offsetting the higher bill — effective cost stays near **$80**, while unhedged rivals bleed. (b) Brent $60: physical fuel is $20 cheaper, but the futures position *lost* ~$20, so the airline is locked into an effective **~$80** while rivals enjoy $60. This is the deliberate trade-off of a **long hedge**: certainty in both directions, giving up the favourable move as the price of protection against the adverse one.

**B3. A wheat contract is worth ₹2.4 lakh and the exchange sets initial margin at 8%. How much capital does a trader post, what is the leverage, and what happens if losses mount?**

Margin posted = 8% × ₹2,40,000 = **₹19,200**, controlling ₹2.4 lakh of exposure — roughly **12.5× leverage.** This capital efficiency is why commodities are attractive but dangerous: a small adverse price move is magnified on the thin margin. If daily mark-to-market losses eat into the margin below the maintenance level, the trader receives a **margin call** and must top up the account or be **liquidated** (the position force-closed). Leverage cuts both ways.

**B4. Spot gold is ₹60,000 per 10g. One-month storage + insurance + financing works out to ₹500 per 10g. In a calm market, roughly where should one-month futures trade, and what is this state called?**

Futures ≈ spot + cost of carry = 60,000 + 500 = **₹60,500 per 10g.** Because the futures price sits *above* spot, the curve is in **contango** — the normal state driven by cost of carry. A long investor rolling this contract each month would pay the ₹500 premium repeatedly (negative roll yield). If, instead, an acute physical shortage pushed the one-month future *below* ₹60,000, that would signal **backwardation** and a positive convenience yield.

**B5. An investor buys a US oil ETF in 2015 expecting a recovery. Over the year spot crude drifts up modestly, yet the investor loses money. Explain how.**

The ETF holds **futures**, not physical oil, and the curve was in persistent **contango**. Each month the fund sold the cheap expiring contract and bought a more expensive next one, bleeding a few percent to **negative roll yield** every roll. Compounded over twelve rolls, that cost outweighed the modest rise in spot, so the investor lost money even though the headline oil price rose. The lesson: with commodity futures you are not simply betting on spot — the *shape of the curve* is part of your return.

**B6. A jeweller hedges physical gold he buys in Zaveri Bazaar using MCX gold futures, but the two prices do not move perfectly together. Name and explain the risk that remains.**

**Basis risk.** The **basis** is the difference between the local physical (spot) price and the futures price. The MCX contract specifies a particular purity, quantity and delivery warehouse, which is never *exactly* the gold the jeweller buys locally, so the two prices can diverge. If the basis moves between putting on the hedge and lifting it, a small residual gain or loss remains even in a well-constructed hedge. The jeweller accepts basis risk as the price of eliminating the far larger outright price risk.

**B7. On 20 April 2020, May WTI crude futures settled at about −$37/barrel. Explain, using contango and storage, how a price can go negative.**

COVID lockdowns collapsed oil demand overnight, and storage — especially at the Cushing, Oklahoma hub — filled to capacity. Traders holding expiring May futures faced *physical delivery* of oil they had nowhere to store. Rather than take barrels they could not house, they **paid others to take the contracts off their hands** — hence a negative price. It is contango and the storage constraint stretched to an absurd extreme: the curve was so steeply upward-sloping and near-term storage so scarce that immediate delivery had *negative* value. Physical reality, not a pricing glitch, drove it.

**B8. India consolidated commodity-derivative regulation after a specific scandal. What happened, and what changed?**

In 2013 the **National Spot Exchange (NSEL)** collapsed on a roughly ₹5,600 crore payment default, exposing weak oversight of spot exchanges in a fragmented, lightly regulated market. This accelerated the **2015 merger of the Forward Markets Commission into SEBI**, giving commodity derivatives the same regulatory rigour — position limits, margining, clearing standards — as securities. Since then SEBI has regulated commodity derivatives in India, and exchanges like NSE and BSE were permitted to offer them.

**B9. A copper trader notices copper futures on the LME are richer than the same-dated contract on SHFE, net of shipping and financing. What role does he play, and what is the market effect?**

He is an **arbitrageur**. He simultaneously *sells* the rich LME future and *buys* the cheap SHFE future, locking in the spread as a near-riskless profit once the two converge. The very act of selling on LME and buying on SHFE pushes the two prices back toward parity — which is precisely *why* such cross-exchange gaps are small and fleeting in liquid markets: arbitrageurs compete them away, keeping global prices consistent and fair.

---

## Section C — Interview-Style Questions with Model Answers

**C1. "In one sentence, why do commodity markets exist?"**

*Model answer:* "Commodity markets exist to give producers and consumers of physical goods **certainty about price** — they use standardised, cleared contracts that separate the *price decision* from the *delivery decision*, so a farmer can fix his selling price in November for wheat he won't deliver until April, transferring the risk of a price fall to someone willing to bear it." Lead with the function — price certainty and risk transfer — then show the mechanism that delivers it.

**C2. "Explain contango and backwardation without using jargon, and tell me what each signals."**

*Model answer:* "Plot futures prices against delivery month and you get a forward curve. **Contango** slopes upward — futures cost more than buying today — because holding the physical commodity costs money in storage, insurance and financing; that cost of carry is priced into deferred delivery. It's the normal, calm-market state. **Backwardation** slopes downward — futures cost *less* than buying today — because there's a shortage right now and people pay a premium for immediate delivery; that premium is the convenience yield. So contango is the market saying 'storage is the dominant cost,' and backwardation is the market saying 'physical supply is tight today.' Neither is good or bad in itself — it depends which side you're on."

**C3. "A producer and a consumer both want to hedge. Walk me through what each does and the trade-off they accept."**

*Model answer:* "A **producer** — a miner, farmer or oil driller — already owns or will own the commodity and fears a price *fall*, so it does a **short hedge**: it *sells* futures. If the price falls, the futures gain offsets the lower price it gets for physical output, locking its revenue. A **consumer** — an airline, food processor or jeweller — will *buy* the commodity and fears a price *rise*, so it does a **long hedge**: it *buys* futures. If the price rises, the futures gain offsets the higher input bill. The trade-off both accept is symmetric — they give up the favourable move too. A hedged producer captures no windfall from a spike; a hedged airline is stuck at a higher effective cost if oil falls. Hedging is insurance, not a profit centre."

**C4. "Why can an oil ETF lose money even when the oil price goes up? This trips up a lot of investors."**

*Model answer:* "Because most oil ETFs hold *futures*, not physical barrels, and futures must be rolled forward as they expire. When the curve is in contango — which oil often is — the next contract is more expensive than the expiring one, so every roll bleeds a little to **negative roll yield**. Over a year of monthly rolls, that cost can exceed a modest rise in spot oil, leaving the investor with a loss despite being 'right' on the direction. The takeaway is that owning a commodity through futures gives you spot movement *plus* roll yield, and in persistent contango the roll can quietly dominate the whole return."

**C5. "Why is gold different from copper, and how should that change how I think about it?"**

*Model answer:* "Copper is an industrial metal — it's consumed in construction and manufacturing, so its price is geared to the economic cycle and to Chinese demand; that's why it's called 'Dr. Copper,' a barometer of global growth. Gold is barely consumed industrially relative to how much is *held* as a store of value. It pays no cash flow, so its price is driven by real interest rates, the dollar and fear, not industrial demand. High real rates hurt gold because holding a yield-less asset has a big opportunity cost; low or negative real rates help it; and it rallies in crises when confidence collapses. Practically, treat gold almost like a currency or an insurance policy, and treat copper and oil as bets on the economic cycle."

**C6. "Are speculators harmful to commodity markets? Give me a balanced view."**

*Model answer:* "In moderation they're essential, not harmful. Hedgers want to shed price risk, but an opposite hedger rarely appears in the exact size and moment needed — so speculators step in, take the other side, and provide the **liquidity** that lets a farmer transact instantly. They also aid **price discovery** by aggregating competing views into the futures curve. The genuine problem is *excessive, manipulative* speculation — cornering a market or distorting prices — which is exactly why regulators like SEBI and the CFTC impose **position limits**. So the honest answer is: the category is load-bearing, but it needs guardrails."

**C7. "Does the futures price predict the future spot price?"**

*Model answer:* "Only loosely, and treating it as a forecast is a classic mistake. The futures price is really the spot price adjusted for the cost of carry and any convenience yield — not a crystal-ball prediction. A steep contango doesn't mean the market expects prices to jump; it often just reflects high storage and financing costs. So the curve's shape tells you about carry and current scarcity far more than it tells you where prices are actually headed. Reading contango as a bullish forecast is how people misinterpret the curve."

**C8. "Close the interview: sum up commodity markets in a couple of sentences."**

*Model answer:* "Physical goods have volatile prices that threaten the people who produce and consume them, so humans invented a way to fix a price today for a transaction that happens later — the standardised, cleared futures contract. Producers sell futures and consumers buy them to swap uncertainty for certainty; speculators take the other side and supply liquidity; and the gap between spot and futures is governed by two opposing physical realities — the cost of storing a commodity over time versus the value of having it on hand right now. Everything else, from Dr. Copper to negative oil, is that one story told from different seats."

---

## Section D — MCQs with Reasoning

**D1. In a normal, calm market where storage and financing are the main costs, the futures curve is typically in:**
(a) Backwardation
(b) Contango
(c) A flat line exactly equal to spot
(d) Negative territory

**Answer: (b).** With no acute shortage, the futures price roughly equals spot plus the **cost of carry** (storage, insurance, financing), producing an upward-sloping **contango** curve. Backwardation (a) requires current scarcity and a convenience yield. The curve is rarely exactly flat (c), and negative prices (d) are an extreme storage-crisis anomaly, not the norm.

**D2. A wheat farmer fearing a price fall before harvest should:**
(a) Buy futures (long hedge)
(b) Sell futures (short hedge)
(c) Buy call options only
(d) Do nothing, since futures can't help producers

**Answer: (b).** A producer who already owns or will own the commodity protects against a *fall* by **selling futures** — a short hedge. If the price falls, the futures gain offsets the lower physical price. Buying futures (a) is a *consumer's* long hedge, protecting against a *rise*. The market absolutely helps producers (d) — they are its founding users.

**D3. Backwardation in a commodity's forward curve most directly signals:**
(a) A glut of the commodity in storage
(b) High storage and financing costs
(c) Tight physical supply / scarcity right now
(d) That the market expects prices to fall

**Answer: (c).** Backwardation means futures trade *below* spot because immediate delivery commands a premium — the **convenience yield** — which happens when physical supply is tight today. A glut (a) and high carry costs (b) push toward contango, not backwardation. And the curve's shape is not a forecast (d); backwardation reflects current scarcity, not an expectation of falling prices.

**D4. An investor holding a long commodity futures position through a contango curve experiences:**
(a) Positive roll yield each time she rolls
(b) Negative roll yield each time she rolls
(c) No roll effect at all
(d) A guaranteed profit if spot is flat

**Answer: (b).** In contango the next contract is *more expensive* than the expiring one, so rolling forward loses money — **negative roll yield**. Positive roll yield (a) occurs in backwardation. Rolling always has an effect when the curve is sloped (c), and far from a guaranteed profit (d), contango can make a long position *lose* money even if spot is flat.

**D5. Which Indian exchange leads in agricultural commodity derivatives?**
(a) MCX
(b) NCDEX
(c) LME
(d) ICE

**Answer: (b).** **NCDEX** is India's leader in agri commodities — chana, guar seed, soybean, mustard, jeera, turmeric, cotton. MCX (a) leads in *non-agri* commodities (gold, silver, crude, base metals). LME (c) is London's base-metals exchange and ICE (d) is a global exchange home to Brent and softs — neither is Indian.

**D6. Which regulator has overseen commodity derivatives in India since 2015?**
(a) The Forward Markets Commission
(b) RBI
(c) SEBI
(d) The Ministry of Agriculture

**Answer: (c).** In 2015 the **Forward Markets Commission was merged into SEBI**, which now regulates commodity derivatives with the same rigour as securities — a shift catalysed by the 2013 NSEL scam. The FMC (a) no longer exists as a separate body. RBI (b) oversees OTC currency/rate derivatives, not exchange-traded commodities, and the Agriculture Ministry (d) is not a market regulator.

**D7. Which single factor is the most important driver of the *gold* price?**
(a) Chinese industrial demand
(b) Real (inflation-adjusted) interest rates
(c) Global construction activity
(d) OPEC production quotas

**Answer: (b).** Gold pays no yield, so its opportunity cost rises and falls with **real interest rates** — high real rates hurt gold, low or negative real rates help it — alongside the dollar and crisis sentiment. Chinese industrial demand (a) and construction (c) drive *industrial* metals like copper, not gold, which is barely consumed industrially. OPEC quotas (d) drive oil, not gold.

**D8. On 20 April 2020, WTI May crude futures settled at roughly −$37/barrel primarily because:**
(a) OPEC flooded the market with cheap oil
(b) Demand collapsed and storage was full, so holders paid others to take delivery
(c) A pricing error on the exchange
(d) The dollar strengthened sharply

**Answer: (b).** COVID lockdowns collapsed demand while storage at Cushing filled up, so traders holding expiring futures faced physical oil they could not store and **paid others to take the contracts** — contango and the storage constraint stretched to an extreme. It was not an OPEC glut (a), not an exchange error (c) — the price was real — and a stronger dollar (d) alone cannot drive a price below zero.

**D9. A forward differs from a future primarily in that a forward is:**
(a) Standardised, exchange-traded and cleared
(b) Marked to market daily
(c) Private, customised and carries counterparty risk
(d) Always cash-settled

**Answer: (c).** A **forward** is a bespoke, over-the-counter agreement between two parties, flexible on size and date but carrying default (counterparty) risk and no daily settlement. Standardisation, exchange trading, clearing (a) and daily mark-to-market (b) are precisely the features of a *future*, not a forward. Settlement method (d) is not the defining distinction — the private, customised, un-cleared nature is.

---

*End of Q&A bank for Chapter 18 — Commodities Markets.*
