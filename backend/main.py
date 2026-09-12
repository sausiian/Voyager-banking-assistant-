"""
Voyager — Backend API
======================
Thin FastAPI layer that wires together features.py, recommendation.py,
stress_detection.py, orchestration.py, and chatbot.py.

Build this AFTER the modules above work independently (run them from the
command line / a notebook first). This file should contain almost no
logic of its own — each endpoint just calls existing functions.

TODO (prompt an AI assistant with this docstring):
    GET  /recommend/{customer_id}   -> build_features -> next_best_action
    GET  /stress-check/{customer_id} -> build_baseline + detect_anomaly
    POST /chat                       -> chatbot.handle_turn
    GET  /decision/{customer_id}     -> calls the above three, then
                                         orchestration.decide_action

Run with: uvicorn main:app --reload
"""

from fastapi import FastAPI

app = FastAPI(title="Voyager API")


@app.get("/")
def root():
    return {"status": "Voyager backend running"}


# TODO: add the endpoints described above, importing from:
# from features import build_features
# from recommendation import next_best_action
# from stress_detection import build_baseline, detect_anomaly
# from orchestration import decide_action
# from chatbot import handle_turn
