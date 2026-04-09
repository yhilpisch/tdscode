"""
The Data Scientist
Book 1 · Python Programming Foundations for Data Science
Chapter 01 · Core Types Demo

(c) Dr. Yves J. Hilpisch
AI-Powered by GPT 5.x
The Python Quants GmbH | https://tpq.io
https://thedatascientist.dev | https://linktr.ee/dyjh
"""

from __future__ import annotations

def demo() -> dict[str, object]:
    price = 19.5
    name = "Ada"
    scores = [88, 92, 95]
    avg = sum(scores) / len(scores)
    mapping = {"name": name, "price": price, "avg": avg}
    return mapping

if __name__ == "__main__":
    print(demo())
