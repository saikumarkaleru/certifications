# Appendix C: Options Question Bank (130+ Q&A)

These are practice interview questions with model answers, spanning beginner fundamentals to advanced exotics and rate/FX derivatives. Formulas are written in plain text.

## Fundamentals

**Q1.** What is a call option versus a put option, and who holds the right versus the obligation?

A call gives the buyer the RIGHT (not obligation) to BUY the underlying at the strike K; a put gives the buyer the right to SELL at K. The option BUYER holds the right and pays a premium; the option SELLER (writer) receives the premium and takes on the OBLIGATION to deliver (call) or buy (put) if exercised. So buyers have limited loss (premium) and sellers have limited gain (premium) but potentially large loss.

**Q2.** What does "long" versus "short" a position mean, and what are the four basic option positions?

Long means you bought/own it; short means you sold/wrote it. The four positions are: long call (bullish, pay premium), short call (bearish/neutral, receive premium), long put (bearish, pay premium), short put (bullish/neutral, receive premium). Long positions have the rights; short positions carry the obligations and the margin requirement.

**Q3.** What is the payoff of a long call at expiry, and write the formula?

Payoff = max(S_T - K, 0), where S_T is the spot at expiry and K the strike. Profit = max(S_T - K, 0) - premium. Example: Nifty call K = 22000 bought for 150; if Nifty expires at 22300, payoff = 300, profit = 300 - 150 = 150 per unit.

**Q4.** What is the payoff of a long put at expiry?

Payoff = max(K - S_T, 0). Profit = max(K - S_T, 0) - premium. Example: a TCS 3800 put bought for 60; if TCS expires at 3700, payoff = 100 and profit = 100 - 60 = 40 per share. A put gains value as the underlying falls, capped because price cannot go below zero.

**Q5.** What are the payoffs to the option WRITER (short call and short put)?

Short call payoff = -max(S_T - K, 0); short put payoff = -max(K - S_T, 0). The writer keeps the premium if the option expires worthless. Profit (short call) = premium - max(S_T - K, 0); a naked short call has theoretically unlimited loss, while a short put's max loss is K - premium (if the stock goes to zero).

**Q6.** Define intrinsic value and time value of an option.

Intrinsic value is the in-the-money amount if exercised now: call = max(S - K, 0), put = max(K - S, 0). Time value = option premium - intrinsic value, reflecting the chance of moving further ITM before expiry. Example: stock 105, call K = 100 priced 8: intrinsic = 5, time value = 3. Time value decays to zero at expiry (theta decay).

**Q7.** Explain moneyness (ITM/ATM/OTM) for calls and puts.

For a call: ITM when S > K, ATM when S ~ K, OTM when S < K. For a put it reverses: ITM when S < K, OTM when S > K. ITM options have intrinsic value; ATM/OTM options are pure time value. Example: spot 100 — the 95 call is ITM, the 100 call ATM, the 105 call OTM; the 105 put is ITM and the 95 put OTM.

**Q8.** What is the difference between a payoff diagram and a profit diagram?

A payoff diagram plots the value at expiry (ignoring cost), so a long call's payoff is a hockey stick that is flat at zero up to K then slopes up at 45 degrees. A profit diagram subtracts the premium paid (or adds premium received), shifting the line down by the premium, so breakeven for a long call is at K + premium, not K. Profit accounts for the upfront cost; payoff does not.

**Q9.** What is the breakeven point for a long call and a long put?

Long call breakeven = K + premium (stock must rise enough to recover the premium). Long put breakeven = K - premium. Example: 22000 Nifty call at 150 breaks even at 22150; 22000 put at 130 breaks even at 21870. Below/above breakeven respectively the buyer is still net negative even if the option is ITM.

**Q10.** What are the main drivers of an option premium?

Six drivers (Black-Scholes inputs): underlying price S, strike K, time to expiry T, volatility sigma, risk-free rate r, and dividends/yield q. Calls rise with S, T, sigma and r, and fall with q; puts rise with K, T, sigma and q, and fall with r. Volatility and time are the key "time value" drivers — higher sigma or more time means more premium for both calls and puts.

**Q11.** Why does higher volatility increase BOTH call and put premiums?

Options have asymmetric payoffs (limited downside, open upside), so a wider distribution of S_T raises the expected payoff of the optionality without a matching penalty. Higher sigma fattens the tails, increasing the probability of finishing deep ITM, while the OTM side is already floored at zero. This is captured by positive vega for both calls and puts.

**Q12.** What is the difference between American and European exercise style?

American options can be exercised any time up to expiry; European options only at expiry. American options are worth at least as much as European (more flexibility). In India, both index options (Nifty, Bank Nifty) AND single-stock options on NSE are European-style; US equity options are typically American, while US index options like SPX are European.

**Q13.** When is it ever optimal to early-exercise an American option?

For a non-dividend-paying stock, an American CALL is never optimally exercised early (you forgo time value and interest on K) — so it equals a European call. American PUTS can be optimal to exercise early (deep ITM, to receive K and earn interest). Early call exercise becomes rational just before a large dividend, to capture the dividend.

**Q14.** State the put-call parity relationship and explain each term.

For European options: C - P = S - K*e^(-r*T), where C and P are call and put prices on the same K and T, S is spot, r the risk-free rate. It says a long call plus short put (same strike) replicates a forward on the stock. Rearranged: C + K*e^(-r*T) = P + S (fiduciary call = protective put). With a dividend yield q, replace S with S*e^(-q*T).

**Q15.** Use put-call parity to value a missing option: S = 100, K = 100, r = 6%, T = 0.5, call = 7. Find the put.

P = C - S + K*e^(-r*T) = 7 - 100 + 100*e^(-0.06*0.5) = 7 - 100 + 100*0.9704 = 7 - 100 + 97.04 = 4.04. The put is worth about 4.04. The call exceeds the put here because the present-valued strike (97.04) is below spot, reflecting the interest carry benefit to the call holder.

**Q16.** How do you build a synthetic forward (or synthetic long stock) using options?

Synthetic long forward = long call + short put at the same strike K and expiry; its payoff is S_T - K, identical to a forward. Synthetic long stock today = long call + short put + invest K*e^(-r*T) in bonds. Conversely synthetic short stock = short call + long put. These follow directly from put-call parity C - P = S - K*e^(-r*T).

**Q17.** What does Indian regulation say about exercise style and how does it affect parity?

SEBI/NSE moved all equity (single-stock) options to European style years ago, and index options were always European, so standard European put-call parity C - P = S - K*e^(-r*T) holds cleanly in India. Because Indian stock options are physically settled, the parity should also account for any expected dividend (use S*e^(-q*T)) and the cost of holding/borrowing the stock to deliver.

**Q18.** What is a covered call versus a naked call?

A covered call is writing a call while owning the underlying stock — the stock covers the delivery obligation, capping upside but earning premium income. A naked (uncovered) call is writing a call without owning the stock, exposing the writer to theoretically unlimited loss and requiring large margin. Covered calls are an income/yield strategy; naked calls are pure short-volatility bets.

**Q19.** What is the difference between exercise and assignment?

Exercise is the option holder (long) choosing to invoke their right to buy/sell at K. Assignment is when the clearing corporation (e.g., NSE Clearing) selects a short option holder to fulfil that obligation. Assignment is usually random across writers; an in-the-money option at expiry is auto-exercised, triggering assignment to a writer who must then deliver or take delivery.

**Q20.** What is the difference between open interest and volume?

Volume is the number of contracts traded during the day (resets daily). Open interest (OI) is the total number of contracts currently open/outstanding (not yet closed or expired). OI rises when a new buyer and new seller create a contract and falls when both close. Rising price with rising OI suggests a strengthening trend; rising price with falling OI suggests short covering.

**Q21.** How do futures differ from forwards?

Futures are exchange-traded, standardized, marked-to-market daily, and guaranteed by a clearinghouse with margin — minimizing counterparty risk. Forwards are OTC, customized, settled at maturity, and carry counterparty/credit risk with no daily cash flows. Because of daily settlement, futures have small convexity differences from forwards, but for short maturities and low rate-correlation they are treated as equal in price.

**Q22.** What is the cost-of-carry fair value of a future/forward? Give the formula.

F = S*e^((r - q)*T) for continuous compounding, where r is the risk-free rate, q the dividend yield (or convenience yield for commodities), and T the time to expiry. For commodities with storage cost u: F = S*e^((r + u - y)*T), y = convenience yield. Example: S = 22000 Nifty, r = 6%, q = 1.5%, T = 0.25: F = 22000*e^(0.045*0.25) = 22000*1.0113 = 22249.

**Q23.** What is contango versus backwardation?

Contango is when futures price is above spot (F > S), the normal state when carry cost (r) exceeds yield (q) — the curve slopes upward. Backwardation is F < S, common when convenience yield or dividends exceed financing cost, or with supply tightness. As expiry approaches, the basis converges to zero, so futures pull toward spot.

**Q24.** Define basis and basis risk.

Basis = spot price - futures price (some texts use futures - spot; be consistent). At expiry basis converges to zero. Basis risk is the risk that the basis changes unpredictably before you close a hedge, so the hedge does not perfectly offset the cash position — it arises when the hedging instrument, location, or maturity does not exactly match the exposure. Example: hedging jet fuel with crude futures leaves basis risk from the fuel-crude spread.

