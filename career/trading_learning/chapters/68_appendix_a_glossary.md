# Appendix A: Glossary of Options & F&O Terms

A quick-reference dictionary of every important term used in this book — defined in plain English, with India/NSE context where it matters.

## A

**American option** — An option that can be exercised on any trading day up to and including expiry. In India, individual stock options are American-style; index options (Nifty, Bank Nifty, FinNifty) are not.

**Adjustment** — Modifying an existing position (rolling a strike, adding a hedge, converting a spread) to manage risk or repair a losing trade, rather than simply closing it.

**Annualized volatility** — Volatility expressed on a yearly basis so different options can be compared on one scale. Daily standard deviation is scaled up by sqrt(252) (about 252 trading days a year).

**Arbitrage** — A theoretically risk-free profit from a price discrepancy, for example when put-call parity is violated. Real arbitrage is rare and fleeting because pros and algorithms close gaps almost instantly.

**Assignment** — The obligation handed to an option seller (writer) when a buyer exercises. The writer of a call must deliver/settle the underlying; the writer of a put must take/settle it. For NSE stock options this means physical delivery of shares.

**At-the-money (ATM)** — An option whose strike is closest to the current price of the underlying. ATM options carry the most time value and the highest gamma.

**Auto square-off** — A broker's forced closing of your position if margins fall short or near expiry of physically settled contracts you cannot honor. It happens at the market's mercy, often at bad prices, so never rely on it.

## B

**Backspread** — A net-long-options ratio strategy: you sell fewer near-the-money options and buy more farther options (for example sell 1 call, buy 2 higher calls). It profits from a large move and rising volatility, with limited risk if structured for a credit.

**Bank Nifty** — The NSE index of major Indian banking stocks. Its options are among the most actively traded in the world and are more volatile than Nifty, so premiums and risk are larger.

**Barrier option** — An exotic option that activates (knock-in) or extinguishes (knock-out) only if the underlying touches a preset barrier price. Common in structured products, not in standard NSE F&O.

**Basis** — The difference between the futures (or synthetic) price and the spot price of the underlying: `basis = futures - spot`. It reflects cost of carry and converges to zero at expiry.

**Bear call spread** — A credit spread: sell a lower-strike call and buy a higher-strike call. It profits when the market stays flat or falls, with capped risk and reward.

**Bear put spread** — A debit spread: buy a higher-strike put and sell a lower-strike put. It profits from a moderate fall, costing less than a naked long put.

**Bid-ask spread** — The gap between the highest price a buyer will pay (bid) and the lowest a seller will accept (ask). A wide spread is a hidden cost; illiquid far-month or far-OTM NSE strikes can have punishing spreads.

**Binomial model** — A pricing method that models the underlying moving up or down in discrete steps, building a tree of possible prices. With enough steps it converges to Black-Scholes and can handle early exercise (American options).

**Black-Scholes (Black-Scholes-Merton, BSM)** — The classic closed-form formula for pricing European options, using spot, strike, time, interest rate, and volatility. It is the foundation of option theory and of every Greek.

**Breakeven** — The underlying price at which a position makes zero profit/loss at expiry. For a long call: `breakeven = strike + premium`; for a long put: `breakeven = strike - premium`.

**Bull call spread** — A debit spread: buy a lower-strike call and sell a higher-strike call. It profits from a moderate rise, cheaper than a naked long call but with capped upside.

**Bull put spread** — A credit spread: sell a higher-strike put and buy a lower-strike put. It profits when the market stays flat or rises, collecting premium with defined risk.

**Butterfly** — A three-strike, four-option strategy (for example buy 1 low, sell 2 middle, buy 1 high) that profits if the underlying pins near the middle strike at expiry. Cheap, defined-risk, and a bet on low movement.

**Box spread** — A four-leg combination of a bull call spread and a bear put spread that locks in a fixed payoff, used to lend or borrow funds at an implied rate or to exploit mispricing. Largely an arbitrage/financing tool.

