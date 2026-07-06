# Q&A — Market Participants and Intermediaries

Companion practice bank for Chapter 11. Every question is followed by a full answer. Section A checks concepts, B applies them to situations and numbers, C rehearses interview questions with model answers, and D sharpens judgement on the tricky distinctions between the intermediaries.

---

## Section A — Concept Check

**A1. What four problems does a "naked" market — buyers and sellers dealing face to face — fail to solve, and how does intermediation solve them?**

The four failures are **search** (finding a willing counterparty), **trust** (will the other side actually perform?), **settlement** (who moves the money and securities, and how do we know it happened?), and **record-keeping** (who owns what, now and permanently). Intermediation solves each by assigning it to a dedicated specialist who does only that one job, for everyone, at massive scale. The broker solves search and access, the exchange solves matching, the dealer solves timing mismatches, the clearing corporation solves trust, and the depository solves record-keeping. Repeating one narrow function millions of times makes it cheap and certain — economies of scale convert an impossible individual burden into a commodity service costing a few rupees.

**A2. State the single most-tested distinction in this chapter: broker versus dealer.**

A **broker** is an **agent** — it arranges a trade between two other parties, never taking ownership of the security, and earns a **commission (brokerage)**. A **dealer** is a **principal** — it is one of the two parties, buying the security onto its own book (inventory) and selling from it, earning the **bid-ask spread** rather than a commission. When you sell to a dealer, the dealer *owns* what you sold; when you sell through a broker, the broker merely routes your order to a buyer. A firm that does both, in separate capacities, is a **broker-dealer**.

**A3. What extra obligation turns an ordinary dealer into a market maker, and what does the market gain?**

A **market maker** is a dealer that commits to *continuously quote two-way prices* — both a bid and an ask — in a security. This obligation guarantees that anyone wishing to trade always finds a counterparty, even when natural buyers and sellers do not coincide in time. The market gains **liquidity**: the ability to trade quickly without moving the price. Market makers are mandated in India for SME-platform stocks (NSE Emerge, BSE SME) and for many ETFs, where an Authorised Participant keeps the ETF price glued to NAV.

**A4. Describe the deliberate three-way separation of a trade, naming the Indian institution for each leg.**

Three logically separate things happen at three separate institutions. (1) **Matching** of buy and sell orders happens at the **exchange** (NSE / BSE). (2) The **guarantee** that the trade settles even if one side defaults is provided by the **clearing corporation** (NSE Clearing Ltd / Indian Clearing Corporation). (3) The **record** that ownership has changed is kept by the **depository** (NSDL / CDSL). No single institution does all three. The separation is a *safety feature*: it prevents any one party from having both the incentive and the ability to cheat.

**A5. What is novation, and why does it make anonymous trading safe?**

**Novation** is the legal substitution by which the clearing corporation steps into the middle of every matched trade, becoming **buyer to every seller and seller to every buyer**. After novation your counterparty is no longer the anonymous stranger on the other side — it is the well-capitalised clearing corporation, the **central counterparty (CCP)**. Even if the original counterparty vanishes, the CCP still performs. This lets you trade with strangers you will never meet, because you are effectively always trading with the same guaranteed institution.

**A6. Distinguish a depository from a custodian.**

A **depository** (NSDL, CDSL) is *market-wide* infrastructure — a central electronic registry that holds the securities of the *whole market* in dematerialised (book-entry) form. A **custodian** is a *private service provider* to one large institutional client (a foreign fund, mutual fund, insurer), safekeeping and administering that client's assets — often held *at* the depository — and running its back office: settlement, dividend collection, tax and regulatory reporting, FX. In short: the depository is public plumbing for everyone; the custodian is a private butler for one big investor.

**A7. What does an RTA do, and how is its role different from the depository's?**