**Q25.** How do you hedge an equity portfolio with index futures using beta? Give the contract formula.

Number of contracts = beta * (Portfolio value) / (Futures price * lot multiplier). Going SHORT that many index futures neutralizes market risk. Example: INR 1 crore portfolio, beta 1.2, Nifty future 22000, lot 50, contract value = 22000*50 = 11,00,000; contracts = 1.2*1,00,00,000 / 11,00,000 = 10.9, so short about 11 contracts.

**Q26.** How do you change a portfolio's beta (not fully hedge) using index futures?

Contracts = (beta_target - beta_current) * Portfolio value / (Futures price * lot multiplier). A positive result means buy futures (raise beta), negative means sell (lower beta). Example: move beta from 1.0 to 0.5 on a INR 1 crore book, Nifty future contract value 11,00,000: contracts = (0.5 - 1.0)*1,00,00,000/11,00,000 = -4.5, so short ~5 contracts.

**Q27.** What is the minimum-variance hedge ratio for a futures hedge?

h* = correlation(spot, futures) * (sigma_spot / sigma_futures) = covariance(spot returns, futures returns) / variance(futures returns). It is the slope of regressing spot price changes on futures price changes, minimizing variance of the hedged position. Number of contracts = h* * (size of exposure) / (futures contract size); for a portfolio this h* effectively equals the beta versus the index.

**Q28.** What are initial margin and maintenance margin, and what triggers a margin call?

Initial margin is the deposit required to open a futures position; maintenance margin is the lower threshold the balance must stay above. As positions are marked-to-market daily, losses reduce the margin account; if it falls below maintenance, a margin call requires topping up back to the initial margin. Example: initial 1,00,000, maintenance 75,000 — if MTM losses drop the balance to 70,000, you must add 30,000.

**Q29.** What is SPAN margin in the Indian F&O market?

SPAN (Standard Portfolio Analysis of Risk) is the system used by NSE/exchanges to compute the worst-case one-day loss of a portfolio across price and volatility scenarios, setting the initial margin. Total upfront margin = SPAN margin + Exposure margin (an additional buffer). SPAN nets risk across a portfolio (e.g., a hedged spread needs far less margin than two outright positions).

**Q30.** What are typical lot sizes and expiries for Nifty and Bank Nifty derivatives?

Lots are exchange-defined and revised periodically — Nifty is commonly 25 (revised from 50/75 over time) and Bank Nifty around 15-35; always check the current NSE circular. Index options had weekly and monthly expiries, though SEBI has rationalized to fewer weekly expiries (one benchmark weekly per exchange) plus monthly contracts that expire on a designated weekday. Stock F&O are monthly only.

**Q31.** What is physical versus cash settlement, and how does India apply it?

Cash settlement pays the net difference in cash at expiry; physical settlement requires actual delivery of the underlying. In India, all single-stock F&O (futures and options) are PHYSICALLY settled — ITM stock options and stock futures held to expiry result in delivery obligations and full contract-value funds/shares. Index derivatives (Nifty, Bank Nifty) are CASH settled against the settlement value, since you cannot deliver an index.

## Pricing & Black-Scholes

**Q32.** What does the Black-Scholes-Merton (BSM) model do, and who is it for?

BSM gives a closed-form fair value for a European option on a non-dividend-paying stock, derived in 1973 by Black, Scholes and Merton. Its central insight is that an option can be perfectly replicated by a continuously rebalanced portfolio of the stock and a risk-free bond, so by no-arbitrage the option must cost the same as that replicating portfolio. This removes any need to know investor risk preferences or the stock's expected return, which is why it became the foundation of modern derivatives pricing.

**Q33.** List the core assumptions behind BSM.

The key assumptions are: (1) stock prices follow geometric Brownian motion, so log returns are normally distributed and prices are lognormal; (2) volatility sigma is constant and known; (3) the risk-free rate r is constant and known; (4) no arbitrage opportunities exist; (5) trading is continuous and the stock is perfectly divisible; (6) no transaction costs or taxes; (7) the option is European (exercise only at expiry); and (8) no dividends in the base model (Merton later relaxed this). Most real-world deviations from BSM trace back to one of these assumptions failing.

**Q34.** Write the BSM formula for a European call.

C = S*N(d1) - K*e^(-r*T)*N(d2), where d1 = (ln(S/K) + (r + 0.5*sigma^2)*T) / (sigma*sqrt(T)) and d2 = d1 - sigma*sqrt(T). Here S is spot, K is strike, T is time to expiry in years, r is the continuously-compounded risk-free rate, sigma is annualized volatility, and N() is the standard normal cumulative distribution function (CDF). The call value is the discounted expected payoff under the risk-neutral measure.

**Q35.** What is the BSM formula for a European put?

P = K*e^(-r*T)*N(-d2) - S*N(-d1), using the same d1 and d2 as the call. Equivalently you can get it from put-call parity: P = C - S + K*e^(-r*T). Both routes give the identical price, since BSM is internally consistent with no-arbitrage parity.

**Q36.** What does "lognormal prices" mean and why does BSM assume it?

It means the stock price S_T at any future date is lognormally distributed, i.e. ln(S_T) is normally distributed. This follows from modeling returns as dS/S = mu*dt + sigma*dW, geometric Brownian motion, where percentage changes (not absolute changes) are random and normally distributed. Lognormality conveniently keeps prices strictly positive and makes the expected payoff integral solvable in closed form.

**Q37.** Interpret N(d2) in the BSM call formula.

N(d2) is the risk-neutral probability that the call finishes in-the-money, i.e. the probability that S_T > K under the risk-neutral measure. The term K*e^(-r*T)*N(d2) is therefore the present value of paying the strike, weighted by the chance you actually exercise. It is a risk-neutral probability, not the real-world probability, because it uses r rather than the true expected return.

**Q38.** Interpret N(d1) in the BSM call formula.

N(d1) is the option's delta — the sensitivity of the call price to the stock — and the term S*N(d1) is the present value of receiving the stock conditional on exercise. More technically N(d1) is the risk-neutral expected value of S_T given finishing ITM, discounted and divided by S. Loosely, N(d1) tells you how many shares to hold to hedge, while N(d2) is the exercise probability.

**Q39.** Why does BSM use the risk-free rate r instead of the stock's real expected return?

Because the option is priced by replication/hedging, not by forecasting. A delta-hedged option position is locally riskless, so it must earn the risk-free rate to avoid arbitrage; the stock's true drift mu cancels out of the pricing equation entirely. This is the essence of risk-neutral valuation: we discount the expected payoff computed under a measure where every asset drifts at r.

**Q40.** What is risk-neutral valuation in one sentence?

Price any derivative as the expected value of its payoff computed under the risk-neutral probability measure (where all assets grow at r), discounted back at the risk-free rate: Price = e^(-r*T) * E_Q[payoff]. It works because of no-arbitrage and replication, and it sidesteps the need to estimate risk premia or real-world drift.

**Q41.** How does Merton's dividend adjustment change the formula?

For a stock paying a continuous dividend yield q, replace S with S*e^(-q*T) everywhere. So C = S*e^(-q*T)*N(d1) - K*e^(-r*T)*N(d2), with d1 = (ln(S/K) + (r - q + 0.5*sigma^2)*T)/(sigma*sqrt(T)). Intuitively dividends leak value out of the stock you would receive on exercise, so the call is worth less and the put more. The same q-adjustment is used to price index options (where q is the index dividend yield) and, via cost-of-carry, FX and futures options.

**Q42.** Describe the Cox-Ross-Rubinstein (CRR) binomial model.

CRR discretizes time into N steps where each step the stock moves up by factor u = e^(sigma*sqrt(dt)) or down by d = 1/u, with risk-neutral up-probability p = (e^(r*dt) - d)/(u - d). You build the price tree forward, then discount expected payoffs backward step by step at the risk-free rate. It is flexible enough to price American options and discrete dividends, which closed-form BSM cannot handle directly.

**Q43.** How does the binomial model relate to BSM?

As the number of steps N goes to infinity (dt -> 0), the CRR binomial price converges to the BSM price for a European option — the discrete lognormal tree approaches continuous geometric Brownian motion. CRR is essentially a numerical scheme that, in the limit, reproduces the closed-form BSM value. This convergence is why binomial trees are taught as the intuitive bridge to BSM.

**Q44.** Why can't BSM price American options directly, and how is it handled?

BSM assumes European exercise (only at expiry), but American options can be exercised early, adding an optimal-stopping decision BSM's formula ignores. American puts (and calls on dividend-paying stocks) can be worth exercising early, so they need numerical methods — binomial/trinomial trees, finite differences, or least-squares Monte Carlo. Note an American call on a non-dividend stock is never optimally exercised early, so it equals its European value (and BSM applies).

**Q45.** What is the volatility smile/skew, and why does it contradict BSM?

BSM assumes a single constant sigma, which would imply identical implied vol across all strikes. In reality, plotting implied vol against strike shows a smile or (for equity indices) a downward skew, with OTM puts priced at higher implied vols. This reflects fat tails and crash fear — markets price more probability into extreme down-moves than the lognormal assumption allows — directly violating BSM's constant-vol and lognormal assumptions.

**Q46.** Name the main situations where BSM breaks down in practice.

