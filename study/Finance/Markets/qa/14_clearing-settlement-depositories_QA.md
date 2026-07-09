# Q&A — Clearing, Settlement and Depositories

Companion practice bank for Chapter 14. Every question is followed by a full answer. Section A checks concepts, B applies them to numbers and situations, C rehearses interview questions with model answers, and D sharpens judgement through MCQs with reasoning.

---

## Section A — Concept Check

**A1. What single primitive problem does the entire post-trade machinery exist to solve?**

The **first-mover problem** — in any exchange of value between strangers, someone must part with their side first, and whoever moves first can be cheated. If the buyer pays first, the seller may vanish with the cash; if the seller delivers first, the buyer may never pay. On an anonymous exchange this is magnified: you cannot vet your counterparty, hundreds of millions of trades happen daily, and prices move continuously so a default tomorrow imposes a replacement cost today. Clearing, settlement and depositories are the trusted plumbing that guarantees the trade completes, removes the fear of the counterparty, and moves ownership safely and fast.

**A2. Distinguish clearing, settlement and the depository — three jobs people wrongly lump together.**

**Clearing** is the *calculation and guarantee* stage: the Clearing Corporation steps into the middle of every trade (novation), works out the net each participant owes or is owed (netting), and guarantees the trade even if a side defaults. **Settlement** is the *actual exchange* stage: funds move from buyers to sellers and securities from sellers to buyers, simultaneously via Delivery-versus-Payment. **Depository** is the *ownership-record* stage: shares live as electronic entries at NSDL or CDSL, so transferring ownership is just editing a database. Clearing is the promise, settlement is the delivery, the depository is the receipt.

**A3. What is novation, and what two things does it achieve?**

**Novation** is the legal substitution that is the heart of clearing: the single contract "Buyer B buys from Seller S" is torn up and replaced by two new contracts — "B buys from the CCP" and "the CCP buys from S." It achieves, first, **centralised counterparty risk** — every participant faces only the well-capitalised CCP, so if S defaults, B is unaffected and the CCP pursues S with its own resources; and second, **preserved anonymity** — B and S never need to know or trust each other. The cost is that the CCP becomes a single, systemically important point of risk, which is why it must be guarded by margin and a default waterfall.

**A4. What is multilateral netting and why does it matter?**

Multilateral netting is the CCP compressing all of a member's buys and sells in a security into **one** net securities position and **one** net cash position per settlement — netting each participant against the whole system rather than against individual counterparties. It matters because it slashes the volume of money and securities that must physically move; CCP studies routinely show netting cuts gross settlement obligations by **90–98%**. Less movement means less liquidity tied up, lower operational risk, and lower cost. Crucially it compresses the *plumbing*, not your ownership — you still legally own every share you bought.

**A5. What does Delivery-versus-Payment (DvP) guarantee, and how?**

DvP guarantees that **neither side is ever exposed mid-transaction** by locking the two legs together: securities and cash change hands *simultaneously*, so a seller never gives up shares without receiving funds and a buyer never pays without receiving shares. It is the direct settlement-stage answer to the first-mover problem — no one has to move first because both move at once.

**A6. What is a depository, and how does a DP relate to it?**

A **depository** is to shares what a bank is to money: it holds your securities as electronic ledger entries rather than physical certificates. India's two are **NSDL (1996, first)** and **CDSL (1999)**. You never deal with the depository directly — a **Depository Participant (DP)**, usually your broker or bank, is the agent through whom you open and operate your demat account, exactly as a bank branch is the access point to the banking system. Your shares sit in *your own* demat account at the depository, not in the broker's, which is what protects you if the broker fails.

**A7. What did dematerialisation kill, and why did it matter for India?**

Demat converted physical share certificates into fungible electronic entries, killing the plagues of the paper era: **forgery and fake certificates, "bad deliveries"** (signature mismatches, torn certificates, wrong transfer deeds), **theft and loss in transit**, and **weeks-long settlement** during which either side could renege. Settlement-failure rates collapsed. This single change — backed by the Depositories Act, 1996 and SEBI making demat compulsory by ~2001 — is why Indian retail participation could scale to crores of investors.

**A8. What is the default waterfall, and why must it exist?**

The default waterfall is the ordered stack of resources a CCP consumes to absorb a member default, without which the CCP's guarantee would not be credible. Losses eat through, top-first: (1) the **defaulting member's own margin and collateral**, (2) the **defaulting member's SGF contribution**, (3) the **CCP's own capital ("skin in the game")**, (4) **non-defaulting members' mutualised SGF contributions**, and (5) **further CCP capital and assessment rights**. A well-run CCP almost never reaches the mutualised layers — the defaulter's own resources usually cover the loss.

**A9. Why is India's settlement cycle a world-leadership story, and where is it heading?**

