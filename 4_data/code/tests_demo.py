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


def add(a: int, b: int) -> int:
    return a + b


def test_add():
    assert add(2, 3) == 5

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