BSM struggles with: (1) American early exercise (needs trees/numerical methods); (2) fat tails and jumps — real returns have more extreme moves than lognormal predicts; (3) the volatility smile/skew — vol is not constant across strikes; (4) stochastic and time-varying volatility; (5) transaction costs and discrete (not continuous) hedging; and (6) discrete dividends and changing rates. Practitioners patch these with local/stochastic-vol models, jump-diffusion, and implied-vol surfaces.

**Q47.** State put-call parity and how it constrains the Greeks of calls and puts.

Put-call parity is C - P = S*e^(-q*T) - K*e^(-r*T) (or C - P = S - K*e^(-r*T) with no dividends). Differentiating gives Greek relationships: call_delta - put_delta = e^(-q*T) (so for q=0, delta_call - delta_put = 1); gamma and vega are identical for a matched call and put; and theta/rho differ only by the derivatives of the deterministic parity terms. This is why a call and put on the same strike/expiry share their gamma and vega exposures exactly.

**Q48.** What is geometric Brownian motion and why is it the standard model for stock prices?

Geometric Brownian motion (GBM) models the stock as the SDE dS = mu*S*dt + sigma*S*dW, where mu is the drift (expected return), sigma the volatility, and dW the increment of a Wiener process. It is "geometric" because returns rather than absolute price levels are random: dividing by S gives dS/S = mu*dt + sigma*dW, so percentage moves are stationary. This is preferred because it keeps prices strictly positive and produces lognormal prices with proportional volatility, matching how equity returns actually behave; it is the engine behind Black-Scholes.

**Q49.** What are the defining properties of a Wiener process (standard Brownian motion)?

A Wiener process W(t) satisfies: W(0) = 0; it has independent increments; each increment is normally distributed with W(t) - W(s) ~ Normal(0, t-s) (variance grows linearly with time); and its paths are continuous but nowhere differentiable. A key scaling consequence is that dW has standard deviation sqrt(dt), i.e., E[dW] = 0 and E[dW^2] = dt, which is why volatility scales with sqrt(T) (the square-root-of-time rule). These properties make W the canonical source of continuous-time randomness in finance.

**Q50.** Apply Ito's lemma to S and explain why d(ln S) carries a -0.5*sigma^2 term.

Ito's lemma is the stochastic chain rule: for f(S) it adds a second-order term, df = (df/dS) dS + 0.5*(d2f/dS2) (dS)^2, where crucially (dW)^2 = dt. Applying it to f = ln S with dS = mu*S*dt + sigma*S*dW gives d(ln S) = (mu - 0.5*sigma^2) dt + sigma*dW. The -0.5*sigma^2 (the Ito correction) appears because ln is concave and (dS)^2 = sigma^2 * S^2 * dt is non-zero in stochastic calculus; intuitively, volatility drags down the growth rate of the log because gains and losses are not symmetric in compounded returns.

**Q51.** Why are stock prices lognormal while log-returns are normal?

From d(ln S) = (mu - 0.5*sigma^2) dt + sigma*dW, the log of the price is normally distributed, so the continuously-compounded return ln(S_T/S_0) is Normal((mu - 0.5*sigma^2)T, sigma^2 * T). Because the price itself is the exponential of a normal variable, S_T = S_0 * exp((mu - 0.5*sigma^2)T + sigma*sqrt(T)*Z), S_T follows a lognormal distribution: skewed right and bounded below at zero. This is economically sensible — prices cannot go negative and a stock can multiply many-fold but only fall to zero, exactly the asymmetry a lognormal captures.

**Q52.** How does Monte-Carlo simulation price a derivative, and how fast does it converge?

Monte-Carlo simulates many price paths under the risk-neutral GBM S_T = S_0 * exp((r - 0.5*sigma^2)T + sigma*sqrt(T)*Z), computes the payoff on each path (e.g., max(S_T - K, 0) for a call), averages them, and discounts: price = exp(-r*T) * (1/N) * sum(payoff_i). Its statistical error shrinks as 1/sqrt(N), so cutting the error in half requires roughly 4x the paths — slow but dimension-independent, which makes it the go-to method for path-dependent and high-dimensional options (Asian, basket, barrier) where closed forms do not exist. Variance-reduction tricks like antithetic variates and control variates tighten the estimate without simply quadrupling N.

**Q53.** What is the difference between the real-world and risk-neutral measures, and why price under risk-neutral?

Under the real-world (physical) measure P the stock drifts at its true expected return mu, reflecting investors' risk premium; under the risk-neutral measure Q the drift is replaced by the risk-free rate r, so dS = r*S*dt + sigma*S*dW and all assets earn r on average. We price derivatives under Q because, by the fundamental theorem of asset pricing, the absence of arbitrage means a discounted price is a martingale under Q, giving price = exp(-r*T) * E_Q[payoff], a value that does not depend on anyone's risk appetite. The real-world measure is used for risk management, forecasting and VaR, while the risk-neutral measure is used purely for consistent, arbitrage-free valuation; only the drift changes between them, the volatility sigma is the same.

## The Greeks

**Q54.** Define delta and give the BSM delta for a call and a put.

Delta is the rate of change of option value per unit change in the underlying: delta = dV/dS. For a (non-dividend) European call, delta = N(d1), ranging from 0 (deep OTM) to 1 (deep ITM); for a put, delta = N(d1) - 1, ranging from -1 to 0. With a dividend yield q the call delta is e^(-q*T)*N(d1). An ATM call has delta around 0.5.

**Q55.** Why is delta also called the hedge ratio?

Because to neutralize the directional risk of one short call you hold delta shares of the underlying (delta shares per option), making the combined position locally insensitive to small spot moves. If you are short a call with delta 0.55 on a lot, you buy 0.55*lot_size shares to be delta-neutral. As spot moves, delta changes, so the hedge must be rebalanced — that is dynamic delta hedging.

**Q56.** Why is delta a rough approximation of the probability of finishing ITM?

For a call, delta = N(d1) while the true risk-neutral ITM probability is N(d2), and since d1 > d2 these differ only by the sigma*sqrt(T) gap. For short-dated, low-vol options that gap is small, so traders use delta as a quick proxy for "chance of expiring ITM." A 25-delta option is loosely treated as having roughly a 25% chance of finishing ITM, though strictly the probability is N(d2), a bit lower.

**Q57.** Define gamma and state where it is largest.

Gamma is the second derivative of value with respect to spot, gamma = d(delta)/dS = d2V/dS2; it measures how fast delta changes. Gamma is identical for a call and the corresponding put (parity), is always positive for long options, and is largest for at-the-money options close to expiry, where delta swings most violently around the strike. The BSM formula is gamma = N'(d1) / (S*sigma*sqrt(T)), where N'() is the normal PDF.

**Q58.** Why do traders care about gamma even though they hedge delta?

Because delta hedging is only exact for infinitesimal moves; gamma measures the hedging error from large moves. High positive gamma means your delta hedge becomes stale quickly, forcing frequent rebalancing, but it also means a delta-neutral long-option book profits from big moves in either direction. Gamma is the curvature that a single delta number cannot capture, so a full hedge tracks both.

**Q59.** Define vega and its units.

Vega is the sensitivity of option value to a change in volatility: vega = dV/dsigma. By convention it is quoted per 1 percentage-point (0.01) change in vol. The BSM formula is vega = S*sqrt(T)*N'(d1) (times e^(-q*T) with dividends); it is the same for calls and puts, always positive for long options. Note "vega" is not a real Greek letter, but the name stuck.

**Q60.** Where is vega largest, and how does it differ from gamma's profile?

Vega is largest for at-the-money options that are longer-dated, because more time means more room for volatility to move the terminal price distribution. This contrasts with gamma, which is also largest ATM but peaks for short-dated options. So a long-dated ATM option is a big vega / small gamma bet, while a near-expiry ATM option is a big gamma / small vega bet.

**Q61.** Define theta and explain its usual sign.

Theta is the rate of change of value with the passage of time: theta = dV/dt, usually quoted per day (per calendar or trading day). For most long options theta is negative — the option loses time value as expiry approaches ("time decay") — and decay is fastest for at-the-money options near expiry. Deep ITM European puts (and some dividend cases) can have positive theta, but the typical long-option holder is fighting theta.

**Q62.** What is the relationship between theta, gamma and vega for an option's time value?

They are linked through the BSM PDE: theta + 0.5*sigma^2*S^2*gamma + r*S*delta - r*V = 0. The key intuition is the gamma-theta tradeoff: positive gamma (good — you profit from moves) is paid for by negative theta (bad — you bleed time value). A delta-neutral long-gamma book earns from realized volatility but pays theta; it is profitable only if realized vol exceeds the implied vol it paid.

**Q63.** Define rho and say when it matters.

Rho is the sensitivity of value to the risk-free rate: rho = dV/dr, quoted per 1 percentage-point change. For a call rho = K*T*e^(-r*T)*N(d2) > 0; for a put rho = -K*T*e^(-r*T)*N(-d2) < 0. Rho matters most for long-dated options (LEAPS) and in high-rate environments; for typical short-dated equity options it is the least important Greek.

**Q64.** Walk through delta hedging and why it must be dynamic.

