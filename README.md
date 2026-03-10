# ARGOS (V1)

**ARGOS V1** is a safety-oriented exploration prototype for underground/cave-like environments, designed by **CALIBOTS KAIROS**.

It operationalizes safety in three moments:
- **Before:** initial risk evaluation
- **During:** continuous monitoring + alerts + telemetry
- **After:** evidence + report for analysis

## Repository structure (stable)
- `docs/` — official documentation (thesis-style chapters, safety protocol, templates)
- `assets/` — brand assets and non-code media (logos, renders)
- `software/` — Raspberry Pi 5 application (Python) + configs + deployment files
- `hardware/` — wiring, BOM, mechanical notes
- `datasets/` — dataset metadata and instructions (raw media is not tracked)
- `tests/` — tests for software modules (grows over time)
- `deploy/` — systemd services and field deployment notes

## Quick start (Raspberry Pi)
See: `software/README.md`

## Documentation entry point
Start here: `docs/README.md`

## Safety note
This is an educational prototype. Do not use it as a substitute for certified safety instruments or professional procedures.