**Buy-write** — Buying the underlying and simultaneously writing a call against it — the entry version of a covered call.

## C

**Calendar spread (time spread)** — Selling a near-expiry option and buying a longer-expiry option at the same strike. It profits from faster time decay in the front leg and from rising volatility.

**Call option** — A contract giving the buyer the right (not obligation) to buy the underlying at the strike price by expiry. Payoff at expiry: `max(spot - strike, 0) - premium` for the buyer.

**Cash settlement** — Settling an option in cash (the in-the-money value) rather than delivering the asset. All NSE index options are cash-settled against the closing settlement price.

**Collar** — Holding the underlying, buying a protective put, and selling a call to fund it. It caps both downside and upside — a low-cost hedge for a stock or portfolio.

**Charm (delta decay)** — A second-order Greek measuring how delta changes as time passes. It matters for hedging near expiry, when an option's delta can swing sharply day to day.

**Condor** — A four-strike strategy similar to a butterfly but with two different middle strikes, giving a wider profit zone in exchange for lower peak profit.

**Contract note** — The broker-issued statement detailing each executed trade, charges (brokerage, STT, GST, stamp duty, exchange fees), and net obligation. Your real cost basis.

**Cost of carry** — The net cost of holding a position to expiry — financing cost minus dividends — which drives the basis between futures and spot.

**Covered call** — Owning the underlying and selling a call against it to earn premium income. It caps upside above the strike but cushions small declines; a core income strategy.

**Credit spread** — Any spread entered for a net premium received (sell the pricier option, buy a cheaper protective one). Profit is the credit; risk is capped by the long leg.

## D

**Debit spread** — Any spread entered for a net premium paid (buy the pricier option, sell a cheaper one to lower cost). Risk is capped at the debit; reward is capped too.

**Delta** — The rate of change of an option's price for a 1-point move in the underlying. Calls have delta 0 to +1, puts 0 to -1; delta also roughly approximates the probability of finishing in-the-money.

**Delta-neutral** — A position whose total delta is near zero, so small moves in the underlying barely change its value. Volatility and theta traders hold delta-neutral books and re-hedge as delta drifts.

**Diagonal spread** — A mix of a calendar and a vertical spread: the two legs differ in both strike and expiry. Used to express direction plus a time-decay or volatility view.

**Dividend yield** — Expected dividends as a percentage of the stock price. Higher dividends lower call values and raise put values, and can trigger early exercise of American calls just before the ex-dividend date.

## E

**Early exercise** — Exercising an American option before expiry. Usually only worthwhile for deep ITM puts, or calls just before a large dividend; otherwise you throw away remaining time value.

**Expected move** — The market's implied one-standard-deviation range for the underlying by expiry, roughly `spot * IV * sqrt(days/365)` or approximated by the ATM straddle price. It frames how far a move is "priced in."

**European option** — An option exercisable only at expiry, not before. All NSE index options are European, which makes them cleanly priceable by Black-Scholes.

**Exercise** — Invoking the right in an option contract to buy (call) or sell (put) at the strike. For cash-settled index options this just means receiving the in-the-money amount in cash.

**Expiry (expiration)** — The last day an option is valid. NSE index options have weekly and monthly expiries; after expiry an option is settled and ceases to exist.

**Exposure margin** — An extra margin on top of SPAN that the exchange/broker charges as a buffer against gap risk on short option/futures positions.

**Extrinsic value (time value)** — The part of an option's premium above its intrinsic value, reflecting time remaining and volatility: `extrinsic = premium - intrinsic`. It decays to zero at expiry.

## F

**FinNifty (Nifty Financial Services)** — An NSE index of financial-sector stocks (banks, NBFCs, insurers). Its options are European and cash-settled, popular for shorter-dated expiry trades.

**Futures** — A standardized contract to buy/sell the underlying at a set price on a future date. Options are often priced and hedged against the corresponding future rather than spot.

## G

