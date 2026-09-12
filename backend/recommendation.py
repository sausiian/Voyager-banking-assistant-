"""
Voyager — Recommendation Engine ("Next Best Action")
=====================================================
Two layers, built in this order:

1. RULE-BASED (build first — this is your explainability baseline)
   TODO: Implement `rule_based_recommendation(feature_row) -> dict`
   returning e.g. {"product": "Term Insurance", "reason": "Regular salary
   credits detected and no existing life insurance on file."}
   Example rules to start with:
     - salary_regular AND NOT has_existing_life_insurance AND 25<=age<=40
         -> recommend Term Insurance
     - emi_to_income_ratio dropped after a loan closed
         -> recommend a Fixed Deposit / investment product
     - top_spend_category == "Baby Products"
         -> recommend Child Insurance / Education Plan

2. ML LAYER (build second, on top of the rules — do not replace them)
   TODO: Implement `train_propensity_model(features_df, labels_df)` and
   `ml_recommendation(feature_row, model) -> dict` using XGBoost/LightGBM
   to score likelihood-of-positive-response per product, then combine
   with the rule output into a final ranked list (top 1-2 only).

Both functions must return a short natural-language `reason` string —
this is what the orchestration layer and dashboard show to satisfy the
"explainable AI" requirement.
"""


def rule_based_recommendation(feature_row: dict) -> dict:
    raise NotImplementedError("Ask your AI assistant to implement this — see module docstring.")


def ml_recommendation(feature_row: dict, model) -> dict:
    raise NotImplementedError("Ask your AI assistant to implement this — see module docstring.")


def next_best_action(feature_row: dict, model=None) -> dict:
    """Combines rule + ML output into the final recommendation shown to the user."""
    rule_result = rule_based_recommendation(feature_row)
    if model is not None:
        ml_result = ml_recommendation(feature_row, model)
        # TODO: merge/rank rule_result and ml_result here
        return ml_result
    return rule_result