A **Registrar and Transfer Agent (RTA)** — KFin Technologies, CAMS — maintains, on behalf of an *issuer* (a company or mutual fund), the master register of who owns its securities and services those owners: IPO allotments, transfers, dividend and interest payments, bonus/rights processing, and grievances. For a mutual fund it processes every purchase and redemption of units. The depository is the *market-level* owner registry (book-entry for the whole market); the RTA is the *issuer-level* record-keeper and investor-servicing arm. One serves the market; the other serves a specific issuer.

**A8. Contrast an investment bank with a broker in terms of *who* they stand between.**

A **broker** stands between two *investors*, arranging a secondary-market trade of an existing security. An **investment bank** (in India, a SEBI-registered **merchant banker**) stands between a *company that needs capital* and the *investors who supply it*, working the *primary* market: underwriting and book-building IPOs and bond issues, plus M&A advisory. The broker facilitates trading of what already exists; the investment bank helps *create* the securities in the first place.

---

## Section B — Applied / Scenario Questions

**B1. Mrs Rao taps "buy 100 Infosys" on her Zerodha app. Trace, in order, every institution that touches the trade and state each one's single job.**

1. **Broker (Zerodha)** — as *agent*, transmits her order into the exchange's order book; also did her KYC and holds her funds. 2. **Exchange (NSE)** — matches her buy order against the best sell order by price-time priority, creating a contract. 3. **Clearing corporation (NSE Clearing / NCL)** — via novation becomes central counterparty, nets the day's trades, collects margins, and guarantees settlement. 4. **Depository (NSDL/CDSL)** — on T+1 debits the shares from the seller's demat account and credits Mrs Rao's. 5. **Clearing banks** — simultaneously move the cash (delivery versus payment). 6. **Registrar/RTA** — updates the issuer's register and later pays her dividends. Mrs Rao interacted with only *one* party (her broker); the other five worked invisibly.

**B2. A full-service broker charges 0.30% brokerage; a discount broker charges a flat ₹20 per order. On a ₹5,00,000 equity delivery trade, compare the cost. At what trade size are they equal?**

Full-service cost = 0.30% × ₹5,00,000 = **₹1,500**. Discount cost = **₹20** flat. The discount broker is ₹1,480 cheaper on this trade — 75× less. They are equal when 0.30% × value = ₹20, i.e. value = ₹20 ÷ 0.003 = **₹6,667**. For any trade above roughly ₹6,700 the flat fee wins, and the gap widens without limit as size grows. This arithmetic is exactly why the discount-broker model (Zerodha, Groww, pioneered globally by Schwab and Robinhood) captured India's retail boom.

**B3. A dealer quotes a bid of ₹99.90 and an ask of ₹100.10 in a bond and turns over 1,00,000 units in a day, buying and selling roughly equal amounts. What is its gross spread income, and what is it being paid for?**

Spread = ₹100.10 − ₹99.90 = **₹0.20** per unit. Capturing the full spread on 1,00,000 round-trip units gives roughly ₹0.20 × 1,00,000 = **₹20,000** gross. It is being paid for *providing immediacy and liquidity* — standing ready to buy from sellers and sell to buyers on demand, warehousing inventory and bearing the price risk that the market moves against its book before it can offload. The spread is compensation for that inventory risk and service, not a commission.

**B4. A foreign pension fund wants to buy ₹2,000 crore of Indian equities. Explain why it appoints a custodian rather than opening a retail demat account, and list four things the custodian does for it.**

A large foreign investor cannot run Indian market back-office operations itself and needs an institutional-grade, regulator-compliant infrastructure — so it appoints a **custodian bank** (HDFC Bank, SBI-SG, Standard Chartered, Citi). Four custodian functions: (1) **safekeeping** the securities (held at the depository); (2) **trade settlement** — instructing and confirming DvP settlement; (3) **corporate actions and income** — collecting dividends/interest, processing bonuses and splits; (4) **reporting** — tax, FPI-regulatory, and NAV reporting, plus FX conversion of rupee proceeds. This lets the fund focus on investment decisions while the plumbing is outsourced.

