"""
data.py -- load, clean and standardise the borrower spread
==========================================================

"Spreading" is the analyst's first job: take a borrower's messy statements and
re-cast every line into ONE standard template so different companies (and
different years) are directly comparable. That standard template is what the
whole rest of the toolkit consumes.

Inputs (bundled, synthetic-but-realistic, so the tool runs fully OFFLINE):
  input/financials.csv    long format: Company, Item, FY2022, FY2023, FY2024
  input/business_risk.csv qualitative 1-5 scores per company
  input/companies.csv     company code -> full name + sector

Output of load_all():
  facts_by_company : dict  code -> DataFrame
        index   = canonical line-item names (Revenue, EBITDA, Total Debt, ...)
        columns = fiscal years as ints (2022, 2023, 2024), oldest -> newest
  meta             : dict  code -> {"name": ..., "sector": ...}
  business         : dict  code -> {"MarketPosition": int, ...}

The spread is validated on load (accounting identities must hold) so a bad
input row is caught here, once, instead of silently poisoning a ratio later.
All figures are in INR crore.
"""

from __future__ import annotations

import os
import pandas as pd

_PKG_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_DIR = os.path.abspath(os.path.join(_PKG_DIR, "..", ".."))
INPUT_DIR = os.path.join(_PROJECT_DIR, "input")

# The canonical order we want every spread to appear in (income statement ->
# balance sheet -> cash flow -> debt schedule). Keeping the order fixed makes
# the Excel output read like a proper spread rather than a random dump.
LINE_ITEM_ORDER = [
    # Income statement
    "Revenue", "COGS", "Operating Expenses", "EBITDA",
    "Depreciation & Amortization", "EBIT", "Interest Expense",
    "PBT", "Tax", "Net Income",
    # Balance sheet
    "Cash & Equivalents", "Accounts Receivable", "Inventory", "Current Assets",
    "Net PPE", "Total Assets", "Accounts Payable", "Short-term Debt",
    "Current Liabilities", "Long-term Debt", "Total Debt", "Total Liabilities",
    "Total Equity",
    # Cash flow + debt schedule
    "Operating Cash Flow", "Capex", "Free Cash Flow",
    "Scheduled Principal Repayment",
]


def _path(name):
    return os.path.join(INPUT_DIR, name)


def load_all():
    """Load, clean and validate every borrower. Returns (facts, meta, business)."""
    raw = pd.read_csv(_path("financials.csv"))
    year_cols = [c for c in raw.columns if c.startswith("FY")]
    # FY2024 -> 2024 so columns are plain ints an analyst can sort/slice.
    year_map = {c: int(c.replace("FY", "")) for c in year_cols}

    facts_by_company = {}
    for code, grp in raw.groupby("Company"):
        df = grp.set_index("Item")[year_cols].rename(columns=year_map)
        # Coerce to numbers; a stray blank becomes NaN rather than a crash.
        df = df.apply(pd.to_numeric, errors="coerce")
        # Reindex onto the canonical order (missing rows surface as NaN).
        df = df.reindex(LINE_ITEM_ORDER)
        _validate(code, df)
        facts_by_company[code] = df

    meta = _load_meta()
    business = _load_business()
    return facts_by_company, meta, business


def _load_meta():
    m = pd.read_csv(_path("companies.csv")).set_index("Code")
    return {code: {"name": r["Name"], "sector": r["Sector"]}
            for code, r in m.iterrows()}


def _load_business():
    b = pd.read_csv(_path("business_risk.csv")).set_index("Company")
    return {code: {k: int(v) for k, v in r.items()} for code, r in b.iterrows()}


def _validate(code, df, tol=1.0):
    """Check the accounting identities that MUST hold in a clean spread.

    We only warn (never crash) so the tool still runs on slightly rough data,
    but a real break in an identity is exactly what a credit analyst wants
    flagged before trusting a single ratio.
    """
    checks = []
    for yr in df.columns:
        rev, cogs, opex = df.at["Revenue", yr], df.at["COGS", yr], df.at["Operating Expenses", yr]
        checks.append(("EBITDA = Rev - COGS - Opex",
                       df.at["EBITDA", yr], rev - cogs - opex, yr))
        checks.append(("EBIT = EBITDA - D&A",
                       df.at["EBIT", yr],
                       df.at["EBITDA", yr] - df.at["Depreciation & Amortization", yr], yr))
        checks.append(("Total Debt = ST + LT",
                       df.at["Total Debt", yr],
                       df.at["Short-term Debt", yr] + df.at["Long-term Debt", yr], yr))
        checks.append(("Assets = Liab + Equity",
                       df.at["Total Assets", yr],
                       df.at["Total Liabilities", yr] + df.at["Total Equity", yr], yr))
    for label, got, exp, yr in checks:
        if pd.notna(got) and pd.notna(exp) and abs(got - exp) > tol:
            print(f"   [WARN] {code} FY{yr}: {label} off by {got - exp:+.1f}")


def latest_year(facts):
    """The most recent fiscal year (max column)."""
    return max(facts.columns)


if __name__ == "__main__":  # quick smoke test
    f, m, b = load_all()
    for c in f:
        print(c, m[c]["name"], "->", latest_year(f[c]))
