"""
Voyager — Synthetic Data Generator
==================================

Generates two files:
  - customers.csv     : one row per customer (profile / demographics)
  - transactions.csv  : many rows per customer (6 months of transaction history)

A subset of customers get INJECTED events so downstream models have real
signal to detect:
  - life_stage events  -> should trigger the Recommendation Engine
  - stress events      -> should trigger the Stress Detection Engine
  - fraud events        -> should trigger the Fraud Detection Engine

Each injected row is tagged with an `event_type` column so you can verify
later (in your model evaluation) that your engines actually caught them.

Usage:
    pip install faker pandas numpy
    python generate_synthetic_data.py
"""

import numpy as np
import pandas as pd
from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker("en_IN")
random.seed(42)
np.random.seed(42)

N_CUSTOMERS = 500
MONTHS_OF_HISTORY = 6
START_DATE = datetime.now() - timedelta(days=30 * MONTHS_OF_HISTORY)

CITY_TIERS = ["Tier-1", "Tier-2", "Tier-3"]
INCOME_BANDS = ["Low (< 25k/mo)", "Mid (25k-75k/mo)", "High (> 75k/mo)"]
LIFE_STAGES = ["Young Professional", "Newly Married", "New Parent", "Homeowner-in-progress"]

INCOME_BAND_RANGE = {
    "Low (< 25k/mo)": (12000, 25000),
    "Mid (25k-75k/mo)": (25000, 75000),
    "High (> 75k/mo)": (75000, 200000),
}

SPEND_CATEGORIES = ["Groceries", "Rent", "Utilities", "Dining", "Travel",
                     "Shopping", "Healthcare", "Education", "EMI", "Entertainment"]


def make_customers(n):
    rows = []
    for i in range(n):
        income_band = random.choice(INCOME_BANDS)
        low, high = INCOME_BAND_RANGE[income_band]
        salary = round(random.uniform(low, high), -2)
        rows.append({
            "customer_id": f"CUST{i:04d}",
            "name": fake.name(),
            "age": random.randint(22, 55),
            "city_tier": random.choice(CITY_TIERS),
            "income_band": income_band,
            "monthly_salary": salary,
            "life_stage": random.choice(LIFE_STAGES),
            "has_existing_life_insurance": random.random() < 0.35,
            "has_existing_loan": random.random() < 0.4,
        })
    return pd.DataFrame(rows)


def make_baseline_transactions(customer):
    """Generate ~6 months of normal recurring transactions for one customer."""
    txns = []
    salary = customer["monthly_salary"]
    cust_id = customer["customer_id"]

    for month in range(MONTHS_OF_HISTORY):
        month_start = START_DATE + timedelta(days=30 * month)

        # Salary credit — regular, same day each month
        txns.append({
            "customer_id": cust_id,
            "date": month_start + timedelta(days=1),
            "category": "Salary Credit",
            "amount": salary,
            "direction": "credit",
            "event_type": "normal",
        })

        # Rent
        if random.random() < 0.7:
            txns.append({
                "customer_id": cust_id,
                "date": month_start + timedelta(days=3),
                "category": "Rent",
                "amount": -round(salary * random.uniform(0.15, 0.3), -2),
                "direction": "debit",
                "event_type": "normal",
            })

        # EMI (if they have a loan)
        if customer["has_existing_loan"]:
            txns.append({
                "customer_id": cust_id,
                "date": month_start + timedelta(days=5),
                "category": "EMI",
                "amount": -round(salary * random.uniform(0.1, 0.25), -2),
                "direction": "debit",
                "event_type": "normal",
            })

        # Everyday spend — several small transactions per month
        for _ in range(random.randint(8, 20)):
            cat = random.choice(SPEND_CATEGORIES[:-1])  # exclude EMI here
            day_offset = random.randint(0, 29)
            txns.append({
                "customer_id": cust_id,
                "date": month_start + timedelta(days=day_offset),
                "category": cat,
                "amount": -round(random.uniform(200, salary * 0.05), -1),
                "direction": "debit",
                "event_type": "normal",
            })

    return txns


