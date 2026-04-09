"""
The Data Scientist
Book 0 · Python Primer for Data Science
Chapter 02 · First Plot

(c) Dr. Yves J. Hilpisch
AI-Powered by GPT 5.x
The Python Quants GmbH | https://tpq.io
https://thedatascientist.dev | https://linktr.ee/dyjh
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

plt.style.use("seaborn-v0_8")


def save_sine_plot(path: Path = Path("figures/primer_sine.png")) -> Path:
    x = np.linspace(0.0, 2.0 * np.pi, 200)
    y = np.sin(x)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(6.0, 3.6))
    ax.plot(x, y, label="sin(x)", color="#0B3C78")
    ax.set_xlabel("x")
    ax.set_ylabel("sin(x)")
    ax.legend()
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return path

if __name__ == "__main__":
    out = save_sine_plot()
    print(f"Figure saved to {out.resolve()}")
