# ARGOS V1 — Sistema de Reconocimiento y Seguridad en Cuevas

ARGOS V1 es un prototipo tecnológico diseñado por **CALIBOTS KAIROS** para convertir la exploración subterránea en un proceso más **seguro, medible y trazable**.

El proyecto se basa en un principio simple:
**medir → decidir → alertar → registrar evidencia**.

## Qué hace ARGOS (en 30 segundos)
ARGOS operacionaliza la seguridad en 3 momentos:

- **Antes:** evaluación inicial del entorno (estado de riesgo y autodiagnóstico).
- **Durante:** monitoreo continuo + anti-colisión + telemetría + evidencia.
- **Después:** reporte final con logs y hallazgos para análisis y mejora.

## Por qué importa
En entornos tipo cueva o “espacio confinado” pueden existir riesgos que no se detectan a simple vista:
baja visibilidad, obstáculos y, especialmente, condiciones de aire peligrosas.

ARGOS V1 no busca “reemplazar” equipos certificados: busca crear una solución educativa, escalable y demostrable, que ayude a tomar decisiones con datos y a dejar evidencia.

## Estado del proyecto (hoy)
- Repositorio y documentación formal listos.
- Prototipo en ejecución sobre **Raspberry Pi 5**.
- Integraciones por completar/estabilizar: LoRa, sensores (lecturas estables), pipeline de visión, reporte final “one-click”.

## Hardware objetivo (V1)
- **Raspberry Pi 5** (plataforma principal)
- Cámara (Webcam USB o iPhone solo como soporte para demo)
- 4 motores (tracción) + driver
- Sensores: **BME280** (T/H), **MQ-135** (proxy aire), **VL53L0X** (ToF distancia)
- **LoRa 433 MHz** (telemetría crítica)
- Iluminación (linterna / LED)

> Nota: MQ-135 es un indicador cualitativo (proxy). No mide O2 y no es selectivo.

## Raspberry Pi 5: consideraciones técnicas mínimas
- Sistema recomendado: Raspberry Pi OS reciente (64-bit recomendado).
- Para estabilidad: fuente USB-C PD de 5A recomendada cuando se usan periféricos exigentes.
- Sensores por I2C requieren habilitar interfaz (raspi-config o GUI).
- Para cámara CSI, el stack recomendado es libcamera/Picamera2 (no “legacy camera stack”).

(Ver referencias oficiales en `docs/referencias/`.)

## Estructura del repositorio (estable)
- `docs/` Documentación oficial (tesis por capítulos, seguridad, plantillas, releases)
- `software/` Código en Raspberry Pi 5 (Python). El prototipo inicial vive en `software/legacy/`
- `hardware/` Cableado, BOM, mecánica, notas de montaje
- `assets/` Identidad visual y medios (logos, renders)
- `datasets/` Metadatos y guías de dataset (no subir crudos por defecto)
- `deploy/` Servicios y despliegue en Pi (systemd, notas de instalación)
- `tests/` Pruebas unitarias/integra (crece con el tiempo)

## Quick start (Raspberry Pi)
1) Ir a `software/`
2) Crear venv: `python3 -m venv .venv && source .venv/bin/activate`
3) Instalar deps: `pip install -r requirements.txt`
4) Config: `cp config/argos.example.yaml config/argos.yaml`
5) Ejecutar: `python -m argos_app --mode simulated`

Para modo hardware: `python -m argos_app --mode hardware`
(Primero completar los módulos de sensores/comms/vision.)

## Seguridad (leer antes de probar)
ARGOS V1 es un prototipo educativo. No usarlo para autorizar ingreso a cuevas reales.
Ver `SECURITY.md` y `docs/seguridad/`.

## Contacto
Proyecto desarrollado por CALIBOTS KAIROS (Colegio Comfandi El Prado, Cali).
Coaches/Mentores: Richard Suárez, Diego.