def inject_life_stage_event(txns, customer):
    """Add a life-stage signal, e.g. wedding spend spike or home-loan enquiry."""
    cust_id = customer["customer_id"]
    event_date = START_DATE + timedelta(days=random.randint(60, 150))
    event_choice = random.choice(["wedding", "home_loan_enquiry", "baby_products"])

    if event_choice == "wedding":
        txns.append({
            "customer_id": cust_id, "date": event_date, "category": "Shopping",
            "amount": -round(random.uniform(50000, 150000), -3),
            "direction": "debit", "event_type": "life_stage_wedding",
        })
    elif event_choice == "home_loan_enquiry":
        txns.append({
            "customer_id": cust_id, "date": event_date, "category": "Registration Fee",
            "amount": -round(random.uniform(5000, 20000), -2),
            "direction": "debit", "event_type": "life_stage_home_purchase",
        })
    else:
        txns.append({
            "customer_id": cust_id, "date": event_date, "category": "Baby Products",
            "amount": -round(random.uniform(2000, 8000), -2),
            "direction": "debit", "event_type": "life_stage_new_parent",
        })


def inject_stress_event(txns, customer):
    """Simulate a missed EMI or a sudden drop in transaction activity."""
    cust_id = customer["customer_id"]
    event_date = START_DATE + timedelta(days=random.randint(90, 170))

    # Remove or mark a missed EMI — represented as a zero/failed EMI row
    txns.append({
        "customer_id": cust_id, "date": event_date, "category": "EMI",
        "amount": 0, "direction": "debit", "event_type": "stress_missed_emi",
    })

    # Also drop the following month's discretionary spend to simulate income stress
    for _ in range(3):
        txns.append({
            "customer_id": cust_id,
            "date": event_date + timedelta(days=random.randint(1, 20)),
            "category": "Groceries",
            "amount": -round(random.uniform(100, 300), -1),  # much smaller than usual
            "direction": "debit", "event_type": "stress_spend_drop",
        })


def inject_fraud_event(txns, customer):
    """Simulate an odd-hour, unusually large transfer — a fraud signature."""
    cust_id = customer["customer_id"]
    event_date = START_DATE + timedelta(days=random.randint(30, 170), hours=random.randint(1, 4))

    txns.append({
        "customer_id": cust_id, "date": event_date, "category": "Transfer",
        "amount": -round(random.uniform(40000, 100000), -3),
        "direction": "debit", "event_type": "fraud_odd_hour_transfer",
    })


def main():
    customers = make_customers(N_CUSTOMERS)

    all_txns = []
    # Pick disjoint subsets of customers to inject each event type into
    ids = customers["customer_id"].tolist()
    random.shuffle(ids)
    life_stage_ids = set(ids[:40])          # ~8% get a life-stage event
    stress_ids = set(ids[40:70])            # ~6% get a stress event
    fraud_ids = set(ids[70:75])             # ~1% get a fraud event

    for _, customer in customers.iterrows():
        txns = make_baseline_transactions(customer)

        if customer["customer_id"] in life_stage_ids:
            inject_life_stage_event(txns, customer)
        if customer["customer_id"] in stress_ids:
            inject_stress_event(txns, customer)
        if customer["customer_id"] in fraud_ids:
            inject_fraud_event(txns, customer)

        all_txns.extend(txns)

    transactions = pd.DataFrame(all_txns).sort_values(["customer_id", "date"])

    customers.to_csv("customers.csv", index=False)
    transactions.to_csv("transactions.csv", index=False)

    print(f"Generated {len(customers)} customers and {len(transactions)} transactions.")
    print(f"Injected events -> life_stage: {len(life_stage_ids)}, "
          f"stress: {len(stress_ids)}, fraud: {len(fraud_ids)}")
    print("Files written: customers.csv, transactions.csv")


if __name__ == "__main__":
    main()
