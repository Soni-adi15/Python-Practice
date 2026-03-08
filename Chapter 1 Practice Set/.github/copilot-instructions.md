# Copilot Instructions for this repository ✅

> NOTE: This repo currently has no discoverable project files (no README, CI, or language-specific manifests found). This document is a living baseline—please update the sections marked TODO with concrete commands and files once available.

## Purpose
- Give AI coding agents the minimal, actionable context needed to be productive immediately: where to run builds, how tests run, repo conventions, and important integration points.
- If information is missing, follow the "Discovery steps" section below to locate it and then update this file.

## Quick discovery steps (run these first) 🔎
1. Search for language files/configs: `pyproject.toml`, `setup.py`, `requirements.txt`, `Pipfile`, `requirements-dev.txt`, `tox.ini`, `Makefile`, `package.json`, `Dockerfile`, `docker-compose.yml`.
2. Check CI/workflows in `.github/workflows/*.yml` for build/test commands.
3. Look for tests: `tests/`, `*/test_*.py`, `pytest.ini`.
4. Inspect top-level directories for services, e.g., `src/`, `app/`, `services/`, `api/`.

> If any of the above exist, record the concrete commands in the "Developer workflows" section below.

## Project "big picture" (what an agent should gather) 💡
- What are the main components? (e.g., web API, worker, CLI, data pipelines)
- Where is runnable entrypoint code (e.g., `main.py`, `app/__init__.py`, `server.py`)?
- Which files define configuration and environment variables? (e.g., `.env`, `config/*.py`, `settings.py`)

Add concrete answers here once discovered.

## Developer workflows (fill these in) 🛠️
- Install dependencies: TODO — replace with actual command (e.g., `pip install -r requirements.txt` or `poetry install`).
- Run tests: TODO — replace with actual command (e.g., `pytest -q` or `tox`).
- Run linters/type checks: TODO (e.g., `flake8`, `mypy`).
- Start app locally: TODO (e.g., `python -m app` or `uvicorn app.main:app --reload`).

Examples (if you discover a Python project):

- Install: `python -m pip install -r requirements.txt`
- Test: `pytest -q tests/`
- Lint: `flake8 src/`

## Project-specific conventions & patterns to look for 📐
- Module/package layout (single `src/` or top-level packages).
- Test naming (e.g., `tests/test_*.py` or `*/tests/*`).
- Logging and error handling styles (look for `logging.getLogger` use or custom exceptions).

Record concrete patterns here after inspection.

## Integration points & external dependencies 🔗
- Note any external services (databases, queues, third-party APIs) referenced in code or CI.
- Record expected environment variables and where they are documented.

## Typical PR tasks and examples ✏️
- Small bugfix: find unit tests that cover the bug, add/modify a unit test in `tests/`, run tests locally.
- Add feature: update the relevant package, add unit+integration tests, update docs/README.

## When information is missing
- If required commands or design rationale are not present in the repo, add a short comment in this file and ask the maintainers the following:
  - What commands are used to install, build, test, and run the app locally?
  - Where is the project architecture documented (diagrams, docs)?
  - Are there any non-standard coding or commit conventions to follow?

## Examples of actionable prompts for maintainers
- "Please specify the test command (pytest, tox, etc.) and the location of test directories."
- "Is there a local dev/start command for the API? If yes, share the exact command and environment variables needed."

---

If anything above is unclear or incomplete, please reply with the specific project files (or paste short excerpts) and I will update this file with precise commands, examples, and cross-references. ✅
