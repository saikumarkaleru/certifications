# Chapter 62: Pricing Options in Python — A Black-Scholes & Greeks Engine

Every professional options desk runs on a pricing engine. When a trader on a Mumbai prop desk glances at a screen and sees that a Nifty 24000 call is "trading two vols cheap," there is a small piece of software behind that judgement: it takes the spot, the strike, the time left, the interest rate, and an implied volatility, and it turns them into a price and a set of Greeks in microseconds. That engine is not magic. It is a few dozen lines of arithmetic that you can write yourself, understand fully, and trust.

This chapter is a hands-on build. By the end you will have a working Black-Scholes-Merton pricer written from scratch in Python — no quant libraries, just the standard library — plus the five analytic Greeks, an implied-volatility solver, and a small test harness that proves the whole thing is correct. The intuition comes first in plain English; the code is the worked example. If you have read the earlier chapters on Black-Scholes and the Greeks, this is where that theory becomes a tool you own.

## Core concepts

### Why build it yourself

You can pull option prices off the NSE site or your broker's terminal. So why write a pricer? Three reasons. First, the market only quotes prices; it does not hand you the Greeks, and the Greeks are how you actually manage risk. Second, to find *implied volatility* — the single most important number in options — you must invert the pricing formula, and that requires the formula in code. Third, when you build it yourself you understand every assumption, so you know exactly when to trust the output and when the model is lying to you. A black box you cannot inspect is a liability on a trading desk.

### The Black-Scholes-Merton formula, in words

Black-Scholes says the fair price of a European option is the *expected payoff at expiry, discounted back to today*, under a specific assumption: that the underlying drifts and diffuses like a lognormal random walk with constant volatility. Index options on the NSE (Nifty, Bank Nifty) are European and cash-settled, which is exactly what this model assumes — so it fits Indian index options cleanly.

The formula for a call with a continuous dividend yield `q` is:

`Call = S * exp(-q*T) * N(d1) - K * exp(-r*T) * N(d2)`

`Put  = K * exp(-r*T) * N(-d2) - S * exp(-q*T) * N(-d1)`

where

`d1 = (ln(S/K) + (r - q + 0.5*sigma^2) * T) / (sigma * sqrt(T))`

`d2 = d1 - sigma * sqrt(T)`

Here `S` is spot, `K` is strike, `T` is time to expiry in years, `r` is the risk-free rate (continuously compounded), `q` is the dividend yield, `sigma` is volatility, and `N()` is the standard normal cumulative distribution function (CDF). Read it intuitively: the first term in the call is roughly "the share you would receive, value-weighted by the chance you finish in the money," and the second term is "the cash you must pay out, weighted by the chance you actually pay it." `N(d2)` is, in the risk-neutral world, the probability the call expires in the money.

For Indian index options, `q` is usually small but not zero — the index has a dividend yield of roughly 1 to 1.5 percent a year. We keep `q` in the formula so the same engine prices both index and single-stock options.

### The one function everything depends on: the normal CDF

Python's `math` module has no normal CDF, but it has `math.erf`, the error function, and the two are related by a clean identity:

`N(x) = 0.5 * (1 + erf(x / sqrt(2)))`

That single line gives us an accurate CDF with no external dependency. We will also need the normal *probability density function* (PDF), `n(x) = exp(-x^2/2) / sqrt(2*pi)`, for the Greeks.

### The Greeks, intuitively

The Greeks are the partial derivatives of the price — they tell you how the option's value reacts to each input moving.

- **Delta** — sensitivity to spot. How much the premium moves per one-point move in Nifty. For a call it runs 0 to 1; for a put, -1 to 0.
- **Gamma** — how fast delta itself changes. High gamma means your delta is unstable, which is the curvature that makes long options exciting and short options dangerous near expiry.
- **Vega** — sensitivity to a one-percentage-point change in volatility. When India VIX jumps, vega tells you how much your option re-prices.
- **Theta** — time decay. How much value bleeds out per day as expiry approaches. It is the rent a buyer pays and a seller collects.
- **Rho** — sensitivity to interest rates. The least important for short-dated index options, but we include it for completeness.

### Implied volatility: running the formula backwards

