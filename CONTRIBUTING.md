# Contributing — ARGOS V1

Este repositorio busca estabilidad: cambios pequeños, bien documentados y con evidencia.

## Reglas rápidas
1) Una tarea = un PR (o un commit claro si trabajan local).
2) No romper estructura del repo sin aprobación del equipo.
3) Todo cambio técnico debe dejar evidencia:
   - logs, video, fotos, o reporte de prueba (según aplique).
4) Actualiza `CHANGELOG.md` cuando el cambio sea “visible” o afecte el uso.

## Flujo recomendado (Git)
- Branch: `feature/<tema>` o `fix/<tema>`
- Commits cortos y descriptivos
- Merge solo si:
  - compila/ejecuta (mínimo)
  - hay evidencia de prueba (cuando aplique)

## Dónde va cada cosa
- Documentación: `docs/`
- Código Pi 5: `software/`
- Cableado y BOM: `hardware/`
- Logos/medios: `assets/`
- Despliegue Pi: `deploy/`
- Dataset: `datasets/` (no subir crudos por defecto)

## Estándares de código (Python)
- Mantener módulos pequeños y legibles.
- Evitar “scripts gigantes”. Si hay un prototipo único:
  - guardarlo en `software/legacy/current_prototype.py`
  - migrar poco a poco a `software/src/argos_app/`

## Pruebas mínimas antes de subir cambios
- `python -m compileall software/src`
- Ejecución en Pi (si toca hardware): iniciar y capturar logs.
- Actualizar bitácora de iteraciones: `docs/plantillas/Bitacora_Iteraciones.md`

## Contacto interno
Si un cambio afecta seguridad o hardware, validar primero con coaches/mentores.