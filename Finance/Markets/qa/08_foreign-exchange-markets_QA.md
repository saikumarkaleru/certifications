# Q&A — Foreign Exchange Markets

A companion practice bank for Chapter 08. Every question is followed by a full answer. Attempt each one before reading the answer; the aim is to reason from the founding problem — value must cross borders that money cannot — not to memorise definitions.

---

## Section A — Concept-Check Questions

**A1. In one sentence, what is an exchange rate, and why must it always be quoted as a pair?**

An exchange rate is simply **the price of one currency expressed in another** — money priced in money. It must be quoted as a pair because you never buy or sell a currency in isolation: buying dollars automatically means selling rupees, so a currency can only rise or fall **relative to something else**. There is no absolute price of a currency, only a relative one.

**A2. Read USD/INR = 83.20. Identify the base and quote currency and state what the number means.**

USD is the **base** currency and INR is the **quote** (counter) currency. In BASE/QUOTE, the number tells you how many units of the quote currency equal **one** unit of the base — so 1 US dollar costs 83.20 Indian rupees. Rising USD/INR means each dollar buys more rupees, i.e., the rupee is depreciating.

**A3. Distinguish a direct quote from an indirect quote, from an Indian standpoint.**

A **direct quote** is home currency per one unit of foreign currency — ₹83.20 per $1. An **indirect quote** is foreign currency per one unit of home currency — $0.01202 per ₹1. They are **reciprocals of the same rate**, viewed from opposite ends. India, like most of the world, conventionally uses **direct quotes** (rupees per dollar); the UK, Australia, the Eurozone, and New Zealand quote indirectly against the dollar.

**A4. What is the single dividing line between a spot and a forward transaction?**

**Timing of delivery.** A spot deal exchanges currencies at today's rate with settlement usually **T+2** (near-immediate). A forward locks a rate **today** but delivers on a chosen **future** date — a month, three months, a year out. Splitting the rate (agreed now) from the money movement (later) is exactly what turns FX from a conversion service into a risk-management tool.

**A5. State covered interest rate parity (CIP) in words, and what it implies about the rupee's forward.**

CIP says the forward rate is the spot rate adjusted by the **interest rate differential** between the two currencies: Forward = Spot × (1 + quote-currency rate) / (1 + base-currency rate). Because Indian interest rates are structurally **higher** than US rates, the rupee trades at a **forward discount** — USD/INR forward rates sit *above* spot. If they didn't match the interest gap, arbitrageurs would earn a riskless profit, forcing the forward back to parity. The forward is therefore **not a forecast** — it is arbitrage-enforced arithmetic.

**A6. What is an FX swap, and why is it the largest FX instrument by turnover?**

An FX swap combines a **spot deal and an offsetting forward** — e.g., buy dollars spot and simultaneously sell them forward. It moves liquidity across time (effectively borrowing one currency and lending another for a period) **without** taking outright currency exposure. Banks use it constantly to manage funding and roll positions, which is why it dominates turnover — most FX flow is financial plumbing, not trade conversion.

**A7. Define a pip and a spread.**

A **pip** is the smallest standard price increment — the fourth decimal place (0.0001) for most pairs, or the second decimal (0.01) for yen pairs. The **spread** is the gap between the dealer's **bid** (the rate at which the dealer buys the base currency from you) and **ask/offer** (at which the dealer sells it to you); it is the dealer's margin, razor-thin for liquid majors and wide for illiquid pairs.

**A8. What is a cross rate, and how is EUR/INR built?**

A cross rate is a rate between two currencies **neither of which is the dollar**. EUR/INR is derived through the dollar as the common leg: EUR/INR = EUR/USD × USD/INR. With EUR/USD = 1.0850 and USD/INR = 83.20, EUR/INR ≈ 90.27. Historically all crosses were routed via the dollar; some majors now trade directly, but the dollar's pivot role persists.

**A9. What does it mean that the rupee runs on a "managed float"?**

The rupee is **broadly market-determined**, but the RBI **intervenes to curb excessive volatility** rather than to defend a fixed level or peg. The RBI does not publish a target rate; it lets fundamentals set direction while smoothing sharp swings, intervening **both ways** — selling dollars to support the rupee, buying dollars to cap appreciation and build reserves.

**A10. What is Herstatt risk, and how is it solved globally?**