India ran ahead of the world in shortening the gap between trade and settlement: weekly account-period + badla pre-2001, then **T+3 (2002) → T+2 (2003) → full T+1 (January 2023)** — becoming the **first large market to fully adopt T+1 for all stocks** — and an **optional T+0 beta from March 2024**, with instant settlement under SEBI consultation. By contrast the **US moved to T+1 only in May 2024** and Europe/UK target it around 2027. Shorter cycles cut the time counterparty and replacement-cost risk stay open and free blocked margin capital.

---

## Section B — Applied / Scenario Questions

**B1. Three brokers trade Infosys among themselves in a day: A buys 1,000 sells 300; B buys 200 sells 900; C buys 500 sells 500. How much actually moves after multilateral netting?**

Net each broker: A = **+700 (receives)**, B = **−700 (delivers)**, C = **0**. Gross activity involved 2,900 share-movements across many trades, but after multilateral netting only **700 shares** actually move — B delivers 700 into the pool and A receives 700; C settles nothing. That compression from 2,900 gross to 700 net (plus a single net cash difference per broker) is exactly why a market can trade in gross but settle in net, with roughly 90%+ of the plumbing movement disappearing.

**B2. Broker X's clients buy 2,00,000 SBI shares and sell 1,85,000 SBI shares across hundreds of trades in a day. What does X settle, and how much movement is saved?**

Without netting, X would deliver 1,85,000 shares, receive 2,00,000, and move both full cash legs. After multilateral netting at NCL, X simply **receives a net 15,000 SBI shares** and pays a single net cash difference. Of the 3,85,000 gross share-movements, only 15,000 remain — roughly **96% of the gross movement evaporates**. That vanished movement is capital freed and operational/settlement risk removed.

**B3. Priya buys 50 HDFC Bank shares at ₹1,600 through Zerodha on Monday. Trace the trade to completion, and say what happens if the original seller defaults.**

**Monday (T):** NSE matches the trade; NCL novates and becomes Priya's counterparty; her obligation nets down with thousands of others. **Monday evening:** Zerodha sees its net obligations; Priya's ₹80,000 is already blocked upfront via a UPI/margin mandate. **Tuesday (T+1):** pay-in — buyers' funds and sellers' shares reach NCL; pay-out — 50 shares are credited to Priya's demat account and ₹80,000 reaches the net sellers, all under DvP. If the original seller had defaulted, **Priya is unaffected** — NCL still delivers her shares using the auction and SGF machinery and pursues the defaulter itself.

**B4. A friend insists "T+1 means I get my shares within 24 clock hours." Correct them with a concrete example.**

T+1 means **one working day** after trade day, not 24 clock hours. A trade on **Friday** settles on **Monday** (weekends and exchange holidays are excluded), which is roughly 72 clock hours, not 24. Similarly a trade the day before a public holiday settles the next working day after it. The "T+N" convention counts settlement days, never fixed hours.

**B5. On a stressed day a large clearing member defaults with a shortfall that exceeds its posted margin. Walk the loss through the waterfall and say when other members feel pain.**

The shortfall first consumes the **defaulter's own margin and collateral**; if that is exhausted, next its **own SGF contribution**; then the **CCP's own capital (skin in the game)**. Only if all three are blown through does the loss reach layer four — the **non-defaulting members' mutualised SGF**. So surviving members feel pain only after the defaulter's entire resources *and* the CCP's own capital are gone, which is rare. This ordering deliberately makes the defaulter and the CCP bear losses before innocent members, aligning incentives and protecting the system.

**B6. Your shares are held in CDSL but you traded on NSE; a colleague says that is impossible. Who is right?**

You are right; the colleague is repeating the **"NSDL is for NSE, CDSL is for BSE" myth**. Both depositories serve both exchanges. Which depository your shares sit in depends on **your broker/DP**, not on the exchange you traded on. You can perfectly well buy a stock on NSE and have it credited to a CDSL demat account, because the depository layer is separate from the trading venue.

**B7. Lehman Brothers collapses holding a $9 trillion notional interest-rate swap book cleared through LCH. What happened, and what does it prove?**

LCH.Clearnet (SwapClear) used **Lehman's posted margin** to hedge and then auction off the positions in an orderly way. The default was managed **without dipping into the mutualised default fund — no other member lost money**. It proves the CCP model working as designed: one member failed, but novation + upfront margin + the default waterfall absorbed the blow so the failure did not cascade. It is the strongest real-world case for central clearing, which is why the G20 later mandated central clearing of standardised OTC derivatives.

**B8. A surveillance-flagged illiquid scrip is put under "trade-for-trade" settlement. Why deny it netting, and what changes for the participant?**

