# Study Guide - Black-Scholes Options Toolkit

Your cheat-sheet to defend this project in an interview. You already know options
from the F&O desk; this connects that intuition to the code you wrote.

## 30-second pitch

"I built a self-contained options-analytics library in Python. It prices European
options with the closed-form Black-Scholes-Merton model including a dividend yield,
computes first- and second-order Greeks, and cross-checks every price three
independent ways - closed form, a Cox-Ross-Rubinstein binomial tree, and
Monte-Carlo. It solves implied volatility from live market quotes with
Newton-Raphson (falling back to bisection), builds the volatility smile from a real
option chain, and validates the analytic Greeks against finite differences. No
scipy - the normal CDF is built from `math.erf` - and it runs fully offline via a
cached-chain fallback."

## What it is

A `pricer` package plus an orchestrator (`main.py`) that runs eight demo steps and
writes an Excel workbook and four charts. Six modules: `black_scholes`,
`implied_vol`, `binomial`, `monte_carlo`, `market_data`, `validation`. Six unit
tests, all passing.

## The single key interview answer

If they ask one thing, it is *"why should I trust your prices?"* Answer:

> "Because three independent methods agree. The closed-form BSM, a binomial tree,
> and Monte-Carlo all land on the same number within tolerance - the tree to ~1e-3,
> Monte-Carlo inside its own standard-error band. And I don't just trust my Greek
> calculus: I bump each input, re-price, and confirm the analytic Greeks match the
> finite-difference slopes to ~1e-8. That's exactly how a desk signs off a pricer
> before it carries real risk."

## Module / flow walkthrough

- **black_scholes.py** - `norm_cdf`/`norm_pdf` (from `math.erf`), `d1_d2`, prices,
  and Greeks. First order: delta, gamma, vega, theta, rho. Second order: vanna,
  volga, charm. Every scaling (per 1% vol, per day) is documented in the docstring.
- **implied_vol.py** - inverts the price for sigma. Newton-Raphson using raw vega,
  with a bisection fallback on `[1e-4, 5.0]` when Newton diverges or vega is flat.
  Checks no-arbitrage bounds first (below intrinsic there is no valid IV).
- **binomial.py** - CRR tree. Builds terminal payoffs, rolls back with the
  risk-neutral probability, and for American options compares continuation value to
  immediate exercise at every node.
- **monte_carlo.py** - simulates terminal GBM prices, averages discounted payoffs,
  uses antithetic variates (Z and -Z) for variance reduction, and reports a
  standard error.
- **market_data.py** - live yfinance chain -> cache to `input/` -> synthetic
  fallback. Guarantees `main.py` always runs.
- **validation.py** - central finite differences vs the analytic Greeks.
- **main.py** - orchestrates all of the above and produces the outputs.

## Interview Q&A

**1. What is put-call parity and why does it matter?**
`C - P = S*e^(-qT) - K*e^(-rT)`. It's model-free - it comes from a no-arbitrage
argument (a call minus a put replicates a forward), so it must hold for *any*
volatility. I use it as a free sanity check: if my call and put prices don't
satisfy parity, one of them is wrong. On a desk it's also how you spot mispriced
pairs and how you convert between call and put risk.

**2. Why do Black-Scholes, the tree, and Monte-Carlo all give the same price?**
They're three ways to compute the same thing: the discounted risk-neutral expected
payoff. BSM does the expectation analytically (the lognormal integral has a closed
form). The binomial tree discretizes the price process and, as steps -> infinity,
its lognormal limit converges to BSM. Monte-Carlo estimates the same expectation by
simulation, converging by the Law of Large Numbers. Same expectation, three
numerical routes.

**3. What does implied volatility actually mean?**
Every BSM input except vol is observable. Implied vol is the single sigma that makes
the model reproduce the *market* price - it's the market's forward-looking estimate
of how much the underlying will move, quoted in vol terms. Plotting it against
strike gives the smile/skew; a flat line would mean the market believed BSM's
constant-vol assumption, and it never does.

**4. Newton-Raphson vs bisection for the IV solve - why both?**
Newton is fast (quadratic convergence) because I have the exact derivative, vega,
so each step is `sigma -= (price-target)/vega`. But Newton can overshoot when vega
is tiny (deep ITM/OTM) or diverge from a bad start. Bisection can't diverge once
the root is bracketed - it just halves the interval - but it's slow. So I try Newton
first and fall back to bisection on `[1e-4, 5.0]` for robustness. Best of both.

**5. What are vanna, volga and charm, and why does a desk care?**
They're second-order Greeks - how your first-order Greeks themselves drift.
*Vanna* = dDelta/dsigma (= dVega/dSpot): your delta hedge moves when vol moves, so a
delta-neutral book still bleeds in a vol spike. *Volga* (vomma) = dVega/dsigma: the
convexity of vega, which is what makes long-vol positions and vol smiles behave
non-linearly. *Charm* = dDelta/dtime: your hedge drifts purely from time passing -
critical into expiry and over weekends when you can't continuously re-hedge. A desk
watches these to know how often and in which direction it must re-hedge.

**6. Why validate Greeks with finite differences?**
The Greeks are hand-derived calculus, and a sign error or a missing `e^(-qT)` is
invisible in the price but poisons a hedge. Finite differences give a completely
independent numeric estimate: bump an input by a tiny `h`, re-price, measure the
slope. If analytic and numeric agree to ~1e-8, the calculus is right. It's cheap
insurance and standard desk practice.

## Vocabulary

- **BSM / Black-Scholes-Merton** - closed-form European option pricing model.
- **Risk-neutral measure** - the pricing world where all assets drift at the
  risk-free rate; prices are discounted expected payoffs under it.
- **Greeks** - sensitivities of price to inputs (delta, gamma, vega, theta, rho).
- **Second-order Greeks** - vanna, volga, charm; sensitivities of the Greeks.
- **Implied volatility** - the sigma that reproduces the market price.
- **Volatility smile/skew** - implied vol plotted against strike.
- **CRR / binomial tree** - discrete up/down lattice for the underlying.
- **American vs European** - exercise any time vs only at expiry.
- **Early-exercise premium** - extra value of an American option over its European
  twin.
- **Antithetic variates** - variance-reduction trick pairing Z with -Z.
- **Standard error** - `sample_std / sqrt(n)`; the tightness of an MC estimate.
- **Put-call parity** - `C - P = S*e^(-qT) - K*e^(-rT)`, a no-arbitrage identity.
- **Finite differences** - numeric derivative by bump-and-reprice.
- **Dividend yield q** - continuous payout; shifts the drift to `r - q`.