To hedge a sold call you buy delta shares; the position is then insensitive to small spot moves. But because gamma is non-zero, delta changes as spot moves and as time passes, so you must continuously rebalance — buy more shares as spot rises, sell as it falls. In a perfect BSM world this continuous re-hedging exactly replicates the option, and the cost of replication equals the BSM premium.

**Q65.** What is gamma scalping?

Gamma scalping is the trading strategy of holding a long-gamma, delta-neutral position (e.g. long a straddle, delta-hedged) and profiting from realized volatility. As spot moves, your delta drifts; you rebalance by selling shares after rallies and buying after dips — mechanically "buy low, sell high" — locking in small profits. These scalping gains must beat the theta you pay; you win when realized vol > implied vol.

**Q66.** Spell out the gamma-theta tradeoff with a quick example.

Long gamma earns money from movement but bleeds theta; short gamma collects theta but loses on big moves. Roughly, the daily P&L of a delta-hedged book is about 0.5*gamma*(dS)^2 - theta_per_day. If a stock's squared move earns more than the day's theta cost, the long-gamma trader profits; otherwise theta wins.

**Q67.** Summarize the sign of each Greek for a long call versus a long put.

Long call: delta + (0 to 1), gamma +, vega +, theta - (usually), rho +. Long put: delta - (-1 to 0), gamma +, vega +, theta - (usually), rho -. Gamma and vega are positive for any long option (call or put); shorting any option flips all signs. The asymmetry is in delta and rho, which carry the directional and rate-direction information.

**Q68.** What is vanna?

Vanna is a second-order Greek measuring how delta changes when volatility changes (or equivalently how vega changes when spot changes): vanna = d2V/(dS dsigma). It is important for risk-managing skew, because it links your directional exposure to vol moves. Books with significant vanna can see their delta shift purely from a change in implied vol, even with spot unchanged.

**Q69.** What is volga (vomma)?

Volga, also called vomma, is the second derivative of value with respect to volatility: volga = d2V/dsigma2, i.e. how vega changes as vol changes. It captures the convexity of the option in vol and is central to pricing volatility-of-volatility and the smile. Long options that are away-from-the-money tend to have high positive volga, which benefits from large swings in implied vol.

**Q70.** What is charm?

Charm (delta decay) measures how delta changes with the passage of time: charm = d(delta)/dt = d2V/(dS dt). It tells a hedger how their delta will drift overnight or over a weekend even if spot does not move, which matters for setting hedges before non-trading periods. ATM options near expiry have the largest charm, so hedges can go stale quickly as time passes.

**Q71.** How do the main Greeks change as an option approaches expiry?

Gamma and theta both spike sharply for at-the-money options as T -> 0 (delta flips between 0 and 1 over a tiny spot range, and time value decays fastest). Vega shrinks toward zero because there is little time left for vol to act. Delta tends toward 0 or 1 (a step function), and rho also shrinks as the discounting horizon collapses.

**Q72.** How do Greeks change as volatility rises?

Higher sigma widens the terminal price distribution: vega is positive so option values rise, and OTM options gain the most in relative terms. Higher vol pushes deltas of OTM/ITM options back toward 0.5 (more uncertainty about ending side of the strike), spreads gamma over a wider spot range (lowering the ATM peak), and increases time value, making theta (in absolute terms) larger. In short, vol "smears" the Greek profiles across strikes.

## Volatility

**Q73.** What is the difference between implied volatility and realized (historical) volatility?

Realized (historical) volatility is backward-looking: it is the actual standard deviation of past returns, e.g. computed as the annualized stdev of daily log returns. Implied volatility (IV) is forward-looking: it is the volatility input embedded in the current market price of an option, i.e. the market's expectation of future volatility over the option's life. They often differ — IV typically trades above realized vol (a "variance risk premium") because option sellers demand compensation for taking on risk.

**Q74.** What exactly is implied volatility?

Implied volatility is the value of sigma that, when plugged into the Black-Scholes-Merton (BSM) formula, makes the model price equal the observed market price of the option. All other BSM inputs (spot S, strike K, time T, rate r, dividend q) are observable, so the option's market price can be "inverted" to back out a single unknown — sigma. It is the market's consensus forecast of annualized volatility expressed in BSM's language, not a directly observed quantity.

**Q75.** Why can't you solve for implied volatility with a closed-form formula?

Because the BSM price is a non-linear, monotonic-but-not-invertible function of sigma — the option price depends on sigma through the cumulative normal N(d1) and N(d2), which cannot be algebraically rearranged to isolate sigma. So IV must be found numerically using iterative root-finding such as Newton-Raphson or bisection. The good news is that price is strictly increasing in sigma (vega > 0), so a unique solution exists for any arbitrage-free price.

**Q76.** How does Newton-Raphson solve for implied volatility?

You iterate IV_{n+1} = IV_n - (model_price(IV_n) - market_price) / vega(IV_n), where vega is the derivative of price with respect to sigma. Starting from a guess (say 20%), each step uses the pricing error divided by vega to correct the estimate, and it converges quadratically — usually 3-5 iterations to high precision. Example: if model price is 4.80 vs market 5.00 and vega is 0.40 (per 1.00 = 100% vol), then IV_{n+1} = IV_n + 0.20/0.40 = IV_n + 0.50 vol points adjustment.

**Q77.** What is the volatility smile?

The volatility smile is the empirical pattern that implied volatility varies with strike (or moneyness) rather than being constant as BSM assumes. When you plot IV against strike, out-of-the-money puts and calls often show higher IV than at-the-money options, producing a U or "smile" shape. It exists because real return distributions have fatter tails and are not lognormal, so the market prices tail strikes richer than a flat-vol BSM would.

**Q78.** What is volatility skew and how does it differ from a smile?

Skew refers to an asymmetric smile where IV is systematically higher on one side of the strike range than the other. Equity indices show a downward (negative) skew: low strikes (downside puts) carry much higher IV than high strikes. A symmetric smile implies the market sees roughly equal fat-tail risk on both sides, whereas skew implies asymmetric crash/tail expectations.

**Q79.** Why do equity index options exhibit a pronounced downward skew?

Three reinforcing reasons: (1) crash-o-phobia — after 1987, markets price a higher probability of sudden large down moves than up moves; (2) the leverage effect — as equity prices fall, firms' debt/equity ratios rise, increasing volatility, so down moves and higher vol are correlated; and (3) supply/demand — institutions persistently buy downside puts for portfolio insurance, bidding up low-strike IV. The Nifty and Bank Nifty options on the NSE show this same negative skew.

**Q80.** Why do some assets (like FX or certain commodities) show a more symmetric smile?

For currencies, a large move in either direction is roughly equally likely and equally feared — a sharp appreciation or depreciation both create tail risk — so demand for OTM puts and calls is more balanced, producing a near-symmetric smile. Equities skew because the downside is the feared, leverage-amplified direction; FX has no such asymmetry between "up" and "down." Some commodities can even show a reverse (upward) skew when supply shocks make spikes the feared tail.

**Q81.** What is the term structure of volatility?

It is how implied volatility varies with time to maturity for a fixed strike or moneyness (typically ATM). In calm markets it usually slopes upward (longer maturities price more vol as uncertainty accumulates and mean-reverts toward a long-run level); in stress it inverts, with near-term IV spiking above long-dated IV because the shock is expected to be acute but temporary. It reflects the market's expected path of volatility over time.

**Q82.** What is the implied volatility surface?

The IV surface is a 3D plot of implied volatility as a function of two axes — strike (or moneyness/delta) and time to maturity. A cross-section at fixed maturity gives the smile/skew; a cross-section at fixed strike gives the term structure. Traders use the whole surface to price and risk-manage exotic and vanilla books consistently, and a well-behaved surface must be free of arbitrage in both the strike and time directions.

**Q83.** What is a 25-delta risk reversal and what does it measure?

A 25-delta risk reversal is the IV of the 25-delta call minus the IV of the 25-delta put (RR = IV(25d call) - IV(25d put)). It quantifies the skew/asymmetry of the smile: a negative risk reversal means puts are bid over calls (typical for equities), signalling downside fear. It is the standard FX-market measure of skew and is quoted directly as a tradable structure (long call / short put at equal delta).

**Q84.** What is a 25-delta butterfly and what does it measure?

The 25-delta butterfly is BF = 0.5*(IV(25d call) + IV(25d put)) - IV(ATM), the average of the two 25-delta wing vols minus the at-the-money vol. It measures the convexity (curvature) of the smile — how much the wings are bid relative to the center, i.e. how fat the market prices both tails. Together, ATM vol, the risk reversal, and the butterfly fully parameterize the smile at a given maturity.

**Q85.** What does the VIX measure and why is it called the "fear gauge"?

The VIX is the CBOE Volatility Index: the market's expected 30-day implied volatility of the S&P 500, expressed in annualized percentage points. It is computed model-free from a strip of OTM SPX option prices (a variance-swap-style weighted sum across strikes), not from a single BSM inversion. It is called the fear gauge because it spikes when investors rush to buy protection during sell-offs — VIX above ~30 signals stress, below ~15 signals calm.

**Q86.** What is India VIX and how does it relate to the VIX?

India VIX is the NSE's volatility index, measuring the expected 30-day implied volatility of the Nifty 50 from near- and next-month Nifty options, using the same CBOE-style model-free methodology. It is widely watched as India's fear gauge: it jumps around events like the Union Budget, RBI policy, and election results. Like the VIX, it is annualized in percent and tends to be negatively correlated with the underlying index.

