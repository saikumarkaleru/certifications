"""Portfolio view: combine the two models, rank issuers, expected loss.

Two things happen here:

1. A COMBINED table lines the accounting view (Altman Z, zone) up against the
   structural view (Merton PD, DD) so we can see where they agree and disagree.

2. PORTFOLIO EXPECTED LOSS. The industry identity for a loan/bond book is

       EL_i = PD_i * LGD * EAD_i

   PD  = probability of default (from Merton),
   LGD = loss given default (fraction NOT recovered; 0.45 for senior unsecured),
   EAD = exposure at default (dollars lent). We use an equal $10M line to each
   issuer, sum the pieces, and express the total as a % of exposure.
"""

from __future__ import annotations

import pandas as pd

LGD = 0.45                 # senior unsecured recovery ~55% -> 45% loss
EAD_PER_ISSUER = 10_000_000.0   # equal $10M exposure to each name


def combine(altman: pd.DataFrame, merton: pd.DataFrame) -> pd.DataFrame:
    """Merge Altman and Merton outputs and add both risk rankings.

    rank_altman : 1 = riskiest by Z (lowest Z first).
    rank_merton : 1 = riskiest by PD (highest PD first).
    agree       : True when both models put the name on the same side of
                  "investment grade-ish" (Safe zone vs low PD).
    """
    combined = pd.DataFrame({
        "Z": altman["Z"],
        "Zone": altman["Zone"],
        "DD": merton["DD"],
        "PD": merton["PD"],
        "converged": merton["converged"],
    })

    # Ranks are nullable ints: a firm with no Altman ratios (e.g. a bank whose
    # working-capital concept is not comparable) legitimately has no Z-rank.
    combined["rank_altman"] = combined["Z"].rank(method="min").astype("Int64")
    combined["rank_merton"] = (
        combined["PD"].rank(method="min", ascending=False).astype("Int64"))

    # Simple agreement flag: does Merton's "risky" (PD above median) line up
    # with Altman's non-Safe zone?
    pd_median = combined["PD"].median()
    merton_risky = combined["PD"] > pd_median
    altman_risky = combined["Zone"] != "Safe"
    combined["agree"] = merton_risky == altman_risky

    return combined.sort_values("PD", ascending=False)


def expected_loss(merton: pd.DataFrame, lgd: float = LGD,
                  ead: float = EAD_PER_ISSUER) -> pd.DataFrame:
    """Per-issuer and portfolio expected loss table.

    Returns a DataFrame with EAD, LGD, PD and EL per issuer. The portfolio
    totals are available via :func:`portfolio_summary`.
    """
    table = pd.DataFrame({
        "PD": merton["PD"],
        "LGD": lgd,
        "EAD": ead,
    })
    table["EL"] = table["PD"] * table["LGD"] * table["EAD"]
    return table.sort_values("EL", ascending=False)


def portfolio_summary(el_table: pd.DataFrame) -> dict:
    """Aggregate the per-issuer EL table into portfolio totals."""
    total_ead = el_table["EAD"].sum()
    total_el = el_table["EL"].sum()
    return {
        "total_ead": total_ead,
        "total_el": total_el,
        "el_pct": (total_el / total_ead) if total_ead else float("nan"),
    }
