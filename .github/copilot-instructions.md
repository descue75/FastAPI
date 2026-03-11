<!-- .github/copilot-instructions.md -->
# Copilot instructions — FastAPI

Purpose
- Help an AI coding agent become productive in this small FastAPI project.

Quick start (how to run & test locally)
- Create and activate a virtual env (Windows):

  ```powershell
  python -m venv .\venv
  .\venv\Scripts\activate
  pip install "fastapi[all]"
  ```
- Run the dev server (common entrypoint):

  ```powershell
  uvicorn app.main:app --reload --port 8000
  ```

What I found (big-picture)
- This repo is a minimal FastAPI app. Key files:
  - [README.md](README.md#L1-L5)
  - [app/main.py](app/main.py)
  - [app/__init__.py](app/__init__.py)
- Currently `app/main.py` and `app/__init__.py` are empty; most work will be adding routes and app wiring inside `app/`.

Project-specific conventions & patterns to follow
- Package namespace: use the `app` package as the service root. Example import targets: `app.main:app` for `uvicorn`.
- Keep application factory or single `FastAPI` instance in `app/main.py` (if you add an application factory, export it as `create_app()` and an `app` instance for convenience).
- Prefer organizing handlers under `app/routers/` (create this folder) and include them in `app/main.py` via `app.include_router(...)`.

Integration points & dependencies
- Primary dependency: `fastapi` (README recommends `fastapi[all]`). Use `uvicorn` as the ASGI server. No database or external services are present yet in repository — if you add integrations, place config in `app/config.py` and clients in `app/services/`.

Developer workflows
- Local dev server: run `uvicorn app.main:app --reload` (see above).
- Virtualenv convention: repository README shows a venv at `./venv` on Windows — follow that for consistent dev environments.
- Tests: none discovered. If adding tests, follow pytest conventions and place them under `tests/`.

How the agent should make changes
- Small, focused PRs: change one logical area (route, service, test) per PR and add or update `README.md` or example usage when adding endpoints.
- When adding new files, update `app/__init__.py` or `app/main.py` to clearly export the app instance (`app`) so `uvicorn app.main:app` continues to work.

Useful examples for the agent
- Add a simple health route in `app/main.py`:

  ```py
  from fastapi import FastAPI

  app = FastAPI()

  @app.get("/health")
  def health():
      return {"status": "ok"}
  ```

Notes & limitations
- No CI, tests, or database code were found — any instructions about those systems must be explicitly added to this repo before relying on them.
- Preserve this file when updating; if you merge an existing `.github/copilot-instructions.md`, prefer keeping the Quick start and What I found sections intact.

If anything here is unclear or you'd like me to expand sections (routing conventions, config layout, example router files, or tests), tell me which area to update.