**Gamma** — The rate of change of delta for a 1-point move in the underlying — the "acceleration" of an option. Gamma is highest for ATM, near-expiry options; long options have positive gamma, short options negative.

**Gamma scalping** — Continuously re-hedging a long-gamma, delta-neutral position by buying low and selling high as the underlying swings, harvesting realized volatility to offset theta paid.

**Greeks** — The set of sensitivities measuring how an option's price responds to its inputs: delta, gamma, theta, vega, rho (first order) and vanna, volga, charm and others (higher order).

## H

**Hedge** — A position taken to reduce the risk of another position, for example buying a put to protect a stock holding. Hedging trades some upside or pays a premium to limit downside.

**Historical volatility (realized volatility)** — How much the underlying has actually moved in the past, measured as the annualized standard deviation of returns. Compare it to implied volatility to judge if options are cheap or dear.

## I

**Implied volatility (IV)** — The volatility figure that, plugged into a pricing model, reproduces an option's current market price. It is the market's forecast of future movement and the single most important traded input.

**India VIX** — NSE's volatility index, derived from Nifty option prices, expressing expected 30-day annualized volatility as a percentage. A rising India VIX signals fear and pumps up option premiums.

**In-the-money (ITM)** — An option with intrinsic value: a call whose strike is below spot, or a put whose strike is above spot.

**Intrinsic value** — The immediate exercise value of an option: `max(spot - strike, 0)` for a call, `max(strike - spot, 0)` for a put. It can never be negative.

**Iron butterfly** — Selling an ATM straddle and buying protective wings (a higher call and lower put). A defined-risk, premium-collecting bet that the underlying pins near the center strike.

**Iron condor** — Selling an OTM put spread and an OTM call spread together. It profits when the underlying stays in a range, with capped risk on both sides — a popular range-bound income trade.

**IV rank** — Where current IV sits between its 52-week low and high, scaled 0 to 100: `IV rank = (IV - IV_low) / (IV_high - IV_low) * 100`. High rank suggests options are relatively expensive.

**IV percentile** — The fraction of days over the past year that IV was below today's level. Unlike IV rank, it is not distorted by a single extreme spike.

## L

**LEAPS** — Long-dated options (typically a year or more to expiry). Rare and illiquid in the Indian retail market, which centers on weekly and monthly contracts.

**Leg** — One individual option (or future) within a multi-part strategy. A spread has two legs; an iron condor has four.

**Liquidity** — How easily a contract can be traded without moving its price, shown by tight bid-ask spreads and high volume/open interest. Nifty and Bank Nifty ATM weeklies are extremely liquid; far strikes and far months are not.

**Lognormal distribution** — The standard assumption for terminal underlying prices: returns are normally distributed, so prices are lognormal (cannot go below zero, with a long upside tail). It underlies Black-Scholes probabilities.

**Long** — Holding a bought position that gains when the asset (or option) rises in value. "Long a call" means you own a call.

**Lot size** — The fixed number of units in one F&O contract, set by NSE (for example Nifty about 75, Bank Nifty about 35 — these change over time). You can only trade in whole-lot multiples.

**LTP (last traded price)** — The price at which an option (or any security) most recently changed hands. For thinly traded strikes the LTP can be stale and misleading versus the live bid-ask.

## M

**Margin** — Cash/collateral you must keep with the broker to hold a position. Option buyers pay only the premium; option sellers post margin (SPAN plus exposure) because their risk is open-ended.

**Mark-to-market (MTM)** — Revaluing open positions at current market prices each day, with gains/losses credited or debited to your account. It is why short F&O positions can trigger margin calls intraday even before expiry.

**Max pain** — The strike at which the largest rupee value of options would expire worthless, theoretically the price that causes maximum loss to option buyers. A widely watched but unreliable expiry-day signpost.

**Margin (peak)** — SEBI's intraday rule requiring brokers to collect margin based on the highest exposure during the day (peak margin snapshots), preventing excessive intraday leverage.