**B5. In 2022 FIIs pulled roughly ₹1.2 lakh crore out of Indian equities, yet the Nifty ended the year roughly flat. Which participant absorbed the selling, and where did its money come from?**

**Domestic Institutional Investors (DIIs)** absorbed almost the entire quantum. Their money came from **retail SIP inflows** into mutual funds (running above ₹20,000 crore per month) plus deployments by **LIC** and **EPFO**. This illustrates the maturing of India's investor base: a domestic institutional counterweight, ultimately funded by millions of small retail savers, buying when volatile foreign money sells and stabilising the market. It is why watching the **daily FII vs DII net-flow figures** is essential to reading Indian market moves.

**B6. An investor buys 50 units of a Nifty 50 ETF and the trade fills instantly at a price almost exactly at NAV. Which intermediary made that possible, and by what mechanism does it keep price near NAV?**

The **market maker / Authorised Participant (AP)** made it possible by quoting continuous two-way prices, so the trade filled instantly. It keeps price near NAV through **creation/redemption arbitrage**: if the ETF price drifts *above* NAV, the AP *creates* new units by delivering the underlying basket of shares to the AMC, then sells those units — the extra supply pushes the price down toward NAV. If the price falls *below* NAV, it does the reverse (buys cheap units, redeems them for the basket). This live arbitrage enforces fair pricing, and it is why an ETF trades close to the value of its holdings.

**B7. During settlement of a batch of trades, a broker-member defaults before delivering cash. Walk through how the clearing corporation ensures the buyers still receive their securities.**

Because the CCP has taken on the trade via **novation**, the defaulting member's counterparties face the CCP, not the defaulter — so the buyers' delivery is unaffected. The CCP covers the gap using its **risk-management waterfall**: first the **margins** (initial and mark-to-market) already collected from the defaulting member, then the defaulter's contribution to the **Settlement Guarantee Fund (SGF)**, then the SGF's mutualised resources and the CCP's own capital. It can also **liquidate the defaulter's open positions** to limit loss. Settlement completes; the loss is absorbed by the prefunded risk structure, not passed to the innocent buyer.

**B8. Reliance's 2020 rights issue was India's largest ever. Name at least five intermediary types that had to assemble and state each one's contribution.**

(1) **Merchant bankers / BRLMs** (Morgan Stanley, Kotak) — structured, priced, and managed the issue. (2) **Registrar/RTA** (KFintech) — processed millions of shareholder entitlements and allotments. (3) **Depositories** (NSDL/CDSL) — credited the partly-paid rights shares into demat accounts. (4) **Clearing corporation** — guaranteed settlement of the rights-entitlement trading on the exchange. (5) **Brokers** — through which retail shareholders subscribed. (6) **Custodians** — through which large institutional holders acted. Six intermediary types, one capital raise — a snapshot of the whole cast in motion.

---

## Section C — Interview-Style Questions

**C1. "Explain the difference between a broker and a dealer, and what a market maker adds."**

A broker is a pure **agent**: it arranges a trade between two other parties, never owns the security, and earns a **commission**. Because it does not take the other side, it has no stake in which way the price moves — which is precisely why over-trading a client's account ("churning") is an abuse. A dealer is a **principal**: it trades from its own inventory, so when you sell to it, it owns what you sold, and it earns the **bid-ask spread** as compensation for warehousing inventory and bearing price risk. A **market maker** is a dealer with an obligation to *continuously quote both a bid and an ask*, guaranteeing a counterparty is always available and thereby supplying the market's liquidity. Many large firms are "broker-dealers" doing both in separate roles.

**C2. "When I buy a share on the NSE, who actually guarantees I'll receive it? Walk me through the plumbing."**

Not the exchange — its job ends at *matching* your order and creating the contract. The guarantee comes from the **clearing corporation** (NSE Clearing Ltd). Through **novation** it becomes the central counterparty — buyer to every seller and seller to every buyer — so your effective counterparty is the well-capitalised CCP, not the anonymous stranger who sold. It also **nets** the day's trades and collects **margins** plus a **Settlement Guarantee Fund** to cover defaults. On **T+1**, the **depository** (NSDL/CDSL) moves the shares between demat accounts while **clearing banks** move the cash simultaneously — **delivery versus payment**, so neither leg happens without the other. Three separate institutions — exchange, clearing corporation, depository — each doing one job, is a deliberate safety design.

