"""
The Data Scientist
Book 3 · Statistics, Machine Learning, and Model Evaluation
Chapter 08 · Machine Learning Evaluation Report

(c) Dr. Yves J. Hilpisch
AI-Powered by GPT 5.x
The Python Quants GmbH | https://tpq.io
https://thedatascientist.dev | https://linktr.ee/dyjh
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


BOOK_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = BOOK_ROOT / "data" / "capstone_customers.csv"

ID_COLUMN = "customer_id"
TARGET_COLUMN = "churned"
NUMERIC_COLUMNS = [
    "tenure_months",
    "sessions_last_30d",
    "avg_session_minutes",
    "support_tickets_last_90d",
    "monthly_price",
]
CATEGORICAL_COLUMNS = ["country", "plan_type", "auto_renew"]
FEATURE_COLUMNS = NUMERIC_COLUMNS + CATEGORICAL_COLUMNS


def load_customers(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load the local customer churn dataset."""
    return pd.read_csv(path)


def split_customers(
    df: pd.DataFrame,
    random_state: int = 42,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.Series, pd.Series, pd.Series]:
    """Split the dataset into train, validation, and test slices."""
    features = df[FEATURE_COLUMNS]
    target = df[TARGET_COLUMN]

    X_train, X_temp, y_train, y_temp = train_test_split(
        features,
        target,
        test_size=0.40,
        random_state=random_state,
        stratify=target,
    )
    X_valid, X_test, y_valid, y_test = train_test_split(
        X_temp,
        y_temp,
        test_size=0.50,
        random_state=random_state,
        stratify=y_temp,
    )
    return X_train, X_valid, X_test, y_train, y_valid, y_test


def build_preprocessor() -> ColumnTransformer:
    """Build the shared feature preprocessing block."""
    return ColumnTransformer(
        [
            ("num", StandardScaler(), NUMERIC_COLUMNS),
            (
                "cat",
                OneHotEncoder(handle_unknown="ignore", sparse_output=False),
                CATEGORICAL_COLUMNS,
            ),
        ]
    )


def build_models(random_state: int = 42) -> dict[str, Pipeline]:
    """Build the two baseline models used in the capstone."""
    return {
        "logistic_regression": Pipeline(
            [
                ("pre", build_preprocessor()),
                ("model", LogisticRegression(max_iter=1000)),
            ]
        ),
        "random_forest": Pipeline(
            [
                ("pre", build_preprocessor()),
                (
                    "model",
                    RandomForestClassifier(
                        n_estimators=200,
                        random_state=random_state,
                        min_samples_leaf=2,
                    ),
                ),
            ]
        ),
    }


def evaluate_predictions(y_true: pd.Series, y_pred: pd.Series) -> dict[str, float]:
    """Return the headline classification metrics for one set of predictions."""
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred, zero_division=0),
        "recall": recall_score(y_true, y_pred, zero_division=0),
    }


def compare_models(df: pd.DataFrame, random_state: int = 42) -> pd.DataFrame:
    """Fit both baselines and compare their validation and test metrics."""
    X_train, X_valid, X_test, y_train, y_valid, y_test = split_customers(
        df,
        random_state=random_state,
    )

    rows: list[dict[str, float | str]] = []
    for name, model in build_models(random_state=random_state).items():
        model.fit(X_train, y_train)
        valid_scores = evaluate_predictions(y_valid, model.predict(X_valid))
        test_scores = evaluate_predictions(y_test, model.predict(X_test))
        rows.append({"model": name, "split": "validation", **valid_scores})
        rows.append({"model": name, "split": "test", **test_scores})

    return pd.DataFrame(rows)


def misclassified_customers(
    model: Pipeline,
    df: pd.DataFrame,
    random_state: int = 42,
) -> pd.DataFrame:
    """Return a small table of misclassified customers from the test set."""
    X_train, X_valid, X_test, y_train, y_valid, y_test = split_customers(
        df,
        random_state=random_state,
    )
    model.fit(pd.concat([X_train, X_valid]), pd.concat([y_train, y_valid]))

    predictions = model.predict(X_test)
    errors = X_test.copy()
    errors[ID_COLUMN] = df.loc[X_test.index, ID_COLUMN].values
    errors["actual"] = y_test.values
    errors["predicted"] = predictions
    errors["error_type"] = (
        errors["actual"].map({0: "active", 1: "churned"})
        + " vs "
        + errors["predicted"].map({0: "active", 1: "churned"})
    )
    return errors.loc[errors["actual"] != errors["predicted"], [ID_COLUMN, "actual", "predicted", "error_type"]]


def main() -> None:
    df = load_customers()
    comparison = compare_models(df)
    print(comparison)
    best_model = build_models()["logistic_regression"]
    print()
    print(misclassified_customers(best_model, df).head())


if __name__ == "__main__":
    main()
