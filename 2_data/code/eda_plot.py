"""
The Data Scientist
Book 2 · Python Data Analysis, Visualization, and Storytelling
Chapter 05 · EDA Plot

(c) Dr. Yves J. Hilpisch
AI-Powered by GPT 5.x
The Python Quants GmbH | https://tpq.io
https://thedatascientist.dev | https://linktr.ee/dyjh
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

plt.style.use("seaborn-v0_8")


def plot_hist(csv_path: Path, column: str, out_path: Path) -> Path:
    df = pd.read_csv(csv_path)
    fig, ax = plt.subplots(figsize=(6.0, 3.6))
    ax.hist(df[column], bins=20, color="#0B3C78", alpha=0.8)
    ax.set_title(f"Distribution of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Count")
    fig.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return out_path

if __name__ == "__main__":
    sample = Path("data/capstone_orders.csv")
    if sample.exists():
        out = plot_hist(sample, "amount", Path("figures/eda_amount_hist.png"))
        print(out.resolve())
    else:
        print("Add data/capstone_orders.csv to run this plot.")