Six inputs go into Black-Scholes, and five of them are observable: spot, strike, time, rate, dividend. The sixth, volatility, is not. So traders flip the problem: take the *market price* of the option as given, and ask "what volatility makes my model output that price?" That answer is the **implied volatility (IV)**. There is no closed-form way to solve for it, so we solve numerically — usually with Newton-Raphson, using vega as the derivative, and a bisection fallback for safety.

## Worked example (₹, Nifty/Bank Nifty)

Let us price an at-the-money weekly Nifty option. Suppose Nifty spot is 24000, we look at the 24000 strike, there are 7 days to expiry, the risk-free rate is 6.5 percent, the dividend yield is 1.2 percent, and the implied volatility is 13 percent (a typical calm-market India VIX level).

In years, `T = 7/365 = 0.01918`. With `sigma = 0.13`:

`sigma * sqrt(T) = 0.13 * sqrt(0.01918) = 0.13 * 0.13849 = 0.018004`

`d1 = (ln(24000/24000) + (0.065 - 0.012 + 0.5*0.13^2)*0.01918) / 0.018004`

The log term is 0, and `(0.065 - 0.012 + 0.00845) = 0.06145`, times `T` gives `0.001179`. So `d1 = 0.001179 / 0.018004 = 0.0655` and `d2 = 0.0655 - 0.018004 = 0.0475`. Both are close to zero, as expected for an at-the-money option. Feeding those through the CDF and discounting gives a call premium of roughly ₹185 per unit of the index (we will let the code produce the exact figure below). The Greeks will show a delta near 0.53, a fat gamma and theta because expiry is close, and a vega telling us how many rupees we gain per one-vol rise in IV.

Now the engine itself.

### The pricer

```python
import math

SQRT_2PI = math.sqrt(2.0 * math.pi)

def norm_cdf(x):
    """Standard normal CDF N(x), built from math.erf (no SciPy needed)."""
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))

def norm_pdf(x):
    """Standard normal PDF n(x) = exp(-x^2/2) / sqrt(2*pi)."""
    return math.exp(-0.5 * x * x) / SQRT_2PI

def _d1_d2(S, K, T, r, sigma, q=0.0):
    """Helper: the two Black-Scholes-Merton arguments d1 and d2."""
    # Guard against zero time or zero vol, which would divide by zero.
    if T <= 0 or sigma <= 0:
        raise ValueError("T and sigma must be positive for d1/d2.")
    vol_sqrt_t = sigma * math.sqrt(T)
    d1 = (math.log(S / K) + (r - q + 0.5 * sigma * sigma) * T) / vol_sqrt_t
    d2 = d1 - vol_sqrt_t
    return d1, d2

def bs_price(S, K, T, r, sigma, q=0.0, option="call"):
    """Black-Scholes-Merton price for a European call or put.

    S     : spot price of the underlying (e.g. Nifty level)
    K     : strike price
    T     : time to expiry in YEARS
    r     : continuously-compounded risk-free rate (e.g. 0.065)
    sigma : volatility as a decimal (e.g. 0.13 for 13%)
    q     : continuous dividend yield (e.g. 0.012)
    option: 'call' or 'put'
    """
    # Handle the expiry edge case: at T=0 the option is worth its intrinsic value.
    if T <= 0:
        intrinsic = max(S - K, 0.0) if option == "call" else max(K - S, 0.0)
        return intrinsic

    d1, d2 = _d1_d2(S, K, T, r, sigma, q)
    disc_r = math.exp(-r * T)   # discount factor for the strike cash flow
    disc_q = math.exp(-q * T)   # discount factor for the dividend-paying spot

    if option == "call":
        return S * disc_q * norm_cdf(d1) - K * disc_r * norm_cdf(d2)
    elif option == "put":
        return K * disc_r * norm_cdf(-d2) - S * disc_q * norm_cdf(-d1)
    else:
        raise ValueError("option must be 'call' or 'put'")
```

A few things to notice. We isolate `d1`/`d2` in a helper because both the pricer and several Greeks need them — write it once, reuse it. We handle `T <= 0` by returning intrinsic value, because a model that throws an exception at expiry is useless in a live system. And every input that changes meaning (decimal vs percent, years vs days) is documented in the docstring, because the single most common bug in a pricer is passing 13 instead of 0.13, or 7 instead of 7/365.

### The Greeks

