"""
Voyager — Financial Stress & Fraud Early-Warning Engine
========================================================
Detects deviations from a customer's own behavioral baseline and assigns
a severity tier. This module should be testable in isolation against the
injected stress/fraud rows in data/transactions.csv (event_type column
starting with "stress_" or "fraud_").

TODO (prompt an AI assistant with this docstring):
    1. `build_baseline(customer_id, transactions_df) -> dict`
       Rolling average + std dev of transaction size/frequency for one
       customer, using only their "normal" history (first ~3 months).

    2. `detect_anomaly(customer_id, transactions_df, baseline) -> list[dict]`
       Compare recent transactions against baseline using z-score or
       Isolation Forest. Return a list of flagged events, each with a
       severity: "low" | "medium" | "high".
       Severity guide (from the ethics design):
         - low:    single missed EMI
         - medium: sustained spend decline + EMI stress
         - high:   odd-hour, high-value transfer or new-device + high-value txn

    3. Validate against ground truth: filter transactions_df for
       event_type in ["stress_missed_emi", "stress_spend_drop",
       "fraud_odd_hour_transfer"] and confirm detect_anomaly() actually
       flags those same customers/dates. Report precision/recall.
"""

import pandas as pd


def build_baseline(customer_id: str, transactions_df: pd.DataFrame) -> dict:
    raise NotImplementedError("Ask your AI assistant to implement this — see module docstring.")


def detect_anomaly(customer_id: str, transactions_df: pd.DataFrame, baseline: dict) -> list:
    raise NotImplementedError("Ask your AI assistant to implement this — see module docstring.")
