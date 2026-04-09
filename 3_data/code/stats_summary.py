"""
The Data Scientist
Book 3 · Statistics, Machine Learning, and Model Evaluation
Chapter 01 · Stats Summary

(c) Dr. Yves J. Hilpisch
AI-Powered by GPT 5.x
The Python Quants GmbH | https://tpq.io
https://thedatascientist.dev | https://linktr.ee/dyjh
"""

import numpy as np
import pandas as pd


def summary(series: pd.Series) -> pd.DataFrame:
    return pd.DataFrame({
        "mean": [series.mean()],
        "std": [series.std(ddof=1)],
        "min": [series.min()],
        "max": [series.max()],
    })

if __name__ == "__main__":
    data = pd.Series(np.random.normal(loc=0.0, scale=1.0, size=500))
    print(summary(data))
