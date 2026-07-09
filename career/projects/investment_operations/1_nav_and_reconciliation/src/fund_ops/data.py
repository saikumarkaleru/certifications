"""Data-access layer: load the synthetic sample files from ``input/``.

Everything is plain CSV so the whole tool runs fully offline. This module only
reads and lightly types the data; all business logic lives in the other modules.
"""

from __future__ import annotations

import os

import pandas as pd

STALE_PRICE_DAYS = 3  # a price older than this many calendar days is "stale"


def _read_csv(input_dir: str, name: str, **kwargs) -> pd.DataFrame:
    return pd.read_csv(os.path.join(input_dir, name), **kwargs)


def load_positions(input_dir: str) -> pd.DataFrame:
    df = _read_csv(input_dir, "positions.csv")
    df["quantity"] = df["quantity"].astype(float)
    return df


def load_prices(input_dir: str, name: str = "prices.csv") -> pd.DataFrame:
    df = _read_csv(input_dir, name, parse_dates=["price_date"])
    df["price"] = df["price"].astype(float)
    return df


def load_trades(input_dir: str, name: str) -> pd.DataFrame:
    df = _read_csv(input_dir, name, parse_dates=["trade_date", "settle_date"])
    for col in ("quantity", "price", "net_amount"):
        df[col] = df[col].astype(float)
    return df


def load_cash(input_dir: str, name: str) -> pd.DataFrame:
    df = _read_csv(input_dir, name, parse_dates=["value_date"])
    df["amount"] = df["amount"].astype(float)
    return df


def load_customers(input_dir: str) -> pd.DataFrame:
    df = _read_csv(input_dir, "customers.csv")
    for col in ("pep_flag", "adverse_media", "account_age_months", "expected_monthly_volume"):
        df[col] = df[col].astype(float)
    return df


def load_transactions(input_dir: str) -> pd.DataFrame:
    df = _read_csv(input_dir, "transactions.csv", parse_dates=["date"])
    df["amount"] = df["amount"].astype(float)
    return df


def load_fund_static(input_dir: str) -> dict:
    """Return the fund-level parameters as a typed dict."""
    raw = _read_csv(input_dir, "fund_static.csv")
    params = dict(zip(raw["parameter"], raw["value"]))
    return {
        "fund_name": params["fund_name"],
        "valuation_date": pd.Timestamp(params["valuation_date"]),
        "prior_valuation_date": pd.Timestamp(params["prior_valuation_date"]),
        "base_currency": params["base_currency"],
        "units_outstanding": float(params["units_outstanding"]),
        "cash_balance": float(params["cash_balance"]),
        "accrued_income": float(params["accrued_income"]),
        "ter_annual": float(params["ter_annual"]),
        "fee_accrual_days": int(float(params["fee_accrual_days"])),
        "other_accrued_expenses": float(params["other_accrued_expenses"]),
        "prior_nav_per_unit": float(params["prior_nav_per_unit"]),
    }
