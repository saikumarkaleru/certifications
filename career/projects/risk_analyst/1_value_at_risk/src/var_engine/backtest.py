"""Backtesting VaR: exception counting plus the Kupiec POF and Christoffersen
independence / conditional-coverage likelihood-ratio tests.

An "exception" (or breach) is a day where the actual portfolio loss exceeds the
VaR forecast, i.e. return < -VaR. A good 95% model should breach ~5% of days,
and breaches should be independent (not clustered). We test both.

No scipy: the chi-square p-value uses a hand-written regularised incomplete
gamma function.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
import pandas as pd

from .var_methods import historical_var


# --- Chi-square p-value (scipy-free) --------------------------------------


def _gammainc_lower(s: float, x: float) -> float:
    """Regularised lower incomplete gamma P(s, x) via series / continued frac."""
    if x <= 0.0:
        return 0.0
    if x < s + 1.0:
        # Series expansion.
        term = 1.0 / s
        total = term
        n = s
        for _ in range(200):
            n += 1.0
            term *= x / n
            total += term
            if abs(term) < abs(total) * 1e-15:
                break
        return total * math.exp(-x + s * math.log(x) - math.lgamma(s))
    # Continued fraction (Lentz) for the upper incomplete gamma, then complement.
    tiny = 1e-300
    b = x + 1.0 - s
    c = 1.0 / tiny
    d = 1.0 / b
    h = d
    for i in range(1, 200):
        an = -i * (i - s)
        b += 2.0
        d = an * d + b
        if abs(d) < tiny:
            d = tiny
        c = b + an / c
        if abs(c) < tiny:
            c = tiny
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < 1e-15:
            break
    upper = math.exp(-x + s * math.log(x) - math.lgamma(s)) * h
    return 1.0 - upper


def chi2_sf(x: float, df: int) -> float:
    """Chi-square survival function (p-value) = 1 - CDF."""
    if x <= 0.0:
        return 1.0
    return 1.0 - _gammainc_lower(df / 2.0, x / 2.0)


# --- Result container -----------------------------------------------------


@dataclass
class BacktestResult:
    n_obs: int
    n_exceptions: int
    expected: float
    conf: float
    lr_uc: float
    p_uc: float
    lr_ind: float
    p_ind: float
    lr_cc: float
    p_cc: float

    def verdict(self, level: float = 0.05) -> str:
        """PASS if we cannot reject correct conditional coverage at `level`."""
        return "PASS" if self.p_cc > level else "FAIL"


# --- Rolling out-of-sample VaR and exceptions -----------------------------


def rolling_var_exceptions(port_returns: pd.Series, window=250, conf=0.95):
    """Walk-forward: estimate VaR on the trailing window, test the next day.

    Returns (exceptions_bool_series, var_series) aligned on the test dates.
    """
    r = port_returns.reset_index(drop=True)
    var_vals, exc, idx = [], [], []
    for t in range(window, len(r)):
        v = historical_var(r.iloc[t - window:t], conf)
        var_vals.append(v)
        exc.append(bool(r.iloc[t] < -v))
        idx.append(port_returns.index[t])
    return pd.Series(exc, index=idx, name="exception"), pd.Series(var_vals, index=idx, name="var")


# --- Kupiec and Christoffersen tests --------------------------------------


def kupiec_pof(n_obs: int, n_exc: int, conf: float):
    """Kupiec proportion-of-failures unconditional coverage test (1 df)."""
    p = 1.0 - conf                       # expected exception rate
    if n_exc == 0:
        lr = -2.0 * n_obs * math.log(1.0 - p)
    elif n_exc == n_obs:
        lr = -2.0 * n_obs * math.log(p)
    else:
        pi = n_exc / n_obs
        log_null = (n_obs - n_exc) * math.log(1.0 - p) + n_exc * math.log(p)
        log_alt = (n_obs - n_exc) * math.log(1.0 - pi) + n_exc * math.log(pi)
        lr = -2.0 * (log_null - log_alt)
    return lr, chi2_sf(lr, 1)


def christoffersen_independence(exceptions: pd.Series):
    """Christoffersen independence test from the 2x2 transition matrix (1 df)."""
    e = exceptions.astype(int).to_numpy()
    n00 = n01 = n10 = n11 = 0
    for prev, cur in zip(e[:-1], e[1:]):
        if prev == 0 and cur == 0:
            n00 += 1
        elif prev == 0 and cur == 1:
            n01 += 1
        elif prev == 1 and cur == 0:
            n10 += 1
        else:
            n11 += 1

    pi01 = n01 / (n00 + n01) if (n00 + n01) else 0.0
    pi11 = n11 / (n10 + n11) if (n10 + n11) else 0.0
    pi = (n01 + n11) / (n00 + n01 + n10 + n11) if e.size > 1 else 0.0

    def _safe_log(x):
        return math.log(x) if x > 0 else 0.0

    log_alt = (n00 * _safe_log(1 - pi01) + n01 * _safe_log(pi01)
               + n10 * _safe_log(1 - pi11) + n11 * _safe_log(pi11))
    log_null = ((n00 + n10) * _safe_log(1 - pi) + (n01 + n11) * _safe_log(pi))
    lr = -2.0 * (log_null - log_alt)
    lr = max(lr, 0.0)
    return lr, chi2_sf(lr, 1)


def run_backtest(port_returns: pd.Series, window=250, conf=0.95) -> BacktestResult:
    """Full backtest: rolling exceptions -> Kupiec + Christoffersen -> combined."""
    exc, _ = rolling_var_exceptions(port_returns, window=window, conf=conf)
    n_obs = len(exc)
    n_exc = int(exc.sum())
    expected = n_obs * (1.0 - conf)

    lr_uc, p_uc = kupiec_pof(n_obs, n_exc, conf)
    lr_ind, p_ind = christoffersen_independence(exc)
    lr_cc = lr_uc + lr_ind                       # conditional coverage (2 df)
    p_cc = chi2_sf(lr_cc, 2)

    return BacktestResult(
        n_obs=n_obs, n_exceptions=n_exc, expected=expected, conf=conf,
        lr_uc=lr_uc, p_uc=p_uc, lr_ind=lr_ind, p_ind=p_ind,
        lr_cc=lr_cc, p_cc=p_cc,
    )
