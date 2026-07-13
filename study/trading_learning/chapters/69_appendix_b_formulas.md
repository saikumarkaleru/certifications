# Appendix B: Formula Cheat-Sheet

Every key formula from the book in one place. Notation: S = spot/underlying price, K = strike, T = time to expiry in years, r = risk-free rate (annual, continuous), q = dividend (or index dividend) yield, sigma = volatility (annual), premium = option price paid/received, N() = standard normal cumulative distribution, N'() = standard normal density. All prices in rupees; use `*` for multiply, `^` for power.

## Payoffs at expiry (per share, before costs)

- `Long call payoff = max(S - K, 0) - premium` — buyer profits if spot finishes above strike by more than the premium.
- `Short call payoff = premium - max(S - K, 0)` — seller keeps premium; loss grows as spot rises above strike.
- `Long put payoff = max(K - S, 0) - premium` — buyer profits if spot finishes below strike by more than the premium.
- `Short put payoff = premium - max(K - S, 0)` — seller keeps premium; loss grows as spot falls below strike.

## Vertical spreads (two strikes, K_low < K_high; width = K_high - K_low)

- `Bull call spread (debit): net debit = premium_long - premium_short` — buy K_low call, sell K_high call.
- `Bull call max profit = width - net debit` — reached at or above K_high.
- `Bull call max loss = net debit` — reached at or below K_low.
- `Bull call breakeven = K_low + net debit` — spot needed at expiry to recover the debit.
- `Bear put spread (debit): net debit = premium_long - premium_short` — buy K_high put, sell K_low put.
- `Bear put max profit = width - net debit` — reached at or below K_low.
- `Bear put max loss = net debit` — reached at or above K_high.
- `Bear put breakeven = K_high - net debit` — spot at expiry that recovers the debit.
- `Bull put spread (credit): net credit = premium_short - premium_long` — sell K_high put, buy K_low put.
- `Bull put max profit = net credit` — reached at or above K_high.
- `Bull put max loss = width - net credit` — reached at or below K_low.
- `Bull put breakeven = K_high - net credit` — below this you start losing.
- `Bear call spread (credit): net credit = premium_short - premium_long` — sell K_low call, buy K_high call.
- `Bear call max profit = net credit` — reached at or below K_low.
- `Bear call max loss = width - net credit` — reached at or above K_high.
- `Bear call breakeven = K_low + net credit` — above this you start losing.

General rule: `Credit-spread max loss = width - net credit`, and `width = max profit + max loss` for any one-width vertical.

## Straddles and strangles

- `Long straddle cost = call premium + put premium` — same strike K, buying both.
- `Long straddle upper breakeven = K + total premium`; `lower breakeven = K - total premium` — needs a big move either way.
- `Short straddle: profit zone = K - total premium to K + total premium` — seller keeps premium if spot stays inside; loss is unlimited outside.
- `Long strangle cost = call premium + put premium` — OTM call at K_call, OTM put at K_put (K_put < K_call).
- `Long strangle upper breakeven = K_call + total premium`; `lower breakeven = K_put - total premium` — cheaper than a straddle, needs a larger move.

## Butterflies and condors (defined-risk, four legs)

- `Long butterfly cost = net debit` — buy 1 K_low, sell 2 K_mid, buy 1 K_high (equal wing widths).
- `Butterfly max profit = wing width - net debit` — at spot = K_mid at expiry.
- `Butterfly max loss = net debit` — outside the wings.
- `Butterfly breakevens = K_low + net debit and K_high - net debit`.
- `Iron butterfly credit = net credit` — sell ATM straddle, buy protective wings.
- `Iron butterfly max profit = net credit` (at K_mid); `max loss = wing width - net credit`.
- `Iron condor credit = net credit` — sell OTM put spread + sell OTM call spread.
- `Iron condor max profit = net credit` (spot between the short strikes); `max loss = wider wing width - net credit`.
- `Iron condor breakevens = short put strike - net credit and short call strike + net credit`.

## Covered call and collar

- `Covered call breakeven = stock cost - call premium received` — long stock + short call.
- `Covered call max profit = (call strike - stock cost) + call premium` — capped if assigned at the strike.
- `Collar cost = put premium paid - call premium received` — long stock + protective put + short call.
- `Collar max loss = stock cost - put strike + collar cost`; `max profit = call strike - stock cost - collar cost` — floor and ceiling on the stock.

## Value: intrinsic and time value

- `Intrinsic value (call) = max(S - K, 0)` — the in-the-money amount of a call right now.
- `Intrinsic value (put) = max(K - S, 0)` — the in-the-money amount of a put right now.
- `Time value = premium - intrinsic value` — the part of the price that decays to zero by expiry.

## Pricing models

### Put-call parity (European options)

- `C - P = S - K*e^(-r*T)` — links call and put prices on the same strike/expiry (no dividends).
- `C - P = S*e^(-q*T) - K*e^(-r*T)` — dividend (index yield q) form; for cash dividends, subtract their present value from S.

### Black-Scholes (European, no dividends)

