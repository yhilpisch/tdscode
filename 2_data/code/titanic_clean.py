"""
The Data Scientist
Book 2 · Python Data Analysis, Visualization, and Storytelling
Chapter 04 · Titanic Cleaning

(c) Dr. Yves J. Hilpisch
AI-Powered by GPT 5.x
The Python Quants GmbH | https://tpq.io
https://thedatascientist.dev | https://linktr.ee/dyjh
"""

from __future__ import annotations

from pathlib import Path
from urllib.request import urlretrieve

import pandas as pd

DATA_URL = "https://hilpisch.com/Titanic.csv"
RAW_PATH = Path("data") / "Titanic.csv"
CLEAN_PATH = Path("data") / "titanic_clean.csv"


def ensure_raw(path: Path = RAW_PATH) -> Path:
    if path.exists():
        return path
    path.parent.mkdir(parents=True, exist_ok=True)
    urlretrieve(DATA_URL, path)
    return path


def load_raw(path: Path = RAW_PATH) -> pd.DataFrame:
    return pd.read_csv(path)


def clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [c.strip().lower() for c in df.columns]
    df = df.rename(columns={"class": "pclass", "freq": "freq"})

    for col in ["pclass", "sex", "age", "survived"]:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()

    if "freq" in df.columns:
        df["freq"] = pd.to_numeric(df["freq"], errors="coerce").fillna(0).astype(int)
    if "survived" in df.columns:
        df["survived_flag"] = df["survived"].str.lower().map({"no": 0, "yes": 1})

    df = df.drop_duplicates()
    return df


def save_clean(df: pd.DataFrame, path: Path = CLEAN_PATH) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return path


def main() -> None:
    raw_path = ensure_raw()
    df_raw = load_raw(raw_path)
    df_clean = clean(df_raw)
    out_path = save_clean(df_clean)
    print(f"Raw rows: {len(df_raw):,} -> Clean rows: {len(df_clean):,}")
    print(f"Saved cleaned data to {out_path}")
    if {"pclass", "sex", "freq", "survived_flag"} <= set(df_clean.columns):
        survival = (
            df_clean.groupby(["pclass", "sex"])
            .apply(
                lambda g: (
                    g["survived_flag"].fillna(0).mul(g["freq"]).sum() / g["freq"].sum()
                    if g["freq"].sum()
                    else float("nan")
                )
            )
            .rename("survival_rate")
        )
        print(survival)


if __name__ == "__main__":
    main()
