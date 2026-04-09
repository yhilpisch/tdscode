"""
The Data Scientist
Book 4 · Software Engineering, Reproducibility, and Deployment Basics
Chapter 04 · Testing Demo

(c) Dr. Yves J. Hilpisch
AI-Powered by GPT 5.x
The Python Quants GmbH | https://tpq.io
https://thedatascientist.dev | https://linktr.ee/dyjh
"""

import pytest
from pathlib import Path
import sys


BOOK_ROOT = Path(__file__).resolve().parents[1]
if str(BOOK_ROOT) not in sys.path:
    sys.path.insert(0, str(BOOK_ROOT))


def is_binary_column(values) -> bool:
    observed = set(values)
    return observed <= {0, 1}


def test_is_binary_column_accepts_binary_values():
    assert is_binary_column([0, 1, 1, 0])


def test_is_binary_column_rejects_other_values():
    assert not is_binary_column([0, 1, 2])

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