- `C = S*N(d1) - K*e^(-r*T)*N(d2)` — fair value of a European call.
- `P = K*e^(-r*T)*N(-d2) - S*N(-d1)` — fair value of a European put.
- `d1 = (ln(S/K) + (r + 0.5*sigma^2)*T) / (sigma*sqrt(T))` — standardized moneyness plus drift.
- `d2 = d1 - sigma*sqrt(T)` — d1 shifted by one volatility unit; N(d2) approx the risk-neutral chance of finishing ITM.

### Merton (Black-Scholes with continuous dividend / index yield q)

- `C = S*e^(-q*T)*N(d1) - K*e^(-r*T)*N(d2)` — call with dividend yield.
- `P = K*e^(-r*T)*N(-d2) - S*e^(-q*T)*N(-d1)` — put with dividend yield.
- `d1 = (ln(S/K) + (r - q + 0.5*sigma^2)*T) / (sigma*sqrt(T))`; `d2 = d1 - sigma*sqrt(T)` — drift now uses (r - q).

### Binomial (one step; u = up factor, d = down factor)

- `p = (e^(r*T) - d) / (u - d)` — risk-neutral probability of an up move (use (r - q) in the exponent if there is a yield).
- `Option price = e^(-r*T) * (p*payoff_up + (1 - p)*payoff_down)` — discounted expected payoff under p.
- `u = e^(sigma*sqrt(dt))`, `d = 1/u` — Cox-Ross-Rubinstein step sizes for a step of length dt.

### Futures fair value

- `F = S*e^((r - q)*T)` — fair forward/futures price; q is the dividend/index yield (cost-of-carry model).

## Greeks (per share; Merton forms, q = 0 if no yield)

- `Delta (call) = e^(-q*T)*N(d1)` — change in option price per 1 rupee move in spot; ranges 0 to +1.
- `Delta (put) = e^(-q*T)*(N(d1) - 1)` — ranges -1 to 0.
- `Gamma = e^(-q*T)*N'(d1) / (S*sigma*sqrt(T))` — change in delta per 1 rupee move; same for calls and puts, highest ATM near expiry.
- `Vega = S*e^(-q*T)*N'(d1)*sqrt(T)` — change in price per 1.00 (100 percentage-point) change in sigma; divide by 100 for a 1-point IV move. Same for calls and puts.
- `Theta (call) = -S*e^(-q*T)*N'(d1)*sigma/(2*sqrt(T)) - r*K*e^(-r*T)*N(d2) + q*S*e^(-q*T)*N(d1)` — time decay per year; divide by 365 for per-day. Usually negative for long options.
- `Theta (put) = -S*e^(-q*T)*N'(d1)*sigma/(2*sqrt(T)) + r*K*e^(-r*T)*N(-d2) - q*S*e^(-q*T)*N(-d1)` — put time decay per year.
- `Rho (call) = K*T*e^(-r*T)*N(d2)`; `Rho (put) = -K*T*e^(-r*T)*N(-d2)` — change in price per 1.00 (100bp) change in r; divide by 100 for a 1bp move.
- `dP ~ delta*dS + 0.5*gamma*dS^2 + theta*dt + vega*dIV` — daily P&L approximation: directional + curvature + decay + vol change.

## Volatility

- `Historical vol = stdev(daily log returns) * sqrt(252)` — annualised realised vol; log return = ln(close_today / close_yesterday), 252 trading days.
- `Expected move ~ Spot * IV * sqrt(T)` — approximate one-standard-deviation range over time T (T in years, IV as a decimal).
- `Daily expected move ~ Spot * (VIX/100) / sqrt(252)` — India VIX day-count shortcut for a one-day move (equivalently Spot * IV / sqrt(252)).
- `Monthly expected move ~ Spot * (VIX/100) / sqrt(12)` — VIX is annual; divide by sqrt(12) for one month.
- `IV rank = (IV_now - IV_low) / (IV_high - IV_low) * 100` — where current IV sits in its 52-week range, 0 to 100.
- `IV_next = IV_now - (model_price - market_price) / vega` — Newton-Raphson step to back out implied vol; repeat until model_price matches market_price (vega here is per 1.00 of vol).

## Risk and position sizing

- `Risk per trade = account size * risk percent` — typically 1 to 2 percent (e.g. 0.01 to 0.02).
- `Position size (lots) = (account size * risk percent) / (max loss per lot)` — round down to whole lots; max loss per lot in rupees.
- `Expectancy = win% * avg_win - loss% * avg_loss` — average rupees (or R) earned per trade; must be positive to have an edge.
- `R-multiple = trade profit or loss / initial risk (1R)` — outcome measured in units of the amount risked; a +3R win returns three times the risk.
- `Kelly fraction f = W - (1 - W)/R` — fraction of capital to risk, where W = win probability and R = avg_win/avg_loss (payoff ratio). Most traders use a fraction (half or quarter) of f.
- `Drawdown recovery = L / (1 - L)` — gain needed to recover a loss of fraction L (e.g. a 0.50 drawdown needs +1.00, i.e. +100 percent, to break even).
