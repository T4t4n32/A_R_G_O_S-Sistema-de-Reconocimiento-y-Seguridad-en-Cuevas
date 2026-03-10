# Contributing — ARGOS V1

Este repositorio mantiene una estructura estable. Los cambios se registran con evidencia y sin reorganizar carpetas.

## Reglas
- Cambios pequeños, commits claros.
- Documentación actualizada cuando cambie comportamiento.
- Evidencia mínima por cambio (logs, foto, video o reporte de prueba).

## Dónde va cada cosa
- Documentación: `docs/`
- Código Raspberry Pi 5: `software/`
- Cableado/BOM/mecánica: `hardware/`
- Logos y medios: `assets/`
- Despliegue: `deploy/`
- Dataset: `datasets/` (no crudos por defecto)

## Prototipo actual
El código existente de una sola pieza vive en:
- `software/legacy/current_prototype.py`

Migración: se mueve funcionalidad a `software/src/` por módulos (sensores, comunicaciones, decisión, visión), sin borrar el archivo original.

## Comando (si una carpeta “local” aparece trackeada)
Carpetas locales no visibles por política:
- `.obsidian/`, `.calibots-kairos-platform/`, `.github/workflows/`

Comando para retirarlas del tracking si ya entraron a Git:
- `git rm -r --cached .obsidian .calibots-kairos-platform .github/workflows`