```python
def bs_greeks(S, K, T, r, sigma, q=0.0, option="call"):
    """Analytic Black-Scholes-Merton Greeks, returned as a dict.

    Conventions used (the desk-standard ones):
      delta : per 1.0 move in spot
      gamma : per 1.0 move in spot
      vega  : per 1 percentage-point (0.01) change in sigma
      theta : per CALENDAR DAY (annual theta / 365)
      rho   : per 1 percentage-point (0.01) change in r
    """
    d1, d2 = _d1_d2(S, K, T, r, sigma, q)
    disc_r = math.exp(-r * T)
    disc_q = math.exp(-q * T)
    pdf_d1 = norm_pdf(d1)
    sqrt_t = math.sqrt(T)

    # Gamma and vega are identical for calls and puts.
    gamma = disc_q * pdf_d1 / (S * sigma * sqrt_t)
    vega = S * disc_q * pdf_d1 * sqrt_t          # per 1.00 change in sigma...
    vega = vega * 0.01                           # ...scaled to per 1 vol point

    if option == "call":
        delta = disc_q * norm_cdf(d1)
        # Annual theta: time decay + carry terms, then divide by 365 for per-day.
        theta_annual = (
            -(S * disc_q * pdf_d1 * sigma) / (2.0 * sqrt_t)
            - r * K * disc_r * norm_cdf(d2)
            + q * S * disc_q * norm_cdf(d1)
        )
        rho = K * T * disc_r * norm_cdf(d2) * 0.01
    elif option == "put":
        delta = -disc_q * norm_cdf(-d1)
        theta_annual = (
            -(S * disc_q * pdf_d1 * sigma) / (2.0 * sqrt_t)
            + r * K * disc_r * norm_cdf(-d2)
            - q * S * disc_q * norm_cdf(-d1)
        )
        rho = -K * T * disc_r * norm_cdf(-d2) * 0.01
    else:
        raise ValueError("option must be 'call' or 'put'")

    theta = theta_annual / 365.0   # per-calendar-day decay

    return {
        "delta": delta,
        "gamma": gamma,
        "vega": vega,
        "theta": theta,
        "rho": rho,
    }
```

The scaling choices matter and they are where engines silently disagree. We report vega per *one vol point* (a 0.01 move in sigma) and rho per *one percent* rate move, because that is how traders think — "this position is long ₹4,000 of vega" means ₹4,000 per vol point. Theta is per calendar day, the annual figure divided by 365, because a trader wants to know the overnight bleed. Always state your conventions; a delta is unambiguous but vega and theta are not.

![Figure: Theta — option value decaying as expiry approaches](figs/theta.png)

### Implied volatility: Newton-Raphson with a bisection fallback

```python
def implied_vol(price, S, K, T, r, q=0.0, option="call",
                tol=1e-6, max_iter=100):
    """Solve for the implied volatility that reproduces `price`.

    Strategy: Newton-Raphson using vega as the derivative (fast), with a
    bisection fallback if Newton misbehaves (robust). Returns sigma or None.
    """
    # Sanity bounds: the price must lie between intrinsic and the spot/strike.
    if T <= 0 or price <= 0:
        return None

    intrinsic = (max(S - K, 0.0) * math.exp(-q * T)) if option == "call" \
        else (max(K - S, 0.0) * math.exp(-r * T))
    if price < intrinsic:
        return None  # price below intrinsic => no real IV (arbitrage / bad quote)

    # --- Newton-Raphson ---
    sigma = 0.20  # a sensible starting guess (~20% vol)
    for _ in range(max_iter):
        model = bs_price(S, K, T, r, sigma, q, option)
        diff = model - price
        if abs(diff) < tol:
            return sigma
        # vega here is the RAW derivative dPrice/dSigma (not the 1%-scaled one).
        d1, _ = _d1_d2(S, K, T, r, sigma, q)
        vega_raw = S * math.exp(-q * T) * norm_pdf(d1) * math.sqrt(T)
        if vega_raw < 1e-8:
            break  # vega too small, Newton will blow up -> fall back
        sigma = sigma - diff / vega_raw
        if sigma <= 0 or sigma > 5:   # ran outside a sane range -> fall back
            break

    # --- Bisection fallback (slow but cannot diverge) ---
    low, high = 1e-4, 5.0
    p_low = bs_price(S, K, T, r, low, q, option) - price
    p_high = bs_price(S, K, T, r, high, q, option) - price
    if p_low * p_high > 0:
        return None  # price not bracketed in [0.01%, 500%] vol -> give up
    for _ in range(max_iter):
        mid = 0.5 * (low + high)
        p_mid = bs_price(S, K, T, r, mid, q, option) - price
        if abs(p_mid) < tol:
            return mid
        if p_low * p_mid < 0:
            high = mid
        else:
            low, p_low = mid, p_mid
    return 0.5 * (low + high)
```

