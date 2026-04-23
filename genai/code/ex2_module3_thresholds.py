"""Exercise: threshold sweep helper."""

import importlib
import sys
from pathlib import Path

try:
    from code.module3_supervised import predict_threshold
except ImportError:
    # Allow direct script execution from the code/ directory.
    _CODE_DIR = Path(__file__).resolve().parent
    if str(_CODE_DIR) not in sys.path:
        sys.path.insert(0, str(_CODE_DIR))
    predict_threshold = importlib.import_module(
        "module3_supervised"
    ).predict_threshold


def sweep(probs, thresholds):
    return {t: predict_threshold(probs, t) for t in thresholds}