**Moneyness** — How far an option's strike is from the current underlying price, classifying it as ITM, ATM, or OTM. It largely determines an option's delta and how much of its premium is intrinsic.

**Monte Carlo simulation** — A pricing/risk method that simulates thousands of random price paths for the underlying and averages the resulting payoffs. Useful for exotic and path-dependent options where no formula exists.

## N

**Naked option (uncovered)** — A short option with no offsetting position or hedge. A naked short call has theoretically unlimited risk; a naked short put risks the strike falling to zero — both demand large margin and respect.

**Nifty 50** — NSE's flagship index of 50 large Indian companies. Its weekly and monthly options are the most-traded, most-liquid derivatives in the Indian market.

**Notional value** — The total underlying value a contract controls: `notional = lot size * number of lots * underlying price`. It shows true exposure, which dwarfs the premium or margin paid.

## O

**Open interest (OI)** — The total number of outstanding (not-yet-closed) contracts at a strike. Rising OI with price confirms a trend; OI clusters mark support/resistance and likely pinning levels.

**Option chain** — The exchange table listing all available strikes for an expiry with their call and put prices, OI, volume, and IV. The trader's primary dashboard for picking strikes.

**Out-of-the-money (OTM)** — An option with no intrinsic value: a call whose strike is above spot, or a put whose strike is below spot. OTM options are all time value and expire worthless if they stay OTM.

## P

**Payoff diagram** — A graph of a position's profit/loss against the underlying price at expiry. The essential tool for visualizing the risk and reward of any strategy before you trade it.

**Peak margin** — See Margin (peak).

**Physical settlement** — Settling by actual delivery of shares rather than cash. NSE stock (not index) options that stay ITM at expiry are physically settled, so unwanted delivery and large margin can surprise the careless.

**Pin risk** — The danger near expiry when the underlying sits right at a short strike, leaving the seller unsure whether they will be assigned. It is mainly a stock-option (physically settled) hazard; cash-settled index options avoid it.

**Premium** — The price paid by the buyer and received by the seller for an option. It equals intrinsic value plus extrinsic (time) value and is quoted per unit but paid per lot.

**Probability of profit (POP)** — The estimated chance a trade finishes profitable at expiry, read off the lognormal price distribution. Credit strategies often have high POP but poor risk-reward; the two must be weighed together.

**Protective put** — Buying a put against an existing long position to insure against a fall. It sets a floor on losses while keeping upside, at the cost of the premium paid.

**Put option** — A contract giving the buyer the right (not obligation) to sell the underlying at the strike by expiry. Buyer payoff at expiry: `max(strike - spot, 0) - premium`.

**Put-call parity** — The fundamental no-arbitrage relationship linking a call, a put, the underlying, and a bond: `call - put = spot - strike * e^(-r*T)` (for European options). It lets you build synthetics and check fair pricing.

## R

**Ratio spread** — Buying and selling unequal numbers of options at different strikes (for example buy 1, sell 2). It can be cheap or a credit, but the extra short leg adds open-ended risk past a point.

**Realized volatility** — See Historical volatility.

**Rho** — The sensitivity of an option's price to a 1% change in the risk-free interest rate. It is the smallest Greek for the short-dated options dominating Indian trading and is usually ignored.

**Risk reversal** — Selling an OTM put and buying an OTM call (or vice versa) to take a directional view cheaply or for a credit. Its price difference also measures volatility skew between puts and calls.

**Risk-free rate** — The interest rate on a safe asset (in India, proxied by T-bill or repo rates) used to discount strikes in option pricing. A model input, not something you trade.

**Rolling** — Closing a near-expiry option and reopening a similar one in a later expiry (or different strike) to extend or adjust a trade. "Rolling up/down/out" shifts strike or time.

## S

**Settlement price** — The official exchange-determined price used to settle contracts at expiry. NSE settles index options against the average of Nifty/Bank Nifty over the last half hour of the expiry day.

**Short** — Holding a sold position that gains when the asset (or option) falls in value or decays. "Short a put" means you wrote/sold a put and carry its obligation.

