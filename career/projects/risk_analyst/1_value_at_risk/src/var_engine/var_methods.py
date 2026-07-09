"""VaR methods: historical, parametric (variance-covariance), Monte Carlo,
Expected Shortfall, and component/marginal VaR.

All VaR/ES numbers are reported as POSITIVE losses expressed as a fraction of
portfolio value (e.g. 0.021 = a 2.1% loss). Convert to dollars by multiplying
by the portfolio notional.

No scipy: the normal PDF, CDF and inverse-CDF are implemented by hand.
"""

from __future__ import annotations

import math

import numpy as np
import pandas as pd

# --- Normal distribution helpers (scipy-free) -----------------------------


def norm_pdf(x: float) -> float:
    """Standard normal probability density."""
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def norm_cdf(x: float) -> float:
    """Standard normal CDF via the error function."""
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def norm_ppf(p: float) -> float:
    """Inverse standard normal CDF (quantile function).

    Beasley-Springer / Moro rational approximation. Accurate to ~1e-9 over the
    usable range, which is far tighter than any VaR application needs.
    """
    if not 0.0 < p < 1.0:
        raise ValueError("p must be in (0, 1)")

    a = [-3.969683028665376e+01, 2.209460984245205e+02, -2.759285104469687e+02,
         1.383577518672690e+02, -3.066479806614716e+01, 2.506628277459239e+00]
    b = [-5.447609879822406e+01, 1.615858368580409e+02, -1.556989798598866e+02,
         6.680131188771972e+01, -1.328068155288572e+01]
    c = [-7.784894002430293e-03, -3.223964580411365e-01, -2.400758277161838e+00,
         -2.549732539343734e+00, 4.374664141464968e+00, 2.938163982698783e+00]
    d = [7.784695709041462e-03, 3.224671290700398e-01, 2.445134137142996e+00,
         3.754408661907416e+00]

    plow, phigh = 0.02425, 1.0 - 0.02425
    if p < plow:
        q = math.sqrt(-2.0 * math.log(p))
        return (((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5]) / \
               ((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1.0)
    if p > phigh:
        q = math.sqrt(-2.0 * math.log(1.0 - p))
        return -(((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5]) / \
                ((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1.0)
    q = p - 0.5
    r = q * q
    return (((((a[0]*r+a[1])*r+a[2])*r+a[3])*r+a[4])*r+a[5]) * q / \
           (((((b[0]*r+b[1])*r+b[2])*r+b[3])*r+b[4])*r+1.0)


# --- VaR methods ----------------------------------------------------------


def historical_var(port_returns, conf: float) -> float:
    """Historical VaR: the negative of the (1-conf) empirical quantile.

    Example: at 95% we take the 5th percentile of returns; a loss, so we flip
    the sign to report a positive number.
    """
    alpha = 1.0 - conf
    q = np.percentile(np.asarray(port_returns), 100.0 * alpha)
    return -q


def parametric_var(mu_p: float, sigma_p: float, conf: float) -> float:
    """Variance-covariance (delta-normal) VaR.

    z is the lower-tail quantile (negative), so VaR = -(mu + z*sigma) is a
    positive loss. At 95% z ~= -1.645, giving the familiar -(mu - 1.645*sigma).
    """
    z = norm_ppf(1.0 - conf)
    return -(mu_p + z * sigma_p)


def portfolio_moments(returns: pd.DataFrame, weights: np.ndarray):
    """Return (mu_p, sigma_p, mean_vec, cov) for the parametric method."""
    mean_vec = returns.mean().to_numpy()
    cov = returns.cov().to_numpy()
    mu_p = float(weights @ mean_vec)
    sigma_p = float(np.sqrt(weights @ cov @ weights))
    return mu_p, sigma_p, mean_vec, cov


def monte_carlo_var(mean_vec, cov, weights, conf, n_sims=50_000, seed=42):
    """Monte Carlo VaR under a multivariate-normal assumption.

    Draw correlated asset returns via the Cholesky factor of the covariance
    matrix (sim = mu + L @ z), aggregate to the portfolio, and read off the
    empirical quantile. Returns (var, simulated_portfolio_returns).
    """
    rng = np.random.default_rng(seed)
    n = len(weights)
    chol = np.linalg.cholesky(cov)
    z = rng.standard_normal((n_sims, n))
    sims = mean_vec + z @ chol.T          # (n_sims, n) correlated asset returns
    port_sims = sims @ weights            # (n_sims,) portfolio returns
    var = -np.percentile(port_sims, 100.0 * (1.0 - conf))
    return float(var), port_sims


# --- Expected shortfall ---------------------------------------------------


def historical_es(port_returns, conf: float) -> float:
    """Historical Expected Shortfall: mean loss in the tail beyond VaR."""
    var = historical_var(port_returns, conf)
    arr = np.asarray(port_returns)
    tail = arr[arr <= -var]
    if tail.size == 0:
        return var
    return -tail.mean()


def parametric_es(mu_p: float, sigma_p: float, conf: float) -> float:
    """Closed-form normal ES: ES = -mu + sigma * pdf(z_alpha)/alpha."""
    alpha = 1.0 - conf
    z_alpha = norm_ppf(alpha)
    return -mu_p + sigma_p * norm_pdf(z_alpha) / alpha


# --- Component / marginal VaR --------------------------------------------


def component_var(returns, weights, conf, tickers):
    """Marginal and component VaR under the parametric model.

    Marginal VaR_i = z * (Sigma w)_i / sigma_p     (sensitivity to weight_i)
    Component VaR_i = w_i * Marginal VaR_i          (additive decomposition)
    With zero mean, sum of component VaR == total parametric VaR (Euler's
    theorem for the homogeneous-degree-1 risk measure).
    """
    mu_p, sigma_p, mean_vec, cov = portfolio_moments(returns, weights)
    z = norm_ppf(conf)  # positive quantile; component VaR reported as positive loss
    sigma_w = cov @ weights
    marginal = z * sigma_w / sigma_p
    component = weights * marginal
    total = component.sum()
    pct = component / total if total != 0 else component * 0.0
    return pd.DataFrame({
        "ticker": tickers,
        "weight": weights,
        "marginal_var": marginal,
        "component_var": component,
        "pct_contribution": pct,
    })


# --- Rolling VaR ----------------------------------------------------------


def rolling_historical_var(port_returns: pd.Series, window=250, conf=0.95) -> pd.Series:
    """Rolling-window historical VaR time series (positive losses)."""
    alpha = 1.0 - conf
    roll = port_returns.rolling(window).quantile(alpha)
    return (-roll).dropna().rename(f"rolling_var_{int(conf*100)}")