**C3. "What's the difference between a depository, a custodian, and a registrar? People confuse all three."**

They sit at different levels. The **depository** (NSDL, CDSL) is *market-wide* infrastructure: the central electronic registry holding everyone's securities in book-entry form — you reach it through a Depository Participant, usually your broker. A **custodian** is a *private* service provider to one large institutional client, safekeeping and administering that client's assets (often held at the depository) and running its back office. A **Registrar and Transfer Agent** works for the *issuer* — maintaining the company's or mutual fund's own register and servicing its investors (allotments, dividends, redemptions). So: depository = the market's vault; custodian = one big investor's butler; RTA = the issuer's record-keeper. Different levels, different clients, different jobs.

**C4. "Why does a clearing corporation get called 'systemically important,' and what changed after 2008?"**

Because a CCP deliberately *concentrates* risk: by becoming counterparty to every trade, it becomes a single node on which the whole market depends. If it managed risk poorly and failed, the failure would cascade across every member simultaneously — so it is heavily regulated and required to hold margins, a Settlement Guarantee Fund, and strong capital. The 2008 crisis exposed the opposite danger — a vast web of *uncleared, bilateral* OTC derivatives where no one knew who was exposed to whom (the AIG problem). The global reform response (Dodd-Frank, EMIR) pushed standardised OTC derivatives to be *centrally cleared* through CCPs, trading diffuse, opaque counterparty risk for concentrated, transparent, well-managed risk.

**C5. "What does an investment bank actually do, and how is it different from the bank where I keep my salary?"**

An **investment bank** works the wholesale capital markets. Its core functions are **underwriting** — helping a company issue shares or bonds, pricing the issue, running the roadshow and book-building, and often guaranteeing the sale by buying any unsold portion — plus **M&A advisory** and **sales, trading, and research** for institutional clients. Your salary bank is a **commercial bank**: it takes deposits and makes loans, earning the interest margin. The investment bank raises capital by *creating and placing securities*; the commercial bank *intermediates deposits into loans*. In India the issue-management function requires a SEBI **Merchant Banker** licence; the lead managers on an IPO are called **BRLMs**. Universal banks like SBI or ICICI run both businesses under one roof.

**C6. "How has India's retail investor base changed, and why does the FII-versus-DII flow number matter?"**

India has seen a historic retail surge: demat accounts jumped from about 4 crore in 2020 to over 15 crore by 2024, and monthly SIP inflows into mutual funds now exceed ₹20,000 crore. This matters because that steady retail money, channelled through **DIIs** (mutual funds, LIC, EPFO), has become a structural *counterweight* to **FII/FPI** flows, which are large and mobile and historically dictated market direction. When foreign funds sell on a global shock, DIIs funded by relentless SIPs now often buy the other side and cushion the fall — as in 2022. So the **daily FII vs DII net-flow figure** tells you who is driving the tape and whether domestic money is absorbing foreign volatility. You cannot read Indian market moves without it.

**C7. "Distinguish an FPI from FDI. Why do regulators treat them so differently?"**

**FPI (Foreign Portfolio Investment)** is buying *tradable securities* — shares, bonds — as a passive financial holding, registered under SEBI's FPI framework. It is liquid and mobile: it can exit in seconds, which is why FPI flows swing the Nifty and the rupee daily. **FDI (Foreign Direct Investment)** is a *controlling or lasting stake* in a business — building a factory, acquiring a company — long-term and illiquid, governed by an entirely different framework (RBI/DPIIT, sectoral caps). Regulators treat them differently because their *stability and intent* differ: portfolio money is "hot" and can destabilise a currency if it flees en masse, so it is monitored for surges and sudden stops, whereas direct investment is "patient" capital tied to real assets and is generally encouraged with fewer liquidity concerns.