Why two methods? Newton-Raphson is fast: it uses the slope (vega) to leap toward the answer, typically converging in three or four steps. But it can misbehave — for deep in- or out-of-the-money options vega is tiny, and dividing by a tiny number sends Newton flying off to a negative or absurd volatility. The fix is a guard: if Newton wanders out of `(0, 5)` or vega collapses, we switch to **bisection**, which simply brackets the answer between 0.01 percent and 500 percent vol and halves the interval repeatedly. Bisection is slower but it cannot diverge as long as the price is bracketed. Fast-but-fragile with a slow-but-safe backup is the standard pattern for any numerical solver on a desk.

### Verifying the engine

Code that prices options is worthless if it is wrong, and pricing bugs are silent — the number looks plausible. So we verify three independent ways.

```python
def verify_engine():
    """Three independent correctness checks. Each prints PASS/FAIL."""
    S, K, T, r, q, sigma = 24000, 24000, 7/365, 0.065, 0.012, 0.13

    # 1) Round-trip: price an option, recover its IV, re-price.
    c = bs_price(S, K, T, r, sigma, q, "call")
    iv = implied_vol(c, S, K, T, r, q, "call")
    print(f"[1] Round-trip IV: input {sigma:.4f} -> recovered {iv:.4f}",
          "PASS" if abs(iv - sigma) < 1e-4 else "FAIL")

    # 2) Put-call parity: C - P = S*exp(-qT) - K*exp(-rT)
    p = bs_price(S, K, T, r, sigma, q, "put")
    lhs = c - p
    rhs = S * math.exp(-q * T) - K * math.exp(-r * T)
    print(f"[2] Put-call parity: C-P={lhs:.4f}, theory={rhs:.4f}",
          "PASS" if abs(lhs - rhs) < 1e-6 else "FAIL")

    # 3) Finite-difference check on delta: bump spot by a small h.
    h = 1.0
    up = bs_price(S + h, K, T, r, sigma, q, "call")
    dn = bs_price(S - h, K, T, r, sigma, q, "call")
    fd_delta = (up - dn) / (2 * h)          # numerical central difference
    an_delta = bs_greeks(S, K, T, r, sigma, q, "call")["delta"]  # analytic
    print(f"[3] Delta: analytic={an_delta:.5f}, finite-diff={fd_delta:.5f}",
          "PASS" if abs(an_delta - fd_delta) < 1e-4 else "FAIL")
```

Each check tests something different. The **round-trip** proves the pricer and the IV solver are mutually consistent. **Put-call parity** is a model-free arbitrage relationship — if our call and put do not satisfy it, one of them is wrong, independent of Black-Scholes being right. And the **finite-difference check** confirms our hand-derived analytic delta matches a brute-force numerical derivative: bump spot up and down by ₹1, see how the price moved, and that slope must equal the formula's delta. If all three pass, the engine is trustworthy.

### A short worked run

```python
if __name__ == "__main__":
    # ATM weekly Nifty 24000 call
    S, K, T, r, q, sigma = 24000, 24000, 7/365, 0.065, 0.012, 0.13

    call = bs_price(S, K, T, r, sigma, q, "call")
    put  = bs_price(S, K, T, r, sigma, q, "put")
    g    = bs_greeks(S, K, T, r, sigma, q, "call")

    print(f"Nifty {K} weekly | spot={S} | {round(T*365)}d | IV={sigma:.0%}")
    print(f"  Call premium : Rs {call:,.2f}")
    print(f"  Put  premium : Rs {put:,.2f}")
    print(f"  Delta : {g['delta']:.4f}")
    print(f"  Gamma : {g['gamma']:.6f}")
    print(f"  Vega  : Rs {g['vega']:.2f}  per vol point")
    print(f"  Theta : Rs {g['theta']:.2f}  per day")
    print(f"  Rho   : Rs {g['rho']:.2f}  per 1% rate")

    print()
    verify_engine()
```

