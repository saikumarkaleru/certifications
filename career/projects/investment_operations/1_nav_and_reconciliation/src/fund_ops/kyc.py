"""KYC/AML customer risk scoring and transaction monitoring.

Two independent controls that an ops/onboarding analyst runs:

1. Customer risk rating -- a weighted score across three factor groups
   (geography, product, profile) mapped to a risk tier that drives the level
   of due diligence: CDD (standard) or EDD (enhanced).

2. Transaction monitoring -- rule-based post-transaction surveillance that
   raises alerts for large value (CTR-style), structuring (splitting to dodge
   a reporting threshold), rapid movement (in/out layering) and high-risk
   counterparty geographies. Alerts feed an analyst review / potential STR.
"""

from __future__ import annotations

import pandas as pd

# --- Factor reference data -------------------------------------------------
# High-risk jurisdictions (illustrative: FATF "black/grey"-style + sanctioned).
GEO_HIGH = {"IR", "KP", "SY", "RU", "AF", "MM"}
GEO_MEDIUM = {"KY", "VN", "PA", "AE", "NG"}

PRODUCT_RISK = {
    "Savings": 20,
    "Brokerage": 40,
    "Derivatives": 70,
    "PrivateBanking": 70,
    "Crypto": 90,
    "CorrespondentBanking": 100,
}
ENTITY_BONUS = {"Individual": 0, "Company": 10, "Trust": 20}

# Factor weights (sum to 1.0).
W_GEO, W_PRODUCT, W_PROFILE = 0.35, 0.35, 0.30

# Tier thresholds on the 0-100 composite.
TIER_MEDIUM, TIER_HIGH = 35, 65

# AML rule parameters.
CTR_THRESHOLD = 10000        # large-value / currency-transaction reporting line
STRUCTURING_BAND = (8000, CTR_THRESHOLD)  # "just under" the threshold
STRUCTURING_MIN_COUNT = 3    # this many sub-threshold deposits -> structuring
RAPID_DAYS = 3               # in then out within this window -> layering
RAPID_RATIO = 0.80           # out >= 80% of in -> pass-through


def _geo_score(country: str) -> int:
    if country in GEO_HIGH:
        return 100
    if country in GEO_MEDIUM:
        return 60
    return 20


def _profile_score(row) -> int:
    score = 10
    score += 40 if row["pep_flag"] else 0
    score += 30 if row["adverse_media"] else 0
    score += ENTITY_BONUS.get(row["entity_type"], 0)
    if row["account_age_months"] < 6:
        score += 20
    elif row["account_age_months"] < 12:
        score += 10
    return min(score, 100)


def score_customers(customers: pd.DataFrame) -> pd.DataFrame:
    """Return per-customer factor scores, composite, tier and diligence level."""
    rows = []
    for _, cust in customers.iterrows():
        geo = _geo_score(cust["country"])
        product = PRODUCT_RISK.get(cust["product"], 40)
        profile = _profile_score(cust)
        composite = W_GEO * geo + W_PRODUCT * product + W_PROFILE * profile

        # Mandatory-EDD overrides: certain factors force enhanced diligence
        # regardless of the numeric score (PEP, sanctioned/high-risk geography,
        # correspondent banking).
        override = bool(
            cust["pep_flag"]
            or cust["country"] in GEO_HIGH
            or cust["product"] == "CorrespondentBanking"
        )

        if composite >= TIER_HIGH or override:
            tier, diligence = "High", "EDD"
        elif composite >= TIER_MEDIUM:
            tier, diligence = "Medium", "CDD+"
        else:
            tier, diligence = "Low", "CDD"

        rows.append(
            {
                "customer_id": cust["customer_id"],
                "name": cust["name"],
                "country": cust["country"],
                "product": cust["product"],
                "geo_score": geo,
                "product_score": product,
                "profile_score": profile,
                "composite_score": round(composite, 1),
                "risk_tier": tier,
                "diligence": diligence,
                "edd_override": override,
            }
        )
    return pd.DataFrame(rows)


def monitor_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    """Apply AML monitoring rules and return one row per alert."""
    txns = transactions.sort_values(["customer_id", "date"])
    alerts = []

    # Rule 1: large single value (CTR-style).
    for _, t in txns.iterrows():
        if t["amount"] >= CTR_THRESHOLD:
            alerts.append(_alert(t["customer_id"], "LARGE_VALUE", "High",
                                 f"{t['txn_id']} amount {t['amount']:,.0f} >= {CTR_THRESHOLD:,}"))
        # Rule 4: high-risk counterparty geography.
        if t["counterparty_country"] in GEO_HIGH:
            alerts.append(_alert(t["customer_id"], "HIGH_RISK_COUNTERPARTY", "Medium",
                                 f"{t['txn_id']} counterparty {t['counterparty_country']}"))

    # Rule 2: structuring -- several deposits just under the threshold.
    lo, hi = STRUCTURING_BAND
    for cid, grp in txns.groupby("customer_id"):
        band = grp[(grp["amount"] >= lo) & (grp["amount"] < hi) & (grp["direction"] == "IN")]
        if len(band) >= STRUCTURING_MIN_COUNT:
            total = band["amount"].sum()
            alerts.append(_alert(cid, "STRUCTURING", "High",
                                 f"{len(band)} deposits in {lo:,}-{hi:,} band totalling {total:,.0f}"))

    # Rule 3: rapid movement -- inflow then a near-equal outflow within a window.
    for cid, grp in txns.groupby("customer_id"):
        ins = grp[grp["direction"] == "IN"]
        outs = grp[grp["direction"] == "OUT"]
        for _, i in ins.iterrows():
            for _, o in outs.iterrows():
                gap = (o["date"] - i["date"]).days
                if 0 <= gap <= RAPID_DAYS and o["amount"] >= RAPID_RATIO * i["amount"]:
                    alerts.append(_alert(cid, "RAPID_MOVEMENT", "High",
                                         f"in {i['amount']:,.0f} then out {o['amount']:,.0f} "
                                         f"in {gap}d"))
                    break

    out = pd.DataFrame(alerts)
    if not out.empty:
        sev_order = {"High": 0, "Medium": 1, "Low": 2}
        out["_s"] = out["severity"].map(sev_order)
        out = out.sort_values(["_s", "customer_id"]).drop(columns="_s").reset_index(drop=True)
    return out


def _alert(customer_id, rule, severity, detail):
    return {"customer_id": customer_id, "rule": rule, "severity": severity, "detail": detail}


def tier_distribution(scored: pd.DataFrame) -> pd.DataFrame:
    order = ["Low", "Medium", "High"]
    counts = scored["risk_tier"].value_counts().to_dict()
    return pd.DataFrame({"risk_tier": order, "count": [counts.get(t, 0) for t in order]})
