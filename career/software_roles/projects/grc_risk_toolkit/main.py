"""
GRC Control & Risk-Register Toolkit
==================================================================
A small, honest Governance-Risk-Compliance workflow in one file — the kind of
thing a Risk/GRC analyst actually maintains:

  1. RISK REGISTER  — score each risk by Likelihood x Impact, rate it, track the
     owner, treatment and remediation status.
  2. ISO 27001 CONTROL MAPPING — map each risk to the relevant ISO 27001:2022
     Annex A control domain and flag whether a control is in place.
  3. VENDOR / THIRD-PARTY QUESTIONNAIRE — score a vendor's security answers into
     a risk tier (a lightweight third-party due-diligence review).

Output: an Excel workbook (Risk_Register / Control_Mapping / Vendor_Assessment)
plus a 5x5 risk heat-map. Read top to bottom — every number is a simple,
defensible calculation.
"""

from __future__ import annotations

import os
import pandas as pd

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    HAVE_PLT = True
except Exception:
    HAVE_PLT = False

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
os.makedirs(OUT, exist_ok=True)


# ---------------------------------------------------------------------------
# 1) RISK REGISTER  (Likelihood x Impact, 1-5 each)
# ---------------------------------------------------------------------------
RISKS = [
    # id, description, category, likelihood, impact, owner, treatment, status, iso_control
    ("R-01", "Phishing leads to credential compromise", "Access", 4, 5, "Security", "Mitigate", "In Progress", "A.5.17 Authentication / A.6.3 Awareness"),
    ("R-02", "Unpatched server exploited", "Vuln Mgmt", 3, 5, "IT Ops", "Mitigate", "Open", "A.8.8 Technical vulnerabilities"),
    ("R-03", "Excessive user access / no least privilege", "Access", 3, 4, "IAM", "Mitigate", "In Progress", "A.5.15 Access control"),
    ("R-04", "Critical vendor suffers a data breach", "Third Party", 3, 5, "Vendor Risk", "Transfer", "Open", "A.5.19 Supplier relationships"),
    ("R-05", "Cloud storage misconfigured (public)", "Cloud", 3, 4, "Cloud", "Mitigate", "Open", "A.8.9 Configuration management"),
    ("R-06", "No tested backups / ransomware recovery", "Resilience", 2, 5, "IT Ops", "Mitigate", "In Progress", "A.8.13 Information backup"),
    ("R-07", "Missing security awareness training", "People", 4, 3, "HR/Security", "Mitigate", "Open", "A.6.3 Awareness & training"),
    ("R-08", "Fraudulent payment / weak segregation of duties", "Fraud", 2, 5, "Finance", "Mitigate", "Open", "A.5.3 Segregation of duties"),
    ("R-09", "Incident with no response plan", "Incident", 2, 4, "Security", "Mitigate", "In Progress", "A.5.24 Incident mgmt planning"),
    ("R-10", "Logging/monitoring gaps hide intrusions", "Monitoring", 3, 4, "SecOps", "Mitigate", "Open", "A.8.15 Logging / A.8.16 Monitoring"),
]

RATINGS = [(20, "Critical"), (12, "High"), (6, "Medium"), (0, "Low")]


def rate(score: int) -> str:
    for threshold, label in RATINGS:
        if score >= threshold:
            return label
    return "Low"


def risk_register() -> pd.DataFrame:
    rows = []
    for rid, desc, cat, L, I, owner, treat, status, iso in RISKS:
        score = L * I
        rows.append({"ID": rid, "Risk": desc, "Category": cat,
                     "Likelihood": L, "Impact": I, "Score": score,
                     "Rating": rate(score), "Owner": owner,
                     "Treatment": treat, "Status": status, "ISO 27001": iso})
    df = pd.DataFrame(rows).sort_values("Score", ascending=False).reset_index(drop=True)
    return df


# ---------------------------------------------------------------------------
# 2) ISO 27001 CONTROL COVERAGE  (are the mapped controls in place?)
# ---------------------------------------------------------------------------
CONTROL_STATUS = {   # illustrative maturity of each Annex A theme
    "A.5 Organizational": "Partial",
    "A.6 People": "Partial",
    "A.7 Physical": "Implemented",
    "A.8 Technological": "Partial",
}


