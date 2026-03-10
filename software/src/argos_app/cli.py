import argparse
from argos_app.runtime import run

def main():
    parser = argparse.ArgumentParser(prog="argos_app", description="ARGOS V1 runtime")
    parser.add_argument("--config", default=None, help="Path to config yaml (default: env ARGOS_CONFIG or software/config/argos.yaml)")
    parser.add_argument("--mode", default="simulated", choices=["simulated", "hardware"], help="Run mode")
    args = parser.parse_args()
    run(config_path=args.config, mode=args.mode)
    return 0