**Q87.** What is the difference between IV rank and IV percentile?

IV rank measures where current IV sits between its 52-week low and high: IV Rank = (IV_now - IV_low) / (IV_high - IV_low) * 100. IV percentile measures the fraction of days over the lookback during which IV was below the current level. IV rank is sensitive to a single extreme spike (it anchors on the min/max), while IV percentile better reflects the typical distribution; an IV rank of 50 with a percentile of 80 tells you IV is mid-range but has rarely been this high day-to-day.

**Q88.** What is vega and how do volatility traders use it to express views?

Vega is the option's sensitivity to a 1-percentage-point change in implied volatility (dPrice/dsigma); for example a vega of 0.12 means the option gains about 0.12 if IV rises by 1 point. A trader who thinks vol is too cheap buys options (long vega); one who thinks vol is too rich sells options (short vega). Vega is largest for at-the-money, longer-dated options, so vol views are often expressed with ATM straddles or variance swaps to get clean vega exposure with minimal directional delta.

**Q89.** Explain sticky-strike versus sticky-delta (sticky-moneyness) regimes.

Sticky-strike assumes each strike keeps its IV as the spot moves, so an option's IV stays put while its moneyness changes — common in quiet, range-bound markets. Sticky-delta (sticky-moneyness) assumes the IV attached to a given delta/moneyness stays fixed, so the whole smile slides with the spot — common in trending markets. The assumption matters for hedging because it changes the effective delta: under sticky-delta the skew adds to the BSM delta, altering how many shares you hedge with.

**Q90.** What no-arbitrage constraints must a volatility surface satisfy?

Two key families: (1) the calendar-spread (term) constraint — total implied variance sigma^2*T must be non-decreasing in maturity for a fixed moneyness, otherwise a calendar arbitrage exists; and (2) the butterfly constraint — the implied risk-neutral density from the strike dimension must be non-negative, which requires call prices to be convex and monotonic in strike. Violations (e.g. IV curving too sharply, or near-dated variance exceeding far-dated) imply free lunches, so quants fit arbitrage-free parameterizations like SVI.

**Q91.** Why is selling options described as "short vol" and "short gamma"?

When you sell an option you are short vega (you lose if IV rises) — hence short vol. You are also short gamma: a delta-hedged short option position must buy as the underlying rises and sell as it falls (buy high, sell low), so realized movement bleeds money via negative gamma P&L. The short option earns positive theta (time decay) to compensate; the position profits when realized volatility comes in below the IV you sold, and loses when the market moves more than priced.

**Q92.** What is the difference between variance and volatility, and why does volatility mean-revert?

Volatility is sigma (standard deviation of returns); variance is sigma^2. The distinction matters because variance is additive over time and is what variance swaps and the VIX actually trade — payoffs are linear in variance but non-linear (concave) in vol, so a vol position has convexity. Implied (and realized) volatility mean-reverts: it oscillates around a long-run average, spiking in crises and decaying back, which is why models like Heston and GARCH include a mean-reversion term and why traders fade extreme IV rank readings expecting normalization.

## Strategies

**Q93.** What is a covered call, and what market view does it express?

A covered call means you hold the underlying (long stock or futures) and sell one call against it, usually slightly out-of-the-money. The view is mildly bullish to neutral: you expect the stock to stay flat or rise modestly, and you collect the premium as extra yield. Max profit = (strike - purchase price) + premium received, capped if the stock rallies above the strike; max loss is large (stock can fall to zero, cushioned only by the premium); breakeven = purchase price - premium. On NSE this is a common Nifty/Bank Nifty F&O overlay where investors write monthly calls on a held position to earn premium income.

**Q94.** What is a protective put and when would you use it?

A protective put is long underlying plus a long put, acting like an insurance policy on your position. The view is bullish but nervous: you want upside exposure while capping downside, so you pay a premium to floor your losses at the strike. Max loss = (purchase price - put strike) + premium paid; max profit is unlimited (stock can keep rising) minus the premium cost; breakeven = purchase price + premium. Indian portfolio managers buy Nifty puts as a hedge before events like the Union Budget or RBI policy to protect against a market drop.

**Q95.** Construct a bull call spread and state its risk profile.

A bull call spread buys a lower-strike call and sells a higher-strike call of the same expiry, financing part of the cost with the short call. The view is moderately bullish with defined risk: you profit if the underlying rises toward the higher strike but you cap both gain and loss. Max profit = (K_high - K_low) - net premium paid; max loss = net premium paid; breakeven = K_low + net premium. Example on Nifty: buy 24000 call at 200, sell 24200 call at 120, net debit 80; max profit = 200 - 80 = 120, max loss = 80, breakeven = 24080.

**Q96.** How does a bear put spread work and what is its payoff?

A bear put spread buys a higher-strike put and sells a lower-strike put of the same expiry, a defined-risk way to play a moderate fall. The view is moderately bearish: you profit as the underlying declines toward the lower strike, with capped gain and capped loss. Max profit = (K_high - K_low) - net premium paid; max loss = net premium paid; breakeven = K_high - net premium. It is the mirror image of the bull call spread and is cheaper than buying a naked put because the short put offsets premium.

**Q97.** What is a long straddle, and when is it profitable?

A long straddle buys a call and a put at the same strike (usually at-the-money) and expiry. The view is long volatility / direction-agnostic: you expect a big move either way but are unsure of direction, common around earnings or binary events. Max loss = total premium paid (if the stock pins the strike at expiry); max profit is unlimited on the upside and large on the downside; there are two breakevens at strike +/- total premium. You need the realized move to exceed the combined premium, so a long straddle loses if implied volatility was already rich and the stock stays quiet.

**Q98.** How does a long strangle differ from a long straddle?

A long strangle buys an out-of-the-money call and an out-of-the-money put (different strikes, same expiry), so it is cheaper than a straddle but needs a larger move to pay off. The view is still long volatility expecting a big swing. Max loss = total premium paid; max profit is unlimited up / large down; breakevens are at K_call + total premium and K_put - total premium. Because both legs start OTM the upfront cost (and max loss) is lower, but the no-profit zone between the strikes is wider than a straddle's.

**Q99.** Describe a short straddle/strangle and its risk.

Selling a straddle (short ATM call + short ATM put) or a strangle (short OTM call + short OTM put) collects premium and profits when the underlying stays range-bound and implied volatility falls. The view is short volatility / neutral. Max profit = premium received (when the stock pins the strikes); max loss is theoretically unlimited on a large move in either direction; breakevens are strike +/- premium (straddle) or each strike +/- premium (strangle). This is high-risk: a sharp gap (e.g., a Bank Nifty move on RBI surprise) can blow past the premium, which is why SEBI margins for short option positions are heavy.

**Q100.** What is a long butterfly spread and what view does it express?

A long call butterfly buys one lower-strike call, sells two middle-strike calls, and buys one higher-strike call (equally spaced strikes, same expiry) for a small net debit. The view is range-bound / short volatility: you expect the underlying to expire near the middle strike. Max profit = (wing width) - net premium, achieved at the middle strike; max loss = net premium paid; two breakevens sit at K_low + net premium and K_high - net premium. It is a cheap, fully defined-risk way to bet on a pin, with the lost premium being the only downside.

**Q101.** Explain the iron condor and the risk reversal as two range / skew strategies.

An iron condor sells an OTM put spread and an OTM call spread simultaneously (four legs), collecting net premium; the view is range-bound short volatility, with max profit = net premium received if the underlying stays between the short strikes, and max loss = (spread width - net premium) capped by the long wings. A risk reversal is directional-plus-skew: sell an OTM put and buy an OTM call (bullish version), often for near-zero cost, giving long-stock-like exposure financed by the put premium; max loss is large if the stock falls below the put strike, max profit is unlimited above the call strike. A collar is the conservative cousin of the risk reversal applied to a held position: long stock + long protective put + short covered call, which caps both downside and upside for little or no net premium and is widely used by Indian PMS/HNI clients to lock in a band around a concentrated holding.

## Advanced & Exotics

**Q102.** What distinguishes a path-dependent option from a path-independent one, and give examples of each?

A path-independent option's payoff depends only on the underlying's level at expiry (or exercise), not the route taken — a vanilla European call paying max(S_T - K, 0) is the canonical example. A path-dependent option's payoff depends on the trajectory: Asian options use the average price over the life, barrier options depend on whether a level was touched, and lookbacks use the running max/min. Path dependence usually rules out simple closed forms and pushes you toward trees, PDEs, or Monte Carlo.

**Q103.** What is an Asian (average) option, why is it cheaper than a vanilla, and who uses it?

An Asian option's payoff uses the average underlying over a set of dates rather than the single expiry price — an average-rate call pays max(A - K, 0) where A is the arithmetic mean of observed prices. Averaging lowers effective volatility, so the option is cheaper than a vanilla and is robust to a single-day spike or expiry-day manipulation. Treasurers and commodity desks use them to hedge a stream of regular transactions (e.g. a fuel buyer hedging monthly purchases) where the average cost is what they actually pay; note the geometric-average version has a closed form while the arithmetic one needs Monte Carlo.

