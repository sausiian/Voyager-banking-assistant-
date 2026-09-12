"""
Voyager — Feature Engineering
=============================
Turns raw transactions (from data/transactions.csv) into per-customer
behavioral features that the Recommendation and Stress engines consume.

TODO (prompt an AI assistant with this docstring + a sample of transactions.csv):
    Build a function `build_features(transactions_df, customers_df) -> pd.DataFrame`
    that returns one row per customer with columns such as:
      - salary_regularity_score   (are salary credits consistent month to month?)
      - emi_to_income_ratio       (total EMI debits / monthly salary)
      - savings_trend             (rolling change in end-of-month balance proxy)
      - spend_velocity            (avg transactions per week, recent vs. baseline)
      - top_spend_category        (dominant discretionary category, for life-stage hints)
      - has_recent_large_debit    (any single debit > 3x their median transaction)

Keep this file free of any ML/rule logic — it should ONLY compute features.
Recommendation and stress-detection logic belong in their own files.
"""

import pandas as pd


def build_features(transactions_df: pd.DataFrame, customers_df: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError("Ask your AI assistant to implement this — see module docstring.")


if __name__ == "__main__":
    transactions = pd.read_csv("../data/transactions.csv", parse_dates=["date"])
    customers = pd.read_csv("../data/customers.csv")
    features = build_features(transactions, customers)
    print(features.head())
