"""
Voyager — Vernacular Conversational AI
========================================
A guided state machine for ONE journey (start with loan application),
in ONE extra language beyond English (e.g., Hindi). The state variable
tracks progress; an LLM call handles only understanding/generating each
turn's language — not deciding what step comes next.

TODO (prompt an AI assistant with this docstring):
    1. Define states, e.g.:
       GREETING -> ASK_PURPOSE -> ASK_AMOUNT -> CONFIRM_INCOME
       -> DOCUMENT_CHECKLIST -> DONE
    2. Implement `handle_turn(session_state: dict, user_message: str) -> dict`
       that:
         - calls an LLM (or simple prompt template) to extract the needed
           slot value from user_message (e.g., loan purpose) in the
           user's language
         - advances session_state to the next step
         - returns a natural-language reply in the same language,
           written in plain terms (no regulatory jargon)
    3. If the LLM's confidence is low or the user seems stuck for 2+ turns,
       set session_state["escalate_to_human"] = True.

Keep the state machine and the "language understanding" concerns
separate — this makes the flow debuggable without needing to poke at
an LLM every time you test step transitions.
"""


def handle_turn(session_state: dict, user_message: str) -> dict:
    raise NotImplementedError("Ask your AI assistant to implement this — see module docstring.")
