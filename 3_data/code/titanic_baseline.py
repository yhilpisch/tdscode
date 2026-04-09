"""
The Data Scientist
Book 3 · Statistics, Machine Learning, and Model Evaluation
Chapter 04 · Titanic Baseline Model

(c) Dr. Yves J. Hilpisch
AI-Powered by GPT 5.x
The Python Quants GmbH | https://tpq.io
https://thedatascientist.dev | https://linktr.ee/dyjh
"""

from __future__ import annotations

from pathlib import Path
from urllib.request import urlretrieve

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


BOOK_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = BOOK_ROOT / "data"
RAW_PATH = DATA_DIR / "Titanic.csv"
DATA_URL = "https://hilpisch.com/Titanic.csv"

TARGET_COLUMN = "survived"
WEIGHT_COLUMN = "freq"
FEATURE_COLUMNS = ["passenger_class", "sex", "age"]
CATEGORICAL_COLUMNS = FEATURE_COLUMNS


def load_titanic_table() -> pd.DataFrame:
    """Load the local aggregated Titanic table.

    The companion book ships the compact frequency table instead of the full
    passenger list. That keeps the data small and makes the weighting logic
    visible. If the local file is missing, the script falls back to the public
    source used in the book.
    """
    if not RAW_PATH.exists():
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        urlretrieve(DATA_URL, RAW_PATH)

    df = pd.read_csv(RAW_PATH)
    df = df.loc[:, ~df.columns.astype(str).str.contains("^unnamed", case=False)]
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    if "class" in df.columns:
        df = df.rename(columns={"class": "passenger_class"})

    for column in ["passenger_class", "sex", "age", "survived"]:
        df[column] = df[column].astype(str).str.strip()

    df["passenger_class"] = df["passenger_class"].str.lower()
    df["sex"] = df["sex"].str.lower()
    df["age"] = df["age"].str.lower()
    df["survived"] = df["survived"].str.lower().map({"yes": 1, "no": 0})
    df["freq"] = pd.to_numeric(df["freq"], errors="coerce").fillna(0).astype(int)

    return df[FEATURE_COLUMNS + [TARGET_COLUMN, WEIGHT_COLUMN]].copy()


def build_pipeline() -> Pipeline:
    """Build the preprocessing and logistic-regression baseline."""
    preprocessor = ColumnTransformer(
        [
            (
                "cat",
                OneHotEncoder(handle_unknown="ignore"),
                CATEGORICAL_COLUMNS,
            ),
        ]
    )
    model = LogisticRegression(max_iter=500)
    return Pipeline([("pre", preprocessor), ("model", model)])


def train_and_report(df: pd.DataFrame) -> None:
    """Train the baseline and print a weighted evaluation report."""
    X = df[FEATURE_COLUMNS]
    y = df[TARGET_COLUMN]
    weights = df[WEIGHT_COLUMN]

    X_train, X_test, y_train, y_test, w_train, w_test = train_test_split(
        X,
        y,
        weights,
        test_size=0.25,
        random_state=42,
        stratify=y,
    )

    pipe = build_pipeline()
    pipe.fit(X_train, y_train, model__sample_weight=w_train)
    preds = pipe.predict(X_test)

    print(f"Accuracy: {accuracy_score(y_test, preds, sample_weight=w_test):.3f}")
    print(confusion_matrix(y_test, preds, sample_weight=w_test))
    print(classification_report(y_test, preds, sample_weight=w_test, digits=3))


def main() -> None:
    df = load_titanic_table()
    train_and_report(df)


if __name__ == "__main__":
    main()
