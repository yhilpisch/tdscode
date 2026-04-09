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
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

DATA_URL = "https://hilpisch.com/Titanic.csv"
RAW_PATH = Path("../2_data/data") / "Titanic.csv"
CLEAN_PATH = Path("../2_data/data") / "titanic_clean.csv"


def ensure_clean() -> pd.DataFrame:
    if CLEAN_PATH.exists():
        return pd.read_csv(CLEAN_PATH)
    RAW_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not RAW_PATH.exists():
        urlretrieve(DATA_URL, RAW_PATH)
    df = pd.read_csv(RAW_PATH)
    df.columns = [c.strip().lower() for c in df.columns]
    for col in ["name", "sex", "ticket", "cabin", "embarked"]:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()
    df["fare"] = pd.to_numeric(df["fare"], errors="coerce")
    df["age"] = pd.to_numeric(df["age"], errors="coerce").fillna(df["age"].median())
    df["embarked"] = df["embarked"].replace({"": None, "nan": None}).fillna("?").str.upper()
    df["sex"] = df["sex"].str.lower()
    df = df.drop_duplicates()
    return df


def build_pipeline(numeric, categorical):
    pre = ColumnTransformer(
        [
            ("num", "passthrough", numeric),
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical),
        ]
    )
    model = LogisticRegression(max_iter=500)
    return Pipeline([("pre", pre), ("model", model)])


def train_and_report(df: pd.DataFrame) -> None:
    features = ["pclass", "sex", "age", "fare", "sibsp", "parch", "embarked"]
    target = "survived"
    df = df.dropna(subset=[target])
    X = df[features]
    y = df[target]
    numeric = ["age", "fare", "sibsp", "parch"]
    categorical = ["pclass", "sex", "embarked"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    pipe = build_pipeline(numeric, categorical)
    pipe.fit(X_train, y_train)
    preds = pipe.predict(X_test)
    print(confusion_matrix(y_test, preds))
    print(classification_report(y_test, preds, digits=3))


def main() -> None:
    df = ensure_clean()
    train_and_report(df)


if __name__ == "__main__":
    main()