def control_coverage(reg: pd.DataFrame) -> pd.DataFrame:
    """How many open risks touch each Annex A theme (A.5/6/7/8)."""
    theme = {"A.5": "A.5 Organizational", "A.6": "A.6 People",
             "A.7": "A.7 Physical", "A.8": "A.8 Technological"}
    rows = []
    for key, name in theme.items():
        touching = reg[reg["ISO 27001"].str.contains(key)]
        open_high = touching[(touching["Status"] != "Closed") &
                             (touching["Rating"].isin(["Critical", "High"]))]
        rows.append({"Annex A theme": name,
                     "Control status": CONTROL_STATUS.get(name, "Unknown"),
                     "Risks mapped": len(touching),
                     "Open High/Critical": len(open_high)})
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# 3) VENDOR SECURITY QUESTIONNAIRE  (weighted third-party due diligence)
# ---------------------------------------------------------------------------
# question, weight, vendor answer (True = control present)
VENDOR = "Acme Cloud Services"
QUESTIONNAIRE = [
    ("Holds ISO 27001 or SOC 2 certification?", 3, True),
    ("Enforces MFA on all admin access?", 3, True),
    ("Encrypts data at rest and in transit?", 3, True),
    ("Documented incident response plan?", 2, True),
    ("Annual penetration testing?", 2, False),
    ("Least-privilege / RBAC access model?", 2, True),
    ("Security awareness training program?", 1, False),
    ("Sub-processor / fourth-party oversight?", 2, False),
    ("Right-to-audit clause in contract?", 1, True),
    ("Breach notification SLA (<= 72h)?", 2, True),
]


def vendor_assessment() -> tuple[pd.DataFrame, dict]:
    rows, earned, total = [], 0, 0
    for q, w, ans in QUESTIONNAIRE:
        total += w
        earned += w if ans else 0
        rows.append({"Question": q, "Weight": w,
                     "Answer": "Yes" if ans else "No",
                     "Score": w if ans else 0})
    pct = 100 * earned / total
    tier = ("Low Risk" if pct >= 85 else "Medium Risk" if pct >= 65 else "High Risk")
    summary = {"vendor": VENDOR, "earned": earned, "total": total,
               "pct": pct, "tier": tier}
    return pd.DataFrame(rows), summary


# ---------------------------------------------------------------------------
# Heat map + reporting
# ---------------------------------------------------------------------------
def heatmap(reg: pd.DataFrame) -> str | None:
    if not HAVE_PLT:
        return None
    import numpy as np
    grid = np.zeros((5, 5), dtype=int)
    for _, r in reg.iterrows():
        grid[5 - r["Impact"], r["Likelihood"] - 1] += 1
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.imshow(grid, cmap="YlOrRd")
    ax.set_xticks(range(5)); ax.set_xticklabels(range(1, 6))
    ax.set_yticks(range(5)); ax.set_yticklabels(range(5, 0, -1))
    ax.set_xlabel("Likelihood"); ax.set_ylabel("Impact")
    ax.set_title("Risk Heat Map (count of risks)")
    for i in range(5):
        for j in range(5):
            if grid[i, j]:
                ax.text(j, i, grid[i, j], ha="center", va="center")
    p = os.path.join(OUT, "risk_heatmap.png")
    fig.tight_layout(); fig.savefig(p, dpi=130); plt.close(fig)
    return p


def main():
    reg = risk_register()
    cov = control_coverage(reg)
    vq, vs = vendor_assessment()

    print("\n=== RISK REGISTER (top risks by score) ===")
    print(reg[["ID", "Risk", "Likelihood", "Impact", "Score", "Rating", "Status"]]
          .to_string(index=False))
    print("\nRating summary:", reg["Rating"].value_counts().to_dict())

    print("\n=== ISO 27001 ANNEX A COVERAGE ===")
    print(cov.to_string(index=False))

    print(f"\n=== VENDOR ASSESSMENT: {vs['vendor']} ===")
    print(f"Score {vs['earned']}/{vs['total']} = {vs['pct']:.0f}%  ->  {vs['tier']}")

    path = os.path.join(OUT, "grc_risk_toolkit.xlsx")
    with pd.ExcelWriter(path, engine="openpyxl") as xl:
        reg.to_excel(xl, sheet_name="Risk_Register", index=False)
        cov.to_excel(xl, sheet_name="Control_Mapping", index=False)
        vq.to_excel(xl, sheet_name="Vendor_Assessment", index=False)
    hm = heatmap(reg)
    print(f"\n[out] {path}")
    if hm:
        print(f"[out] {hm}")


if __name__ == "__main__":
    main()
