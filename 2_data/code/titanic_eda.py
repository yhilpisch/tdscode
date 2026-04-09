"""
The Data Scientist
Book 2 · Python Data Analysis, Visualization, and Storytelling
Chapter 05 · Titanic EDA Plots

(c) Dr. Yves J. Hilpisch
AI-Powered by GPT 5.x
The Python Quants GmbH | https://tpq.io
https://thedatascientist.dev | https://linktr.ee/dyjh
"""

from __future__ import annotations
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

plt.style.use("seaborn-v0_8")
CLEAN_PATH = Path("data") / "titanic_clean.csv"


def load_clean(path: Path = CLEAN_PATH) -> pd.DataFrame:
    return pd.read_csv(path)


def survival_by(df: pd.DataFrame, column: str, out_path: Path) -> Path:
    grouped = (
        df.groupby(column)["survived"].mean().rename("survival_rate").sort_values(ascending=False)
    )
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    grouped.plot(kind="bar", ax=ax, color="#0B3C78")
    ax.set_ylabel("Survival rate")
    ax.set_xlabel(column.title())
    ax.set_ylim(0, 1)
    fig.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return out_path


def main() -> None:
    df = load_clean()
    print(df.head())
    out1 = survival_by(df, "sex", Path("figures/titanic_survival_by_sex.png"))
    out2 = survival_by(df, "pclass", Path("figures/titanic_survival_by_pclass.png"))
    print("Saved:", out1.resolve())
    print("Saved:", out2.resolve())


if __name__ == "__main__":
    main()
