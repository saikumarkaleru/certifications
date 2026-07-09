"""
binomial.py  --  Cox-Ross-Rubinstein (CRR) binomial tree
=========================================================

WHY A TREE WHEN WE ALREADY HAVE A FORMULA?
  Black-Scholes only prices EUROPEAN options (exercise at expiry only). Many real
  contracts are AMERICAN (exercise any time). The binomial tree handles both, and
  it is the cleanest way to SHOW that discrete option pricing converges to the
  continuous Black-Scholes value as the number of steps N -> infinity.

CRR PARAMETERS (the classic choice that matches the lognormal variance):
  dt = T / N
  u  = e^(sigma*sqrt(dt))     up-move factor
  d  = 1/u                    down-move factor (recombining tree)
  p  = (e^((r-q)*dt) - d) / (u - d)     risk-neutral up-probability

METHOD:
  1. Build the vector of terminal payoffs at expiry (N+1 nodes).
  2. Roll BACKWARD: each node = discounted risk-neutral average of its children.
  3. AMERICAN: at every node compare that 'continuation value' to the payoff of
     exercising RIGHT NOW and keep the larger -- that's the early-exercise test.
"""

import math


def crr_price(S, K, T, r, sigma, option="call", q=0.0, N=500, american=False):
    """Price a European or American option with an N-step CRR binomial tree.

    Returns the option price as a float.
    """
    option = option.lower()
    dt = T / N                                  # length of one time step (years)
    u = math.exp(sigma * math.sqrt(dt))         # up factor
    d = 1.0 / u                                 # down factor (recombining)
    disc = math.exp(-r * dt)                    # one-step discount factor
    p = (math.exp((r - q) * dt) - d) / (u - d)  # risk-neutral up-probability

    # Guard: with too few steps or extreme inputs p can leave [0,1]; that would
    # mean the tree is mis-specified rather than a valid probability.
    if not (0.0 <= p <= 1.0):
        raise ValueError(f"Risk-neutral probability p={p:.4f} outside [0,1]; "
                         f"increase N or check inputs.")

    # --- Step 1: terminal asset prices and payoffs at maturity ---
    # Node j (0..N) has had j up-moves and (N-j) down-moves.
    values = []
    for j in range(N + 1):
        ST = S * (u ** j) * (d ** (N - j))
        if option == "call":
            values.append(max(ST - K, 0.0))
        else:
            values.append(max(K - ST, 0.0))

    # --- Step 2/3: backward induction, with optional early-exercise test ---
    for i in range(N - 1, -1, -1):              # walk time layers back to today
        for j in range(i + 1):
            # Continuation value = discounted expected value of the two children.
            cont = disc * (p * values[j + 1] + (1.0 - p) * values[j])
            if american:
                # Spot at this node, then the payoff if we exercise immediately.
                ST = S * (u ** j) * (d ** (i - j))
                exercise = (ST - K) if option == "call" else (K - ST)
                values[j] = max(cont, exercise)  # take the better of the two
            else:
                values[j] = cont
    return values[0]