Running this prints, approximately:

```
Nifty 24000 weekly | spot=24000 | 7d | IV=13%
  Call premium : Rs 184.71
  Put  premium : Rs 160.33
  Delta : 0.5260
  Gamma : 0.000921
  Vega  : Rs 13.23  per vol point
  Theta : Rs -14.08  per day
  Rho   : Rs 2.39   per 1% rate
[1] Round-trip IV: input 0.1300 -> recovered 0.1300 PASS
[2] Put-call parity: C-P=24.38, theory=24.38 PASS
[3] Delta: analytic=0.52598, finite-diff=0.52598 PASS
```

Read those Greeks like a trader. Delta 0.53 says this call moves like roughly half a unit of Nifty — gain about ₹53 for a 100-point rally. Theta -14.08 says the position bleeds about ₹14 a day to time decay even if Nifty does not move, which for a one-lot (25 units) buyer is about ₹352 of decay per day. Vega 13.23 says if India VIX rises one point, the call gains about ₹13. Those numbers are the whole reason we built the engine: the market gave us only the ₹185 premium, and our code extracted everything else.

This is, in miniature, exactly the kind of engine that sits at the heart of a real quant or options trading project — a market-maker's quoting system, a risk dashboard that aggregates portfolio Greeks across hundreds of NSE strikes, or a backtester that needs theoretical values for instruments that did not trade. The production versions add a volatility surface, an American-option model for single stocks, and a faster vectorised implementation, but the core is precisely what you just wrote.

## Common mistakes / risk note

- **Unit bugs.** Passing time in days instead of years, or volatility as `13` instead of `0.13`, produces a confidently wrong price. This is the number-one pricer bug. Validate inputs and document units obsessively.
- **Trusting the model where it does not apply.** Black-Scholes assumes European exercise, constant volatility, and lognormal returns. NSE *index* options are European and fit well. NSE *single-stock* options are American and physically settled, so this model is an approximation for them — early exercise and the settlement mechanics are not captured.
- **Constant volatility is a fiction.** Real markets show a volatility smile/skew: out-of-the-money Nifty puts trade at higher IVs than ATM options because crash protection is in demand. A single-sigma Black-Scholes does not know this. Feeding it one number per strike (the implied vol of that strike) is how desks cope, but the model itself is blind to the smile.
- **Theta is not free money.** New sellers see positive theta and think they are collecting rent risk-free. They are short gamma — a sharp move against a short option can lose multiples of the premium collected in a single session. The engine will faithfully show you a large negative gamma right before it hurts you; read it.
- **Garbage in from stale quotes.** If you feed `implied_vol` an option price below intrinsic value (common with stale or wide bid-ask quotes near the close), there is no real IV. Our solver returns `None` rather than a fake number — handle that case instead of plotting nonsense.
- **The honest backdrop.** A pricing engine sharpens your edge; it does not create one. SEBI studies show roughly nine in ten retail F&O traders lose money. Better tools help you size, hedge, and avoid mispriced trades — they do not turn a losing strategy into a winning one.

## Key takeaways

- The normal CDF needed for Black-Scholes is one line: `N(x) = 0.5*(1 + erf(x/sqrt(2)))` — no external library required.
- The pricer is just `d1`, `d2`, two discount factors, and the CDF; isolate `d1`/`d2` in a helper since the Greeks reuse it.
- Gamma and vega are the same for calls and puts; delta, theta, and rho differ in sign and detail.
- Always state your Greek conventions: vega per vol point, theta per calendar day, rho per one-percent rate move.
- Implied volatility has no closed form — solve it with fast Newton-Raphson and a bisection fallback that cannot diverge.
- Verify with three independent checks: an IV round-trip, model-free put-call parity, and a finite-difference Greek.
- The model fits European cash-settled index options cleanly; treat single-stock American options as approximations.

## Practice problems

1. **CDF sanity.** Without running code, what are `norm_cdf(0)`, `norm_cdf` of a large positive number, and a large negative number? Why must an at-the-money option have `d1` and `d2` near zero?

2. **Parity by hand.** Using the worked example (call ≈ ₹184.71, put ≈ ₹160.33, S=24000, K=24000, T=7/365, r=6.5%, q=1.2%), verify put-call parity numerically: compute `S*exp(-qT) - K*exp(-rT)` and check it equals C − P.

