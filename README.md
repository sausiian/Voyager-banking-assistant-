# Voyager — AI-Powered Hyper-Personalized Banking for Bharat

## Repo structure

```
voyager/
├── data/
│   └── generate_synthetic_data.py   # run this first — outputs customers.csv, transactions.csv
├── backend/
│   ├── features.py                  # raw transactions -> per-customer features
│   ├── recommendation.py            # rule-based + ML "next best action" engine
│   ├── stress_detection.py          # anomaly / stress / fraud detection
│   ├── orchestration.py             # combines all engines, enforces ethics rules
│   ├── chatbot.py                   # vernacular guided conversation state machine
│   ├── main.py                      # FastAPI app wiring it all together
│   └── requirements.txt
├── frontend/
│   └── README.md                    # what to build once the API is ready
└── docs/                            # architecture diagram, ethics note, etc.
```

## Build order

1. `cd data && python generate_synthetic_data.py`
2. `backend/features.py` — implement `build_features()`, test standalone
3. `backend/recommendation.py` — rule-based first, then layer ML on top
4. `backend/stress_detection.py` — build and validate against injected events
5. `backend/main.py` — wire steps 2–4 into FastAPI endpoints
6. `backend/chatbot.py` — one journey, one extra language
7. `backend/orchestration.py` — ethics rules, build/review this one carefully yourself
8. `frontend/` — dashboard + chat widget, built against the real API

Each `backend/*.py` file (except `orchestration.py` and `main.py`) has a
docstring at the top written as a ready-to-use prompt for an AI coding
assistant — paste it in along with a sample of `customers.csv` /
`transactions.csv` and ask it to implement the `TODO`.

## Notes

- Test every module standalone (run the `if __name__ == "__main__"` block
  or a quick script) before wiring it into `main.py`.
- `orchestration.py` is the one file you should write or review most
  carefully — it's where the "never recommend a loan to a stressed
  customer" rule lives, and that rule needs to actually be enforced in
  code, not just described in your docs.