**Q104.** Define knock-in versus knock-out barrier options, the parity linking them to vanillas, and why their Greeks are dangerous.

A knock-out starts alive and dies if the underlying touches the barrier (an up-and-out call dies if S hits H above spot); a knock-in only springs into existence once the barrier is touched, and for the same terms knock-in + knock-out = the vanilla. Barriers are cheaper than vanillas because you forgo payoff in some scenarios, which is why FX desks and structured notes love them. Near the barrier the value can jump to zero over a tiny move, so delta and gamma spike and flip sign, making delta-hedging extremely costly — dealers manage this with barrier shifting or vanilla over-hedges.

**Q105.** What is a lookback option and why is it expensive?

A lookback's payoff references the best price reached over the life: a floating-strike lookback call pays S_T - min(S), effectively letting you buy at the low, while a fixed-strike version pays max(max(S) - K, 0). Because you always capture the optimal historical price, lookbacks embed perfect market-timing you could never achieve, so they are expensive and mostly a structuring/teaching tool rather than a liquid product.

**Q106.** Explain a digital (binary) option and how desks actually hedge its blow-up risk near the strike.

A cash-or-nothing digital pays a fixed amount (say 1) if S_T > K and zero otherwise, so its payoff is a step function. As expiry nears, delta becomes a tall narrow spike at K and gamma flips sign violently around it. Dealers therefore replicate and hedge a digital with a tight vanilla call spread — long a call at K-eps, short at K+eps, scaled by 1/(2*eps) — which caps the local risk and is what really gets traded.

**Q107.** What is a chooser option and how does it decompose?

A chooser lets the holder decide at a future date t whether the option becomes a call or a put (same strike K, expiry T). At the choice date a rational holder takes max(C, P), so via put-call parity a simple chooser equals a call expiring at T plus a put expiring at the earlier choice date t. It suits a buyer expecting a big move of uncertain direction and is cheaper than buying an outright straddle.

**Q108.** What is a compound option and where do compound options arise naturally?

A compound option is an option on an option — e.g. a call-on-a-call gives the right to buy a call for a preset premium at the first expiry, so it has two strikes and two dates. They appear in real-options analysis (a phased capital project is a sequence of options on options), in hedging contingent deals where the underlying hedge may or may not be needed, and in installment-premium structures. They are very sensitive to volatility, exhibiting strong gamma-of-vega.

**Q109.** What is a basket option and why is correlation its key risk?

A basket option pays off on a weighted portfolio of underlyings, e.g. max(w1*S1 + w2*S2 + ... - K, 0). Its price hinges on pairwise correlations because basket variance = sum over i,j of w_i*w_j*sigma_i*sigma_j*rho_ij; higher correlation raises basket vol and the price. Buyers use baskets to express a view on a group (an index, an FX basket) more cheaply than buying options on each name, precisely because diversification lowers basket vol.

**Q110.** Derive the risk-neutral up-probability in a binomial tree and state the CRR choice of u and d.

Risk-neutral pricing requires the discounted expected stock to equal today's price: S = e^(-r*dt)*(p*S*u + (1-p)*S*d), giving p = (e^(r*dt) - d) / (u - d), which must satisfy d < e^(r*dt) < u so 0 < p < 1. Cox-Ross-Rubinstein sets u = e^(sigma*sqrt(dt)) and d = 1/u so the tree recombines and matches lognormal variance as dt -> 0. Example: S=100, sigma=20%, dt=1y, r=5% gives u=1.221, d=0.819, p=(1.0513-0.819)/(1.221-0.819)=0.578; p is a pricing measure, not the real-world probability.

**Q111.** How does a binomial tree price an American option, and when is early exercise actually optimal?

You roll backward from expiry taking value = max(immediate exercise payoff, e^(-r*dt)*(p*V_up + (1-p)*V_down)) at every node, comparing intrinsic value to continuation value — backward induction is required because a node's continuation value needs its children's already-computed values. This early-exercise test is exactly what Black-Scholes cannot capture. Early exercise is never optimal for an American call on a non-dividend stock (you would forfeit time value and interest on the strike), but can pay for a deep in-the-money American put or a call just before a large dividend.

**Q112.** What does a trinomial tree add over a binomial tree?

A trinomial tree allows three moves per step (up, unchanged, down), giving an extra degree of freedom that improves stability and convergence and maps directly onto an explicit finite-difference scheme. The middle branch lets you align nodes with specific levels — invaluable for barrier options and for interest-rate models like Hull-White — and fit the local drift/vol more flexibly than a binomial lattice.

**Q113.** Why is Monte Carlo natural for exotics, and why does its error shrink only like 1/sqrt(N)?

Monte Carlo simulates many risk-neutral paths, averages the payoffs, and discounts: price = e^(-r*T)*mean(payoff); it handles path dependence and high dimensions (baskets, many dates) trivially where trees suffer the curse of dimensionality. By the Central Limit Theorem the standard error is sigma_payoff/sqrt(N), so error falls as 1/sqrt(N) — halving it needs 4x the paths and one extra decimal needs 100x. Its weakness is early exercise (needs Longstaff-Schwartz regression) and this slow convergence, which is why variance reduction matters.

**Q114.** Explain antithetic and control variates as variance-reduction techniques.

Antithetic variates pair each random draw Z with -Z; the two payoffs are negatively correlated, so Var((X+Y)/2) = (Var(X)+Var(Y)+2Cov(X,Y))/4 shrinks when Cov is negative — essentially free and best for monotonic payoffs. A control variate uses a correlated quantity with a known analytic price: estimator = MC(target) - b*(MC(control) - TrueValue(control)), with optimal b = Cov(target,control)/Var(control). For an arithmetic Asian the geometric Asian is the classic control because it is highly correlated and has a closed form, often cutting variance by an order of magnitude.

**Q115.** What are finite-difference methods conceptually, and how do explicit and implicit schemes differ?

Finite-difference methods solve the Black-Scholes PDE directly by discretizing price and time onto a grid, approximating derivatives with differences, and stepping backward from the payoff boundary. The explicit scheme is simple but only stable under a tight time-step condition (like a trinomial tree); implicit and Crank-Nicolson schemes solve a linear system each step but are unconditionally stable and more accurate. FDM excels for low-dimensional American and barrier problems where you want the full price surface and clean Greeks.

**Q116.** Why do models beyond Black-Scholes exist — what does the volatility smile prove?

Black-Scholes assumes one constant volatility, which would imply a flat implied-vol curve across strikes; the market instead shows a smile/skew (out-of-the-money equity puts priced richer). This proves the real return distribution has fatter tails and negative skew than lognormal, so a single sigma cannot price all strikes consistently. Hence local-vol, stochastic-vol, and jump models exist to reproduce the observed smile and price exotics consistently with vanillas.

**Q117.** Contrast local volatility (Dupire) with stochastic volatility models.

Local volatility makes sigma a deterministic function sigma(S,t) calibrated to fit today's entire vanilla surface exactly via the Dupire equation, but it predicts unrealistic, flattening future smile dynamics. Stochastic volatility makes variance itself a random process with its own vol-of-vol and spot correlation, capturing the realistic forward skew that matters for exotics and forward-starting products. Desks often use local-stochastic-vol (LSV) hybrids to get both an exact fit and sensible dynamics.

**Q118.** What do the Heston and SABR stochastic-volatility models add, and what do their parameters control?

Heston models variance as a mean-reverting CIR process dv = kappa*(theta - v)*dt + xi*sqrt(v)*dW2 correlated (rho) with spot: kappa is reversion speed, theta the long-run variance, xi the vol-of-vol setting smile convexity, and rho (negative for equities) the skew — it has a semi-closed form for vanillas making calibration fast. SABR models a forward as dF = alpha*F^beta*dW1, d(alpha) = nu*alpha*dW2: alpha sets the vol level, beta the backbone (0 normal, 1 lognormal), rho the skew, nu the curvature. SABR is the market standard for swaption smiles because Hagan's formula gives implied vol per strike directly.

**Q119.** What does Merton's jump-diffusion model capture that pure diffusion cannot?

Merton adds a compound-Poisson jump term to geometric Brownian motion, so the stock can gap: dS/S = (mu - lambda*k)*dt + sigma*dW + (J-1)*dN with jump intensity lambda. Jumps generate the steep short-dated skew and fat tails that pure diffusion cannot (diffusion smiles flatten at short maturities), and they make perfect delta-hedging impossible, so markets become incomplete. This matters for crash risk, gap risk on barriers, and overnight/earnings moves.

**Q120.** Explain delta-hedging P&L, the gamma-theta relationship and the breakeven daily move, and how transaction costs alter it.

For a delta-hedged book the P&L over a small interval is roughly 0.5*gamma*(dS)^2 + theta*dt — long gamma earns on big moves while theta bleeds time value — so the two break even at dS ~ S*sigma*sqrt(dt), about one implied standard deviation. Example: S=20000, sigma=15%, dt=1/252 gives breakeven ~ 20000*0.15*sqrt(1/252) ~ 189 points/day; move more and long gamma wins, less and theta wins. In reality you rehedge discretely, so transaction costs act like a volatility add-on (Leland) that scales with sqrt(rehedge frequency), and bid-ask plus impact can erode the theoretical realized-minus-implied-vol edge entirely.

