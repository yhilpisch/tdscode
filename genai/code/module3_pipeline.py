"""Module 3 pipeline scaffold."""

import importlib
import sys
from pathlib import Path

try:
    from code.ex1_module3_baseline import accuracy
except ImportError:
    # Allow direct script execution from the code/ directory.
    _CODE_DIR = Path(__file__).resolve().parent
    if str(_CODE_DIR) not in sys.path:
        sys.path.insert(0, str(_CODE_DIR))
    accuracy = importlib.import_module("ex1_module3_baseline").accuracy


def evaluate_demo():
    return accuracy([1, 0, 1], [1, 1, 1])


if __name__ == "__main__":
    print(evaluate_demo())
