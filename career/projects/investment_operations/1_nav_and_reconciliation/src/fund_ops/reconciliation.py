"""Two-way reconciliation engine (internal book vs custodian).

A single generic engine reconciles both **trades** and **cash** by an ID key
and classifies every record into one break type. This mirrors an ops
reconciliation control: the internal book (the fund accountant's records) is
matched against the custodian's statement and every difference becomes an
exception on an aged queue.

Break taxonomy
--------------
  MATCHED               : key present both sides, all compared fields agree.
  QUANTITY_MISMATCH     : same trade, different quantity.
  PRICE_AMOUNT_MISMATCH : same trade/cash, different price or settlement amount.
  DUPLICATE             : the same key booked more than once on one side.
  MISSING_AT_CUSTODIAN  : in the book but absent from the custodian (unmatched book).
  ORPHAN_AT_CUSTODIAN   : at the custodian but absent from the book (unmatched custodian).

Each break is aged (trade/value date -> valuation date) and bucketed, and given
a severity so the exception queue can be worked worst-first.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

AMOUNT_TOL = 0.01  # sub-cent differences are treated as equal (rounding noise)

SEVERITY = {
    "PRICE_AMOUNT_MISMATCH": "High",
    "MISSING_AT_CUSTODIAN": "High",
    "ORPHAN_AT_CUSTODIAN": "High",
    "QUANTITY_MISMATCH": "Medium",
    "DUPLICATE": "Medium",
}


def _aging_bucket(days: float) -> str:
    if days <= 2:
        return "0-2d"
    if days <= 5:
        return "3-5d"
    if days <= 10:
        return "6-10d"
    return "10d+"


def _duplicate_keys(df: pd.DataFrame, key: str) -> set:
    counts = df[key].value_counts()
    return set(counts[counts > 1].index)


def reconcile(book, cust, key, primary_value, compare_cols, date_col, valuation_date):
    """Reconcile two record sets and return the exception queue (breaks only).

    Parameters
    ----------
    key           : column that uniquely identifies a record (e.g. ``trade_id``).
    primary_value : the headline monetary column (``net_amount`` / ``amount``).
    compare_cols  : ordered dict {column: break_type} of fields to compare.
    date_col      : date column used for aging.
    """
    book_dupes = _duplicate_keys(book, key)
    cust_dupes = _duplicate_keys(cust, key)

    b = book.drop_duplicates(subset=key, keep="first").set_index(key)
    c = cust.drop_duplicates(subset=key, keep="first").set_index(key)
    all_keys = list(dict.fromkeys(list(b.index) + list(c.index)))

    rows = []
    for k in all_keys:
        in_b, in_c = k in b.index, k in c.index

        if in_b and in_c:
            br, cr = b.loc[k], c.loc[k]
            diffs = []
            break_type = "MATCHED"
            for col, label in compare_cols.items():
                if abs(float(br[col]) - float(cr[col])) > AMOUNT_TOL:
                    diffs.append(f"{col}: book={br[col]:g} vs cust={cr[col]:g}")
                    if break_type == "MATCHED":
                        break_type = label
            if k in book_dupes or k in cust_dupes:
                break_type = "DUPLICATE"
                side = "book" if k in book_dupes else "custodian"
                diffs.append(f"duplicated on {side}")
            bval, cval = float(br[primary_value]), float(cr[primary_value])
            date_val = br[date_col]
        elif in_b:
            br = b.loc[k]
            break_type = "MISSING_AT_CUSTODIAN"
            bval, cval = float(br[primary_value]), np.nan
            diffs = ["present in book, absent at custodian"]
            date_val = br[date_col]
        else:
            cr = c.loc[k]
            break_type = "ORPHAN_AT_CUSTODIAN"
            bval, cval = np.nan, float(cr[primary_value])
            diffs = ["present at custodian, absent in book"]
            date_val = cr[date_col]

        if break_type == "MATCHED":
            continue  # only breaks go on the exception queue

        age = (valuation_date - pd.Timestamp(date_val)).days
        diff_val = (bval if not np.isnan(bval) else 0.0) - (cval if not np.isnan(cval) else 0.0)
        rows.append(
            {
                "key": k,
                "break_type": break_type,
                "severity": SEVERITY.get(break_type, "Low"),
                "book_value": bval,
                "custodian_value": cval,
                "difference": diff_val,
                "age_days": age,
                "aging_bucket": _aging_bucket(age),
                "detail": "; ".join(diffs),
            }
        )

    queue = pd.DataFrame(rows)
    if not queue.empty:
        sev_order = {"High": 0, "Medium": 1, "Low": 2}
        queue["_s"] = queue["severity"].map(sev_order)
        queue = queue.sort_values(["_s", "age_days"], ascending=[True, False]).drop(columns="_s")
        queue = queue.reset_index(drop=True)
    return queue


def reconcile_trades(book_trades, cust_trades, valuation_date) -> pd.DataFrame:
    return reconcile(
        book_trades, cust_trades,
        key="trade_id", primary_value="net_amount",
        compare_cols={"quantity": "QUANTITY_MISMATCH", "net_amount": "PRICE_AMOUNT_MISMATCH"},
        date_col="trade_date", valuation_date=valuation_date,
    )


def reconcile_cash(book_cash, cust_cash, valuation_date) -> pd.DataFrame:
    # Cash movements share no common id across the two systems, so we key on the
    # business reference (type + reference) instead of the internal cash_id.
    book = book_cash.copy()
    cust = cust_cash.copy()
    book["match_key"] = book["cash_type"] + "|" + book["reference"]
    cust["match_key"] = cust["cash_type"] + "|" + cust["reference"]
    return reconcile(
        book, cust,
        key="match_key", primary_value="amount",
        compare_cols={"amount": "PRICE_AMOUNT_MISMATCH"},
        date_col="value_date", valuation_date=valuation_date,
    )


def break_summary(queue: pd.DataFrame) -> pd.DataFrame:
    """Counts by break type for the console / Excel summary."""
    if queue.empty:
        return pd.DataFrame(columns=["break_type", "count"])
    out = queue.groupby("break_type").size().reset_index(name="count")
    return out.sort_values("count", ascending=False).reset_index(drop=True)


def aging_summary(queue: pd.DataFrame) -> pd.DataFrame:
    """Counts by aging bucket for the break-aging chart."""
    order = ["0-2d", "3-5d", "6-10d", "10d+"]
    if queue.empty:
        return pd.DataFrame({"aging_bucket": order, "count": [0, 0, 0, 0]})
    counts = queue["aging_bucket"].value_counts().to_dict()
    return pd.DataFrame({"aging_bucket": order, "count": [counts.get(b, 0) for b in order]})