Herstatt (settlement) risk is the danger that in an FX trade you **pay out one leg but never receive the other**, because the two legs settle in different countries and time zones. It is named after a 1974 German bank that failed after receiving Deutschmarks but before paying out dollars. The global solution is **CLS (Continuous Linked Settlement)**, which settles both legs **simultaneously** on a payment-versus-payment (PvP) basis across 18 major currencies — if one side doesn't pay, neither leg goes through.

---

## Section B — Applied / Scenario Questions

**B1. Spot USD/INR is 83.00. US 3-month rate is 5% p.a., India's is 7% p.a. Compute the no-arbitrage 3-month forward, and show what an arbitrageur would do if a bank quoted only 83.10.**

Forward ≈ 83.00 × (1 + 0.07/4) / (1 + 0.05/4) = 83.00 × 1.0175 / 1.0125 ≈ **83.41.**
If a bank quoted the forward at only 83.10 (too low), the arbitrageur would **borrow dollars at 5%, convert to rupees at spot, invest the rupees at 7%, and sell rupees forward at 83.10** — locking a riskless profit because the forward under-charges for the interest gap. Those trades would push the forward up until it reached ≈83.41. This is precisely why forward points track interest differentials, not forecasts.

**B2. Infosys will receive $10 million in 3 months. Spot is 83.00; the 3-month forward is 83.60. It fears the rupee strengthening to 81.00. What should it do, and what is the outcome under each scenario?**

Infosys should **sell $10 million forward at 83.60**, locking in **₹83.60 crore** regardless of where spot goes. If spot falls to 81.00 (rupee stronger), the hedge saved ₹2.60 per dollar — ₹2.6 crore versus converting at spot. If spot rises to 85.00 (rupee weaker), Infosys **forgoes** the ₹1.40 per dollar gain — the price of certainty. An exporter fearing a *rising* rupee sells dollars forward; that is the textbook transaction-exposure hedge.

**B3. An importer owes $1 million in 90 days and fears the rupee falling (dollar strengthening). Contrast a forward hedge with a currency-option hedge.**

**Forward:** the importer **buys dollars forward**, locking the rupee cost today at no premium. It removes downside *and* upside — if the rupee strengthens, the importer cannot benefit. **Option (a USD call):** the importer pays an **upfront premium** for the *right, not the obligation,* to buy dollars at a strike. If the rupee weakens, the option protects; if it strengthens, the importer lets the option lapse and buys cheaper in the market. The option is insurance that keeps upside; the forward is a free but rigid lock.

**B4. Compute EUR/INR given EUR/USD = 1.0920 and USD/INR = 83.15. Which two "legs" are you chaining, and why through the dollar?**

EUR/INR = EUR/USD × USD/INR = 1.0920 × 83.15 ≈ **90.80.** You chain the euro-to-dollar leg and the dollar-to-rupee leg, cancelling the shared USD term. It routes through the dollar because the USD is the world's **vehicle currency** — on one side of roughly 88% of all trades — so dollar-based quotes are the deepest and most reliable pivot for pricing a non-dollar cross.

**B5. In late 2022 the rupee slid toward 83 as the Fed hiked aggressively. The RBI sold dollars and reserves fell from ~$640bn to below $530bn. Did the RBI defend a level, and what does this reveal about its philosophy?**

No — it **smoothed the descent, it did not reverse it.** The slide was driven by global dollar strength; the RBI sold dollars in spot and forward markets to slow a disorderly fall, not to peg the rupee at a target. This is the **managed-float philosophy in action: cushion the move, don't fight the fundamentals.** Spending reserves to lean against a fundamentally driven trend buys orderliness and time, not a permanent floor.

**B6. Overnight, a global risk-off event hits while Mumbai is closed. The Singapore USD/INR NDF spikes higher. What happens when Indian markets open, and why does the RBI care?**

When Mumbai opens, onshore spot **"gaps" up to catch the NDF-implied level** — the offshore market has already priced the shock. The RBI cares because price discovery for the rupee is partly being set **outside Indian hours and jurisdiction**, ceding pricing power to offshore centres. This is why the rupee has an active **NDF market** (it is not fully capital-account convertible, so NDFs cash-settle the difference in dollars against the RBI reference rate), and why the RBI has encouraged **onshore banks to participate** and pushed rupee derivatives to **GIFT City** — to bring price discovery back home.

