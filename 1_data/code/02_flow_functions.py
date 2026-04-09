"""
The Data Scientist
Book 1 · Python Programming Foundations for Data Science
Chapter 03 · Flow and Functions

(c) Dr. Yves J. Hilpisch
AI-Powered by GPT 5.x
The Python Quants GmbH | https://tpq.io
https://thedatascientist.dev | https://linktr.ee/dyjh
"""

from __future__ import annotations
from typing import Iterable


def count_long_words(words: Iterable[str], min_len: int = 5) -> int:
    return sum(1 for w in words if len(w) >= min_len)


def fizzbuzz(n: int = 20) -> list[str]:
    out = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            out.append("fizzbuzz")
        elif i % 3 == 0:
            out.append("fizz")
        elif i % 5 == 0:
            out.append("buzz")
        else:
            out.append(str(i))
    return out

if __name__ == "__main__":
    words = ["python", "data", "analysis", "ai"]
    print("long words >=5:", count_long_words(words))
    print(fizzbuzz(16))