Under **trade-for-trade (gross) settlement, each trade settles individually** rather than being netted down. Regulators impose it on surveillance-flagged or illiquid scrips because netting could **hide manipulation** — offsetting buys and sells within a day can disguise circular or wash trading, and gross settlement forces every leg to actually deliver and pay, exposing artificial volume. For the participant, it means no netting compression: every buy must be funded and every sell must be delivered in full, with no intraday offset and no squaring off to avoid delivery.

---

## Section C — Interview-Style Questions (with model answers)

**C1. "Walk me through what happens between a matched trade and the shares landing in my demat account."**

*Model answer:* Six post-trade steps. (1) **Trade capture** — the exchange sends the matched trade to its Clearing Corporation (NCL for NSE, ICCL for BSE). (2) **Novation** — the CCP splits the trade into two contracts each facing itself, so I no longer care who my counterparty was. (3) **Netting** — across the day the CCP compresses all obligations into one net securities and one net cash position per clearing member. (4) **Obligation download** — after close, each member learns its net funds and securities obligations. (5) **Settlement on T+1** — pay-in (net sellers deliver shares, net buyers pay funds into the CCP), then pay-out (the CCP releases shares to net buyers and funds to net sellers), all locked as DvP. (6) **Depository update** — NSDL/CDSL debit the seller's demat account and credit mine. The whole design lets anonymous strangers finish a trade without trusting each other.

**C2. "A CCP concentrates risk into one institution. Isn't that more dangerous than leaving risk spread out bilaterally?"**

*Model answer:* It transforms the risk rather than deleting it, and on balance makes the system safer. Bilaterally, every participant carries hidden exposure to every counterparty, and one big default can cascade unpredictably — as 2008 nearly showed. A CCP replaces that opaque web with a single, transparent counterparty engineered to never fail: it collects **upfront margin** (VaR/SPAN, ELM, mark-to-market, peak), maintains a **Core Settlement Guarantee Fund**, and stacks a **default waterfall** behind its guarantee. So yes, risk is concentrated — which is precisely why CCPs are designated **systemically important FMIs** and supervised under the CPMI-IOSCO Principles. The trade is: swap diffuse, cascading bilateral risk for concentrated risk in an institution that is heavily capitalised, margined and watched. The Lehman-through-LCH episode — no surviving member lost money — is the proof it is worth it.

**C3. "Why did India shorten its settlement cycle to T+1, and why not just go instantly to T+0 for everything?"**

*Model answer:* The settlement gap is the window in which counterparty and replacement-cost risk stay open and margin capital sits locked. Shortening it — T+3 in 2002, T+2 in 2003, full **T+1 by January 2023**, ahead of the US which reached T+1 only in May 2024 — cuts systemic risk and frees capital faster. But going instantly to T+0 for everything is not costlessly better. First, **netting efficiency collapses**: instant settlement means gross, trade-by-trade movement, so you lose the 90%+ netting compression and far more liquidity must be pre-funded. Second, **foreign investors and time zones**: FPIs must arrange rupee funding within tight windows, which is operationally hard. So India introduced **T+0 as an optional parallel from March 2024**, not a forced replacement — capturing the risk benefit for those who want it while preserving netting for those who need it.

**C4. "Explain the difference between how India and the US structure share ownership in the depository, and why it matters."**

*Model answer:* India uses a **direct beneficial-owner model**: securities sit in the *investor's own* demat account at NSDL/CDSL, with the investor recorded as beneficial owner at individual level. The US uses the **"street name" model**: DTC holds shares through its nominee **Cede & Co.**, and brokers hold for clients in an omnibus/nominee structure — the US investor is a beneficial owner but not the direct registered holder. It matters because India's model gives cleaner, individual-level transparency and stronger protection: your shares are demonstrably yours and ring-fenced from your broker's failure, whereas the US nominee chain layers broker/DTC intermediation between you and the register. India further hardened this with client-level segregation and upstreaming of client funds to clearing corporations.

**C5. "What is the CCP's safety stack, and how do the pieces fit together?"**

*Model answer:* Three layers in sequence. First, **margins** collected before and during trading: **initial/VaR margin** (SPAN-style, covering the likely worst-case price move), **Extreme Loss Margin** for tail moves, **mark-to-market margin** settling daily gains and losses, plus **peak/upfront margins** that India tightened in 2020–21 so leverage cannot build up intraday. Second, the **Core Settlement Guarantee Fund**, a pre-funded pool from the CCP, exchange and members, sized to survive the default of the largest members under stress. Third, the **default waterfall**, the ordered consumption of resources when a default actually happens. Margin is the frontline that makes most defaults self-covering; the SGF and waterfall are the backstops that keep the guarantee credible in extremis. Together they are why the CCP's promise is believable.

---

## Section D — Multiple-Choice Questions (with reasoning)

**D1. Which institution performs novation and guarantees the trade?**
(a) The stock exchange
(b) The depository
(c) The Clearing Corporation / CCP
(d) The Depository Participant

