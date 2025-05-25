# src/utils.py
import yaml
import os

def load_keys(path="config/keys.yaml"):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)