**Q121.** Define vega, vanna, and volga and why a book must watch all three.

Vega is sensitivity to volatility (dV/dsigma); vanna is the cross term dVega/dSpot (equivalently dDelta/dsigma); and volga (vomma) is dVega/dsigma, the convexity of value in vol. A vega-neutral book can still bleed when spot moves (vanna) or when vol moves a lot (volga), so smile-risk management requires hedging all three — this underpins the vanna-volga pricing method in FX. Ignoring vanna/volga is why naive vega hedges fail in skewed, moving markets.

**Q122.** How does a variance swap pay off and how is it replicated with a strip of options?

A variance swap pays notional*(realized_variance - K_var), where realized variance is the annualized sum of squared log returns, giving pure variance exposure with no path-dependent delta. It is replicated statically by a portfolio of out-of-the-money calls and puts weighted by 1/K^2 across all strikes, plus a dynamic delta hedge; the fair strike is essentially the 1/K^2-weighted integral of option prices (the model-free basis for the VIX). The 1/K^2 weighting is precisely what makes the payoff track variance regardless of where spot goes.

**Q123.** How does a volatility swap differ from a variance swap, and why is the variance swap easier to hedge?

A variance swap settles on realized variance (vol squared) while a volatility swap settles on realized volatility itself, notional*(realized_vol - K_vol). The variance swap has clean static replication via the 1/K^2 option strip, but a vol swap's payoff is the concave square root of variance, so by Jensen's inequality its fair strike sits below sqrt(variance strike) by a convexity adjustment and it cannot be statically replicated. That vol-of-vol convexity is an extra risk that makes vol swaps harder to hedge.

**Q124.** What is dispersion trading and what view does it express?

Dispersion trading sells index volatility/variance and buys volatility on the constituent single names (or vice versa), profiting when realized correlation differs from the implied correlation embedded in index vol. Since index variance = sum of weighted single-name variances plus correlation terms, the trade is essentially short implied correlation — it makes money when stocks move idiosyncratically while index vol stays subdued. The main risk is a correlation spike in a sell-off, when everything moves together and the short-index-vol leg loses badly.

**Q125.** Decompose a capital-guaranteed (principal-protected) note into options.

A capital-guaranteed note is a zero-coupon bond plus a long call: the issuer puts most of the principal into a discount bond that accretes to par (guaranteeing capital) and spends the residual buying upside via a call, often capped or with a participation rate. Example: at 5% rates, ~78 of 100 buys a 5y zero maturing at 100, leaving ~22 to buy index calls; the participation rate is whatever option exposure that budget funds. This is why low rates make these notes far less attractive — less premium is left for the call.

**Q126.** Decompose a reverse convertible and an autocallable into options.

A reverse convertible is a high-coupon note where the investor is effectively short a put: you receive an enhanced coupon for selling downside protection and are repaid in shares (taking the loss) if the underlying breaches a level at maturity. An autocallable embeds a short down-and-in put plus a series of digital/barrier coupons with an automatic early-redemption feature — it pays attractive coupons and redeems early if the underlying is above a trigger on observation dates, but exposes the buyer to sharp losses through the protection barrier. Both are yield-enhancement products that sell tail risk to coupon-hungry investors.

**Q127.** What is a quanto option and what extra risk does it introduce?

A quanto pays off on a foreign-currency underlying but settles in the domestic currency at a fixed exchange rate — e.g. an option on the S&P 500 paying in INR at a pre-agreed rate, removing FX risk for the rupee investor. Pricing requires a quanto drift adjustment: the foreign asset's drift shifts by -rho*sigma_S*sigma_FX because the payoff is exposed to the asset-FX covariance. The key extra risk is therefore the unobservable asset-FX correlation, which must be estimated and hedged.

**Q128.** What is CVA and how does counterparty risk enter OTC derivative pricing?

Credit Valuation Adjustment is the market value of counterparty default risk — the amount you mark down a derivative's risk-free value because the counterparty might default when you are in-the-money. Conceptually CVA = integral over time of (loss-given-default * expected positive exposure * marginal default probability), discounted, so it depends on the counterparty's credit spread and your future exposure profile. Post-2008, XVA desks price CVA (plus DVA, FVA, MVA, KVA) into every OTC trade, which is why uncollateralized trades cost more than cleared/collateralized ones.

**Q129.** How do you compute and manage the Greeks of a whole derivatives portfolio?

Because the Greeks are partial derivatives of value, they add across positions on a common underlying: portfolio delta = sum of (position delta * quantity), and likewise for gamma, vega, theta. A desk nets these to a few aggregate numbers and hedges the residual — trade the underlying to zero delta, then use options to flatten gamma and vega within limits. The subtlety is that vega across strikes/expiries is not truly fungible (smile and term-structure risk), so books bucket vega by tenor and strike rather than summing one number.

**Q130.** Distinguish risk-neutral from real-world probabilities and explain why pricing uses the risk-neutral measure.

Real-world (physical) probabilities include a risk premium and are used for forecasting, P&L distributions, and risk metrics like VaR. Risk-neutral probabilities are an artificial measure under which all assets drift at the risk-free rate, so a derivative's price equals the discounted risk-neutral expected payoff — this holds because it enforces no-arbitrage via replication, not because investors are actually risk-neutral. The two are linked by the market price of risk (Girsanov): you price with risk-neutral but forecast and size risk with real-world.

**Q131.** Why does gamma explode near expiry for at-the-money index options, and what does it mean for weekly Nifty/Bank Nifty expiries?

For an at-the-money option, gamma scales roughly as 1/(S*sigma*sqrt(T)), so as T -> 0 gamma blows up and tiny spot moves cause huge delta swings. On NSE weekly expiries, dealers short these cheap near-dated options carry enormous gamma, and their delta-hedging forces large index buying/selling that can pin price near big open-interest strikes or amplify intraday moves on expiry day. This is why expiry sessions see sharp, mean-reverting moves around key strikes and why short-gamma sellers can be badly hurt by a single large move.

## Rate/FX Derivatives

**Q132.** What is an interest-rate swap (IRS)?

An interest-rate swap is an OTC contract in which two parties agree to exchange interest payments on a notional principal: typically one party pays a fixed rate while the other pays a floating rate (e.g. SOFR, EURIBOR, or in India MIBOR/MIFOR). Only interest cash flows are exchanged, and they are usually netted, so it is a tool to transform the interest character of an asset or liability without touching the underlying principal. A "plain vanilla" IRS is fixed-for-floating in a single currency.

**Q133.** In a plain-vanilla IRS, is the notional principal exchanged?

No. The notional is purely a reference amount used to compute the interest cash flows; it is never exchanged in a single-currency interest-rate swap. This is the key difference from a currency swap, where principal usually is exchanged. Because principal stays put, the credit exposure of an IRS is far smaller than its notional suggests.

**Q134.** What does "net settlement" mean in a swap?

On each payment date both legs are calculated, and only the difference between the fixed and floating amounts changes hands, paid by whichever party owes more. For example, on a USD 10m notional, if the fixed payer owes 5% (USD 500k for the year) and the floating receiver is owed 4.5% (USD 450k), only USD 50k is paid by the fixed payer. Netting reduces settlement risk and the size of cash flows actually moving.

**Q135.** Why would a company use an interest-rate swap?

The classic motive is converting floating-rate debt into fixed-rate (to lock in costs and hedge against rising rates) or vice versa. A firm with a floating loan can enter a "pay-fixed, receive-floating" swap: the floating it receives offsets the floating it owes on the loan, leaving it with a net fixed cost. Swaps also let firms exploit comparative advantage in different markets, manage duration, and speculate on rate moves.

**Q136.** Explain the comparative-advantage argument for swaps.

If Company A borrows more cheaply in fixed and Company B more cheaply in floating, but each actually wants the other type, they can each borrow where they have an advantage and swap. The total interest saving (the difference between the two fixed spreads and the two floating spreads) is shared between them, so both end up paying less than borrowing directly in their preferred market. Critics note part of this "free lunch" reflects hidden credit-risk differences and renewal risk in floating rates.

**Q137.** A firm has a floating loan at MIBOR+150 bps and wants certainty. How does a swap help?

It enters a pay-fixed/receive-MIBOR swap on the same notional, say paying 7% fixed and receiving MIBOR. Its net cost becomes (MIBOR + 1.50%) on the loan minus MIBOR received plus 7% paid = 8.50% fixed. The floating exposure cancels, locking the all-in cost at 8.50% regardless of where MIBOR moves.

**Q138.** Why is the value of a swap approximately zero at initiation?

At inception the fixed rate (the swap rate) is set precisely so that the present value of the fixed leg equals the present value of the expected floating leg, so neither party pays the other to enter. As market rates move afterward, one leg becomes more valuable and the swap acquires positive value to one party and negative to the other. V_mid = PV(fixed leg) - PV(floating leg) = 0 at t=0.

**Q139.** How can a swap be valued as a portfolio of bonds?

To the fixed-rate receiver, a swap equals being long a fixed-coupon bond and short a floating-rate bond: V = B_fixed - B_floating. The fixed bond is discounted at current rates; the floating-rate bond resets to par at each reset, so right after a reset it is worth its notional. Thus immediately after a reset, V (to fixed receiver) = B_fixed - Notional.