**Answer: (c).** The Clearing Corporation (NCL for NSE, ICCL for BSE) novates and guarantees. The exchange only matches orders and discovers price; the depository only records electronic ownership; the DP is merely the access point to the depository. In India these are deliberately separate entities.

**D2. Novation means:**
(a) Netting many trades into one net position
(b) Replacing one bilateral contract with two contracts each facing the CCP
(c) Simultaneous exchange of cash and securities
(d) Converting paper certificates to electronic form

**Answer: (b).** Novation legally tears up "B buys from S" and creates "B buys from CCP" and "CCP buys from S." Option (a) is netting, (c) is DvP, and (d) is dematerialisation — all distinct mechanisms.

**D3. Multilateral netting typically reduces gross settlement obligations by roughly:**
(a) 10–20%
(b) 40–50%
(c) 90–98%
(d) It does not reduce them at all

**Answer: (c).** CCP studies routinely show netting compresses gross obligations by about 90–98%, which is why so little money and stock actually has to move relative to gross trading volume. This compression is the core efficiency argument for central clearing.

**D4. Delivery-versus-Payment (DvP) primarily ensures that:**
(a) Trades settle within 24 clock hours
(b) Neither side gives up its leg without receiving the other, simultaneously
(c) The CCP earns the bid-ask spread
(d) Shares are converted to electronic form

**Answer: (b).** DvP locks the securities leg and the cash leg together so they move at once, directly removing first-mover risk. It says nothing about clock hours (that is the settlement cycle), spreads, or dematerialisation.

**D5. India completed its full move to T+1 equity settlement in:**
(a) April 2003
(b) January 2023
(c) May 2024
(d) March 2024

**Answer: (b).** Full T+1 for all stocks was completed in January 2023, making India the first large market to do so. April 2003 was the move to T+2; May 2024 is when the *US* reached T+1; March 2024 is when India launched its optional T+0 beta.

**D6. Which is the correct top-to-bottom order of the CCP default waterfall?**
(a) Non-defaulters' SGF → CCP capital → defaulter's margin
(b) Defaulter's margin → defaulter's SGF → CCP capital → non-defaulters' SGF
(c) CCP capital → defaulter's margin → non-defaulters' SGF
(d) Defaulter's margin → non-defaulters' SGF → CCP capital

**Answer: (b).** Losses eat the defaulter's own margin first, then its SGF contribution, then the CCP's own capital ("skin in the game"), and only then the mutualised non-defaulters' SGF. The ordering makes the defaulter and the CCP absorb losses before innocent members.

**D7. Which statement about India's depositories is correct?**
(a) NSDL serves only NSE and CDSL only BSE
(b) The broker owns and holds the client's shares
(c) Both NSDL and CDSL serve both exchanges; your shares sit in your own demat account
(d) The exchange holds your shares directly

**Answer: (c).** Both depositories serve both exchanges, and shares sit in the investor's own demat account, not the broker's — which protects you if the broker fails. Option (a) is a common myth; (b) and (d) misstate who holds securities.

**D8. Trade-for-trade (gross) settlement is typically imposed on a scrip in order to:**
(a) Increase netting efficiency
(b) Reward high-liquidity blue-chip stocks
(c) Prevent netting from hiding manipulation in surveillance-flagged or illiquid scrips
(d) Speed settlement to T+0

**Answer: (c).** Gross settlement forces every trade to deliver and pay individually, exposing wash or circular trading that netting could disguise. It is a surveillance tool for flagged/illiquid scrips, the opposite of rewarding liquidity, and it removes rather than adds netting efficiency.

**D9. In the Lehman Brothers default, its interest-rate swap portfolio cleared through LCH was managed by:**
(a) Immediately tapping the mutualised default fund, causing member losses
(b) Using Lehman's posted margin to hedge and auction positions, with no surviving member losing money
(c) A government bailout of the CCP
(d) Cancelling all the swaps outright

**Answer: (b).** LCH used Lehman's own margin to hedge and auction the book in an orderly way, without dipping into the mutualised fund — no other member lost money. It is the flagship proof that novation plus margin plus the default waterfall makes central clearing work under real stress.

**D10. The Depositories Act that provides the legal backbone for demat in India was passed in:**
(a) 1992
(b) 1996
(c) 2001
(d) 2013

**Answer: (b).** The Depositories Act, 1996 created the framework; SEBI then made demat compulsory for most listed shares by around 2001. 1992 is the year of the Harshad Mehta scam (and SEBI's statutory empowerment); 2001 is when paper trading was effectively killed, not when the Act was passed.

---

*End of practice bank. Re-attempt Section D from memory after a day; if you can also reproduce the six-step post-trade lifecycle (C1) and the three-way split of clearing / settlement / depository (A2) unprompted, the chapter is secure.*