---

## Section D — Multiple-Choice Questions (with reasoning)

**D1. When you sell shares to a dealer, the dealer:**
A. Passes your shares to another investor for a commission
B. Takes the shares onto its own inventory and earns the spread
C. Guarantees the trade via novation
D. Records your ownership in a demat account

**Answer: B.** A dealer is a *principal* — it buys the shares onto its own book and earns the bid-ask spread. A describes a *broker* (agent, commission). C is the *clearing corporation*. D is the *depository*. The dealer's defining feature is taking the security onto its own inventory.

**D2. Which institution becomes the central counterparty to every trade through novation?**
A. The stock exchange
B. The depository
C. The clearing corporation
D. The custodian

**Answer: C.** Novation — becoming buyer to every seller and seller to every buyer — is the clearing corporation's defining act, making it the CCP. The exchange only *matches*; the depository only *records and moves* securities; the custodian only serves one client. Confusing the exchange with the clearing corporation is a classic error — NSE and NSE Clearing are deliberately separate entities.

**D3. India has how many depositories, and which are they?**
A. One — NSDL
B. Two — NSDL and CDSL
C. Two — NSE and BSE
D. Three — NSDL, CDSL and SEBI

**Answer: B.** India has exactly two depositories: **NSDL** (older, promoted by IDBI/NSE/UTI, historically larger by value) and **CDSL** (promoted by BSE, larger by number of accounts, and itself publicly listed). NSE and BSE are *exchanges*, not depositories; SEBI is the regulator.

**D4. A market maker's defining obligation is to:**
A. Match buy and sell orders by price-time priority
B. Continuously quote both a bid and an ask
C. Underwrite new share issues
D. Safekeep assets for foreign investors

**Answer: B.** A market maker must *continuously quote two-way prices*, guaranteeing a counterparty is always available and supplying liquidity. A is the exchange's function; C is an investment bank's; D is a custodian's.

**D5. The simultaneous exchange of securities and cash at settlement, so that neither leg happens without the other, is called:**
A. Novation
B. Netting
C. Delivery versus Payment (DvP)
D. Book-building

**Answer: C.** DvP links the securities leg and the cash leg so that delivery and payment occur together, eliminating the risk of paying and not receiving. Novation is the CCP substitution; netting collapses many trades into one net obligation; book-building is an IPO pricing method.

**D6. Which pair is correctly matched to the market it primarily operates in?**
A. Investment bank — secondary market
B. Broker — primary market
C. Investment bank — primary market
D. Depository — primary market only

**Answer: C.** Investment banks (merchant bankers) dominate the *primary* market — creating new securities via underwriting and IPOs. Brokers and dealers dominate the *secondary* market (A and B are reversed). Depositories operate across both, so D is wrong.

**D7. A large foreign fund holds its Indian securities through, and gets back-office administration from, a:**
A. Depository Participant it opens directly
B. Custodian bank
C. Registrar and Transfer Agent
D. Sub-broker

**Answer: B.** Large institutional investors appoint a **custodian bank** to safekeep and administer their assets (settlement, income collection, reporting). A depository is reached through a DP but is not a private administrator; the RTA serves the *issuer*, not the investor; a sub-broker merely brings clients to a main broker.

**D8. FPI differs from FDI primarily in that FPI is:**
A. A controlling stake in a business, held long term
B. A passive, liquid holding of tradable securities that can exit quickly
C. Regulated by RBI's sectoral caps rather than SEBI
D. Restricted to government securities only

**Answer: B.** FPI is passive, portfolio investment in tradable securities — liquid and mobile, which is why its flows swing markets daily. A describes FDI. C is backwards — FPI sits under SEBI's framework while FDI faces sectoral caps. D is false — FPI covers equities and corporate bonds, not just G-secs.

---

*30 questions: 8 concept-check, 8 applied, 7 interview, 7 MCQ — each with a full answer.*
