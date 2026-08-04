# Q&A — Market Participants & Intermediaries

Theory and worked scenarios on the ecosystem of issuers, investors, and intermediaries.

---

### Q1. Map a single institutional trade through every intermediary it touches, and state each one's distinct role.

**Model answer.** A mutual fund (investor) instructs its broker (execution intermediary) to buy shares on the NSE (exchange, provides the matching venue and price discovery); the trade is guaranteed by the clearing corporation (central counterparty); the depository (NSDL/CDSL) transfers the shares in demat form into the fund's custodian's account (safekeeping/settlement support for institutions) on T+1. Five distinct intermediaries, each solving a different friction: distribution/execution, matching, counterparty guarantee, custody/transfer, and institutional safekeeping.

---

### Q2. Why does the composition of a stock's investor base (retail vs FPI vs DII vs promoter) matter to an analyst forecasting volatility?

**Model answer.** Different investor types have different horizons and reaction speeds: FPIs can move large sums quickly in response to global risk sentiment or currency moves, amplifying volatility; DIIs (insurers, pension funds) tend to be longer-horizon and more stable, often acting as a stabilising counterweight; promoters are typically long-term, control-oriented holders. A stock heavily held by fast-moving FPIs will react more sharply to negative headlines than an otherwise-similar stock dominated by patient domestic institutional holders — the holder-base composition is itself a volatility signal, independent of the company's fundamentals.

---

### Q3. Distinguish the roles of an exchange, a clearing corporation, and a depository — a classic three-way confusion trap.

**Model answer.** The exchange (NSE/BSE) provides the trading platform and matches buy/sell orders — price discovery happens here. The clearing corporation becomes the central counterparty to every matched trade, guaranteeing settlement so neither party bears the other's default risk. The depository (NSDL/CDSL) holds securities in dematerialised form and physically executes the transfer of ownership. A common interview trap is treating any two of these as interchangeable — each solves a genuinely distinct friction (matching vs guaranteeing vs custody/transfer).

---

### Q4. What's the difference between sell-side and buy-side, and where would a candidate coming from a trading/derivatives background naturally fit?

**Model answer.** Sell-side firms (investment banks, brokers) create products, execute trades, and publish research to win and service client business — their research and trading desks are ultimately commercial functions serving external clients. Buy-side firms (asset managers, mutual funds, hedge funds, pension funds) invest their own or client capital directly, consuming sell-side research as one input among many to make investment decisions. A candidate with direct trading/derivatives desk experience (as opposed to client-facing sales or research-publishing experience) often has skills that map most naturally to buy-side execution/trading roles or to sell-side trading desks, as distinct from sell-side equity research roles, which screen more for the research/writing/client-communication skill set.

---

### Q5. What does SEBI actually regulate, concretely, across issuers, intermediaries, and markets?

**Model answer.** For issuers: disclosure requirements (prospectus content, ongoing reporting, related-party transaction rules). For intermediaries: registration and conduct standards (brokers, merchant bankers, investment advisers must be SEBI-registered and follow conduct codes). For markets: surveillance against insider trading and price manipulation, oversight of exchanges and clearing corporations, and setting rules like circuit breakers and margin requirements. The unifying purpose across all three is investor protection and market integrity — a useful one-line answer is that SEBI's job is to make sure information is disclosed fairly, intermediaries behave honestly, and market mechanics can be trusted.

---

### Q6. Worked scenario — how would surveillance likely detect the insider-trading pattern in this case, and what happens next?
*A promoter sells a large block of shares three days before the company announces disappointing earnings, having had no prior pattern of similar sales.*

**Model answer.** SEBI's surveillance systems flag unusual trading patterns ahead of price-sensitive announcements — specifically, a departure from an individual's established trading behaviour (no prior pattern of large sales) combined with timing that precedes a material negative disclosure is a classic red flag pattern. This typically triggers an investigation (examining trading records, communications, and access to the pre-announcement information), and if insider trading is substantiated, results in penalties (fines, trading bans, potential criminal referral) — the broader function this serves is preserving the market's trust that prices reflect fairly available information, which is what keeps outside investors willing to participate.

---

### Q7. What's the difference between a custodian and a broker, and why might an institutional investor use both?

**Model answer.** A broker executes trading instructions (buy/sell orders) on the investor's behalf. A custodian safekeeps the institution's assets, handles settlement mechanics on the institution's side, and often provides additional services (corporate action processing, reporting, fund administration support). An institutional investor typically uses a broker for execution and a separate custodian for safekeeping and back-office settlement — this separation (rather than one entity doing both) is itself a risk-management practice, reducing the concentration of control over both trade execution and asset custody in a single counterparty.

---

### Q8. Why do RTAs (Registrars & Transfer Agents) matter to a retail shareholder, even though most investors never interact with one directly?

**Model answer.** RTAs maintain the official record of shareholding and process corporate actions (dividend payments, rights/bonus share credits, name/address changes, dematerialisation requests) on behalf of the issuing company — even though a retail investor's day-to-day interaction is with their broker/demat account, the RTA is the entity that ultimately ensures corporate-action entitlements (a declared dividend, a bonus share) are correctly credited to the right shareholder of record, making it a quietly essential piece of infrastructure behind every corporate action an investor experiences.