3. **Extend the engine.** Write a function `portfolio_greeks(positions)` that takes a list of `(option_dict, quantity)` tuples and returns the net delta, gamma, vega, and theta of the book. (Conceptual: describe the structure and the one-line aggregation.)

4. **IV from a market quote.** A Bank Nifty 52000 weekly call (S=52000, T=5/365, r=6.5%, q=1.2%) is quoted at ₹360 in the market. Roughly, will the implied vol be higher or lower than 13%, and how would you get the exact number using the engine?

5. **Theta and lot size.** The ATM Nifty call shows theta of −₹14.08 per day. If the Nifty lot size is 25, what is the daily rupee decay for one long call lot, and what does that mean for a buyer who is right on direction but a week early?

6. **Where the model breaks.** A trader prices a deep out-of-the-money Nifty 26000 put with the engine and gets a tiny premium. Name two reasons the real market price could be meaningfully higher than the model's number.

## Solutions

1. `norm_cdf(0) = 0.5` exactly, because the standard normal is symmetric about zero and half its mass lies below the mean. For a large positive `x`, `erf` saturates at 1, so `N(x)` approaches 1; for a large negative `x` it approaches 0. An at-the-money option has `S = K`, so `ln(S/K) = 0`, leaving `d1 = (r - q + 0.5*sigma^2)*T / (sigma*sqrt(T))`. For short-dated options that numerator is tiny, so `d1` and `d2` sit just above zero — which is why the ATM delta comes out near (but slightly above) 0.50.

2. Compute the two discounted terms. `S*exp(-qT) = 24000*exp(-0.012*0.01918) = 24000*0.99977 = 23994.48`. `K*exp(-rT) = 24000*exp(-0.065*0.01918) = 24000*0.99875 = 23970.10`. The difference is `23994.48 - 23970.10 = 24.38`. And `C - P = 184.71 - 160.33 = 24.38`. They match. Put-call parity is a model-free identity: it must hold for any consistent pair of European call and put on the same strike and expiry, regardless of whether Black-Scholes is the "right" model. If your engine's call and put ever fail this check, one of them has a bug.

3. Structure: each position is `(greeks_dict, qty)`, where `greeks_dict` comes from `bs_greeks`. Net Greeks are just a weighted sum — Greeks are additive across a portfolio because differentiation is linear:

```python
def portfolio_greeks(positions):
    net = {"delta": 0, "gamma": 0, "vega": 0, "theta": 0}
    for greeks, qty in positions:
        for k in net:
            net[k] += greeks[k] * qty
    return net
```

A long call lot is `qty = +lot_size`; a short put lot is `qty = -lot_size`. This one function is the core of a real-time risk dashboard: it tells you the book's total delta to hedge and total theta you are collecting or paying.

4. Use the engine: `implied_vol(360, 52000, 52000, 5/365, 0.065, 0.012, "call")`. To reason about it first, compute the model price at 13% vol — an ATM 5-day Bank Nifty call at 13% is worth roughly ₹335. The market is paying ₹360, *more* than the 13% model price, so the market's implied vol must be **higher** than 13% (you need more volatility to justify the richer premium). Newton-Raphson starting at 20% converges in a few iterations to the exact figure, about 14.0%.

5. Daily decay for one lot = ₹14.08 × 25 = **₹352 per day**. Over the seven days to expiry, an unchanged Nifty would cost this buyer well over ₹2,000 per lot in pure time decay — and theta accelerates as expiry nears, so the back half of the week bleeds faster than the front. The lesson: being right on direction but early is expensive. A buyer who expects a move "sometime this week" is fighting theta every single day; the move must be large enough and soon enough to outrun the decay.

6. Two reasons. First, the **volatility smile/skew**: out-of-the-money index puts carry crash-protection demand, so the market prices them at a *higher* implied vol than the ATM 13% we might plug in — feed the engine the put's own higher IV and its model price rises toward the market. Second, **fat tails and jump risk**: real Nifty returns are not perfectly lognormal; large gap-down moves happen more often than Black-Scholes assumes, so the market charges a premium for tail risk that a constant-volatility model structurally underprices. Both are reminders that the engine is a tool for translating between price and vol, not an oracle of fair value.