**Q140.** How can a swap be valued as a series of FRAs?

Each exchange of fixed-for-floating on a future date is economically a forward rate agreement: you can value each settlement by replacing the unknown future floating rate with today's forward rate, compute the net cash flow, and discount it back. The swap value is the sum of these discounted FRA values. This "strip of FRAs" view and the bond view give the same answer.

**Q141.** What is the swap rate?

The swap rate is the fixed rate that makes a new swap have zero value at initiation, i.e. the fixed rate at which PV(fixed leg) = PV(floating leg). It equals a weighted average of the forward rates implied by the curve. Formula: swap rate = (1 - DF_n) / (sum of DF_i * tau_i), where DF are discount factors and tau the accrual fractions.

**Q142.** What is the swap curve and why does it matter?

The swap curve plots par swap rates against maturity (2y, 5y, 10y, etc.) and is a key benchmark term structure, often more liquid than government bonds in some tenors. It is used to discount cash flows, price other derivatives, and gauge market rate expectations and credit/liquidity conditions. In India, the INR OIS (MIBOR-based) curve serves this role for rupee rates.

**Q143.** What is a forward rate agreement (FRA)?

An FRA is an OTC contract that fixes an interest rate on a notional for a future period; one party locks a borrowing/lending rate today for, say, a 3-month period starting in 6 months (a "6x9 FRA"). At settlement only the difference between the agreed rate and the realized reference rate is exchanged. It is effectively a single-period building block of a swap.

**Q144.** What is the payoff of an FRA and how is it settled?

Payoff to the fixed-rate payer (borrower) = Notional * (R_reference - R_FRA) * (days/360) / (1 + R_reference*(days/360)). The cash flow is settled at the start of the reference period, so it is discounted back from the period end, which is why the divisor appears. If realized rates exceed the locked rate, the fixed payer (who feared rising rates) receives the payment.

**Q145.** Worked FRA example: 6x12 FRA, notional USD 5m, agreed 4.00%, settles at 5.00%.

The period is 6 months (~182 days, ~0.5 year). Unadjusted gain to the fixed payer = 5m * (5.00% - 4.00%) * 0.5 = USD 25,000. Discounted to settlement at the start of the period: 25,000 / (1 + 0.05*0.5) = USD 24,390. The borrower who locked 4% benefits because rates rose to 5%.

**Q146.** What was LIBOR and why is the market transitioning away from it?

LIBOR (London Interbank Offered Rate) was a survey-based estimate of unsecured interbank borrowing costs, long used as the floating benchmark for trillions in loans and derivatives. It was discredited by the 2012 rigging scandal and undermined by the collapse of actual interbank lending, making it manipulable and unrepresentative. Regulators ceased its publication (USD LIBOR's last panel rates ended June 2023), forcing a move to transaction-based risk-free rates.

**Q147.** What is SOFR and how does it differ from LIBOR?

SOFR (Secured Overnight Financing Rate) is the US replacement: an overnight rate based on actual secured (repo) Treasury transactions, making it robust and nearly manipulation-proof. Unlike term, forward-looking, unsecured LIBOR, SOFR is overnight, secured (so it carries almost no bank-credit premium), and is typically compounded in arrears to build term rates. Because it lacks LIBOR's credit spread, contracts add a fixed spread adjustment (e.g. ~26 bps for 3-month USD) when converting.

**Q148.** Name the risk-free reference rates in major markets.

US: SOFR; UK: SONIA; Euro area: ESTR (and EURIBOR still survives reformed); Switzerland: SARON; Japan: TONA. India uses MIBOR (Mumbai Interbank Offer Rate / FBIL overnight MIBOR) as the basis for the rupee OIS market, plus MIFOR for FX-implied rupee rates. These are largely overnight, transaction-anchored rates compounded for term exposure.

**Q149.** What is OIS and what is OIS discounting?

An Overnight Indexed Swap exchanges a fixed rate for the geometric average of an overnight index (SOFR, ESTR, or MIBOR in India) over the period. Post-2008, dealers shifted to "OIS discounting" — using the OIS curve, not LIBOR, to discount collateralized swap cash flows, because cash collateral earns the overnight rate, making OIS the true funding/discount rate. This better reflects the near-risk-free cost of funding posted collateral.

**Q150.** What is a currency swap?

A currency swap exchanges principal and interest payments in one currency for principal and interest in another. Unlike an IRS, the principal usually IS exchanged at the start and re-exchanged at maturity (at the original spot rate). It lets a firm raise cheap funding in one currency and convert it into the currency it actually needs while hedging both interest and FX exposure.

**Q151.** What is cross-currency basis?

The cross-currency basis is the spread added to one leg of a cross-currency swap that deviates from what covered interest parity would predict, reflecting supply/demand imbalances for funding in a given currency. A negative USD basis means non-US borrowers pay a premium to swap into dollars, common in stress periods when dollar funding is scarce. It is a market measure of how expensive it is to obtain a currency via the FX swap market.

**Q152.** What is an FX forward?

An FX forward is an OTC agreement to exchange two currencies at a fixed rate on a future date, locking in the exchange rate today and removing uncertainty about the future spot. An importer owing USD in 3 months can buy USD forward to fix its INR cost. The forward rate is determined by spot and the interest-rate differential, not by a forecast of the future spot.

**Q153.** State covered interest rate parity (CIP).

CIP says the forward exchange rate is pinned by the interest-rate differential, otherwise arbitrage is possible: F = S * (1 + r_domestic) / (1 + r_foreign), where rates are for the contract horizon and S, F are quoted as domestic per foreign. The currency with the higher interest rate trades at a forward discount, exactly offsetting its rate advantage so no risk-free profit exists.

**Q154.** Worked CIP example: INR/USD, spot 83.00, INR rate 7%, USD rate 5%, 1 year.

Treating INR as domestic and USD as foreign: F = 83.00 * (1 + 0.07) / (1 + 0.05) = 83.00 * 1.07/1.05 = 83.00 * 1.01905 = 84.58. So the 1-year USD/INR forward is about 84.58, i.e. USD is at a forward premium of ~1.58 rupees because INR's higher rate must be offset.

**Q155.** What is a forward premium versus a forward discount?

A currency is at a forward premium if it is more expensive to buy forward than spot, and at a discount if cheaper. Annualized forward premium ~ (F - S)/S * (12/months). By CIP the low-interest-rate currency trades at a forward premium and the high-rate currency at a discount; in INR/USD terms the rupee, with higher rates, trades at a forward discount (you get more INR per USD forward).

**Q156.** How does an FX swap differ from a currency swap?

An FX swap is a single contract combining a spot (or near-date) exchange with a simultaneous reverse forward exchange of the same two currencies — it is a short-dated funding/rollover tool with no intermediate interest payments; the rate differential is baked into the forward points. A cross-currency (currency) swap is longer-dated and involves periodic interest payments on both legs throughout its life. In short: FX swap = two principal exchanges, no coupons; currency swap = principal plus a stream of interest payments.

**Q157.** What is an interest-rate cap, and how does it relate to caplets?

A cap is an option-based hedge that pays the holder whenever a floating reference rate rises above a strike (cap) rate, effectively setting a ceiling on borrowing cost. It is a strip (portfolio) of "caplets," one per reset period, each a call option on the interest rate. Caplet payoff = Notional * max(R_reference - R_strike, 0) * (days/360), and the cap premium is the sum of the caplet premiums.

**Q158.** What are floors and collars?

A floor is the mirror image of a cap: a strip of "floorlets" (puts on the rate) that pays when the floating rate falls below a strike, guaranteeing a minimum return to a lender/investor. A collar combines buying a cap and selling a floor (for a borrower), so the rate is confined to a band; the premium received from the sold floor offsets the cost of the bought cap, and a "zero-cost collar" sets strikes so net premium is nil.

**Q159.** What is a swaption?

A swaption is an option granting the right, but not the obligation, to enter a swap at a preset fixed rate on a future date. A "payer swaption" gives the right to pay fixed/receive floating (valuable if rates rise); a "receiver swaption" gives the right to receive fixed (valuable if rates fall). Firms use them to hedge anticipated financing or to lock a future borrowing rate with optionality, paying an upfront premium.

**Q160.** What is basis risk in interest-rate/FX hedging?

Basis risk is the residual risk that a hedge does not move perfectly with the exposure because the hedge references a different rate, index, or tenor than the underlying. For example, hedging a loan tied to 1-month MIBOR with a 3-month MIBOR swap, or hedging SOFR-linked debt against a term-rate exposure, leaves a "basis" that can move against you. It is why LIBOR-to-SOFR transition and tenor mismatches matter to hedgers.

**Q161.** How did post-2008 reform change swap markets via clearing and netting, and what is India's framework?

After 2008, the G20 mandated that standardized OTC derivatives be centrally cleared through CCPs (which novate trades and net exposures), reported to trade repositories, and margined, sharply reducing counterparty risk; netting agreements (ISDA master agreements) collapse many trades into a single net obligation on default. In India, rupee IRS/OIS and MIFOR swaps clear through the Clearing Corporation of India (CCIL), while currency and FX derivatives are jointly regulated by RBI and SEBI — exchange-traded currency futures/options trade on NSE/BSE with RBI-set position limits, and OTC forwards require an underlying exposure under RBI's FEMA rules.
