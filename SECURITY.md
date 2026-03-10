# SECURITY — ARGOS V1 (seguridad técnica y seguridad física)

ARGOS V1 es un prototipo educativo. No reemplaza instrumentos certificados ni autoriza ingreso a cuevas reales.

GitHub recomienda publicar un `SECURITY.md` para guiar reportes y buenas prácticas.
Referencia: https://docs.github.com/github/managing-security-vulnerabilities/adding-a-security-policy-to-your-repository

## 1) Seguridad física (obligatoria)
- Probar solo en entornos controlados (cueva simulada).
- No usar MQ-135 como medición de vida o muerte (es proxy cualitativo).
- Siempre usar supervisión responsable (adultos/coaches).
- Si hay baterías LiPo/Li-ion: usar BMS/fusible y no operar sin protección.

## 2) Umbrales y referencias (no certificación)
Cualquier umbral usado en el software es una referencia de ingeniería y debe verificarse en pruebas controladas.
Las referencias formales viven en `docs/referencias/`.

## 3) Reporte de vulnerabilidades (software)
Si alguien encuentra un fallo de seguridad (ej. exposición de datos, ejecución remota, etc.):
1) No lo publiques en issues.
2) Reporta por canal privado al equipo/coaches.
3) Registra el incidente en `docs/seguridad/` (sin datos sensibles).

## 4) Versiones soportadas
- Versión soportada para prototipo activo: `1.x`
- Versiones anteriores: no soportadas (solo histórico)

## 5) Alcance de esta política
Incluye:
- software en Raspberry Pi 5
- scripts de despliegue
- documentación de instalación

No incluye:
- certificaciones industriales
- protocolos oficiales de rescate