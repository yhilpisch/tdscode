"""
The Data Scientist
Book 2 · Python Data Analysis, Visualization, and Storytelling
Chapter 02 · NumPy Vectorization

(c) Dr. Yves J. Hilpisch
AI-Powered by GPT 5.x
The Python Quants GmbH | https://tpq.io
https://thedatascientist.dev | https://linktr.ee/dyjh
"""

import numpy as np


def compare_loop_vs_vector(n: int = 1_000_000) -> dict[str, float]:
    x = np.random.rand(n)
    y = np.random.rand(n)
    vectorized = (x * y + x).sum()
    loop_sum = 0.0
    for a, b in zip(x, y):
        loop_sum += a * b + a
    return {"vectorized": float(vectorized), "loop": loop_sum}

if __name__ == "__main__":
    results = compare_loop_vs_vector(100_000)
    print(results)