**B7. An Indian IT firm has no invoiced dollar exposure today but its future competitiveness depends on the rupee. Which type of exposure is this, and can a forward fully hedge it?**

This is **economic exposure** — the deeper effect of currency moves on the firm's competitiveness on *un-invoiced* future sales, not a specific known cash flow. A forward hedges **transaction exposure** (a known future cash flow) cleanly, but it cannot fully hedge economic exposure because the amounts and timing are uncertain and structural. The better mitigant is a **natural hedge** — matching foreign-currency revenues with foreign-currency costs — which is free but only partial. (A **currency swap** suits long-dated loan or bond exposures, exchanging principal and interest streams over the full tenor.)

---

## Section C — Interview-Style Questions

**C1. "Explain covered interest rate parity as if the whole forward market depended on it — because it does."**

The forward rate is not a forecast; it is the **spot rate adjusted by the interest-rate differential**, enforced by arbitrage. Formally, Forward = Spot × (1 + quote-currency rate) / (1 + base-currency rate). If the forward ever drifted away from this, you could borrow the low-rate currency, convert at spot, invest in the high-rate currency, and lock the exchange back with a forward — pocketing a **riskless profit**. Those arbitrage flows push the forward straight back to parity. Because Indian rates exceed US rates, the rupee trades at a **forward discount** — USD/INR forwards sit above spot. My killer one-liner: "The forward isn't a forecast — it's the spot rate plus the interest-rate gap, enforced by arbitrage."

**C2. "USD/INR moves from 80 to 83. Did the rupee strengthen or weaken? A lot of candidates get this wrong."**

The rupee **weakened** — it **depreciated.** USD/INR is a direct quote from India's standpoint: rupees per dollar. When that number rises, each dollar costs more rupees, which means the rupee is worth less. The reliable rule is: **direct quote rising = home currency weakening.** The confusion comes from seeing a bigger number and assuming "bigger is stronger," but the number measures how many rupees it takes to buy one dollar, so more rupees means a cheaper rupee.

**C3. "Is a stronger rupee good for India? Give me the nuanced answer."**

There is no unqualified "good." A **stronger rupee helps importers** — cheaper crude, machinery, and foreign travel — and eases imported inflation. But it **hurts exporters and IT firms** whose revenues are in dollars, because each dollar earned converts to fewer rupees, squeezing margins and competitiveness. Currency strength always has **winners and losers**; the policy question is the balance, which is why the RBI runs a managed float smoothing volatility rather than chasing a "strong rupee" as an end in itself.

**C4. "How does a central bank actually manage its currency without a peg?"**

Through a **managed float**. The RBI lets fundamentals broadly set the rupee's direction but **intervenes to smooth excessive volatility**, both ways. Its toolkit: buying or selling dollars in the **spot and forward** markets, using **FX swaps** and its **$600bn+ reserves** to manage liquidity and level, and publishing a daily **1:30 pm reference rate** as a settlement benchmark. Selling dollars supports the rupee; buying dollars caps appreciation and rebuilds reserves. The philosophy is to cushion sharp moves, not defend a fixed number — as in 2022, when it slowed the slide toward 83 without reversing a globally driven trend.

**C5. "What drives an exchange rate in the short-to-medium term? Rank the biggest lever."**

The single most powerful short-to-medium-term driver is **interest rate differentials** — higher rates attract yield-seeking capital, lifting the currency, which is why the dollar strengthens when the Fed hikes. Behind that: **inflation** (higher inflation erodes purchasing power and depreciates a currency over time — the logic of purchasing power parity); the **balance of payments** (a large current-account deficit, like India's, needs capital inflows to fund it); **capital flows** (FPI into Indian equities and bonds is a dominant rupee driver — the 2013 taper tantrum saw the rupee crash as FPIs fled); **risk sentiment** (risk-off flights to the dollar, yen, and Swiss franc); and **commodity prices** (rising crude widens India's deficit and pressures the rupee).

**C6. "Why is FX settlement risky, and what stops a domino from a failed FX trade?"**

