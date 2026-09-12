# Voyager Frontend

Build this LAST, once the backend API works end-to-end.

Recommended: `npx create-react-app .` (or Vite) inside this folder, add
Tailwind, then build three components against your real API responses:

1. **NextBestActionCard** — calls `GET /recommend/{customer_id}`, shows
   the recommended product + the one-line reason string.
2. **ChatWidget** — calls `POST /chat`, renders the guided conversation
   turn by turn.
3. **StressAlertBanner** — calls `GET /stress-check/{customer_id}`,
   shows an empathetic message (not a red "blocked" warning) for
   low/medium severity, and a clear escalation notice for high severity.

Charts (if you add a spend-overview view): Recharts or D3, fed from
the same feature data your backend already computes.
