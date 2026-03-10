from __future__ import annotations
import os
from pathlib import Path
import yaml
from rich.console import Console

console = Console()

def load_config(config_path: str | None) -> dict:
    # Priority: explicit arg -> env -> default
    if config_path:
        path = Path(config_path)
    else:
        env = os.getenv("ARGOS_CONFIG")
        path = Path(env) if env else Path(__file__).resolve().parents[2] / "config" / "argos.yaml"
    if not path.exists():
        raise FileNotFoundError(f"Config not found: {path}")
    return yaml.safe_load(path.read_text(encoding="utf-8"))

def run(config_path: str | None, mode: str) -> None:
    cfg = load_config(config_path)
    console.rule(f"ARGOS V1 — mode={mode}")
    console.print(f"Project: {cfg.get('project', {}).get('name')} v{cfg.get('project', {}).get('version')}")
    console.print("This is a scaffold. Integrate sensors, LoRa and vision step-by-step.")
    console.print("Next: implement modules in sensors/, comms/, decision/, vision/.")