**Skew (volatility skew)** — The pattern where IV differs across strikes, typically higher for downside puts than upside calls because crashes are feared. It tells you the market's asymmetric risk pricing.

**Smile (volatility smile)** — The U-shaped curve of IV across strikes, with OTM options on both sides pricing higher IV than ATM. Equity indices usually show a one-sided "smirk" (skew) rather than a symmetric smile.

**SPAN margin** — The core portfolio margin (Standardized Portfolio Analysis of Risk) NSE charges on short F&O positions, computed by stress-testing the position across price and volatility scenarios.

**Spot** — The current cash-market price of the underlying (the live Nifty/Bank Nifty level), as opposed to its futures or option price.

**Spread** — Any position combining two or more options of the same type to define and cap risk, such as vertical, calendar, or diagonal spreads. The building block of most professional strategies.

**Straddle** — Buying (or selling) a call and a put at the same strike and expiry. A long straddle profits from a big move either way; a short straddle profits from the underlying staying still.

**Strangle** — Buying (or selling) an OTM call and an OTM put at different strikes. Cheaper than a straddle for the buyer and a wider profit range for the seller, but needs a larger move to pay off when long.

**Strike (exercise price)** — The fixed price at which an option can be exercised. NSE lists a ladder of strikes around spot at regular intervals for every expiry.

**STT (Securities Transaction Tax)** — A government tax on F&O trades. It is charged on the premium when options are sold/traded and, importantly, on the full intrinsic value if an option is exercised — a trap that makes letting deep-ITM options expire costly.

**Synthetic** — A position built from options (and/or the underlying) that replicates another instrument's payoff, for example a synthetic long stock = long call + short put at the same strike. Synthetics flow directly from put-call parity.

## T

**Term structure (of volatility)** — How implied volatility varies across expiries for the same underlying. Normally upward-sloping; it can invert before known events (results, budget, elections) when near-term IV spikes.

**Theta** — The rate at which an option loses value as one day passes, all else equal — time decay. Theta is negative for buyers (a daily cost) and positive for sellers (daily income), and accelerates near expiry for ATM options.

**Theta decay** — The erosion of an option's time value as expiry approaches; another name for the effect measured by theta. It is non-linear, speeding up sharply in the final days of weekly options.

**Time decay** — See Theta decay.

**Time value** — See Extrinsic value.

**Time spread** — See Calendar spread.

## U

**Underlying** — The asset an option derives its value from — the index (Nifty, Bank Nifty, FinNifty) or stock on which the contract is written.

## V

**Vanna** — A second-order Greek: how delta changes when volatility moves (equivalently, how vega changes when spot moves). It matters for skew trading and for hedging large option books.

**Vega** — The change in an option's price for a 1-point (1%) change in implied volatility. Long options are long vega (gain when IV rises); ATM, longer-dated options have the most vega.

**Vertical spread** — A spread using two options of the same type and expiry but different strikes (bull/bear, call/put). The basic defined-risk directional structure.

**Volatility** — A measure of how much the underlying's price fluctuates, the lifeblood of option value. It comes in two flavors: realized (historical) and implied (forward-looking).

**Volatility surface** — The full three-dimensional map of implied volatility across both strike and expiry. It combines skew/smile and term structure into one picture pros use to price and hedge.

**Volga (vomma)** — A second-order Greek: how vega changes as volatility changes — the convexity of an option to volatility. Important when trading options on volatility itself.

**Volume** — The number of contracts traded in a period. Together with open interest, it gauges liquidity and the strength of a price move.

## W

**Wing** — A protective long option bought at a far strike to cap the risk of a short option, as in the "wings" of an iron condor or iron butterfly. Wider wings mean more credit but larger maximum loss.

**Writer** — The seller of an option, who receives the premium and takes on the obligation to deliver/settle if assigned. Writing options earns theta but carries large (sometimes unlimited) risk, which is why most retail F&O losses come from mismanaged short options.
