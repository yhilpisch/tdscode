"""
The Data Scientist
Book 3 · Statistics, Machine Learning, and Model Evaluation
Chapter 04 · Baseline Models

(c) Dr. Yves J. Hilpisch
AI-Powered by GPT 5.x
The Python Quants GmbH | https://tpq.io
https://thedatascientist.dev | https://linktr.ee/dyjh
"""

from __future__ import annotations
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression


def baseline_linear(df: pd.DataFrame, target: str) -> float:
    X = df.drop(columns=[target])
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    try:
        return float(mean_squared_error(y_test, preds, squared=False))
    except TypeError:
        # Older scikit-learn versions do not support the squared argument.
        return float(mean_squared_error(y_test, preds) ** 0.5)

if __name__ == "__main__":
    # small synthetic example
    import numpy as np
    rng = np.random.default_rng(0)
    df = pd.DataFrame({
        "feature": rng.normal(size=200),
    })
    df["target"] = 3 * df["feature"] + rng.normal(scale=0.5, size=200)
    rmse = baseline_linear(df, "target")
    print(f"Baseline linear RMSE: {rmse:.3f}")
