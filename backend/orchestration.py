"""
Voyager — Orchestration / Decision Layer
==========================================
The single place where all three engine outputs meet and the ethics
guardrails are enforced. Build this LAST, once recommendation.py and
stress_detection.py both work independently — and write this one
yourself (or review an AI's version closely) since it encodes your
hard ethical rules.

TODO: Implement `decide_action(recommendation, stress_result, chat_intent=None) -> dict`
Required behavior:
    - If stress_result["severity"] in ("medium", "high"):
        -> suppress any loan/credit product recommendation, regardless
           of what the recommendation engine returned (hard rule, not
           a soft preference — see Ethical Safeguards in the write-up).
    - If stress_result["severity"] == "high":
        -> action = "escalate", route to human agent / fraud team.
    - If stress_result["severity"] == "low":
        -> action = "support", surface an empathetic nudge (not a block).
    - Otherwise:
        -> action = "recommend", pass through the recommendation as-is.

Return shape example:
    {
        "action": "support",             # recommend | educate | support | escalate
        "message": "...",                # user-facing text
        "reason": "...",                 # one-line explainability string
        "requires_human_review": False,  # True for medium/high severity
    }
"""


def decide_action(recommendation: dict, stress_result: dict, chat_intent: dict = None) -> dict:
    raise NotImplementedError("Implement this yourself first — it encodes the ethics rules.")
