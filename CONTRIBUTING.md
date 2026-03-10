# Contributing (ARGOS)

## Workflow
1. Create a branch: `feature/<short-name>`
2. Keep commits small and descriptive.
3. Update relevant docs when changing behavior.
4. Add a short entry to `CHANGELOG.md` for user-visible changes.

## Required checks (local)
- `python -m compileall software/src`
- `python -m pytest` (when tests exist)
- Run the app in a simulated mode before merging.

## Roles
- Docs updates: `docs/`
- Software updates: `software/`
- Hardware notes and wiring: `hardware/`
