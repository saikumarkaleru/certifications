"""
actuals.py - simulate the ACTUAL results and cache them to CSV.

The budget is "the plan"; actuals are "what really happened". Real life never
lands exactly on plan, so we apply realistic DRIFT to each driver:

  * volume drift  - some product lines beat plan, some fall short
  * price drift   - realised prices differ from the list price (discounts,
                    mix of deals, or premium pricing)
  * unit-cost drift - input costs creep up or savings come through
  * opex drift    - cost centres over- or under-spend their budgets

Each driver gets a SYSTEMATIC bias (a deliberate story - e.g. "Beta had a
volume shortfall but held price") plus small month-to-month random NOISE. All
randomness comes from a single seeded generator, so the simulation is
DETERMINISTIC: the same seed always produces the exact same actuals. That is
the project's "always-runs, no-network" guarantee.

We also CACHE the generated data to input/*.csv. On the next run we simply
reload the CSVs, so the numbers are reproducible even if the generation logic
were ever changed.
"""

import os
import numpy as np
import pandas as pd

from . import budget as budget_mod

# Default seed. A fixed seed => deterministic output => the model always runs
# to the identical result. Print this so a reviewer knows the "data source".
DEFAULT_SEED = 42

# ---------------------------------------------------------------------------
# SYSTEMATIC BIAS per product (the deliberate business story).
#   volume : Alpha & Gamma beat plan; Beta & Delta fall short.
#   price  : Beta holds a premium (+5%); Gamma discounts (-2%).
#   cost   : Gamma's unit cost creeps +5% (a margin problem to flag later).
# These are annual average biases; monthly noise wobbles around them.
# ---------------------------------------------------------------------------
VOLUME_BIAS = {"Alpha Sensor": +0.04, "Beta Controller": -0.08,
               "Gamma Module": +0.06, "Delta Analyzer": -0.03}
PRICE_BIAS  = {"Alpha Sensor": +0.00, "Beta Controller": +0.05,
               "Gamma Module": -0.02, "Delta Analyzer": +0.02}
COST_BIAS   = {"Alpha Sensor": +0.02, "Beta Controller": +0.01,
               "Gamma Module": +0.05, "Delta Analyzer": +0.00}

# Cost-centre spending bias: S&M overspends, G&A saves, others near plan.
OPEX_BIAS = {"Manufacturing": +0.03, "Sales & Marketing": +0.06,
             "G&A": -0.02, "R&D": +0.01}

# Size of the random monthly noise (standard deviation, as a fraction).
VOL_SIGMA, PRICE_SIGMA, COST_SIGMA, OPEX_SIGMA = 0.05, 0.02, 0.02, 0.03


def simulate_actuals(budget, seed=DEFAULT_SEED):
    """Simulate actual results from a budget, using a seeded RNG.

    Returns a dict with the same shape as build_budget():
      'products' : product x month actual volume/price/unit_cost/revenue/cogs
      'opex'     : cost-centre x month actual opex
    """
    rng = np.random.default_rng(seed)          # the single source of randomness

    # ----- Product actuals -------------------------------------------------
    bp = budget["products"].copy()
    n = len(bp)

    # Draw one noise value per row for each driver. rng.normal(mean, sd, size).
    vol_noise   = rng.normal(0.0, VOL_SIGMA,   n)
    price_noise = rng.normal(0.0, PRICE_SIGMA, n)
    cost_noise  = rng.normal(0.0, COST_SIGMA,  n)

    # Map each row's product to its systematic bias.
    vol_bias   = bp["product"].map(VOLUME_BIAS).to_numpy()
    price_bias = bp["product"].map(PRICE_BIAS).to_numpy()
    cost_bias  = bp["product"].map(COST_BIAS).to_numpy()

    # Actual driver = budget driver x (1 + bias) x (1 + noise).
    act_volume = np.round(bp["volume"].to_numpy() * (1 + vol_bias) * (1 + vol_noise)).astype(int)
    act_price  = np.round(bp["price"].to_numpy()  * (1 + price_bias) * (1 + price_noise), 2)
    act_cost   = np.round(bp["unit_cost"].to_numpy() * (1 + cost_bias) * (1 + cost_noise), 2)

    products = pd.DataFrame({
        "product":   bp["product"],
        "month":     bp["month"],
        "month_num": bp["month_num"],
        "volume":    act_volume,
        "price":     act_price,
        "unit_cost": act_cost,
        "revenue":   np.round(act_price * act_volume, 2),   # derived
        "cogs":      np.round(act_cost  * act_volume, 2),   # derived
    })

    # ----- Opex actuals ----------------------------------------------------
    bo = budget["opex"].copy()
    opex_noise = rng.normal(0.0, OPEX_SIGMA, len(bo))
    opex_bias  = bo["cost_centre"].map(OPEX_BIAS).to_numpy()
    opex = pd.DataFrame({
        "cost_centre": bo["cost_centre"],
        "month":       bo["month"],
        "month_num":   bo["month_num"],
        "opex":        np.round(bo["opex"].to_numpy() * (1 + opex_bias) * (1 + opex_noise), 2),
    })

    return {"products": products, "opex": opex}


# ---------------------------------------------------------------------------
# CACHING - write/read the generated datasets to input/*.csv so runs are
# reproducible and offline. get_datasets() is the single entry point main.py
# uses: it loads the cache if present, otherwise builds+simulates and saves.
# ---------------------------------------------------------------------------
_FILES = {
    "budget_products": "budget_products.csv",
    "budget_opex":     "budget_opex.csv",
    "actual_products": "actual_products.csv",
    "actual_opex":     "actual_opex.csv",
}


def _paths(input_dir):
    return {k: os.path.join(input_dir, v) for k, v in _FILES.items()}


def _cache_exists(input_dir):
    return all(os.path.exists(p) for p in _paths(input_dir).values())


def save_datasets(budget, actuals, input_dir):
    """Write budget and actual datasets to input/ as CSV."""
    os.makedirs(input_dir, exist_ok=True)
    p = _paths(input_dir)
    budget["products"].to_csv(p["budget_products"], index=False)
    budget["opex"].to_csv(p["budget_opex"], index=False)
    actuals["products"].to_csv(p["actual_products"], index=False)
    actuals["opex"].to_csv(p["actual_opex"], index=False)


def load_datasets(input_dir):
    """Read budget and actual datasets back from input/ CSVs."""
    p = _paths(input_dir)
    budget = {"products": pd.read_csv(p["budget_products"]),
              "opex":     pd.read_csv(p["budget_opex"])}
    actuals = {"products": pd.read_csv(p["actual_products"]),
               "opex":     pd.read_csv(p["actual_opex"])}
    return budget, actuals


def get_datasets(input_dir, seed=DEFAULT_SEED, use_cache=True):
    """Return (budget, actuals, source_str).

    If the CSV cache exists we reload it (fast, reproducible). Otherwise we
    build the budget, simulate actuals with the seed, save the cache, and
    return that. `source_str` documents where the numbers came from.
    """
    if use_cache and _cache_exists(input_dir):
        budget, actuals = load_datasets(input_dir)
        return budget, actuals, f"cached CSVs in input/ (originally seed={seed})"

    budget = budget_mod.build_budget()
    actuals = simulate_actuals(budget, seed=seed)
    save_datasets(budget, actuals, input_dir)
    return budget, actuals, f"generated fresh (numpy seed={seed}), cached to input/"
