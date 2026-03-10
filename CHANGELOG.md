# Changelog

Todos los cambios relevantes del proyecto se documentan aquí.

Formato basado en **Keep a Changelog** y versionado **SemVer**.
- Keep a Changelog: https://keepachangelog.com/en/1.1.0/
- SemVer: https://semver.org/spec/v2.0.0.html

## [Unreleased]
### Added
- (pendiente) Integración real LoRa 433 MHz (telemetría crítica) con pruebas RSSI/SNR.
- (pendiente) Lecturas estables de BME280 + VL53L0X + pipeline de logs unificado.
- (pendiente) Pipeline de cámara + evidencia (capturas por evento).
- (pendiente) Script de “Reporte de sesión” (resumen automático).

### Changed
- (pendiente) Migración del prototipo único a módulos (`sensors/`, `comms/`, `vision/`, `decision/`).

### Fixed
- (pendiente) Robustez de arranque y recuperación ante fallos de sensores.

## [1.0.0] - 2026-03-10
### Added
- Estructura estable del repositorio (docs/software/hardware/assets/deploy/tests/datasets).
- Documentación formal del proyecto (capítulos 1–5) y manual del equipo.
- Plantillas operativas: cronograma, plan de pruebas, bitácora, checklist, BOM.
- Política inicial de seguridad (SECURITY.md) y archivos de comunidad (CONTRIBUTING, CODE_OF_CONDUCT).

### Notes
- Esta versión marca el **baseline** del proyecto: repositorio, documentación y base de ejecución en Raspberry Pi 5.
- La funcionalidad completa del prototipo (telemetría, sensores, visión) está en progreso y se registrará en `Unreleased`.