FX settlement is risky because the two legs are in **different countries and time zones**, so you can pay out one currency before receiving the other — classic **Herstatt risk**, from the 1974 German bank failure that left counterparties stranded. The global fix is **CLS (Continuous Linked Settlement)**, which settles both legs **simultaneously** on a payment-versus-payment basis across 18 major currencies — no payment, no settlement, so principal risk is eliminated. The rupee is **not** yet a CLS currency, so INR trades still settle bilaterally or through **CCIL**, India's Clearing Corporation, which acts as central counterparty and guarantees onshore USD/INR settlement, hugely reducing systemic risk.

**C7. "Give me the one-sentence framing of what the FX market is."**

The FX market is the global plumbing that lets value cross the borders money cannot — pricing each currency as a relative pair, separating the rate (agreed now) from delivery (spot or forward), so that both conversion and currency risk transfer can happen at the scale of trillions a day (~$7.5 trillion, BIS 2022, with the dollar on ~88% of trades).

---

## Section D — Multiple-Choice Questions (with reasoning)

**D1. USD/INR moves from 82.50 to 84.00. This means:**
(a) The rupee appreciated (b) The dollar weakened (c) The rupee depreciated (d) No change in relative value

**Answer: (c) The rupee depreciated.** USD/INR is a direct quote (rupees per dollar); a rising number means each dollar costs more rupees, so the rupee is worth less. Rising direct quote = home currency weakening.

**D2. Indian rates are 7% and US rates are 5%. Relative to spot, the USD/INR forward will be:**
(a) Below spot (rupee at a forward premium) (b) Above spot (rupee at a forward discount) (c) Equal to spot (d) Unrelated to interest rates

**Answer: (b) Above spot, rupee at a forward discount.** By covered interest parity, the higher-interest currency (INR) trades at a forward discount, so USD/INR forwards sit above spot. Arbitrage enforces this; it is not a forecast of rupee weakness.

**D3. Which instrument is a simultaneous spot purchase and offsetting forward sale of the same currency?**
(a) Currency option (b) FX swap (c) NDF (d) Currency future

**Answer: (b) FX swap.** It moves liquidity across time without outright currency exposure and is the largest FX instrument by turnover. An option gives a right at a strike; an NDF is a cash-settled offshore forward; a future is an exchange-traded forward.

**D4. Given EUR/USD = 1.10 and USD/INR = 83.00, the EUR/INR cross rate is closest to:**
(a) 75.45 (b) 84.10 (c) 91.30 (d) 82.00

**Answer: (c) 91.30.** EUR/INR = EUR/USD × USD/INR = 1.10 × 83.00 = 91.30. The shared dollar leg cancels, leaving euros priced in rupees.

**D5. An exporter will receive dollars in three months and fears the rupee strengthening. The standard hedge is to:**
(a) Buy dollars forward (b) Sell dollars forward (c) Buy a USD call option (d) Do nothing

**Answer: (b) Sell dollars forward.** The exporter locks the rupee value of future dollar receipts, removing the risk that a stronger rupee shrinks proceeds. Buying dollars forward is the importer's hedge, not the exporter's.

**D6. The rupee's active offshore NDF market exists primarily because:**
(a) Indian rates are too high (b) The rupee is not fully capital-account convertible (c) NDFs are cheaper than forwards (d) The RBI mandates offshore trading

**Answer: (b) The rupee is not fully capital-account convertible.** Because the rupee cannot be freely delivered offshore, non-deliverable forwards cash-settle the difference in dollars against the RBI reference rate. Convertibility, not cost or mandate, is the driver.

**D7. Herstatt (settlement) risk in FX arises because:**
(a) Exchange rates are volatile (b) Interest rates differ across countries (c) The two legs settle at different times in different countries (d) Central banks intervene

**Answer: (c) The two legs settle at different times in different countries.** You may pay one currency before receiving the other. CLS solves this with simultaneous payment-versus-payment settlement; volatility and rate differentials are separate risks.

**D8. Roughly what share of global FX turnover funds actual imports and exports?**
(a) The large majority (b) About half (c) A small fraction; most is financial (d) Exactly the trade-deficit amount

**Answer: (c) A small fraction; most is financial.** Of the ~$7.5 trillion daily turnover, only a small slice is trade conversion — the bulk is bank position management, swaps, and speculation. FX is as much a financial market as a utility.

---

*End of Q&A bank — Chapter 08, Foreign Exchange Markets.*
