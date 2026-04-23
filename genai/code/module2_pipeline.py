"""Module 2 pipeline scaffold."""

import importlib
import sys
from pathlib import Path

try:
    from code.module2_cleaning import clean_signups
except ImportError:
    # Allow direct script execution from the code/ directory.
    _CODE_DIR = Path(__file__).resolve().parent
    if str(_CODE_DIR) not in sys.path:
        sys.path.insert(0, str(_CODE_DIR))
    clean_signups = importlib.import_module("module2_cleaning").clean_signups


def run_pipeline():
    clean_signups("data/signups_raw.csv", "data/signups_clean.csv")
    return "ok"


if __name__ == "__main__":
    print(run_pipeline())
