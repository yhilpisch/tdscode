"""
The Data Scientist
Book 2 · Python Data Analysis, Visualization, and Storytelling
Chapter 04 · Cleaning Orders

(c) Dr. Yves J. Hilpisch
AI-Powered by GPT 5.x
The Python Quants GmbH | https://tpq.io
https://thedatascientist.dev | https://linktr.ee/dyjh
"""

import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/capstone_orders.csv")


def load_orders(path: Path = DATA_PATH) -> pd.DataFrame:
    return pd.read_csv(path)


def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()
    df["amount"] = df["amount"].astype(float)
    df["channel"] = df["channel"].str.strip().str.lower()
    return df

if __name__ == "__main__":
    if DATA_PATH.exists():
        orders = basic_clean(load_orders())
        print(orders.head())
    else:
        print("data/capstone_orders.csv not found; add the sample data to run this script.")
